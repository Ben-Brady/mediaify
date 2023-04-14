from .configs import (
    ResizeConfig,
    WEBPImageEncodeConfig,
    WEBPAnimationEncodeConfig,
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
            resize=ResizeConfig(
                max_height=64,
                max_width=64,
            ),
            quality=60,
        )
    ),
    ThumbnailConfig(
        offset=0.2,
        encoding=WEBPImageEncodeConfig(
            resize=ResizeConfig(
                max_height=128,
                max_width=128,
            ),
            quality=70,
        )
    ),
    ThumbnailConfig(
        offset=0.2,
        encoding=WEBPImageEncodeConfig(
            resize=ResizeConfig(
                max_height=256,
                max_width=256,
            ),
            quality=80,
        )
    ),
    ThumbnailConfig(
        offset=0.2,
        encoding=WEBPImageEncodeConfig(
            resize=ResizeConfig(
                max_height=512,
                max_width=512,
            ),
            quality=80,
        )
    ),
]


class Default:
    image: "ImageConfig" = WEBPImageEncodeConfig(quality=95)
    animation: "AnimationConfig" = WEBPAnimationEncodeConfig(quality=90)
    video: "VideoConfig" = UnencodedConfig()

    batch_image = list(_default_thumbnails + [
        WEBPImageEncodeConfig(
            resize=ResizeConfig(
                max_width=1024,
                max_height=1024,
            ),
            quality=90,
        ),
        UnencodedConfig(),
    ])
    batch_animation = list(_default_thumbnails + [UnencodedConfig()])
    batch_video = list(_default_thumbnails + [UnencodedConfig()])

__all__ = [
    "Default",
]
