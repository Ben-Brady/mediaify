from ..files import ImageFile
from ..configs import UnencodedEncoding, ImageEncodingType
from .encode import encode_with_config, open_as_pillow
from typing import List


def encode_image(
        data: bytes,
        config: "ImageEncodingType|None" = None,
        ) -> "ImageFile":
    """Encodes an image using an image config

    Returns:
        ImageFile: The encoded image

    Raises:
        ValueError: Image is too big to process
        ValueError: Could not Load Image
    """
    pillow = open_as_pillow(data)
    return encode_with_config(data, pillow, config)


def batch_encode_image(
        data: bytes,
        configs: "List[ImageEncodingType]",
        ) -> "List[ImageFile]":
    """Encodes an image using a list of image configs,
    more efficent than calling `encode_image` multiple times

    Returns:
        List[ImageFile]: List of encoded images, guarenteed to be in the same order as the configs

    Raises:
        ValueError: Image is too big to process
        ValueError: Could not Load Image
    """
    pillow = open_as_pillow(data)
    return [encode_with_config(data, pillow, config) for config in configs]
