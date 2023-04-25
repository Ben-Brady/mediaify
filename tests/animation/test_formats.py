from .utils import validate_animation
from ..data import FRACTAL_ANIMATION
import mediaify
from mediaify.configs import (
    WEBPAnimationFormat,
    GIFFormat,
    TargetResolutionResize,
)
import pytest


@pytest.mark.parametrize(
    "mimetype,config",
    [
        ("image/gif", GIFFormat()),
        ("image/webp", WEBPAnimationFormat()),
    ],
    ids=["gif", "webp"],
)
def test_encode_animation(mimetype, config):
    with open(FRACTAL_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    animation = mediaify.encode_animation(data, config)

    assert isinstance(animation, mediaify.AnimationFile)
    assert animation.mimetype == mimetype
    assert animation.frame_count == FRACTAL_ANIMATION.frame_count
    assert validate_animation(animation.data)


@pytest.mark.parametrize(
    "config_type",
    [GIFFormat, WEBPAnimationFormat],
    ids=["gif", "webp"],
)
def test_encode_animation_with_resize(config_type):
    with open(FRACTAL_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    config = config_type(
        resize=TargetResolutionResize(
            width=100,
            height=100,
        ),
    )
    animation = mediaify.encode_animation(data, config)

    assert isinstance(animation, mediaify.AnimationFile)
    assert animation.width == 100
    assert animation.height == 100
    assert animation.frame_count == FRACTAL_ANIMATION.frame_count
    assert validate_animation(animation.data)
