---
title: Hermes Atropos Environments — Build, test, and debug Hermes Agent RL environments for Atropos training | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-hermes-atropos-environments
source: crawler
fetched_at: 2026-04-24T17:01:24.195648209-03:00
rendered_js: false
word_count: 917
summary: This document serves as a comprehensive guide detailing how to build, test, and debug Reinforcement Learning (RL) environments for the Atropos training framework within the hermes-agent repository. It outlines the required methods, architecture, and setup procedures necessary for creating agentic RL experiences.
tags:
    - hermes-agent
    - rl-environments
    - atropos
    - reinforcement-learning
    - guide
    - llm-training
category: guide
---

Build, test, and debug Hermes Agent RL environments for Atropos training. Covers the HermesAgentBaseEnv interface, reward functions, agent loop integration, evaluation with tools, wandb logging, and the three CLI modes (serve/process/evaluate). Use when creating, reviewing, or fixing RL environments in the hermes-agent repo.

SourceOptional — install with `hermes skills install official/mlops/hermes-atropos-environments`Path`optional-skills/mlops/hermes-atropos-environments`Version`1.1.0`AuthorHermes AgentLicenseMITTags`atropos`, `rl`, `environments`, `training`, `reinforcement-learning`, `reward-functions`Related skills[`axolotl`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/mlops/mlops-training-axolotl), [`fine-tuning-with-trl`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/mlops/mlops-training-trl-fine-tuning), `lm-evaluation-harness`

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Hermes Agent Atropos Environments

Guide for building RL environments in the hermes-agent repo that integrate with the Atropos training framework.

## Architecture Overview[​](#architecture-overview "Direct link to Architecture Overview")

```text
Atropos BaseEnv (atroposlib/envs/base.py)
    └── HermesAgentBaseEnv (environments/hermes_base_env.py)
            ├── Handles agent loop orchestration
            ├── Handles tool resolution per group
            ├── Handles ToolContext for reward verification
            └── YOUR ENVIRONMENT (environments/your_env.py)
                    Only implements: setup, get_next_item, format_prompt,
                                    compute_reward, evaluate, wandb_log
```

Hermes environments are special because they run a **multi-turn agent loop with tool calling** — not just single-turn completions. The base env handles the loop; you implement the task and scoring.

## File Locations[​](#file-locations "Direct link to File Locations")

FilePurpose`environments/hermes_base_env.py`Base class with agent loop + tool resolution`environments/agent_loop.py``HermesAgentLoop` + `AgentResult` dataclass`environments/tool_context.py``ToolContext` for reward verification`environments/tool_call_parsers.py`Phase 2 tool call parsers (hermes, mistral, etc.)`environments/your_env.py`Your environment implementation

## Inference Setup — Ask the User First[​](#inference-setup--ask-the-user-first "Direct link to Inference Setup — Ask the User First")

**IMPORTANT:** Before running any test, evaluation, or data generation command, always ask the user how they want to handle inference. Do NOT assume OpenRouter or any specific endpoint. Present these options:

1. **OpenRouter** — Ask which model they want to use (e.g., `anthropic/claude-sonnet-4.5`, `google/gemini-2.5-pro`, `meta-llama/llama-3.3-70b-instruct`, etc.). Requires `OPENROUTER_API_KEY` in environment.
2. **Self-hosted VLLM endpoint** — Ask for their base URL (e.g., `http://localhost:8000/v1`) and model name. Set `--openai.server_type vllm`.
3. **Other OpenAI-compatible API** — Ask for the base URL, model name, and any required API key. Set `--openai.server_type openai` and `--openai.health_check false`.
4. **Local Atropos training server** — For `serve` mode with a live training loop. Default `http://localhost:8000/v1`.

Once the user tells you their setup, use those values in all CLI commands for that session. Example prompts:

