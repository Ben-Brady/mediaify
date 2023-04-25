from dataclasses import dataclass


@dataclass
class TestAudio:
    filepath: str
    mimetype: str
    duration: float
    sample_rate: int


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
    framerate: float
    hasAudio: bool


MONKEY_AUDIO = TestAudio(
    filepath="./tests/data/audio/monkey.mp3",
    mimetype="image/webp",
    duration=158.34,
    sample_rate=44100,
)


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

KFC_VIDEO = TestVideo(
    filepath="./tests/data/video/kfc.mp4",
    mimetype="video/mp4",
    width=426,
    height=240,
    duration=5.99,
    framerate=29.97,
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

RICARDO_ANIMATION = TestAnimation(
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
