from .. import Dimensions, ImageFile
from . import probe
from PIL import Image as PILImage
import io


def encode_image(data: bytes, configs: "list[ImageEncodingConfig]", max_size: "int|None" = None) -> "list[ImageFile]":
    """Raises:
    - ValueError: Image is too big to process
    - ValueError: Could not Load Image
    """
    # Set max acceptable image size to prevent DOS
    # TODO: Add Max Image Size to settings
    if max_size is not None:
        PILImage.MAX_IMAGE_PIXELS = max_size

    buf = io.BytesIO(data)
    try:
        # formats=None means attempt to load all formats
        pillow = PILImage.open(buf, formats=None)
    except PILImage.DecompressionBombError:
        raise ValueError("Image is too big to process")
    except Exception as e:
        raise ValueError(str(e))

    return [encode_with_config(pillow, config) for config in configs]


def encode_with_config(pillow: PILImage.Image, config: ImageEncodingConfig) -> ImageFile:
    actual_size = Dimensions(pillow.width, pillow.height)
    target_size = Dimensions(config.width, config.height)
    size = calculate_downscale(actual_size, target_size)

    buf = io.BytesIO()
    (
        pillow
        .resize((size.x, size.y), PILImage.LANCZOS)
        .save(
            fp=buf,
            format='webp',
            quality=config.quality,
            lossless=config.lossless
        )
    )
    data = buf.getvalue()

    return ImageFile(
        data=data,
        mimetype='image/webp',
        width=size.x,
        height=size.y,
    )


def calculate_downscale(resolution: Dimensions, target: Dimensions) -> Dimensions:
    biggest_factor = max(
        1,
        resolution.x / target.x,
        resolution.y / target.y,
    )

    output_width = int(resolution.x / biggest_factor)
    output_height = int(resolution.y / biggest_factor)

    return Dimensions(output_width, output_height)
