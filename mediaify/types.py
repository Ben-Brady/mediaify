from dataclasses import dataclass
from typing import Union

@dataclass
class ImageFile:
    data: bytes
    mimetype: str
    height: int
    width: int


@dataclass
class AnimationFile:
    data: bytes
    mimetype: str
    height: int
    width: int
    frame_count: int
    duration: float


@dataclass
class VideoFile:
    data: bytes
    mimetype: str
    height: int
    width: int
    duration: float
    framerate: str
    hasAudio: bool


GenericFile = Union[ImageFile, AnimationFile, VideoFile]
