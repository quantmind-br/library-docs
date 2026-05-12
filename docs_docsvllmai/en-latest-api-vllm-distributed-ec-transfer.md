---
title: ec_transfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/
source: sitemap
fetched_at: 2026-05-07T21:17:44.197379486-03:00
rendered_js: false
word_count: 8
summary: This function initializes the EC cache connector agent for vLLM distributed transfer instances if the configuration is present.
tags:
    - vllm
    - ec-transfer
    - distributed-computing
    - cache-connector
    - initialization
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