---
title: Songsee — Generate spectrograms and audio feature visualizations (mel, chroma, MFCC, tempogram, etc | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-songsee
source: crawler
fetched_at: 2026-04-24T17:05:34.57417265-03:00
rendered_js: false
word_count: 53
summary: This document details the command-line interface (CLI) functionality of a tool named 'songsee' used to generate various visualizations from audio files, including spectrograms and multiple audio features.
tags:
    - audio-visualization
    - spectrogram-generation
    - cli-tool
    - audio-features
    - mel-chroma-mfcc
    - command-line
category: tutorial
---

Generate spectrograms and audio feature visualizations (mel, chroma, MFCC, tempogram, etc.) from audio files via CLI. Useful for audio analysis, music production debugging, and visual documentation.

Generate spectrograms and multi-panel audio feature visualizations from audio files.

Optional: `ffmpeg` for formats beyond WAV/MP3.

```bash
# Basic spectrogram
songsee track.mp3

# Save to specific file
songsee track.mp3 -o spectrogram.png

# Multi-panel visualization grid
songsee track.mp3 --viz spectrogram,mel,chroma,hpss,selfsim,loudness,tempogram,mfcc,flux

# Time slice (start at 12.5s, 8s duration)
songsee track.mp3 --start12.5--duration8-o slice.jpg

# From stdin
cat track.mp3 | songsee - --format png -o out.png
```

Multiple `--viz` types render as a grid in a single image.