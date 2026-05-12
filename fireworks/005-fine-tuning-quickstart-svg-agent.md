---
title: Remote Agent Quickstart - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/quickstart-svg-agent
source: sitemap
fetched_at: 2026-04-27T20:16:02.408388807-03:00
rendered_js: false
word_count: 756
summary: This quickstart guides users through setting up and running Reinforcement Fine-Tuning (RFT) training to generate SVG drawings. It details the process from local installation and testing using Eval Protocol to launching the remote training job on Fireworks.
tags:
    - svg-generation
    - remote-training
    - eval-protocol
    - fireworks-ai
    - rft-tuning
    - quickstart
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Train an agent to generate SVG drawings using remote rollout processing. Your agent runs in a remote server (Vercel) while Fireworks handles the training.

## What You'll Learn

- **Apply RFT to production agents** — Train models that work with remote servers and existing infrastructure
- **Remote rollout processing** — Connect your production environment to Fireworks RFT using Eval Protocol
- **Monitor and debug training** — Track progress, inspect rollouts, and debug issues with live logs

## 1. Installation

1. **Clone the quickstart repo**:

```bash
git clone git@github.com:eval-protocol/quickstart.git
cd quickstart
```

2. **Install Eval Protocol**:

```bash
pip install "eval-protocol[svgbench]"
```

3. **Environment Setup**:

Copy the `env.example` file and fill in your API keys:

```bash
cp evaluator/env.example evaluator/.env
```

Edit `evaluator/.env`:

```
FIREWORKS_API_KEY=your-fireworks-key-here
OPENAI_API_KEY=your-openai-key-here
```

For more details on Fireworks Secret Management, see [[064-fine-tuning-using-secret-in-evaluator|using secret in evaluator]].

## 2. Test your evaluator locally

**Terminal 1** - Start the local UI server:

**Terminal 2** - Kick off the test:

```bash
cd evaluator
ep local-test
```

This command discovers and runs your `@evaluation_test` with pytest. The test uses the Vercel remote server:

```python
rollout_processor=RemoteRolloutProcessor(
    remote_base_url="https://vercel-svg-server-ts.vercel.app",
)
```

