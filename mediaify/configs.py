from dataclasses import dataclass
from typing_extensions import TypeAlias

ImageConfig: TypeAlias = """
    PNGEncodeConfig |
    JPEGEncodeConfig |
    WEBPImageEncodeConfig |
    UnencodedConfig |
    ThumbnailConfig
"""
AnimationConfig: TypeAlias = """
    GIFEncodeConfig |
    WEBPAnimationEncodeConfig |
    UnencodedConfig |
    ThumbnailConfig
"""
VideoConfig: TypeAlias = """
    AnimationSummaryConfig  |
    UnencodedConfig |
    ThumbnailConfig
"""


@dataclass
class UnencodedConfig:
    pass


@dataclass
class WEBPImageEncodeConfig:
    width: int
    height: int
    quality: int = 85
    lossless: bool = False


@dataclass
class PNGEncodeConfig:
    width: int
    height: int


@dataclass
class JPEGEncodeConfig:
    width: int
    height: int
    quality: int = 85
    progressive: bool = True


@dataclass
class GIFEncodeConfig:
    width: int
    height: int


@dataclass
class WEBPAnimationEncodeConfig:
    width: int
    height: int
    quality: int = 85
    lossless: bool = False


@dataclass
class ThumbnailConfig:
    encoding: ImageConfig
    offset: float = 0.2


@dataclass
class AnimationSummaryConfig:
    encoding: AnimationConfig
    framerate: int = 15
    frames: int = 45
