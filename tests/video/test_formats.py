from ..data import KFC_VIDEO
import mediaify
from mediaify import (
    WEBMFormat,
    MP4Format,
    VideoEncodingType,
    VP9Codec,
    H264Codec,
    TargetResolutionResize,
)
import pytest

QUICK_H264 = H264Codec(preset="ultrafast")
QUICK_VP9 = VP9Codec(preset="realtime")


def encode_file(path: str, config: VideoEncodingType) -> mediaify.VideoFile:
    with open(path, 'rb') as f:
        data = f.read()

    return mediaify.encode_video(data, config)  # type: ignore


@pytest.mark.parametrize(
    "mimetype, config",
    [
        ("video/mp4", MP4Format(video_codec=QUICK_H264)),
        ("video/webm", WEBMFormat(video_codec=QUICK_VP9)),
    ],
    ids=["mp4", "webm"],)
def test_video_encodes_successfully(mimetype, config):
    video = encode_file(KFC_VIDEO.filepath, config)

    assert len(video.data) != 0
    assert video.width == KFC_VIDEO.width
    assert video.height == KFC_VIDEO.height
    assert video.mimetype == mimetype


@pytest.mark.parametrize(
    "config",
    [
        MP4Format(framerate=10, video_codec=QUICK_H264),
        WEBMFormat(framerate=10, video_codec=QUICK_VP9),
    ],
    ids=["mp4", "webm"],)
def test_video_change_framerate(config):
    video = encode_file(KFC_VIDEO.filepath, config)

    assert len(video.data) != 0
    assert video.framerate == 10
    assert video.width == KFC_VIDEO.width
    assert video.height == KFC_VIDEO.height


@pytest.mark.parametrize(
    "config",
    [
        MP4Format(video_codec=QUICK_H264),
        WEBMFormat(video_codec=QUICK_VP9)
    ],
    ids=["mp4", "webm"],
)
def test_video_resizes_successfully(config: "MP4Format | WEBMFormat"):
    config.resize = TargetResolutionResize(width=320, height=240)
    video = encode_file(KFC_VIDEO.filepath, config)
    assert video.width == 320
    assert video.height == 240
