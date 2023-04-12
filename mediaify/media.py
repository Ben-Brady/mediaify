from . import image, animation, video
from .presets import Default
from .configs import ImageConfig, AnimationConfig, VideoConfig
from .files import MediaFile
from .utils import is_animated_sequence, guess_mimetype
from typing import List
from typing_extensions import Literal


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


def load_media(data: bytes) -> MediaFile:
    type = guess_type(data)

    if type == 'image':
        return image.load_image(data)
    elif type == 'animation':
        return animation.load_animation(data)
    elif type == 'video':
        return video.load_video(data)
    else:
        raise ValueError("Filetype not supported")


def encode_media(
        data: bytes,
        image_config: ImageConfig = Default.image,
        animation_config: AnimationConfig = Default.animation,
        video_config: VideoConfig = Default.video,
        ) -> MediaFile:
    type = guess_type(data)

    if type == 'image':
        return image.encode_image(data, image_config)
    elif type == 'animation':
        return animation.encode_animation(data, animation_config)
    elif type == 'video':
        return video.encode_video(data, video_config)
    else:
        raise ValueError("Filetype not supported")


def batch_encode_media(
        data: bytes,
        image_configs: "List[ImageConfig]" = Default.batch_image,
        animation_configs: "List[AnimationConfig]" = Default.batch_animation,
        video_configs: "List[VideoConfig]" = Default.batch_video,
        ) -> "List[MediaFile]":
    type = guess_type(data)

    if type == 'image':
        return list(image.batch_encode_image(data, image_configs))
    elif type == 'animation':
        return list(animation.batch_encode_animation(data, animation_configs))
    elif type == 'video':
        return list(video.batch_encode_video(data, video_configs))
    else:
        raise ValueError("Filetype not supported")



__all__ = [
    "guess_type",
    "guess_mimetype",
    "encode_media",
    "batch_encode_media",
]
