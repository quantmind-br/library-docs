---
title: Get started with Unsloth Studio
url: https://unsloth.ai/docs/new/studio/start.md
source: llms
fetched_at: 2026-04-27T18:13:21.880960653-03:00
rendered_js: false
word_count: 2470
summary: Browser-based GUI for fine-tuning LLMs without code. Covers setup and four main areas: Model selection, Dataset preparation, Hyperparameter configuration, and Training settings.
tags:
    - llm-fine-tuning
    - studio-gui
    - unsloth
    - model-selection
    - dataset-handling
    - hyperparameters
    - lora-config
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Get started with Unsloth Studio

Local, browser-based GUI for fine-tuning LLMs without code. Wraps the full training pipeline: model loading, dataset formatting, hyperparameter config, and live training monitoring.

## Setup

Launch via local install or cloud. Follow [[098-new-studio-install|install instructions]] or use the [free Colab](https://unsloth.ai/docs/new/studio/..#google-colab-notebook). Local launch:

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Open `http://localhost:8888`. First launch requires creating a password. A brief onboarding wizard appears (model, dataset, settings) — skip anytime and configure manually.

## Studio Quickstart

Homepage has 4 areas: Model, Dataset, Parameters, Training/Config.

- **Easy model/data setup** from Hugging Face or local files
- **Flexible training** — QLoRA, LoRA, or full fine-tuning with pre-filled defaults
- **Config tools** for splits, column mapping, hyperparameters, YAML export
- **Live observability** — progress, GPU stats, charts, startup status

### 1. Select Model and Method

#### Model Type

| Type | Use Case |
| --- | --- |
| **Text** | Chat, instruction following, completion |
| **Vision** | Image + text (VLMs) |
| **Audio** | Speech / audio understanding |
| **Embeddings** | Sentence embeddings, retrieval |

#### Training Method

| Method | Description | VRAM |
| --- | --- | --- |
| **QLoRA** | 4-bit quantized base + LoRA adapter | Lowest |
| **LoRA** | Full-precision base + LoRA adapter | Medium |
| **Full Fine-tuning** | All weights trained | Highest |

Search Hugging Face Hub from the combobox. Local models in `~/.unsloth/studio/models` and HF cache also appear.

> [!warning] GGUF format models are inference only — excluded from training.

Model selection auto-fetches config and pre-fills hyperparameter defaults.

**HuggingFace Token** — paste for gated models (Llama, Gemma). Validated in real-time; invalid tokens show inline errors.

### 2. Dataset

Two tabs:

- **HuggingFace Hub** — live search, shows last-updated date per result
- **Local** — drag-and-drop or click to upload: `PDF`, `DOCX`, `JSONL`, `JSON`, `CSV`, `Parquet`. Previously uploaded datasets listed and auto-refreshed.

See [[060-get-started-fine-tuning-llms-guide-datasets-guide|Datasets Guide]] for details.

#### Format Selection

| Format | Columns / Structure |
| --- | --- |
| `auto` | Auto-detect format |
| `alpaca` | `instruction` / `input` / `output` |
| `chatml` | OpenAI-style `messages` array |
| `sharegpt` | ShareGPT-style conversations |

#### Splits and Slicing

- **Subset** — auto-populated from dataset card
- **Train split / Eval split** — choose splits; eval split enables Eval Loss chart during training
- **Dataset slice** — restrict to a row range (start/end index) for quick experiments

#### Column Mapping

If auto-mapping fails, a **Dataset Preview dialog** opens with sample rows. Assign each column to `instruction`, `input`, `output`, `image`, etc. Suggested mappings pre-filled where possible.

### 3. Hyperparameters

Grouped into collapsible sections. See [[061-get-started-fine-tuning-llms-guide-lora-hyperparameters-guide|LoRA Hyperparameters Guide]].

| Parameter | Default | Notes |
| --- | --- | --- |
| **Max Steps** | `0` | `0` = use Epochs instead |
| **Context Length** | `2048` | Range: 512 – 32768 |
| **Learning Rate** | `2e-4` | |

#### LoRA Settings

Hidden when Full Fine-tuning is selected.

| Parameter | Default | Notes |
| --- | --- | --- |
| **Rank** | `16` | Slider 4–128 |
| **Alpha** | `32` | Slider 4–256 |
| **Dropout** | `0.05` | |
| **LoRA Variant** | `LoRA` | `LoRA` / `RS-LoRA` / `LoftQ` |
| **Target Modules** | All on | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` |

For **Vision** models with image datasets, four additional checkboxes: Vision Layers, Language Layers, Attention Modules, MLP Modules.

#### Training Hyperparameters

**Optimization tab:**

| Parameter | Default |
| --- | --- |
| Epochs | 3 |
| Batch Size | 4 |
| Gradient Accumulation | 8 |
| Weight Decay | 0.01 |
| Optimizer | AdamW 8-bit |

**Schedule tab:**

| Parameter | Default |
| --- | --- |
| LR Scheduler | linear |
| Warmup Steps | 5 |
| Gradient Checkpointing | unsloth |
| Random Seed | 3407 |
| Save Steps | 0 |
| Eval Steps | 0 |
| Packing | false |
| Train on Completions | false |

**Logging tab:**

| Parameter | Default |
| --- | --- |
| Enable W&B | false |
| W&B Project | llm-finetuning |
| Enable TensorBoard | false |
| TensorBoard Dir | runs |
| Log Frequency | 10 |

> [!info] **Unsloth Gradient Checkpointing**: The `unsloth` option uses Unsloth's custom memory-efficient implementation, reducing VRAM significantly vs standard PyTorch. Recommended default. See [[103-blog-500k-context-length-fine-tuning|500K Context Length Fine-tuning]].

### 4. Training and Config

Bottom-right card: **Upload** (load `.yaml`), **Save** (export YAML), **Reset** (revert to model defaults), and **Start Training**.

Start Training stays disabled until model + dataset are configured. Validation errors appear inline (e.g., eval steps without eval split, text model with vision dataset).

#### Loading Screen

Full-page overlay with animated terminal showing phase updates:

- **Blue** — downloading model / dataset
- **Amber** — loading model / dataset
- **Blue** — configuring
- **Green** — training

Cancel anytime via the **x** button (confirmation dialog).

#### Training Progress and Observability

Overlay dismisses after first training step; live training view revealed. Complete when steps reach 100%.

**Status Panel (left):**

- **Epoch** — fractional (e.g. `Epoch 1.23`)
- **Progress bar** — step-based with percentage
- **Key metrics** — Loss (4dp), LR (scientific notation), Grad Norm, Model name, Method (`QLoRA`/`LoRA`/`Full`)
- **Timing** — elapsed, ETA, steps/sec, total tokens processed

**GPU Monitor (right):**

- **Utilization** — percentage bar
- **Temperature** — C bar
- **VRAM** — used / total GB
- **Power** — draw / limit watts

**Stopping Training** — **Stop Training** button in top-right; dialog offers **Stop & Save** (checkpoint) or **Cancel** (no checkpoint).

#### Charts

Four live charts:

1. **Training Loss** — raw values + EMA-smoothed line + running average
2. **Learning Rate** — schedule curve
3. **Gradient Norm** — over steps
4. **Eval Loss** — only when eval split configured

Chart settings (gear icon):

| Option | Default |
| --- | --- |
| Viewing window | Last N steps slider |
| EMA Smoothing | `0.6` |
| Show Raw | On |
| Show Smoothed | On |
| Show Average line | On |
| Scale (per series) | Linear / Log |
| Outlier clipping | No clip / p99 / p95 |

#### Config Files

Configs saved/loaded as YAML, auto-named:

```
{model}_{method}_{dataset}_{timestamp}.yaml
```

```yaml
training:
  max_steps: 0
  num_train_epochs: 3
  per_device_train_batch_size: 4
  ...

lora:
  r: 16
  lora_alpha: 32
  ...

logging:
  report_to: none
  ...
```

Enables reproducibility, sharing, and version control.

## Data Recipes - Quickstart

[[100-new-studio-data-recipe|Unsloth Data Recipes]] transforms uploaded documents (PDFs, CSVs) into usable datasets via a graph-node workflow (powered by NVIDIA [DataDesigner](https://github.com/NVIDIA-NeMo/DataDesigner)). Recipes stored locally in the browser.

Workflow:

1. Open recipes page; create or pick a recipe
2. Add blocks to define the dataset workflow
3. Click **Validate** to catch config issues
4. Run a preview to inspect sample rows
5. Run a full dataset build
6. Review progress in graph or **Executions** view
7. Select the resulting dataset in **Studio** and fine-tune

## Export - Quickstart

Export, save, or convert models to GGUF, Safetensors, or LoRA for deployment, sharing, or local inference (Unsloth, llama.cpp, Ollama, vLLM, etc.). Works with trained checkpoints or any existing model.

See [[101-new-studio-export|Export guide]].

## Chat - Quickstart

[[099-new-studio-chat|Unsloth Studio Chat]] runs models 100% offline.

- **Download + Run** — GGUFs, fine-tuned adapters, safetensors
- **Compare** model outputs side-by-side (Model Arena)
- **Upload** documents, images, audio in prompts
- **Tune** inference settings — temperature, top-p, top-k, system prompt

## Video Tutorial

> [!warning] Videos show older Studio versions, not reflective of current UI.

- [NVIDIA getting-started tutorial](https://www.youtube.com/watch?v=mmbkP8NARH4)
- [Install Unsloth Studio tutorial](https://youtu.be/1lEDuRJWHh4?si=GHaS77ZZPOGjn3GJ)

## Advanced Settings

### CLI Commands

```
Usage: cli.py [COMMAND]

Commands:
  train             Fine-tune a model
  inference         Run inference on a trained model
  export            Export a trained adapter
  list-checkpoints  List saved checkpoints
  ui                Launch the Unsloth Studio web UI
  studio            Launch the studio (alias)
```

### Project Structure

```
new-ui-prototype/
├── cli.py                     # CLI entry point
├── cli/                       # Typer CLI commands
│   └── commands/
│       ├── train.py
│       ├── inference.py
│       ├── export.py
│       ├── ui.py
│       └── studio.py
├── setup.sh                   # Bootstrap (Linux / WSL / Colab)
├── setup.ps1                  # Bootstrap (Windows native)
├── setup.bat                  # Wrapper to launch setup.ps1 via double-click
├── install_python_stack.py    # Cross-platform Python dependency installer
└── studio/
    ├── backend/
    │   ├── main.py            # FastAPI app & middleware
    │   ├── run.py             # Server launcher (uvicorn)
    │   ├── auth/              # Auth storage & JWT logic
    │   ├── routes/            # API route handlers
    │   │   ├── training.py
    │   │   ├── models.py
    │   │   ├── inference.py
    │   │   ├── datasets.py
    │   │   └── auth.py
    │   ├── models/            # Pydantic request/response schemas
    │   ├── core/              # Training engine & config
    │   ├── utils/             # Hardware detection, helpers
    │   └── requirements.txt
    ├── frontend/
    │   ├── src/
    │   │   ├── features/      # Feature modules
    │   │   │   ├── auth/      # Login / signup flow
    │   │   │   ├── training/  # Training config & monitoring
    │   │   │   ├── studio/    # Main studio workspace
    │   │   │   ├── chat/      # Inference chat UI
    │   │   │   ├── export/    # Model export flow
    │   │   │   └── onboarding/# Onboarding wizard
    │   │   ├── components/    # Shared UI components (shadcn)
    │   │   ├── hooks/         # Custom React hooks
    │   │   ├── stores/        # Zustand state stores
    │   │   └── types/         # TypeScript type definitions
    │   ├── package.json
    │   └── vite.config.ts
    └── tests/                 # Backend test suite
```

### API Reference

All endpoints require `Authorization: Bearer <token>` JWT header (except `/api/auth/*` and `/api/health`).

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/health` | Health check |
| `GET` | `/api/system` | System info (GPU, CPU, memory) |
| `POST` | `/api/auth/signup` | Create account (setup token required on first run) |
| `POST` | `/api/auth/login` | Login, receive JWT tokens |
| `POST` | `/api/auth/refresh` | Refresh expired access token |
| `GET` | `/api/auth/status` | Check if auth is initialized |
| `POST` | `/api/train/start` | Start training job |
| `POST` | `/api/train/stop` | Stop running training job |
| `POST` | `/api/train/reset` | Reset training state |
| `GET` | `/api/train/status` | Current training status |
| `GET` | `/api/train/metrics` | Training metrics (loss, LR, steps) |
| `GET` | `/api/train/stream` | SSE stream of real-time training progress |
| `GET` | `/api/models/` | List available models |
| `POST` | `/api/inference/chat` | Send chat message for inference |
| `GET` | `/api/datasets/` | List / manage datasets |

#unsloth #studio #fine-tuning #gui #llm
