from .utils import guess_type
from . import configs
from .image import (
    load_image,
    encode_image,
    batch_encode_image,
    ImageFile,
)
from .animation import (
    load_animation,
    encode_animation,
    batch_encode_animation,
    AnimationFile,
)
from .video import (
    load_video,
    encode_video,
    batch_encode_video,
    VideoFile,
)

__all__ = [
    "configs",

    "load_image",
    "encode_image",
    "batch_encode_image",
    "ImageFile",

    "load_animation",
    "encode_animation",
    "batch_encode_animation",
    "AnimationFile",

    "load_video",
    "encode_video",
    "batch_encode_video",
    "VideoFile",
]
