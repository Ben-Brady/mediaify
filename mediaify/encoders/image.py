from .. import ImageFile, GenericFile, configs
from ._dimensions import Dimensions
from PIL import Image as PILImage
import io


def encode_image(
        data: bytes,
        configs: "list[configs.ImageConfig]",
        ) -> "list[GenericFile]":
    """Raises:
    - ValueError: Image is too big to process
    - ValueError: Could not Load Image
    """
    buf = io.BytesIO(data)
    try:
        # formats=None means attempt to load all formats
        pillow = PILImage.open(buf, formats=None)
    except PILImage.DecompressionBombError:
        raise ValueError("Image is too big to process")
    except Exception as e:
        raise ValueError(str(e))

    files = []
    for config in configs:
        files.append(encode_with_config(pillow, config))

    return files


def encode_with_config(pillow: PILImage.Image, config: configs.ImageConfig) -> ImageFile:
    size = Dimensions(pillow.width, pillow.height)
    target_size = Dimensions(config.width, config.height)

    size = size.calculate_downscale(target_size)

    buf = io.BytesIO()
    (
        pillow
        .resize((size.x, size.y), PILImage.LANCZOS)
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
        width=size.x,
        height=size.y,
    )

