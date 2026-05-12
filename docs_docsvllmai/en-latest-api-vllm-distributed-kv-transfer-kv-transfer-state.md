---
title: kv_transfer_state - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_transfer_state/
source: sitemap
fetched_at: 2026-05-07T21:18:59.085489842-03:00
rendered_js: false
word_count: 64
summary: This function verifies whether a provided or global KV connector instance belongs to the v1 implementation.
tags:
    - kv-connector
    - distributed-computing
    - vllm
    - internal-api
    - state-management
category: api
---

Check if the KV connector is the v1 connector. If the argument is None, it will check the global KV connector

Parameters:

Name Type Description Default `connector` `KVConnectorBaseType | None`

The KV connector to check. If None, it will check the global KV connector.

`None`

Note

This function will no-longer be needed after the v1 KV connector becomes the default.

Source code in `vllm/distributed/kv_transfer/kv_transfer_state.py`

```
defis_v1_kv_transfer_group(connector: KVConnectorBaseType | None = None) -> bool:
"""Check if the KV connector is the v1 connector.
    If the argument is None, it will check the global KV connector

    Args:
        connector: The KV connector to check. If None, it will check the
            global KV connector.

    Note:
        This function will no-longer be needed after the v1 KV connector
        becomes the default.
    """
    if connector is None:
        connector = _KV_CONNECTOR_AGENT

    if connector is None:
        return False

    return isinstance(connector, KVConnectorBase_V1)
```