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
class ResizeConfig:
    width: "int | None" = None
    height: "int | None" = None
    
    max_width: "int | None" = None
    max_height: "int | None" = None


@dataclass
class UnencodedConfig:
    pass


@dataclass
class WEBPImageEncodeConfig:
    resize: "ResizeConfig | None" = None
    quality: int = 85
    lossless: bool = False


@dataclass
class PNGEncodeConfig:
    resize: "ResizeConfig | None" = None


@dataclass
class JPEGEncodeConfig:
    resize: "ResizeConfig | None" = None
    quality: int = 85
    progressive: bool = True


@dataclass
class GIFEncodeConfig:
    resize: "ResizeConfig | None" = None


@dataclass
class WEBPAnimationEncodeConfig:
    resize: "ResizeConfig | None" = None
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
