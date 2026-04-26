---
title: Development
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/development.md
source: git
fetched_at: 2026-04-26T05:48:12.404890871-03:00
rendered_js: false
word_count: 191
summary: This document provides developer guidelines for setting up, reconfiguring, and maintaining the pi-mono repository.
tags:
    - project-setup
    - forking
    - path-resolution
    - debugging
    - testing
    - project-structure
category: guide
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Development

See [[000-index|AGENTS.md]] for additional guidelines.

## Setup

```bash
git clone https://github.com/badlogic/pi-mono
cd pi-mono
npm install
npm run build
```

Run from source:

```bash
/path/to/pi-mono/pi-test.sh
```

The script runs from any directory. Pi preserves the caller's working directory.

## Forking / Rebranding

Configure via `package.json`:

```json
{
  "piConfig": {
    "name": "pi",
    "configDir": ".pi"
  }
}
```

Change `name`, `configDir`, and `bin` for your fork — affects CLI banner, config paths, and env var names.

## Path Resolution

Three execution modes: npm install, standalone binary, tsx from source.

> [!warning] Always use `src/config.ts` for package assets — never `__dirname`.

```typescript
import { getPackageDir, getThemeDir } from "./config.js";
```

## Debug Command

`/debug` (hidden) writes to `~/.pi/agent/pi-debug.log`:
- Rendered TUI lines with ANSI codes
- Last messages sent to the LLM

## Testing

```bash
./test.sh                         # Non-LLM tests (no API keys needed)
npm test                          # All tests
npm test -- test/specific.test.ts # Specific test
```

## Project Structure

```
packages/
  ai/           # LLM provider abstraction
  agent/        # Agent loop and message types
  tui/          # Terminal UI components
  coding-agent/ # CLI and interactive mode
```

#project-setup #forking #testing
