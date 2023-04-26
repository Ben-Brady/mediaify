from dataclasses import dataclass
from warnings import warn
from mimetypes import guess_extension, add_type
from typing_extensions import TypeAlias, Literal
add_type('image/apng', '.apng')
add_type('image/webp', '.webp')


class BaseFile:
    data: bytes
    "The file's raw data, can be used to save to a file"
    mimetype: str
    "The file's mimetype E.g. 'image/png'"
    type: Literal["audio", "image", "animation", "video"]
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

    def save(self, filepath: str) -> None:
        "Saves the file to the given path"
        with open(filepath, "wb") as f:
            f.write(self.data)


@dataclass(repr=False)
class AudioFile(BaseFile):
    data: bytes
    mimetype: str
    type = "audio"

    def __repr__(self) -> str:
        return (
            "AudioFile("
            f"{self.mimetype}, {format_bytes(len(self.data))}"
            ")"
        )


@dataclass(repr=False)
class ImageFile(BaseFile):
    data: bytes
    mimetype: str
    type = "image"
    height: int
    width: int

    def __repr__(self) -> str:
        FORMAT = "ImageFile({w}x{h}, {mime}, {size})"
        return FORMAT.format(
            w=self.width,
            h=self.height,
            mime=self.mimetype,
            size=format_bytes(len(self.data)),
        )


@dataclass(repr=False)
class AnimationFile(BaseFile):
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
        FORMAT = "AnimationFile({w}x{h}, {dur}s {frames} frames, {fps}fps, {mime}, {size})"
        return FORMAT.format(
            w=self.width,
            h=self.height,
            dur=self.duration,
            frames=self.frame_count,
            fps=round(self.frame_count / self.duration, 2),
            mime=self.mimetype,
            size=format_bytes(len(self.data)),
        )


@dataclass(repr=False)
class VideoFile(BaseFile):
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
        FORMAT = "VideoFile({w}x{h}, {dur}s, {fps}fps, {audio}, {mime}, {size})"
        return FORMAT.format(
            w=self.width,
            h=self.height,
            dur=round(self.duration, 2),
            fps=round(self.framerate, 2),
            audio="audio" if self.hasAudio else "no audio",
            mime=self.mimetype,
            size=format_bytes(len(self.data)),
        )


# https://stackoverflow.com/a/1094933
def format_bytes(length: float) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]:
        if abs(length) < 1000.0:
            return f"{length:3.1f}{unit}"
        length /= 1000.0

    return f"{length:.1f}Yi"


MediaFile: TypeAlias = "AudioFile | ImageFile | AnimationFile | VideoFile"

__all__ = [
    "MediaFile",
    "AudioFile",
    "ImageFile",
    "AnimationFile",
    "VideoFile",
]
