from ..files import VideoFile, AnimationFile, ImageFile
from ..configs import (
    VideoConfig,
    UnencodedConfig,
    ThumbnailConfig,
    AnimationSummaryConfig,
)
from .info import VideoInfo
from .summary import encode_as_animation_summary
from .thumbnail import encode_as_thumbnail


def encode_video_with_config(
        data: bytes,
        path: str,
        info: VideoInfo,
        config: "VideoConfig"
        ) -> "VideoFile|AnimationFile|ImageFile":
    if isinstance(config, UnencodedConfig):
        return encode_as_original(data, info)
    elif isinstance(config, ThumbnailConfig):
        return encode_as_thumbnail(data, path, info, config)
    elif isinstance(config, AnimationSummaryConfig):
        return encode_as_animation_summary(data, path, info, config)
    else:
        raise ValueError("Invalid encoding config")


def encode_as_original(data: bytes, info: VideoInfo) -> VideoFile:
    return VideoFile(
        data=data,
        mimetype=info.mimetype,
        height=info.height,
        width=info.width,
        duration=info.duration,
        framerate=info.framerate,
        hasAudio=info.audio,
    )
