---
title: Voice Mode | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode
source: crawler
fetched_at: 2026-04-24T17:00:02.747877535-03:00
rendered_js: false
word_count: 1502
summary: This document details how Hermes Agent supports full voice interaction across CLI and various messaging platforms like Discord and Telegram. It covers prerequisites, system dependencies, configuration options, and specific modes for voice input and audio output.
tags:
    - hermes-agent
    - voice-interaction
    - cli-mode
    - discord-integration
    - telegram-gateway
    - tts-streaming
    - config-guide
category: guide
---

Hermes Agent supports full voice interaction across CLI and messaging platforms. Talk to the agent using your microphone, hear spoken replies, and have live voice conversations in Discord voice channels.

If you want a practical setup walkthrough with recommended configurations and real usage patterns, see [Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before using voice features, make sure you have:

1. **Hermes Agent installed** — `pip install hermes-agent` (see [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation))
2. **An LLM provider configured** — run `hermes model` or set your preferred provider credentials in `~/.hermes/.env`
3. **A working base setup** — run `hermes` to verify the agent responds to text before enabling voice

tip

The `~/.hermes/` directory and default `config.yaml` are created automatically the first time you run `hermes`. You only need to create `~/.hermes/.env` manually for API keys.

## Overview[​](#overview "Direct link to Overview")

FeaturePlatformDescription**Interactive Voice**CLIPress Ctrl+B to record, agent auto-detects silence and responds**Auto Voice Reply**Telegram, DiscordAgent sends spoken audio alongside text responses**Voice Channel**DiscordBot joins VC, listens to users speaking, speaks replies back

## Requirements[​](#requirements "Direct link to Requirements")

### Python Packages[​](#python-packages "Direct link to Python Packages")

```bash
# CLI voice mode (microphone + audio playback)
pip install"hermes-agent[voice]"

# Discord + Telegram messaging (includes discord.py[voice] for VC support)
pip install"hermes-agent[messaging]"

# Premium TTS (ElevenLabs)
pip install"hermes-agent[tts-premium]"

# Local TTS (NeuTTS, optional)
python -m pip install-U neutts[all]

# Everything at once
pip install"hermes-agent[all]"
```

ExtraPackagesRequired For`voice``sounddevice`, `numpy`CLI voice mode`messaging``discord.py[voice]`, `python-telegram-bot`, `aiohttp`Discord & Telegram bots`tts-premium``elevenlabs`ElevenLabs TTS provider

Optional local TTS provider: install `neutts` separately with `python -m pip install -U neutts[all]`. On first use it downloads the model automatically.

info

`discord.py[voice]` installs **PyNaCl** (for voice encryption) and **opus bindings** automatically. This is required for Discord voice channel support.

### System Dependencies[​](#system-dependencies "Direct link to System Dependencies")

```bash
# macOS
brew install portaudio ffmpeg opus
brew install espeak-ng   # for NeuTTS

# Ubuntu/Debian
sudoaptinstall portaudio19-dev ffmpeg libopus0
sudoaptinstall espeak-ng   # for NeuTTS
```

DependencyPurposeRequired For**PortAudio**Microphone input and audio playbackCLI voice mode**ffmpeg**Audio format conversion (MP3 → Opus, PCM → WAV)All platforms**Opus**Discord voice codecDiscord voice channels**espeak-ng**Phonemizer backendLocal NeuTTS provider

### API Keys[​](#api-keys "Direct link to API Keys")

Add to `~/.hermes/.env`:

```bash
# Speech-to-Text — local provider needs NO key at all
# pip install faster-whisper          # Free, runs locally, recommended
GROQ_API_KEY=your-key                 # Groq Whisper — fast, free tier (cloud)
VOICE_TOOLS_OPENAI_KEY=your-key       # OpenAI Whisper — paid (cloud)

# Text-to-Speech (optional — Edge TTS and NeuTTS work without any key)
ELEVENLABS_API_KEY=***           # ElevenLabs — premium quality
# VOICE_TOOLS_OPENAI_KEY above also enables OpenAI TTS
```

tip

If `faster-whisper` is installed, voice mode works with **zero API keys** for STT. The model (~150 MB for `base`) downloads automatically on first use.

* * *

## CLI Voice Mode[​](#cli-voice-mode "Direct link to CLI Voice Mode")

### Quick Start[​](#quick-start "Direct link to Quick Start")

Start the CLI and enable voice mode:

```bash
hermes                # Start the interactive CLI
```

Then use these commands inside the CLI:

```text
/voice          Toggle voice mode on/off
/voice on       Enable voice mode
/voice off      Disable voice mode
/voice tts      Toggle TTS output
/voice status   Show current state
```

### How It Works[​](#how-it-works "Direct link to How It Works")

1. Start the CLI with `hermes` and enable voice mode with `/voice on`
2. **Press Ctrl+B** — a beep plays (880Hz), recording starts
3. **Speak** — a live audio level bar shows your input: `● [▁▂▃▅▇▇▅▂] ❯`
4. **Stop speaking** — after 3 seconds of silence, recording auto-stops
5. **Two beeps** play (660Hz) confirming the recording ended
6. Audio is transcribed via Whisper and sent to the agent
7. If TTS is enabled, the agent's reply is spoken aloud
8. Recording **automatically restarts** — speak again without pressing any key

This loop continues until you press **Ctrl+B** during recording (exits continuous mode) or 3 consecutive recordings detect no speech.

tip

The record key is configurable via `voice.record_key` in `~/.hermes/config.yaml` (default: `ctrl+b`).

### Silence Detection[​](#silence-detection "Direct link to Silence Detection")

Two-stage algorithm detects when you've finished speaking:

1. **Speech confirmation** — waits for audio above the RMS threshold (200) for at least 0.3s, tolerating brief dips between syllables
2. **End detection** — once speech is confirmed, triggers after 3.0 seconds of continuous silence

If no speech is detected at all for 15 seconds, recording stops automatically.

Both `silence_threshold` and `silence_duration` are configurable in `config.yaml`. You can also disable the record start/stop beeps with `voice.beep_enabled: false`.

### Streaming TTS[​](#streaming-tts "Direct link to Streaming TTS")

When TTS is enabled, the agent speaks its reply **sentence-by-sentence** as it generates text — you don't wait for the full response:

1. Buffers text deltas into complete sentences (min 20 chars)
2. Strips markdown formatting and `<think>` blocks
3. Generates and plays audio per sentence in real-time

### Hallucination Filter[​](#hallucination-filter "Direct link to Hallucination Filter")

Whisper sometimes generates phantom text from silence or background noise ("Thank you for watching", "Subscribe", etc.). The agent filters these out using a set of 26 known hallucination phrases across multiple languages, plus a regex pattern that catches repetitive variations.

* * *

## Gateway Voice Reply (Telegram & Discord)[​](#gateway-voice-reply-telegram--discord "Direct link to Gateway Voice Reply (Telegram & Discord)")

If you haven't set up your messaging bots yet, see the platform-specific guides:

- [Telegram Setup Guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)
- [Discord Setup Guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord)

Start the gateway to connect to your messaging platforms:

```bash
hermes gateway        # Start the gateway (connects to configured platforms)
hermes gateway setup  # Interactive setup wizard for first-time configuration
```

### Discord: Channels vs DMs[​](#discord-channels-vs-dms "Direct link to Discord: Channels vs DMs")

The bot supports two interaction modes on Discord:

ModeHow to TalkMention RequiredSetup**Direct Message (DM)**Open the bot's profile → "Message"NoWorks immediately**Server Channel**Type in a text channel where the bot is presentYes (`@botname`)Bot must be invited to the server

**DM (recommended for personal use):** Just open a DM with the bot and type — no @mention needed. Voice replies and all commands work the same as in channels.

**Server channels:** The bot only responds when you @mention it (e.g. `@hermesbyt4 hello`). Make sure you select the **bot user** from the mention popup, not the role with the same name.

tip

To disable the mention requirement in server channels, add to `~/.hermes/.env`:

```bash
DISCORD_REQUIRE_MENTION=false
```

Or set specific channels as free-response (no mention needed):

```bash
DISCORD_FREE_RESPONSE_CHANNELS=123456789,987654321
```

### Commands[​](#commands "Direct link to Commands")

These work in both Telegram and Discord (DMs and text channels):

```text
/voice          Toggle voice mode on/off
/voice on       Voice replies only when you send a voice message
/voice tts      Voice replies for ALL messages
/voice off      Disable voice replies
/voice status   Show current setting
```

### Modes[​](#modes "Direct link to Modes")

ModeCommandBehavior`off``/voice off`Text only (default)`voice_only``/voice on`Speaks reply only when you send a voice message`all``/voice tts`Speaks reply to every message

Voice mode setting is persisted across gateway restarts.

### Platform Delivery[​](#platform-delivery "Direct link to Platform Delivery")

PlatformFormatNotes**Telegram**Voice bubble (Opus/OGG)Plays inline in chat. ffmpeg converts MP3 → Opus if needed**Discord**Native voice bubble (Opus/OGG)Plays inline like a user voice message. Falls back to file attachment if voice bubble API fails

* * *

## Discord Voice Channels[​](#discord-voice-channels "Direct link to Discord Voice Channels")

The most immersive voice feature: the bot joins a Discord voice channel, listens to users speaking, transcribes their speech, processes through the agent, and speaks the reply back in the voice channel.

### Setup[​](#setup "Direct link to Setup")

#### 1. Discord Bot Permissions[​](#1-discord-bot-permissions "Direct link to 1. Discord Bot Permissions")

If you already have a Discord bot set up for text (see [Discord Setup Guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord)), you need to add voice permissions.

Go to the [Discord Developer Portal](https://discord.com/developers/applications) → your application → **Installation** → **Default Install Settings** → **Guild Install**:

**Add these permissions to the existing text permissions:**

PermissionPurposeRequired**Connect**Join voice channelsYes**Speak**Play TTS audio in voice channelsYes**Use Voice Activity**Detect when users are speakingRecommended

**Updated Permissions Integer:**

LevelIntegerWhat's IncludedText only`274878286912`View Channels, Send Messages, Read History, Embeds, Attachments, Threads, ReactionsText + Voice`274881432640`All above + Connect, Speak

**Re-invite the bot** with the updated permissions URL:

```text
https://discord.com/oauth2/authorize?client_id=YOUR_APP_ID&scope=bot+applications.commands&permissions=274881432640
```

Replace `YOUR_APP_ID` with your Application ID from the Developer Portal.

warning

Re-inviting the bot to a server it's already in will update its permissions without removing it. You won't lose any data or configuration.

#### 2. Privileged Gateway Intents[​](#2-privileged-gateway-intents "Direct link to 2. Privileged Gateway Intents")

In the [Developer Portal](https://discord.com/developers/applications) → your application → **Bot** → **Privileged Gateway Intents**, enable all three:

IntentPurpose**Presence Intent**Detect user online/offline status**Server Members Intent**Map voice SSRC identifiers to Discord user IDs**Message Content Intent**Read text message content in channels

All three are required for full voice channel functionality. **Server Members Intent** is especially critical — without it, the bot cannot identify who is speaking in the voice channel.

#### 3. Opus Codec[​](#3-opus-codec "Direct link to 3. Opus Codec")

The Opus codec library must be installed on the machine running the gateway:

```bash
# macOS (Homebrew)
brew install opus

# Ubuntu/Debian
sudoaptinstall libopus0
```

The bot auto-loads the codec from:

- **macOS:** `/opt/homebrew/lib/libopus.dylib`
- **Linux:** `libopus.so.0`

#### 4. Environment Variables[​](#4-environment-variables "Direct link to 4. Environment Variables")

```bash
# ~/.hermes/.env

# Discord bot (already configured for text)
DISCORD_BOT_TOKEN=your-bot-token
DISCORD_ALLOWED_USERS=your-user-id

# STT — local provider needs no key (pip install faster-whisper)
# GROQ_API_KEY=your-key            # Alternative: cloud-based, fast, free tier

# TTS — optional. Edge TTS and NeuTTS need no key.
# ELEVENLABS_API_KEY=***      # Premium quality
# VOICE_TOOLS_OPENAI_KEY=***  # OpenAI TTS / Whisper
```

### Start the Gateway[​](#start-the-gateway "Direct link to Start the Gateway")

```bash
hermes gateway        # Start with existing configuration
```

The bot should come online in Discord within a few seconds.

### Commands[​](#commands-1 "Direct link to Commands")

Use these in the Discord text channel where the bot is present:

```text
/voice join      Bot joins your current voice channel
/voice channel   Alias for /voice join
/voice leave     Bot disconnects from voice channel
/voice status    Show voice mode and connected channel
```

info

You must be in a voice channel before running `/voice join`. The bot joins the same VC you're in.

### How It Works[​](#how-it-works-1 "Direct link to How It Works")

When the bot joins a voice channel, it:

1. **Listens** to each user's audio stream independently
2. **Detects silence** — 1.5s of silence after at least 0.5s of speech triggers processing
3. **Transcribes** the audio via Whisper STT (local, Groq, or OpenAI)
4. **Processes** through the full agent pipeline (session, tools, memory)
5. **Speaks** the reply back in the voice channel via TTS

### Text Channel Integration[​](#text-channel-integration "Direct link to Text Channel Integration")

When the bot is in a voice channel:

- Transcripts appear in the text channel: `[Voice] @user: what you said`
- Agent responses are sent as text in the channel AND spoken in the VC
- The text channel is the one where `/voice join` was issued

### Echo Prevention[​](#echo-prevention "Direct link to Echo Prevention")

The bot automatically pauses its audio listener while playing TTS replies, preventing it from hearing and re-processing its own output.

### Access Control[​](#access-control "Direct link to Access Control")

Only users listed in `DISCORD_ALLOWED_USERS` can interact via voice. Other users' audio is silently ignored.

```bash
# ~/.hermes/.env
DISCORD_ALLOWED_USERS=284102345871466496
```

* * *

## Configuration Reference[​](#configuration-reference "Direct link to Configuration Reference")

### config.yaml[​](#configyaml "Direct link to config.yaml")

```yaml
# Voice recording (CLI)
voice:
record_key:"ctrl+b"# Key to start/stop recording
max_recording_seconds:120# Maximum recording length
auto_tts:false# Auto-enable TTS when voice mode starts
beep_enabled:true# Play record start/stop beeps
silence_threshold:200# RMS level (0-32767) below which counts as silence
silence_duration:3.0# Seconds of silence before auto-stop

# Speech-to-Text
stt:
provider:"local"# "local" (free) | "groq" | "openai"
local:
model:"base"# tiny, base, small, medium, large-v3
# model: "whisper-1"              # Legacy: used when provider is not set

# Text-to-Speech
tts:
provider:"edge"# "edge" (free) | "elevenlabs" | "openai" | "neutts" | "minimax"
edge:
voice:"en-US-AriaNeural"# 322 voices, 74 languages
elevenlabs:
voice_id:"pNInz6obpgDQGcFmaJgB"# Adam
model_id:"eleven_multilingual_v2"
openai:
model:"gpt-4o-mini-tts"
voice:"alloy"# alloy, echo, fable, onyx, nova, shimmer
base_url:"https://api.openai.com/v1"# optional: override for self-hosted or OpenAI-compatible endpoints
neutts:
ref_audio:''
ref_text:''
model: neuphonic/neutts-air-q4-gguf
device: cpu
```

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

```bash
# Speech-to-Text providers (local needs no key)
# pip install faster-whisper        # Free local STT — no API key needed
GROQ_API_KEY=...                    # Groq Whisper (fast, free tier)
VOICE_TOOLS_OPENAI_KEY=...         # OpenAI Whisper (paid)

# STT advanced overrides (optional)
STT_GROQ_MODEL=whisper-large-v3-turbo    # Override default Groq STT model
STT_OPENAI_MODEL=whisper-1               # Override default OpenAI STT model
GROQ_BASE_URL=https://api.groq.com/openai/v1     # Custom Groq endpoint
STT_OPENAI_BASE_URL=https://api.openai.com/v1    # Custom OpenAI STT endpoint

# Text-to-Speech providers (Edge TTS and NeuTTS need no key)
ELEVENLABS_API_KEY=***             # ElevenLabs (premium quality)
# VOICE_TOOLS_OPENAI_KEY above also enables OpenAI TTS

# Discord voice channel
DISCORD_BOT_TOKEN=...
DISCORD_ALLOWED_USERS=...
```

### STT Provider Comparison[​](#stt-provider-comparison "Direct link to STT Provider Comparison")

ProviderModelSpeedQualityCostAPI Key**Local**`base`Fast (depends on CPU/GPU)GoodFreeNo**Local**`small`MediumBetterFreeNo**Local**`large-v3`SlowBestFreeNo**Groq**`whisper-large-v3-turbo`Very fast (~0.5s)GoodFree tierYes**Groq**`whisper-large-v3`Fast (~1s)BetterFree tierYes**OpenAI**`whisper-1`Fast (~1s)GoodPaidYes**OpenAI**`gpt-4o-transcribe`Medium (~2s)BestPaidYes

Provider priority (automatic fallback): **local** &gt; **groq** &gt; **openai**

### TTS Provider Comparison[​](#tts-provider-comparison "Direct link to TTS Provider Comparison")

ProviderQualityCostLatencyKey Required**Edge TTS**GoodFree~1sNo**ElevenLabs**ExcellentPaid~2sYes**OpenAI TTS**GoodPaid~1.5sYes**NeuTTS**GoodFreeDepends on CPU/GPUNo

NeuTTS uses the `tts.neutts` config block above.

* * *

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### "No audio device found" (CLI)[​](#no-audio-device-found-cli 'Direct link to "No audio device found" (CLI)')

PortAudio is not installed:

```bash
brew install portaudio    # macOS
sudoaptinstall portaudio19-dev  # Ubuntu
```

### Bot doesn't respond in Discord server channels[​](#bot-doesnt-respond-in-discord-server-channels "Direct link to Bot doesn't respond in Discord server channels")

The bot requires an @mention by default in server channels. Make sure you:

1. Type `@` and select the **bot user** (with the #discriminator), not the **role** with the same name
2. Or use DMs instead — no mention needed
3. Or set `DISCORD_REQUIRE_MENTION=false` in `~/.hermes/.env`

### Bot joins VC but doesn't hear me[​](#bot-joins-vc-but-doesnt-hear-me "Direct link to Bot joins VC but doesn't hear me")

- Check your Discord user ID is in `DISCORD_ALLOWED_USERS`
- Make sure you're not muted in Discord
- The bot needs a SPEAKING event from Discord before it can map your audio — start speaking within a few seconds of joining

### Bot hears me but doesn't respond[​](#bot-hears-me-but-doesnt-respond "Direct link to Bot hears me but doesn't respond")

- Verify STT is available: install `faster-whisper` (no key needed) or set `GROQ_API_KEY` / `VOICE_TOOLS_OPENAI_KEY`
- Check the LLM model is configured and accessible
- Review gateway logs: `tail -f ~/.hermes/logs/gateway.log`

### Bot responds in text but not in voice channel[​](#bot-responds-in-text-but-not-in-voice-channel "Direct link to Bot responds in text but not in voice channel")

- TTS provider may be failing — check API key and quota
- Edge TTS (free, no key) is the default fallback
- Check logs for TTS errors

### Whisper returns garbage text[​](#whisper-returns-garbage-text "Direct link to Whisper returns garbage text")

The hallucination filter catches most cases automatically. If you're still getting phantom transcripts:

- Use a quieter environment
- Adjust `silence_threshold` in config (higher = less sensitive)
- Try a different STT model