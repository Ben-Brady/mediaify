# Mediaify

A library designed to make encoding media simple and easy.

```python
import mediaify

with open('fractal.gif', 'rb') as f:
    data = f.read()

files = mediaify.encode_media(data)
>>> [
    ImageFile(128x128, image/webp),
    ImageFile(500x500, image/webp),
    AnimationFile(500x500 600ms, image/webp),
    AnimationFile(500x500 600ms, image/gif)
]
```

# Installation

[https://pypi.org/project/mediaify/](https://pypi.org/project/mediaify/)

```
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
