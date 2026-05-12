---
title: 'Loss Functions - Fireworks AI Docs'
url: https://docs.fireworks.ai/fine-tuning/training-api/loss-functions
source: sitemap
fetched_at: 2026-04-27T20:15:29.346341271-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - training-api
    - loss-functions
    - custom-loss
    - gradient-descent
    - datum-building
category: guide
word_count: 694
---
## What this is

The Training API supports two loss computation methods:

1. **Built-in losses** via `forward_backward` with a string identifier (e.g. `"cross_entropy"`) — fastest, no extra forward pass needed.
2. **Custom losses** via `forward_backward_custom` with an arbitrary Python function — flexible, supports any differentiable objective at the cost of an additional forward pass.

## Built-in loss: cross_entropy

```
result = training_client.forward_backward(datums, "cross_entropy").result()
```

Computes standard next-token prediction loss on the server side.

For a **forward-only pass** (e.g. reference logprobs without weight updates):

```
result = training_client.forward(datums, "cross_entropy").result()
ref_logprobs = [result.loss_fn_outputs[i]["logprobs"].data for i in range(len(datums))]
```

## Custom losses: forward_backward_custom

`forward_backward_custom` lets you implement any objective in Python. You provide the loss computation; the API handles the forward pass on remote GPUs, passes logprobs back, then sends gradients back for the backward pass.

### How it works

1. Call `training_client.forward_backward_custom(datums, loss_fn)`.
2. Trainer runs a forward pass on the GPU and returns per-token logprobs.
3. Logprobs are converted to PyTorch tensors with `requires_grad=True`.
4. Your `loss_fn` is called with datums and logprobs.
5. API calls `loss.backward()` to compute `d_loss/d_logprob` gradients.
6. Gradients sent back to the trainer GPU for the model backward pass.

Your loss function runs **locally** (on your machine), while forward and backward passes run on **remote GPUs**.

### Loss function signature

```python
def loss_fn(
    data: list[tinker.Datum],
    logprobs_list: list[torch.Tensor],
) -> tuple[torch.Tensor, dict[str, float]]:
    """
    Args:
        data: The same datums you passed to forward_backward_custom.
              Access token weights via data[i].loss_fn_inputs["weights"].data
        logprobs_list: Per-token log-probabilities from the forward pass.
              Each tensor has requires_grad=True. Shape: (seq_len,) per sequence.

    Returns:
        loss: A scalar tensor. Must be differentiable w.r.t. logprobs_list entries.
        metrics: A dict of float values for logging (not used for training).
    """
```

### Key rules

- **`logprobs_list[i]`** has `requires_grad=True` — loss must be differentiable through it.
- **Use `torch.dot()`** to compute weighted sums — correctly propagates gradients through logprobs.
- **Return a scalar tensor** as loss and a `dict[str, float]` as metrics.
- **Access token weights** via `data[i].loss_fn_inputs["weights"].data` — `0` for prompt tokens, `1` for response tokens.

## Building datums

### Using tinker_cookbook (weight-based)

```python
import tinker
import torch
from tinker_cookbook.supervised.common import datum_from_model_input_weights

tokens = [101, 2054, 2003, ...]
weights = torch.zeros(len(tokens), dtype=torch.float32)
weights[prompt_len:] = 1.0  # Only train on response tokens

datum = datum_from_model_input_weights(tinker.ModelInput.from_ints(tokens), weights, max_length=8192)
```

### Using tinker.Datum directly (target-token-based)

For RL-style objectives (routing matrices, custom `loss_fn_inputs`):

```python
import tinker

model_input_len = len(tokens) - 1
datum = tinker.Datum(
    model_input=tinker.ModelInput.from_ints(tokens[:-1]),
    loss_fn_inputs={
        "target_tokens": tinker.TensorData(
            data=tokens[1:], dtype="int64", shape=[model_input_len],
        ),
    },
)
```

## Example: simple cross-entropy

```python
def cross_entropy_loss(data, logprobs_list):
    total_loss = torch.tensor(0.0)
    for i, logprobs in enumerate(logprobs_list):
        weights = torch.tensor(data[i].loss_fn_inputs["weights"].data, dtype=torch.float32)
        min_len = min(len(logprobs), len(weights))
        weighted_sum = torch.dot(logprobs[:min_len].float(), weights[:min_len])
        total_loss = total_loss - weighted_sum  # Negative log-likelihood
    loss = total_loss / len(logprobs_list)
    return loss, {"cross_entropy": loss.item()}

result = training_client.forward_backward_custom(datums, cross_entropy_loss).result()
```

## Example: GRPO with KL penalty

```python
def make_grpo_loss(rewards, ref_logprobs, kl_beta=0.001):
    advantages = compute_advantages(rewards)
    ref_tensors = [torch.tensor(lp, dtype=torch.float32) for lp in ref_logprobs]

    def loss_fn(data, logprobs_list):
        total_loss = torch.tensor(0.0)
        for i in range(len(logprobs_list)):
            weights = torch.tensor(data[i].loss_fn_inputs["weights"].data, dtype=torch.float32)
            pi = logprobs_list[i][:len(weights)]
            ref = ref_tensors[i][:len(weights)]

            pg_loss = -advantages[i] * torch.dot(pi.float(), weights)
            kl_term = torch.dot((pi - ref).float(), weights)
            total_loss = total_loss + pg_loss + kl_beta * kl_term

        return total_loss / len(logprobs_list), {"loss": (total_loss / len(logprobs_list)).item()}

    return loss_fn
```

