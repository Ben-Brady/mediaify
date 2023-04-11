from ..types import MediaFile, ImageFile
from ..configs import OriginalFileConfig, ImageEncodeConfig
from .utils import _calculate_downscale
from PIL import Image as PILImage
from typing import Sequence
import io


def encode_image(
        data: bytes,
        configs: "list[ImageEncodeConfig|OriginalFileConfig]",
        ) -> "Sequence[ImageFile]":
    """Raises:
    - ValueError: Image is too big to process
    - ValueError: Could not Load Image
    """
    pillow = _open_pillow_image(data)
    return [encode_with_config(data, pillow, config) for config in configs]


def encode_single_image(
        data: bytes,
        config: ImageEncodeConfig,
        ) -> "ImageFile":
    """Raises:
    - ValueError: Image is too big to process
    - ValueError: Could not Load Image
    """
    pillow = _open_pillow_image(data)
    return encode_with_config(data, pillow, config)


def encode_with_config(
        data: bytes,
        pillow: PILImage.Image,
        config: "ImageEncodeConfig|OriginalFileConfig",
        ) -> "ImageFile":
    if isinstance(config, ImageEncodeConfig):
        return encode_pillow_with_image_config(pillow, config)
    elif isinstance(config, OriginalFileConfig):
        return encode_pillow_with_originalfile_config(data, pillow)
    else:
        raise ValueError("Invalid encoding config")


def encode_pillow_with_image_config(pillow: PILImage.Image, config: ImageEncodeConfig) -> ImageFile:
    size = _calculate_downscale(
        current=(pillow.width, pillow.height),
        target=(config.width, config.height),
    )

    buf = io.BytesIO()
    (
        pillow
        .resize(size, PILImage.LANCZOS)
        .save(
            fp=buf,
            format="webp",
            quality=config.quality,
            lossless=config.lossless
        )
    )
    data = buf.getvalue()

    return ImageFile(
        data=data,
        mimetype='image/webp',
        width=size[0],
        height=size[1],
    )


def encode_pillow_with_originalfile_config(data:bytes, pillow: PILImage.Image) -> ImageFile:
    return ImageFile(
        data=data,
        mimetype='image/webp',
        width=pillow.width,
        height=pillow.height,
    )


def _open_pillow_image(data: bytes) -> PILImage.Image:
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
