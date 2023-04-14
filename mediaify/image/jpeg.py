from ..files import ImageFile
from ..configs import (
    JPEGEncodeConfig,
)
from ..resize import calculate_downscale
from PIL import Image as PILImage
import io


def encode_as_jpeg(
        pillow: PILImage.Image,
        config: JPEGEncodeConfig
        ) -> ImageFile:
    if config.resize is not None:
        im_size = (pillow.width, pillow.height)
        size = calculate_downscale(im_size, config.resize)
        pillow = pillow.resize(size, PILImage.LANCZOS)

    buf = io.BytesIO()
    pillow.save(
        fp=buf,
        format="jpeg",
        optimize=True,
        quality=config.quality,
        progressive=config.progressive,
    )

    return ImageFile(
        data=buf.getvalue(),
        mimetype='image/jpeg',
        width=pillow.width,
        height=pillow.height,
    )
