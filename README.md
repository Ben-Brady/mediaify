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
    AnimationFile(500x500 600ms, image/webp),
]
```

# Dependencies

- ffmpeg
    - Used to re-encode videos
    - Debain/Ubuntu: `sudo apt-get install ffmpeg`
    - [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- libmagic
    - Non-windows platform need to manually install libmagic
    - Debian/Ubuntu: `sudo apt-get install libmagic1`
    - Homebrew: `brew install libmagic`
    - macports: `port install file`

