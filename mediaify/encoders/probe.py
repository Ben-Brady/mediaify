import mimetypes
from typing import Any, Union
from magic import Magic
import ffmpeg # type: ignore


class VideoProbe:
    filepath: str
    data: bytes

    def __init__(self, filepath: str):
        with open(filepath, 'rb') as f:
            self.data = f.read()
        self.filepath = filepath
        self.probe_data = ffmpeg.probe(self.filepath)

    @property
    def video_stream(self) -> "dict[str, Any]":
        streams = self.probe_data['streams']
        video_streams = [x for x in streams if x['codec_type'] == 'video']
        if len(video_streams) == 1:
            return video_streams[0] # type: ignore
        else:
            raise Exception('No or Multiple Video Streams Found')

    @property
    def height(self) -> int:
        return int(self.video_stream['height'])

    @property
    def width(self) -> int:
        return int(self.video_stream['width'])

    @property
    def framerate(self) -> str:
        framerate = eval(self.video_stream['r_frame_rate'])
        if framerate % 1 == 0:
            framerate = int(framerate)

        return str(framerate)

    @property
    def mimetype(self) -> str:
        magic = Magic(mime=True)
        return magic.from_buffer(self.data)

    @property
    def extention(self) -> str:
        ext = mimetypes.guess_extension(self.mimetype)
        if isinstance(ext, str):
            return ext
        else:
            raise Exception("Couldn't Guess File Extention")

    @property
    def audio(self) -> bool:
        for stream in self.probe_data['streams']:
            if stream['codec_type'] == 'audio':
                return True
        return False

    @property
    def duration(self) -> float:
        return float(self.probe_data['format']['duration'])

    @property
    def frame_count(self) -> Union[float, None]:
        if 'nb_frames' in self.video_stream:
            return float(self.video_stream['nb_frames'])
        else:
            return None

