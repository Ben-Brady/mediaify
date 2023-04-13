from ..files import ImageFile
from ..configs import UnencodedConfig, ImageConfig
from ..presets import Default
from .encode import encode_with_config, open_as_pillow
from typing import List


def load_image(data: bytes) -> "ImageFile":
    """Raises:
    - ValueError: Image is too big to process
    - ValueError: Could not Load Image
    """
    pillow = open_as_pillow(data)
    return encode_with_config(data, pillow, UnencodedConfig())


def encode_image(
        data: bytes,
        config: ImageConfig = Default.image,
        ) -> "ImageFile":
    """Raises:
    - ValueError: Image is too big to process
    - ValueError: Could not Load Image
    """
    pillow = open_as_pillow(data)
    return encode_with_config(data, pillow, config)


def batch_encode_image(
        data: bytes,
        configs: "List[ImageConfig]" = Default.batch_image,
        ) -> "List[ImageFile]":
    """Raises:
    - ValueError: Image is too big to process
    - ValueError: Could not Load Image
    """
    pillow = open_as_pillow(data)
    return [encode_with_config(data, pillow, config) for config in configs]
