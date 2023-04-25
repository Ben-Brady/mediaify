from ..data import MONKEY_AUDIO
import mediaify
from mediaify import (
    AudioFile,
    MP3Format,
    OpusFormat,
    WAVFormat,
    FLACFormat,
    AudioEncodingType,
)
import pytest


def encode_file(filepath: str, config: AudioEncodingType) -> AudioFile:
    with open(filepath, 'rb') as f:
        data = f.read()

    return mediaify.encode_audio(data, config)


@pytest.mark.parametrize(
    ids=["mp3", "opus", "wav", "flac"],
    argnames="mimetype, config",
    argvalues=[
        ("audio/mpeg", MP3Format()),
        ("audio/opus", OpusFormat()),
        ("audio/wav", WAVFormat()),
        ("audio/flac", FLACFormat()),
    ],
)
def test_audio_encodes_successfully(mimetype, config):
    video = encode_file(MONKEY_AUDIO.filepath, config)

    assert len(video.data) != 0
    assert video.mimetype == mimetype
