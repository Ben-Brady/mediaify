from dataclasses import dataclass


@dataclass
class TestImage:
    filepath: str
    mimetype: str
    width: int
    height: int


@dataclass
class TestAnimation:
    filepath: str
    mimetype: str
    width: int
    height: int
    duration: int


@dataclass
class TestVideo:
    filepath: str
    mimetype: str
    width: int
    height: int
    duration: float
    framerate: int
    hasAudio: bool


MASSIVE_IMAGE = TestImage(
    filepath="./data/test/image/Massive.webp",
    mimetype="image/webp",
    width=10000,
    height=10000,
)

SMALL_IMAGE = TestImage(
    filepath="./test/data/image/Small.webp",
    mimetype="image/webp",
    width=5,
    height=5,
)

COMPLEX_IMAGE = TestImage(
    filepath="./test/data/image/Complex.webp",
    mimetype="image/webp",
    width=2000,
    height=2000,
)

LANDSPACE_IMAGE = TestImage(
    filepath="./test/data/image/Landscape.webp",
    mimetype="image/webp",
    width=1600,
    height=840,
)

HEAVY_VIDEO = TestVideo(
    filepath="./test/data/video/Heavy.mp4",
    mimetype="video/mp4",
    width=1280,
    height=720,
    duration=13.83,
    framerate=24,
    hasAudio=True,
)

FIRE_VIDEO = TestVideo(
    filepath="./test/data/video/Fire.webm",
    mimetype="video/webm",
    width=492,
    height=360,
    duration=10.00,
    framerate=25,
    hasAudio=True,
)

TRANSPARENT_ANIMATION = TestAnimation(
    filepath="./test/data/animation/ricardo.gif",
    mimetype="image/gif",
    width=241,
    height=300,
    duration=6400,
)

SINGLE_FRAME_ANIMATION = TestAnimation(
    filepath="./test/data/animation/SingleFrame.gif",
    mimetype="image/gif",
    width=241,
    height=300,
    duration=50,
)

FRACTAL_ANIMATION = TestAnimation(
    filepath="./test/data/animation/fractal.gif",
    mimetype="image/gif",
    width=500,
    height=500,
    duration=600,
)
