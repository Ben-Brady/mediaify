from .utils import validate_animation
from ..data import FRACTAL_ANIMATION
from mediaify import (
    GIFEncodeConfig,
    ResizeConfig,
    AnimationFile,
    encode_animation,
)


def test_encode_as_gif():
    with open(FRACTAL_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    animation = encode_animation(
        data,
        config=GIFEncodeConfig(
            resize=ResizeConfig(
                width=100,
                height=100,
            ),
        )
    )

    assert isinstance(animation, AnimationFile)
    assert animation.width == 100
    assert animation.height == 100
    assert animation.mimetype == "image/gif"
    assert animation.frame_count == FRACTAL_ANIMATION.frame_count
    assert validate_animation(animation.data)
