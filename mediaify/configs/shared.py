from .base import ImageFormat
from dataclasses import dataclass


@dataclass
class UnencodedEncoding:
    """
    Process the video without re-encoding it, instead extracts the metadata.
    This works for all media types and is used as the default.
    """


@dataclass
class ThumbnailEncoding:
    """Creates a thumbnail for images, animations and videos
    \nFunctions as an image, animation, or video config.
    """
    encoding: "ImageFormat|None" = None
    offset: float = 0.2
