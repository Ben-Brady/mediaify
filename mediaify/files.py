from dataclasses import dataclass
from warnings import warn
from mimetypes import guess_extension, add_type
from typing_extensions import TypeAlias, Literal
add_type('image/apng', '.apng')
add_type('image/webp', '.webp')


class GenericMediaFile:
    data: bytes
    "The file's raw data, can be used to save to a file"
    mimetype: str
    "The file's mimetype E.g. 'image/png'"
    type: Literal["image", "animation", "video"]
    "The media type, one of 'image', 'animation', 'video'"

    @property
    def ext(self) -> str:
        """
        The file extention for this file including the '.'.
        If the mimetype is unknown, '.bin' is returned
        """

        ext = guess_extension(self.mimetype)
        if ext is None:
            warn(
                f"Could not guess extention for mimetype '{self.mimetype}'\n"
                "Using '.bin' instead"
            )
            return ".bin"
        else:
            return ext


@dataclass(repr=False)
class ImageFile(GenericMediaFile):
    data: bytes
    mimetype: str
    type = "image"
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
    type = "animation"
    height: int
    width: int
    frame_count: int
    "The number of frames in the animation"
    duration: float
    "The duration of the animation in seconds"

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
    type = "video"
    height: int
    width: int
    duration: float
    "The duration of the video in seconds"
    framerate: float
    "The framerate of the video in fps"
    hasAudio: bool
    "Does this video contain audio?"

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

__all__ = [
    "ImageFile",
    "AnimationFile",
    "VideoFile",
]
