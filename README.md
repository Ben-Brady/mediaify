# Mediaify


Media encoding made simple!

Encode media without the hassle of wrangling ffmpeg and pillow, instead declare your output declaratively!

[Documentation](https://mediaify.readthedocs.io/)

[![Documentation Status](https://readthedocs.org/projects/mediaify/badge/?version=latest)](https://mediaify.readthedocs.io/en/latest/?badge=latest)

```python
import mediaify

with open('./image.png', 'rb') as f:
    data = f.read()

image = mediaify.encode_image(data, mediaify.WEBPImageFormat(quality=90))
image.save("./image.webp")
```

## Multimedia Support

Supports transcoding of several different media types.

- Audio
- Image
- Animation
- Video

```python
with open("./audio.mp4", "rb") as f:
    data = f.read()

mediaify.encode_audio(data)
>>> AudioFile(audio/mpeg, 2.5MB)

with open("./image.png", "rb") as f:
    data = f.read()

mediaify.encode_image(data)
>>> ImageFile(1200x1600, image/png, 35.4KB)


with open("./animation.gif", "rb") as f:
    data = f.read()

mediaify.encode_animation(data)
>>> AnimationFile(1280x800, 1.1s 11 frames, 10.0fps, image/gif, 132.8KB)


with open("./examples/input/video.mp4", "rb") as f:
    data = f.read()

mediaify.encode_video(data)
>>> VideoFile(1280x720, 60.458s, 24.0fps, audio, video/mp4, 8.5MB)
```

## Customisable

Encode videos with multiple resolutions, formats, codecs as well as thumbnails and previews easily.

```python
import mediaify

thumbnail = mediaify.ThumbnailEncoding(
    encoding=mediaify.WEBPImageFormat(
        resize=mediaify.TargetResolutionResize(width=640, height=360),
        quality=80,
    ),
)
preview = mediaify.VideoPreviewAnimationEncoding(
    encoding=mediaify.WEBPAnimationFormat(
        resize=mediaify.TargetResolutionResize(width=640, height=360),
        quality=50,
        lossless=False,
    ),
    framerate=5,
    frames=60,
)
video_360p = mediaify.WEBMFormat(
    resize=mediaify.TargetResolutionResize(width=640, height=360),
    video_codec=mediaify.AV1Codec(crf=50, preset=7),
    audio_codec=mediaify.OpusCodec(bitrate=128_000),
)
video_720p = mediaify.WEBMFormat(
    resize=mediaify.TargetResolutionResize(width=1280, height=720),
    video_codec=mediaify.AV1Codec(crf=45, preset=6),
    audio_codec=mediaify.OpusCodec(bitrate=128_000),
)
fallback = mediaify.MP4Format(
    resize=mediaify.TargetResolutionResize(width=1280, height=720),
    video_codec=mediaify.H264Codec(crf=21, preset="medium"),
    audio_codec=mediaify.OpusCodec(bitrate=128_000),
)


configs = [thumbnail, preview, video_360p, video_720p, fallback]
with open('./examples/input/video.mp4', 'rb') as f:
    data = f.read()

mediaify.batch_encode_video(data, configs)
>>> [
    ImageFile(640x360, image/webp, 10.1KB),
    AnimationFile(640x360, 12.0s 60 frames, 5.0fps, image/webp, 1.8MB),
    VideoFile(640x360, 60.45s, 24.0fps, audio, video/webm, 2.2MB),
    VideoFile(1280x720, 60.45s, 24.0fps, audio, video/webm, 4.2MB),
    VideoFile(1280x720, 60.45s, 24.0fps, audio, video/mp4, 14.2MB),
]
```

# Installation

[https://pypi.org/project/mediaify/](https://pypi.org/project/mediaify/)

```bash
python -m pip install mediaify
```

## Dependencies

### ffmpeg

Ensure ffmpeg is installed and on $PATH, try running `ffmpeg` to check

- Debain/Ubuntu: `sudo apt-get install ffmpeg`
- Other: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

### libmagic

- Windows: N/A, installed automatically
- Debian/Ubuntu: `sudo apt-get install libmagic1`
- Homebrew: `brew install libmagic`
- macports: `port install file`

# Roadmap

If you want any of these features to be developed, just flag an issue and I'll work on it.

- New Encoders
    - [x] Video
        - [X] WEBM
        - [X] MP4
        - [ ] DASH Video
        - [ ] Video to Animation
        - [ ] Video to Audio
    - [x] Audio Support
- Better Resizing
    - [ ] Blackbars
    - [ ] Cropping
