---
title: partition_rules - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/partition_rules/
source: sitemap
fetched_at: 2026-05-07T21:16:19.172508961-03:00
rendered_js: false
word_count: 58
summary: A context manager utility that temporarily registers custom partition rules for the Inductor scheduler to influence graph segmentation during model compilation.
tags:
    - inductor
    - graph-partitioning
    - context-manager
    - compilation-rules
    - pytorch-optimization
category: api
---

Context manager to temporarily register Inductor partition rules.

Registers custom partition rules for specified operators, forcing the Inductor scheduler to partition the graph at these operators. The rules are automatically restored to their previous state on exit.

Parameters:

Name Type Description Default `splitting_ops` `list[str] | None`

List of operator names to partition on.

*required*

Source code in `vllm/compilation/partition_rules.py`

```
@contextlib.contextmanager
definductor_partition_rule_context(
    splitting_ops: list[str] | None,
) -> Generator[None, None, None]:
"""Context manager to temporarily register Inductor partition rules.

    Registers custom partition rules for specified operators, forcing the
    Inductor scheduler to partition the graph at these operators. The rules
    are automatically restored to their previous state on exit.

    Args:
        splitting_ops: List of operator names to partition on.
    """
    if not splitting_ops:
        logger.debug("No partition ops provided; skipping rule registration.")
        yield
        return

    # Save current state before registering

    saved_splitting_ops: list[str] = list(
        torch._inductor.config.custom_should_partition_ops
    )
    torch._inductor.config.custom_should_partition_ops = splitting_ops

    logger.debug(
        "Registered inductor partition rules for %d operators", len(splitting_ops)
    )

    try:
        yield
    finally:
        # Clear and restore previous state
        torch._inductor.config.custom_should_partition_ops = saved_splitting_ops
        logger.debug("Restored previous partition rules state.")
```