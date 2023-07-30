from typing_extensions import Literal
import mediaify
from . import data
import pytest

def test_encode_file():
    with open(data.SINGLE_FRAME_ANIMATION.filepath, 'rb') as f:
        file_data = f.read()

    file = mediaify.encode_file(file_data, mediaify.ThumbnailEncoding())
    assert isinstance(file, mediaify.ImageFile)
