from .base import VideoFormat, AnimationFormat
from . import (
    ResizeConfig,
    UnencodedEncoding,
    ThumbnailEncoding,
)
from . import H264Codec, OpusCodec, VP9Codec, AV1Codec
from dataclasses import dataclass, field
from typing import Union


@dataclass
class WEBMFormat(VideoFormat):
    "Encode as a .webm video"
    resize: "ResizeConfig | None" = None
    "How to resize the video, None to disable resizing. Defaults to None."
    framerate: "float|None" = None
    """
    The framerate to encode the video at, None to use the original framerate.
    Defaults to None.
    """
    video_codec: "VP9Codec|AV1Codec" = field(default_factory=VP9Codec)
    "The video codec to use, defaults to VP9EncodeConfig"
    audio_codec: "OpusCodec|None" = field(default_factory=OpusCodec)
    "The audio codec to use, defaults to OpusEncodeConfig"

    def __repr__(self) -> str:
        if self.audio_codec is None:
            audio = ""
        else:
            audio = f" {self.audio_codec}"

        if self.resize is None:
            resize = ""
        else:
            resize = f"{self.resize} "

        return f"WEBMFormat({resize}{self.video_codec}{audio})"


@dataclass
class MP4Format(VideoFormat):
    "Encode as a .mp4 video"
    resize: "ResizeConfig | None" = None
    "How to resize the video, None to disable resizing. Defaults to None."
    framerate: "float|None" = None
    """
    The framerate to encode the video at, None to use the original framerate.
    Defaults to None.
    """
    video_codec: "H264Codec|AV1Codec" = field(default_factory=H264Codec)
    "The video codec to use, defaults to H264EncodeConfig"
    audio_codec: "OpusCodec|None" = field(default_factory=OpusCodec)
    "The audio codec to use, defaults to OpusEncodeConfig"

    def __repr__(self) -> str:
        if self.audio_codec is None:
            audio = ""
        else:
            audio = f" {self.audio_codec}"

        if self.resize is None:
            resize = ""
        else:
            resize = f"{self.resize} "

        return f"WEBMFormat({resize}{self.video_codec}{audio})"


@dataclass
class VideoPreviewAnimationEncoding:
    "Encode a video as a short animation, useful for previews."
    encoding: "AnimationFormat|None" = None
    framerate: float = 15
    "What FPS should the output animation be"
    frames: int = 45
    "How many frames to generate"


VideoEncodingType = Union[
    VideoFormat,
    VideoPreviewAnimationEncoding,
    UnencodedEncoding,
    ThumbnailEncoding,
]
