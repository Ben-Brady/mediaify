import mimetypes
from typing import Any
from dataclasses import dataclass
from magic import Magic
import shutil
import numexpr  # type: ignore
from MediaInfo import MediaInfo  # type: ignore


@dataclass
class VideoInfo:
    height: int
    width: int
    framerate: float
    mimetype: str
    extention: str
    hasAudio: bool
    duration: float
    frame_count: int


def get_video_info(filepath: str) -> VideoInfo:
    info: dict[str, Any] = MediaInfo(filename=filepath).getInfo()

    width = int(info['videoWidth'])
    height = int(info['videoHeight'])
    framerate = numexpr.evaluate(info['videoFrameRate'])[()]
    frame_count = int(info['videoFrameCount'])
    if info['videoDuration'] is not None:
        duration = float(info['videoDuration'])
    else:
        duration = framerate * frame_count

    hasAudio = info["haveAudio"] == 1

    magic = Magic(mime=True)
    mimetype = magic.from_file(filepath)

    extention = mimetypes.guess_extension(mimetype)
    if extention is None:
        raise Exception("Couldn't Guess File Extention")

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
