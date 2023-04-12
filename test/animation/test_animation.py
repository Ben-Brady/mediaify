import mediaify
from test.data import FRACTAL_ANIMATION, SINGLE_FRAME_ANIMATION, TRANSPARENT_ANIMATION
import pytest
import io
import unittest
from PIL import Image as PILImage


animation_config = mediaify.configs.GIFEncodeConfig(
    width=256,
    height=256,
    quality=90,
    lossless=True,
)


def load_PIL_from_bytes(data: bytes) -> PILImage.Image:
    buf = io.BytesIO(data)
    return PILImage.open(buf)


def test_Animations_Require_More_Than_One_Frame():
    with open(SINGLE_FRAME_ANIMATION.filepath, "rb") as f:
        data = f.read()

    with pytest.raises(ValueError):
        mediaify.image.encode_single_animation(data, animation_config)


@pytest.mark.skip("TODO: https://trello.com/c/p5Fv7jne/106-bug-fix-gif-encoding-strips-transparency")
def test_Animations_Preserve_Transparency():
    with open(TRANSPARENT_ANIMATION.filepath, 'rb') as f:
        data = f.read()

    animation = mediaify.image.encode_single_animation(data, animation_config)
    pillow = load_PIL_from_bytes(data)
    for x in range(pillow.n_frames):
        pillow.seek(x)
        RGB_MinMax_Values = pillow.getextrema()
        MaxTransparency = RGB_MinMax_Values[3][0]
        assert MaxTransparency != 255, f"Frame {x} is not transparent"


def test_animation_originalfile():
    ...


def test_animation_animationencode():
    ...


def test_animation_thumbnail():
    ...


# class test_Animation_Full(unittest.TestCase):
#     def setUp(self) -> None:
#         self.original_file = TestData.Transparent.file
#         with open(TestData.Transparent.file, 'rb') as f:
#             with AnimationEncoder(f.read()) as anim:
#                 self.full = anim.original()

#     def test_Is_AnimationFile(self):
#         assert isinstance(
#             self.full, AnimationFile), "Did not generate a full version correctly"

#     def test_Full_Is_Valid(self):
#         PIL = load_PIL_from_data(self.full.data)
#         PIL.verify()
#         assert PIL.is_animated, "Did not save as animation"

#     def test_Attributes_are_Correct(self):
#         assert self.full.frame_count == 128, f"Number of frames is not correct: {self.full.frame_count}"
#         assert self.full.duration == 6.4, f"File Duration is incorrect: {self.full.duration}"

#     def test_Save_Example_Image(self):
#         PIL = load_PIL_from_data(self.full.data)
#         PIL.save(OutputLocation.full, save_all=True)


# class test_Animation_Preview(unittest.TestCase):
#     def setUp(self) -> None:
#         self.original_file = TestData.Transparent.file
#         with open(TestData.Transparent.file, 'rb') as f:
#             with AnimationEncoder(f.read()) as anim:
#                 self.preview = anim.preview()

#     def test_Preview_isnt_Generated(self):
#         assert isinstance(
#             self.preview, ImageFile), "Animation Preview is not an Image"


# class test_Animation_Thumbnail(unittest.TestCase):
#     def setUp(self) -> None:
#         self.original_file = TestData.Transparent.file
#         with open(TestData.Transparent.file, 'rb') as f:
#             with AnimationEncoder(f.read()) as anim:
#                 self.thumbnail = anim.thumbnail()
#                 self.data = self.thumbnail.data

#     def test_Thumbnail_is_ImageFile(self):
#         assert isinstance(
#             self.thumbnail, ImageFile), "Did not generate a thumbnail version correctly"

#     def test_Thumbnail_Is_Correct_Resolution(self):
#         max_width = settings.THUMBNAIL_WIDTH
#         max_height = settings.THUMBNAIL_HEIGHT
#         width, height = self.thumbnail.width, self.thumbnail.height
#         assert (width == max_width) or (
#             height == max_height), f"Thumbnail is not the correct resolution: {width}x{height}"

#     def test_Thumbnail_Is_Valid(self):
#         PIL = load_PIL_from_data(self.data)
#         PIL.verify()

#     def test_Save_Example(self):
#         PIL = load_PIL_from_data(self.data)
#         PIL.save(OutputLocation.thumbnail)
