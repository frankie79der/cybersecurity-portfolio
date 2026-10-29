from PIL import Image

# Create a 400x300 RGB image
img = Image.new("RGB", (400, 300))

# Fill the image with a color gradient
for y in range(300):
    for x in range(400):
        r = int(x / 400 * 255)
        g = int(y / 300 * 255)
        b = 150

        img.putpixel((x, y), (r, g, b))

img.save("original.png")

print("Image created: original.png")
