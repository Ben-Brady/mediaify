from .utils import validate_image
from ..data import COMPLEX_IMAGE
from mediaify import JPEGEncodeConfig, ResizeConfig, encode_image


def test_encode_as_jpeg():
    with open(COMPLEX_IMAGE.filepath, 'rb') as f:
        data = f.read()

    image = encode_image(
        data,
        config=JPEGEncodeConfig(
            resize=ResizeConfig(
                width=100,
                height=100,
            ),
            quality=60,
            progressive=True,
        )
    )

    assert image.width == 100
    assert image.height == 100
    assert image.mimetype == "image/jpeg"
    assert validate_image(image.data)
