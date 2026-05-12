---
title: Translate audio - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/audio-translations
source: sitemap
fetched_at: 2026-04-27T20:15:03.477872871-03:00
rendered_js: false
word_count: 842
summary: This document details the parameters and structure for using a Fireworks API, which supports audio transcription and translation. It outlines accepted file formats, configurable models (VAD and alignment), various response formats, and lists all supported source languages for translation to English.
tags:
    - api-key
    - audio-transcription
    - translation-api
    - request-parameters
    - response-structure
    - language-support
category: reference
optimized: true
optimized_at: 2026-04-27T23:04:00Z
---
# Translate Audio

POST `/v1/audio/translations`

Translates audio from any supported language to English using Whisper-v3. Authentication via `Authorization: Bearer <API_KEY>`.

> [!note]
> Audio is resampled to 16kHz, downmixed to mono, and reformatted to 16-bit signed little-endian before processing. Pre-converting files before sending can improve runtime.

## Request

### Body (multipart/form-data)

| Field | Type | Default | Description |
|---|---|---|---|
| `file` | `file \| string` | required | Audio file or public URL. Max 1 GB. Supports mp3, flac, wav. |
| `model` | `string` | `"whisper-v3"` | Model name |
| `language` | `string` | — | Source language code. See [Supported Languages](#supported-languages) |
| `prompt` | `string` | — | Input prompt to guide transcription style or specify custom words |
| `temperature` | `float \| list[float]` | `"0"` | Sampling temperature. Pass a list to enable fallback decoding |
| `response_format` | `string` | `"json"` | Output format: `json`, `text`, `srt`, `verbose_json`, `vtt` |
| `timestamp_granularities[]` | `string` | `segment` | Granularities when `response_format=verbose_json`: `word`, `segment`, or `word,segment` |
| `vad` | `string` | — | VAD model: `silero` or `whisperx-pyannet` |
| `align_model` | `string` | — | Alignment model: `mms_fa` (multilingual), `tdnn_ffn` (English-only) |
| `preprocessing` | `string` | — | Audio preprocessing mode: `none`, `dynamic`, `soft_dynamic`, `bass_dynamic` |

## Response

### `json` / `text` / `srt` / `vtt`

| Field | Type | Description |
|---|---|---|
| `task` | `string` | Task performed: `transcribe` or `translate` |
| `language` | `string` | Language of the translated text |
| `duration` | `float` | Audio duration in seconds |
| `text` | `string` | Translated text |
| `words` | `object[]` | Words with timestamps (if `verbose_json`) |
| `segments` | `object[]` | Segments with details (if `verbose_json`) |

### `verbose_json` — Word properties

| Field | Type | Description |
|---|---|---|
| `word` | `string` | Text content |
| `start` | `float` | Start time (seconds) |
| `end` | `float` | End time (seconds) |

### `verbose_json` — Segment properties

| Field | Type | Description |
|---|---|---|
| `text` | `string` | Segment text |
| `language` | `string` | Segment language |
| `start` | `float` | Start time (seconds) |
| `end` | `float` | End time (seconds) |

## Supported Languages {#supported-languages}

Translation is from one of the following languages to English:

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
