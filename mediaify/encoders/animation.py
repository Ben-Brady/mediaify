from .. import AnimationFile, ImageFile, configs
from . import image
import io
import warnings
from PIL import Image as PILImage

warnings.simplefilter('ignore', PILImage.DecompressionBombWarning)
PILImage.MAX_IMAGE_PIXELS = (5000 * 5000) * 2
# x2 max pixels, warning is raised on MAX_IMAGE_PIXELS

def encode_animation(
    data: bytes,
    encodings: """list[
        configs.AnimationConfig|
        configs.ThumbnailConfig|
        configs.VideoConfig
    ]""",
    ) -> "list[AnimationFile|ImageFile]":
    """Raises:
    - ValueError("Animation was too large")
    - ValueError("Could not Load Animation")
    - ValueError("Animation Only Has 1 Frame")
    """
    buf = io.BytesIO(data)
    try:
        pillow = PILImage.open(buf, formats=None)
        # formats=None attempt to load all formats
    except PILImage.DecompressionBombError:
        raise ValueError("Animation was too large")
    except Exception:
        raise ValueError("Could not Load Animation")
    if pillow.n_frames == 1:
        raise ValueError("Animation Only Has 1 Frame")

    media = []
    for encoding in encodings:
        if isinstance(encoding, configs.ThumbnailConfig):
            media.append(encode_thumbnail_with_config(pillow, encoding))
        elif isinstance(encoding, configs.AnimationConfig):
            media.append(encode_animation_with_config(pillow, encoding))
        elif isinstance(encoding, configs.VideoConfig):
            raise NotImplementedError("Video Encoding Not Implemented")

    return media


def encode_animation_with_config(pillow: PILImage.Image, config: configs.AnimationConfig) -> AnimationFile:
    buf = io.BytesIO()
    pillow.save(
        fp=buf,
        format='webp',
        save_all=True,  # Save as an animation
        transparency=0,
        duration=get_frame_lengths(pillow),
        background=(0, 0, 0, 0),  # RGBA,
        disposal=2,
    )

    return AnimationFile(
        data=buf.getvalue(),
        mimetype='image/webp',
        height=pillow.height,
        width=pillow.width,
        frame_count=pillow.n_frames,
        duration=get_animation_duration(pillow),
    )


def encode_thumbnail_with_config(pillow: PILImage.Image, config: configs.ThumbnailConfig) -> ImageFile:
    # Seek to the correct offset
    # TODO: Rewrite to be neater
    total_duration = get_animation_duration(pillow)
    cur_frame_time = 0
    for x in range(pillow.n_frames):
        pillow.seek(x)
        cur_frame_time += pillow.info['duration']
        percentage_in = total_duration / cur_frame_time
        if percentage_in >= config.offset:
            break

    return image.encode_with_config(pillow, config)


def get_animation_duration(pillow: PILImage.Image) -> int:
    "Get animation duration in milliseconds"
    return sum(get_frame_lengths(pillow))


def get_frame_lengths(pillow: PILImage.Image) -> "list[int]":
    frame_durations = []
    for x in range(pillow.n_frames):
        pillow.seek(x)
        duration = int(pillow.info['duration'])
        frame_durations.append(duration)

    return frame_durations
