from dataclasses import dataclass
from abc import ABC, abstractmethod
from warnings import warn
from mimetypes import guess_extension, add_type
from typing_extensions import TypeAlias
add_type('image/apng', '.apng')
add_type('image/webp', '.webp')


class GenericMediaFile(ABC):
    data: bytes
    mimetype: str

    @property
    def ext(self) -> str:
        "Returns the file extention for this file, including the '.'"

        ext = guess_extension(self.mimetype)
        if ext is None:
            warn(
                f"Could not guess extention for mimetype '{self.mimetype}'\n"
                "Using '.bin' instead"
            )
            return ".bin"
        else:
            return ext

    @abstractmethod
    def __repr__(self) -> str:
        ...


@dataclass(repr=False)
class ImageFile(GenericMediaFile):
    data: bytes
    mimetype: str
    height: int
    width: int

    def __repr__(self) -> str:
        return f"ImageFile(" \
            f"{self.width}x{self.height}, " \
            f"{self.mimetype}, {format_bytes(len(self.data))}" \
            ")"


@dataclass(repr=False)
class AnimationFile(GenericMediaFile):
    data: bytes
    mimetype: str
    height: int
    width: int
    frame_count: int
    duration: float

    def __repr__(self) -> str:
        return f'AnimationFile(' \
            f"{self.width}x{self.height}, " \
            f"{self.duration}s {self.frame_count} frames, "\
            f"{(self.frame_count / self.duration):.2f}fps, " \
            f"{self.mimetype}, " \
            f"{format_bytes(len(self.data))}" \
            ")"


@dataclass(repr=False)
class VideoFile(GenericMediaFile):
    data: bytes
    mimetype: str
    height: int
    width: int
    duration: float
    framerate: int
    hasAudio: bool

    def __repr__(self) -> str:
        return f'VideoFile(' \
            f"{self.width}x{self.height}, " \
            f"{self.duration:.3f}s, {self.framerate}fps, " \
            f"{'audio' if self.hasAudio else 'no audio'}, " \
            f"{self.mimetype}, {format_bytes(len(self.data))}" \
            ")"


# https://stackoverflow.com/a/1094933
def format_bytes(length: float) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]:
        if abs(length) < 1000.0:
            return f"{length:3.1f}{unit}"
        length /= 1000.0
    
    return f"{length:.1f}Yi"


MediaFile: TypeAlias = "ImageFile | AnimationFile | VideoFile"
