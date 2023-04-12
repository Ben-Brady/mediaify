from ..files import ImageFile
from ..configs import (
    WEBPImageEncodeConfig,
)
from ..utils import calculate_downscale
from PIL import Image as PILImage
import io


def encode_as_webp(
        pillow: PILImage.Image,
        config: WEBPImageEncodeConfig
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
        format="webp",
        quality=config.quality,
        lossless=config.lossless
    )

    data = buf.getvalue()

    return ImageFile(
        data=data,
        mimetype='image/webp',
        width=width,
        height=height,
    )
