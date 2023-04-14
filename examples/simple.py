import mediaify

with open('./input/ricardo.gif', 'rb') as f:
    data = f.read()

files = mediaify.batch_encode_animation(data)

for i, file in enumerate(files):
    with open(f"./output/ricardo-{i}{file.ext}", "wb") as f:
        f.write(file.data)
        print(f"Saved {file.ext} to {f.name}")
