from . import UnencodedEncoding
from .base import AudioFormat
from dataclasses import dataclass
from typing import Literal
from typing_extensions import TypeAlias


@dataclass
class MP3Format(AudioFormat):
    "Encode as an .mp3 audio file"
    quality: Literal[0,1,2,3,4,5,6,7,8,9] = 6
    """
    The quality preset to use for libmp3lame for average bitrate.
    9 is the worst quality, 0 is the best quality.
    https://trac.ffmpeg.org/wiki/Encode/MP3#VBREncoding
    """


@dataclass
class FLACFormat(AudioFormat):
    "Encode as a .flac audio file"


@dataclass
class WAVFormat(AudioFormat):
    "Encode as a .wav audio file"


@dataclass
class OpusFormat(AudioFormat):
    "Encode as a .opus audio file"

    bitrate: int = 128_000
    "The bitrate to encode the audio in bits per second, defaults to 128kbps"


AudioEncodingType: TypeAlias = "AudioFormat | UnencodedEncoding"
