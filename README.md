# Mediaify


Media encoding made simple!

Encode media without the hassle of wrangling ffmpeg and pillow, instead declare your output declaratively!

[Documentation](https://mediaify.readthedocs.io/)

[![Documentation Status](https://readthedocs.org/projects/mediaify/badge/?version=latest)](https://mediaify.readthedocs.io/en/latest/?badge=latest)

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

## Simple

```python
import mediaify

with open('./image.png', 'rb') as f:
    data = f.read()

mediaify.encode_image(data, mediaify.WEBPImageFormat(quality=90))
>>> ImageFile(1200x1600, image/webp, 162.6KB)
```

## Multimedia Support

Supports transcoding of several different media types.

- Audio
- Image
- Animation
- Video

```python
with open("./image.png", "rb") as f:
    data = f.read()
    print(mediaify.encode_audio(data))

with open("./image.png", "rb") as f:
    data = f.read()
    print(mediaify.encode_image(data))


with open("./animation.gif", "rb") as f:
    data = f.read()
    print(mediaify.encode_animation(data))


with open("./examples/input/video.mp4", "rb") as f:
    data = f.read()
    print(mediaify.encode_video(data))

>>> ImageFile(1200x1600, image/png, 35.4KB)
>>> AnimationFile(1280x800, 1.1s 11 frames, 10.00fps, image/gif, 132.8KB)
>>> VideoFile(1242x1242, 17.800s, 25.0fps, audio, video/mp4, 4.2MB)
```

## Customisable

Encode videos with multiple resolutions, formats, codecs as well as thumbnails and previews easily.

```python
import mediaify

thumbnail = mediaify.ThumbnailEncoding(
    encoding=mediaify.WEBPImageFormat(
        resize=mediaify.TargetResolutionResize(width=192, height=108),
        quality=80,
    ),
)
preview = mediaify.VideoPreviewAnimationEncoding(
    encoding=mediaify.WEBPAnimationFormat(
        resize=mediaify.TargetResolutionResize(width=640, height=360)
    )
)
video = mediaify.WEBMFormat(
    video_codec=mediaify.AV1Codec(crf=45, preset=6),
    audio_codec=mediaify.OpusCodec(bitrate=128_000),
    resize=mediaify.TargetResolutionResize(width=1280, height=720),
)

configs = [thumbnail, preview, video]
with open('./examples/input/video.mp4', 'rb') as f:
    data = f.read()

mediaify.batch_encode_video(data, configs)
>>> [
    ImageFile(192x108, image/webp, 2.2KB),
    AnimationFile(1280x720, 2.99s 45 frames, 15.05fps, image/webp, 4.5MB),
    VideoFile(1280x720, 34824.0s, 24.0fps, audio, video/webm, 4.1MB),
]
```

| Thumbnail | Summary |
| - | - |
| ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/demo/video_encoding-thumbnail.webp) | ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/demo/video_encoding-preview.webp) |

[Video.webm](https://user-images.githubusercontent.com/64110708/234427566-b3412283-72ee-408c-813d-0b77a8d939f7.webm)

# Roadmap

If you want any of these features to be developed, just flag an issue and I'll work on it.

- New Encoders
    - [x] Video
        - [X] WEBM
        - [X] MP4
        - [ ] Video to Animation
        - [ ] Video to Audio
    - [x] Audio Support
- Better Resizing
    - [ ] Blackbars
    - [ ] Cropping
