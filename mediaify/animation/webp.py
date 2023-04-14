from ..files import AnimationFile
from ..configs import (
    WEBPAnimationEncodeConfig,
)
from ..resize import calculate_downscale
from .utils import (
    get_animation_duration_in_seconds,
    get_frame_lengths,
    extract_animation_frames,
)

import io
from PIL import Image as PILImage, features as PILFeatures


def encode_as_webp(
        pillow: PILImage.Image,
        config: WEBPAnimationEncodeConfig,
        ) -> AnimationFile:
    if not PILFeatures.check("webp_anim"):
        raise RuntimeError("WebP animation support not available, WeBP library outdated?")

    frames = extract_animation_frames(pillow)

    if config.resize is not None:
        im_size = (pillow.width, pillow.height)
        size = calculate_downscale(im_size, config.resize)
        frames = [
            frame.resize(size, PILImage.LANCZOS)
            for frame in frames
        ]

    first_frame = frames[0]
    buf = io.BytesIO()
    first_frame.save(
        fp=buf,
        format='webp',
        lossless=config.lossless,
        quality=config.quality,
        allow_mixed=not config.lossless,  # Allow mixed lossy/lossless frames
        minimize_size=True,

        save_all=True,  # Save as an animation
        append_images=frames[1:],
        transparency=0,
        duration=get_frame_lengths(pillow),
        background=(0, 0, 0, 0),  # Transparent background
        disposal=2,
    )

    return AnimationFile(
        data=buf.getvalue(),
        mimetype='image/webp',
        width=first_frame.width,
        height=first_frame.height,
        frame_count=pillow.n_frames,
        duration=get_animation_duration_in_seconds(pillow),
    )
