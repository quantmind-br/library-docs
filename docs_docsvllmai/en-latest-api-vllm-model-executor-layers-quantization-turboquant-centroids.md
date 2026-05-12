---
title: centroids - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/turboquant/centroids/
source: sitemap
fetched_at: 2026-05-07T21:27:45.878290085-03:00
rendered_js: false
word_count: 135
summary: This document provides the technical implementation for computing Lloyd-Max optimal scalar quantizer centroids and decision boundaries for the TurboQuant algorithm.
tags:
    - turboquant
    - quantization
    - lloyd-max
    - scalar-quantization
    - vllm
    - deep-learning-optimization
category: reference
---

## vllm.model\_executor.layers.quantization.turboquant.centroids [¶](#vllm.model_executor.layers.quantization.turboquant.centroids "Permanent link")

Lloyd-Max optimal scalar quantizer for TurboQuant.

After rotating a d-dimensional unit vector by a random orthogonal matrix, each coordinate approximately follows N(0, 1/d) for d &gt;= 64. We solve the Lloyd-Max conditions to find optimal centroids.

Based on: turboquant-pytorch/lloyd\_max.py (Zandieh et al.)

## \_trapz [¶](#vllm.model_executor.layers.quantization.turboquant.centroids._trapz "Permanent link")

Trapezoidal numerical integration (replaces scipy.integrate.quad).

Source code in `vllm/model_executor/layers/quantization/turboquant/centroids.py`

```
def_trapz(f, a: float, b: float, n: int = 200) -> float:
"""Trapezoidal numerical integration (replaces scipy.integrate.quad)."""
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h
```

## get\_centroids `cached` [¶](#vllm.model_executor.layers.quantization.turboquant.centroids.get_centroids "Permanent link")

Get precomputed Lloyd-Max centroids (cached).

Source code in `vllm/model_executor/layers/quantization/turboquant/centroids.py`

```
@lru_cache(maxsize=32)
defget_centroids(d: int, bits: int) -> torch.Tensor:
"""Get precomputed Lloyd-Max centroids (cached)."""
    centroids, _ = solve_lloyd_max(d, bits)
    return centroids
```

## solve\_lloyd\_max [¶](#vllm.model_executor.layers.quantization.turboquant.centroids.solve_lloyd_max "Permanent link")

Solve Lloyd-Max optimal quantizer for N(0, 1/d) distribution.

Parameters:

Name Type Description Default `d` `int`

Vector dimension (determines variance = 1/d).

*required* `bits` `int`

Number of quantization bits.

*required* `max_iter` `int`

Maximum Lloyd-Max iterations.

`200` `tol` `float`

Convergence tolerance.

`1e-10`

Returns:

Name Type Description `centroids` `Tensor`

Sorted tensor of 2^bits optimal centroids.

`boundaries` `Tensor`

Sorted tensor of 2^bits - 1 decision boundaries.

Source code in `vllm/model_executor/layers/quantization/turboquant/centroids.py`

```
defsolve_lloyd_max(
    d: int,
    bits: int,
    max_iter: int = 200,
    tol: float = 1e-10,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Solve Lloyd-Max optimal quantizer for N(0, 1/d) distribution.

    Args:
        d: Vector dimension (determines variance = 1/d).
        bits: Number of quantization bits.
        max_iter: Maximum Lloyd-Max iterations.
        tol: Convergence tolerance.

    Returns:
        centroids: Sorted tensor of 2^bits optimal centroids.
        boundaries: Sorted tensor of 2^bits - 1 decision boundaries.
    """
    n_levels = 2**bits
    sigma2 = 1.0 / d
    sigma = math.sqrt(sigma2)

    defpdf(x):
        return _gaussian_pdf(x, sigma2)

    lo, hi = -3.5 * sigma, 3.5 * sigma
    centroids = [lo + (hi - lo) * (i + 0.5) / n_levels for i in range(n_levels)]

    for _ in range(max_iter):
        boundaries = [
            (centroids[i] + centroids[i + 1]) / 2.0 for i in range(n_levels - 1)
        ]
        edges = [lo * 3] + boundaries + [hi * 3]
        new_centroids = []
        for i in range(n_levels):
            a, b = edges[i], edges[i + 1]
            num = _trapz(lambda x: x * pdf(x), a, b)
            den = _trapz(pdf, a, b)
            new_centroids.append(num / den if den > 1e-15 else centroids[i])

        if max(abs(new_centroids[i] - centroids[i]) for i in range(n_levels)) < tol:
            break
        centroids = new_centroids

    boundaries = [(centroids[i] + centroids[i + 1]) / 2.0 for i in range(n_levels - 1)]
    return (
        torch.tensor(centroids, dtype=torch.float32),
        torch.tensor(boundaries, dtype=torch.float32),
    )
```