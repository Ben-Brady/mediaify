from dataclasses import dataclass

@dataclass
class ImageEncodingConfig:
    width: int
    height: int
    quality: int = 100
    lossless: bool = False


@dataclass
class VideoEncodingConfig:
    width: int
    height: int
    quality: int = 100
    lossless: bool = False
