---
title: Unsloth Updates
url: https://unsloth.ai/docs/new/changelog.md
source: llms
fetched_at: 2026-04-27T18:13:27.841473765-03:00
rendered_js: false
word_count: 1939
summary: Comprehensive update log for Unsloth: UI redesigns, model support (Qwen3.6, Kimi K2.6, Gemma 4), and bug fixes.
tags:
    - updates
    - unsloth-studio
    - model-releases
    - ui-redesign
    - gemma-4
    - qwen3-6
    - llm-enhancements
category: guide
optimized: true
optimized_at: 2026-04-27T21:27:00Z
---

# Unsloth Updates

To use latest changes, [[098-new-studio-install|update Unsloth]].

## 2026-04-23 — Brand New UI Redesign (v0.1.37-beta)

- Collapsible sidebar (community feedback)
- Delete chats and search past conversations
- **Preserve Thinking toggle** for supported models (e.g., Qwen3.6)
- Cleaner, more consistent design with easier navigation
- Expanded Settings page (profile picture, name, more)
- No more entering Hugging Face token twice
- **gpt-oss**: low/medium/high thinking toggles
- Latest llama.cpp prebuilt, even on Linux CUDA
- Bug, consistency, and stability fixes
- **Kimi-K2.6** can now run
- Experimental API support (guides/announcement coming)
- Qwen3.6-27B already supported for running and training

## 2026-04-22 — Qwen3.6-27B + Kimi K2.6

- [[022-models-qwen3.6|Qwen3.6-27B]]: run (18GB RAM) + fine-tune in Unsloth Studio
- [[015-models-kimi-k2.6|Kimi K2.6]]: run (350GB RAM)

## 2026-04-16 — Qwen3.6

- [[022-models-qwen3.6|Qwen3.6]]: run + fine-tune in Unsloth Studio. 23GB RAM. Strongest mid-sized LLM on nearly all benchmarks.

## 2026-04-11 — Gemma 4 Update + MiniMax-M2.7

