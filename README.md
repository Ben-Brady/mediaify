# Mediaify

Media encoding made simple. Encode media without the hassle by describing the output declaratively!

## [Simple](./examples/simple.py)

```python
import mediaify

with open('ricardo.gif', 'rb') as f:
    data = f.read()

mediaify.batch_encode_animation(data)
>>> [
  ImageFile(51x64, image/webp, 402.0B),
  ImageFile(102x128, image/webp, 808.0B),
  ImageFile(205x256, image/webp, 2.5KiB),
  ImageFile(241x300, image/webp, 3.3KiB),
  AnimationFile(241x300, 6.4s 128 frames, 20.00fps, image/gif, 390.9KiB)
]
```

| 1 | 2 | 3 | 4 | 5 |
| - | - | - | - | - |
| ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/fractal-0.webp) | ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/fractal-1.webp) | ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/fractal-2.webp) | ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/fractal-3.webp) | ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/fractal-4.gif) |


## [Highly Customisable](./examples/customisable.py)

```python
import mediaify
from mediaify.configs import (
    WEBPImageEncodeConfig,
    ImageConfig,
    UnencodedConfig,
)

encoding_config = [
    WEBPImageEncodeConfig(
        height=64,
        width=64,
        quality=50
    ),
    WEBPImageEncodeConfig(
        height=256,
        width=256,
        quality=70
    ),
    WEBPImageEncodeConfig(
        height=512,
        width=512,
        quality=80
    ),
    UnencodedConfig()
]


with open('./landscape.webp', 'rb') as f:
    data = f.read()


mediaify.batch_encode_image(data, encoding_config)
>>> [
  ImageFile(64x33, image/webp, 802.0B),
  ImageFile(256x134, image/webp, 9.9KiB),
  ImageFile(512x268, image/webp, 39.0KiB),
  ImageFile(1600x840, image/webp, 277.6KiB)
]
```

| 1 | 2 | 3 | 4 |
| - | - | - | - |
| ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/landscape-0.webp) | ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/landscape-1.webp) | ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/landscape-2.webp) | ![](https://raw.githubusercontent.com/Ben-Brady/mediaify/master/examples/output/landscape-3.webp) |

## [Multimedia Support](./examples/customisable.py)

```python
import mediaify

with open("./heavy.mp4", "wb") as f:
    mediaify.encode_media(f.read())
>>> VideoFile(1280x720, 13.834s, 24fps, audio, video/mp4, 3.2MiB)

with open("./ricardo.gif", "wb") as f:
    mediaify.encode_media(f.read())
>>> AnimationFile(241x300, 6.4s 128 frames, 20.00fps, image/gif, 390.9KiB)

with open("./landscape.webp", "wb") as f:
    mediaify.encode_media(f.read())
>>> ImageFile(1600x840, image/webp, 277.6KiB)
```

# Installation

[https://pypi.org/project/mediaify/](https://pypi.org/project/mediaify/)

```bash
python -m pip install mediaify
```

## Dependencies

- ffmpeg
  - Ensure ffmpeg is on PATH, try running `ffmpeg` to check
  - Debain/Ubuntu: `sudo apt-get install ffmpeg`
  - Other: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- libmagic
  - Windows: N/A, installed automatically
  - Debian/Ubuntu: `sudo apt-get install libmagic1`
  - Homebrew: `brew install libmagic`
  - macports: `port install file`

# Documentation

Unfinished.
