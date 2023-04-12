from . import FIRE_VIDEO, HEAVY_VIDEO
import mediaify
import pytest
import json
from pathlib import Path

def test_video():
    suite.addTest(unittest.makeSuite(test_Fire))
    suite.addTest(unittest.makeSuite(test_Heavy))
    return suite
class test_Heavy(unittest.TestCase):
    def setUp(self):
        self.info = test_data.heavy
        with open(self.info.file, 'rb') as f:
            data = f.read()
        with VideoEncoder(data) as vid:
            self.full = vid.original()
            self.preview = vid.preview()
            self.thumbnail = vid.thumbnail()

    def test_Preview_Isnt_Generated(self):
        assert self.preview == None

    def test_Thumbnail_is_Image(self):
        assert type(self.thumbnail) == ImageFile

    def test_Video_Metadata_Is_Correct(self):
        full = self.full
        assert full.height == self.info.height, full.height
        assert full.width == self.info.width, full.width
        assert full.framerate == self.info.framerate, full.framerate
        self.assertAlmostEqual(full.duration, self.info.duration, delta=0.1)
        assert full.mimetype == self.info.mimetype, full.mimetype
        assert full.hasAudio == self.info.hasAudio, full.hasAudio

    def test_Thumbnail_Visual_Test(self):
        with open(OutputLocation.thumbnail, 'wb') as f:
            f.write(self.thumbnail.data)

    def test_Thumbnail_is_generated_at_correct_point(self):
        with open(OutputLocation.thumbnail, 'wb') as f:
            f.write(self.thumbnail.data)

    def test_Full_Visual_Test(self):
        with open(OutputLocation.full, 'wb') as f:
            f.write(self.full.data)
