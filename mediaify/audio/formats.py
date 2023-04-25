from ..files import AudioFile
from ..configs import FLACFormat, OpusFormat, MP3Format, WAVFormat, UnencodedEncoding, AudioEncodingType
from ..utils import guess_mimetype
from tempfile import NamedTemporaryFile
from ffmpeg import FFmpeg
from typing import Callable


def encode_as_original(data: bytes) -> AudioFile:
    return AudioFile(
        data=data,
        mimetype=guess_mimetype(data),
    )


def encode_as_mp3(data: bytes, config: MP3Format) -> AudioFile:
    def process(ffmpeg: FFmpeg) -> FFmpeg:
        return (
            ffmpeg
            .option("f", "mp3")
            .option("codec:a", "libmp3lame")
            .option("qscale:a", config.quality)
        )

    return encode_as_generic(data, process, "audio/mpeg")


def encode_as_opus(data: bytes, config: OpusFormat) -> AudioFile:
    def process(ffmpeg: FFmpeg) -> FFmpeg:
        return (
            ffmpeg
            .option("f", "opus")
            .option("codec:a", "libopus")
            .option("b:a", config.bitrate)
        )

    return encode_as_generic(data, process, "audio/opus")


def encode_as_flac(data: bytes, config: FLACFormat) -> AudioFile:
    def process(ffmpeg: FFmpeg) -> FFmpeg:
        return (
            ffmpeg
            .option("f", "flac")
        )

    return encode_as_generic(data, process, "audio/flac")


def encode_as_wav(data: bytes, config: WAVFormat) -> AudioFile:
    def process(ffmpeg: FFmpeg) -> FFmpeg:
        return (
            ffmpeg
            .option("f", "wav")
        )

    return encode_as_generic(data, process, "audio/wav")


def encode_as_generic(
        data: bytes,
        process_func: Callable[[FFmpeg], FFmpeg],
        mimetype: str,
        ) -> AudioFile:
    with NamedTemporaryFile("wb") as f:
        f.write(data)

        ffmpeg = (
            FFmpeg()
            .option("i", f.name)
            .output("pipe:")
        )
        ffmpeg = process_func(ffmpeg)
        output_data = ffmpeg.execute()

    return AudioFile(
        data=output_data,
        mimetype=mimetype,
    )
