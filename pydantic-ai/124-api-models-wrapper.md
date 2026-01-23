---
title: pydantic_ai.models.wrapper - Pydantic AI
url: https://ai.pydantic.dev/api/models/wrapper/
source: sitemap
fetched_at: 2026-01-22T22:24:43.387390946-03:00
rendered_js: false
word_count: 0
summary: This document defines the WrapperModel base class, which provides a structural foundation for wrapping and delegating operations to an underlying model instance.
tags:
    - python
    - model-wrapper
    - delegation-pattern
    - api-design
    - asynchronous-methods
category: api
---

```
17
18
19
20
21
22
23
24
25
26
27
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
```

```
@dataclass(init=False)
classWrapperModel(Model):
"""Model which wraps another model.

    Does nothing on its own, used as a base class.
    """

    wrapped: Model
"""The underlying model being wrapped."""

    def__init__(self, wrapped: Model | KnownModelName):
        super().__init__()
        self.wrapped = infer_model(wrapped)

    async defrequest(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        return await self.wrapped.request(messages, model_settings, model_request_parameters)

    async defcount_tokens(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> RequestUsage:
        return await self.wrapped.count_tokens(messages, model_settings, model_request_parameters)

    @asynccontextmanager
    async defrequest_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        async with self.wrapped.request_stream(
            messages, model_settings, model_request_parameters, run_context
        ) as response_stream:
            yield response_stream

    defcustomize_request_parameters(self, model_request_parameters: ModelRequestParameters) -> ModelRequestParameters:
        return self.wrapped.customize_request_parameters(model_request_parameters)  # pragma: no cover

    defprepare_request(
        self,
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[ModelSettings | None, ModelRequestParameters]:
        return self.wrapped.prepare_request(model_settings, model_request_parameters)

    @property
    defmodel_name(self) -> str:
        return self.wrapped.model_name

    @property
    defsystem(self) -> str:
        return self.wrapped.system

    @cached_property
    defprofile(self) -> ModelProfile:
        return self.wrapped.profile

    @property
    defsettings(self) -> ModelSettings | None:
"""Get the settings from the wrapped model."""
        return self.wrapped.settings

    def__getattr__(self, item: str):
        return getattr(self.wrapped, item)
```