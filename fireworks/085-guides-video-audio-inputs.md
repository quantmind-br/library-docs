---
title: Video & Audio Inputs - Fireworks AI Docs
url: https://docs.fireworks.ai/guides/video-audio-inputs
source: sitemap
fetched_at: 2026-04-27T20:18:13.555380972-03:00
rendered_js: false
word_count: 386
summary: This document describes how to use multimodal models, such as Qwen3 Omni, that accept video and audio inputs alongside text. It details the process of creating a dedicated deployment for these models and provides comprehensive examples for making API calls using Python and curl, along with tips for optimizing media preprocessing via ffmpeg.
tags:
    - multimodal-models
    - video-audio-input
    - api-integration
    - deployment-setup
    - ffmpeg-optimization
    - qwen3-omni
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Omni/multimodal models like Qwen3 Omni process video, audio, and text inputs in a single request. Deploy these models using [[008-getting-started-ondemand-quickstart|dedicated deployments]] for production workloads.

## Available Models

| Model | Input Support | Notes |
|---|---|---|
| [Qwen3 Omni 30B A3B Instruct](https://fireworks.ai/models/fireworks/qwen3-omni-30b-a3b-instruct) | Video, audio, text | Dedicated deployment required |
| [Molmo2-4B](https://fireworks.ai/models/fireworks/molmo2-4b) | Video, text | Dedicated deployment required |
| [Molmo2-8B](https://fireworks.ai/models/fireworks/molmo2-8b) | Video, text | Dedicated deployment required |

## Create a Deployment

Video and audio models require dedicated deployments. Create one using firectl:

```bash
firectl deployment create qwen3-omni-30b-a3b-instruct \
  --account-id <YOUR_ACCOUNT_ID> \
  --min-replica-count 1 \
  --max-replica-count 1 \
  --deployment-shape qwen3-omni-30b-a3b-instruct-minimal
```

## Chat Completions API

Provide video and audio as base64-encoded data URLs. The model accepts `video_url`, `audio_url`, and `text` content types.

```python
import os
import base64
import requests

# Load and encode your preprocessed video and audio
with open("processed_video.mp4", "rb") as f:
    video_b64 = base64.b64encode(f.read()).decode("utf-8")

with open("audio.ogg", "rb") as f:
    audio_b64 = base64.b64encode(f.read()).decode("utf-8")

# API configuration
url = "https://api.fireworks.ai/inference/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['FIREWORKS_API_KEY']}",
}

# Request payload
payload = {
    "model": "accounts/<YOUR_ACCOUNT_ID>/models/qwen3-omni-30b-a3b-instruct#accounts/<YOUR_ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    "max_tokens": 1000,
    "temperature": 0.3,
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_b64}"}},
                {"type": "audio_url", "audio_url": {"url": f"data:audio/ogg;base64,{audio_b64}"}},
                {"type": "text", "text": "Describe what happens in this video."},
            ],
        },
    ],
}

# Send request
response = requests.post(url, headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
```

```bash
# Encode your files (run these separately)
VIDEO_B64=$(base64 -i processed_video.mp4)
AUDIO_B64=$(base64 -i audio.ogg)

curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/<YOUR_ACCOUNT_ID>/models/qwen3-omni-30b-a3b-instruct#accounts/<YOUR_ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    "max_tokens": 1000,
    "temperature": 0.3,
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "video_url", "video_url": {"url": "data:video/mp4;base64,'$VIDEO_B64'"}},
          {"type": "audio_url", "audio_url": {"url": "data:audio/ogg;base64,'$AUDIO_B64'"}},
          {"type": "text", "text": "Describe what happens in this video."}
        ]
      }
    ]
  }'
```

## Working with Videos

Video models perform best with preprocessed inputs that balance quality and token efficiency. Use ffmpeg to optimize your video and audio before sending requests.

### Preprocessing Video

Extract frames at 1 FPS and downscale to 360p for efficient processing:

```bash
ffmpeg -y -i input_video.mp4 \
  -t 60 \
  -vf "fps=1,scale=-1:360" \
  -c:v libx264 -preset fast \
  -an \
  processed_video.mp4
```

| Parameter | Description |
|---|---|
| `-t 60` | Limit to first 60 seconds |
| `fps=1` | Extract 1 frame per second |
| `scale=-1:360` | Downscale to 360p height, maintain aspect ratio |
| `-an` | Remove audio track (extracted separately) |

### Preprocessing Audio

Extract audio as Opus in an Ogg container for optimal compression:

```bash
ffmpeg -y -i input_video.mp4 \
  -t 60 \
  -vn \
  -c:a libopus \
  -b:a 24k \
  -ar 16000 \
  -ac 1 \
  audio.ogg
```

| Parameter | Description |
|---|---|
| `-t 60` | Limit to first 60 seconds |
| `-vn` | Remove video track |
| `-c:a libopus` | Use Opus codec |
| `-b:a 24k` | 24 kbps bitrate |
| `-ar 16000` | 16 kHz sample rate |
| `-ac 1` | Mono audio |

### Complete Preprocessing Example

```python
import subprocess
import tempfile
import base64
import os

def preprocess_video(video_path: str) -> tuple[str, str]:
    """
    Preprocess video for optimal model input.

    Returns:
        Tuple of (video_base64, audio_base64)
    """
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp_video:
        processed_video_path = tmp_video.name
    with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as tmp_audio:
        audio_path = tmp_audio.name

    try:
        # Process video: 1 FPS, 360p, max 60 seconds
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path,
            "-t", "60",
            "-vf", "fps=1,scale=-1:360",
            "-c:v", "libx264", "-preset", "fast",
            "-an",
            processed_video_path
        ], check=True, capture_output=True)

        # Extract audio: Opus/Ogg, mono, 16kHz, 24kbps
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path,
            "-t", "60",
            "-vn",
            "-c:a", "libopus",
            "-b:a", "24k",
            "-ar", "16000",
            "-ac", "1",
            audio_path
        ], check=True, capture_output=True)

        with open(processed_video_path, "rb") as f:
            video_b64 = base64.b64encode(f.read()).decode("utf-8")

        with open(audio_path, "rb") as f:
            audio_b64 = base64.b64encode(f.read()).decode("utf-8")

        return video_b64, audio_b64

    finally:
        os.unlink(processed_video_path)
        os.unlink(audio_path)
```

## Performance Considerations

> [!tip] Optimal throughput tips:
> - **Preprocess all videos** – 1 FPS at 360p provides good quality with minimal tokens
> - **Extract audio separately** – Opus/Ogg at 24kbps offers excellent compression
> - **Limit video duration** – Cap at 60 seconds for consistent performance
> - **Use dedicated deployments** – Scale replicas based on your throughput needs

## Known Limitations

> [!warning]
> - **Video duration**: Maximum 60 seconds recommended for optimal performance
> - **Supported formats**: `.mp4` for video, `.ogg` (Opus) for audio
> - **Base64 size**: Total encoded payload should be under 10MB
> - **Deployment required**: Video models are not available on serverless; dedicated deployment required

#video-audio-input #qwen3-omni #ffmpeg #multimodal-models
