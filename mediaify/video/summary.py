from ..configs import (
    AnimationSummaryConfig,
)
from ..files import AnimationFile
from ..animation import encode_animation
from .info import VideoInfo
from tempfile import NamedTemporaryFile
import ffmpeg  # type: ignore


def encode_as_animation_summary(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: AnimationSummaryConfig,
        ) -> AnimationFile:
    if info.frame_count is not None:
        timescale = min(4, max(1, info.frame_count / config.frames))
    else:
        timescale = 1.0

    with NamedTemporaryFile(suffix=".gif") as f:
        try:
            data, _ = (
                ffmpeg
                .input(pathname)
                .filter(
                    "setpts",
                    f"PTS/{2}"
                )
                .output(
                    f.name,
                    f='gif',
                    vframes=config.frames,
                    r=config.framerate,
                )
                .overwrite_output()
                .run(
                    capture_stderr=True,
                )
            )
        except ffmpeg.Error as e:
            raise ValueError(e.stderr.decode())

        f.seek(0)
        data = f.read()

    animation = encode_animation(data, config.encoding)
    if not isinstance(animation, AnimationFile):
        raise SystemError("Animation Summary returned ImageFile instead of AnimationFile?")

    return animation
