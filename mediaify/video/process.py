from ..configs import (
    WEBMFormat,
    MP4Format,
    ResizeConfig,
    VideoEncodingType
)
from ..files import VideoFile
from ..resize import calculate_downscale
from .info import VideoInfo, get_video_info
from tempfile import NamedTemporaryFile
from typing import Callable
from ffmpeg import FFmpeg, FFmpegError, Progress  # type: ignore
from tqdm import tqdm  # type: ignore


def encode_generic_video(
        pathname: str,
        info: VideoInfo,
        *,
        encoding_name: "str" = "Unknown",
        resize_config: "ResizeConfig|None" = None,
        framerate: "float|None" = None,
        process_func: "Callable[[FFmpeg], FFmpeg]|None" = None,
        ) -> VideoFile:
    try:
        ffmpeg = FFmpeg().option("i", pathname)

        if framerate is not None:
            ffmpeg = change_framerate(ffmpeg, framerate)
        if resize_config is not None:
            ffmpeg = resize_video(ffmpeg, info, resize_config)
        if process_func is not None:
            ffmpeg = process_func(ffmpeg)

        with NamedTemporaryFile() as f:
            ffmpeg.option("y")
            ffmpeg.output(f.name)
            ffmpeg.execute()
            output_info = get_video_info(f.name)
            data = f.read()
    except FFmpegError as e:
        raise ValueError(f"FFmpeg Error: {e}")

    return VideoFile(
        data=data,
        mimetype=output_info.mimetype,
        height=output_info.height,
        width=output_info.width,
        framerate=output_info.framerate,
        duration=output_info.duration,
        hasAudio=output_info.hasAudio,
    )


def resize_video(
        ffmpeg: FFmpeg,
        info: VideoInfo,
        resize: "ResizeConfig|None"
        ) -> FFmpeg:
    if resize is None:
        return ffmpeg

    size = (info.width, info.height)
    width, height = calculate_downscale(size, resize)
    return (
        ffmpeg
        .option("vf", f"scale={width}:{height}",)
        .option("sws_flags", "lanczos",)
    )


def change_framerate(ffmpeg: FFmpeg, framerate: "float|None") -> FFmpeg:
    if framerate is None:
        return ffmpeg
    else:
        return (
            ffmpeg.option("filter:v", f"fps={framerate}")
        )
