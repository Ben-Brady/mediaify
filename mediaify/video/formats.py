from ..configs import (
    MP4Format,
    WEBMFormat,
    H264Codec,
    VP9Codec,
    OpusCodec,
    AV1Codec,
)
from ..files import VideoFile
from .process import encode_generic_video
from .info import VideoInfo
from .codecs import (
    apply_av1_codec,
    apply_vp9_codec,
    apply_h264_codec,
    apply_opus_codec,
    apply_no_audio,
)
from ffmpeg import FFmpeg  # type: ignore
from typing import TypeVar, Type, Callable


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
    def process(ffmpeg: FFmpeg) -> FFmpeg:
        VIDEO_CODECS = {
            AV1Codec: apply_av1_codec,
            H264Codec: apply_h264_codec,
        }
        AUDIO_CODECS = {
            OpusCodec: apply_opus_codec,
            type(None): apply_no_audio,
        }

        ffmpeg = ffmpeg.option("f", "mp4")
        ffmpeg = apply_codec(ffmpeg, VIDEO_CODECS, config.video_codec)
        ffmpeg = apply_codec(ffmpeg, AUDIO_CODECS, config.audio_codec)
        return ffmpeg

    return encode_generic_video(
        pathname,
        info,
        encoding_name=repr(config),
        framerate=config.framerate,
        resize_config=config.resize,
        process_func=process,
    )


def encode_as_webm(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: WEBMFormat,
        ) -> VideoFile:
    def process(ffmpeg: FFmpeg) -> FFmpeg:
        VIDEO_CODECS = {
            AV1Codec: apply_av1_codec,
            VP9Codec: apply_vp9_codec,
        }
        AUDIO_CODECS = {
            OpusCodec: apply_opus_codec,
            type(None): apply_no_audio,
        }

        ffmpeg = ffmpeg.option("f", "webm")
        ffmpeg = apply_codec(ffmpeg, VIDEO_CODECS, config.video_codec)
        ffmpeg = apply_codec(ffmpeg, AUDIO_CODECS, config.audio_codec)
        return ffmpeg

    return encode_generic_video(
        pathname,
        info,
        encoding_name=repr(config),
        framerate=config.framerate,
        resize_config=config.resize,
        process_func=process,
    )


T = TypeVar("T")

def apply_codec(
        ffmpeg: FFmpeg,
        supported_configs: dict[Type[T], Callable[[FFmpeg, T], FFmpeg]],
        config: T
        ) -> FFmpeg:
    encoder = supported_configs.get(type(config), None)
    if encoder is None:
        raise ValueError(f"Unsupported Codec: {type(config)}")

    return encoder(ffmpeg, config)

