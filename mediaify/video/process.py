from ..configs import (
    WEBMEncodeConfig,
    MP4EncodeConfig,
    ResizeConfig,
)
from ..files import VideoFile
from ..resize import calculate_downscale
from .info import VideoInfo, get_video_info
from tempfile import NamedTemporaryFile
from typing import Callable
from ffmpeg import FFmpeg, FFmpegError, Progress


def encode_generic_video(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: "WEBMEncodeConfig | MP4EncodeConfig",
        save_functon: "Callable[[FFmpeg, str], None]",
        ):
    try:
        ffmpeg = FFmpeg().input(pathname)
        # Fails to encode
        # ffmpeg = change_framerate(ffmpeg, config.framerate)
        # ffmpeg = resize(ffmpeg, info, config.resize)

        with NamedTemporaryFile(suffix=".mp4") as f:
            ffmpeg = ffmpeg.option("y") # overwrite output file
            save_functon(ffmpeg, f.name)
            output_info = get_video_info(f.name)
            data = f.read()
    except FFmpegError as e:
        raise ValueError("FFmpeg Error", e)
    else:
        return VideoFile(
            data=data,
            mimetype=output_info.mimetype,
            height=output_info.height,
            width=output_info.width,
            framerate=output_info.framerate,
            duration=output_info.duration,
            hasAudio=output_info.hasAudio,
        )


def resize(
        ffmpeg: FFmpeg,
        info: VideoInfo,
        resize: "ResizeConfig|None"
        ) -> FFmpeg:
    if resize is None:
        return ffmpeg
    else:
        size = (info.width, info.height)
        width, height = calculate_downscale(size, resize)
        return (ffmpeg
            .option("vf", f"scale={width}x{height}:flags=lanczos",)
            .option("ws_flags", "billinear",)
        )

def change_framerate(ffmpeg: FFmpeg, framerate: "float|None") -> FFmpeg:
    if framerate is None:
        return ffmpeg
    else:
        return (
            ffmpeg.option("filter:v", f"fps={framerate}")
        )

