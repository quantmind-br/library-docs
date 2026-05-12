---
title: Use Voice and Images to Prompt Agents | Guides | Warp
url: https://docs.warp.dev/guides/agent-workflows/how-to-use-voice-and-images-to-prompt-coding-agents
source: sitemap
fetched_at: 2026-04-29T15:06:24.268239854-03:00
rendered_js: false
word_count: 492
summary: This guide explains how to enhance productivity when using CLI coding agents in Warp by leveraging multimodal inputs like voice transcription and image attachments.
tags:
    - warp-terminal
    - coding-agent
    - voice-input
    - multimodal-ai
    - cli-tools
    - developer-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T15:06:24.268239854-03:00
---
# Use Voice and Images to Prompt Agents

Typing detailed prompts for coding agents can be slow. Describe a bug from a screenshot, dictate a complex refactoring plan, or explain a UI change from a mockup — voice and images make these tasks faster than text alone.

## Prerequisites

- **Warp** — Download from [warp.dev](https://warp.dev)
- **Microphone** (for voice) — Built-in, external, or Bluetooth

## 1. Enable voice input

1. Click the **microphone icon** in the input area, or use the voice input keybinding
2. Speak your prompt naturally — Warp transcribes and places text in the input field
3. Review the transcription, edit if needed, then submit

> [!info]
> Configure the voice input keybinding: **Settings** → **Agents** → **Warp Agent** → **Voice**. Default uses the `fn` key.

Voice input works for both Warp's built-in agent and third-party CLI agents when the agent utility bar is active.

## 2. Prompt with voice instead of typing

Voice is fastest for prompts easy to say but tedious to type: complex descriptions, multi-step plans, or explanations referencing what you're looking at.

## 3. Attach screenshots as context

Paste (`⌘+V`) or drag images directly into the input area. Use cases:

- **Bug reports** — Screenshot the error in your browser and ask the agent to fix it
- **Design mockups** — Paste a Figma screenshot and ask the agent to implement the UI
- **Error messages** — Screenshot a stack trace instead of copying and reformatting
- **Visual diffs** — Show what the UI looks like now vs. what it should look like

## 4. Combine voice and images for design-to-code workflows

1. Take a screenshot of a design mockup from Figma
2. Paste it into the input area
3. Use voice to describe what you want

The agent sees the design and hears your implementation requirements simultaneously — faster than writing a detailed specification by hand.

## 5. Use voice and images with third-party agents

Voice and image input work with any CLI agent Warp detects (Claude Code, Codex, etc.). The **agent utility bar** appears automatically when Warp detects an agent session.

1. Start the agent in your terminal (e.g., `claude` or `codex`)
2. The agent utility bar appears automatically
3. Use the microphone icon for voice input, paste images as context
4. Press `Ctrl+G` to open the rich input editor for complex prompts

> [!info]
> If you don't see the utility bar, ensure you're on the latest Warp version and the agent is running inside Warp.

## Productivity tips

- **Use voice for code review feedback** — Dictate changes while looking at the diff in the [[182-code-code-review]]
- **Screenshot UI issues** — Just screenshot, send to the agent, and describe what to change
- **Dictate commit messages** — After reviewing changes, use voice; the agent formats it as a proper commit message
- **Use with Rules** — Combine image context with [[041-agent-platform-warp-agents-capabilities-overview-rules]] that define your project's UI patterns

#tags #voice-input #multimodal-ai #coding-agent
