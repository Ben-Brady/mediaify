from ..files import VideoFile, AnimationFile, ImageFile
from ..configs import VideoConfig
from ..presets import Default
from .info import get_video_info
from .encode import encode_video_with_config, encode_as_original
from tempfile import NamedTemporaryFile
from typing import List


def load_video(data: bytes) -> "VideoFile":
    with NamedTemporaryFile() as f:
        f.write(data)
        info = get_video_info(f.name)

    return encode_as_original(data, info)


def encode_video(
        data: bytes,
        config: "VideoConfig" = Default.video,
        ) -> "VideoFile|AnimationFile|ImageFile":
    with NamedTemporaryFile() as f:
        f.write(data)
        info = get_video_info(f.name)
        return encode_video_with_config(data, f.name, info, config)


def batch_encode_video(
        data: bytes,
        configs: "List[VideoConfig]" = Default.batch_video,
        ) -> "List[VideoFile|AnimationFile|ImageFile]":
    with NamedTemporaryFile() as f:
        f.write(data)
        info = get_video_info(f.name)
        return [
            encode_video_with_config(data, f.name, info, config)
            for config in configs
        ]
