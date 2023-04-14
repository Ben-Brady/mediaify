import mediaify

with open('./input/heavy.mp4', 'rb') as f:
    data = f.read()

config = mediaify.AnimationSummaryConfig(
    frames=60,
    framerate=15,
    encoding=mediaify.WEBPAnimationEncodeConfig(
        resize=mediaify.ResizeConfig(
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
