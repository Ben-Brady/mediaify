from ..files import AnimationFile, ImageFile
from ..configs import AnimationEncodingType, ThumbnailEncoding, AnimationFormat, UnencodedEncoding
from .encode import open_as_pillow, encode_with_config, encode_as_original
from typing import List, overload


@overload
def encode_animation(
        data: bytes,
        config: "ThumbnailEncoding",
        ) -> "ImageFile":
    ...


@overload
def encode_animation(
        data: bytes,
        config: "AnimationFormat|UnencodedEncoding|None",
        ) -> "AnimationFile":
    ...


def encode_animation(
        data: bytes,
        config: "AnimationEncodingType|None" = None,
        ) -> "AnimationFile|ImageFile":
    """Encodes an animation using an animation config

    Returns:
        AnimationFile|ImageFile: The encoded output

    Raises:
        ValueError: Animation was too large
        ValueError: Could not Load Animation
    """
    pillow = open_as_pillow(data)
    return encode_with_config(data, pillow, config)


def batch_encode_animation(
        data: bytes,
        configs: "List[AnimationEncodingType]",
        ) -> "List[AnimationFile|ImageFile]":
    """
    Encodes an animation using a list of animation configs,
    more efficent than calling `encode_animation` multiple times

    Returns:
        List[AnimationFile|ImageFile]: List of encoded output, guarenteed to be in the same order as the configs

    Raises:
        ValueError: Animation is too big to process
        ValueError: Could not Load Image
    """
    pillow = open_as_pillow(data)
    return [encode_with_config(data, pillow, config) for config in configs]

