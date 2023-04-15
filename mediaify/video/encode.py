from ..files import VideoFile, AnimationFile, ImageFile
from ..configs import (
    VideoConfig,
    UnencodedConfig,
    ThumbnailConfig,
    WEBMEncodeConfig,
    MP4EncodeConfig,
    AnimationSummaryConfig,
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
        config: "VideoConfig"
        ) -> "VideoFile|AnimationFile|ImageFile":
    if not shutil.which("ffprobe"):
        raise RuntimeError("ffprobe is not installed")

    if isinstance(config, UnencodedConfig):
        return encode_as_original(data, info)
    elif isinstance(config, WEBMEncodeConfig):
        return encode_as_webm(data, path, info, config)
    elif isinstance(config, MP4EncodeConfig):
        return encode_as_mp4(data, path, info, config)
    elif isinstance(config, ThumbnailConfig):
        return encode_as_thumbnail(data, path, info, config)
    elif isinstance(config, AnimationSummaryConfig):
        return encode_as_animation_summary(data, path, info, config)
    else:
        raise ValueError("Invalid encoding config")
