---
title: GitMCP Extension | goose
url: https://block.github.io/goose/docs/mcp/gitmcp-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:17.540673064-03:00
rendered_js: true
word_count: 423
summary: This document provides a comprehensive overview of OpenAI's Whisper model, detailing its installation, model variants, and practical usage for speech-to-text and translation tasks.
tags:
    - speech-to-text
    - openai-whisper
    - transcription
    - audio-processing
    - machine-learning
    - python-library
category: guide
---

I'll help you understand OpenAI Whisper by exploring their GitHub repository. Let me fetch the documentation and relevant information.

`─── owner | repo ──────────────────────────`

Now let me search for some specific setup and usage information:

`─── owner | query ──────── repo ────────────`

Let me search for more technical details and examples:

`─── owner | query ──────── repo ────────────`

Perfect! Now I have all the information I need from the OpenAI Whisper repository. Let me create a comprehensive Markdown guide for you.

OpenAI Whisper Speech-to-Text Model Guide

Overview Whisper is a general-purpose speech recognition model developed by OpenAI. It's a powerful, multitasking neural network that can perform:

- Multilingual speech recognition (99+ languages)
- Speech translation (convert foreign speech to English text)
- Language identification (detect what language is being spoken)
- Voice activity detection (identify when speech is present)

Key Features:

- ✅ Robust Performance: Trained on 680,000 hours of diverse, multilingual audio data
- ✅ Zero-shot Transfer: Works on many languages without fine-tuning
- ✅ Multiple Model Sizes: From tiny (39M params) to large (1.55B params)
- ✅ Easy to Use: Simple command-line interface and Python API
- ✅ Open Source: MIT licensed with freely available model weights

Architecture Whisper uses a Transformer sequence-to-sequence model that processes audio in 30-second chunks. It converts audio to log-Mel spectrograms and uses special tokens to specify tasks (transcribe, translate, language ID, etc.).

Command-Line Usage Basic Transcription

## Getting Started Checklist[​](#getting-started-checklist "Direct link to Getting Started Checklist")

1. **✅ Install Python 3.8-3.11**
2. **✅ Install FFmpeg** for your operating system
3. **✅ Install Whisper**: `pip install -U openai-whisper`
4. **✅ Test installation**: `whisper --help`
5. **✅ Try basic transcription**: `whisper your_audio_file.mp3`

### First Run[​](#first-run "Direct link to First Run")

On your first run, Whisper will automatically download the model weights:

- `tiny`: ~39 MB download
- `base`: ~142 MB download
- `small`: ~461 MB download
- `medium`: ~1.42 GB download
- `large`: ~2.87 GB download
- `turbo`: ~1.5 GB download

Models are cached locally, so subsequent runs are much faster.

## Tips & Best Practices[​](#tips--best-practices "Direct link to Tips & Best Practices")

### 🎯 **Model Selection**[​](#-model-selection "Direct link to -model-selection")

- **English-only**: Use `.en` models (`base.en`, `small.en`, etc.)
- **Fast transcription**: Use `tiny` or `base` models
- **High accuracy**: Use `medium` or `large` models
- **Translation tasks**: Use `medium` or `large` (NOT `turbo`)

### 🎵 **Audio Quality**[​](#-audio-quality "Direct link to -audio-quality")

- Clean, clear audio produces better results
- Whisper handles various audio formats (MP3, WAV, FLAC, M4A, etc.)
- Background noise may affect accuracy

### 🌍 **Language Support**[​](#-language-support "Direct link to -language-support")

- Supports 99+ languages
- Some languages perform better than others
- Check the [language performance breakdown](https://github.com/openai/whisper#available-models-and-languages) in the repository

### 💾 **Resource Management**[​](#-resource-management "Direct link to -resource-management")

- Larger models require more VRAM/RAM
- Consider your hardware limitations when choosing models
- Use smaller models for real-time applications

Whisper is released under the **MIT License**, making it free to use for both personal and commercial projects.