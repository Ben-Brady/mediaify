from ..configs import (
    VideoPreviewAnimationConfig,
)
from ..files import AnimationFile
from ..animation import encode_animation
from .info import VideoInfo
from tempfile import NamedTemporaryFile
from ffmpeg import FFmpeg, FFmpegError


def encode_as_animation_summary(
    data: bytes,
    pathname: str,
    info: VideoInfo,
    config: VideoPreviewAnimationConfig,
) -> AnimationFile:
    with NamedTemporaryFile(suffix=".gif") as f:
        try:
            (
                FFmpeg()
                .input(pathname)
                .option("vf", "setpts=PTS/{2}")  # set timescale
                .option("y", None)  # overwrite output
                .output(
                    f.name,
                    f="gif",
                    vframes=config.frames,
                    r=config.framerate,
                )
            )
        except FFmpegError as e:
            raise ValueError(str(e))

        f.seek(0)
        data = f.read()

    animation = encode_animation(data, config.encoding)
    if not isinstance(animation, AnimationFile):
        raise SystemError(
            "Animation Summary returned ImageFile instead of AnimationFile?"
        )

    return animation
