# Mediaify

Media encoding made simple.

## [Simple](./examples/simple.py)

```python
import mediaify

with open('ricardo.gif', 'rb') as f:
    data = f.read()

mediaify.batch_encode_animation(data)
>>> [
  ImageFile(128x128, image/webp, 6.2KiB),
  ImageFile(500x500, image/webp, 55.1KiB),
  AnimationFile(500x500, 0.6s, 0.05fps, image/webp, 23.4KiB),
  AnimationFile(500x500, 0.6s, 0.05fps, image/gif, 1.0MiB)
]
```

### Output

| 1 | 2 | 3 | 4 | 5 |
| - | - | - | - | - |
| ![](examples/output/fractal-0.webp) | ![](examples/output/fractal-1.webp) | ![](examples/output/fractal-2.webp) | ![](examples/output/fractal-3.webp) | ![](examples/output/fractal-4.gif) |


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

Output:

| 1 | 2 | 3 | 4 |
| - | - | - | - |
| ![](examples/output/landscape-0.webp) | ![](examples/output/landscape-1.webp) | ![](examples/output/landscape-2.webp) | ![](examples/output/landscape-3.webp) |

## [Multimeader Support](./examples/customisable.py)

```python
import mediaify

with open("./heavy.mp4") as f:
  data = f.read()

with open("./fractal.mp4") as f:
  data = f.read()

mediaify.load_media(data)
>>>
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
