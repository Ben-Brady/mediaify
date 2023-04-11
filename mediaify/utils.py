from . import configs, encoders, presets, GenericFile
from .encoders import probe
from typing_extensions import Literal


def encode_media(
        data: bytes,
        image_configs: "list[configs.ImageConfig]" = presets.Default.image,
        animation_configs: """list[
            configs.AnimationConfig|
            configs.ThumbnailConfig|
            configs.VideoConfig
        ]""" = presets.Default.animation,
    ) -> "list[GenericFile]":
    type = guess_type(data)

    if type == 'image':
        return encoders.encode_image(data, image_configs)
    elif type == 'animation':
        return encoders.encode_animation(data, animation_configs)
    elif type == 'video':
        raise NotADirectoryError("Video files are not supported yet")
    else:
        raise ValueError("Filetype not supported")


def guess_type(data: bytes) -> "Literal['image', 'video', 'animation']|None":
    """Raises:
    - ValueError: Filetype not supported
    """
    mime = probe.guess_mimetype(data)
    type, subtype = mime.split('/')

    if subtype in {"webp", "gif", "apng"}:
        if probe.is_animated_sequence(data):
            return "animation"
        else:
            return "image"
    elif type == 'image':
        return "image"
    elif type == 'video':
        return "video"
    else:
        return None
