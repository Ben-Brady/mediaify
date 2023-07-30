from . import guess_type, encode_video, encode_animation, encode_image
from . import ThumbnailEncoding, ImageFile, MediaFile, UnencodedEncoding
from typing import overload


@overload
def encode_file(
    data: bytes,
    config: "ThumbnailEncoding"
    ) -> ImageFile:
    ...


@overload
def encode_file(
    data: bytes,
    config: "UnencodedEncoding|None" = None
    ) -> MediaFile:
    ...


def encode_file(
    data: bytes,
    config: "ThumbnailEncoding|UnencodedEncoding|None" = None
    ) -> MediaFile:
    type = guess_type(data)
    if type == "audio":
        return encode_animation(data, config)
    elif type == "image":
        return encode_image(data, config)
    elif type == "animation":
        return encode_animation(data, config)
    else:
        return encode_video(data, config)

