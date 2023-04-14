from ..files import ImageFile
from ..configs import (
    WEBPImageEncodeConfig,
)
from ..resize import calculate_downscale
from PIL import Image as PILImage
import io


def encode_as_webp(
        pillow: PILImage.Image,
        config: WEBPImageEncodeConfig
        ) -> ImageFile:
    if config.resize is not None:
        im_size = (pillow.width, pillow.height)
        size = calculate_downscale(im_size, config.resize)
        pillow = pillow.resize(size, PILImage.LANCZOS)

    buf = io.BytesIO()
    pillow.save(
        fp=buf,
        format="webp",
        quality=config.quality,
        lossless=config.lossless
    )

    return ImageFile(
        data=buf.getvalue(),
        mimetype='image/webp',
        width=pillow.width,
        height=pillow.height,
    )
