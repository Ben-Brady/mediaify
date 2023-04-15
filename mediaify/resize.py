from dataclasses import dataclass
from typing import Tuple


@dataclass
class ResizeConfig:
    width: "int | None" = None
    height: "int | None" = None

    max_width: "int | None" = None
    max_height: "int | None" = None


def calculate_downscale(size: "Tuple[int, int]", config: ResizeConfig) -> "Tuple[int, int]":
    width, height = size

    downscale_factors = [1.0]
    if config.max_width is not None:
        downscale_factors.append(width / config.max_width)
    if config.max_height is not None:
        downscale_factors.append(height / config.max_height)
    downscale_factor = max(downscale_factors)


    if config.width is not None:
        output_width = config.width
    else:
        output_width = int(width / downscale_factor)

    if config.height is not None:
        output_height = config.height
    else:
        output_height = int(height / downscale_factor)

    return (output_width, output_height)
