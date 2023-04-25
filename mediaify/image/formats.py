from typing import Callable
from ..files import ImageFile
from ..configs import (
    JPEGFormat,
    PNGFormat,
    WEBPImageFormat,
    ResizeConfig,
)
from ..resize import calculate_downscale
from PIL import Image as PILImage
import io


def encode_as_jpeg(
        pillow: PILImage.Image,
        config: JPEGFormat
        ) -> ImageFile:
    def save(image: PILImage.Image, fp: io.BytesIO) -> None:
        image.save(
        fp=fp,
        format="jpeg",
        optimize=True,
        quality=config.quality,
        progressive=config.progressive,
    )

    return encode_generic_image(
        pillow,
        config.resize,
        save,
        "image/jpeg"
    )


def encode_as_png(
        pillow: PILImage.Image,
        config: PNGFormat,
        ) -> ImageFile:
    def save(image: PILImage.Image, fp: io.BytesIO) -> None:
        image.save(
            fp=fp,
            format="png",
            optimize=True,
        )

    return encode_generic_image(
        pillow,
        config.resize,
        save,
        "image/png"
    )


def encode_as_webp(
        pillow: PILImage.Image,
        config: WEBPImageFormat
        ) -> ImageFile:
    def save(image: PILImage.Image, fp: io.BytesIO) -> None:
        image.save(
            fp,
            "webp",
            quality=config.quality,
            lossless=config.lossless
        )

    return encode_generic_image(
        pillow,
        config.resize,
        save,
        "image/webp"
    )


def encode_generic_image(
        pillow: PILImage.Image,
        resize: "ResizeConfig|None",
        save_function: "Callable[[PILImage.Image, io.BytesIO], None]",
        mimetype: str,
        ) -> ImageFile:
    if resize is not None:
        im_size = (pillow.width, pillow.height)
        size = calculate_downscale(im_size, resize)
        pillow = pillow.resize(size, PILImage.LANCZOS)

    buf = io.BytesIO()
    save_function(pillow, buf)

    return ImageFile(
        data=buf.getvalue(),
        mimetype=mimetype,
        width=pillow.width,
        height=pillow.height,
    )

