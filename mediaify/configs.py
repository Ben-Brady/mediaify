from dataclasses import dataclass
from typing_extensions import TypeAlias

ImageConfig: TypeAlias = \
    "ThumbnailConfig | UnencodedConfig | WEBPImageEncodeConfig"
AnimationConfig: TypeAlias = \
    "ThumbnailConfig | UnencodedConfig | GIFEncodeConfig | WEBPAnimationEncodeConfig"
VideoConfig: TypeAlias = \
    "ThumbnailConfig | UnencodedConfig | AnimationSummaryConfig"


@dataclass
class UnencodedConfig:
    pass


@dataclass
class WEBPImageEncodeConfig:
    width: int
    height: int
    quality: int = 100
    lossless: bool = False


@dataclass
class GIFEncodeConfig:
    width: int
    height: int


@dataclass
class WEBPAnimationEncodeConfig:
    width: int
    height: int
    quality: int = 100
    lossless: bool = False


@dataclass
class ThumbnailConfig:
    encoding: ImageConfig
    offset: float = 0.2


@dataclass
class AnimationSummaryConfig:
    encoding: AnimationConfig
    framerate: int = 5
    frames: int = 20
