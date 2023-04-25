import mediaify

with open('./examples/input/image.png', 'rb') as f:
    data = f.read()

image = mediaify.encode_image(
    data,
    mediaify.WEBPImageFormat(quality=90),
)

with open("./examples/output/simple.webp", "wb") as f:
    f.write(image.data)
