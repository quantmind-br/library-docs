---
title: Batch Processing | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing
source: crawler
fetched_at: 2026-04-24T17:00:06.99089764-03:00
rendered_js: false
word_count: 238
summary: This document describes the functionality of a batch processing runner used to generate structured training data from numerous prompts for an agent, detailing the input format (JSONL), output structure, and advanced features like toolset distributions and containerization support.
tags:
    - batch-processing
    - training-data
    - trajectory-generation
    - jsonl-input
    - toolsets
    - sharegpt
category: guide
---

Batch processing lets you run the Hermes agent across hundreds or thousands of prompts in parallel, generating structured trajectory data. This is primarily used for **training data generation** — producing ShareGPT-format trajectories with tool usage statistics that can be used for fine-tuning or evaluation.

The batch runner (`batch_runner.py`) processes a JSONL dataset of prompts, running each through a full agent session with tool access. Each prompt gets its own isolated environment. The output is structured trajectory data with full conversation history, tool call statistics, and reasoning coverage metrics.

The input dataset is a JSONL file (one JSON object per line). Each entry must have a `prompt` field:

Each prompt gets a randomly sampled set of toolsets from a **distribution**. This ensures training data covers diverse tool combinations. Use `--list_distributions` to see all available distributions.

In the current implementation, distributions assign a probability to **each individual toolset**. The sampler flips each toolset independently, then guarantees that at least one toolset is enabled. This is different from a hand-authored table of prebuilt combinations.

```text
data/my_run/
├── trajectories.jsonl    # Combined final output (all batches merged)
├── batch_0.jsonl         # Individual batch results
├── batch_1.jsonl
├── ...
├── checkpoint.json       # Resume checkpoint
└── statistics.json       # Aggregate tool usage stats
```

```json
{
"prompt_index":42,
"conversations":[
{"from":"human","value":"Write a function..."},
{"from":"gpt","value":"I'll create that function...",
"tool_calls":[...]},
{"from":"tool","value":"..."},
{"from":"gpt","value":"Here's the completed function..."}
],
"metadata":{
"batch_num":2,
"timestamp":"2026-01-15T10:30:00",
"model":"anthropic/claude-sonnet-4.6"
},
"completed":true,
"partial":false,
"api_calls":3,
"toolsets_used":["terminal","file"],
"tool_stats":{
"terminal":{"count":2,"success":2,"failure":0},
"read_file":{"count":1,"success":1,"failure":0}
},
"tool_error_counts":{
"terminal":0,
"read_file":0
}
}
```

The `conversations` field uses a ShareGPT-like format with `from` and `value` fields. Tool stats are normalized to include all possible tools with zero defaults, ensuring consistent schema across entries for HuggingFace datasets compatibility.

Statistics are also saved to `statistics.json` for programmatic analysis.

For benchmarks requiring specific environments, each prompt can specify its own container image:

The batch runner verifies Docker images are accessible before running each prompt.