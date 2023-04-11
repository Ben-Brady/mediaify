from .types import (
    GenericFile,
    AnimationFile,
    ImageFile,
    VideoFile,
    Dimensions
)
from . import encoders
from .utils import generate_encoder, encode_media

ACCEPTED_FILE_EXTENTIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".jpef",
    ".webp",
    ".apng",
    ".gif",
    ".webm",
    ".mp4",
}
