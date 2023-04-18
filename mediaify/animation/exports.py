from ..files import AnimationFile, ImageFile
from ..configs import AnimationConfig
from ..presets import Default
from .encode import open_as_pillow, encode_with_config, encode_as_original
from typing import List


def load_animation(data: bytes) -> "AnimationFile":
    """
    Loads an animation without any processing,
    identical to `encode_animation(data, UnencodedConfig())`

    Returns:
        AnimationFile: The loaded animation

    Raises:
        ValueError: Animation was too large
        ValueError: Could not Load Animation
    """
    pillow = open_as_pillow(data)
    return encode_as_original(data, pillow)


def encode_animation(
        data: bytes,
        config: "AnimationConfig|None" = None,
        ) -> "AnimationFile|ImageFile":
    """Encodes an animation using an AnimationConfig

    Returns:
        AnimationFile|ImageFile: The encoded output

    Raises:
        ValueError: Animation was too large
        ValueError: Could not Load Animation
    """
    config = config or Default.animation
    pillow = open_as_pillow(data)
    return encode_with_config(data, pillow, config)


def batch_encode_animation(
        data: bytes,
        configs: "List[AnimationConfig]|None" = None,
        ) -> "List[AnimationFile|ImageFile]":
    """
    Encodes an animation using a list of AnimationConfigs,
    more efficent than calling `encode_animation` multiple times

    Returns:
        List[AnimationFile|ImageFile]: List of encoded output, guarenteed to be in the same order as the configs

    Raises:
        ValueError: Image is too big to process
        ValueError: Could not Load Image
    """
    configs = configs or Default.batch_animation
    pillow = open_as_pillow(data)
    return [encode_with_config(data, pillow, config) for config in configs]

