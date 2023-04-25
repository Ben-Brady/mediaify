from ..data import KFC_VIDEO
import mediaify
from mediaify import (
    WEBMFormat,
    MP4Format,
    VideoEncodingType,
    AV1Codec,
    VP9Codec,
    H264Codec,
    OpusCodec,
)
import pytest

def encode_file(path: str, config: VideoEncodingType) -> mediaify.VideoFile:
    with open(path, 'rb') as f:
        data = f.read()

    return mediaify.encode_video(data, config)  # type: ignore

a = WEBMFormat(video_codec=VP9Codec(preset="realtime"))

@pytest.mark.parametrize(
    "config",
    [
        (MP4Format(video_codec=AV1Codec(preset=8))),
        (MP4Format(video_codec=H264Codec(preset="ultrafast"))),
        (WEBMFormat(video_codec=AV1Codec(preset=8))),
        (WEBMFormat(video_codec=VP9Codec(preset="realtime"))),
    ],
    ids=lambda x: f"{x.__class__.__name__}-{x.video_codec.__class__.__name__}",
)
def test_video_encodes_with_all_video_codecs(config):
    video = encode_file(KFC_VIDEO.filepath, config)

    assert len(video.data) != 0
    assert video.width == KFC_VIDEO.width
    assert video.height == KFC_VIDEO.height


@pytest.mark.parametrize(
    "config",
    [
        (MP4Format(audio_codec=OpusCodec(bitrate=32_000))),
        (WEBMFormat(audio_codec=OpusCodec(bitrate=32_000))),
    ],
    ids=lambda x: f"{x.__class__.__name__}-{x.audio_codec.__class__.__name__}",
)
def test_video_encodes_with_all_audio_codecs(config):
    video = encode_file(KFC_VIDEO.filepath, config)

    assert len(video.data) != 0
    assert video.width == KFC_VIDEO.width
    assert video.height == KFC_VIDEO.height
