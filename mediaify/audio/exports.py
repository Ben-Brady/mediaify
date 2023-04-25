from ..files import AudioFile
from ..configs import AudioEncodingType
from .encode import encode_with_config
from typing import List


def encode_audio(
        data: bytes,
        config: "AudioEncodingType|None" = None,
        ) -> "AudioFile":
    """Encodes an image using an audio config

    Returns:
        ImageFile: The encoded image

    Raises:
        ValueError: Image is too big to process
        ValueError: Could not Load Image
    """
    return encode_with_config(data, config)


def batch_encode_audio(
        data: bytes,
        configs: "List[AudioEncodingType]",
        ) -> "List[AudioFile]":
    """Encodes an image using a list of audio configs,
    more efficent than calling `encode_audio` multiple times

    Returns:
        List[AudioFile]: List of encoded audio files, guarenteed to be in the same order as the configs

    Raises:
        ValueError: Could Not Encode Audio
    """
    return [encode_with_config(data, config) for config in configs]
