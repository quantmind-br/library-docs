---
title: ec_transfer_state - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_transfer_state/
source: sitemap
fetched_at: 2026-05-07T21:17:48.910092298-03:00
rendered_js: false
word_count: 8
summary: This document describes the initialization process for the EC cache connector within the vLLM distributed transfer framework.
tags:
    - vllm
    - ec-transfer
    - cache-connector
    - distributed-computing
    - initialization-logic
category: api
---

Initialize EC cache connector.

Source code in `vllm/distributed/ec_transfer/ec_transfer_state.py`

```
defensure_ec_transfer_initialized(vllm_config: "VllmConfig") -> None:
"""
    Initialize EC cache connector.
    """

    global _EC_CONNECTOR_AGENT

    if vllm_config.ec_transfer_config is None:
        return

    if (
        vllm_config.ec_transfer_config.is_ec_transfer_instance
        and _EC_CONNECTOR_AGENT is None
    ):
        _EC_CONNECTOR_AGENT = ECConnectorFactory.create_connector(
            config=vllm_config, role=ECConnectorRole.WORKER
        )
```