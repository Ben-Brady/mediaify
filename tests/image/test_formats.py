from .utils import validate_image
from ..data import COMPLEX_IMAGE, TestImage
from mediaify import (
    JPEGEncodeConfig,
    PNGEncodeConfig,
    WEBPImageEncodeConfig,
    ResizeConfig,
    ImageConfig,
    ImageFile,
    encode_image,
)


def load_image(filepath: str, config: ImageConfig) -> ImageFile:
    with open(filepath, 'rb') as f:
        data = f.read()

    return encode_image(data, config)


def assert_encoded_correctly(data: TestImage, image: ImageFile, mimetype: str):
    assert image.width == data.width
    assert image.height == data.height
    assert image.mimetype == mimetype
    assert validate_image(image.data)


def test_encode_as_jpeg():
    image = load_image(
        COMPLEX_IMAGE.filepath,
        config=JPEGEncodeConfig(
            quality=60,
            progressive=True,
        )
    )

    assert_encoded_correctly(COMPLEX_IMAGE, image, "image/jpeg")


def test_encode_as_png():
    image = load_image(
        COMPLEX_IMAGE.filepath,
        config=PNGEncodeConfig()
    )

    assert_encoded_correctly(COMPLEX_IMAGE, image, "image/png")


def test_encode_as_webp():
    image = load_image(
        COMPLEX_IMAGE.filepath,
        config=WEBPImageEncodeConfig(
            quality=60,
        )
    )

    assert_encoded_correctly(COMPLEX_IMAGE, image, "image/webp")
