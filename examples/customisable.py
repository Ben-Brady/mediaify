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
        height=128,
        width=128,
        quality=60
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
    WEBPImageEncodeConfig(
        height=1024,
        width=1024,
        quality=85
    ),
    UnencodedConfig()
]


with open('./input/landscape.webp', 'rb') as f:
    data = f.read()


files = mediaify.batch_encode_image(data, encoding_config)
for i, file in enumerate(files):
    with open(f"./landscape-{i}{file.ext}", "wb") as f:
        f.write(file.data)
print(files)
