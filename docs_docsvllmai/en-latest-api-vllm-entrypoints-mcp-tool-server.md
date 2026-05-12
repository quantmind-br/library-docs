---
title: tool_server - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/mcp/tool_server/
source: sitemap
fetched_at: 2026-05-07T21:19:46.026105341-03:00
rendered_js: false
word_count: 61
summary: Defines the abstract base class ToolServer for managing tool discovery, descriptions, and session creation within a Model Context Protocol environment.
tags:
    - python-api
    - tool-server
    - mcp
    - abstract-base-class
    - interface-definition
category: reference
---

## ToolServer [¶](#vllm.entrypoints.mcp.tool_server.ToolServer "Permanent link")

Bases: `ABC`

Source code in `vllm/entrypoints/mcp/tool_server.py`

```
classToolServer(ABC):
    @abstractmethod
    defhas_tool(self, tool_name: str) -> bool:
"""
        Return True if the tool is supported, False otherwise.
        """
        pass

    @abstractmethod
    defget_tool_description(
        self, tool_name: str, allowed_tools: list[str] | None = None
    ) -> ToolNamespaceConfig | None:
"""
        Return the tool description for the given tool name.
        If the tool is not supported, return None.
        """
        pass

    @abstractmethod
    defnew_session(
        self, tool_name: str, session_id: str, headers: dict[str, str] | None = None
    ) -> AbstractAsyncContextManager[Any]:
"""
        Create a session for the tool.
        """
        ...
```

### get\_tool\_description `abstractmethod` [¶](#vllm.entrypoints.mcp.tool_server.ToolServer.get_tool_description "Permanent link")

```
get_tool_description(
    tool_name: str, allowed_tools: list[str] | None = None
) -> ToolNamespaceConfig | None
```

Return the tool description for the given tool name. If the tool is not supported, return None.

Source code in `vllm/entrypoints/mcp/tool_server.py`

```
@abstractmethod
defget_tool_description(
    self, tool_name: str, allowed_tools: list[str] | None = None
) -> ToolNamespaceConfig | None:
"""
    Return the tool description for the given tool name.
    If the tool is not supported, return None.
    """
    pass
```

### has\_tool `abstractmethod` [¶](#vllm.entrypoints.mcp.tool_server.ToolServer.has_tool "Permanent link")

Return True if the tool is supported, False otherwise.

Source code in `vllm/entrypoints/mcp/tool_server.py`

```
@abstractmethod
defhas_tool(self, tool_name: str) -> bool:
"""
    Return True if the tool is supported, False otherwise.
    """
    pass
```

### new\_session `abstractmethod` [¶](#vllm.entrypoints.mcp.tool_server.ToolServer.new_session "Permanent link")

Create a session for the tool.

Source code in `vllm/entrypoints/mcp/tool_server.py`

```
@abstractmethod
defnew_session(
    self, tool_name: str, session_id: str, headers: dict[str, str] | None = None
) -> AbstractAsyncContextManager[Any]:
"""
    Create a session for the tool.
    """
    ...
```