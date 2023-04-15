from PIL import Image as PILImage
from magic import Magic
import io


def is_animated_sequence(data: bytes) -> bool:
    pil_img = PILImage.open(io.BytesIO(data))
    return pil_img.is_animated


def guess_mimetype(data: bytes) -> str:
    magic = Magic(mime=True)
    return magic.from_buffer(data)
