from ..files import ImageFile
from ..configs import (
    UnencodedConfig,
    WEBPImageEncodeConfig,
    PNGEncodeConfig,
    JPEGEncodeConfig,
    ThumbnailConfig,
    ImageConfig
)
from ..utils import guess_mimetype
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
        config: "ImageConfig",
        ) -> "ImageFile":
    if isinstance(config, ThumbnailConfig):
        return encode_with_config(data, pillow, config.encoding)

    if isinstance(config, UnencodedConfig):
        return encode_as_original(data, pillow)
    elif isinstance(config, PNGEncodeConfig):
        return encode_as_png(pillow, config)
    elif isinstance(config, JPEGEncodeConfig):
        return encode_as_jpeg(pillow, config)
    elif isinstance(config, WEBPImageEncodeConfig):
        return encode_as_webp(pillow, config)
    else:
        raise ValueError("Invalid encoding config")


def encode_pilllow_with_config(
        pillow: PILImage.Image,
        config: "ImageConfig",
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
    """Raises:
    - ValueError: Image is too big to process
    - ValueError: Could not Load Image
    """
    buf = io.BytesIO(data)
    try:
        pillow = PILImage.open(buf, formats=None)
    except PILImage.DecompressionBombError:
        raise ValueError("Image is too big to process")
    except Exception as e:
        raise ValueError(str(e))

    return pillow
