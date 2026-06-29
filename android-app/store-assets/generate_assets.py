"""
Generates Play Store assets for the Elevated Radiation Map app:
  - icon_512.png       (512x512, app icon - required)
  - feature_1024x500.png (feature graphic - required for store listing)
  - screenshot_template.png (1080x1920 reference for taking screenshots)

The icon design matches the in-app adaptive icon:
  blue map-pin + dark navy inner disc + yellow ISO radiation trefoil.
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path(__file__).resolve().parent

# Brand colours
NAVY = (26, 26, 46)        # #1a1a2e
NAVY_MID = (22, 33, 62)     # #16213e
BLUE = (55, 138, 221)       # #378ADD
YELLOW = (255, 214, 0)      # #FFD600
WHITE = (255, 255, 255)


def draw_pin_with_trefoil(draw: ImageDraw.ImageDraw, cx: float, cy: float, scale: float):
    """
    Draws the map-pin + radiation trefoil composition centred at (cx, cy).
    `scale` is the pin total height in pixels (top to point).
    Geometry matches ic_launcher_foreground.xml (108dp viewport, pin height ~60dp).
    """
    # ------------------------------------------------------------------
    # 1. Blue map-pin teardrop
    # ------------------------------------------------------------------
    # In the 108-unit viewport the pin is from y=22 (top) to y=82 (tip), height=60.
    # Pin head radius is 20 (so head spans x=34..74), centred at (54, 42).
    # We map: head_radius = scale * 20/60, head_centre_y = cy - scale*8/60
    head_r = scale * 20 / 60
    head_cy = cy - scale * 8 / 60
    head_cx = cx
    tip_y = cy + scale * 32 / 60

    # Draw the pin as: a circle (head) + a triangle (point) merged.
    # Easiest: build with polygon points sampling the original cubic.
    # Approximation good enough for store icon: head as circle + triangle.
    draw.ellipse(
        [head_cx - head_r, head_cy - head_r, head_cx + head_r, head_cy + head_r],
        fill=BLUE,
    )
    # Triangle for the point: from the bottom edges of the circle to the tip.
    # Tangent angle ~ 50° from vertical gives a nice teardrop.
    ang = math.radians(50)
    p_left = (head_cx - head_r * math.sin(ang), head_cy + head_r * math.cos(ang))
    p_right = (head_cx + head_r * math.sin(ang), head_cy + head_r * math.cos(ang))
    p_tip = (head_cx, tip_y)
    draw.polygon([p_left, p_right, p_tip], fill=BLUE)

    # ------------------------------------------------------------------
    # 2. Inner navy disc inside the pin head
    # ------------------------------------------------------------------
    inner_r = scale * 12 / 60   # radius 12 in 108-viewport
    draw.ellipse(
        [head_cx - inner_r, head_cy - inner_r, head_cx + inner_r, head_cy + inner_r],
        fill=NAVY,
    )

    # ------------------------------------------------------------------
    # 3. Yellow ISO trefoil (3 blades + centre dot), centred at the pin head
    # ------------------------------------------------------------------
    # ISO proportions:
    #   blade outer radius R_outer = 14/108 of viewport
    #   blade inner radius R_inner = 4.2/108
    #   centre dot radius R_dot   = 2.8/108
    R_outer = scale * 14 / 60
    R_inner = scale * 4.2 / 60
    R_dot = scale * 2.8 / 60

    # Three blades, each 60° wide. Centres at 90° (down), 210°, 330°.
    blade_centres = [90, 210, 330]
    for centre_deg in blade_centres:
        start = math.radians(centre_deg - 30)
        end = math.radians(centre_deg + 30)
        # Build polygon along outer arc then inner arc reversed
        outer_pts = []
        for t in [start + i * (end - start) / 32 for i in range(33)]:
            outer_pts.append((head_cx + R_outer * math.cos(t), head_cy + R_outer * math.sin(t)))
        inner_pts = []
        for t in [end - i * (end - start) / 32 for i in range(33)]:
            inner_pts.append((head_cx + R_inner * math.cos(t), head_cy + R_inner * math.sin(t)))
        draw.polygon(outer_pts + inner_pts, fill=YELLOW)

    # Centre dot
    draw.ellipse(
        [head_cx - R_dot, head_cy - R_dot, head_cx + R_dot, head_cy + R_dot],
        fill=YELLOW,
    )


# ----------------------------------------------------------------------
# 1) Store icon 512×512
# ----------------------------------------------------------------------
def make_icon():
    size = 512
    img = Image.new("RGB", (size, size), NAVY)
    draw = ImageDraw.Draw(img)
    # Pin centred slightly above middle so the pin tip + head are visually balanced.
    # In the 108-viewport the pin spans y=22..82 (centre at y=52). We want this
    # centred in 512×512, with comfortable margin.
    cx = size / 2
    cy = size / 2
    pin_height = int(size * 0.78)   # 400 px tall pin
    draw_pin_with_trefoil(draw, cx, cy, pin_height)
    out = OUT_DIR / "icon_512.png"
    img.save(out, "PNG")
    print(f"Wrote {out}")


# ----------------------------------------------------------------------
# 2) Feature graphic 1024×500
# ----------------------------------------------------------------------
def make_feature():
    w, h = 1024, 500
    img = Image.new("RGB", (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Subtle gradient overlay (top→bottom: NAVY → NAVY_MID)
    for y in range(h):
        t = y / h
        r = int(NAVY[0] * (1 - t) + NAVY_MID[0] * t)
        g = int(NAVY[1] * (1 - t) + NAVY_MID[1] * t)
        b = int(NAVY[2] * (1 - t) + NAVY_MID[2] * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Pin on the left
    pin_h = 380
    cx = 250
    cy = h // 2
    draw_pin_with_trefoil(draw, cx, cy, pin_h)

    # Title text on the right
    # Try to load a nice system font; fall back to default.
    title_font = None
    sub_font = None
    for candidate in ["arialbd.ttf", "segoeuib.ttf", "DejaVuSans-Bold.ttf"]:
        try:
            title_font = ImageFont.truetype(candidate, 72)
            sub_font = ImageFont.truetype(candidate.replace("b.ttf", ".ttf").replace("bd.ttf", ".ttf"), 30)
            break
        except OSError:
            continue
    if title_font is None:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

    title1 = "Elevated"
    title2 = "Radiation Map"
    subtitle = "Locations with unusual µSv/h readings"

    text_x = 470
    draw.text((text_x, 130), title1, font=title_font, fill=WHITE)
    draw.text((text_x, 215), title2, font=title_font, fill=YELLOW)
    draw.text((text_x, 320), subtitle, font=sub_font, fill=(200, 210, 230))

    out = OUT_DIR / "feature_1024x500.png"
    img.save(out, "PNG")
    print(f"Wrote {out}")


# ----------------------------------------------------------------------
# 3) Screenshot template 1080×1920 (a starting point - you will overwrite
#    with real screenshots from the device, but this gives a placeholder)
# ----------------------------------------------------------------------
def make_screenshot_template():
    w, h = 1080, 1920
    img = Image.new("RGB", (w, h), (245, 245, 245))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, 140], fill=NAVY)
    try:
        font_small = ImageFont.truetype("arial.ttf", 36)
    except OSError:
        font_small = ImageFont.load_default()
    draw.text((30, 50), "Elevated Radiation Map", font=font_small, fill=WHITE)
    draw.text(
        (50, h // 2 - 30),
        "Replace this template with a real screenshot\n"
        "from your device (1080×1920 or any 16:9 ratio).",
        font=font_small,
        fill=(80, 80, 80),
    )
    out = OUT_DIR / "screenshot_template.png"
    img.save(out, "PNG")
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_icon()
    make_feature()
    make_screenshot_template()
    print("\nAll Play Store assets generated in:", OUT_DIR)
