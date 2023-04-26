import mediaify

with open("./examples/input/audio.mp3", "rb") as f:
    data = f.read()
print(mediaify.encode_audio(data))

with open("./examples/input/image.png", "rb") as f:
    data = f.read()
print(mediaify.encode_image(data))

with open("./examples/input/animation.gif", "rb") as f:
    data = f.read()
print(mediaify.encode_animation(data))

with open("./examples/input/video.mp4", "rb") as f:
    data = f.read()
print(mediaify.encode_video(data))
