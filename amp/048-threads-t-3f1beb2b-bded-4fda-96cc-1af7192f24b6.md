---
title: Plan implementation for showing cursor beam
url: https://ampcode.com/threads/T-3f1beb2b-bded-4fda-96cc-1af7192f24b6
source: crawler
fetched_at: 2026-02-06T02:10:06.521237636-03:00
rendered_js: false
word_count: 1200
summary: This document outlines a technical implementation plan for rendering a cursor beam in a terminal application, covering shader modifications, data structures, and blink logic.
tags:
    - terminal-emulator
    - graphics-programming
    - metal-api
    - cursor-rendering
    - implementation-plan
category: guide
---

[](#message-0-block-0 "Link to this block")

[![Thorsten](https://ampcode.com/avatars/user_01K9KJJDPFGCG05B1WFFETGX8E-2b95ad144eeb3acd.webp)](https://ampcode.com/@mrnugget)

Implement a plan for how to show the current cursor position as a beam |

[](#message-1-block-0 "Link to this block")

The user wants me to implement a plan for showing

[](#message-2-block-0 "Link to this block")

[![Thorsten](https://ampcode.com/avatars/user_01K9KJJDPFGCG05B1WFFETGX8E-2b95ad144eeb3acd.webp)](https://ampcode.com/@mrnugget)

Sorry, \*come up* with that plan: analyze the code, think hard, come up with a plan

[](#message-3-block-0 "Link to this block")

The user wants me to analyze the code and come up with a plan for how to show a cursor position as a beam (like a text cursor). Let me first understand the current codebase structure.

I should:

1. Read the relevant files to understand the architecture
2. Look at the renderer and how text is currently being displayed
3. Understand the data structures for cursor position
4. Come up with a plan for rendering a cursor beam

Let me start by exploring the codebase structure and reading key files.

[](#message-3-block-1 "Link to this block")

I'll analyze the codebase to understand how to implement a cursor beam.

[](#message-13-block-1 "Link to this block")

1. TL;DR

<!--THE END-->

- Represent the cursor as an optional Cursor in Scene with position, color, style (beam), and visible flag.
- Add a tiny second render pipeline for solid-colored quads (reusing the existing text vertex shader, new fragment that ignores texture).
- Compute the beam quad in NDC from GridConfig and window size; toggle visibility with a simple Instant-based timer; feed cursor row/col from Terminal::cursor\_position each frame.

<!--THE END-->

1. Recommended approach (simple path)

<!--THE END-->

- Scene representation
  
  - Add a Cursor struct and field to Scene:
    
    - struct Cursor { pos: CellPosition, color: Rgba, style: CursorStyle, visible: bool }
    - enum CursorStyle { Beam { width\_px: f32 } } // keep just Beam for now; leave room for Block/Underline later
  - Extend Scene to carry cursor: Option. Keep it optional so you can disable cursor rendering without branching elsewhere.
- Reuse vs new pipeline
  
  - Add a small “solid color” pipeline for the cursor. Keep text\_vertex as-is; add a new fragment shader solid\_fragment that returns in.color directly. This avoids touching the atlas or text sampler and prevents sampling/bleed issues.
- Shader changes
  
  - Add to shaders.metal:
    
    - fragment float4 solid\_fragment(TextVertexOut in \[\[stage\_in]]) { return in.color; }
  - No changes to text\_vertex or TextVertexIn/Out needed. You’ll use the same vertex buffer layout; just ignore texCoords in the cursor path.
- Calculating cursor position in NDC
  
  - Use GridConfig::grid\_to\_ndc to get top-left NDC of the target cell:
    
    - let (ndc\_left, ndc\_top) = grid\_config.grid\_to\_ndc(CellPosition { row, col }, &window\_size, scale\_factor)
  - Convert beam dimensions from pixels to NDC:
    
    - window\_width\_px = window\_size.width as f32 * scale\_factor as f32
    - window\_height\_px = window\_size.height as f32 * scale\_factor as f32
    - beam\_w\_px = cursor.style.width\_px (e.g., max(2.0, 0.1 * cell\_width))
    - beam\_h\_px = grid\_config.cell\_height
    - beam\_w\_ndc = 2.0 * (beam\_w\_px / window\_width\_px)
    - beam\_h\_ndc = 2.0 * (beam\_h\_px / window\_height\_px)
  - Build a triangle strip (4 vertices) for a rectangle starting at the cell’s left edge:
    
    - TL: (ndc\_left, ndc\_top)
    - BL: (ndc\_left, ndc\_top - beam\_h\_ndc)
    - TR: (ndc\_left + beam\_w\_ndc, ndc\_top)
    - BR: (ndc\_left + beam\_w\_ndc, ndc\_top - beam\_h\_ndc)
  - Colors: set vertex color to the desired cursor color; texCoords can be zeroed (unused by solid\_fragment).
- Blinking (timing mechanism)
  
  - In Renderer, add:
    
    - cursor\_blink\_interval: Duration (e.g., 500 ms)
    - cursor\_blink\_last\_toggle: Instant
    - cursor\_blink\_on: bool
  - Each frame (or render pass), toggle if elapsed() &gt;= interval:
    
    - if last\_toggle.elapsed() &gt;= interval { cursor\_blink\_on = !cursor\_blink\_on; last\_toggle = Instant::now(); }
  - When input occurs (key press), reset blink:
    
    - cursor\_blink\_on = true; cursor\_blink\_last\_toggle = Instant::now();
  - Only draw the cursor when cursor.visible && cursor\_blink\_on.
- Integration with Terminal cursor tracking
  
  - Wherever the Scene is built from Terminal:
    
    - let (row, col) = terminal.cursor\_position();
    - scene.cursor = Some(Cursor {  
      pos: CellPosition { row, col },  
      color: Rgba { r: 1.0, g: 1.0, b: 1.0, a: 1.0 },  
      style: CursorStyle::Beam { width\_px: max(2.0, 0.1 * grid\_config.cell\_width) },  
      visible: true  
      });
  - Keep Terminal::max\_cols in sync with grid columns:
    
    - Ideally call terminal.update\_max\_cols(renderer.grid\_config.cols) on resize or font change (you already compute cols in GridConfig; the Terminal method exists but is commented—re-enable or replicate).
  - Render order: draw text first (existing path), then draw the cursor quad with the solid pipeline so it sits on top of glyphs.
  - Minimal Renderer additions (suggested fields and setup):
    
    - solid\_pipeline\_state: RenderPipelineState
    - reuse text\_vertex\_buffer for the 4 cursor vertices (or a small dedicated buffer)
    - During init:
      
      - solid\_pipeline\_state = prepare\_pipeline\_state(&device, &library, "text\_vertex", "solid\_fragment")
    - During draw:
      
      - if let Some(cursor) = scene.cursor and cursor\_blink\_on { fill 4 vertices; set\_pipeline\_state(solid); set\_vertex\_buffer; draw\_primitives(TriangleStrip, vertex\_start=0, vertex\_count=4); }

Example minimal code snippets (only where needed)

- shaders.metal
  
  - Add:
    
    - fragment float4 solid\_fragment(TextVertexOut in \[\[stage\_in]]) { return in.color; }
- Scene
  
  - pub struct Cursor { pub pos: CellPosition, pub color: Rgba, pub style: CursorStyle, pub visible: bool }
  - pub enum CursorStyle { Beam { width\_px: f32 } }
  - pub struct Scene { pub background: Rgba, pub cells: Vec, pub cursor: Option }
- Renderer fields
  
  - solid\_pipeline\_state: RenderPipelineState
  - cursor\_blink\_interval: std::time::Duration
  - cursor\_blink\_last\_toggle: std::time::Instant
  - cursor\_blink\_on: bool
- Renderer::new setup
  
  - let solid\_pipeline\_state = prepare\_pipeline\_state(&device, &library, "text\_vertex", "solid\_fragment");
  - init blink timers (interval=Duration::from\_millis(500), last\_toggle=Instant::now(), cursor\_blink\_on=true)
- Per-frame
  
  - Update blink
  - If scene.cursor and blink\_on:
    
    - compute quad vertices as above; colors from scene.cursor.color; texCoords = float2(0,0)
    - text\_vertex\_buffer.copy(&device, vertices);
    - encoder.set\_render\_pipeline\_state(&solid\_pipeline\_state);
    - encoder.set\_vertex\_buffer(0, Some(&text\_vertex\_buffer.buffer), 0);
    - encoder.draw\_primitives(metal::MTLPrimitiveType::TriangleStrip, 0, 4);

Effort/scope

- M (1–3h): new fragment shader + pipeline, Scene additions, simple blink timer, quad generation, draw call after text, and wiring Terminal cursor to Scene.

<!--THE END-->

1. Rationale and trade-offs

<!--THE END-->

- A dedicated solid-color pipeline is the simplest robust way to draw a filled beam without modifying the atlas or risking texture sampling artifacts or shader conditionals. It also keeps the text path unchanged and makes future cursor styles easy (block/underline).
- Reusing the text pipeline with a “white texel” atlas entry is possible but more brittle (needs atlas mutation and careful sampling to avoid edge bleed with linear filtering).

<!--THE END-->

1. Risks and guardrails

<!--THE END-->

- Off-by-one/fractional pixel jitter on HiDPI: compute all positions in pixels first, then convert to NDC as shown; prefer integer beam width in px to avoid subpixel shimmering.
- Blend state: ensure the solid pipeline uses the same color attachment format and blending as text so alpha works; otherwise the beam may appear opaque when desired to be slightly translucent.
- Z order: draw the cursor after text; don’t forget to bind the correct pipeline before issuing the draw call.
- Resizes/font changes: keep Terminal::max\_cols synchronized with GridConfig.cols to keep wrapping logic and cursor col in range.

<!--THE END-->

1. When to consider the advanced path

<!--THE END-->

- You need multiple cursor styles (block, underline), inverted colors, or XOR blending across glyphs.
- Cursor needs to animate smoothly (e.g., fade in/out) rather than toggle.
- You want to avoid an extra pipeline switch for performance in very high-frequency draw loops.

<!--THE END-->

1. Optional advanced path

<!--THE END-->

- Single-pipeline approach: reuse text pipeline by binding a dedicated 1x1 A8 texture filled with 255 for the cursor pass and sampling that in text\_fragment; pass texCoords=(0.5,0.5) for all vertices. This eliminates the second pipeline at the cost of managing an extra texture.
- Style extensions: extend CursorStyle with Block and Underline; for Block, draw a full cell quad; for Underline, draw a short-height quad positioned at the baseline + small offset using GridConfig.baseline\_offset for placement.
- Smooth blinking: keep a running time uniform and compute alpha via a sin() in a fragment shader, or do CPU-side alpha interpolation and update per-frame.

[](#message-15-block-0 "Link to this block")

Based on the analysis, here's the plan for implementing a cursor beam:

## Cursor Beam Implementation Plan

### 1. **Data Model Changes**

- Add `Cursor` struct with position, color, style (beam width), and visibility flag
- Add `CursorStyle::Beam { width_px }` enum for future extensibility
- Extend `Scene` to include `cursor: Option<Cursor>`

### 2. **Shader Pipeline**

- Add new `solid_fragment` shader that renders solid color without texture sampling
- Reuse existing `text_vertex` shader and `TextVertexIn` structure
- Create separate `solid_pipeline_state` in Renderer

### 3. **Rendering Logic**

- Use `GridConfig::grid_to_ndc()` to calculate cursor position in NDC
- Generate 4-vertex triangle strip for thin vertical beam at cursor column
- Beam dimensions: 2-3px width × full cell height
- Render cursor **after** text so it appears on top

### 4. **Blinking Mechanism**

- Add `Instant`-based timer fields to Renderer: `cursor_blink_interval`, `cursor_blink_last_toggle`, `cursor_blink_on`
- Toggle visibility every ~500ms
- Reset blink to "on" state on keyboard input

### 5. **Integration**

- Pull cursor position from `Terminal::cursor_position()` when building Scene
- Re-enable `Terminal::update_max_cols()` to sync with `GridConfig.cols` on resize
- Pass cursor data through Scene → Renderer → draw call

### 6. **Implementation Order**

1. Add shader function (solid\_fragment)
2. Update Scene structs (Cursor, CursorStyle)
3. Add Renderer blink timer fields & pipeline setup
4. Implement cursor quad generation in draw()
5. Wire Terminal cursor to Scene in app/window code
6. Test & tune beam width and blink timing

This approach keeps text rendering untouched while adding minimal, clean cursor rendering with ~100 lines of new code.

[](#message-16-block-0 "Link to this block")

[![Thorsten](https://ampcode.com/avatars/user_01K9KJJDPFGCG05B1WFFETGX8E-2b95ad144eeb3acd.webp)](https://ampcode.com/@mrnugget)

great!

[](#message-17-block-0 "Link to this block")

The user is acknowledging the plan and seems satisfied with it. They said "great!" which is a positive acknowledgment. I should keep my response brief and concise as per the instructions.

I should just acknowledge their response briefly. I don't need to do anything else unless they ask me to proceed with implementation.

Public

### Reference Thread

`T-3f1beb2b-bded-4fda-96cc-1af7192f24b6`