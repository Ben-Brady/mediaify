import mediaify

with open('./input/ricardo.gif', 'rb') as f:
    data = f.read()

files = mediaify.batch_encode_animation(data)

print(files)
for i, file in enumerate(files):
    with open(f"./output/fractal-{i}{file.ext}", "wb") as f:
        f.write(file.data)
