from ..files import ImageFile
from ..utils import guess_mimetype
from ..configs import (
    ThumbnailEncoding,
    UnencodedEncoding,
    PNGFormat,
    JPEGFormat,
    WEBPImageFormat,
    ImageEncodingType,
)
from .formats import (
    encode_as_jpeg,
    encode_as_png,
    encode_as_webp
)
from PIL import Image as PILImage
import io


def encode_with_config(
        data: bytes,
        pillow: PILImage.Image,
        config: "ImageEncodingType|None",
        ) -> "ImageFile":
    if isinstance(config, ThumbnailEncoding):
        return encode_with_config(data, pillow, config.encoding)

    if isinstance(config, UnencodedEncoding) or config is None:
        return encode_as_original(data, pillow)
    elif isinstance(config, PNGFormat):
        return encode_as_png(pillow, config)
    elif isinstance(config, JPEGFormat):
        return encode_as_jpeg(pillow, config)
    elif isinstance(config, WEBPImageFormat):
        return encode_as_webp(pillow, config)
    else:
        raise ValueError("Invalid encoding config")


def encode_pilllow_with_config(
        pillow: PILImage.Image,
        config: "ImageEncodingType|None",
        ) -> "ImageFile":
    buf = io.BytesIO()
    pillow.save(fp=buf, format="png")
    return encode_with_config(buf.getvalue(), pillow, config)


def encode_as_original(data: bytes, pillow: PILImage.Image) -> ImageFile:
    return ImageFile(
        data=data,
        mimetype=guess_mimetype(data),
        width=pillow.width,
        height=pillow.height,
    )


def open_as_pillow(data: bytes) -> PILImage.Image:
    """
    Raises:
        ValueError: Image is too big to process
        ValueError: Could not Load Image
    """
    buf = io.BytesIO(data)
    try:
        pillow = PILImage.open(buf, formats=None)
    except PILImage.DecompressionBombError:
        raise ValueError("Image is too big to process")
    except Exception as e:
        raise ValueError(str(e))

    return pillow
