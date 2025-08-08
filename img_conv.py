from PIL import Image

image = Image.open("img.png").convert("RGB")
image = image.resize((320, 240))
pixels = image.load()

output = []

def rgb888_to_rgb565(red8, green8, blue8):
    # Convert 8-bit red to 5-bit red.
    red5 = round(red8 / 255 * 31)
    # Convert 8-bit green to 6-bit green.
    green6 = round(green8 / 255 * 63)
    # Convert 8-bit blue to 5-bit blue.
    blue5 = round(blue8 / 255 * 31)

    # Shift the red value to the left by 11 bits.
    red5_shifted = red5 << 11
    # Shift the green value to the left by 5 bits.
    green6_shifted = green6 << 5

    # Combine the red, green, and blue values.
    rgb565 = red5_shifted | green6_shifted | blue5

    return rgb565


for y in range(240):
    for x in range(320):
        r, g, b = pixels[x, y]

        output.append(f"0x{rgb888_to_rgb565(r, g, b):04X}")

with open("img.txt", "w") as f:
    f.write(",".join(output))