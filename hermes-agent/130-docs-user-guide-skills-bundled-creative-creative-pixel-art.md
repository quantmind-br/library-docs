---
title: Pixel Art — Convert images into retro pixel art with hardware-accurate palettes (NES, Game Boy, PICO-8, C64, etc | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/creative/creative-pixel-art
source: crawler
fetched_at: 2026-04-24T17:05:30.800052388-03:00
rendered_js: false
word_count: 765
summary: This document provides a detailed reference for a pixel art generation skill that converts images into retro, hardware-accurate pixel art, with the option to animate them into short videos. It outlines workflows, available presets (like NES, Game Boy, PICO-8), scene effects, and invocation patterns.
tags:
    - pixel-art
    - retro-gaming
    - image-to-video
    - palette-quantization
    - preset-catalog
    - hardware-fidelity
    - animation-effects
category: reference
---

Convert images into retro pixel art with hardware-accurate palettes (NES, Game Boy, PICO-8, C64, etc.), and animate them into short videos. Presets cover arcade, SNES, and 10+ era-correct looks. Use `clarify` to let the user pick a style before generating.

SourceBundled (installed by default)Path`skills/creative/pixel-art`Version`2.0.0`Authordodo-reachLicenseMITTags`creative`, `pixel-art`, `arcade`, `snes`, `nes`, `gameboy`, `retro`, `image`, `video`

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Pixel Art

Convert any image into retro pixel art, then optionally animate it into a short MP4 or GIF with era-appropriate effects (rain, fireflies, snow, embers).

Two scripts ship with this skill:

- `scripts/pixel_art.py` — photo → pixel-art PNG (Floyd-Steinberg dithering)
- `scripts/pixel_art_video.py` — pixel-art PNG → animated MP4 (+ optional GIF)

Each is importable or runnable directly. Presets snap to hardware palettes when you want era-accurate colors (NES, Game Boy, PICO-8, etc.), or use adaptive N-color quantization for arcade/SNES-style looks.

## When to Use[​](#when-to-use "Direct link to When to Use")

- User wants retro pixel art from a source image
- User asks for NES / Game Boy / PICO-8 / C64 / arcade / SNES styling
- User wants a short looping animation (rain scene, night sky, snow, etc.)
- Posters, album covers, social posts, sprites, characters, avatars

## Workflow[​](#workflow "Direct link to Workflow")

Before generating, confirm the style with the user. Different presets produce very different outputs and regenerating is costly.

### Step 1 — Offer a style[​](#step-1--offer-a-style "Direct link to Step 1 — Offer a style")

Call `clarify` with 4 representative presets. Pick the set based on what the user asked for — don't just dump all 14.

Default menu when the user's intent is unclear:

```python
clarify(
    question="Which pixel-art style do you want?",
    choices=[
"arcade — bold, chunky 80s cabinet feel (16 colors, 8px)",
"nes — Nintendo 8-bit hardware palette (54 colors, 8px)",
"gameboy — 4-shade green Game Boy DMG",
"snes — cleaner 16-bit look (32 colors, 4px)",
],
)
```

When the user already named an era (e.g. "80s arcade", "Gameboy"), skip `clarify` and use the matching preset directly.

### Step 2 — Offer animation (optional)[​](#step-2--offer-animation-optional "Direct link to Step 2 — Offer animation (optional)")

If the user asked for a video/GIF, or the output might benefit from motion, ask which scene:

```python
clarify(
    question="Want to animate it? Pick a scene or skip.",
    choices=[
"night — stars + fireflies + leaves",
"urban — rain + neon pulse",
"snow — falling snowflakes",
"skip — just the image",
],
)
```

Do NOT call `clarify` more than twice in a row. One for style, one for scene if animation is on the table. If the user explicitly asked for a specific style and scene in their message, skip `clarify` entirely.

### Step 3 — Generate[​](#step-3--generate "Direct link to Step 3 — Generate")

Run `pixel_art()` first; if animation was requested, chain into `pixel_art_video()` on the result.

## Preset Catalog[​](#preset-catalog "Direct link to Preset Catalog")

PresetEraPaletteBlockBest for`arcade`80s arcadeadaptive 168pxBold posters, hero art`snes`16-bitadaptive 324pxCharacters, detailed scenes`nes`8-bitNES (54)8pxTrue NES look`gameboy`DMG handheld4 green shades8pxMonochrome Game Boy`gameboy_pocket`Pocket handheld4 grey shades8pxMono GB Pocket`pico8`PICO-816 fixed6pxFantasy-console look`c64`Commodore 6416 fixed8px8-bit home computer`apple2`Apple II hi-res6 fixed10pxExtreme retro, 6 colors`teletext`BBC Teletext8 pure10pxChunky primary colors`mspaint`Windows MS Paint24 fixed8pxNostalgic desktop`mono_green`CRT phosphor2 green6pxTerminal/CRT aesthetic`mono_amber`CRT amber2 amber6pxAmber monitor look`neon`Cyberpunk10 neons6pxVaporwave/cyber`pastel`Soft pastel10 pastels6pxKawaii / gentle

Named palettes live in `scripts/palettes.py` (see `references/palettes.md` for the complete list — 28 named palettes total). Any preset can be overridden:

```python
pixel_art("in.png","out.png", preset="snes", palette="PICO_8", block=6)
```

## Scene Catalog (for video)[​](#scene-catalog-for-video "Direct link to Scene Catalog (for video)")

SceneEffects`night`Twinkling stars + fireflies + drifting leaves`dusk`Fireflies + sparkles`tavern`Dust motes + warm sparkles`indoor`Dust motes`urban`Rain + neon pulse`nature`Leaves + fireflies`magic`Sparkles + fireflies`storm`Rain + lightning`underwater`Bubbles + light sparkles`fire`Embers + sparkles`snow`Snowflakes + sparkles`desert`Heat shimmer + dust

## Invocation Patterns[​](#invocation-patterns "Direct link to Invocation Patterns")

### Python (import)[​](#python-import "Direct link to Python (import)")

```python
import sys
sys.path.insert(0,"/home/teknium/.hermes/skills/creative/pixel-art/scripts")
from pixel_art import pixel_art
from pixel_art_video import pixel_art_video

# 1. Convert to pixel art
pixel_art("/path/to/photo.jpg","/tmp/pixel.png", preset="nes")

# 2. Animate (optional)
pixel_art_video(
"/tmp/pixel.png",
"/tmp/pixel.mp4",
    scene="night",
    duration=6,
    fps=15,
    seed=42,
    export_gif=True,
)
```

### CLI[​](#cli "Direct link to CLI")

```bash
cd /home/teknium/.hermes/skills/creative/pixel-art/scripts

python pixel_art.py in.jpg out.png --preset gameboy
python pixel_art.py in.jpg out.png --preset snes --palette PICO_8 --block6

python pixel_art_video.py out.png out.mp4 --scene night --duration6--gif
```

## Pipeline Rationale[​](#pipeline-rationale "Direct link to Pipeline Rationale")

**Pixel conversion:**

1. Boost contrast/color/sharpness (stronger for smaller palettes)
2. Posterize to simplify tonal regions before quantization
3. Downscale by `block` with `Image.NEAREST` (hard pixels, no interpolation)
4. Quantize with Floyd-Steinberg dithering — against either an adaptive N-color palette OR a named hardware palette
5. Upscale back with `Image.NEAREST`

Quantizing AFTER downscale keeps dithering aligned with the final pixel grid. Quantizing before would waste error-diffusion on detail that disappears.

**Video overlay:**

- Copies the base frame each tick (static background)
- Overlays stateless-per-frame particle draws (one function per effect)
- Encodes via ffmpeg `libx264 -pix_fmt yuv420p -crf 18`
- Optional GIF via `palettegen` + `paletteuse`

## Dependencies[​](#dependencies "Direct link to Dependencies")

- Python 3.9+
- Pillow (`pip install Pillow`)
- ffmpeg on PATH (only needed for video — Hermes installs package this)

## Pitfalls[​](#pitfalls "Direct link to Pitfalls")

- Pallet keys are case-sensitive (`"NES"`, `"PICO_8"`, `"GAMEBOY_ORIGINAL"`).
- Very small sources (&lt;100px wide) collapse under 8-10px blocks. Upscale the source first if it's tiny.
- Fractional `block` or `palette` will break quantization — keep them positive ints.
- Animation particle counts are tuned for ~640x480 canvases. On very large images you may want a second pass with a different seed for density.
- `mono_green` / `mono_amber` force `color=0.0` (desaturate). If you override and keep chroma, the 2-color palette can produce stripes on smooth regions.
- `clarify` loop: call it at most twice per turn (style, then scene). Don't pepper the user with more picks.

## Verification[​](#verification "Direct link to Verification")

- PNG is created at the output path
- Clear square pixel blocks visible at the preset's block size
- Color count matches preset (eyeball the image or run `Image.open(p).getcolors()`)
- Video is a valid MP4 (`ffprobe` can open it) with non-zero size

## Attribution[​](#attribution "Direct link to Attribution")

Named hardware palettes and the procedural animation loops in `pixel_art_video.py` are ported from [pixel-art-studio](https://github.com/Synero/pixel-art-studio) (MIT). See `ATTRIBUTION.md` in this skill directory for details.