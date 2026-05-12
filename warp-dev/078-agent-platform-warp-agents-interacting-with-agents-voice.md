---
title: Voice | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents/voice
source: sitemap
fetched_at: 2026-04-29T15:04:03.960289846-03:00
rendered_js: false
word_count: 357
summary: This document explains how to set up, configure, and use the voice input feature in the Warp terminal for hands-free command entry and agent interaction.
tags:
    - voice-input
    - terminal-productivity
    - warp-agent
    - microphone-setup
    - speech-to-text
    - accessibility-tools
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Voice

Speak commands and questions instead of typing them, powered by [Wispr Flow](https://wisprflow.ai/).

Configure voice input in **Settings** > **Agents** > **Warp Agent** > **Voice**.

## Initial Setup

First-time users must grant microphone permissions:

| OS | Steps |
|----|-------|
| macOS | Accept system prompt or allow in System Settings > Privacy & Security > Microphone |
| Windows | Allow in Settings > Privacy & Security > Microphone |
| Linux | Configure through system sound settings |

## Using Voice

Two ways to activate:

1. **Microphone Button in Agent Mode**
   - Click the microphone icon in Agent Mode
   - Start speaking when the indicator shows it's listening
   - Click again to stop recording

2. **Hotkey Method**
   - Press and hold `Fn` key (configurable) to start recording
   - Speak your command while holding the key
   - Release to stop recording and transcribe

## Sample Use Cases

- Multi-step commands: "Create a new Node.js project, install Express and MongoDB, then set up a basic server"
- Explanations: "What's the difference between chmod and chown? Give me examples"
- System tasks: "Find all log files with errors from the last 24 hours, create a summary, and email it"
- Works across all Warp input interfaces: Find dialog, terminal commands, input editors

## Privacy & Security

Voice data is processed in real-time by Wispr Flow and is not retained as a recording after transcription.

## Usage Limits

Voice features have anti-abuse limits in place, subject to change.

## Troubleshooting

### Microphone Not Detected
1. Check system permissions to ensure Warp has access
2. Verify the microphone is properly connected
3. Try restarting Warp to reset the connection

### Poor Transcription Quality
- Minimize background noise
- Position closer to the microphone
- Verify microphone input levels in system settings
- Speak clearly at a natural pace with complete sentences
- Enunciate file names and commands clearly
- Review transcription before sending

### Feature Not Activating
- Confirm hotkey settings are correctly configured in Warp
- Check for conflicting keyboard shortcuts
- Ensure running the latest version of Warp
- Enterprise users: administrator may have disabled Voice functionality
