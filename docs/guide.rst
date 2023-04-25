Guide
==================

Mediaify uses configs to encode media, you specify the
encoding settings
::

    import mediaify

    with open("./examples/input/landscape.webp", "rb") as f:
        image_data = f.read()

    png_config = mediaify.PNGFormat()
    png_image = mediaify.encode_image(image_data, png_config)
    print(png_image)
    # >>> ImageFile(1600x840, image/png, 1.9MB)

    webp_config = mediaify.WEBPImageFormat(
        quality=80,
        lossless=False,
    )
    webp_image = mediaify.encode_image(image_data, webp_config)
    print(webp_image)
    # >>> ImageFile(1600x840, image/webp, 172.9KB)


Videos
-----------------

Video files are made up of three parts, the video container (format),
the video codec and the audio codec.
::

    import mediaify
    from mediaify import VP9Codec, OpusCodec

    with open("./example.mp4", "rb") as f:
        video_data = f.read()

    encoding_config = mediaify.configs.WEBMFormat(
        framerate=10,
        codec=VP9EncodeConfig(
            crf=23,
        ),
        audio_codec=OpusEncodeConfig(
            bitrate=128_000,,
        )
    )
    re_encoded_video = mediaify.encode_video(video_data, encoding_config)
    print(re_encoded_video)
    # >>> ImageFile(1600x840, image/png, 1.9MB)
