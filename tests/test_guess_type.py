from typing_extensions import Literal
import mediaify
from . import data
import pytest

def test_guess_type():
    assert_guess_type(data.SINGLE_FRAME_ANIMATION.filepath, 'image')
    assert_guess_type(data.FRACTAL_ANIMATION.filepath, 'animation')
    assert_guess_type(data.RICARDO_ANIMATION.filepath, 'animation')
    assert_guess_type(data.COMPLEX_IMAGE.filepath, 'image')
    assert_guess_type(data.SMALL_IMAGE.filepath, 'image')
    assert_guess_type(data.KFC_VIDEO.filepath, 'video')
    assert_guess_type(data.FIRE_VIDEO.filepath, 'video')


def assert_guess_type(
        filepath: str,
        intended_type: "Literal['image', 'animation', 'video']"
        ):
    with open(filepath, 'rb') as f:
        data = f.read()

    guessed_type = mediaify.guess_type(data)
    assert guessed_type == intended_type

