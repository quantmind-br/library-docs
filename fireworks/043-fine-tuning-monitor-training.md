---
title: Fine Tuning Monitor Training
url: https://docs.fireworks.ai/fine-tuning/monitor-training
source: sitemap
fetched_at: 2026-04-27T20:16:03.473670331-03:00
rendered_js: false
word_count: 954
summary: Comprehensive guide to monitoring Reinforcement Fine-Tuning (RFT) jobs using the Fireworks dashboard, including reward curves, rollout inspection, diagnostics, and cost optimization.
tags:
    - rft-monitoring
    - dashboard-guide
    - training-metrics
    - rollout-inspection
    - fine-tuning
    - diagnostics
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Monitor Training

The Fireworks dashboard provides comprehensive monitoring tools for RFT jobs: track progress, inspect individual rollouts, and debug issues.

## Accessing the monitoring dashboard

After creating your RFT job, use the dashboard link from CLI output:

```
Dashboard Links:
   RFT Job: https://app.fireworks.ai/dashboard/fine-tuning/reinforcement/abc123
```

Or navigate manually:
1. Go to [Fireworks Dashboard](https://app.fireworks.ai)
2. Click **Fine-Tuning** in the sidebar
3. Select your job from the list

## Overview metrics

| Metric | Description |
|--------|-------------|
| Elapsed time | How long the job has been running |
| Progress | Current epoch and step counts |
| Reward | Latest mean reward from rollouts |
| Model | Base model and output model names |

## Training metrics

### Reward curves

The most important metric in RFT. **What to look for**:

- **Upward trend** — Model is learning and improving
- **Plateauing** — Model may have converged; consider stopping or adjusting parameters
- **Decline** — Potential issue with evaluator or training instability
- **Spikes** — Could indicate noisy rewards or outliers in evaluation

### Training loss

- **Decreasing loss** — Normal learning behavior
- **Increasing loss** — Learning rate may be too high
- **Flat loss** — Model may not be learning; check evaluator rewards

### Evaluation metrics

If you provided an evaluation dataset:

- **Eval reward**: Model performance on held-out data
- **Generalization gap**: Difference between training and eval rewards

## Inspecting rollouts

### Rollout overview table

Click any **Epoch** in the training timeline, then click the **table icon** to view all rollouts for that step.

| Column | Description |
|--------|-------------|
| Row ID | Unique identifier for each dataset row used in this rollout |
| Prompt | The input prompt sent to the model |
| Messages | The model's generated response messages |
| Valid | Whether the rollout completed successfully without errors |
| Reason | Explanation if the rollout failed or was marked invalid |
| Score | Reward score assigned by your evaluator (0.0 to 1.0) |

**What to check**:
- Most rollouts succeeding (status: complete)
- Reward distribution makes sense (high for good outputs, low for bad)
- Many failures indicate evaluator issues
- All rewards identical may indicate evaluator is broken

### Individual rollout details

Click any row in the rollout table to see:
1. **Full prompt**: Exact messages sent to the model
2. **Model response**: Complete generated output
3. **Evaluation result**: Reward score and reasoning (if provided)
4. **Metadata**: Token counts, timing, temperature settings
5. **Tool calls**: For agentic rollouts with function calling

### Quality spot checks

**Early training (first epoch)**:
- Verify evaluator is working correctly
- Check that high-reward rollouts are actually good
- Ensure low-reward rollouts are actually bad

**Mid-training**:
- Confirm model quality is improving
- Look for new strategies or behaviors emerging
- Check that evaluator isn't being gamed

**Late training**:
- Verify final model quality meets your standards
- Check for signs of overfitting (memorizing training data)
- Ensure diversity in responses (not all identical)

## Live logs

Click the **Logs icon** next to the table icon to view real-time logs.

**Using logs for debugging**:
1. **Filter by error level**: Focus on `[ERROR]` and `[WARNING]` messages
2. **Search for rollout IDs**: Track specific rollouts through their lifecycle
3. **Look for patterns**: Repeated errors indicate systematic issues
4. **Check timestamps**: Correlate errors with metric changes

## Training diagnostics

### Available in the managed flow

- **Reward curves**: Mean reward over training steps
- **Training loss**: Policy loss over time
- **Rollout inspection**: Individual rollouts with scores, messages, and metadata

### Traces page

The **Traces** page provides per-rollout execution traces including timing, token counts, and evaluation results. Download trace data for offline analysis using the download button.

### Metrics not directly surfaced

The following diagnostics are not directly surfaced in the managed RFT dashboard today:

- **Filtering rates**: How many zero-variance groups were dropped per iteration
- **Effective batch size**: Actual number of training groups after filtering
- **Advantage magnitude and distribution**: Per-step advantage statistics
- **KL divergence**: Distance between the current policy and the reference model
- **Per-token importance sampling ratios**: Clipping frequency and magnitude

For richer per-step diagnostics, consider using [[002-fine-tuning-training-api-introduction|Training API]], which gives you full Python control over the training loop and allows you to log any metric you need.

## Performance optimization

### Speeding up training

If training is slower than expected, consider reducing rollout count or max tokens.

### Cost optimization

- **Start small**: Experiment with `qwen3-0p6b` before scaling to larger models
- **Reduce rollouts**: Use `--n 4` instead of 8
- **Shorter responses**: Lower `--max-tokens` to minimum needed
- **Fewer epochs**: Start with 1 epoch, only add more if needed
- **Efficient evaluators**: Minimize API calls and computation

## Stopping and resuming jobs

### Stopping a running job

1. Click **Cancel Job** in the dashboard
2. Or via CLI: `firectl rftj delete <job-id>`

The model state at the last checkpoint is saved and can be deployed.

### Using checkpoints

Continue from a checkpoint using [[038-fine-tuning-deploying-loras|warm start]]:

```bash
eval-protocol create rft \
  --warm-start-from accounts/your-account/models/previous-checkpoint \
  --output-model continued-training
```

This is useful for:
- Extending training after early stopping
- Trying different hyperparameters on a trained model
- Building on previous successful training runs

## Comparing multiple jobs

1. Navigate to **Fine-Tuning** dashboard
2. Select multiple jobs using checkboxes
3. Click **Compare**

This shows:
- Reward curves overlaid on same graph
- Parameter differences highlighted
- Final metrics comparison
- Training time and cost comparison

## Exporting metrics

### Via dashboard

1. Click **Export** button in job view
2. Choose format: CSV, JSON
3. Select metrics to export (rewards, loss, rollout data)

### Via API

```python
import requests

response = requests.get(
    f"https://api.fireworks.ai/v1/accounts/{account}/reinforcementFineTuningJobs/{job_id}/metrics",
    headers={"Authorization": f"Bearer {api_key}"}
)

metrics = response.json()
```

### Weights & Biases integration

If you enabled W&B when creating the job:

```bash
eval-protocol create rft \
  --wandb-project my-experiments \
  --wandb-entity my-org \
  ...
```

All metrics automatically sync to W&B for advanced analysis, comparison, and sharing.

#rft-monitoring #training-metrics #rollout-inspection
