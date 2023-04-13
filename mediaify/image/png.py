from ..files import ImageFile
from ..configs import (
    PNGEncodeConfig,
)
from ..utils import calculate_downscale
from PIL import Image as PILImage
import io


def encode_as_png(
        pillow: PILImage.Image,
        config: PNGEncodeConfig,
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
        format="png",
        optimize=True,
    )

    return ImageFile(
        data=buf.getvalue(),
        mimetype='image/png',
        width=width,
        height=height,
    )
