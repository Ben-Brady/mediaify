from .configs import (
    WEBPImageEncodeConfig,
    ThumbnailConfig,
    UnencodedConfig,
    ImageConfig,
    AnimationConfig,
    VideoConfig,
)
from typing import List

_default_thumbnails = [
    ThumbnailConfig(
        offset=0.2,
        encoding=WEBPImageEncodeConfig(
            height=64,
            width=64,
            quality=60,
            lossless=False,
        )
    ),
    ThumbnailConfig(
        offset=0.2,
        encoding=WEBPImageEncodeConfig(
            height=128,
            width=128,
            quality=60,
            lossless=False,
        )
    ),
    ThumbnailConfig(
        offset=0.2,
        encoding=WEBPImageEncodeConfig(
            height=256,
            width=256,
            quality=80,
            lossless=False,
        )
    ),
    ThumbnailConfig(
        offset=0.2,
        encoding=WEBPImageEncodeConfig(
            height=512,
            width=512,
            quality=80,
            lossless=False,
        )
    ),
]


class Default:
    image: "ImageConfig" = WEBPImageEncodeConfig(
        width=1024,
        height=1024,
        quality=90,
        lossless=False,
    )
    animation: "AnimationConfig" = UnencodedConfig()
    video: "VideoConfig" = UnencodedConfig()

    batch_image = list(_default_thumbnails + [
        WEBPImageEncodeConfig(
            width=1024,
            height=1024,
            quality=90,
            lossless=False,
        ),
        UnencodedConfig(),
    ])
    batch_animation = list(_default_thumbnails + [
        UnencodedConfig(),
    ])
    batch_video = list(_default_thumbnails + [
        UnencodedConfig(),
    ])


class SpaceSaving:
    image: "List[ImageConfig]" = [
        ThumbnailConfig(
            offset=0.2,
            encoding=WEBPImageEncodeConfig(
                height=128,
                width=128,
                quality=70
            )
        ),
        UnencodedConfig(),
    ]

    animation: "List[AnimationConfig]" = [
        ThumbnailConfig(
            offset=0.2,
            encoding=WEBPImageEncodeConfig(
                height=128,
                width=128,
                quality=70
            )
        ),
        UnencodedConfig(),
    ]

    video: "List[VideoConfig]" = [
        ThumbnailConfig(
            offset=0.2,
            encoding=WEBPImageEncodeConfig(
                height=128,
                width=128,
                quality=70
            )
        ),
        UnencodedConfig(),
    ]


__all__ = [
    "Default",
    "SpaceSaving",
]
