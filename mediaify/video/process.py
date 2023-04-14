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
import ffmpeg  # type: ignore


def encode_generic_video(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: "WEBMEncodeConfig | MP4EncodeConfig",
        save_functon: "Callable[[ffmpeg.Stream, str], None]",
        ):
    try:
        stream = ffmpeg.input(pathname)
        stream = preprocess(stream, info, config.resize, config.framerate)

        with NamedTemporaryFile(suffix=".mp4") as f:
            stream = save_functon(stream, f.name)
            output_info = get_video_info(f.name)
            data = f.read()
    except ffmpeg.Error as e:
        raise ValueError(e.stderr.decode())


    return VideoFile(
        data=data,
        mimetype=output_info.mimetype,
        height=output_info.height,
        width=output_info.width,
        framerate=output_info.framerate,
        duration=output_info.duration,
        hasAudio=output_info.hasAudio,
    )


def preprocess(
        stream: ffmpeg.Stream,
        info: VideoInfo,
        resize: "ResizeConfig|None",
        framerate: "float|None",
        ) -> ffmpeg.Stream:
    if resize:
        size = (info.width, info.height)
        size = calculate_downscale(size, resize)
        stream = ffmpeg.filter(
            stream,
            "scale",
            *size,
            flags="lanczos"
        )

    if framerate:
        stream = ffmpeg.filter(
            stream,
            "fps",
            fps=framerate
        )

    return stream

