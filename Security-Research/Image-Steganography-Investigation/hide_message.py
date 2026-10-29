from PIL import Image

img = Image.open("original.png").convert("RGB")

message = "A"
bits = format(ord(message), "08b")

print("Character:", message)
print("Binary:", bits)

for i, bit in enumerate(bits):
    r, g, b = img.getpixel((i, 0))

    # Replace the least significant bit of blue
    new_b = (b & 0b11111110) | int(bit)

    img.putpixel((i, 0), (r, g, new_b))

    print(f"Pixel {i}: Blue {b} -> {new_b}")

img.save("hidden.png")

print("Created: hidden.png")
