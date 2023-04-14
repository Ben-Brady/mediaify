from ..configs import (
    MP4EncodeConfig,
    WEBMEncodeConfig,
)
from ..files import VideoFile
from .process import encode_as_generic
from .info import VideoInfo
import ffmpeg  # type: ignore


def encode_as_mp4(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: MP4EncodeConfig,
        ) -> VideoFile:
    def save(stream: ffmpeg.Stream, filepath: str):
        (ffmpeg
            .output(
                stream,
                filepath,
                f='mp4',
            )
            .overwrite_output()
            .run(capture_stderr=True)
        )

    return encode_as_generic(data, pathname, info, config, save)


def encode_as_webm(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: WEBMEncodeConfig,
        ) -> VideoFile:
    def save(stream: ffmpeg.Stream, filepath: str):
        (ffmpeg
            .output(
                stream,
                filepath,
                f='webm',
            )
            .overwrite_output()
            .run(capture_stderr=True)
        )

    return encode_as_generic(data, pathname, info, config, save)
