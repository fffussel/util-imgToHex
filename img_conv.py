from PIL import Image

image = Image.open("img.png").convert("RGB")
image = image.resize((0, 0, 320, 240))
pixels = image.load()

output = []

for y in range(240):
    for x in range(320):
        r, g, b = pixels[x, y]

        # Convert to RGB565
        r5 = r >> 3
        g6 = g >> 2
        b5 = b >> 3

        color = (r5 << 11) | (g6 << 5) | b5

        # Swap bytes for little-endian .hword
        color_le = ((color & 0xFF) << 8) | (color >> 8)

        output.append(f"0x{color_le:04X}")

with open("img.txt", "w") as f:
    f.write(", ".join(output))