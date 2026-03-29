---
title: ElevenLabs Extension | goose
url: https://block.github.io/goose/docs/mcp/elevenlabs-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:06.464423828-03:00
rendered_js: true
word_count: 489
summary: This tutorial explains how to integrate the ElevenLabs MCP Server into goose to enable AI voice generation, cloning, and text-to-speech features.
tags:
    - elevenlabs
    - goose
    - mcp-server
    - text-to-speech
    - voice-synthesis
    - ai-audio
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial covers how to add the [ElevenLabs MCP Server](https://github.com/elevenlabs/elevenlabs-mcp) as a goose extension to enable AI-powered voice generation, voice cloning, audio editing, and speech-to-text transcription.

TLDR

- goose Desktop
- goose CLI

**Environment Variable**

```
ELEVENLABS_API_KEY: <YOUR_API_KEY>
```

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [uv](https://docs.astral.sh/uv/#installation) installed on your system to run this command, as it uses `uvx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=uvx&arg=elevenlabs-mcp&id=elevenlabs&name=ElevenLabs&description=ElevenLabs%20voice%20synthesis%20server&env=ELEVENLABS_API_KEY%3DElevenLabs%20API%20Key)
2. Click `Yes` to confirm the installation
3. Get your [ElevenLabs API Key](https://elevenlabs.io/app/settings/api-keys) and paste it in
4. Click `Add Extension`
5. Click the button in the top-left to open the sidebar
6. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

In this example, I’ll show you how to use goose with the ElevenLabs Extension to create AI-generated voiceovers for a YouTube Short. goose will take a sample script I provided, generate a narrated version using different AI voices, and seamlessly switch tones mid-script to match the content flow.

By connecting to the ElevenLabs MCP server, goose can transform plain text into natural-sounding speech, offering multiple voice styles and character options — all without any manual recording or editing.

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

> Hey goose, create a script for me for my youtube short video, I want there to be two different voices. The first voice should cut me off and be a human narrator style and then switch to a cassual AI tone after I read the prompt. Here's an example of a YT short script I've done in the past:

Wait… Within Seconds, goose performed Security Audits Across Multiple Projects?! 🔥

Lets, plug & play to find out how

Let’s provide goose with the command it needs to connect to the Filesystem MCP server extension…

Now lets play propmt: "Hey goose, I need to perform a security audit across multiple projects. Let's check for…🔹 Hardcoded Credentials – API keys, passwords, and secrets left in the code.🔹 SQL Injection Risks – Unsafe queries that could expose data.🔹 Insecure Cryptographic Practices – Weak encryption methods that put data at risk.AND🔹 Exposed Config Files – Sensitive information that shouldn't be public.🔹 Outdated Dependencies – Security vulnerabilities in third-party libraries."

Go goose, go goose!

✅ goose scanned the entire codebase across 3 different projects, identified security risks, generated a detailed report with fixes and provided me with step by step instructions on how I can test and verify these code fixes!

If that’s not amazing idk what is …

🚀 to get started visit block.github.io/goose_

### goose Output[​](#goose-output "Direct link to goose Output")

Desktop

I'll create your YouTube script for you using the given script as reference.

───────────── Text To Speech ─────────────

───────────── Text To Speech ─────────────

───────────── Text To Speech ─────────────

───────────── Text To Speech ─────────────

───────────── Text To Speech ─────────────

───────────── Play Audio ────────────────

───────────── Play Audio ────────────────

The script has been created and read aloud using the specified voices and style. The audio files have been saved to your desktop.

Press play and hear it for yourself! 🔊

Your browser does not support the audio element.