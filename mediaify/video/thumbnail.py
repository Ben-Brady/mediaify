from ..configs import (
    ThumbnailConfig,
)
from ..files import ImageFile
from ..image import encode_image
from .info import VideoInfo
from ffmpeg import FFmpeg, FFmpegError


def encode_as_thumbnail(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: ThumbnailConfig,
        ) -> ImageFile:
    offset = float(info.duration * config.offset)
    offset = min(offset, info.duration)

    try:
        data = FFmpeg(
            ).input(pathname
            ).output(
                "pipe:",
                f='image2',
                vframes=1,
                ss=offset,
            ).execute()
    except FFmpegError as e:
        raise ValueError(str(e))

    return encode_image(data, config)
