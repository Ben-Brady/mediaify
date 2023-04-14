from ..data import FIRE_VIDEO, TestVideo
from mediaify import (
    WEBMEncodeConfig,
    MP4EncodeConfig,
    VideoConfig,
    VideoFile,
    ResizeConfig,
    encode_video
)
import pytest


def encode_file(filepath: str, config: VideoConfig) -> VideoFile:
    with open(filepath, 'rb') as f:
        data = f.read()

    return encode_video(data, config)  # type: ignore


@pytest.mark.parametrize("args", [
    ("video/mp4", MP4EncodeConfig()),
    ("video/webm", WEBMEncodeConfig()),
])
def test_video_encode(args):
    mimetype, config = args
    video = encode_file(FIRE_VIDEO.filepath, config)

    assert len(video.data) != 0
    assert video.width == FIRE_VIDEO.width
    assert video.height == FIRE_VIDEO.height
    assert video.mimetype == mimetype


@pytest.mark.parametrize("config", [
    MP4EncodeConfig(),
    WEBMEncodeConfig(),
])
def test_video_resize(config: "MP4EncodeConfig | WEBMEncodeConfig"):
    config.resize = ResizeConfig(width=320, height=240)
    video = encode_file(FIRE_VIDEO.filepath, config)
    assert video.width == 320
    assert video.height == 240
