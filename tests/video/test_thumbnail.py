from ..data import KFC_VIDEO
import mediaify
from PIL import Image
import io


def test_encode_as_video_thumbnail():
    with open(KFC_VIDEO.filepath, 'rb') as f:
        data = f.read()

    config = mediaify.ThumbnailEncoding(
        encoding=mediaify.WEBPImageFormat(),
    )
    image = mediaify.encode_video(data, config)

    assert isinstance(image, mediaify.ImageFile)
    assert image.width == KFC_VIDEO.width
    assert image.height == KFC_VIDEO.height
    assert not image_is_black(image)


def image_is_black(image: mediaify.ImageFile) -> bool:
    im = Image.open(io.BytesIO(image.data))
    center = im.width // 2, im.height // 2
    return im.getpixel(center) == (0, 0, 0)
