from ..files import VideoFile, AnimationFile, ImageFile
from ..configs import (
    VideoEncodingType,
    UnencodedEncoding,
    ThumbnailEncoding,
    WEBMFormat,
    MP4Format,
    VideoPreviewAnimationEncoding,
)
from .info import VideoInfo
from .thumbnail import encode_as_thumbnail
from .summary import encode_as_animation_summary
from .codecs import generate_video_options, generate_audio_options
from .process import encode_generic_video


def encode_video_with_config(
    data: bytes, path: str, info: VideoInfo, config: "VideoEncodingType|None"
) -> "VideoFile|AnimationFile|ImageFile":
    if isinstance(config, UnencodedEncoding) or config is None:
        return encode_as_original(data, info)
    elif isinstance(config, WEBMFormat):
        return encode_as_webm(data, path, info, config)
    elif isinstance(config, MP4Format):
        return encode_as_mp4(data, path, info, config)
    elif isinstance(config, ThumbnailEncoding):
        return encode_as_thumbnail(data, path, info, config)
    elif isinstance(config, VideoPreviewAnimationEncoding):
        return encode_as_animation_summary(data, path, info, config)
    else:
        raise ValueError("Invalid encoding config")


def encode_as_original(data: bytes, info: VideoInfo) -> VideoFile:
    return VideoFile(
        data=data,
        mimetype=info.mimetype,
        height=info.height,
        width=info.width,
        duration=info.duration,
        framerate=info.framerate,
        hasAudio=info.hasAudio,
    )


def encode_as_mp4(
    data: bytes,
    pathname: str,
    info: VideoInfo,
    config: MP4Format,
) -> VideoFile:
    options = {"f": "mp4"}
    options.update(generate_video_options(config.video_codec))
    options.update(generate_audio_options(config.audio_codec))

    return encode_generic_video(
        pathname,
        info,
        framerate=config.framerate,
        resize_config=config.resize,
        options=options,
    )


def encode_as_webm(
    data: bytes,
    pathname: str,
    info: VideoInfo,
    config: WEBMFormat,
) -> VideoFile:
    options = {"f": "webm"}
    options.update(generate_video_options(config.video_codec))
    options.update(generate_audio_options(config.audio_codec))

    return encode_generic_video(
        pathname,
        info,
        framerate=config.framerate,
        resize_config=config.resize,
        options=options,
    )
