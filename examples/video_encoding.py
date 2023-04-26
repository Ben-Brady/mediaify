import mediaify

with open('./examples/input/video.mp4', 'rb') as f:
    data = f.read()


thumbnail = mediaify.ThumbnailEncoding(
    encoding=mediaify.WEBPImageFormat(
        resize=mediaify.TargetResolutionResize(width=640, height=360),
        quality=80,
    ),
)
preview = mediaify.VideoPreviewAnimationEncoding(
    encoding=mediaify.WEBPAnimationFormat(
        quality=50,
        lossless=False,
        resize=mediaify.TargetResolutionResize(width=640, height=360)
    ),
    framerate=5,
    frames=60,
)
video_144p = mediaify.WEBMFormat(
    video_codec=mediaify.AV1Codec(crf=55, preset=8),
    audio_codec=mediaify.OpusCodec(bitrate=128_000),
    resize=mediaify.TargetResolutionResize(width=256, height=144),
)
video_360p = mediaify.WEBMFormat(
    video_codec=mediaify.AV1Codec(crf=50, preset=7),
    audio_codec=mediaify.OpusCodec(bitrate=128_000),
    resize=mediaify.TargetResolutionResize(width=640, height=360),
)
video_720p = mediaify.WEBMFormat(
    video_codec=mediaify.AV1Codec(crf=45, preset=6),
    audio_codec=mediaify.OpusCodec(bitrate=128_000),
    resize=mediaify.TargetResolutionResize(width=1280, height=720),
)
fallback = mediaify.MP4Format(
    video_codec=mediaify.H264Codec(crf=21, preset="slow"),
    audio_codec=mediaify.OpusCodec(bitrate=128_000),
    resize=mediaify.TargetResolutionResize(width=1280, height=720),
)

configs = [thumbnail, preview, video_360p, video_720p, fallback]
files = mediaify.batch_encode_video(data, configs)
file_names = ["thumbnail", "preview", "144p", "360p", "720p", "fallback"]

for name, file in zip(file_names, files):
    with open(f"./examples/output/video_encoding-{name}{file.ext}", "wb") as f:
        f.write(file.data)
        print(f"Saved {file} to {f.name}")
