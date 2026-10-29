from PIL import Image
from collections import Counter

original = Image.open("suspect.jpg").convert("RGB")
modified = Image.open("encryptedImage.png").convert("RGB")

channels = Counter()
changes = []

for y in range(original.height):
    for x in range(original.width):
        a = original.getpixel((x, y))
        b = modified.getpixel((x, y))

        for i, name in enumerate(("R", "G", "B")):
            if a[i] != b[i]:
                channels[name] += 1
                changes.append((x, y, name, a[i], b[i]))

print("CHANNEL CHANGES:")
print(dict(channels))

print("\nFIRST 40 CHANGES:")
for change in changes[:40]:
    print(change)
