from ..files import AnimationFile
from ..configs import (
    WEBPAnimationEncodeConfig,
)
from ..utils import calculate_downscale
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

    size = calculate_downscale(
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
    )

    return AnimationFile(
        data=buf.getvalue(),
        mimetype='image/webp',
        height=pillow.height,
        width=pillow.width,
        frame_count=pillow.n_frames,
        duration=get_animation_duration_in_seconds(pillow),
    )
