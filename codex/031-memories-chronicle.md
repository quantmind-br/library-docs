---
title: Chronicle
url: https://developers.openai.com/codex/memories/chronicle.md
source: llms
fetched_at: 2026-04-30T10:15:51.68766191-03:00
rendered_js: false
word_count: 674
summary: Chronicle is a feature that augments Codex memories by capturing screen context to provide relevant information and reduce the need for manual prompt context. This document outlines the setup, privacy considerations, operational controls, and security risks associated with the tool.
tags:
    - macos-automation
    - context-awareness
    - screen-recording
    - memory-management
    - privacy-security
    - prompt-engineering
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Chronicle

> [!warning]
> **Opt-in research preview.** ChatGPT Pro subscribers on macOS only. Not available in the EU, UK, and Switzerland. Review the Privacy and Security section before enabling.

Augments Codex memories with context from your screen. When you prompt Codex, those memories help it understand what you've been working on with less need to restate context.

Requires macOS Screen Recording and Accessibility permissions. Before enabling, be aware that Chronicle:
- Uses rate limits quickly
- Increases risk of prompt injection
- Stores memories unencrypted on your device

## How Chronicle helps

| Use case | Description |
|----------|-------------|
| Use what's on screen | Understand what you're currently looking at, saving time and context switching |
| Fill in missing context | Codex fills gaps without carefully crafted prompts |
| Remember tools and workflows | Codex learns which tools you use, saving time long-term |

When another source is better (specific file, Slack thread, Google Doc, dashboard, PR), Codex uses Chronicle to identify the source and then uses that source directly.

## Enable Chronicle

1. Open Settings in the Codex app.
2. Go to **Personalization** and ensure **Memories** is enabled.
3. Turn on **Chronicle** below Memories.
4. Review the consent dialog and choose **Continue**.
5. Grant macOS Screen Recording and Accessibility permissions when prompted.
6. When setup completes, choose **Try it out** or start a new thread.

If macOS reports permission denied, open **System Settings > Privacy & Security > Screen Recording / Accessibility** and enable Codex. If restricted by organization, Chronicle starts after the restriction is removed.

## Pause or disable

- **Pause/Resume** via Codex menu bar icon. Pause before meetings or when viewing sensitive content.
- **Disable** in **Settings > Personalization > Memories** by turning off Chronicle.
- Per-thread memory usage: see [[059-memories|Memories]].

## Rate limits

Chronicle runs sandboxed agents in the background to generate memories from captured screen images. These agents currently consume rate limits quickly.

## Privacy and security

Chronicle uses screen captures, which can include sensitive information visible on your screen. It does not access microphone or system audio. Don't use Chronicle to record meetings or communications without consent. Pause when viewing content you don't want remembered.

### Where data is stored

Screen captures are ephemeral, saved temporarily on your computer under `$TMPDIR/chronicle/screen_recording/`. Captures older than 6 hours are deleted while Chronicle is running.

Generated memories are unencrypted Markdown files stored locally under `$CODEX_HOME/memories_extensions/chronicle/` (typically `~/.codex/memories_extensions/chronicle/`). You can read, modify, or delete them. Don't manually add new information.

> [!danger]
> Both screen capture and memory directories might contain sensitive information. Don't share content with others, and be aware that other programs on your computer can also access these files.

### What data gets shared with OpenAI

Chronicle captures screen context locally, then periodically uses Codex to summarize recent activity into memories. The ephemeral session may process selected screenshot frames, OCR text, timing information, and local file paths for the relevant time window.

Screen captures are processed on OpenAI servers to generate memories, then stored locally. Screenshots are not stored on servers after processing unless required by law, and are not used for training.

Generated memories are local Markdown files. When Codex uses memories in a future session, relevant memory contents may be included as context, and may be used to improve models if allowed in your ChatGPT settings. [Learn more](https://help.openai.com/en/articles/7730893-data-controls-faq).

## Prompt injection risk

Using Chronicle increases risk of prompt injection attacks from screen content. If you browse a site with malicious agent instructions, Codex may follow them.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Chronicle setting not visible | Ensure you're on a Codex app build that includes Chronicle and that Memories is enabled in Settings > Personalization |
| Setup doesn't complete | Confirm Screen Recording and Accessibility permissions; quit and reopen Codex app; check Chronicle status in Settings > Personalization |
| Which model for memory generation? | Same model as other [[059-memories|Memories]]. Default = your default Codex model. Configure via `consolidation_model` in [[055-config-basic|config]]: |

```toml
[memories]
consolidation_model = "gpt-5.4-mini"
```

#chronicle #memories #macos #privacy #preview