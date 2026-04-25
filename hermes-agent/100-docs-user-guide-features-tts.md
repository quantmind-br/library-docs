---
title: Voice & TTS | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/tts
source: crawler
fetched_at: 2026-04-24T17:00:07.601685271-03:00
rendered_js: false
word_count: 546
summary: This document provides a comprehensive guide to Hermes Agent's capabilities for handling voice communication, detailing configuration options for both Text-to-Speech (TTS) generation and Speech-to-Text (STT) transcription across various platforms.
tags:
    - tts
    - stt
    - voice-generation
    - transcription
    - configuration
    - api-provider
    - hermes-agent
category: guide
---

Hermes Agent supports both text-to-speech output and voice message transcription across all messaging platforms.

Nous Subscribers

If you have a paid [Nous Portal](https://portal.nousresearch.com) subscription, OpenAI TTS is available through the [**Tool Gateway**](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway) without a separate OpenAI API key. Run `hermes model` or `hermes tools` to enable it.

## Text-to-Speech[​](#text-to-speech "Direct link to Text-to-Speech")

Convert text to speech with nine providers:

ProviderQualityCostAPI Key**Edge TTS** (default)GoodFreeNone needed**ElevenLabs**ExcellentPaid`ELEVENLABS_API_KEY`**OpenAI TTS**GoodPaid`VOICE_TOOLS_OPENAI_KEY`**MiniMax TTS**ExcellentPaid`MINIMAX_API_KEY`**Mistral (Voxtral TTS)**ExcellentPaid`MISTRAL_API_KEY`**Google Gemini TTS**ExcellentFree tier`GEMINI_API_KEY`**xAI TTS**ExcellentPaid`XAI_API_KEY`**NeuTTS**GoodFree (local)None needed**KittenTTS**GoodFree (local)None needed

### Platform Delivery[​](#platform-delivery "Direct link to Platform Delivery")

PlatformDeliveryFormatTelegramVoice bubble (plays inline)Opus `.ogg`DiscordVoice bubble (Opus/OGG), falls back to file attachmentOpus/MP3WhatsAppAudio file attachmentMP3CLISaved to `~/.hermes/audio_cache/`MP3

### Configuration[​](#configuration "Direct link to Configuration")

```yaml
# In ~/.hermes/config.yaml
tts:
provider:"edge"# "edge" | "elevenlabs" | "openai" | "minimax" | "mistral" | "gemini" | "xai" | "neutts" | "kittentts"
speed:1.0# Global speed multiplier (provider-specific settings override this)
edge:
voice:"en-US-AriaNeural"# 322 voices, 74 languages
speed:1.0# Converted to rate percentage (+/-%)
elevenlabs:
voice_id:"pNInz6obpgDQGcFmaJgB"# Adam
model_id:"eleven_multilingual_v2"
openai:
model:"gpt-4o-mini-tts"
voice:"alloy"# alloy, echo, fable, onyx, nova, shimmer
base_url:"https://api.openai.com/v1"# Override for OpenAI-compatible TTS endpoints
speed:1.0# 0.25 - 4.0
minimax:
model:"speech-2.8-hd"# speech-2.8-hd (default), speech-2.8-turbo
voice_id:"English_Graceful_Lady"# See https://platform.minimax.io/faq/system-voice-id
speed:1# 0.5 - 2.0
vol:1# 0 - 10
pitch:0# -12 - 12
mistral:
model:"voxtral-mini-tts-2603"
voice_id:"c69964a6-ab8b-4f8a-9465-ec0925096ec8"# Paul - Neutral (default)
gemini:
model:"gemini-2.5-flash-preview-tts"# or gemini-2.5-pro-preview-tts
voice:"Kore"# 30 prebuilt voices: Zephyr, Puck, Kore, Enceladus, Gacrux, etc.
xai:
voice_id:"eve"# xAI TTS voice (see https://docs.x.ai/docs/api-reference#tts)
language:"en"# ISO 639-1 code
sample_rate:24000# 22050 / 24000 (default) / 44100 / 48000
bit_rate:128000# MP3 bitrate; only applies when codec=mp3
# base_url: "https://api.x.ai/v1"   # Override via XAI_BASE_URL env var
neutts:
ref_audio:''
ref_text:''
model: neuphonic/neutts-air-q4-gguf
device: cpu
kittentts:
model: KittenML/kitten-tts-nano-0.8-int8   # 25MB int8; also: kitten-tts-micro-0.8 (41MB), kitten-tts-mini-0.8 (80MB)
voice: Jasper                               # Jasper, Bella, Luna, Bruno, Rosie, Hugo, Kiki, Leo
speed:1.0# 0.5 - 2.0
clean_text:true# Expand numbers, currencies, units
```

**Speed control**: The global `tts.speed` value applies to all providers by default. Each provider can override it with its own `speed` setting (e.g., `tts.openai.speed: 1.5`). Provider-specific speed takes precedence over the global value. Default is `1.0` (normal speed).

### Telegram Voice Bubbles & ffmpeg[​](#telegram-voice-bubbles--ffmpeg "Direct link to Telegram Voice Bubbles & ffmpeg")

Telegram voice bubbles require Opus/OGG audio format:

- **OpenAI, ElevenLabs, and Mistral** produce Opus natively — no extra setup
- **Edge TTS** (default) outputs MP3 and needs **ffmpeg** to convert:
- **MiniMax TTS** outputs MP3 and needs **ffmpeg** to convert for Telegram voice bubbles
- **Google Gemini TTS** outputs raw PCM and uses **ffmpeg** to encode Opus directly for Telegram voice bubbles
- **xAI TTS** outputs MP3 and needs **ffmpeg** to convert for Telegram voice bubbles
- **NeuTTS** outputs WAV and also needs **ffmpeg** to convert for Telegram voice bubbles
- **KittenTTS** outputs WAV and also needs **ffmpeg** to convert for Telegram voice bubbles

```bash
# Ubuntu/Debian
sudoaptinstall ffmpeg

# macOS
brew install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

Without ffmpeg, Edge TTS, MiniMax TTS, NeuTTS, and KittenTTS audio are sent as regular audio files (playable, but shown as a rectangular player instead of a voice bubble).

tip

If you want voice bubbles without installing ffmpeg, switch to the OpenAI, ElevenLabs, or Mistral provider.

## Voice Message Transcription (STT)[​](#voice-message-transcription-stt "Direct link to Voice Message Transcription (STT)")

Voice messages sent on Telegram, Discord, WhatsApp, Slack, or Signal are automatically transcribed and injected as text into the conversation. The agent sees the transcript as normal text.

ProviderQualityCostAPI Key**Local Whisper** (default)GoodFreeNone needed**Groq Whisper API**Good–BestFree tier`GROQ_API_KEY`**OpenAI Whisper API**Good–BestPaid`VOICE_TOOLS_OPENAI_KEY` or `OPENAI_API_KEY`

Zero Config

Local transcription works out of the box when `faster-whisper` is installed. If that's unavailable, Hermes can also use a local `whisper` CLI from common install locations (like `/opt/homebrew/bin`) or a custom command via `HERMES_LOCAL_STT_COMMAND`.

### Configuration[​](#configuration-1 "Direct link to Configuration")

```yaml
# In ~/.hermes/config.yaml
stt:
provider:"local"# "local" | "groq" | "openai" | "mistral"
local:
model:"base"# tiny, base, small, medium, large-v3
openai:
model:"whisper-1"# whisper-1, gpt-4o-mini-transcribe, gpt-4o-transcribe
mistral:
model:"voxtral-mini-latest"# voxtral-mini-latest, voxtral-mini-2602
```

### Provider Details[​](#provider-details "Direct link to Provider Details")

**Local (faster-whisper)** — Runs Whisper locally via [faster-whisper](https://github.com/SYSTRAN/faster-whisper). Uses CPU by default, GPU if available. Model sizes:

ModelSizeSpeedQuality`tiny`~75 MBFastestBasic`base`~150 MBFastGood (default)`small`~500 MBMediumBetter`medium`~1.5 GBSlowerGreat`large-v3`~3 GBSlowestBest

**Groq API** — Requires `GROQ_API_KEY`. Good cloud fallback when you want a free hosted STT option.

**OpenAI API** — Accepts `VOICE_TOOLS_OPENAI_KEY` first and falls back to `OPENAI_API_KEY`. Supports `whisper-1`, `gpt-4o-mini-transcribe`, and `gpt-4o-transcribe`.

**Mistral API (Voxtral Transcribe)** — Requires `MISTRAL_API_KEY`. Uses Mistral's [Voxtral Transcribe](https://docs.mistral.ai/capabilities/audio/speech_to_text/) models. Supports 13 languages, speaker diarization, and word-level timestamps. Install with `pip install hermes-agent[mistral]`.

**Custom local CLI fallback** — Set `HERMES_LOCAL_STT_COMMAND` if you want Hermes to call a local transcription command directly. The command template supports `{input_path}`, `{output_dir}`, `{language}`, and `{model}` placeholders.

### Fallback Behavior[​](#fallback-behavior "Direct link to Fallback Behavior")

If your configured provider isn't available, Hermes automatically falls back:

- **Local faster-whisper unavailable** → Tries a local `whisper` CLI or `HERMES_LOCAL_STT_COMMAND` before cloud providers
- **Groq key not set** → Falls back to local transcription, then OpenAI
- **OpenAI key not set** → Falls back to local transcription, then Groq
- **Mistral key/SDK not set** → Skipped in auto-detect; falls through to next available provider
- **Nothing available** → Voice messages pass through with an accurate note to the user