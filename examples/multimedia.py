import mediaify

with open("./input/heavy.mp4", "rb") as f:
  data = f.read()

print(mediaify.load_media(data))

with open("./input/ricardo.gif", "rb") as f:
  data = f.read()

print(mediaify.load_media(data))

with open("./input/landscape.webp", "rb") as f:
  data = f.read()

print(mediaify.load_media(data))
