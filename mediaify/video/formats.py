from ..configs import (
    MP4EncodeConfig,
    WEBMEncodeConfig,
    H264EncodeConfig,
    VP9EncodeConfig,
    OpusEncodeConfig,
)
from ..files import VideoFile
from .process import encode_generic_video
from .info import VideoInfo
from ffmpeg import FFmpeg


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
        config: MP4EncodeConfig,
        ) -> VideoFile:

    def save(ffmpeg: FFmpeg, filepath: str):
        params = {}

        video_codec = config.video_codec
        if isinstance(video_codec, H264EncodeConfig):
            params["c:v"] = "libx264"
            params["preset"] = video_codec.preset
            params["crf"] = video_codec.crf
        else:
            raise ValueError(f"Unsupported Video Codec: {type(video_codec).__name__}")

        audio_codec = config.audio_codec
        if isinstance(audio_codec, OpusEncodeConfig):
            params["c:a"] = "libopus"
            params["b:a"] = audio_codec.bitrate
        elif config.audio_codec is None:
            params["an"] = None
        else:
            raise ValueError(f"Unsupported Audio Codec: {type(audio_codec).__name__}")

        (ffmpeg
            .output(
                filepath,
                params,
                f='mp4',
            )
            .execute()
        )

    return encode_generic_video(data, pathname, info, config, save)


def encode_as_webm(
        data: bytes,
        pathname: str,
        info: VideoInfo,
        config: WEBMEncodeConfig,
        ) -> VideoFile:
    def save(ffmpeg: FFmpeg, filepath: str):
        params = {}

        video_codec = config.video_codec
        if isinstance(video_codec, VP9EncodeConfig):
            params["c:v"] = "libvpx-vp9"
            params["crf"] = video_codec.crf
            params["deadline"] = video_codec.preset
        else:
            raise ValueError(f"Unsupported Video Codec: {type(video_codec).__name__}")

        audio_codec = config.audio_codec
        if isinstance(audio_codec, OpusEncodeConfig):
            params["c:a"] = "libopus"
            params["b:a"] = str(audio_codec.bitrate)
        else:
            raise ValueError(f"Unsupported Audio Codec: {type(audio_codec).__name__}")

        (ffmpeg
            .output(
                filepath,
                params,
                f='webm',
            )
            .execute()
        )

    return encode_generic_video(data, pathname, info, config, save)
