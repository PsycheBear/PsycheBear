import resvg_py

with open("banner.svg", "r", encoding="utf-8") as f:
    svg = f.read()

png_bytes = resvg_py.svg_to_bytes(svg_string=svg, width=1200)

with open("banner-preview.png", "wb") as f:
    f.write(bytes(png_bytes))

print("OK")
