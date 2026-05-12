---
title: kv_connector - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/kv_connector/
source: sitemap
fetched_at: 2026-05-07T21:42:26.438074579-03:00
rendered_js: false
word_count: 9
summary: This document defines the KVConnector interface, which provides hook methods for managing key-value cache operations within a GPU model runner.
tags:
    - kv-connector
    - gpu-model-runner
    - vllm
    - interface-definition
    - cache-management
category: reference
---

KVConnector interface used by GPUModelRunner.

Source code in `vllm/v1/worker/gpu/kv_connector.py`

```
classKVConnector:
"""KVConnector interface used by GPUModelRunner."""

    defpre_forward(self, scheduler_output: "SchedulerOutput") -> None:
        pass

    defpost_forward(
        self, scheduler_output: "SchedulerOutput", wait_for_save: bool = True
    ) -> KVConnectorOutput | None:
        return None

    defno_forward(self, scheduler_output: "SchedulerOutput") -> ModelRunnerOutput:
        return EMPTY_MODEL_RUNNER_OUTPUT

    defset_disabled(self, disabled: bool) -> None:
        pass
```