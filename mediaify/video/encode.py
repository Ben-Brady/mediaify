from ..files import VideoFile, AnimationFile, ImageFile
from ..configs import (
    VideoEncodingType,
    UnencodedEncoding,
    ThumbnailEncoding,
    WEBMFormat,
    MP4Format,
    VideoPreviewAnimationEncoding,
)
from .info import VideoInfo
from .formats import encode_as_original, encode_as_mp4, encode_as_webm
from .summary import encode_as_animation_summary
from .thumbnail import encode_as_thumbnail
import shutil


def encode_video_with_config(
        data: bytes,
        path: str,
        info: VideoInfo,
        config: "VideoEncodingType|None"
        ) -> "VideoFile|AnimationFile|ImageFile":
    if isinstance(config, UnencodedEncoding) or config is None:
        return encode_as_original(data, info)
    elif isinstance(config, WEBMFormat):
        return encode_as_webm(data, path, info, config)
    elif isinstance(config, MP4Format):
        return encode_as_mp4(data, path, info, config)
    elif isinstance(config, ThumbnailEncoding):
        return encode_as_thumbnail(data, path, info, config)
    elif isinstance(config, VideoPreviewAnimationEncoding):
        return encode_as_animation_summary(data, path, info, config)
    else:
        raise ValueError("Invalid encoding config")
