import mediaify
from tests.data import TRANSPARENT_ANIMATION
import pytest
import io
from PIL import Image as PILImage


animation_config = mediaify.WEBPAnimationEncodeConfig(
    quality=90,
    lossless=True,
)


def test_Webp_Preserve_Transparency():
    with open(TRANSPARENT_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    animation = mediaify.encode_animation(data, animation_config)

    buf = io.BytesIO(animation.data)
    pillow = PILImage.open(buf)
    for x in range(pillow.n_frames):
        pillow.seek(x)
        RGB_MinMax_Values = pillow.getextrema()
        MaxTransparency = RGB_MinMax_Values[3][0]
        assert MaxTransparency != 255, f"Frame {x} is not transparent"

