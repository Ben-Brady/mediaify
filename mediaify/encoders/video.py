from .. import VideoFile, ImageFile
from ..configs import OriginalFileConfig, ThumbnailConfig
from .image import encode_single_image
from .probe import VideoProbe
import ffmpeg # type: ignore
from tempfile import NamedTemporaryFile
from typing import Sequence


def encode_video(
        data: bytes,
        configs: "list[OriginalFileConfig|ThumbnailConfig]"
        ) -> "Sequence[VideoFile|ImageFile]":
    with NamedTemporaryFile("w+b") as f:
        f.write(data)
        probe = VideoProbe(f.name)
        return [
            encode_video_with_config(data, f.name, probe, config)
            for config in configs
        ]


def encode_single_video(
        data: bytes,
        config: "OriginalFileConfig|ThumbnailConfig"
        ) -> "VideoFile|ImageFile":
    with NamedTemporaryFile("w+b") as f:
        f.write(data)
        probe = VideoProbe(f.name)
        return encode_video_with_config(data, f.name, probe, config)


def encode_video_with_config(
        data: bytes,
        path: str,
        probe: VideoProbe,
        config: "OriginalFileConfig|ThumbnailConfig"
        ) -> "VideoFile|ImageFile":
    if isinstance(config, OriginalFileConfig):
        return encode_video_with_original_config(data, probe)
    elif isinstance(config, ThumbnailConfig):
        return encode_file_with_thumbnail_config(data, path, probe, config)
    else:
        raise ValueError("Invalid encoding config")


def encode_video_with_original_config(data: bytes, probe: VideoProbe) -> VideoFile:
    return VideoFile(
        data=data,
        mimetype=probe.mimetype,
        height=probe.height,
        width=probe.width,
        duration=probe.duration,
        framerate=probe.framerate,
        hasAudio=probe.audio,
    )


def encode_file_with_thumbnail_config(
        data: bytes,
        pathname: str,
        probe: VideoProbe,
        config: ThumbnailConfig
        ) -> ImageFile:
    offset = float(probe.duration * config.offset)
    if offset > probe.duration:
        offset = probe.duration

    try:
        data, err = (
            ffmpeg
            .input(pathname)
            .output(
                "pipe:",
                f='image2',
                vframes=1,
                ss=offset,
            )
            .run(
                input=data,
                capture_stdout=True,
                capture_stderr=True
            )
        )
    except ffmpeg.Error as e:
        raise ValueError(e.stderr)

    return encode_single_image(data, config)