- Gemma 4 GGUFs updated with Google's official chat template fixes (improved tool-calling) + latest llama.cpp fixes. Update llama.cpp, re-download quants to fix `unused token` issues.
- [[016-models-minimax-m27|MiniMax-M2.7]]: run locally with GGUFs, 4-bit quant on 128GB RAM/unified memory. [MiniMax-M2.7 GGUF](https://huggingface.co/unsloth/MiniMax-M2.7-GGUF)

## 2026-04-08 — Gemma 4 Fixes

[[007-models-gemma-4-train|Full guide and notebooks]]. Bugs are universal (affected all training packages) and did **not** originate from Unsloth. Unsloth identified and fixed them.

- **8GB VRAM** to train **Gemma-4-E2B** locally
- Unsloth trains Gemma 4 **~1.5x faster, ~60% less VRAM** than FA2

### Gemma 4 Training Fixes

1. **Gradient accumulation** — no more loss explosions (was 300-400; expected 10-15)
2. **IndexError** fix for **26B** and **31B** inference in `transformers`
3. **Gibberish outputs** fix for E2B/E4B when `use_cache=False` ([transformers#45242](https://github.com/huggingface/transformers/issues/45242))
4. **float16 audio overflow** fix from `-1e9` values

If losses above **13-15** (e.g., 100, 300), gradient accumulation is handled incorrectly. Fixed in both Unsloth and Unsloth Studio.

### Gemma 4 Quant Re-uploads

Re-download required. Issues **not caused by Unsloth**:

1. CUDA: buffer overlap check before fusing — critical `<unused24>` fix ([llama.cpp#21566](https://github.com/ggml-org/llama.cpp/pull/21566))
2. `kv-cache`: attention rotation for heterogeneous iSWA ([#21513](https://github.com/ggml-org/llama.cpp/pull/21513))
3. `vocab`: byte token handling to BPE detokenizer ([#21488](https://github.com/ggml-org/llama.cpp/pull/21488))
4. `convert`: set `"add bos" == True` ([#21500](https://github.com/ggml-org/llama.cpp/pull/21500))
5. `common`: Gemma 4 specialized parser ([#21418](https://github.com/ggml-org/llama.cpp/pull/21418))
6. `llama-model`: read `final_logit_softcapping` ([#21390](https://github.com/ggml-org/llama.cpp/pull/21390))
7. `llama`: custom newline split ([#21406](https://github.com/ggml-org/llama.cpp/pull/21406))

### Unsloth Studio Updates

- **Speculative decoding** support (ngram-mod, on by default)
- Llama.cpp updated with all Gemma 4 fixes
- Qwen3.5 and Gemma 4 training fixes
- Gemma 4 model export/save enabled
- Hardened sandbox security for terminal/python tools
- Recipes use model loaded in Chat
- Empty chat threads fix on navigation/tab switch
- Non-LLM recipes enabled; Data tab moved first in executions
- Reuse HF cached repo casing to prevent duplicate downloads

## 2026-04-03 — Google Gemma 4 (v0.1.36-beta)

- [[008-models-gemma-4|Gemma 4]]: run and train in Unsloth
- Intel Mac support
- Pre-compiled llama.cpp binaries with 2 Gemma 4 fixes:
  - vocab: fix Gemma4 tokenizer ([#21343](https://github.com/ggml-org/llama.cpp/pull/21343))
  - fix: gemma 4 template ([#21326](https://github.com/ggml-org/llama.cpp/pull/21326))
- Tool calls for smaller models: more stable, no cutoff
- Pre-compiled binaries: Windows, Linux, Mac, WSL (CPU + GPU)
- Speculative Decoding for non-vision models (Gemma-4 and Qwen3.5 are vision, excluded)
- Context length properly applied
- Web search returns actual content, not summaries
- 90% reduced HF API calls (fewer rate limits)

## 2026-03-31 — +50% Tool Call Accuracy

- Tool calls: **+30% to +80% more accurate** across all models
- Web search returns actual content
- Tool call limit increased: 25 (was 10)
- Better termination (less looping/repetition)
- More tool call healing and de-duplication (no XML leaking)

| Metric | Before | After |
|--------|--------|-------|
| XML leaks in response | 10/10 | 0/10 |
| URL fetches used | 0 | 4/10 runs |
| Runs with correct song names | 0/10 | 2/10 |
| Avg tool calls | 5.5 | 3.8 |
| Avg response time | 12.3s | 9.8s |

### New Features

- **Custom folders** for any GGUFs (Advanced Settings > Chat > Custom Folders)
- **Update button** now visible
- Install script styling updated
- Preliminary **automatic multi-GPU support** for inference and training
- Intel Macs work out of the box

### Performance

- Fixed timeouts on large model downloads
- Fixed Hugging Face rate limiting (90% fewer API calls)
- Fixed bun on Windows, faster installs

## 2026-03-27 — Important Updates

- **Inference 20-30% faster** — tool-calling and repeat penalty no longer slow inference below `llama-server`/`llama.cpp` speeds
- **Auto-detects older models** from LM Studio, Hugging Face, etc.
- **Token/s calculated correctly** — no longer includes startup time
- **CPU usage spikes fixed** — inline querier identity no longer changes every render
- **Shutdown X button** — closes properly; launch from shortcut opens terminal
- Better tool-calling and websearch
- Updated docs: [[098-new-studio-install|deleting models, uninstalling]]
- Cleaner install/setup logging (Windows + Linux), supports `--verbose`
- Training history now viewable

## 2026-03-25 — First Release Post Unsloth Studio

- **Update**: `unsloth studio update`
- **Windows** CPU/GPU works seamlessly
- **App shortcuts** for Windows, macOS, Linux
- **Pre-compiled `llama.cpp` binaries** + `mamba_ssm` — 6x faster installs, <300MB
- **50% reduced installation** (-7GB+ savings), 2x faster installs, 50% smaller pypi
- **Tool calling improved** — better llama.cpp parsing, no raw tool markup, faster inference, Tool Outputs panel, timers
- MacOS/CPU: [[100-new-studio-data-recipe|Data Recipes]] with multi-file upload
- **AMD support** preliminary (Linux only, auto-detects)
- **Settings sidebar redesign** — Model, Sampling, Tools, Preferences
- **Context length** adjustable (llama.cpp uses exact context via `--fit on`)
- **Multi-file upload** — PDF, DOCX, TXT, MD with backend extraction, saved uploads, improved previews
- **Colab** with free T4 GPUs fixed ([try it](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb)), 20x faster with pre-compiled binaries
- **Chat observability** — llama-server timings, context-window usage bar, richer source hover cards
- **Better UX** — clickable links, better LaTeX parsing, tool/code/web tooltips
- **LiteLLM** — Unsloth Studio/Unsloth **NOT** affected by LiteLLM compromise (Nemo Data Designer only used up to 1.80, removed entirely)
- One-line install: `curl -fsSL https://unsloth.ai/install.sh | sh`

### Fixes

- Windows: silent exits, Anaconda/conda-forge crashes, non-NVIDIA installs, stale-venv checks
- System prompts fixed for non-GGUF text/vision inference
- Persistent system prompts and presets across reloads
- GGUF export expanded — full fine-tunes (not just LoRA/PEFT), better base model resolution
- Chat scroll/layout fixes — scroll-position during generation, thinking-panel layout shift, viewport jumps
- Smarter port conflict detection — loopback detection, blocking process identification, clearer fallback messages

## 2026-03-17 — New Tool Calling + Windows Stability

- Claude Artifacts: HTML execution in chat (e.g., snake game)
- +30% more accurate tool calls (especially small models) + timer
- Tool + Web Search outputs can be saved + toggle auto healing
- Windows CPU works, Mac more seamless, faster/smaller installs

---

# Agent Instructions: Querying This Documentation

If you need additional information not on this page, query dynamically:

```
GET https://unsloth.ai/docs/new/changelog.md?ask=<question>
```

Question should be specific, self-contained, natural language. Returns direct answer with relevant excerpts and sources.

#unsloth-studio #model-releases #gemma-4 #qwen3.6 #changelog
