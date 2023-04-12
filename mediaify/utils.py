from PIL import Image as PILImage
from magic import Magic
import io
from typing import Tuple


def calculate_downscale(current: "Tuple[int, int]", target: "Tuple[int, int]") -> "Tuple[int, int]":
    biggest_factor = max(
        1,
        current[0] / target[0],
        current[1] / target[1],
    )

    output_width = int(current[0] / biggest_factor)
    output_height = int(current[1] / biggest_factor)

    return (output_width, output_height)


def is_animated_sequence(data: bytes) -> bool:
    buf = io.BytesIO(data)
    pil_img = PILImage.open(buf, formats=None)
    return pil_img.is_animated


def guess_mimetype(data: bytes) -> str:
    magic = Magic(mime=True)
    return magic.from_buffer(data)
