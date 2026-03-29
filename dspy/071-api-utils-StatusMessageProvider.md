---
title: StatusMessageProvider - DSPy
url: https://dspy.ai/api/utils/StatusMessageProvider/
source: sitemap
fetched_at: 2026-01-23T08:02:53.271672582-03:00
rendered_js: false
word_count: 228
summary: This document defines the StatusMessageProvider base class used for creating and customizing status message streaming during various stages of DSPy program execution.
tags:
    - dspy
    - streaming
    - status-messages
    - api-reference
    - observability
    - customization
category: api
---

Provides customizable status message streaming for DSPy programs.

This class serves as a base for creating custom status message providers. Users can subclass and override its methods to define specific status messages for different stages of program execution, each method must return a string.

Example:

```
classMyStatusMessageProvider(StatusMessageProvider):
    deflm_start_status_message(self, instance, inputs):
        return f"Calling LM with inputs {inputs}..."

    defmodule_end_status_message(self, outputs):
        return f"Module finished with output: {outputs}!"

program = dspy.streamify(dspy.Predict("q->a"), status_message_provider=MyStatusMessageProvider())
```

### Functions[¶](#dspy.streaming.StatusMessageProvider-functions "Permanent link")

#### `lm_end_status_message(outputs: Any)` [¶](#dspy.streaming.StatusMessageProvider.lm_end_status_message "Permanent link")

Status message after a `dspy.LM` is called.

Source code in `dspy/streaming/messages.py`

```
deflm_end_status_message(self, outputs: Any):
"""Status message after a `dspy.LM` is called."""
    pass
```

#### `lm_start_status_message(instance: Any, inputs: dict[str, Any])` [¶](#dspy.streaming.StatusMessageProvider.lm_start_status_message "Permanent link")

Status message before a `dspy.LM` is called.

Source code in `dspy/streaming/messages.py`

```
deflm_start_status_message(self, instance: Any, inputs: dict[str, Any]):
"""Status message before a `dspy.LM` is called."""
    pass
```

#### `module_end_status_message(outputs: Any)` [¶](#dspy.streaming.StatusMessageProvider.module_end_status_message "Permanent link")

Status message after a `dspy.Module` or `dspy.Predict` is called.

Source code in `dspy/streaming/messages.py`

```
defmodule_end_status_message(self, outputs: Any):
"""Status message after a `dspy.Module` or `dspy.Predict` is called."""
    pass
```

#### `module_start_status_message(instance: Any, inputs: dict[str, Any])` [¶](#dspy.streaming.StatusMessageProvider.module_start_status_message "Permanent link")

Status message before a `dspy.Module` or `dspy.Predict` is called.

Source code in `dspy/streaming/messages.py`

```
defmodule_start_status_message(self, instance: Any, inputs: dict[str, Any]):
"""Status message before a `dspy.Module` or `dspy.Predict` is called."""
    pass
```

#### `tool_end_status_message(outputs: Any)` [¶](#dspy.streaming.StatusMessageProvider.tool_end_status_message "Permanent link")

Status message after a `dspy.Tool` is called.

Source code in `dspy/streaming/messages.py`

```
deftool_end_status_message(self, outputs: Any):
"""Status message after a `dspy.Tool` is called."""
    return "Tool calling finished! Querying the LLM with tool calling results..."
```

#### `tool_start_status_message(instance: Any, inputs: dict[str, Any])` [¶](#dspy.streaming.StatusMessageProvider.tool_start_status_message "Permanent link")

Status message before a `dspy.Tool` is called.

Source code in `dspy/streaming/messages.py`

```
deftool_start_status_message(self, instance: Any, inputs: dict[str, Any]):
"""Status message before a `dspy.Tool` is called."""
    return f"Calling tool {instance.name}..."
```