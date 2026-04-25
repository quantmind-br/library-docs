---
title: Adding Tools | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools
source: crawler
fetched_at: 2026-04-24T17:00:21.210108864-03:00
rendered_js: false
word_count: 151
summary: This document explains the definitions and registration process for various 'Skills' and 'Tools,' detailing how functions are discovered, integrated into a system, and configured to handle synchronous or asynchronous operations.
tags:
    - tool-definition
    - skill-implementation
    - registry-pattern
    - api-integration
    - auto-discovery
    - configuration
category: guide
---

Make it a **Skill** when the capability can be expressed as instructions + shell commands + existing tools (arXiv search, git workflows, Docker management, PDF processing).

Make it a **Tool** when it requires end-to-end integration with API keys, custom processing logic, binary data handling, or streaming (browser automation, TTS, vision analysis).

Any `tools/*.py` file with a top-level `registry.register()` call is auto-discovered at startup — no manual import list required.

```python
# tools/weather_tool.py
"""Weather Tool -- look up current weather for a location."""

import json
import os
import logging

logger = logging.getLogger(__name__)


# --- Availability check ---

defcheck_weather_requirements()->bool:
"""Return True if the tool's dependencies are available."""
returnbool(os.getenv("WEATHER_API_KEY"))


# --- Handler ---

defweather_tool(location:str, units:str="metric")->str:
"""Fetch weather for a location. Returns JSON string."""
    api_key = os.getenv("WEATHER_API_KEY")
ifnot api_key:
return json.dumps({"error":"WEATHER_API_KEY not configured"})
try:
# ... call weather API ...
return json.dumps({"location": location,"temp":22,"units": units})
except Exception as e:
return json.dumps({"error":str(e)})


# --- Schema ---

WEATHER_SCHEMA ={
"name":"weather",
"description":"Get current weather for a location.",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"City name or coordinates (e.g. 'London' or '51.5,-0.1')"
},
"units":{
"type":"string",
"enum":["metric","imperial"],
"description":"Temperature units (default: metric)",
"default":"metric"
}
},
"required":["location"]
}
}


# --- Registration ---

from tools.registry import registry

registry.register(
    name="weather",
    toolset="weather",
    schema=WEATHER_SCHEMA,
    handler=lambda args,**kw: weather_tool(
        location=args.get("location",""),
        units=args.get("units","metric")),
    check_fn=check_weather_requirements,
    requires_env=["WEATHER_API_KEY"],
)
```

```python
# If it should be available on all platforms (CLI + messaging):
_HERMES_CORE_TOOLS =[
...
"weather",# <-- add here
]

# Or create a new standalone toolset:
"weather":{
"description":"Weather lookup tools",
"tools":["weather"],
"includes":[]
},
```

Tool modules with a top-level `registry.register()` call are auto-discovered by `discover_builtin_tools()` in `tools/registry.py`. No manual import list to maintain — just create your file in `tools/` and it's picked up at startup.

```python
asyncdefweather_tool_async(location:str)->str:
asyncwith aiohttp.ClientSession()as session:
...
return json.dumps(result)

registry.register(
    name="weather",
    toolset="weather",
    schema=WEATHER_SCHEMA,
    handler=lambda args,**kw: weather_tool_async(args.get("location","")),
    check_fn=check_weather_requirements,
    is_async=True,# registry calls _run_async() automatically
)
```

The registry handles async bridging transparently — you never call `asyncio.run()` yourself.

```python
def_handle_weather(args,**kw):
    task_id = kw.get("task_id")
return weather_tool(args.get("location",""), task_id=task_id)

registry.register(
    name="weather",
...
    handler=_handle_weather,
)
```

Some tools (`todo`, `memory`, `session_search`, `delegate_task`) need access to per-session agent state. These are intercepted by `run_agent.py` before reaching the registry. The registry still holds their schemas, but `dispatch()` returns a fallback error if the intercept is bypassed.

```python
OPTIONAL_ENV_VARS ={
...
"WEATHER_API_KEY":{
"description":"Weather API key for weather lookup",
"prompt":"Weather API key",
"url":"https://weatherapi.com/",
"tools":["weather"],
"password":True,
},
}
```