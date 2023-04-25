from .configs import ResizeConfig, MaxResolutionResize, TargetResolutionResize
from typing import Tuple


def calculate_downscale(size: "Tuple[int, int]", config: ResizeConfig) -> "Tuple[int, int]":
    width, height = size

    if isinstance(config, MaxResolutionResize):
        downscale_factors = [1.0]
        if config.max_width is not None:
            downscale_factors.append(width / config.max_width)
        if config.max_height is not None:
            downscale_factors.append(height / config.max_height)
        downscale_factor = max(downscale_factors)

        output_width = int(width / downscale_factor)
        output_height = int(height / downscale_factor)
        return (output_width, output_height)
    elif isinstance(config, TargetResolutionResize):
        width = config.width or size[0]
        height = config.height or size[1]
        return width, height
    else:
        raise ValueError(f"Unknown resize config type: {type(config).__name__}")
