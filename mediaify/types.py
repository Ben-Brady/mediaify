from dataclasses import dataclass
from typing_extensions import TypeAlias


@dataclass(repr=False)
class ImageFile:
    data: bytes
    mimetype: str
    height: int
    width: int

    def __repr__(self) -> str:
        return f'ImageFile({self.width}x{self.height}, {self.mimetype})'


@dataclass(repr=False)
class AnimationFile:
    data: bytes
    mimetype: str
    height: int
    width: int
    frame_count: int
    duration: float

    def __repr__(self) -> str:
        return f'AnimationFile({self.width}x{self.height} {self.duration}ms, {self.mimetype})'


@dataclass(repr=False)
class VideoFile:
    data: bytes
    mimetype: str
    height: int
    width: int
    duration: float
    framerate: str
    hasAudio: bool

    def __repr__(self) -> str:
        return f'VideoFile(' \
            f"{self.width}x{self.height} {self.duration}s " \
            f"{'audio' if self.hasAudio else 'no audio'}, " \
            f"{self.mimetype})"


MediaFile: TypeAlias = "ImageFile | AnimationFile | VideoFile"
