from dataclasses import dataclass
from typing_extensions import TypeAlias


@dataclass
class OriginalFileConfig:
    pass


@dataclass
class ImageEncodeConfig:
    width: int
    height: int
    quality: int = 100
    lossless: bool = False


@dataclass
class AnimationEncodeConfig:
    width: int
    height: int
    quality: int = 100
    lossless: bool = False


@dataclass
class ThumbnailConfig(ImageEncodeConfig):
    offset: float = 0.5


@dataclass
class AnimationSummaryConfig(AnimationEncodeConfig):
    frames: int = 0


ImageConfig: TypeAlias = "ImageEncodeConfig | OriginalFileConfig"
AnimationConfig: TypeAlias = "ThumbnailConfig | AnimationEncodeConfig | OriginalFileConfig"
VideoConfig: TypeAlias = "ThumbnailConfig | OriginalFileConfig"
