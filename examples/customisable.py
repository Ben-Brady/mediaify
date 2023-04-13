import mediaify
from mediaify.configs import (
    WEBPImageEncodeConfig,
    PNGEncodeConfig,
    JPEGEncodeConfig,
    UnencodedConfig,
)

encoding_config = [
    WEBPImageEncodeConfig(
        height=64,
        width=64,
        quality=50
    ),
    PNGEncodeConfig(
        height=256,
        width=256
    ),
    JPEGEncodeConfig(
        height=512,
        width=512,
        quality=80
    ),
    UnencodedConfig()
]



with open('./input/landscape.webp', 'rb') as f:
    data = f.read()


files = mediaify.batch_encode_image(data, encoding_config)
for i, file in enumerate(files):
    with open(f"./output/landscape-{i}{file.ext}", "wb") as f:
        f.write(file.data)
        print(f"Saved {file} to {f.name}")

