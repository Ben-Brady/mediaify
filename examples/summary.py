import mediaify

with open('./input/heavy.mp4', 'rb') as f:
    data = f.read()

summary = mediaify.encode_video(data, mediaify.AnimationSummaryConfig(
    frames=60,
    framerate=15,
    encoding=mediaify.WEBPAnimationEncodeConfig(
        width=320,
        height=320,
    ),
))


filepath = f"./output/summary{summary.ext}"
with open(filepath, "wb") as f:
    f.write(summary.data)

print(f"{summary} saved to {filepath}")
