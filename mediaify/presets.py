from .configs import (
    AnimationEncodeConfig,
    ImageEncodeConfig,
    ThumbnailConfig,
    OriginalFileConfig,
    ImageConfig,
    AnimationConfig,
    VideoConfig,
)


class Default:
    image: "list[ImageConfig]" = [
        ImageEncodeConfig(
            height=64,
            width=64,
            quality=80,
            lossless=False,
        ),
        ImageEncodeConfig(
            height=128,
            width=128,
            quality=80,
            lossless=False,
        ),
        ImageEncodeConfig(
            width=512,
            height=512,
            quality=90,
            lossless=False,
        ),
        ImageEncodeConfig(
            width=1024,
            height=1024,
            quality=90,
            lossless=False,
        ),
        OriginalFileConfig(),
    ]

    animation: "list[AnimationConfig]" = [
        ThumbnailConfig(
            height=128,
            width=128,
            quality=60,
            lossless=False,
        ),
        ThumbnailConfig(
            height=512,
            width=512,
            quality=70,
            lossless=False,
        ),
        AnimationEncodeConfig(
            width=256,
            height=256,
            quality=80,
            lossless=False,
        ),
        OriginalFileConfig(),
    ]

    video: "list[VideoConfig]" = [
        ThumbnailConfig(
            height=128,
            width=128,
            quality=80,
            lossless=False,
        ),
        ThumbnailConfig(
            height=512,
            width=512,
            quality=85,
            lossless=False,
        ),
        OriginalFileConfig(),
    ]

class SpaceSaving:
    image: "list[ImageConfig]" = [
        ImageEncodeConfig(
            height=64,
            width=64,
            quality=80,
            lossless=False,
        ),
        OriginalFileConfig(),
    ]

    animation: "list[AnimationConfig]" = [
        ThumbnailConfig(
            height=128,
            width=128,
            quality=60,
            lossless=False,
        ),
        OriginalFileConfig(),
    ]

    video: "list[VideoConfig]" = [
        ThumbnailConfig(
            height=128,
            width=128,
            quality=80,
            lossless=False,
        ),
        OriginalFileConfig(),
    ]


__all__ = [
    "Default",
    "SpaceSaving",
]
