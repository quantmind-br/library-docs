---
title: Transcribe audio - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/audio-transcriptions
source: sitemap
fetched_at: 2026-04-27T20:15:04.204075232-03:00
rendered_js: false
word_count: 936
summary: This document outlines the parameters and structure for making a request to an API, detailing inputs like audio files and various model settings, as well as the possible outputs including transcribed text, timestamps, and speaker diarization information.
tags:
    - api-request
    - audio-transcription
    - whisper-v3
    - model-settings
    - response-format
    - language-support
category: reference
optimized: true
optimized_at: 2026-04-27T23:04:00Z
---
# Transcribe Audio

POST `/v1/audio/transcriptions`

Transcribes or translates audio using Whisper-v3. Authentication via `Authorization: Bearer <API_KEY>`.

> [!note]
> Audio is resampled to 16kHz, downmixed to mono, and reformatted to 16-bit signed little-endian before transcription. Pre-converting files before sending can improve runtime.

## Request

### Body (multipart/form-data)

| Field | Type | Default | Description |
|---|---|---|---|
| `file` | `file \| string` | required | Audio file or public URL. Max 1 GB. Supports mp3, flac, wav. |
| `model` | `string` | `"whisper-v3"` | Model name |
| `language` | `string` | — | Target language code. See [Supported Languages](#supported-languages) |
| `prompt` | `string` | — | Input prompt to guide transcription style or specify custom words. E.g. `Um, here's, uh, what was recorded.` |
| `temperature` | `float \| list[float]` | `"0"` | Sampling temperature (0–1). Pass a list e.g. `0.0,0.2,0.4,0.6,0.8,1.0` to enable fallback decoding |
| `response_format` | `string` | `"json"` | Output format: `json`, `text`, `srt`, `verbose_json`, `vtt` |
| `timestamp_granularities[]` | `string` | `segment` | Granularities when `response_format=verbose_json`: `word`, `segment`, or `word,segment` |
| `diarize` | `boolean` | `false` | Enable speaker diarization. Requires `response_format=verbose_json` and `timestamp_granularities[]` to include `word` |
| `min_speakers` | `integer` | `1` | Minimum speakers to detect (requires `diarize=true`) |
| `max_speakers` | `integer` | `inf` | Maximum speakers to detect (requires `diarize=true`) |
| `vad` | `string` | — | VAD model: `silero` or `whisperx-pyannet` |
| `align_model` | `string` | — | Alignment model: `mms_fa` (multilingual), `tdnn_ffn` (English-only) |
| `preprocessing` | `string` | — | Audio preprocessing mode: `none`, `dynamic`, `soft_dynamic`, `bass_dynamic` |

## Response

### `json` / `text` / `srt` / `vtt`

| Field | Type | Description |
|---|---|---|
| `task` | `string` | Task performed: `transcribe` or `translate` |
| `language` | `string` | Language code(s) of transcribed text |
| `duration` | `float` | Audio duration in seconds |
| `text` | `string` | Transcribed text |
| `words` | `object[]` | Words with timestamps (if `verbose_json`) |
| `segments` | `object[]` | Segments with details (if `verbose_json`) |

### `verbose_json` — Word properties

| Field | Type | Description |
|---|---|---|
| `word` | `string` | Text content |
| `language` | `string` | Word language |
| `probability` | `float` | Probability |
| `hallucination_score` | `float` | Hallucination score |
| `start` | `float` | Start time (seconds) |
| `end` | `float` | End time (seconds) |
| `speaker` | `string` | Speaker label |

### `verbose_json` — Segment properties

| Field | Type | Description |
|---|---|---|
| `text` | `string` | Segment text |
| `language` | `string` | Segment language |
| `start` | `float` | Start time (seconds) |
| `end` | `float` | End time (seconds) |
| `speaker` | `string` | Speaker label |

## Supported Languages {#supported-languages}

| Code | Language | | Code | Language | | Code | Language |
|---|---|---|---|---|---|---|---|
| `en` | English | `ar` | Arabic | `bn` | Bengali |
| `zh` | Chinese | `sv` | Swedish | `sr` | Serbian |
| `de` | German | `it` | Italian | `az` | Azerbaijani |
| `es` | Spanish | `id` | Indonesian | `is` | Icelandic |
| `ru` | Russian | `hi` | Hindi | `sq` | Albanian |
| `ko` | Korean | `fi` | Finnish | `sw` | Swahili |
| `fr` | French | `vi` | Vietnamese | `gl` | Galician |
| `ja` | Japanese | `he` | Hebrew | `mr` | Marathi |
| `pt` | Portuguese | `uk` | Ukrainian | `pa` | Punjabi |
| `tr` | Turkish | `el` | Greek | `si` | Sinhala |
| `pl` | Polish | `ms` | Malay | `km` | Khmer |
| `ca` | Catalan | `cs` | Czech | `sn` | Shona |
| `nl` | Dutch | `ro` | Romanian | `yo` | Yoruba |
| `ta` | Tamil | `da` | Danish | `so` | Somali |
| `no` | Norwegian | `hu` | Hungarian | `af` | Afrikaans |
| `th` | Thai | `sk` | Slovak | `oc` | Occitan |
| `ur` | Urdu | `te` | Telugu | `ka` | Georgian |
| `hr` | Croatian | `fa` | Persian | `be` | Belarusian |
| `bg` | Bulgarian | `lv` | Latvian | `tg` | Tajik |
| `lt` | Lithuanian | `kn` | Kannada | `sd` | Sindhi |
| `la` | Latin | `et` | Estonian | `gu` | Gujarati |
| `mi` | Maori | `mk` | Macedonian | `am` | Amharic |
| `ml` | Malayalam | `br` | Breton | `yi` | Yiddish |
| `cy` | Welsh | `eu` | Basque | `lo` | Lao |
| `uz` | Uzbek | `ne` | Nepali | `fo` | Faroese |
| `tk` | Turkmen | `mn` | Mongolian | `ht` | Haitian Creole |
| `nn` | Nynorsk | `bs` | Bosnian | `ps` | Pashto |
| `mt` | Maltese | `kk` | Kazakh | `sa` | Sanskrit |
| `lb` | Luxembourgish | `hy` | Armenian | `my` | Myanmar |
| `bo` | Tibetan | `tl` | Tagalog | `mg` | Malagasy |
| `as` | Assamese | `tt` | Tatar | `haw` | Hawaiian |
| `ln` | Lingala | `ha` | Hausa | `ba` | Bashkir |
| `jw` | Javanese | `su` | Sundanese | `yue` | Cantonese |
| `zh-hant` | Traditional Chinese | `zh-hans` | Simplified Chinese | | |
