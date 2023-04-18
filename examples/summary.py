import mediaify
from mediaify.configs import (
    VideoPreviewAnimationConfig,
    WEBPAnimationEncodeConfig,
    ResizeConfig,
)

with open('./input/heavy.mp4', 'rb') as f:
    data = f.read()

config = VideoPreviewAnimationConfig(
    frames=60,
    framerate=15,
    encoding=WEBPAnimationEncodeConfig(
        resize=ResizeConfig(
            width=192,
            height=108,
        ),
        quality=70,
    )
)

summary = mediaify.encode_video(data, config)


filepath = f"./output/summary{summary.ext}"
with open(filepath, "wb") as f:
    f.write(summary.data)

print(f"{summary} saved to {filepath}")
