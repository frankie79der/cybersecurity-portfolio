from PIL import Image

img = Image.open("hidden.png").convert("RGB")

bits = ""

for i in range(8):
    r, g, b = img.getpixel((i, 0))

    bit = b & 1
    bits += str(bit)

    print(f"Pixel {i}: Blue={b}, LSB={bit}")

ascii_value = int(bits, 2)
character = chr(ascii_value)

print("Extracted bits:", bits)
print("ASCII value:", ascii_value)
print("Recovered message:", character)
