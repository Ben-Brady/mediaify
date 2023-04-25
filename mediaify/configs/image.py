from .base import ImageFormat
from . import (
    ResizeConfig,
    UnencodedEncoding,
    ThumbnailEncoding
)
from dataclasses import dataclass
from typing import Union


@dataclass
class WEBPImageFormat(ImageFormat):
    "Encode as a .webp image"
    resize: "ResizeConfig | None" = None
    quality: int = 85
    "The webp quality"
    lossless: bool = False
    "Should the image be lossless?"

    def __repr__(self) -> str:
        if self.lossless:
            quality = f"lossless"
        else:
            quality = f"quality={self.quality}"

        return f"Webp({self.resize} {quality})"


@dataclass
class PNGFormat(ImageFormat):
    "Encode as a .png image"
    resize: "ResizeConfig | None" = None

    def __repr__(self) -> str:
        return f"PNG({self.resize})"

@dataclass
class JPEGFormat(ImageFormat):
    "Encode as a .jpg image"
    resize: "ResizeConfig | None" = None
    quality: int = 85
    "The JPEG quality option"
    progressive: bool = True
    "Encode in a way that allows it to be displayed in low quality before it is fully downloaded."

    def __repr__(self) -> str:
        if self.progressive:
            return f"JPEG({self.resize} quality={self.quality} progressive)"
        else:
            return f"JPEG({self.resize} quality={self.quality})"


ImageEncodingType = Union[
    ImageFormat,
    UnencodedEncoding,
    ThumbnailEncoding,
]