## Example: DPO margin loss

```python
import torch.nn.functional as F

def make_dpo_loss(ref_chosen, ref_rejected, beta=0.1):
    ref_c = torch.tensor(ref_chosen, dtype=torch.float32)
    ref_r = torch.tensor(ref_rejected, dtype=torch.float32)

    def loss_fn(data, logprobs_list):
        pi_c, pi_r = logprobs_list[0], logprobs_list[1]
        w_c = torch.tensor(data[0].loss_fn_inputs["weights"].data, dtype=torch.float32)
        w_r = torch.tensor(data[1].loss_fn_inputs["weights"].data, dtype=torch.float32)

        margin = (torch.dot(pi_c.float(), w_c) - torch.dot(ref_c, w_c)) - \
                 (torch.dot(pi_r.float(), w_r) - torch.dot(ref_r, w_r))

        return -F.logsigmoid(beta * margin), {"margin": margin.item()}

    return loss_fn
```

## Built-in loss methods: GRPO vs DAPO vs GSPO-token

When using the managed RFT flow or the cookbook's RL recipe, three built-in loss methods are available via `--rl-loss-method`:

| Method | Clipping | KL penalty | Loss aggregation | Importance sampling |
|---|---|---|---|---|
| `grpo` (default) | Symmetric `[0.8, 1.2]` | Yes (`0.001`) | Token-mean | Token-level |
| `dapo` | Asymmetric `[0.8, 1.28]` | No | Token-mean | Token-level |
| `gspo-token` | Very tight `[1-3e-4, 1+4e-4]` | No | Seq-mean-token-mean | Sequence-level |

- **GRPO** ([arXiv:2402.03300](https://arxiv.org/abs/2402.03300)) — safe default with KL regularization.
- **DAPO** ([arXiv:2503.14476](https://arxiv.org/abs/2503.14476)) — removes KL, asymmetric clipping for more aggressive exploration in the improve direction.
- **GSPO-token** ([arXiv:2507.18071](https://arxiv.org/abs/2507.18071)) — sequence-level importance ratios, extremely tight clipping. The `seq-mean-token-mean` aggregation normalizes per-sequence before averaging, reducing bias toward longer responses.

> [!info]
> For Training API users implementing custom loss functions via `forward_backward_custom`, these methods serve as reference implementations. See [[044-fine-tuning-parameter-tuning#loss-method]] for guidance on choosing each method.

## Applying the optimizer step

```
training_client.forward_backward_custom(datums, loss_fn).result()
training_client.optim_step(
    tinker.AdamParams(
        learning_rate=1e-5,
        beta1=0.9,
        beta2=0.999,
        eps=1e-8,
        weight_decay=0.01,
    )
).result()
```

For gradient accumulation, call `forward_backward_custom` multiple times before `optim_step`:

```
for micro_batch in micro_batches:
    training_client.forward_backward_custom(micro_batch, loss_fn).result()

# One optimizer step after accumulating gradients
training_client.optim_step(tinker.AdamParams(learning_rate=1e-5, ...)).result()
```

## Gradient accumulation normalization

When accumulating micro-batches before `optim_step`, normalization can happen inside your loss function or server-side via `grad_accumulation_normalization`. Use only one:

```
training_client.forward_backward_custom(datums, loss_fn).result()
training_client.optim_step(
    tinker.AdamParams(learning_rate=1e-5, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.01),
    grad_accumulation_normalization="num_loss_tokens",
).result()
```

| Mode | Divides by | Best for |
|---|---|---|
| `"num_loss_tokens"` | Total non-zero-grad tokens across accumulated micro-batches | Raw-sum token-level losses, such as RL/GRPO-style objectives |
| `"num_sequences"` | Total sequences with at least one non-zero-grad token | Raw-sum sequence-level objectives |
| `None` | Nothing | Losses that already return per-token or per-sequence means (SFT, DPO, ORPO) |

### Choosing the right mode

- **Raw sum over tokens** → `"num_loss_tokens"`
- **Raw sum over sequences** → `"num_sequences"`
- **Already a mean** → leave unset

### Recipe defaults

| Recipe | Default | Rationale |
|---|---|---|
| SFT | `None` | SFT loss already normalized client-side |
| GRPO / RL | `"num_loss_tokens"` | RL losses use server-side per-token normalization by default |
| DPO | `None` | DPO loss already normalized client-side |
| ORPO | `None` | ORPO loss already normalized client-side |

## Common pitfalls

- **Token-weight misalignment** silently breaks objective semantics — truncate to `min_len`.
- **Ignoring per-step diagnostics** makes instability hard to attribute — log metrics from every train step.
- **Forgetting `.result()`** — all Tinker API calls return futures. Without `.result()`, errors are silently swallowed.
- **Non-differentiable loss** — if your loss doesn't depend on `logprobs_list` entries through differentiable ops, gradients will be zero.

<!--THE END-->