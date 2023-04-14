from .configs import ResizeConfig
from typing import Tuple


def calculate_downscale(size: "Tuple[int, int]", config: ResizeConfig) -> "Tuple[int, int]":
    width, height = size

    downscale_factors = [1.0]
    if config.max_width is not None:
        downscale_factors.append(width / config.max_width)

    if config.max_height is not None:
        downscale_factors.append(height / config.max_height)

    biggest_factor = max(downscale_factors)
    output_width = int(width / biggest_factor)
    output_height = int(height / biggest_factor)

    if config.width is not None:
        output_width = config.width

    if config.height is not None:
        output_height = config.height


    return (output_width, output_height)
