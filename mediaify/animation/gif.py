from ..files import AnimationFile
from ..configs import (
    GIFEncodeConfig,
)
from ..resize import calculate_downscale
from .utils import (
    get_animation_duration_in_seconds,
    get_frame_lengths,
    extract_animation_frames,
    resize_animation,
)

import io
from PIL import Image as PILImage


def encode_as_gif(
        pillow: PILImage.Image,
        config: GIFEncodeConfig
        ) -> AnimationFile:
    frames = extract_animation_frames(pillow)
    frames = resize_animation(frames, config.resize)

    first_frame = frames[0]
    buf = io.BytesIO()
    first_frame.save(
        fp=buf,
        format='gif',
        save_all=True,  # Save as an animation
        append_images=frames[1:],
        duration=get_frame_lengths(pillow),
        optimize=True,
        loop=0,
    )

    return AnimationFile(
        data=buf.getvalue(),
        mimetype='image/gif',
        width=first_frame.width,
        height=first_frame.height,
        frame_count=pillow.n_frames,
        duration=get_animation_duration_in_seconds(pillow),
    )
