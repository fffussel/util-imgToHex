from PIL import Image

image = Image.open("./img.png").convert("RGB")
image = image.crop((0, 0, input("Width: "), input("Height: ")))  # Ensure it's 320x240

pixels = image.load()

output = []

for y in range(240):
    for x in range(320):
        r, g, b = pixels[x, y]
        output.append(f"0x{r:02X}{g:02X}{b:02X}")

print(','.join(output))