from ..files import AudioFile
from ..configs import (
    FLACFormat,
    WAVFormat,
    OpusFormat,
    MP3Format,
    UnencodedEncoding,
    AudioEncodingType,
)
from .formats import (
    encode_as_original,
    encode_as_mp3,
    encode_as_opus,
    encode_as_flac,
    encode_as_wav,
)

def encode_with_config(
        data: bytes,
        config: "AudioEncodingType|None",
        ) -> AudioFile:
    if isinstance(config, UnencodedEncoding) or config is None:
        return encode_as_original(data)
    elif isinstance(config, MP3Format):
        return encode_as_mp3(data, config)
    elif isinstance(config, FLACFormat):
        return encode_as_flac(data, config)
    elif isinstance(config, WAVFormat):
        return encode_as_wav(data, config)
    elif isinstance(config, OpusFormat):
        return encode_as_opus(data, config)
    else:
        raise ValueError(f"Unknown encoding type: {config}")
