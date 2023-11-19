from ..configs import (
    AV1Codec,
    H264Codec,
    VP9Codec,
    OpusCodec,
)
import subprocess
from ffmpeg import FFmpeg
from typing import Any, Union
import warnings


def codec_supported(codec: str) -> bool:
    with subprocess.Popen(
        ["ffmpeg", "-codecs"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        ) as p:
        p.wait()
        if p.stdout is None:
            warnings.warn(
                "ffmpeg codecs check process closed unexpectedly.\n"
                f"Defaulting to {codec} being suppported\n,"
                "possiblity of ffmpeg failure after.\n"
            )
            return True
        stdout = p.stdout.read().decode()

    return codec in stdout


def assert_codec_supported(codec: str):
    if not codec_supported(codec):
        raise RuntimeError(f"ffmpeg not installed with {codec}")


def generate_video_options(
    codec: Union[AV1Codec, H264Codec, VP9Codec]
) -> dict[str, Any]:
    if isinstance(codec, AV1Codec):
        # Multiple encoders
        return generate_av1_options(codec)
    elif isinstance(codec, H264Codec):
        assert_codec_supported("libx264")
        return {
            "c:v": "libx264",
            "preset": codec.preset,
            "crf": codec.crf,
        }
    elif isinstance(codec, VP9Codec):
        assert_codec_supported("libvpx-vp9")
        return {
            "c:v": "libvpx-vp9",
            "crf": codec.crf,
            "deadline": codec.preset,
        }
    else:
        raise ValueError(f"Invalid video codec: {type(codec)}")


def generate_audio_options(codec: Union[OpusCodec, None]) -> dict[str, Any]:
    if codec is None:
        return {"an": None}
    elif isinstance(codec, OpusCodec):
        assert_codec_supported("libx264")
        return {
            "c:a": "libopus",
            "b:a": codec.bitrate,
        }
    else:
        raise ValueError(f"Invalid audio codec: {type(codec)}")


def generate_av1_options(codec: AV1Codec) -> dict[str, Any]:
    # Prefer libsvtav1 if available
    if codec_supported("libsvtav1"):
        return {
            "c:v": "libsvtav1",
            "preset": codec.preset,
            "crf": codec.crf,
        }
    elif codec_supported("libaom-av1"):
        return {
            "c:v": "libaom-av1",
            "cpu-used": codec.preset,
            "crf": codec.crf,
        }
    else:
        raise RuntimeError("ffmpeg not installed with libaom-av1 or libsvtav1")
