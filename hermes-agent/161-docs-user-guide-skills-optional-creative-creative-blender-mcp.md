---
title: Blender Mcp — Control Blender directly from Hermes via socket connection to the blender-mcp addon | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-blender-mcp
source: crawler
fetched_at: 2026-04-24T17:01:19.566927386-03:00
rendered_js: false
word_count: 388
summary: This document details the Blender MCP skill, which allows external control of a running Blender instance via a TCP socket connection. It provides setup instructions, protocol definitions, available commands, Python helpers, and common usage patterns for manipulating 3D objects and animations.
tags:
    - blender-mcp
    - socket-control
    - bpy-api
    - blender-integration
    - tcp-protocol
    - addon-skill
category: reference
---

Control Blender directly from Hermes via socket connection to the blender-mcp addon. Create 3D objects, materials, animations, and run arbitrary Blender Python (bpy) code. Use when user wants to create or modify anything in Blender.

SourceOptional — install with `hermes skills install official/creative/blender-mcp`Path`optional-skills/creative/blender-mcp`Version`1.0.0`Authoralireza78a

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Blender MCP

Control a running Blender instance from Hermes via socket on TCP port 9876.

## Setup (one-time)[​](#setup-one-time "Direct link to Setup (one-time)")

### 1. Install the Blender addon[​](#1-install-the-blender-addon "Direct link to 1. Install the Blender addon")

curl -sL [https://raw.githubusercontent.com/ahujasid/blender-mcp/main/addon.py](https://raw.githubusercontent.com/ahujasid/blender-mcp/main/addon.py) -o ~/Desktop/blender\_mcp\_addon.py

In Blender: Edit &gt; Preferences &gt; Add-ons &gt; Install &gt; select blender\_mcp\_addon.py Enable "Interface: Blender MCP"

### 2. Start the socket server in Blender[​](#2-start-the-socket-server-in-blender "Direct link to 2. Start the socket server in Blender")

Press N in Blender viewport to open sidebar. Find "BlenderMCP" tab and click "Start Server".

### 3. Verify connection[​](#3-verify-connection "Direct link to 3. Verify connection")

nc -z -w2 localhost 9876 && echo "OPEN" || echo "CLOSED"

## Protocol[​](#protocol "Direct link to Protocol")

Plain UTF-8 JSON over TCP -- no length prefix.

Send: {"type": "&lt;command&gt;", "params": {&lt;kwargs&gt;}} Receive: {"status": "success", "result": &lt;value&gt;} {"status": "error", "message": "&lt;reason&gt;"}

## Available Commands[​](#available-commands "Direct link to Available Commands")

typeparamsdescriptionexecute\_codecode (str)Run arbitrary bpy Python codeget\_scene\_info(none)List all objects in sceneget\_object\_infoobject\_name (str)Details on a specific objectget\_viewport\_screenshot(none)Screenshot of current viewport

## Python Helper[​](#python-helper "Direct link to Python Helper")

Use this inside execute\_code tool calls:

import socket, json

def blender\_exec(code: str, host="localhost", port=9876, timeout=15): s = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) s.connect((host, port)) s.settimeout(timeout) payload = json.dumps({"type": "execute\_code", "params": {"code": code}}) s.sendall(payload.encode("utf-8")) buf = b"" while True: try: chunk = s.recv(4096) if not chunk: break buf += chunk try: json.loads(buf.decode("utf-8")) break except json.JSONDecodeError: continue except socket.timeout: break s.close() return json.loads(buf.decode("utf-8"))

## Common bpy Patterns[​](#common-bpy-patterns "Direct link to Common bpy Patterns")

### Clear scene[​](#clear-scene "Direct link to Clear scene")

bpy.ops.object.select\_all(action='SELECT') bpy.ops.object.delete()

### Add mesh objects[​](#add-mesh-objects "Direct link to Add mesh objects")

bpy.ops.mesh.primitive\_uv\_sphere\_add(radius=1, location=(0, 0, 0)) bpy.ops.mesh.primitive\_cube\_add(size=2, location=(3, 0, 0)) bpy.ops.mesh.primitive\_cylinder\_add(radius=0.5, depth=2, location=(-3, 0, 0))

### Create and assign material[​](#create-and-assign-material "Direct link to Create and assign material")

mat = bpy.data.materials.new(name="MyMat") mat.use\_nodes = True bsdf = mat.node\_tree.nodes.get("Principled BSDF") bsdf.inputs\["Base Color"].default\_value = (R, G, B, 1.0) bsdf.inputs\["Roughness"].default\_value = 0.3 bsdf.inputs\["Metallic"].default\_value = 0.0 obj.data.materials.append(mat)

### Keyframe animation[​](#keyframe-animation "Direct link to Keyframe animation")

obj.location = (0, 0, 0) obj.keyframe\_insert(data\_path="location", frame=1) obj.location = (0, 0, 3) obj.keyframe\_insert(data\_path="location", frame=60)

### Render to file[​](#render-to-file "Direct link to Render to file")

bpy.context.scene.render.filepath = "/tmp/render.png" bpy.context.scene.render.engine = 'CYCLES' bpy.ops.render.render(write\_still=True)

## Pitfalls[​](#pitfalls "Direct link to Pitfalls")

- Must check socket is open before running (nc -z localhost 9876)
- Addon server must be started inside Blender each session (N-panel &gt; BlenderMCP &gt; Connect)
- Break complex scenes into multiple smaller execute\_code calls to avoid timeouts
- Render output path must be absolute (/tmp/...) not relative
- shade\_smooth() requires object to be selected and in object mode