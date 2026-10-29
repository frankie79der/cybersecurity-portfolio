from PIL import Image, ImageChops

original = Image.open("original.png").convert("RGB")
hidden = Image.open("hidden.png").convert("RGB")

difference = ImageChops.difference(original, hidden)

# Highlight every changed pixel in red
mask = difference.convert("RGB")
output = Image.new("RGB", original.size, (0, 0, 0))

for y in range(original.height):
    for x in range(original.width):
        if mask.getpixel((x, y)) != (0, 0, 0):
            output.putpixel((x, y), (255, 0, 0))

# Enlarge the image to make individual pixels visible
output = output.resize(
    (1600, 1200),
    Image.Resampling.NEAREST
)

output.save("difference_highlighted.png")

print("Created: difference_highlighted.png")
