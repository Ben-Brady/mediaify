from .ffmpeg import assert_ffmpeg_installed
from ..files import VideoFile
import mimetypes
from typing import Any
from typing import Dict
from dataclasses import dataclass
from magic import Magic
import numexpr  # type: ignore
import ffmpeg  # type: ignore


@dataclass
class VideoInfo:
    height: int
    width: int
    framerate: int
    mimetype: str
    extention: str
    hasAudio: bool
    duration: float
    frame_count: "int|None"


def get_video_info(filepath: str) -> VideoInfo:
    assert_ffmpeg_installed()
    probe_data = ffmpeg.probe(filepath)
    video_stream = _get_video_stream(probe_data)

    width = int(video_stream['width'])
    height = int(video_stream['height'])

    framerate = numexpr.evaluate(video_stream['r_frame_rate'])[()]
    framerate = int(framerate)

    duration = float(probe_data['format']['duration'])

    if 'nb_frames' in video_stream:
        frame_count = int(video_stream['nb_frames'])
    else:
        frame_count = int(duration * framerate)

    magic = Magic(mime=True)
    mimetype = magic.from_file(filepath)

    extention = mimetypes.guess_extension(mimetype)
    if extention is None:
        raise Exception("Couldn't Guess File Extention")

    audio_streams = [
        stream for stream in probe_data['streams']
        if stream['codec_type'] == 'audio'
    ]
    hasAudio = len(audio_streams) > 0

    return VideoInfo(
        width=width,
        height=height,
        mimetype=mimetype,
        extention=extention,
        framerate=framerate,
        hasAudio=hasAudio,
        frame_count=frame_count,
        duration=duration,
    )


def _get_video_stream(probe_data: Dict[str, Any]) -> "Dict[str, Any]":
    video_streams = [
        x for x in probe_data['streams']
        if x['codec_type'] == 'video'
    ]
    if len(video_streams) == 0:
        raise Exception('No Video Streams Found')

    return video_streams[0]  # type: ignore
