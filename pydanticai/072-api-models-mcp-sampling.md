---
title: pydantic_ai.models.mcp_sampling - Pydantic AI
url: https://ai.pydantic.dev/api/models/mcp-sampling/
source: sitemap
fetched_at: 2026-01-22T22:24:34.520248987-03:00
rendered_js: false
word_count: 191
summary: This document defines the MCPSamplingModel and MCPSamplingModelSettings classes, which enable MCP servers to request model interactions by calling back to the connected MCP client. It details the session management, preference configurations, and fallback parameters required for Model Context Protocol sampling.
tags:
    - mcp-sampling
    - model-context-protocol
    - pydantic-ai
    - python-sdk
    - model-integration
category: api
---

### MCPSamplingModelSettings

Bases: `ModelSettings`

Settings used for an MCP Sampling model request.

Source code in `pydantic_ai_slim/pydantic_ai/models/mcp_sampling.py`

```
classMCPSamplingModelSettings(ModelSettings, total=False):
"""Settings used for an MCP Sampling model request."""

    # ALL FIELDS MUST BE `mcp_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    mcp_model_preferences: ModelPreferences
"""Model preferences to use for MCP Sampling."""
```

#### mcp\_model\_preferences `instance-attribute`

```
mcp_model_preferences: ModelPreferences
```

Model preferences to use for MCP Sampling.

### MCPSamplingModel `dataclass`

Bases: `Model`

A model that uses MCP Sampling.

[MCP Sampling](https://modelcontextprotocol.io/docs/concepts/sampling) allows an MCP server to make requests to a model by calling back to the MCP client that connected to it.

Source code in `pydantic_ai_slim/pydantic_ai/models/mcp_sampling.py`

```
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
```

```
@dataclass
classMCPSamplingModel(Model):
"""A model that uses MCP Sampling.

    [MCP Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
    allows an MCP server to make requests to a model by calling back to the MCP client that connected to it.
    """

    session: ServerSession
"""The MCP server session to use for sampling."""

    _: KW_ONLY

    default_max_tokens: int = 16_384
"""Default max tokens to use if not set in [`ModelSettings`][pydantic_ai.settings.ModelSettings.max_tokens].

    Max tokens is a required parameter for MCP Sampling, but optional on
    [`ModelSettings`][pydantic_ai.settings.ModelSettings], so this value is used as fallback.
    """

    async defrequest(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        system_prompt, sampling_messages = _mcp.map_from_pai_messages(messages)

        model_settings, _ = self.prepare_request(model_settings, model_request_parameters)
        model_settings = cast(MCPSamplingModelSettings, model_settings or {})

        result = await self.session.create_message(
            sampling_messages,
            max_tokens=model_settings.get('max_tokens', self.default_max_tokens),
            system_prompt=system_prompt,
            temperature=model_settings.get('temperature'),
            model_preferences=model_settings.get('mcp_model_preferences'),
            stop_sequences=model_settings.get('stop_sequences'),
        )
        if result.role == 'assistant':
            return ModelResponse(
                parts=[_mcp.map_from_sampling_content(result.content)],
                model_name=result.model,
            )
        else:
            raise exceptions.UnexpectedModelBehavior(
                f'Unexpected result from MCP sampling, expected "assistant" role, got {result.role}.'
            )

    @asynccontextmanager
    async defrequest_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        raise NotImplementedError('MCP Sampling does not support streaming')
        yield

    @property
    defmodel_name(self) -> str:
"""The model name.

        Since the model name isn't known until the request is made, this property always returns `'mcp-sampling'`.
        """
        return 'mcp-sampling'

    @property
    defsystem(self) -> str:
"""The system / model provider, returns `'MCP'`."""
        return 'MCP'
```

#### session `instance-attribute`

The MCP server session to use for sampling.

#### default\_max\_tokens `class-attribute` `instance-attribute`

```
default_max_tokens: int = 16384
```

Default max tokens to use if not set in [`ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings.max_tokens "max_tokens            instance-attribute   ").

Max tokens is a required parameter for MCP Sampling, but optional on [`ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings"), so this value is used as fallback.

#### model\_name `property`

The model name.

Since the model name isn't known until the request is made, this property always returns `'mcp-sampling'`.

#### system `property`

The system / model provider, returns `'MCP'`.