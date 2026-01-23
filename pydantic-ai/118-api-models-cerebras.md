---
title: pydantic_ai.models.cerebras - Pydantic AI
url: https://ai.pydantic.dev/api/models/cerebras/
source: sitemap
fetched_at: 2026-01-22T22:24:24.997127587-03:00
rendered_js: false
word_count: 260
summary: This document defines the technical reference for Cerebras model integration, detailing the model classes, settings, and type definitions used for OpenAI-compatible inference.
tags:
    - pydantic-ai
    - cerebras
    - llm-integration
    - openai-compatible
    - inference-api
    - model-settings
category: reference
---

## Setup

For details on how to set up authentication with this model, see [model configuration for Cerebras](https://ai.pydantic.dev/models/cerebras/).

Cerebras model implementation using OpenAI-compatible API.

### CerebrasModelName `module-attribute`

```
CerebrasModelName = str | LatestCerebrasModelNames
```

Possible Cerebras model names.

Since Cerebras supports a variety of models and the list changes frequently, we explicitly list known models but allow any name in the type hints.

See [https://inference-docs.cerebras.ai/models/overview](https://inference-docs.cerebras.ai/models/overview) for an up to date list of models.

### CerebrasModelSettings

Bases: `ModelSettings`

Settings used for a Cerebras model request.

ALL FIELDS MUST BE `cerebras_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

Source code in `pydantic_ai_slim/pydantic_ai/models/cerebras.py`

```
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
```

```
classCerebrasModelSettings(ModelSettings, total=False):
"""Settings used for a Cerebras model request.

    ALL FIELDS MUST BE `cerebras_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.
    """

    cerebras_disable_reasoning: bool
"""Disable reasoning for the model.

    This setting is only supported on reasoning models: `zai-glm-4.6` and `gpt-oss-120b`.

    See [the Cerebras docs](https://inference-docs.cerebras.ai/resources/openai#passing-non-standard-parameters) for more details.
    """
```

#### cerebras\_disable\_reasoning `instance-attribute`

```
cerebras_disable_reasoning: bool
```

Disable reasoning for the model.

This setting is only supported on reasoning models: `zai-glm-4.6` and `gpt-oss-120b`.

See [the Cerebras docs](https://inference-docs.cerebras.ai/resources/openai#passing-non-standard-parameters) for more details.

### CerebrasModel `dataclass`

Bases: `OpenAIChatModel`

A model that uses Cerebras's OpenAI-compatible API.

Cerebras provides ultra-fast inference powered by the Wafer-Scale Engine (WSE).

Apart from `__init__`, all methods are private or match those of the base class.

Source code in `pydantic_ai_slim/pydantic_ai/models/cerebras.py`

```
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
```

```
@dataclass(init=False)
classCerebrasModel(OpenAIChatModel):
"""A model that uses Cerebras's OpenAI-compatible API.

    Cerebras provides ultra-fast inference powered by the Wafer-Scale Engine (WSE).

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    def__init__(
        self,
        model_name: CerebrasModelName,
        *,
        provider: Literal['cerebras'] | Provider[AsyncOpenAI] = 'cerebras',
        profile: ModelProfileSpec | None = None,
        settings: CerebrasModelSettings | None = None,
    ):
"""Initialize a Cerebras model.

        Args:
            model_name: The name of the Cerebras model to use.
            provider: The provider to use. Defaults to 'cerebras'.
            profile: The model profile to use. Defaults to a profile based on the model name.
            settings: Model-specific settings that will be used as defaults for this model.
        """
        super().__init__(model_name, provider=provider, profile=profile, settings=settings)

    @override
    defprepare_request(
        self,
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[ModelSettings | None, ModelRequestParameters]:
        merged_settings, customized_parameters = super().prepare_request(model_settings, model_request_parameters)
        new_settings = _cerebras_settings_to_openai_settings(cast(CerebrasModelSettings, merged_settings or {}))
        return new_settings, customized_parameters
```

#### \_\_init\__

```
__init__(
    model_name: CerebrasModelName,
    *,
    provider: (
        Literal["cerebras"] | Provider[AsyncOpenAI]
    ) = "cerebras",
    profile: ModelProfileSpec | None = None,
    settings: CerebrasModelSettings | None = None
)
```

Initialize a Cerebras model.

Parameters:

Name Type Description Default `model_name` `CerebrasModelName`

The name of the Cerebras model to use.

*required* `provider` `Literal['cerebras'] | Provider[AsyncOpenAI]`

The provider to use. Defaults to 'cerebras'.

`'cerebras'` `profile` `ModelProfileSpec | None`

The model profile to use. Defaults to a profile based on the model name.

`None` `settings` `CerebrasModelSettings | None`

Model-specific settings that will be used as defaults for this model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/models/cerebras.py`

```
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
```

```
def__init__(
    self,
    model_name: CerebrasModelName,
    *,
    provider: Literal['cerebras'] | Provider[AsyncOpenAI] = 'cerebras',
    profile: ModelProfileSpec | None = None,
    settings: CerebrasModelSettings | None = None,
):
"""Initialize a Cerebras model.

    Args:
        model_name: The name of the Cerebras model to use.
        provider: The provider to use. Defaults to 'cerebras'.
        profile: The model profile to use. Defaults to a profile based on the model name.
        settings: Model-specific settings that will be used as defaults for this model.
    """
    super().__init__(model_name, provider=provider, profile=profile, settings=settings)
```