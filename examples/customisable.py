import mediaify
from mediaify.configs import (
    WEBPImageEncodeConfig,
    PNGEncodeConfig,
    ResizeConfig,
    JPEGEncodeConfig,
    UnencodedConfig,
)

encoding_config = [
    WEBPImageEncodeConfig(
        resize=ResizeConfig(
            max_height=64,
            max_width=64,
        ),
        quality=50
    ),
    PNGEncodeConfig(
        resize=ResizeConfig(
            max_height=256,
            max_width=256,
        )
    ),
    JPEGEncodeConfig(
        resize=ResizeConfig(
            max_height=512,
            max_width=512,
        ),
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

