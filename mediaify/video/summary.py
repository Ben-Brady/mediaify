from ..configs import (
    VideoPreviewAnimationEncoding,
)
from ..files import AnimationFile
from ..animation import encode_animation
from .info import VideoInfo
from .process import resize_video
from tempfile import NamedTemporaryFile
from ffmpeg import FFmpeg, FFmpegError  # type: ignore


def encode_as_animation_summary(
    data: bytes,
    pathname: str,
    info: VideoInfo,
    config: VideoPreviewAnimationEncoding,
) -> AnimationFile:
    if config.frames > info.frame_count:
        frame_count = info.frame_count
        timescale = 1.
    else:
        frame_count = config.frames
        timescale = min(2, info.frame_count / config.frames)

    ffmpeg = (
        FFmpeg()
        .option("i", pathname)
        .option("f", "gif")
        .option("frames", frame_count)
        .option("r", config.framerate)
        .option("vf", f"setpts=PTS/{timescale}")
    )
    if config.encoding and config.encoding.resize:
        ffmpeg = resize_video(ffmpeg, info, config.encoding.resize)

    try:
        out_data = ffmpeg.output("pipe:").execute()
    except FFmpegError as e:
        raise ValueError(str(e))
    else:
        animation = encode_animation(out_data, config.encoding)

        if not isinstance(animation, AnimationFile):
            raise ValueError("Animation Summary encoded with ImageConfig")

        return animation
