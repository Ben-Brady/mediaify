from .. import AnimationFile, ImageFile, configs
from ..configs import AnimationConfig
from .utils import guess_mimetype, _calculate_downscale
from . import image
import io
import warnings
from PIL import Image as PILImage
from typing import Sequence


def encode_animation(
    data: bytes,
    configs: "list[AnimationConfig]",
    ) -> "Sequence[AnimationFile|ImageFile]":
    """Raises:
    - ValueError("Animation was too large")
    - ValueError("Could not Load Animation")
    - ValueError("Animation Only Has 1 Frame")
    """
    pillow = _open_pillow(data)
    return [encode_with_config(data, pillow, config) for config in configs]



def encode_single_animation(
    data: bytes,
    config: AnimationConfig,
    ) -> "AnimationFile|ImageFile":
    """Raises:
    - ValueError("Animation was too large")
    - ValueError("Could not Load Animation")
    - ValueError("Animation Only Has 1 Frame")
    """
    pillow = _open_pillow(data)
    return encode_with_config(data, pillow, config)


def encode_with_config(
        data: bytes,
        pillow: PILImage.Image,
        config: AnimationConfig
        ) -> "AnimationFile|ImageFile":
    if isinstance(config, configs.ThumbnailConfig):
        return encode_thumbnail_with_config(pillow, config)
    elif isinstance(config, configs.AnimationEncodeConfig):
        return encode_animation_with_animation_config(pillow, config)
    elif isinstance(config, configs.OriginalFileConfig):
        return encode_animation_with_originalfile_config(data, pillow)
    else:
        raise ValueError("Invalid encoding config")


def encode_animation_with_originalfile_config(
        data: bytes,
        pillow: PILImage.Image,
    ) -> AnimationFile:
    return AnimationFile(
        data=data,
        mimetype=guess_mimetype(data),
        height=pillow.height,
        width=pillow.width,
        frame_count=pillow.n_frames,
        duration=_get_animation_duration(pillow),
    )

def encode_animation_with_animation_config(
        pillow: PILImage.Image,
        config: configs.AnimationEncodeConfig
    ) -> AnimationFile:
    size = _calculate_downscale(
        current=(pillow.width, pillow.height),
        target=(config.width, config.height),
    )

    buf = io.BytesIO()
    (
    pillow.resize(
        size=size,
        resample=PILImage.LANCZOS,
    ).save(
        fp=buf,
        format='webp',
        save_all=True,  # Save as an animation
        transparency=0,
        duration=_get_frame_lengths(pillow),
        background=(0, 0, 0, 0),  # RGBA,
        disposal=2,
    )
    )

    return AnimationFile(
        data=buf.getvalue(),
        mimetype='image/webp',
        height=pillow.height,
        width=pillow.width,
        frame_count=pillow.n_frames,
        duration=_get_animation_duration(pillow),
    )


def encode_thumbnail_with_config(
        pillow: PILImage.Image,
        config: configs.ThumbnailConfig
        ) -> ImageFile:
    # Seek to the correct offset
    # TODO: Rewrite to be neater
    total_duration = _get_animation_duration(pillow)
    cur_frame_time = 0
    for x in range(pillow.n_frames):
        pillow.seek(x)
        cur_frame_time += pillow.info['duration']
        percentage_in = total_duration / cur_frame_time
        if percentage_in >= config.offset:
            break

    return image.encode_pillow_with_image_config(pillow, config)


def _open_pillow(data: bytes) -> PILImage.Image:
    buf = io.BytesIO(data)
    try:
        # formats=None attempt to load all formats
        pillow = PILImage.open(buf, formats=None)
    except PILImage.DecompressionBombError:
        raise ValueError("Animation was too large")
    except Exception:
        raise ValueError("Could not Load Animation")

    if pillow.n_frames == 1:
        raise ValueError("Animation Only Has 1 Frame")

    return pillow


def _get_animation_duration(pillow: PILImage.Image) -> int:
    "Get animation duration in milliseconds"
    return sum(_get_frame_lengths(pillow))


def _get_frame_lengths(pillow: PILImage.Image) -> "list[int]":
    frame_durations = []
    for x in range(pillow.n_frames):
        pillow.seek(x)
        duration = int(pillow.info['duration'])
        frame_durations.append(duration)

    return frame_durations
