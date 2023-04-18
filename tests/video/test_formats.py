from ..data import FIRE_VIDEO, TestVideo
import mediaify
from mediaify.configs import (
    WEBMEncodeConfig,
    MP4EncodeConfig,
    VideoConfig,
    ResizeConfig,
)
import pytest


def encode_file(filepath: str, config: VideoConfig) -> mediaify.VideoFile:
    with open(filepath, 'rb') as f:
        data = f.read()

    return mediaify.encode_video(data, config)  # type: ignore


@pytest.mark.parametrize(
    "mimetype, config",
    [
        ("video/mp4", MP4EncodeConfig()),
        ("video/webm", WEBMEncodeConfig()),
    ],
    ids=["mp4", "webm"],)
def test_video_encodes_successfully(mimetype, config):
    video = encode_file(FIRE_VIDEO.filepath, config)

    assert len(video.data) != 0
    assert video.width == FIRE_VIDEO.width
    assert video.height == FIRE_VIDEO.height
    assert video.mimetype == mimetype

@pytest.mark.parametrize(
    "config",
    [
        (MP4EncodeConfig(framerate=10)),
        (WEBMEncodeConfig(framerate=10)),
    ],
    ids=["mp4", "webm"],)
def test_video_change_framerate(config):
    video = encode_file(FIRE_VIDEO.filepath, config)

    assert len(video.data) != 0
    assert video.framerate == 10
    assert video.width == FIRE_VIDEO.height
    assert video.height == FIRE_VIDEO.height


@pytest.mark.parametrize(
    "config",
    [MP4EncodeConfig(), WEBMEncodeConfig()],
    ids=["mp4", "webm"],
)
def test_video_resizes_successfully(config: "MP4EncodeConfig | WEBMEncodeConfig"):
    config.resize = ResizeConfig(width=320, height=240)
    video = encode_file(FIRE_VIDEO.filepath, config)
    assert video.width == 320
    assert video.height == 240
