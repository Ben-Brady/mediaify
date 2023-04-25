from .base import AnimationFormat
from . import (
    ResizeConfig,
    UnencodedEncoding,
    ThumbnailEncoding,
)
from dataclasses import dataclass
from typing import Union
from typing_extensions import TypeAlias

@dataclass
class GIFFormat(AnimationFormat):
    "Encode as a .gif animation"
    resize: "ResizeConfig | None" = None

    def __repr__(self) -> str:
        return f"GifAnimation({self.resize})"


@dataclass
class WEBPAnimationFormat(AnimationFormat):
    "Encode as a .webp animation"
    resize: "ResizeConfig | None" = None

    quality: int = 85
    "The webp quality"
    lossless: bool = False
    "Should the image be lossless?"

    def __repr__(self) -> str:
        if self.lossless:
            quality = "lossless"
        else:
            quality = f"quality={self.quality}"

        resize = repr(self.resize) if self.resize else ""
        return f"WebpAnimation({resize} {quality})"



AnimationEncodingType = Union[
    AnimationFormat,
    UnencodedEncoding,
    ThumbnailEncoding,
]