> "Before I run this, how would you like to handle inference?
> 
> 1. OpenRouter (I'll need your preferred model, e.g. claude-sonnet-4.5)
> 2. A self-hosted VLLM endpoint (give me the URL and model name)
> 3. Another OpenAI-compatible API (give me the URL, model, and any auth details)
> 4. Local Atropos training server (serve mode)"

### Key flags by provider:[​](#key-flags-by-provider "Direct link to Key flags by provider:")

Provider`--openai.server_type``--openai.health_check``--openai.api_key`OpenRouter`openai``false``$OPENROUTER_API_KEY`VLLM (self-hosted)`vllm`(default)(not needed)Other OpenAI-compatible`openai``false`As neededLocal Atropos(default)(default)(not needed)

## Required Methods[​](#required-methods "Direct link to Required Methods")

### 1. `setup()` — Load dataset and initialize state[​](#1-setup--load-dataset-and-initialize-state "Direct link to 1-setup--load-dataset-and-initialize-state")

```python
asyncdefsetup(self)->None:
"""Called once at startup. Load datasets, initialize state."""
# Try HuggingFace first, fallback to built-in samples
try:
from datasets import load_dataset
        ds = load_dataset("your/dataset", split="test")
        self._items =[...]
except Exception:
        self._items = BUILTIN_SAMPLES

# Always split into train/eval
    random.shuffle(self._items)
    eval_size =max(20,int(len(self._items)*0.1))
    self._eval_items = self._items[:eval_size]
    self._items = self._items[eval_size:]
```

### 2. `get_next_item()` — Return next training item[​](#2-get_next_item--return-next-training-item "Direct link to 2-get_next_item--return-next-training-item")

```python
asyncdefget_next_item(self)->dict:
"""Return next item, cycling through dataset."""
    item = self._items[self._index %len(self._items)]
    self._index +=1
return item
```

### 3. `format_prompt(item)` — Convert item to user message[​](#3-format_promptitem--convert-item-to-user-message "Direct link to 3-format_promptitem--convert-item-to-user-message")

```python
defformat_prompt(self, item:dict)->str:
"""Convert a dataset item into the user-facing prompt."""
returnf"Research this question: {item['question']}"
```

### 4. `compute_reward(item, result, ctx)` — Score the rollout[​](#4-compute_rewarditem-result-ctx--score-the-rollout "Direct link to 4-compute_rewarditem-result-ctx--score-the-rollout")

**CRITICAL**: `result` is an `AgentResult`, NOT a dict. It has these attributes:

- `result.messages` — List of message dicts (OpenAI format)
- `result.turns_used` — Number of LLM calls made
- `result.finished_naturally` — True if model stopped voluntarily
- `result.tool_errors` — List of ToolError objects

**AgentResult does NOT have**: `final_response`, `tool_calls`, `tools_used`. You must extract these from `result.messages`:

```python
asyncdefcompute_reward(self, item, result: AgentResult, ctx: ToolContext)->float:
# Extract final response (last assistant message with content)
    final_response =""
    tools_used =[]
for msg inreversed(result.messages):
if msg.get("role")=="assistant"and msg.get("content")andnot final_response:
            final_response = msg["content"]
if msg.get("role")=="assistant"and msg.get("tool_calls"):
for tc in msg["tool_calls"]:
                fn = tc.get("function",{})ifisinstance(tc,dict)else{}
                name = fn.get("name","")
if name:
                    tools_used.append(name)

# Score using LLM judge, heuristic, or ToolContext verification
    correctness =await self._llm_judge(item, final_response)
return correctness
```

`ctx` (ToolContext) gives you terminal/file access to the agent's sandbox for verification:

```python
# Run tests in the agent's sandbox
result = ctx.terminal("pytest /workspace/test.py")
return1.0if result["exit_code"]==0else0.0
```

### 5. `evaluate()` — Periodic evaluation with full agent loop[​](#5-evaluate--periodic-evaluation-with-full-agent-loop "Direct link to 5-evaluate--periodic-evaluation-with-full-agent-loop")

**MUST use the full agent loop with tools**, not single-turn chat\_completion. The whole point of hermes-agent environments is agentic evaluation:

```python
asyncdefevaluate(self,*args,**kwargs)->None:
import time, uuid
from environments.agent_loop import HermesAgentLoop
from environments.tool_context import ToolContext

    start_time = time.time()
    tools, valid_names = self._resolve_tools_for_group()
    samples =[]

for item in self._eval_items[:self.config.eval_size]:
        task_id =str(uuid.uuid4())
        messages =[]
if self.config.system_prompt:
            messages.append({"role":"system","content": self.config.system_prompt})
        messages.append({"role":"user","content": self.format_prompt(item)})

        agent = HermesAgentLoop(
            server=self.server,
            tool_schemas=tools,
            valid_tool_names=valid_names,
            max_turns=self.config.max_agent_turns,
            task_id=task_id,
            temperature=0.0,# Deterministic for eval
            max_tokens=self.config.max_token_length,
            extra_body=self.config.extra_body,
)
        result =await agent.run(messages)

        ctx = ToolContext(task_id)
try:
            reward =await self.compute_reward(item, result, ctx)
finally:
            ctx.cleanup()

        samples.append({"prompt":...,"response":...,"reward": reward})

    eval_metrics ={"eval/mean_reward":...}
await self.evaluate_log(metrics=eval_metrics, samples=samples,
                            start_time=start_time, end_time=time.time())
```

### 6. `wandb_log()` — Custom metrics logging[​](#6-wandb_log--custom-metrics-logging "Direct link to 6-wandb_log--custom-metrics-logging")

Always call `super().wandb_log()` at the end:

```python
asyncdefwandb_log(self, wandb_metrics=None):
if wandb_metrics isNone:
        wandb_metrics ={}
if self._reward_buffer:
        n =len(self._reward_buffer)
        wandb_metrics["train/mean_reward"]=sum(self._reward_buffer)/ n
        self._reward_buffer.clear()
awaitsuper().wandb_log(wandb_metrics)# MUST call super
```

**Pitfall**: `compute_reward` appends to metric buffers. During eval, this pollutes training metrics. Roll back buffer entries added during eval.

## Config Class[​](#config-class "Direct link to Config Class")

Always create a custom config subclass with Pydantic Field descriptors. Key inherited fields you can tune: `enabled_toolsets`, `max_agent_turns`, `agent_temperature`, `system_prompt`, `terminal_backend`, `group_size`, `steps_per_eval`, `total_steps`.

## config\_init() — Default Configuration[​](#config_init--default-configuration "Direct link to config_init() — Default Configuration")

Classmethod returning `(YourEnvConfig, [APIServerConfig(...)])`. Set server\_type to "openai" for OpenRouter/external APIs. Load API key from environment variable.

## Three CLI Modes[​](#three-cli-modes "Direct link to Three CLI Modes")

```bash
# SERVE — Full training loop (connects to Atropos API server)
python environments/my_env.py serve --openai.base_url http://localhost:8000/v1

# PROCESS — Offline data generation (saves JSONL)
python environments/my_env.py process --env.total_steps10--env.group_size1\
--env.use_wandbfalse--env.data_path_to_save_groups output.jsonl \
--openai.base_url"<USER_BASE_URL>"\
--openai.model_name"<USER_MODEL>"\
--openai.server_type<USER_SERVER_TYPE>--openai.health_checkfalse

# EVALUATE — Standalone eval (runs setup + evaluate only)
python environments/my_env.py evaluate --env.eval_size20\
--env.data_dir_to_save_evals /tmp/eval_results \
--openai.base_url"<USER_BASE_URL>"\
--openai.model_name"<USER_MODEL>"\
--openai.server_type<USER_SERVER_TYPE>--openai.health_checkfalse
```

Config priority: CLI args &gt; YAML file &gt; config\_init() defaults.

## Common Pitfalls[​](#common-pitfalls "Direct link to Common Pitfalls")

01. **AgentResult has .messages, not .final\_response** — Extract the final response by iterating reversed(result.messages) looking for the last assistant message with content.
02. **evaluate() must use HermesAgentLoop, not chat\_completion** — Single-turn chat\_completion has no tools. The whole point of hermes-agent benchmarks is agentic evaluation with tool use.
03. **Don't call \_llm\_judge twice** — If compute\_reward already calls it, extract the score from the buffer instead of calling judge separately in evaluate().
04. **Eval pollutes training buffers** — compute\_reward appends to metric buffers. During eval, roll back buffer entries to keep training metrics clean.
05. **Always set health\_check=false for OpenRouter** — OpenRouter has no /health endpoint.
06. **Set data\_dir\_to\_save\_evals in evaluate mode** — Without it, results aren't saved.
07. **default\_toolsets class variable vs enabled\_toolsets config** — The class variable is a hint; the config field is what actually controls tool resolution.
08. **Tool call parsing in messages** — Tool calls are dicts with `{"function": {"name": ..., "arguments": ...}}`. Always check `isinstance(tc, dict)`.
09. **ToolContext.cleanup()** — Always call in a finally block to release sandbox resources.
10. **server\_type must be "openai" for external APIs** — Without it, Atropos assumes a local VLLM server.
11. **Always ask the user for their inference setup** — Never hardcode or assume a specific provider/model. See the "Inference Setup" section above.

## Reward Function Patterns[​](#reward-function-patterns "Direct link to Reward Function Patterns")

### LLM Judge (for open-ended tasks)[​](#llm-judge-for-open-ended-tasks "Direct link to LLM Judge (for open-ended tasks)")

Use `self.server.chat_completion()` with a scoring prompt. Parse JSON response for score float. Always include a heuristic fallback (keyword overlap) for when the judge call fails.

### Binary Verification (for code/terminal tasks)[​](#binary-verification-for-codeterminal-tasks "Direct link to Binary Verification (for code/terminal tasks)")

Use `ctx.terminal("pytest test.py -q")` to run tests in the agent's sandbox. Return 1.0 for pass, 0.0 for fail.

### Multi-Signal (combine multiple indicators)[​](#multi-signal-combine-multiple-indicators "Direct link to Multi-Signal (combine multiple indicators)")

Weight correctness (0.6) + tool usage (0.2) + efficiency (0.2) + optional bonuses. Clamp to \[0, 1].

## Testing Your Environment[​](#testing-your-environment "Direct link to Testing Your Environment")

1. **Import test**: `python -c "from environments.my_env import MyEnv; print('OK')"`
2. **Ask the user for inference setup** (see "Inference Setup" section above)
3. **Process mode** (1 item): Verify JSONL output has valid tokens, masks, scores
4. **Evaluate mode**: Verify full agent loop runs with tools, metrics logged correctly
5. **Check reward range**: Scores should be in \[0, 1], not all identical

## Minimum Implementation Checklist[​](#minimum-implementation-checklist "Direct link to Minimum Implementation Checklist")

```python
classMyEnv(HermesAgentBaseEnv):
    name ="my-env"
    env_config_cls = MyEnvConfig

@classmethod
defconfig_init(cls):...# Default server + env config
asyncdefsetup(self):...# Load dataset + train/eval split
asyncdefget_next_item(self):...# Cycle through training items
defformat_prompt(self, item):...# Item → user message string
asyncdefcompute_reward(self, item, result, ctx):...# Score rollout
asyncdefevaluate(self,*args,**kwargs):...# Full agent loop eval
asyncdefwandb_log(self, metrics=None):...# Custom metrics + super()

if __name__ =="__main__":
    MyEnv.cli()
```