from abc import ABCMeta

class ResizeConfig(metaclass=ABCMeta):
    pass


class AudioFormat(metaclass=ABCMeta):
    pass


class ImageFormat(metaclass=ABCMeta):
    resize: "ResizeConfig | None" = None
    "How to resize the image, None to disable resizing. Defaults to None."


class AnimationFormat(metaclass=ABCMeta):
    resize: "ResizeConfig | None" = None
    "How to resize the animation, None to disable resizing. Defaults to None."


class VideoFormat(metaclass=ABCMeta):
    resize: "ResizeConfig | None" = None
    "How to resize the video, None to disable resizing. Defaults to None."

