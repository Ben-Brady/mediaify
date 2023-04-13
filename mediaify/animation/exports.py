from ..files import AnimationFile, ImageFile
from ..configs import AnimationConfig
from ..presets import Default
from .encode import open_as_pillow, encode_with_config, encode_as_original
from typing import List


def load_animation(data: bytes) -> "AnimationFile":
    """Raises:
    - ValueError("Animation was too large")
    - ValueError("Could not Load Animation")
    """
    pillow = open_as_pillow(data)
    return encode_as_original(data, pillow)


def encode_animation(
        data: bytes,
        config: AnimationConfig = Default.animation,
        ) -> "AnimationFile|ImageFile":
    """Raises:
    - ValueError("Animation was too large")
    - ValueError("Could not Load Animation")
    """
    pillow = open_as_pillow(data)
    return encode_with_config(data, pillow, config)


def batch_encode_animation(
        data: bytes,
        configs: "List[AnimationConfig]" = Default.batch_animation,
        ) -> "List[AnimationFile|ImageFile]":
    """Raises:
    - ValueError("Animation was too large")
    - ValueError("Could not Load Animation")
    """
    pillow = open_as_pillow(data)
    return [encode_with_config(data, pillow, config) for config in configs]