If you want to use a local development Vercel server instead, see [Local Development Server](#local-development-server).

> [!note]
> - If your evaluation setup has custom system dependencies (e.g., Chromium), add a `Dockerfile`. When you run `ep local-test`, it will build an image and run `pytest` inside Docker.
> - If you don't need Docker, `ep local-test` runs pytest on your host machine by default.
> - Force host execution with: `ep local-test --ignore-docker`.

### Dockerfile constraints for RFT evaluators

RFT evaluators run in sandboxed environments. Your Dockerfile must follow these constraints:

**Base image:**
- Only Debian-based images are supported (e.g., Debian, Ubuntu, or `python:3.x-slim`)
- Alpine, CentOS, and other non-Debian distros are not supported

**Supported instructions:**
- `FROM`: Base image (required, only one allowed)
- `RUN`: Execute commands
- `COPY` / `ADD`: Copy files into the image
- `WORKDIR`: Set working directory
- `USER`: Set the user
- `ENV`: Set environment variables
- `CMD` / `ENTRYPOINT`: Set the start command
- `ARG`: Build-time variables

**Unsupported features:**

| Feature | Status |
|---------|--------|
| Non-Debian base images | ❌ Not supported |
| Multi-stage builds | ❌ Not supported |
| `EXPOSE` | ⚠️ Ignored |
| `VOLUME` | ⚠️ Ignored |

**Example Dockerfile:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    chromium \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-vs"]
```

### Expected Test Output

Navigate to [http://localhost:8000](http://localhost:8000) to see the Eval Protocol UI.

```
INFO:eval_protocol.pytest.remote_rollout_processor:Found status log for rollout democratic-way-12: Rollout democratic-way-12 completed
INFO:eval_protocol.pytest.remote_rollout_processor:Found Fireworks log for rollout democratic-way-12 with status code 100.0
INFO:eval_protocol.adapters.fireworks_tracing:Successfully converted 1 traces to evaluation rows | 3/8 [00:19<00:22, 4.52s/rollout]
...
Runs (Parallel): 100%|████████████████████████████████████████████| 1/1 [00:31<00:00, 31.07s/run]
PASSED
```

![Eval Protocol Logs Interface](https://mintcdn.com/fireworksai/XAK4ji8XrlzPoITj/images/ep_logs.png?fit=max&auto=format&n=XAK4ji8XrlzPoITj&q=85&s=e995ac057588a0cc621de0476ed198c2)

## 3. Start training with a single command

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-0p6b \
  --chunk-size 10
```

This command:
1. Uploads secrets — reads your `.env` and uploads API keys as Fireworks secrets
2. Uploads evaluator — packages and uploads your evaluation code
3. Waits for build — polls evaluator status until ACTIVE (timeout: 10 minutes)
4. Creates dataset — uploads your `svgbench_dataset.jsonl`
5. Launches RFT job — starts reinforcement fine-tuning with your evaluator

> [!tip]
> For a complete list of available RFT flags, see [Fireworks RFT Command Documentation](https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-create).

**Changing Evaluators**: To upload a new version:

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-0p6b \
  --chunk-size 10 \
  --force
```

**Evaluator Upload Timing Out**: If your evaluator takes longer than 10 minutes to build, monitor the evaluator upload at the link and run the command again when ACTIVE.

## 4. Monitor Training Progress

After successful job creation:

```
✅ Created Reinforcement Fine-tuning Job
   name: accounts/pyroworks/reinforcementFineTuningJobs/sdnld4yn

📊 Dashboard Links:
   Evaluator: https://app.fireworks.ai/dashboard/evaluators/test-svgagent-test-svg-generation-evaluation
   Dataset:   https://app.fireworks.ai/dashboard/datasets/svgbench-dataset
   RFT Job:   https://app.fireworks.ai/dashboard/fine-tuning/reinforcement/sdnld4yn
```

Click on the **RFT Job** link to view real-time training progress, epoch counts, and rollout data.

### Training Results

After training, you should see performance improvements reflected in training metrics:
![SVG Agent Training Progress](https://mintcdn.com/fireworksai/XAK4ji8XrlzPoITj/images/graph.png?fit=max&auto=format&n=XAK4ji8XrlzPoITj&q=85&s=ca1852e3a9d3019952b047b38d28316b)

### SVG Quality Improvement

**Before (1st Epoch):**
![SVG Generation - Before Training](https://mintcdn.com/fireworksai/XAK4ji8XrlzPoITj/images/before.png?fit=max&auto=format&n=XAK4ji8XrlzPoITj&q=85&s=b4753fbb936a452d05ebac0346289319)

**After (8th Epoch):**
![SVG Generation - After Training](https://mintcdn.com/fireworksai/XAK4ji8XrlzPoITj/images/after.png?fit=max&auto=format&n=XAK4ji8XrlzPoITj&q=85&s=19b5b5461d91f8d34a4cf08eacce1b6c)

## Debugging Tips

### Rollout Overview

Click any **Epoch** or **Step** in the training dashboard, then the **table icon** to see all rollouts. Check if any rollouts failed and for what reason.
![Rollout Overview Table](https://mintcdn.com/fireworksai/XAK4ji8XrlzPoITj/images/rollouts.png?fit=max&auto=format&n=XAK4ji8XrlzPoITj&q=85&s=6725e79f84cbf189b5497f0afc8b7822)

### Individual Rollout Details

Click a specific row in the rollout table to see the prompt and model response. Copy and paste the generated SVG code to render it yourself.
![Individual Rollout Details](https://mintcdn.com/fireworksai/XAK4ji8XrlzPoITj/images/rollout_details.png?fit=max&auto=format&n=XAK4ji8XrlzPoITj&q=85&s=f154026928bf9ae5ee22abc76820ea2e)

### Live Log Streaming

Click **View Logs** to see logs streamed in real-time. Useful for debugging rollout errors.
![Live Log Streaming](https://mintcdn.com/fireworksai/XAK4ji8XrlzPoITj/images/logs.png?fit=max&auto=format&n=XAK4ji8XrlzPoITj&q=85&s=ab84e6d4713e93d8416961d44017d4ba)

## Additional resources

- [Discord Server](https://discord.gg/mMqQxvFD9A) - Come talk to us in the #eval-protocol channel!
- [Eval Protocol Documentation](https://evalprotocol.io/introduction)
- [Remote Rollout Processor Tutorial](https://evalprotocol.io/tutorial/remote-rollout-processor)
- [SVGBench Dataset](https://github.com/johnbean393/SVGBench)

## Appendix

### How Remote Rollout Processing Works

Eval Protocol enables **reinforcement learning that meets you where you are**. Your remote server is only responsible for:

- **Executing rollouts** - Run your agent logic (in this case, SVG generation from text prompts)
- **Logging to tracing** - Send structured logs to `tracing.fireworks.ai` for evaluation

> 📖 Learn More: For a complete deep-dive, see the [Remote Rollout Processor Tutorial](https://evalprotocol.io/tutorial/remote-rollout-processor).

### Local Development Server

```bash
cd vercel_svg_server_ts
vercel dev
```

Swap out `remote_base_url` to point to the local server:

```python
rollout_processor=RemoteRolloutProcessor(
    remote_base_url="http://localhost:3000",
)
```

> See [Vercel CLI documentation](https://vercel.com/docs/cli/dev) for more information.
