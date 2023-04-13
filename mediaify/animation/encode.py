from ..image import encode as image_encode
from ..files import AnimationFile, ImageFile
from ..configs import (
    AnimationConfig,
    ThumbnailConfig,
    GIFEncodeConfig,
    WEBPAnimationEncodeConfig,
    UnencodedConfig,
)
from ..utils import guess_mimetype
from .utils import (
    get_animation_duration_in_milliseconds,
    get_animation_duration_in_seconds,
)
from .gif import encode_as_gif
from .webp import encode_as_webp
import io
from PIL import Image as PILImage


def encode_with_config(
        data: bytes,
        pillow: PILImage.Image,
        config: AnimationConfig
        ) -> "AnimationFile|ImageFile":
    if isinstance(config, UnencodedConfig):
        return encode_as_original(data, pillow)
    elif isinstance(config, GIFEncodeConfig):
        return encode_as_gif(pillow, config)
    elif isinstance(config, WEBPAnimationEncodeConfig):
        return encode_as_webp(pillow, config)
    elif isinstance(config, ThumbnailConfig):
        return encode_as_thumbnail(pillow, config)
    else:
        raise ValueError("Invalid encoding config")


def encode_as_original(
        data: bytes,
        pillow: PILImage.Image,
        ) -> AnimationFile:
    return AnimationFile(
        data=data,
        mimetype=guess_mimetype(data),
        height=pillow.height,
        width=pillow.width,
        frame_count=pillow.n_frames,
        duration=get_animation_duration_in_seconds(pillow),
    )


def encode_as_thumbnail(
        pillow: PILImage.Image,
        config: ThumbnailConfig
        ) -> ImageFile:
    # Seek to the correct offset
    # TODO: Rewrite to be neater
    total_duration = get_animation_duration_in_milliseconds(pillow)
    cur_frame_time = 0
    for x in range(pillow.n_frames):
        pillow.seek(x)
        cur_frame_time += pillow.info['duration']
        percentage_in = total_duration / cur_frame_time
        if percentage_in >= config.offset:
            break

    return image_encode.encode_pilllow_with_config(pillow, config.encoding)


def open_as_pillow(data: bytes) -> PILImage.Image:
    buf = io.BytesIO(data)
    try:
        # formats=None attempt to load all formats
        pillow = PILImage.open(buf, formats=None)
    except PILImage.DecompressionBombError:
        raise ValueError("Animation was too large")
    except Exception:
        raise ValueError("Could not Load Animation")

    return pillow
