from ..data import KFC_VIDEO
import mediaify
import pytest


def test_encode_as_video_summary():
    with open(KFC_VIDEO.filepath, 'rb') as f:
        data = f.read()

    config = mediaify.VideoPreviewAnimationEncoding(
        encoding=mediaify.WEBPAnimationFormat(),
        framerate=15,
        frames=30,
    )
    animation = mediaify.encode_video(data, config)

    assert isinstance(animation, mediaify.AnimationFile)
    assert animation.duration == pytest.approx(2.0, 0.1)
    assert animation.frame_count == 30
    assert animation.width == KFC_VIDEO.width
    assert animation.height == KFC_VIDEO.height
