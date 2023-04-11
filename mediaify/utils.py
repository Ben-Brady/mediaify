from . import encoders, presets, MediaFile, ImageFile
from .configs import ImageConfig, AnimationConfig, VideoConfig
from .encoders.utils import is_animated_sequence, guess_mimetype
from PIL import Image as PILImage
from magic import Magic
from typing import Sequence
from typing_extensions import Literal
import io


def encode_media(
        data: bytes,
        image_configs: "None|list[ImageConfig]" = presets.Default.image,
        animation_configs: "None|list[AnimationConfig]" = presets.Default.animation,
        video_configs: "None|list[VideoConfig]" = presets.Default.video,
    ) -> "Sequence[MediaFile]":
    type = guess_type(data)

    if type == 'image':
        if image_configs is None:
            raise ValueError("Image encoding disabled")
        else:
            return encoders.encode_image(data, image_configs)
    elif type == 'animation':
        if animation_configs is None:
            raise ValueError("Animation encoding disabled")
        else:
            return encoders.encode_animation(data, animation_configs)
    elif type == 'video':
        if video_configs is None:
            raise ValueError("Video encoding disabled")
        else:
            return encoders.encode_video(data, video_configs)
    else:
        raise ValueError("Filetype not supported")


def guess_type(data: bytes) -> "Literal['image', 'video', 'animation']|None":
    """Raises:
    - ValueError: Filetype not supported
    """
    mime = guess_mimetype(data)
    type, subtype = mime.split('/')

    if subtype in {"webp", "gif", "apng"}:
        if is_animated_sequence(data):
            return "animation"
        else:
            return "image"
    elif type == 'image':
        return "image"
    elif type == 'video':
        return "video"
    else:
        return None


__all__ = [
    "encode_media",
    "guess_type",
    "is_animated_sequence",
    "guess_mimetype",
]
