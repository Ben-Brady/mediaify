import mediaify
from mediaify.configs import (
    WEBPAnimationFormat,
    GIFFormat,
    AnimationEncodingType,
)
from tests.data import FRACTAL_ANIMATION, RICARDO_ANIMATION
import pytest
import io
import random
from PIL import Image as PILImage


def assert_animations_the_same(
        original_im: PILImage.Image,
        encoded_im: PILImage.Image
        ):
    for i in range(original_im.n_frames):
        original_im.seek(i)
        encoded_im.seek(i)
        original_frame = original_im.copy().convert('RGBA')
        encoded_frame = encoded_im.copy().convert('RGBA')
        # Sample 100 pixels to compare
        for _ in range(100):
            x = random.randint(0, original_frame.width - 1)
            y = random.randint(0, original_frame.height - 1)
            original_pix = original_frame.getpixel((x, y))
            encoded_pix = encoded_frame.getpixel((x, y))
            assert original_pix == encoded_pix


@pytest.mark.parametrize(
    "config",
    [
        WEBPAnimationFormat(lossless=True),
        GIFFormat(),
    ],
    ids=lambda config: config.__class__.__name__,
)
def test_encoding_animations_preserve_image(config: AnimationEncodingType):
    with open(FRACTAL_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    animation = mediaify.encode_animation(data, config)

    original_im = PILImage.open(io.BytesIO(data))
    encoded_im = PILImage.open(io.BytesIO(animation.data))
    assert_animations_the_same(original_im, encoded_im)


@pytest.mark.parametrize(
    "config",
    [
        WEBPAnimationFormat(quality=100, lossless=True),
        GIFFormat(),
    ],
    ids=lambda config: config.__class__.__name__,
)
def test_encoding_animations_preserve_transparency(config):
    with open(RICARDO_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    animation = mediaify.encode_animation(data, config)

    original_im = PILImage.open(io.BytesIO(data))
    encoded_im = PILImage.open(io.BytesIO(animation.data))

    for i in range(original_im.n_frames):
        original_im.seek(i)
        encoded_im.seek(i)
        original_frame = original_im.copy().convert('RGBA')
        encoded_frame = encoded_im.copy().convert('RGBA')

        # Sample 100 pixels to compare
        for _ in range(500):
            x = random.randint(0, original_frame.width - 1)
            y = random.randint(0, original_frame.height - 1)
            original_pix = original_frame.getpixel((0, 0    ))
            encoded_pix = encoded_frame.getpixel((x, y))
            assert bool(original_pix[3]) == bool(encoded_pix[3])
