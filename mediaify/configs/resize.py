from . import ResizeConfig
from dataclasses import dataclass
from typing import Literal


@dataclass
class MaxResolutionResize(ResizeConfig):
    max_width: "int | None" = None
    "With maximum width before downscaling"
    max_height: "int | None" = None
    "With maximum height before downscaling"

    def __repr__(self) -> str:
        return f"MaxRes({self.max_width}x{self.max_height})"

@dataclass
class TargetResolutionResize(ResizeConfig):
    width: "int | None" = None
    "The width to resize to"
    height: "int | None" = None
    "The height to resize to"
    method: "Literal['stretch']" = "stretch"
    "How to change the video aspect ratio, defaults to stretch"

    def __repr__(self) -> str:
        return f"TargetRes({self.width}x{self.height})"
