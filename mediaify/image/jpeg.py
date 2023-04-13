from ..files import ImageFile
from ..configs import (
    JPEGEncodeConfig,
)
from ..utils import calculate_downscale
from PIL import Image as PILImage
import io


def encode_as_jpeg(
        pillow: PILImage.Image,
        config: JPEGEncodeConfig
        ) -> ImageFile:
    width, height = calculate_downscale(
        current=(pillow.width, pillow.height),
        target=(config.width, config.height),
    )

    buf = io.BytesIO()
    pillow.resize(
        (width, height),
        PILImage.LANCZOS,
    ).save(
        fp=buf,
        format="jpeg",
        optimize=True,
        quality=config.quality,
        progressive=config.progressive,
    )

    return ImageFile(
        data=buf.getvalue(),
        mimetype='image/jpeg',
        width=width,
        height=height,
    )
