from .utils import validate_image
from ..data import COMPLEX_IMAGE, TestImage
import mediaify
from mediaify.configs import (
    JPEGFormat,
    PNGFormat,
    WEBPImageFormat,
    ResizeConfig,
    ImageEncodingType,
)
import pytest


def load_image(filepath: str, config: ImageEncodingType) -> mediaify.ImageFile:
    with open(filepath, 'rb') as f:
        data = f.read()

    return mediaify.encode_image(data, config)


@pytest.mark.parametrize(
    "mimetype,config",
    [
        ("image/jpeg", JPEGFormat(quality=60, progressive=True)),
        ("image/png", PNGFormat()),
        ("image/webp", WEBPImageFormat()),
    ],
    ids=["jpeg", "png", "webp"],
)
def test_encode_image_formats(mimetype, config):
    with open(COMPLEX_IMAGE.filepath, 'rb') as f:
        data = f.read()

    image = mediaify.encode_image(data, config)

    assert image.width == COMPLEX_IMAGE.width
    assert image.height == COMPLEX_IMAGE.height
    assert image.mimetype == mimetype
    assert validate_image(image.data)


@pytest.mark.parametrize(
    "mimetype,config",
    [
        ("image/jpeg", JPEGFormat(quality=60, progressive=True)),
        ("image/png", PNGFormat()),
        ("image/webp", WEBPImageFormat()),
    ],
    ids=["jpeg", "png", "webp"],
)
def test_encode_image_with_resize(mimetype, config):
    with open(COMPLEX_IMAGE.filepath, 'rb') as f:
        data = f.read()

    image = mediaify.encode_image(data, config)

    assert image.width == COMPLEX_IMAGE.width
    assert image.height == COMPLEX_IMAGE.height
    assert image.mimetype == mimetype
    assert validate_image(image.data)
