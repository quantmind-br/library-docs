---
title: Single-Turn Training Quickstart - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/quickstart-math
source: sitemap
fetched_at: 2026-04-27T20:15:55.06219401-03:00
rendered_js: false
word_count: 287
summary: This quickstart tutorial demonstrates how to train a small language model (Qwen3 0.6B) on the GSM8K dataset by first setting up the evaluation components and then launching a Reinforcement Fine-Tuning (RFT) job using the Eval Protocol SDK.
tags:
    - quickstart
    - language-model
    - gsm8k
    - eval-protocol
    - training
    - rft-job
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
In this quickstart, you'll train `Qwen3 0.6B` to solve mathematical reasoning problems from the GSM8K dataset.

## What you'll learn

- Set up and test an evaluator locally using the Eval Protocol SDK
- Launch an RFT job from the command line
- Monitor training progress and evaluate accuracy improvements

## Prerequisites

- Python 3.10+
- A Fireworks API key (stored in your shell or `.env`)
- Command-line access

## 1. Install dependencies and set up files

Clone the quickstart-gsm8k repository and install dependencies:

```bash
git clone https://github.com/eval-protocol/quickstart-gsm8k.git
cd quickstart-gsm8k
pip install -r requirements.txt
```

Create the `gsm8k_artifacts/` folder structure and copy files:

```bash
mkdir -p gsm8k_artifacts/{tests/pytest/gsm8k,development}
cp evaluation.py gsm8k_artifacts/tests/pytest/gsm8k/test_pytest_math_example.py
cp gsm8k_sample.jsonl gsm8k_artifacts/development/gsm8k_sample.jsonl
```

The repository includes:
- **Evaluator** (`evaluation.py`): Defines how to evaluate math answers
- **Dataset** (`gsm8k_sample.jsonl`): Contains example math problems to test on

Install the latest `eval-protocol` SDK, `pytest`, and `requests`:

```bash
python -m pip install --upgrade pip
python -m pip install pytest requests git+https://github.com/eval-protocol/python-sdk.git
```

Download the evaluator and dataset files by running this Python script:

```python
from pathlib import Path
import requests

ARTIFACT_ROOT = Path("gsm8k_artifacts")
TEST_PATH = ARTIFACT_ROOT / "tests" / "pytest" / "gsm8k" / "test_pytest_math_example.py"
DATASET_PATH = ARTIFACT_ROOT / "development" / "gsm8k_sample.jsonl"

files_to_download = {
    TEST_PATH: "https://raw.githubusercontent.com/eval-protocol/python-sdk/main/tests/pytest/gsm8k/test_pytest_math_example.py",
    DATASET_PATH: "https://raw.githubusercontent.com/eval-protocol/python-sdk/main/development/gsm8k_sample.jsonl",
}

for local_path, url in files_to_download.items():
    local_path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    local_path.write_bytes(response.content)
    print(f"Saved {url} -> {local_path}")
```

Expected output:

```
Saved https://raw.githubusercontent.com/.../test_pytest_math_example.py -> gsm8k_artifacts/tests/pytest/gsm8k/test_pytest_math_example.py
Saved https://raw.githubusercontent.com/.../gsm8k_sample.jsonl -> gsm8k_artifacts/development/gsm8k_sample.jsonl
```

## 2. Test your evaluator locally

Test your evaluator locally before launching training. Iterate on the evaluator until it gives the expected output.

## 3. Start training

Set your Fireworks API key:

```bash
export FIREWORKS_API_KEY="<your-fireworks-key>"
```

Launch the RFT job using the evaluator and dataset you registered:

```bash
cd ..
eval-protocol create rft \
    --base-model accounts/fireworks/models/qwen3-0p6b
```

The CLI outputs dashboard links for monitoring your training job in real-time.

## Monitor your training progress

Your RFT job is now running. Monitor progress using the dashboard links provided by the CLI.

### What's happening behind the scenes

1. **Evaluation registration**: The pytest script evaluates a GSM8K subset using numeric answer checking, then automatically registers both your evaluator and dataset with Fireworks
2. **RFT job creation**: The `create rft` command connects your registered evaluator and dataset to a Reinforcement Fine-Tuning job
3. **Continuous improvement**: As training progresses, evaluation scores reflect improved accuracy

## Next steps

> [!tip]
> For more advanced fine-tuning options, see the [Reinforcement Fine-Tuning documentation](https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models).
