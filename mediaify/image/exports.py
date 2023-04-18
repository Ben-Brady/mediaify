from ..files import ImageFile
from ..configs import UnencodedConfig, ImageConfig
from ..presets import Default
from .encode import encode_with_config, open_as_pillow
from typing import List


def load_image(data: bytes) -> "ImageFile":
    """Loads an image without any processing,
    identical to `encode_image(data, UnencodedConfig())`

    Returns:
        ImageFile: The loaded image

    Raises:
        ValueError: Image is too big to process
        ValueError: Could not Load Image
    """
    pillow = open_as_pillow(data)
    return encode_with_config(data, pillow, UnencodedConfig())


def encode_image(
        data: bytes,
        config: "ImageConfig|None" = None,
        ) -> "ImageFile":
    """Encodes an image using an ImageConfig

    Returns:
        ImageFile: The encoded image

    Raises:
        ValueError: Image is too big to process
        ValueError: Could not Load Image
    """
    config = config or Default.image
    pillow = open_as_pillow(data)
    return encode_with_config(data, pillow, config)


def batch_encode_image(
        data: bytes,
        configs: "List[ImageConfig]|None" = None,
        ) -> "List[ImageFile]":
    """Encodes an image using a list of ImageConfigs,
    more efficent than calling `encode_image` multiple times

    Returns:
        List[ImageFile]: List of encoded images, guarenteed to be in the same order as the configs

    Raises:
        ValueError: Image is too big to process
        ValueError: Could not Load Image
    """
    configs = configs or Default.batch_image
    pillow = open_as_pillow(data)
    return [encode_with_config(data, pillow, config) for config in configs]
