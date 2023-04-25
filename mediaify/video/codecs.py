from ..configs import (
    AV1Codec,
    H264Codec,
    VP9Codec,
    OpusCodec,
)
import subprocess
from ffmpeg import FFmpeg
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


def apply_av1_codec(ffmpeg: FFmpeg, codec: AV1Codec) -> FFmpeg:
    assert_codec_supported("libaom-av1")
    # Prefer libsvtav1 if available
    if codec_supported("libsvtav1"):
        return (
            ffmpeg
            .option("c:v", "libsvtav1")
            .option("preset", codec.preset)
            .option("crf", codec.crf)
        )
    elif codec_supported("libaom-av1"):
        return (
            ffmpeg
            .option("c:v", "libaom-av1")
            .option("cpu-used", codec.preset)
            .option("crf", codec.crf)
        )
    else:
        raise RuntimeError("ffmpeg not installed with libaom-av1 or libsvtav1")


def apply_h264_codec(ffmpeg: FFmpeg, codec: H264Codec) -> FFmpeg:
    assert_codec_supported("libx264")
    return (
        ffmpeg
        .option("c:v", "libx264")
        .option("preset", codec.preset)
        .option("crf", codec.crf)
    )


def apply_vp9_codec(ffmpeg: FFmpeg, codec: VP9Codec) -> FFmpeg:
        return (
            ffmpeg
            .option("c:v", "libvpx-vp9")
            .option("crf", codec.crf)
            .option("deadline", codec.preset)
        )


def apply_opus_codec(ffmpeg: FFmpeg, codec: OpusCodec) -> FFmpeg:
    assert_codec_supported("libx264")
    return (
        ffmpeg
        .option("c:a", "libopus")
        .option("b:a", codec.bitrate)
    )


def apply_no_audio(ffmpeg: FFmpeg) -> FFmpeg:
    assert_codec_supported("libx264")
    return (
        ffmpeg
        .option("an", None)
    )
