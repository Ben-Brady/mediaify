from dataclasses import dataclass

@dataclass
class ImageConfig:
    width: int
    height: int
    quality: int = 100
    lossless: bool = False


@dataclass
class AnimationConfig:
    width: int
    height: int
    quality: int = 100
    lossless: bool = False


@dataclass
class VideoConfig:
    width: int
    height: int


@dataclass
class ThumbnailConfig(ImageConfig):
    offset: float = 0.5


@dataclass
class AnimationSummaryConfig(AnimationConfig):
    frames: int = 0
