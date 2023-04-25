from ..files import AnimationFile
from ..configs import (
    GIFFormat,
    WEBPAnimationFormat,
    ResizeConfig
)
from .utils import (
    get_animation_duration_in_seconds,
    get_frame_lengths,
    extract_animation_frames,
    resize_animation,
)
from PIL import Image as PILImage, features as PILFeatures
import io
from typing import Callable


def encode_as_gif(
        pillow: PILImage.Image,
        config: GIFFormat
        ) -> AnimationFile:
    def save_gif(
            buf: io.BytesIO,
            pillow: PILImage.Image,
            frames: list[PILImage.Image]
            ) -> None:
        frames[0].save(
            fp=buf,
            format='gif',
            save_all=True,  # Save as an animation
            append_images=frames[1:],
            duration=get_frame_lengths(pillow),
            optimize=True,
            disposal=2,
            loop=0,
        )

    return encode_as_generic(pillow, config.resize, save_gif, 'image/gif')


def encode_as_webp(
        pillow: PILImage.Image,
        config: WEBPAnimationFormat,
        ) -> AnimationFile:
    if not PILFeatures.check("webp_anim"):  #type: ignore
        raise RuntimeError("WebP animation support not available, WeBP library outdated?")
    def save_webp(
            buf: io.BytesIO,
            pillow: PILImage.Image,
            frames: list[PILImage.Image]
            ) -> None:
        frames[0].save(
            fp=buf,
            format='webp',
            lossless=config.lossless,
            quality=config.quality,

            save_all=True,  # Save as an animation
            loop=0,
            append_images=frames[1:],
            duration=get_frame_lengths(pillow),
            transparency=0,
            minimize_size=True,
            allow_mixed=not config.lossless,  # Allow mixed lossy/lossless frames
        )

    return encode_as_generic(pillow, config.resize, save_webp, 'image/webp')


def encode_as_generic(
        pillow: PILImage.Image,
        resize: "ResizeConfig|None",
        save_function: Callable[[io.BytesIO, PILImage.Image, list[PILImage.Image]], None],
        mimetype: str,
        ) -> AnimationFile:
    frames = extract_animation_frames(pillow)
    frames = resize_animation(frames, resize)

    buf = io.BytesIO()
    save_function(buf, pillow, frames)

    return AnimationFile(
        data=buf.getvalue(),
        mimetype=mimetype,
        width=frames[0].width,
        height=frames[0].height,
        frame_count=pillow.n_frames,
        duration=get_animation_duration_in_seconds(pillow),
    )
