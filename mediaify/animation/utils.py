from PIL.Image import Image
from typing import List


def get_animation_duration_in_milliseconds(pillow: Image) -> int:
    "Get animation duration in seconds"
    return sum(get_frame_lengths(pillow))


def get_animation_duration_in_seconds(pillow: Image) -> float:
    "Get animation duration in seconds"
    return sum(get_frame_lengths(pillow)) / 1000


def get_frame_lengths(pillow: Image) -> "List[int]":
    frame_durations = []
    for x in range(pillow.n_frames):
        pillow.seek(x)
        duration = int(pillow.info['duration'])
        frame_durations.append(duration)

    return frame_durations


def get_animation_frames(pillow: Image) -> "List[Image]":
    frames = []
    for x in range(pillow.n_frames):
        pillow.seek(x)
        frames.append(pillow.copy())

    return frames
