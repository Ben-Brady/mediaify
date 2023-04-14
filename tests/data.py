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
    frame_count: int


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
    filepath="./data/tests/image/massive.webp",
    mimetype="image/webp",
    width=10000,
    height=10000,
)

SMALL_IMAGE = TestImage(
    filepath="./tests/data/image/small.webp",
    mimetype="image/webp",
    width=5,
    height=5,
)

COMPLEX_IMAGE = TestImage(
    filepath="./tests/data/image/complex.webp",
    mimetype="image/webp",
    width=2000,
    height=2000,
)

LANDSPACE_IMAGE = TestImage(
    filepath="./tests/data/image/landscape.webp",
    mimetype="image/webp",
    width=1600,
    height=840,
)

HEAVY_VIDEO = TestVideo(
    filepath="./tests/data/video/heavy.mp4",
    mimetype="video/mp4",
    width=1280,
    height=720,
    duration=13.83,
    framerate=24,
    hasAudio=True,
)

FIRE_VIDEO = TestVideo(
    filepath="./tests/data/video/fire.webm",
    mimetype="video/webm",
    width=492,
    height=360,
    duration=10.00,
    framerate=25,
    hasAudio=True,
)

TRANSPARENT_ANIMATION = TestAnimation(
    filepath="./tests/data/animation/ricardo.gif",
    mimetype="image/gif",
    width=241,
    height=300,
    frame_count=128,
)

SINGLE_FRAME_ANIMATION = TestAnimation(
    filepath="./tests/data/animation/single_frame.gif",
    mimetype="image/gif",
    width=241,
    height=300,
    frame_count=1,
)

FRACTAL_ANIMATION = TestAnimation(
    filepath="./tests/data/animation/fractal.gif",
    mimetype="image/gif",
    width=500,
    height=500,
    frame_count=12,
)
