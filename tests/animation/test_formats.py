from .utils import validate_animation
from ..data import FRACTAL_ANIMATION
import mediaify
from mediaify.configs import (
    WEBPAnimationEncodeConfig,
    GIFEncodeConfig,
    ResizeConfig,
)
import pytest


@pytest.mark.parametrize(
    "mimetype,config",
    [
        ("image/gif", GIFEncodeConfig()),
        ("image/webp", WEBPAnimationEncodeConfig()),
    ],
    ids=["gif", "webp"],
)
def test_encode_with_format(mimetype, config):
    with open(FRACTAL_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    animation = mediaify.encode_animation(data, config)

    assert isinstance(animation, mediaify.AnimationFile)
    assert animation.mimetype == mimetype
    assert animation.frame_count == FRACTAL_ANIMATION.frame_count
    assert validate_animation(animation.data)


@pytest.mark.parametrize(
    "config_type",
    [GIFEncodeConfig, WEBPAnimationEncodeConfig],
    ids=["gif", "webp"],
)
def test_encode_as_webp_animation(config_type):
    with open(FRACTAL_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    config = config_type(
        resize=ResizeConfig(
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
