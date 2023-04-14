from ..files import AnimationFile
from ..configs import (
    WEBPAnimationEncodeConfig,
)
from ..resize import calculate_downscale
from .utils import (
    get_animation_duration_in_seconds,
    get_frame_lengths,
    get_animation_frames,
)

import io
from PIL import Image as PILImage, features as PILFeatures


def encode_as_webp(
        pillow: PILImage.Image,
        config: WEBPAnimationEncodeConfig,
        ) -> AnimationFile:
    if not PILFeatures.check("webp_anim"):
        raise RuntimeError("WebP animation support not available, WeBP library outdated?")

    if config.resize is not None:
        im_size = (pillow.width, pillow.height)
        size = calculate_downscale(im_size, config.resize)
        pillow = pillow.resize(size, PILImage.LANCZOS)

    buf = io.BytesIO()
    pillow.save(
        fp=buf,
        format='webp',
        lossless=config.lossless,
        quality=config.quality,
        save_all=True,  # Save as an animation
        transparency=0,
        duration=get_frame_lengths(pillow),
        background=(0, 0, 0, 0),  # Transparent background
        minimize_size=True,
        allow_mixed=not config.lossless,
        disposal=2,
    )

    return AnimationFile(
        data=buf.getvalue(),
        mimetype='image/webp',
        width=pillow.width,
        height=pillow.height,
        frame_count=pillow.n_frames,
        duration=get_animation_duration_in_seconds(pillow),
    )
