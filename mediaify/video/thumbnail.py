from ..configs import (
    ThumbnailConfig,
)
from ..files import ImageFile
from ..image import encode_image
from .info import VideoInfo
import ffmpeg  # type: ignore


def encode_as_thumbnail(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: ThumbnailConfig,
        ) -> ImageFile:
    offset = float(info.duration * config.offset)
    if offset > info.duration:
        offset = info.duration

    try:
        data, _ = (
            ffmpeg
            .input(pathname)
            .output(
                "pipe:",
                f='image2',
                vframes=1,
                ss=offset,
            )
            .run(
                input=data,
                capture_stdout=True,
                capture_stderr=True
            )
        )
    except ffmpeg.Error as e:
        raise ValueError(e.stderr.decode())

    return encode_image(data, config)
