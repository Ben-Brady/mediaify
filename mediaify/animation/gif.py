from ..files import AnimationFile
from ..configs import (
    GIFEncodeConfig,
)
from ..resize import calculate_downscale
from .utils import (
    get_animation_duration_in_seconds,
    get_frame_lengths,
    get_animation_frames,
)

import io
from PIL import Image as PILImage


def encode_as_gif(
        pillow: PILImage.Image,
        config: GIFEncodeConfig
        ) -> AnimationFile:
    if config.resize is not None:
        im_size = (pillow.width, pillow.height)
        size = calculate_downscale(im_size, config.resize)
        pillow = pillow.resize(size, PILImage.LANCZOS)

    buf = io.BytesIO()
    pillow.save(
        fp=buf,
        format='gif',
        save_all=True,  # Save as an animation
        append_images=get_animation_frames(pillow),
        duration=get_frame_lengths(pillow),
        optimize=True,
        loop=0,
    )

    return AnimationFile(
        data=buf.getvalue(),
        mimetype='image/gif',
        width=pillow.width,
        height=pillow.height,
        frame_count=pillow.n_frames,
        duration=get_animation_duration_in_seconds(pillow),
    )
