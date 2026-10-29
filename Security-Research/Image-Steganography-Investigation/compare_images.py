from PIL import Image, ImageChops

original = Image.open("original.png").convert("RGB")
hidden = Image.open("hidden.png").convert("RGB")

if original.size != hidden.size:
    raise ValueError("Image dimensions do not match")

changed_pixels = 0

for y in range(original.height):
    for x in range(original.width):
        if original.getpixel((x, y)) != hidden.getpixel((x, y)):
            changed_pixels += 1
            print(f"Modified pixel: ({x}, {y})")
            print(f"  Original: {original.getpixel((x, y))}")
            print(f"  Hidden:   {hidden.getpixel((x, y))}")

total_pixels = original.width * original.height

print("\n--- FORENSIC COMPARISON ---")
print(f"Total pixels: {total_pixels}")
print(f"Modified pixels: {changed_pixels}")
print(f"Unchanged pixels: {total_pixels - changed_pixels}")
print(f"Modified percentage: {changed_pixels / total_pixels * 100:.6f}%")

# Generate a visual difference image
difference = ImageChops.difference(original, hidden)
difference.save("difference.png")

print("Difference image saved: difference.png")
