from .files import (
    GenericMediaFile,
    AnimationFile,
    ImageFile,
    VideoFile,
)
from .configs import (
    WEBPImageEncodeConfig,
    GIFEncodeConfig,
    WEBPAnimationEncodeConfig,
    UnencodedConfig,
    ThumbnailConfig,
    AnimationSummaryConfig,

    AnimationConfig,
    ImageConfig,
    VideoConfig,
)
from . import presets
from .image import (
    load_image,
    encode_image,
    batch_encode_image,
)
from .animation import (
    load_animation,
    encode_animation,
    batch_encode_animation,
)
from .video import (
    load_video,
    encode_video,
    batch_encode_video,
)
from .media import (
    guess_type,
    load_media,
    encode_media,
    batch_encode_media,
)

__all__ = [
    "presets",
    "configs",

    "guess_type",
    "load_media",
    "encode_media",
    "batch_encode_media",

    "load_image",
    "encode_image",
    "batch_encode_image",

    "load_animation",
    "encode_animation",
    "batch_encode_video",

    "load_video",
    "encode_video",
    "batch_encode_animation",

    "GenericMediaFile",
    "AnimationFile",
    "ImageFile",
    "VideoFile",

    "WEBPImageEncodeConfig",
    "GIFEncodeConfig",
    "WEBPAnimationEncodeConfig",
    "UnencodedConfig",
    "ThumbnailConfig",
    "AnimationSummaryConfig",

    "AnimationConfig",
    "ImageConfig",
    "VideoConfig",
]
