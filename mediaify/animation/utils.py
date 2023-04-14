from PIL.Image import Image, LANCZOS
from typing import List, Tuple


def get_animation_duration_in_milliseconds(pillow: Image) -> int:
    "Get animation duration in seconds"
    return sum(get_frame_lengths(pillow))


def get_animation_duration_in_seconds(pillow: Image) -> float:
    "Get animation d`uration in seconds"
    return sum(get_frame_lengths(pillow)) / 1000


def resize_animation(pillow: Image, size: "Tuple[int, int]") -> "list[Image]":
    return [
        frame.resize(size, LANCZOS)
        for frame in extract_animation_frames(pillow)
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
