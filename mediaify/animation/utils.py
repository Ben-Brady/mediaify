from ..configs import ResizeConfig
from ..resize import calculate_downscale
from PIL.Image import Image, LANCZOS
from typing import List


def get_animation_duration_in_milliseconds(pillow: Image) -> int:
    "Get animation duration in seconds"
    return sum(get_frame_lengths(pillow))


def get_animation_duration_in_seconds(pillow: Image) -> float:
    "Get animation d`uration in seconds"
    return sum(get_frame_lengths(pillow)) / 1000


def resize_animation(frames: "List[Image]", resize: "ResizeConfig|None") -> "List[Image]":
    if resize is None:
        return frames

    pillow = frames[0]
    size = (pillow.width, pillow.height)
    size = calculate_downscale(size, resize)
    return [
        frame.resize(size, LANCZOS)
        for frame in frames
    ]


def get_frame_lengths(pillow: Image) -> "List[int]":
    frame_durations = []
    for x in range(pillow.n_frames):
        pillow.seek(x)
        duration = int(pillow.info['duration'])
        frame_durations.append(duration)

    return frame_durations


def extract_animation_frames(pillow: Image) -> "List[Image]":
    frames = []
    for x in range(pillow.n_frames):
        pillow.seek(x)
        frames.append(pillow.copy())

    pillow.seek(0)
    return frames
