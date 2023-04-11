from PIL import Image as PILImage
from magic import Magic
import io


def _calculate_downscale(current: "tuple[int, int]", target: "tuple[int, int]") -> "tuple[int, int]":
    width, hieght = current
    target_w, target_h = target
    biggest_factor = max(
        1,
        width / target_w,
        hieght / target_h,
    )

    output_width = int(width / biggest_factor)
    output_height = int(hieght / biggest_factor)

    return (output_width, output_height)


def is_animated_sequence(data: bytes) -> bool:
    buf = io.BytesIO(data)
    pil_img = PILImage.open(buf, formats=None)
    return pil_img.is_animated


def guess_mimetype(data: bytes) -> str:
    magic = Magic(mime=True)
    return magic.from_buffer(data)
