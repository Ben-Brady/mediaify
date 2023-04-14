from .utils import validate_animation
from ..data import FRACTAL_ANIMATION
from mediaify import (
    WEBPAnimationEncodeConfig,
    ResizeConfig,
    AnimationFile,
    encode_animation,
)


def test_encode_as_webp_animation():
    with open(FRACTAL_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    animation = encode_animation(
        data,
        config=WEBPAnimationEncodeConfig(
            resize=ResizeConfig(
                width=100,
                height=100,
            ),
            quality=60,
        )
    )

    assert isinstance(animation, AnimationFile)
    assert animation.width == 100
    assert animation.height == 100
    assert animation.mimetype == "image/webp"
    assert animation.frame_count == FRACTAL_ANIMATION.frame_count
    assert validate_animation(animation.data)
