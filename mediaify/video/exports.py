from ..files import VideoFile, AnimationFile, ImageFile
from ..configs import (
    VideoEncodingType,
    ThumbnailEncoding,
    VideoPreviewAnimationEncoding,
    UnencodedEncoding,
    VideoFormat
)
from .info import get_video_info
from .encode import encode_video_with_config
from tempfile import NamedTemporaryFile
from typing import List, overload


@overload
def encode_video(
        data: bytes,
        config: "ThumbnailEncoding",
        ) -> "ImageFile":
    ...


@overload
def encode_video(
        data: bytes,
        config: "VideoPreviewAnimationEncoding",
        ) -> "AnimationFile":
    ...


@overload
def encode_video(
        data: bytes,
        config: "VideoFormat|UnencodedEncoding|None",
        ) -> "VideoFile":
    ...


def encode_video(
        data: bytes,
        config: "VideoEncodingType|None" = None,
        ) -> "VideoFile|AnimationFile|ImageFile":
    """Encodes a video using a video config

    Returns:
        VideoFile|AnimationFile|ImageFile: The encoded output

    Raises:
        ValueError: Video could not be encoded
    """
    with NamedTemporaryFile() as f:
        f.write(data)
        info = get_video_info(f.name)
        return encode_video_with_config(data, f.name, info, config)


def batch_encode_video(
        data: bytes,
        configs: "List[VideoEncodingType]",
        ) -> "List[VideoFile|AnimationFile|ImageFile]":
    """
    Encodes a video using a list of video configs,
    more efficent than calling `encode_video` multiple times

    Returns:
        List[VideoFile|AnimationFile|ImageFile]: List of encoded output, guarenteed to be in the same order as the configs

    Raises:
        ValueError: Video could not be encoded
    """
    with NamedTemporaryFile() as f:
        f.write(data)
        info = get_video_info(f.name)
        return [
            encode_video_with_config(data, f.name, info, config)
            for config in configs
        ]
