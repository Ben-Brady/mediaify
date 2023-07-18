from PIL import Image as PILImage
from magic import Magic
import io
from typing import Literal


def is_animated_sequence(data: bytes) -> bool:
    pil_img = PILImage.open(io.BytesIO(data))
    if hasattr(pil_img, 'is_animated'):
        return pil_img.is_animated
    else:
        return False


def guess_mimetype(data: bytes) -> str:
    magic = Magic(mime=True)
    return magic.from_buffer(data)


def guess_type(data: bytes) -> "Literal['audio', 'image', 'video', 'animation']":
    """Guesses the type of the file from it's data

    Returns:
        "audio" | "image" | "animaton" | "video"

    Raises:
        ValueError: Filetype not supported
    """
    mimetype = guess_mimetype(data)

    if mimetype.startswith('video'):
        return "video"
    elif mimetype.startswith('audio'):
        return "audio"
    elif mimetype.startswith('image') or mimetype.startswith('animation'):
        if is_animated_sequence(data):
            return "animation"
        else:
            return "image"
    else:
        raise ValueError("Filetype not supported")
