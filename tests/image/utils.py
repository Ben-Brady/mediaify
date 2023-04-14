from PIL import Image as PILImage
import io


def validate_image(data: bytes) -> bool:
    try:
        PILImage.open(io.BytesIO(data))
        return True
    except:
        return False
