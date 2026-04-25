# Qwen3-TTS Documentation Index

## Metadata Summary

| Property | Value |
|----------|-------|
| Source | https://github.com/QwenLM/Qwen3-TTS |
| Total Documents | 7 |
| Organization Date | 2026-04-20 |
| Organization Version | 1.0.0 |

---

## Document Index by Category

### Foundation (Get Started Here)

| Sequence | File | Title | Category |
|----------|------|-------|----------|
| 001 | `001-README.md` | README | Introduction & Overview |
| 002 | `002-finetuning-README.md` | Fine-Tuning Guide | Tutorial & How-To |

### Configuration

| Sequence | File | Title | Category |
|----------|------|-------|----------|
| 003 | `003-pyproject.toml` | Python Package Configuration | Configuration & Settings |

### Community & Support

| Sequence | File | Title | Category |
|----------|------|-------|----------|
| 004 | `004-.github-ISSUE-TEMPLATE-config.yml` | GitHub Issue Configuration | Meta & Resources |
| 005 | `005-.github-ISSUE-TEMPLATE-bug-report.yml` | Bug Report Template | Troubleshooting & Support |

### CI/CD & Automation

| Sequence | File | Title | Category |
|----------|------|-------|----------|
| 006 | `006-.github-workflows-translate.yaml` | Translation Workflow | Automation & Workflow |
| 007 | `007-.github-workflows-inactive.yaml` | Inactive Thread Management | Operations & Deployment |

---

## Quick Search by Topics

### Voice Generation & TTS
- **Primary**: `001-README.md` - Main documentation with voice clone, voice design, custom voice generation
- **Fine-tuning**: `002-finetuning-README.md` - Train custom voice models

### Models
- Qwen3-TTS-12Hz-1.7B-VoiceDesign
- Qwen3-TTS-12Hz-1.7B-CustomVoice
- Qwen3-TTS-12Hz-1.7B-Base
- Qwen3-TTS-12Hz-0.6B-CustomVoice
- Qwen3-TTS-12Hz-0.6B-Base
- Qwen3-TTS-Tokenizer-12Hz

### Languages Supported
Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian

### Installation & Dependencies
- **Python package**: `003-pyproject.toml` - qwen-tts v0.1.1
- **Dependencies**: transformers, accelerate, gradio, librosa, torchaudio, soundfile, sox, onnxruntime, einops

### GitHub Automation
- **Translation workflow**: `006-.github-workflows-translate.yaml`
- **Maintenance**: `007-.github-workflows-inactive.yaml`
- **Issue templates**: `004-.github-ISSUE-TEMPLATE-config.yml`, `005-.github-ISSUE-TEMPLATE-bug-report.yml`

---

## Learning Path

### 1. Foundation
Start here to understand Qwen3-TTS capabilities:
1. `001-README.md` - Overview, features, models, quickstart examples

### 2. Core Usage
Learn how to use the models:
1. `001-README.md` - Custom voice generation, voice design, voice clone, tokenizer
1. `002-finetuning-README.md` - Fine-tune for custom voices

### 3. Configuration
Understand the package setup:
1. `003-pyproject.toml` - Python package configuration

### 4. Reference
For CI/CD and advanced operations:
1. `006-.github-workflows-translate.yaml`
1. `007-.github-workflows-inactive.yaml`

### 5. Support
Get help and contribute:
1. `004-.github-ISSUE-TEMPLATE-config.yml`
1. `005-.github-ISSUE-TEMPLATE-bug-report.yml`

---

## File Listing

```
000-index.md                                      <- This file
001-README.md                                     <- Introduction & Overview
002-finetuning-README.md                          <- Tutorial & How-To
003-pyproject.toml                                <- Configuration & Settings
004-.github-ISSUE-TEMPLATE-config.yml             <- Meta & Resources
005-.github-ISSUE-TEMPLATE-bug-report.yml         <- Troubleshooting & Support
006-.github-workflows-translate.yaml              <- Automation & Workflow
007-.github-workflows-inactive.yaml               <- Operations & Deployment
metadata.json                                     <- Document metadata
```
