# Mediaify

A library designed to make encoding media simple and easy.

```python
import mediaify

with open('fractal.gif', 'rb') as f:
    data = f.read()

files = mediaify.encode_media(data)
>>> [
    <mediaify.types.ImageFile object at 0x7f0d35d78820>,
    <mediaify.types.ImageFile object at 0x7f0d35d78970>,
    <mediaify.types.AnimationFile object at 0x7f0d35d788e0>,
    <mediaify.types.AnimationFile object at 0x7f0d35d78850>
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

