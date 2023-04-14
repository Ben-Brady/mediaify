import mediaify
from mediaify.configs import (
    WEBPImageEncodeConfig,
    PNGEncodeConfig,
    ResizeConfig,
    JPEGEncodeConfig,
    UnencodedConfig,
)

encoding_config = [
    JPEGEncodeConfig(
        resize=ResizeConfig(
            max_height=64,
            max_width=64,
        ),
        quality=80,
    ),
    PNGEncodeConfig(
        resize=ResizeConfig(
            height=256,
            width=256,
        )
    ),
    WEBPImageEncodeConfig(
        quality=90
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

