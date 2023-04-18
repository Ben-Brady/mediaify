from ..files import VideoFile, AnimationFile, ImageFile
from ..configs import VideoConfig
from ..presets import Default
from .info import get_video_info
from .encode import encode_video_with_config, encode_as_original
from tempfile import NamedTemporaryFile
from typing import List


def load_video(data: bytes) -> VideoFile:
    """
    Loads a video without any processing,
    identical to `encode_video(data, UnencodedConfig())`

    Returns:
        VideoFile: The loaded video

    Raises:
        ValueError: Video could not be encoded
    """
    with NamedTemporaryFile() as f:
        f.write(data)
        info = get_video_info(f.name)

    return encode_as_original(data, info)


def encode_video(
        data: bytes,
        config: "VideoConfig|None" = None,
        ) -> "VideoFile|AnimationFile|ImageFile":
    """Encodes a video using a VideoConfig

    Returns:
        VideoFile|AnimationFile|ImageFile: The encoded output

    Raises:
        ValueError: Video could not be encoded
    """
    config = config or Default.video
    with NamedTemporaryFile() as f:
        f.write(data)
        info = get_video_info(f.name)
        return encode_video_with_config(data, f.name, info, config)


def batch_encode_video(
        data: bytes,
        configs: "List[VideoConfig]|None" = None,
        ) -> "List[VideoFile|AnimationFile|ImageFile]":
    """
    Encodes a video using a list of VideoConfigs,
    more efficent than calling `encode_video` multiple times

    Returns:
        List[VideoFile|AnimationFile|ImageFile]: List of encoded output, guarenteed to be in the same order as the configs

    Raises:
        ValueError: Video could not be encoded
    """
    configs = configs or Default.batch_video
    with NamedTemporaryFile() as f:
        f.write(data)
        info = get_video_info(f.name)
        return [
            encode_video_with_config(data, f.name, info, config)
            for config in configs
        ]
