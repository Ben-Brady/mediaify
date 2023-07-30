from ..configs import (
    ThumbnailEncoding,
)
from ..files import ImageFile
from ..image import encode_image
from .info import VideoInfo
from .process import resize_video
from ffmpeg import FFmpeg, FFmpegError  # type: ignore


def encode_as_thumbnail(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: ThumbnailEncoding,
        ) -> ImageFile:
    offset = float(info.duration * config.offset)
    offset = min(offset, info.duration)

    ffmpeg = (
        FFmpeg()
        .option("i", pathname)
        .option("f", "webp")
        .option("vframes", 1)
        .option("ss", offset)
    )

    if config.encoding and config.encoding.resize:
        ffmpeg = resize_video(ffmpeg, info, config.encoding.resize)

    try:
        data = (
            ffmpeg
            .output("pipe:")
            .execute()
        )
    except FFmpegError as e:
        raise ValueError(str(e))
    else:
        return encode_image(data, config)
