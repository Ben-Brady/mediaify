from dataclasses import dataclass
from typing import Literal
from typing_extensions import TypeAlias


class ImageEncodeConfig:
    resize: "ResizeConfig | None" = None
    "How to resize the image, None to disable resizing. Defaults to None."


class AnimationEncodeConfig:
    resize: "ResizeConfig | None" = None
    "How to resize the animation, None to disable resizing. Defaults to None."


class VideoEncodeConfig:
    resize: "ResizeConfig | None" = None
    "How to resize the video, None to disable resizing. Defaults to None."


ImageConfig: TypeAlias = "ImageEncodeConfig | UnencodedConfig | ThumbnailConfig"
AnimationConfig: TypeAlias = "AnimationEncodeConfig | UnencodedConfig | ThumbnailConfig"
VideoConfig: TypeAlias = "VideoEncodeConfig | VideoPreviewAnimationConfig | UnencodedConfig | ThumbnailConfig"


@dataclass
class UnencodedConfig:
    """
    Process the video without re-encoding it,
    simply extracting the metadata
    """


@dataclass
class ResizeConfig:
    width: "int | None" = None
    height: "int | None" = None

    max_width: "int | None" = None
    max_height: "int | None" = None


@dataclass
class WEBPImageEncodeConfig(ImageEncodeConfig):
    "Encode as a .webp image"
    resize: "ResizeConfig | None" = None
    quality: int = 85
    "The webp quality"
    lossless: bool = False
    "Should the image be lossless?"


@dataclass
class PNGEncodeConfig(ImageEncodeConfig):
    "Encode as a .png image"
    resize: "ResizeConfig | None" = None


@dataclass
class JPEGEncodeConfig(ImageEncodeConfig):
    "Encode as a .jpg image"
    resize: "ResizeConfig | None" = None
    quality: int = 85
    "The JPEG quality option"
    progressive: bool = True
    "Encode in a way that allows it to be displayed in low quality before it is fully downloaded."


@dataclass
class GIFEncodeConfig(AnimationEncodeConfig):
    "Encode as a .gif animation"
    resize: "ResizeConfig | None" = None


@dataclass
class WEBPAnimationEncodeConfig(AnimationEncodeConfig):
    "Encode as a .webp animation"
    resize: "ResizeConfig | None" = None

    quality: int = 85
    "The webp quality"
    lossless: bool = False
    "Should the image be lossless?"


@dataclass
class H264EncodeConfig:
    "The H264 video codec"
    crf: int = 21
    """Constant Rate Factor. Lower is better quality, but larger file size.\n
    0 is worst quality and 51 is best quality"""

    preset: Literal[
        "ultrafast", "superfast", "veryfast",
        "faster", "fast", "medium", "slow",
        "slower", "veryslow"
    ] = "fast"
    "The speed to encode the video at, slower means lower filesize at same quality."


@dataclass
class VP9EncodeConfig:
    "The VP9 video codec"
    crf: int = 21
    """Constant Rate Factor. Lower is better quality, but larger file size.\n
    0 is best quality and 63 is worst quality"""
    preset: Literal["good", "best", "realtime"] = "good"
    """
    The speed to encode the video at, slower means lower filesize at same quality.
    \nRealtime is the fastest, worst quality
    \nGood is the default, a mix of speed and file size, default
    \nBest is the slowest, smallest file size
    """


@dataclass
class OpusEncodeConfig:
    "The Opus audio codec"
    bitrate: int = 128_000
    "The bitrate to encode the audio in bits per second, defaults to 128kbps"


@dataclass
class WEBMEncodeConfig(VideoEncodeConfig):
    "Encode as a .webm video"
    resize: "ResizeConfig | None" = None
    "How to resize the video, None to disable resizing. Defaults to None."
    framerate: "float|None" = None
    "The framerate to encode the video at, None to use the original framerate. Defaults to None."
    video_codec: VP9EncodeConfig = VP9EncodeConfig()
    "The video codec to use, defaults to VP9EncodeConfig"
    audio_codec: "OpusEncodeConfig|None" = OpusEncodeConfig()
    "The audio codec to use, defaults to OpusEncodeConfig"


@dataclass
class MP4EncodeConfig(VideoEncodeConfig):
    "Encode as a .mp4 video"
    resize: "ResizeConfig | None" = None
    "How to resize the video, None to disable resizing. Defaults to None."
    framerate: "float|None" = None
    "The framerate to encode the video at, None to use the original framerate. Defaults to None."
    video_codec: H264EncodeConfig = H264EncodeConfig()
    "The video codec to use, defaults to H264EncodeConfig"
    audio_codec: "OpusEncodeConfig|None" = OpusEncodeConfig()
    "The audio codec to use, defaults to OpusEncodeConfig"


@dataclass
class ThumbnailConfig:
    """Functions as an image, animation, or video config.
    \nCreates a thumbnail for animations and videos, simply re-encodes images"""
    encoding: ImageEncodeConfig = WEBPImageEncodeConfig()
    offset: float = 0.2


@dataclass
class VideoPreviewAnimationConfig:
    "Encode a video as a short animation, useful for previews."
    encoding: AnimationEncodeConfig = WEBPAnimationEncodeConfig()
    framerate: int = 15
    "What FPS should the output animation be"
    frames: int = 45
    "How many frames to generate"

__all__ = [
    "WEBPImageEncodeConfig",
    "JPEGEncodeConfig",
    "PNGEncodeConfig",

    "GIFEncodeConfig",
    "WEBPAnimationEncodeConfig",

    "WEBMEncodeConfig",
    "MP4EncodeConfig",
    "H264EncodeConfig",
    "VP9EncodeConfig",
    "OpusEncodeConfig",

    "VideoPreviewAnimationConfig",
    "ThumbnailConfig",
    "UnencodedConfig",
    "ResizeConfig",

    "AnimationConfig",
    "ImageConfig",
    "VideoConfig",
]
