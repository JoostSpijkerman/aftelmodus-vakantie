from PIL import Image, ImageDraw

def make_icon(size):
    img = Image.new("RGB", (size, size), "#0b1420")
    d = ImageDraw.Draw(img)

    # background gradient (dark navy to slightly lighter navy at bottom)
    top = (11, 20, 32)
    bottom = (18, 34, 51)
    for y in range(size):
        t = y / size
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        d.line([(0, y), (size, y)], fill=(r, g, b))

    # sun
    cx, cy, r = size * 0.5, size * 0.40, size * 0.18
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#fb923c")

    # sea horizon
    horizon_y = size * 0.62
    d.rectangle([0, horizon_y, size, size], fill="#14b8a6")

    # sun reflection stripe on water
    d.rectangle([cx - size * 0.05, horizon_y, cx + size * 0.05, size], fill="#5eead4")

    # keep fully opaque square: iOS/Android apply their own icon masking
    return img

for size, name in [(180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
    icon = make_icon(size)
    icon.save(f"icons/{name}")
    print("wrote", name, icon.size)
