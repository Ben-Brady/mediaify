from .utils import validate_image
from ..data import COMPLEX_IMAGE
from mediaify import JPEGEncodeConfig, encode_image


def test_encode_as_jpeg():
    with open(COMPLEX_IMAGE.filepath, 'rb') as f:
        data = f.read()

    output_width = COMPLEX_IMAGE.width // 2
    output_height = COMPLEX_IMAGE.height // 2
    image = encode_image(data, JPEGEncodeConfig(
        width=output_width,
        height=output_height,
        quality=60,
        progressive=True,
    ))

    assert image.width == output_width
    assert image.height == output_height
    assert image.mimetype == "image/jpeg"
    assert validate_image(image.data)
