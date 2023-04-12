from ..files import AnimationFile
from ..configs import (
    GIFEncodeConfig,
)
from ..utils import calculate_downscale
from .utils import (
    get_animation_duration_in_seconds,
    get_frame_lengths,
    get_animation_frames,
)

import io
from PIL import Image as PILImage


# def encode_as_gif(
#         pillow: PILImage.Image,
#         config: GIFEncodeConfig
#         ) -> AnimationFile:
#     raise NotImplementedError("GIF encoding is not yet implemented")


def encode_as_gif(
        pillow: PILImage.Image,
        config: GIFEncodeConfig
        ) -> AnimationFile:
    size = calculate_downscale(
        current=(pillow.width, pillow.height),
        target=(config.width, config.height),
    )

    buf = io.BytesIO()
    pillow.resize(
        size=size,
        resample=PILImage.LANCZOS,
    ).save(
        fp=buf,
        format='gif',
        save_all=True,  # Save as an animation
        append_images=get_animation_frames(pillow),
        duration=get_frame_lengths(pillow.copy()),
        optimize=True,
        loop=0,
    )

    return AnimationFile(
        data=buf.getvalue(),
        mimetype='image/gif',
        height=pillow.height,
        width=pillow.width,
        frame_count=pillow.n_frames,
        duration=get_animation_duration_in_seconds(pillow),
    )
