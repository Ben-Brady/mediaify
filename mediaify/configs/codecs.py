from dataclasses import dataclass
from typing import Literal


@dataclass
class H264Codec:
    "The H264 video codec"
    crf: int = 21
    """Constant Rate Factor. Lower is better quality, but larger file size.\n
    0 is worst quality and 51 is best quality"""

    preset: Literal[
        "ultrafast", "superfast", "veryfast",
        "faster", "fast", "medium", "slow",
        "slower", "veryslow", "placebo"
    ] = "fast"
    """
    The speed to encode the video at, slower means lower filesize at same quality.

    From fastest to slowest:
        `ultrafast`, `superfast`, `veryfast`, `faster`, `fast`,
        `medium`, `slow`, `slower`, `veryslow`, `placebo`
    """
    def __repr__(self) -> str:
        return f"H264('{self.preset}' crf={self.crf})"



@dataclass
class VP9Codec:
    "The VP9 video codec"
    crf: int = 21
    """Constant Rate Factor. Lower is better quality, but larger file size.\n
    0 is best quality and 63 is worst quality"""
    preset: Literal["good", "best", "realtime"] = "good"
    """
    The speed to encode the video at, slower means lower filesize at same quality.
    \n`realtime` is the fastest, worst quality
    \n`good` is the default, a mix of speed and file size, default
    \n`best` is the slowest, smallest file size
    """

    def __repr__(self) -> str:
        return f"VP9('{self.preset}' crf={self.crf})"


@dataclass
class AV1Codec:
    "The AV1 video codec"
    crf: int = 50
    """Constant Rate Factor. Lower is better quality, but larger file size.\n
    0 is best quality and 63 is worst quality"""
    preset: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8] = 5
    """The speed to encode the video at,
    slower means lower filesize at same quality.
    \n0 is the slowest, best quality. 8 is the fastest, worst quality.
    """

    def __repr__(self) -> str:
        return f"AV1(preset:{self.preset} crf={self.crf})"


@dataclass
class OpusCodec:
    "The Opus audio codec"
    bitrate: int = 128_000
    "The bitrate to encode the audio in bits per second, defaults to 128kbps"

    def __repr__(self) -> str:
        return f"Opus({self.bitrate}bps)"
