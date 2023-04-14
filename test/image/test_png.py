from .utils import validate_image
from ..data import COMPLEX_IMAGE
from mediaify import PNGEncodeConfig, ResizeConfig, encode_image


def test_encode_as_png():
    with open(COMPLEX_IMAGE.filepath, 'rb') as f:
        data = f.read()

    image = encode_image(
        data,
        config=PNGEncodeConfig(
            resize=ResizeConfig(
                width=100,
                height=100,
            )
        )
    )

    assert image.width == 100
    assert image.height == 100
    assert image.mimetype == "image/png"
    assert validate_image(image.data)
