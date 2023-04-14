from ..files import ImageFile
from ..configs import (
    PNGEncodeConfig,
)
from ..resize import calculate_downscale
from PIL import Image as PILImage
import io


def encode_as_png(
        pillow: PILImage.Image,
        config: PNGEncodeConfig,
        ) -> ImageFile:
    if config.resize is not None:
        im_size = (pillow.width, pillow.height)
        size = calculate_downscale(im_size, config.resize)
        pillow = pillow.resize(size, PILImage.LANCZOS)

    buf = io.BytesIO()
    pillow.save(
        fp=buf,
        format="png",
        optimize=True,
    )

    return ImageFile(
        data=buf.getvalue(),
        mimetype='image/png',
        width=pillow.width,
        height=pillow.height,
    )
