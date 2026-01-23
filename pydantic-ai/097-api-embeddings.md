---
title: pydantic_ai.embeddings - Pydantic AI
url: https://ai.pydantic.dev/api/embeddings/
source: sitemap
fetched_at: 2026-01-22T22:23:58.467889238-03:00
rendered_js: false
word_count: 5511
summary: This document defines the abstract base class for embedding models, providing the standard interface and utility methods required to implement custom embedding providers.
tags:
    - embedding-model
    - abstract-base-class
    - pydantic-ai
    - text-embeddings
    - python-api
category: api
---

### EmbeddingModel

Bases: `ABC`

Abstract base class for embedding models.

Implement this class to create a custom embedding model. For most use cases, use one of the built-in implementations:

- [`OpenAIEmbeddingModel`](#pydantic_ai.embeddings.openai.OpenAIEmbeddingModel "OpenAIEmbeddingModel            dataclass   ")
- [`CohereEmbeddingModel`](#pydantic_ai.embeddings.cohere.CohereEmbeddingModel "CohereEmbeddingModel            dataclass   ")
- [`GoogleEmbeddingModel`](#pydantic_ai.embeddings.google.GoogleEmbeddingModel "GoogleEmbeddingModel            dataclass   ")
- [`SentenceTransformerEmbeddingModel`](#pydantic_ai.embeddings.sentence_transformers.SentenceTransformerEmbeddingModel "SentenceTransformerEmbeddingModel            dataclass   ")

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
  8
  9
 10
 11
 12
 13
 14
 15
 16
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
```

```
classEmbeddingModel(ABC):
"""Abstract base class for embedding models.

    Implement this class to create a custom embedding model. For most use cases,
    use one of the built-in implementations:

    - [`OpenAIEmbeddingModel`][pydantic_ai.embeddings.openai.OpenAIEmbeddingModel]
    - [`CohereEmbeddingModel`][pydantic_ai.embeddings.cohere.CohereEmbeddingModel]
    - [`GoogleEmbeddingModel`][pydantic_ai.embeddings.google.GoogleEmbeddingModel]
    - [`SentenceTransformerEmbeddingModel`][pydantic_ai.embeddings.sentence_transformers.SentenceTransformerEmbeddingModel]
    """

    _settings: EmbeddingSettings | None = None

    def__init__(
        self,
        *,
        settings: EmbeddingSettings | None = None,
    ) -> None:
"""Initialize the model with optional settings.

        Args:
            settings: Model-specific settings that will be used as defaults for this model.
        """
        self._settings = settings

    @property
    defsettings(self) -> EmbeddingSettings | None:
"""Get the default settings for this model."""
        return self._settings

    @property
    defbase_url(self) -> str | None:
"""The base URL for the provider API, if available."""
        return None

    @property
    @abstractmethod
    defmodel_name(self) -> str:
"""The name of the embedding model."""
        raise NotImplementedError()

    @property
    @abstractmethod
    defsystem(self) -> str:
"""The embedding model provider/system identifier (e.g., 'openai', 'cohere')."""
        raise NotImplementedError()

    @abstractmethod
    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
"""Generate embeddings for the given inputs.

        Args:
            inputs: A single string or sequence of strings to embed.
            input_type: Whether the inputs are queries or documents.
            settings: Optional settings to override the model's defaults.

        Returns:
            An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing
            the embeddings and metadata.
        """
        raise NotImplementedError

    defprepare_embed(
        self, inputs: str | Sequence[str], settings: EmbeddingSettings | None = None
    ) -> tuple[list[str], EmbeddingSettings]:
"""Prepare the inputs and settings for embedding.

        This method normalizes inputs to a list and merges settings.
        Subclasses should call this at the start of their `embed()` implementation.

        Args:
            inputs: A single string or sequence of strings.
            settings: Optional settings to merge with defaults.

        Returns:
            A tuple of (normalized inputs list, merged settings).
        """
        inputs = [inputs] if isinstance(inputs, str) else list(inputs)

        settings = merge_embedding_settings(self._settings, settings) or {}

        return inputs, settings

    async defmax_input_tokens(self) -> int | None:
"""Get the maximum number of tokens that can be input to the model.

        Returns:
            The maximum token count, or `None` if unknown.
        """
        return None  # pragma: no cover

    async defcount_tokens(self, text: str) -> int:
"""Count the number of tokens in the given text.

        Args:
            text: The text to tokenize and count.

        Returns:
            The number of tokens.

        Raises:
            NotImplementedError: If the model doesn't support token counting.
            UserError: If the model or tokenizer is not supported.
        """
        raise NotImplementedError
```

#### \_\_init\__

```
__init__(
    *, settings: EmbeddingSettings | None = None
) -> None
```

Initialize the model with optional settings.

Parameters:

Name Type Description Default `settings` `EmbeddingSettings | None`

Model-specific settings that will be used as defaults for this model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
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
```

```
def__init__(
    self,
    *,
    settings: EmbeddingSettings | None = None,
) -> None:
"""Initialize the model with optional settings.

    Args:
        settings: Model-specific settings that will be used as defaults for this model.
    """
    self._settings = settings
```

#### settings `property`

```
settings: EmbeddingSettings | None
```

Get the default settings for this model.

#### base\_url `property`

The base URL for the provider API, if available.

#### model\_name `abstractmethod` `property`

The name of the embedding model.

#### system `abstractmethod` `property`

The embedding model provider/system identifier (e.g., 'openai', 'cohere').

#### embed `abstractmethod` `async`

Generate embeddings for the given inputs.

Parameters:

Name Type Description Default `inputs` `str | Sequence[str]`

A single string or sequence of strings to embed.

*required* `input_type` `EmbedInputType`

Whether the inputs are queries or documents.

*required* `settings` `EmbeddingSettings | None`

Optional settings to override the model's defaults.

`None`

Returns:

Type Description `EmbeddingResult`

An [`EmbeddingResult`](#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult            dataclass   ") containing

`EmbeddingResult`

the embeddings and metadata.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
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
```

```
@abstractmethod
async defembed(
    self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
"""Generate embeddings for the given inputs.

    Args:
        inputs: A single string or sequence of strings to embed.
        input_type: Whether the inputs are queries or documents.
        settings: Optional settings to override the model's defaults.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing
        the embeddings and metadata.
    """
    raise NotImplementedError
```

#### prepare\_embed

Prepare the inputs and settings for embedding.

This method normalizes inputs to a list and merges settings. Subclasses should call this at the start of their `embed()` implementation.

Parameters:

Name Type Description Default `inputs` `str | Sequence[str]`

A single string or sequence of strings.

*required* `settings` `EmbeddingSettings | None`

Optional settings to merge with defaults.

`None`

Returns:

Type Description `tuple[list[str], EmbeddingSettings]`

A tuple of (normalized inputs list, merged settings).

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
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
```

```
defprepare_embed(
    self, inputs: str | Sequence[str], settings: EmbeddingSettings | None = None
) -> tuple[list[str], EmbeddingSettings]:
"""Prepare the inputs and settings for embedding.

    This method normalizes inputs to a list and merges settings.
    Subclasses should call this at the start of their `embed()` implementation.

    Args:
        inputs: A single string or sequence of strings.
        settings: Optional settings to merge with defaults.

    Returns:
        A tuple of (normalized inputs list, merged settings).
    """
    inputs = [inputs] if isinstance(inputs, str) else list(inputs)

    settings = merge_embedding_settings(self._settings, settings) or {}

    return inputs, settings
```

#### max\_input\_tokens `async`

```
max_input_tokens() -> int | None
```

Get the maximum number of tokens that can be input to the model.

Returns:

Type Description `int | None`

The maximum token count, or `None` if unknown.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
async defmax_input_tokens(self) -> int | None:
"""Get the maximum number of tokens that can be input to the model.

    Returns:
        The maximum token count, or `None` if unknown.
    """
    return None  # pragma: no cover
```

#### count\_tokens `async`

```
count_tokens(text: str) -> int
```

Count the number of tokens in the given text.

Parameters:

Name Type Description Default `text` `str`

The text to tokenize and count.

*required*

Returns:

Type Description `int`

The number of tokens.

Raises:

Type Description `NotImplementedError`

If the model doesn't support token counting.

`UserError`

If the model or tokenizer is not supported.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
102
103
104
105
106
107
108
109
110
111
112
113
114
115
```

```
async defcount_tokens(self, text: str) -> int:
"""Count the number of tokens in the given text.

    Args:
        text: The text to tokenize and count.

    Returns:
        The number of tokens.

    Raises:
        NotImplementedError: If the model doesn't support token counting.
        UserError: If the model or tokenizer is not supported.
    """
    raise NotImplementedError
```

### InstrumentedEmbeddingModel `dataclass`

Bases: `WrapperEmbeddingModel`

Embedding model which wraps another model so that requests are instrumented with OpenTelemetry.

See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/instrumented.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
```

```
@dataclass(init=False)
classInstrumentedEmbeddingModel(WrapperEmbeddingModel):
"""Embedding model which wraps another model so that requests are instrumented with OpenTelemetry.

    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
    """

    instrumentation_settings: InstrumentationSettings
"""Instrumentation settings for this model."""

    def__init__(
        self,
        wrapped: EmbeddingModel | str,
        options: InstrumentationSettings | None = None,
    ) -> None:
        super().__init__(wrapped)
        self.instrumentation_settings = options or InstrumentationSettings()

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        with self._instrument(inputs, input_type, settings) as finish:
            result = await super().embed(inputs, input_type=input_type, settings=settings)
            finish(result)
            return result

    @contextmanager
    def_instrument(
        self,
        inputs: list[str],
        input_type: EmbedInputType,
        settings: EmbeddingSettings | None,
    ) -> Iterator[Callable[[EmbeddingResult], None]]:
        operation = 'embeddings'
        span_name = f'{operation}{self.model_name}'

        inputs_count = len(inputs)

        attributes: dict[str, AttributeValue] = {
            'gen_ai.operation.name': operation,
            **self.model_attributes(self.wrapped),
            'input_type': input_type,
            'inputs_count': inputs_count,
        }

        if settings:
            attributes['embedding_settings'] = json.dumps(self.serialize_any(settings))

        if self.instrumentation_settings.include_content:
            attributes['inputs'] = json.dumps(inputs)

        attributes['logfire.json_schema'] = json.dumps(
            {
                'type': 'object',
                'properties': {
                    'input_type': {'type': 'string'},
                    'inputs_count': {'type': 'integer'},
                    'embedding_settings': {'type': 'object'},
                    **(
                        {'inputs': {'type': ['array']}, 'embeddings': {'type': 'array'}}
                        if self.instrumentation_settings.include_content
                        else {}
                    ),
                },
            }
        )

        record_metrics: Callable[[], None] | None = None
        try:
            with self.instrumentation_settings.tracer.start_as_current_span(span_name, attributes=attributes) as span:

                deffinish(result: EmbeddingResult):
                    # Prepare metric recording closure first so metrics are recorded
                    # even if the span is not recording.
                    provider_name = attributes[GEN_AI_PROVIDER_NAME_ATTRIBUTE]
                    request_model = attributes[GEN_AI_REQUEST_MODEL_ATTRIBUTE]
                    response_model = result.model_name or request_model
                    price_calculation = None

                    def_record_metrics():
                        token_attributes = {
                            GEN_AI_PROVIDER_NAME_ATTRIBUTE: provider_name,
                            'gen_ai.operation.name': operation,
                            GEN_AI_REQUEST_MODEL_ATTRIBUTE: request_model,
                            'gen_ai.response.model': response_model,
                            'gen_ai.token.type': 'input',
                        }
                        tokens = result.usage.input_tokens or 0
                        if tokens:  # pragma: no branch
                            self.instrumentation_settings.tokens_histogram.record(tokens, token_attributes)
                            if price_calculation is not None:
                                self.instrumentation_settings.cost_histogram.record(
                                    float(getattr(price_calculation, 'input_price', 0.0)),
                                    token_attributes,
                                )

                    nonlocal record_metrics
                    record_metrics = _record_metrics

                    if not span.is_recording():
                        return

                    attributes_to_set: dict[str, AttributeValue] = {
                        **result.usage.opentelemetry_attributes(),
                        'gen_ai.response.model': response_model,
                    }

                    try:
                        price_calculation = result.cost()
                    except LookupError:
                        # The cost of this provider/model is unknown, which is common.
                        pass
                    except Exception as e:  # pragma: no cover
                        warnings.warn(
                            f'Failed to get cost from response: {type(e).__name__}: {e}', CostCalculationFailedWarning
                        )
                    else:
                        attributes_to_set['operation.cost'] = float(price_calculation.total_price)

                    embeddings = result.embeddings
                    if embeddings:  # pragma: no branch
                        attributes_to_set['gen_ai.embeddings.dimension.count'] = len(embeddings[0])
                        if self.instrumentation_settings.include_content:
                            attributes['embeddings'] = json.dumps(embeddings)

                    if result.provider_response_id is not None:
                        attributes_to_set['gen_ai.response.id'] = result.provider_response_id

                    span.set_attributes(attributes_to_set)

                yield finish
        finally:
            if record_metrics:  # pragma: no branch
                # Record metrics after the span finishes to avoid duplication.
                record_metrics()

    @staticmethod
    defmodel_attributes(model: EmbeddingModel) -> dict[str, AttributeValue]:
        attributes: dict[str, AttributeValue] = {
            GEN_AI_PROVIDER_NAME_ATTRIBUTE: model.system,
            GEN_AI_REQUEST_MODEL_ATTRIBUTE: model.model_name,
        }
        if base_url := model.base_url:
            try:
                parsed = urlparse(base_url)
            except Exception:  # pragma: no cover
                pass
            else:
                if parsed.hostname:  # pragma: no branch
                    attributes['server.address'] = parsed.hostname
                if parsed.port:
                    attributes['server.port'] = parsed.port  # pragma: no cover

        return attributes

    @staticmethod
    defserialize_any(value: Any) -> str:
        try:
            return ANY_ADAPTER.dump_python(value, mode='json')
        except Exception:  # pragma: no cover
            try:
                return str(value)
            except Exception as e:
                return f'Unable to serialize: {e}'
```

#### instrumentation\_settings `instance-attribute`

Instrumentation settings for this model.

### instrument\_embedding\_model

Instrument an embedding model with OpenTelemetry/logfire.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/instrumented.py`

```
30
31
32
33
34
35
36
37
38
```

```
definstrument_embedding_model(model: EmbeddingModel, instrument: InstrumentationSettings | bool) -> EmbeddingModel:
"""Instrument an embedding model with OpenTelemetry/logfire."""
    if instrument and not isinstance(model, InstrumentedEmbeddingModel):
        if instrument is True:
            instrument = InstrumentationSettings()

        model = InstrumentedEmbeddingModel(model, instrument)

    return model
```

### EmbeddingResult `dataclass`

The result of an embedding operation.

This class contains the generated embeddings along with metadata about the operation, including the original inputs, model information, usage statistics, and timing.

Example:

```
frompydantic_aiimport Embedder

embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    result = await embedder.embed_query('What is AI?')

    # Access embeddings by index
    print(len(result.embeddings[0]))
    #> 1536

    # Access embeddings by original input text
    print(result['What is AI?'] == result.embeddings[0])
    #> True

    # Check usage
    print(f'Tokens used: {result.usage.input_tokens}')
    #> Tokens used: 3
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
```

````
@dataclass
classEmbeddingResult:
"""The result of an embedding operation.

    This class contains the generated embeddings along with metadata about
    the operation, including the original inputs, model information, usage
    statistics, and timing.

    Example:
    ```python
    from pydantic_ai import Embedder

    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        result = await embedder.embed_query('What is AI?')

        # Access embeddings by index
        print(len(result.embeddings[0]))
        #> 1536

        # Access embeddings by original input text
        print(result['What is AI?'] == result.embeddings[0])
        #> True

        # Check usage
        print(f'Tokens used: {result.usage.input_tokens}')
        #> Tokens used: 3
    ```
    """

    embeddings: Sequence[Sequence[float]]
"""The computed embedding vectors, one per input text.

    Each embedding is a sequence of floats representing the text in vector space.
    """

    _: KW_ONLY

    inputs: Sequence[str]
"""The original input texts that were embedded."""

    input_type: EmbedInputType
"""Whether the inputs were embedded as queries or documents."""

    model_name: str
"""The name of the model that generated these embeddings."""

    provider_name: str
"""The name of the provider (e.g., 'openai', 'cohere')."""

    timestamp: datetime = field(default_factory=_now_utc)
"""When the embedding request was made."""

    usage: RequestUsage = field(default_factory=RequestUsage)
"""Token usage statistics for this request."""

    provider_details: dict[str, Any] | None = None
"""Provider-specific details from the response."""

    provider_response_id: str | None = None
"""Unique identifier for this response from the provider, if available."""

    def__getitem__(self, item: int | str) -> Sequence[float]:
"""Get the embedding for an input by index or by the original input text.

        Args:
            item: Either an integer index or the original input string.

        Returns:
            The embedding vector for the specified input.

        Raises:
            IndexError: If the index is out of range.
            ValueError: If the string is not found in the inputs.
        """
        if isinstance(item, str):
            item = self.inputs.index(item)

        return self.embeddings[item]

    defcost(self) -> genai_types.PriceCalculation:
"""Calculate the cost of the embedding request.

        Uses [`genai-prices`](https://github.com/pydantic/genai-prices) for pricing data.

        Returns:
            A price calculation object with `total_price`, `input_price`, and other cost details.

        Raises:
            LookupError: If pricing data is not available for this model/provider.
        """
        assert self.model_name, 'Model name is required to calculate price'
        return calc_price(
            self.usage,
            self.model_name,
            provider_id=self.provider_name,
            genai_request_timestamp=self.timestamp,
        )
````

#### embeddings `instance-attribute`

The computed embedding vectors, one per input text.

Each embedding is a sequence of floats representing the text in vector space.

#### inputs `instance-attribute`

The original input texts that were embedded.

#### input\_type `instance-attribute`

```
input_type: EmbedInputType
```

Whether the inputs were embedded as queries or documents.

#### model\_name `instance-attribute`

The name of the model that generated these embeddings.

#### provider\_name `instance-attribute`

The name of the provider (e.g., 'openai', 'cohere').

#### timestamp `class-attribute` `instance-attribute`

When the embedding request was made.

#### usage `class-attribute` `instance-attribute`

Token usage statistics for this request.

#### provider\_details `class-attribute` `instance-attribute`

Provider-specific details from the response.

#### provider\_response\_id `class-attribute` `instance-attribute`

```
provider_response_id: str | None = None
```

Unique identifier for this response from the provider, if available.

#### \_\_getitem\__

Get the embedding for an input by index or by the original input text.

Parameters:

Name Type Description Default `item` `int | str`

Either an integer index or the original input string.

*required*

Returns:

Type Description `Sequence[float]`

The embedding vector for the specified input.

Raises:

Type Description `IndexError`

If the index is out of range.

`ValueError`

If the string is not found in the inputs.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`

```
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
100
101
```

```
def__getitem__(self, item: int | str) -> Sequence[float]:
"""Get the embedding for an input by index or by the original input text.

    Args:
        item: Either an integer index or the original input string.

    Returns:
        The embedding vector for the specified input.

    Raises:
        IndexError: If the index is out of range.
        ValueError: If the string is not found in the inputs.
    """
    if isinstance(item, str):
        item = self.inputs.index(item)

    return self.embeddings[item]
```

#### cost

```
cost() -> PriceCalculation
```

Calculate the cost of the embedding request.

Uses [`genai-prices`](https://github.com/pydantic/genai-prices) for pricing data.

Returns:

Type Description `PriceCalculation`

A price calculation object with `total_price`, `input_price`, and other cost details.

Raises:

Type Description `LookupError`

If pricing data is not available for this model/provider.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`

```
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
```

```
defcost(self) -> genai_types.PriceCalculation:
"""Calculate the cost of the embedding request.

    Uses [`genai-prices`](https://github.com/pydantic/genai-prices) for pricing data.

    Returns:
        A price calculation object with `total_price`, `input_price`, and other cost details.

    Raises:
        LookupError: If pricing data is not available for this model/provider.
    """
    assert self.model_name, 'Model name is required to calculate price'
    return calc_price(
        self.usage,
        self.model_name,
        provider_id=self.provider_name,
        genai_request_timestamp=self.timestamp,
    )
```

### EmbeddingSettings

Bases: `TypedDict`

Common settings for configuring embedding models.

These settings apply across multiple embedding model providers. Not all settings are supported by all models - check the specific model's documentation for details.

Provider-specific settings classes (e.g., [`OpenAIEmbeddingSettings`](#pydantic_ai.embeddings.openai.OpenAIEmbeddingSettings "OpenAIEmbeddingSettings"), [`CohereEmbeddingSettings`](#pydantic_ai.embeddings.cohere.CohereEmbeddingSettings "CohereEmbeddingSettings")) extend this with additional provider-prefixed options.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/settings.py`

```
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
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
```

```
classEmbeddingSettings(TypedDict, total=False):
"""Common settings for configuring embedding models.

    These settings apply across multiple embedding model providers.
    Not all settings are supported by all models - check the specific
    model's documentation for details.

    Provider-specific settings classes (e.g.,
    [`OpenAIEmbeddingSettings`][pydantic_ai.embeddings.openai.OpenAIEmbeddingSettings],
    [`CohereEmbeddingSettings`][pydantic_ai.embeddings.cohere.CohereEmbeddingSettings])
    extend this with additional provider-prefixed options.
    """

    dimensions: int
"""The number of dimensions for the output embeddings.

    Supported by:

    * OpenAI
    * Cohere
    * Google
    * Sentence Transformers
    * VoyageAI
    """

    truncate: bool
"""Whether to truncate inputs that exceed the model's context length.

    Defaults to `False`. If `True`, inputs that are too long will be truncated.
    If `False`, an error will be raised for inputs that exceed the context length.

    For more control over truncation, you can use
    [`max_input_tokens()`][pydantic_ai.embeddings.Embedder.max_input_tokens] and
    [`count_tokens()`][pydantic_ai.embeddings.Embedder.count_tokens] to implement
    your own truncation logic.

    Provider-specific truncation settings (e.g., `cohere_truncate`) take precedence
    if specified.

    Supported by:

    * Cohere
    * VoyageAI
    """

    extra_headers: dict[str, str]
"""Extra headers to send to the model.

    Supported by:

    * OpenAI
    * Cohere
    """

    extra_body: object
"""Extra body to send to the model.

    Supported by:

    * OpenAI
    * Cohere
    """
```

#### dimensions `instance-attribute`

The number of dimensions for the output embeddings.

Supported by:

- OpenAI
- Cohere
- Google
- Sentence Transformers
- VoyageAI

#### truncate `instance-attribute`

Whether to truncate inputs that exceed the model's context length.

Defaults to `False`. If `True`, inputs that are too long will be truncated. If `False`, an error will be raised for inputs that exceed the context length.

For more control over truncation, you can use [`max_input_tokens()`](#pydantic_ai.embeddings.Embedder.max_input_tokens "max_input_tokens            async   ") and [`count_tokens()`](#pydantic_ai.embeddings.Embedder.count_tokens "count_tokens            async   ") to implement your own truncation logic.

Provider-specific truncation settings (e.g., `cohere_truncate`) take precedence if specified.

Supported by:

- Cohere
- VoyageAI

Extra headers to send to the model.

Supported by:

- OpenAI
- Cohere

#### extra\_body `instance-attribute`

Extra body to send to the model.

Supported by:

- OpenAI
- Cohere

### merge\_embedding\_settings

```
merge_embedding_settings(
    base: EmbeddingSettings | None,
    overrides: EmbeddingSettings | None,
) -> EmbeddingSettings | None
```

Merge two sets of embedding settings, with overrides taking precedence.

Parameters:

Name Type Description Default `base` `EmbeddingSettings | None`

Base settings (typically from the embedder or model).

*required* `overrides` `EmbeddingSettings | None`

Settings that should override the base (typically per-call settings).

*required*

Returns:

Type Description `EmbeddingSettings | None`

Merged settings, or `None` if both inputs are `None`.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/settings.py`

```
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
```

```
defmerge_embedding_settings(
    base: EmbeddingSettings | None, overrides: EmbeddingSettings | None
) -> EmbeddingSettings | None:
"""Merge two sets of embedding settings, with overrides taking precedence.

    Args:
        base: Base settings (typically from the embedder or model).
        overrides: Settings that should override the base (typically per-call settings).

    Returns:
        Merged settings, or `None` if both inputs are `None`.
    """
    # Note: we may want merge recursively if/when we add non-primitive values
    if base and overrides:
        return base | overrides
    else:
        return base or overrides
```

### TestEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

A mock embedding model for testing.

This model returns deterministic embeddings (all 1.0 values) and tracks the settings used in the last call via the `last_settings` attribute.

Example:

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddingsimport TestEmbeddingModel

test_model = TestEmbeddingModel()
embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    with embedder.override(model=test_model):
        await embedder.embed_query('test')
        assert test_model.last_settings is not None
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/test.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
```

````
@dataclass(init=False)
classTestEmbeddingModel(EmbeddingModel):
"""A mock embedding model for testing.

    This model returns deterministic embeddings (all 1.0 values) and tracks
    the settings used in the last call via the `last_settings` attribute.

    Example:
    ```python
    from pydantic_ai import Embedder
    from pydantic_ai.embeddings import TestEmbeddingModel

    test_model = TestEmbeddingModel()
    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        with embedder.override(model=test_model):
            await embedder.embed_query('test')
            assert test_model.last_settings is not None
    ```
    """

    # NOTE: Avoid test discovery by pytest.
    __test__ = False

    _model_name: str
"""The model name to report in results."""

    _provider_name: str
"""The provider name to report in results."""

    _dimensions: int
"""The number of dimensions for generated embeddings."""

    last_settings: EmbeddingSettings | None = None
"""The settings used in the most recent embed call."""

    def__init__(
        self,
        model_name: str = 'test',
        *,
        provider_name: str = 'test',
        dimensions: int = 8,
        settings: EmbeddingSettings | None = None,
    ):
"""Initialize the test embedding model.

        Args:
            model_name: The model name to report in results.
            provider_name: The provider name to report in results.
            dimensions: The number of dimensions for the generated embeddings.
            settings: Optional default settings for the model.
        """
        self._model_name = model_name
        self._provider_name = provider_name
        self._dimensions = dimensions
        self.last_settings = None
        super().__init__(settings=settings)

    @property
    defmodel_name(self) -> str:
"""The embedding model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The embedding model provider."""
        return self._provider_name

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        self.last_settings = settings

        dimensions = settings.get('dimensions') or self._dimensions

        return EmbeddingResult(
            embeddings=[[1.0] * dimensions] * len(inputs),
            inputs=inputs,
            input_type=input_type,
            usage=RequestUsage(input_tokens=sum(_estimate_tokens(text) for text in inputs)),
            model_name=self.model_name,
            provider_name=self.system,
            provider_response_id=str(uuid.uuid4()),
        )

    async defmax_input_tokens(self) -> int | None:
        return 1024

    async defcount_tokens(self, text: str) -> int:
        return _estimate_tokens(text)
````

#### last\_settings `class-attribute` `instance-attribute`

```
last_settings: EmbeddingSettings | None = None
```

The settings used in the most recent embed call.

#### \_\_init\__

```
__init__(
    model_name: str = "test",
    *,
    provider_name: str = "test",
    dimensions: int = 8,
    settings: EmbeddingSettings | None = None
)
```

Initialize the test embedding model.

Parameters:

Name Type Description Default `model_name` `str`

The model name to report in results.

`'test'` `provider_name` `str`

The provider name to report in results.

`'test'` `dimensions` `int`

The number of dimensions for the generated embeddings.

`8` `settings` `EmbeddingSettings | None`

Optional default settings for the model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/test.py`

```
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
```

```
def__init__(
    self,
    model_name: str = 'test',
    *,
    provider_name: str = 'test',
    dimensions: int = 8,
    settings: EmbeddingSettings | None = None,
):
"""Initialize the test embedding model.

    Args:
        model_name: The model name to report in results.
        provider_name: The provider name to report in results.
        dimensions: The number of dimensions for the generated embeddings.
        settings: Optional default settings for the model.
    """
    self._model_name = model_name
    self._provider_name = provider_name
    self._dimensions = dimensions
    self.last_settings = None
    super().__init__(settings=settings)
```

#### model\_name `property`

The embedding model name.

#### system `property`

The embedding model provider.

### WrapperEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

Base class for embedding models that wrap another model.

Use this as a base class to create custom embedding model wrappers that modify behavior (e.g., caching, logging, rate limiting) while delegating to an underlying model.

By default, all methods are passed through to the wrapped model. Override specific methods to customize behavior.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/wrapper.py`

```
15
16
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
```

```
@dataclass(init=False)
classWrapperEmbeddingModel(EmbeddingModel):
"""Base class for embedding models that wrap another model.

    Use this as a base class to create custom embedding model wrappers
    that modify behavior (e.g., caching, logging, rate limiting) while
    delegating to an underlying model.

    By default, all methods are passed through to the wrapped model.
    Override specific methods to customize behavior.
    """

    wrapped: EmbeddingModel
"""The underlying embedding model being wrapped."""

    def__init__(self, wrapped: EmbeddingModel | str):
"""Initialize the wrapper with an embedding model.

        Args:
            wrapped: The model to wrap. Can be an
                [`EmbeddingModel`][pydantic_ai.embeddings.EmbeddingModel] instance
                or a model name string (e.g., `'openai:text-embedding-3-small'`).
        """
        from.import infer_embedding_model

        super().__init__()
        self.wrapped = infer_embedding_model(wrapped) if isinstance(wrapped, str) else wrapped

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        return await self.wrapped.embed(inputs, input_type=input_type, settings=settings)

    async defmax_input_tokens(self) -> int | None:
        return await self.wrapped.max_input_tokens()

    async defcount_tokens(self, text: str) -> int:
        return await self.wrapped.count_tokens(text)

    @property
    defmodel_name(self) -> str:
        return self.wrapped.model_name

    @property
    defsystem(self) -> str:
        return self.wrapped.system

    @property
    defsettings(self) -> EmbeddingSettings | None:
"""Get the settings from the wrapped embedding model."""
        return self.wrapped.settings

    @property
    defbase_url(self) -> str | None:
        return self.wrapped.base_url

    def__getattr__(self, item: str):
        return getattr(self.wrapped, item)  # pragma: no cover
```

#### wrapped `instance-attribute`

The underlying embedding model being wrapped.

#### \_\_init\__

```
__init__(wrapped: EmbeddingModel | str)
```

Initialize the wrapper with an embedding model.

Parameters:

Name Type Description Default `wrapped` `EmbeddingModel | str`

The model to wrap. Can be an [`EmbeddingModel`](#pydantic_ai.embeddings.EmbeddingModel "EmbeddingModel") instance or a model name string (e.g., `'openai:text-embedding-3-small'`).

*required*

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/wrapper.py`

```
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
```

```
def__init__(self, wrapped: EmbeddingModel | str):
"""Initialize the wrapper with an embedding model.

    Args:
        wrapped: The model to wrap. Can be an
            [`EmbeddingModel`][pydantic_ai.embeddings.EmbeddingModel] instance
            or a model name string (e.g., `'openai:text-embedding-3-small'`).
    """
    from.import infer_embedding_model

    super().__init__()
    self.wrapped = infer_embedding_model(wrapped) if isinstance(wrapped, str) else wrapped
```

#### settings `property`

```
settings: EmbeddingSettings | None
```

Get the settings from the wrapped embedding model.

### KnownEmbeddingModelName `module-attribute`

```
KnownEmbeddingModelName = TypeAliasType(
    "KnownEmbeddingModelName",
    Literal[
        "google-gla:gemini-embedding-001",
        "google-vertex:gemini-embedding-001",
        "google-vertex:text-embedding-005",
        "google-vertex:text-multilingual-embedding-002",
        "openai:text-embedding-ada-002",
        "openai:text-embedding-3-small",
        "openai:text-embedding-3-large",
        "cohere:embed-v4.0",
        "cohere:embed-english-v3.0",
        "cohere:embed-english-light-v3.0",
        "cohere:embed-multilingual-v3.0",
        "cohere:embed-multilingual-light-v3.0",
        "voyageai:voyage-4-large",
        "voyageai:voyage-4",
        "voyageai:voyage-4-lite",
        "voyageai:voyage-3-large",
        "voyageai:voyage-3.5",
        "voyageai:voyage-3.5-lite",
        "voyageai:voyage-code-3",
        "voyageai:voyage-finance-2",
        "voyageai:voyage-law-2",
        "voyageai:voyage-code-2",
    ],
)
```

Known model names that can be used with the `model` parameter of [`Embedder`](#pydantic_ai.embeddings.Embedder "Embedder            dataclass   ").

`KnownEmbeddingModelName` is provided as a concise way to specify an embedding model.

### infer\_embedding\_model

Infer the model from the name.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
```

```
definfer_embedding_model(
    model: EmbeddingModel | KnownEmbeddingModelName | str,
    *,
    provider_factory: Callable[[str], Provider[Any]] = infer_provider,
) -> EmbeddingModel:
"""Infer the model from the name."""
    if isinstance(model, EmbeddingModel):
        return model

    try:
        provider_name, model_name = model.split(':', maxsplit=1)
    except ValueError as e:
        raise ValueError('You must provide a provider prefix when specifying an embedding model name') frome

    provider = provider_factory(provider_name)

    model_kind = provider_name
    if model_kind.startswith('gateway/'):
        from..providers.gatewayimport normalize_gateway_provider

        model_kind = normalize_gateway_provider(model_kind)

    if model_kind in (
        'openai',
        # For now, we assume that every chat and completions-compatible provider also
        # supports the embeddings endpoint, as at worst the user would get an `ModelHTTPError`.
        *get_args(OpenAIChatCompatibleProvider.__value__),
        *get_args(OpenAIResponsesCompatibleProvider.__value__),
    ):
        from.openaiimport OpenAIEmbeddingModel

        return OpenAIEmbeddingModel(model_name, provider=provider)
    elif model_kind == 'cohere':
        from.cohereimport CohereEmbeddingModel

        return CohereEmbeddingModel(model_name, provider=provider)
    elif model_kind in ('google-gla', 'google-vertex'):
        from.googleimport GoogleEmbeddingModel

        return GoogleEmbeddingModel(model_name, provider=provider)
    elif model_kind == 'sentence-transformers':
        from.sentence_transformersimport SentenceTransformerEmbeddingModel

        return SentenceTransformerEmbeddingModel(model_name)
    elif model_kind == 'voyageai':
        from.voyageaiimport VoyageAIEmbeddingModel

        return VoyageAIEmbeddingModel(model_name, provider=provider)
    else:
        raise UserError(f'Unknown embeddings model: {model}')  # pragma: no cover
```

### Embedder `dataclass`

High-level interface for generating text embeddings.

The `Embedder` class provides a convenient way to generate vector embeddings from text using various embedding model providers. It handles model inference, settings management, and optional OpenTelemetry instrumentation.

Example:

```
frompydantic_aiimport Embedder

embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    result = await embedder.embed_query('What is machine learning?')
    print(result.embeddings[0][:5])  # First 5 dimensions
    #> [1.0, 1.0, 1.0, 1.0, 1.0]
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
```

````
@dataclass(init=False)
classEmbedder:
"""High-level interface for generating text embeddings.

    The `Embedder` class provides a convenient way to generate vector embeddings from text
    using various embedding model providers. It handles model inference, settings management,
    and optional OpenTelemetry instrumentation.

    Example:
    ```python
    from pydantic_ai import Embedder

    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        result = await embedder.embed_query('What is machine learning?')
        print(result.embeddings[0][:5])  # First 5 dimensions
        #> [1.0, 1.0, 1.0, 1.0, 1.0]
    ```
    """

    instrument: InstrumentationSettings | bool | None
"""Options to automatically instrument with OpenTelemetry.

    Set to `True` to use default instrumentation settings, which will use Logfire if it's configured.
    Set to an instance of [`InstrumentationSettings`][pydantic_ai.models.instrumented.InstrumentationSettings] to customize.
    If this isn't set, then the last value set by
    [`Embedder.instrument_all()`][pydantic_ai.embeddings.Embedder.instrument_all]
    will be used, which defaults to False.
    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
    """

    _instrument_default: ClassVar[InstrumentationSettings | bool] = False

    def__init__(
        self,
        model: EmbeddingModel | KnownEmbeddingModelName | str,
        *,
        settings: EmbeddingSettings | None = None,
        defer_model_check: bool = True,
        instrument: InstrumentationSettings | bool | None = None,
    ) -> None:
"""Initialize an Embedder.

        Args:
            model: The embedding model to use. Can be specified as:

                - A model name string in the format `'provider:model-name'`
                  (e.g., `'openai:text-embedding-3-small'`)
                - An [`EmbeddingModel`][pydantic_ai.embeddings.EmbeddingModel] instance
            settings: Optional [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for all embed calls.
            defer_model_check: Whether to defer model validation until first use.
                Set to `False` to validate the model immediately on construction.
            instrument: OpenTelemetry instrumentation settings. Set to `True` to enable with defaults,
                or pass an [`InstrumentationSettings`][pydantic_ai.models.instrumented.InstrumentationSettings]
                instance to customize. If `None`, uses the value from
                [`Embedder.instrument_all()`][pydantic_ai.embeddings.Embedder.instrument_all].
        """
        self._model = model if defer_model_check else infer_embedding_model(model)
        self._settings = settings
        self.instrument = instrument

        self._override_model: ContextVar[EmbeddingModel | None] = ContextVar('_override_model', default=None)

    @staticmethod
    definstrument_all(instrument: InstrumentationSettings | bool = True) -> None:
"""Set the default instrumentation options for all embedders where `instrument` is not explicitly set.

        This is useful for enabling instrumentation globally without modifying each embedder individually.

        Args:
            instrument: Instrumentation settings to use as the default. Set to `True` for default settings,
                `False` to disable, or pass an
                [`InstrumentationSettings`][pydantic_ai.models.instrumented.InstrumentationSettings]
                instance to customize.
        """
        Embedder._instrument_default = instrument

    @property
    defmodel(self) -> EmbeddingModel | KnownEmbeddingModelName | str:
"""The embedding model used by this embedder."""
        return self._model

    @contextmanager
    defoverride(
        self,
        *,
        model: EmbeddingModel | KnownEmbeddingModelName | str | _utils.Unset = _utils.UNSET,
    ) -> Iterator[None]:
"""Context manager to temporarily override the embedding model.

        Useful for testing or dynamically switching models.

        Args:
            model: The embedding model to use within this context.

        Example:
        ```python
        from pydantic_ai import Embedder

        embedder = Embedder('openai:text-embedding-3-small')


        async def main():
            # Temporarily use a different model
            with embedder.override(model='openai:text-embedding-3-large'):
                result = await embedder.embed_query('test')
                print(len(result.embeddings[0]))  # 3072 dimensions for large model
                #> 3072
        ```
        """
        if _utils.is_set(model):
            model_token = self._override_model.set(infer_embedding_model(model))
        else:
            model_token = None

        try:
            yield
        finally:
            if model_token is not None:
                self._override_model.reset(model_token)

    async defembed_query(
        self, query: str | Sequence[str], *, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
"""Embed one or more query texts.

        Use this method when embedding search queries that will be compared against document embeddings.
        Some models optimize embeddings differently based on whether the input is a query or document.

        Args:
            query: A single query string or sequence of query strings to embed.
            settings: Optional settings to override the embedder's default settings for this call.

        Returns:
            An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
            and metadata about the operation.
        """
        return await self.embed(query, input_type='query', settings=settings)

    async defembed_documents(
        self, documents: str | Sequence[str], *, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
"""Embed one or more document texts.

        Use this method when embedding documents that will be stored and later searched against.
        Some models optimize embeddings differently based on whether the input is a query or document.

        Args:
            documents: A single document string or sequence of document strings to embed.
            settings: Optional settings to override the embedder's default settings for this call.

        Returns:
            An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
            and metadata about the operation.
        """
        return await self.embed(documents, input_type='document', settings=settings)

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
"""Embed text inputs with explicit input type specification.

        This is the low-level embedding method. For most use cases, prefer
        [`embed_query()`][pydantic_ai.embeddings.Embedder.embed_query] or
        [`embed_documents()`][pydantic_ai.embeddings.Embedder.embed_documents].

        Args:
            inputs: A single string or sequence of strings to embed.
            input_type: The type of input, either `'query'` or `'document'`.
            settings: Optional settings to override the embedder's default settings for this call.

        Returns:
            An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
            and metadata about the operation.
        """
        model = self._get_model()
        settings = merge_embedding_settings(self._settings, settings)
        return await model.embed(inputs, input_type=input_type, settings=settings)

    async defmax_input_tokens(self) -> int | None:
"""Get the maximum number of tokens the model can accept as input.

        Returns:
            The maximum token count, or `None` if the limit is unknown for this model.
        """
        model = self._get_model()
        return await model.max_input_tokens()

    async defcount_tokens(self, text: str) -> int:
"""Count the number of tokens in the given text.

        Args:
            text: The text to tokenize and count.

        Returns:
            The number of tokens in the text.

        Raises:
            NotImplementedError: If the model doesn't support token counting.
            UserError: If the model or tokenizer is not supported.
        """
        model = self._get_model()
        return await model.count_tokens(text)

    defembed_query_sync(
        self, query: str | Sequence[str], *, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
"""Synchronous version of [`embed_query()`][pydantic_ai.embeddings.Embedder.embed_query]."""
        return _utils.get_event_loop().run_until_complete(self.embed_query(query, settings=settings))

    defembed_documents_sync(
        self, documents: str | Sequence[str], *, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
"""Synchronous version of [`embed_documents()`][pydantic_ai.embeddings.Embedder.embed_documents]."""
        return _utils.get_event_loop().run_until_complete(self.embed_documents(documents, settings=settings))

    defembed_sync(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
"""Synchronous version of [`embed()`][pydantic_ai.embeddings.Embedder.embed]."""
        return _utils.get_event_loop().run_until_complete(self.embed(inputs, input_type=input_type, settings=settings))

    defmax_input_tokens_sync(self) -> int | None:
"""Synchronous version of [`max_input_tokens()`][pydantic_ai.embeddings.Embedder.max_input_tokens]."""
        return _utils.get_event_loop().run_until_complete(self.max_input_tokens())

    defcount_tokens_sync(self, text: str) -> int:
"""Synchronous version of [`count_tokens()`][pydantic_ai.embeddings.Embedder.count_tokens]."""
        return _utils.get_event_loop().run_until_complete(self.count_tokens(text))

    def_get_model(self) -> EmbeddingModel:
"""Create a model configured for this embedder.

        Returns:
            The embedding model to use, with instrumentation applied if configured.
        """
        model_: EmbeddingModel
        if some_model := self._override_model.get():
            model_ = some_model
        else:
            model_ = self._model = infer_embedding_model(self.model)

        instrument = self.instrument
        if instrument is None:
            instrument = self._instrument_default

        return instrument_embedding_model(model_, instrument)
````

#### \_\_init\__

Initialize an Embedder.

Parameters:

Name Type Description Default `model` `EmbeddingModel | KnownEmbeddingModelName | str`

The embedding model to use. Can be specified as:

- A model name string in the format `'provider:model-name'` (e.g., `'openai:text-embedding-3-small'`)
- An [`EmbeddingModel`](#pydantic_ai.embeddings.EmbeddingModel "EmbeddingModel") instance

*required* `settings` `EmbeddingSettings | None`

Optional [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for all embed calls.

`None` `defer_model_check` `bool`

Whether to defer model validation until first use. Set to `False` to validate the model immediately on construction.

`True` `instrument` `InstrumentationSettings | bool | None`

OpenTelemetry instrumentation settings. Set to `True` to enable with defaults, or pass an [`InstrumentationSettings`](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings            dataclass   ") instance to customize. If `None`, uses the value from [`Embedder.instrument_all()`](#pydantic_ai.embeddings.Embedder.instrument_all "instrument_all            staticmethod   ").

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
```

```
def__init__(
    self,
    model: EmbeddingModel | KnownEmbeddingModelName | str,
    *,
    settings: EmbeddingSettings | None = None,
    defer_model_check: bool = True,
    instrument: InstrumentationSettings | bool | None = None,
) -> None:
"""Initialize an Embedder.

    Args:
        model: The embedding model to use. Can be specified as:

            - A model name string in the format `'provider:model-name'`
              (e.g., `'openai:text-embedding-3-small'`)
            - An [`EmbeddingModel`][pydantic_ai.embeddings.EmbeddingModel] instance
        settings: Optional [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for all embed calls.
        defer_model_check: Whether to defer model validation until first use.
            Set to `False` to validate the model immediately on construction.
        instrument: OpenTelemetry instrumentation settings. Set to `True` to enable with defaults,
            or pass an [`InstrumentationSettings`][pydantic_ai.models.instrumented.InstrumentationSettings]
            instance to customize. If `None`, uses the value from
            [`Embedder.instrument_all()`][pydantic_ai.embeddings.Embedder.instrument_all].
    """
    self._model = model if defer_model_check else infer_embedding_model(model)
    self._settings = settings
    self.instrument = instrument

    self._override_model: ContextVar[EmbeddingModel | None] = ContextVar('_override_model', default=None)
```

#### instrument `instance-attribute`

Options to automatically instrument with OpenTelemetry.

Set to `True` to use default instrumentation settings, which will use Logfire if it's configured. Set to an instance of [`InstrumentationSettings`](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings            dataclass   ") to customize. If this isn't set, then the last value set by [`Embedder.instrument_all()`](#pydantic_ai.embeddings.Embedder.instrument_all "instrument_all            staticmethod   ") will be used, which defaults to False. See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.

#### instrument\_all `staticmethod`

Set the default instrumentation options for all embedders where `instrument` is not explicitly set.

This is useful for enabling instrumentation globally without modifying each embedder individually.

Parameters:

Name Type Description Default `instrument` `InstrumentationSettings | bool`

Instrumentation settings to use as the default. Set to `True` for default settings, `False` to disable, or pass an [`InstrumentationSettings`](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings            dataclass   ") instance to customize.

`True`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
191
192
193
194
195
196
197
198
199
200
201
202
203
```

```
@staticmethod
definstrument_all(instrument: InstrumentationSettings | bool = True) -> None:
"""Set the default instrumentation options for all embedders where `instrument` is not explicitly set.

    This is useful for enabling instrumentation globally without modifying each embedder individually.

    Args:
        instrument: Instrumentation settings to use as the default. Set to `True` for default settings,
            `False` to disable, or pass an
            [`InstrumentationSettings`][pydantic_ai.models.instrumented.InstrumentationSettings]
            instance to customize.
    """
    Embedder._instrument_default = instrument
```

#### model `property`

The embedding model used by this embedder.

#### override

Context manager to temporarily override the embedding model.

Useful for testing or dynamically switching models.

Parameters:

Name Type Description Default `model` `EmbeddingModel | KnownEmbeddingModelName | str | Unset`

The embedding model to use within this context.

`UNSET`

Example:

```
frompydantic_aiimport Embedder

embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    # Temporarily use a different model
    with embedder.override(model='openai:text-embedding-3-large'):
        result = await embedder.embed_query('test')
        print(len(result.embeddings[0]))  # 3072 dimensions for large model
        #> 3072
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
```

````
@contextmanager
defoverride(
    self,
    *,
    model: EmbeddingModel | KnownEmbeddingModelName | str | _utils.Unset = _utils.UNSET,
) -> Iterator[None]:
"""Context manager to temporarily override the embedding model.

    Useful for testing or dynamically switching models.

    Args:
        model: The embedding model to use within this context.

    Example:
    ```python
    from pydantic_ai import Embedder

    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        # Temporarily use a different model
        with embedder.override(model='openai:text-embedding-3-large'):
            result = await embedder.embed_query('test')
            print(len(result.embeddings[0]))  # 3072 dimensions for large model
            #> 3072
    ```
    """
    if _utils.is_set(model):
        model_token = self._override_model.set(infer_embedding_model(model))
    else:
        model_token = None

    try:
        yield
    finally:
        if model_token is not None:
            self._override_model.reset(model_token)
````

#### embed\_query `async`

Embed one or more query texts.

Use this method when embedding search queries that will be compared against document embeddings. Some models optimize embeddings differently based on whether the input is a query or document.

Parameters:

Name Type Description Default `query` `str | Sequence[str]`

A single query string or sequence of query strings to embed.

*required* `settings` `EmbeddingSettings | None`

Optional settings to override the embedder's default settings for this call.

`None`

Returns:

Type Description `EmbeddingResult`

An [`EmbeddingResult`](#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult            dataclass   ") containing the embeddings

`EmbeddingResult`

and metadata about the operation.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
```

```
async defembed_query(
    self, query: str | Sequence[str], *, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
"""Embed one or more query texts.

    Use this method when embedding search queries that will be compared against document embeddings.
    Some models optimize embeddings differently based on whether the input is a query or document.

    Args:
        query: A single query string or sequence of query strings to embed.
        settings: Optional settings to override the embedder's default settings for this call.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
        and metadata about the operation.
    """
    return await self.embed(query, input_type='query', settings=settings)
```

#### embed\_documents `async`

Embed one or more document texts.

Use this method when embedding documents that will be stored and later searched against. Some models optimize embeddings differently based on whether the input is a query or document.

Parameters:

Name Type Description Default `documents` `str | Sequence[str]`

A single document string or sequence of document strings to embed.

*required* `settings` `EmbeddingSettings | None`

Optional settings to override the embedder's default settings for this call.

`None`

Returns:

Type Description `EmbeddingResult`

An [`EmbeddingResult`](#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult            dataclass   ") containing the embeddings

`EmbeddingResult`

and metadata about the operation.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
```

```
async defembed_documents(
    self, documents: str | Sequence[str], *, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
"""Embed one or more document texts.

    Use this method when embedding documents that will be stored and later searched against.
    Some models optimize embeddings differently based on whether the input is a query or document.

    Args:
        documents: A single document string or sequence of document strings to embed.
        settings: Optional settings to override the embedder's default settings for this call.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
        and metadata about the operation.
    """
    return await self.embed(documents, input_type='document', settings=settings)
```

#### embed `async`

Embed text inputs with explicit input type specification.

This is the low-level embedding method. For most use cases, prefer [`embed_query()`](#pydantic_ai.embeddings.Embedder.embed_query "embed_query            async   ") or [`embed_documents()`](#pydantic_ai.embeddings.Embedder.embed_documents "embed_documents            async   ").

Parameters:

Name Type Description Default `inputs` `str | Sequence[str]`

A single string or sequence of strings to embed.

*required* `input_type` `EmbedInputType`

The type of input, either `'query'` or `'document'`.

*required* `settings` `EmbeddingSettings | None`

Optional settings to override the embedder's default settings for this call.

`None`

Returns:

Type Description `EmbeddingResult`

An [`EmbeddingResult`](#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult            dataclass   ") containing the embeddings

`EmbeddingResult`

and metadata about the operation.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
```

```
async defembed(
    self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
"""Embed text inputs with explicit input type specification.

    This is the low-level embedding method. For most use cases, prefer
    [`embed_query()`][pydantic_ai.embeddings.Embedder.embed_query] or
    [`embed_documents()`][pydantic_ai.embeddings.Embedder.embed_documents].

    Args:
        inputs: A single string or sequence of strings to embed.
        input_type: The type of input, either `'query'` or `'document'`.
        settings: Optional settings to override the embedder's default settings for this call.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing the embeddings
        and metadata about the operation.
    """
    model = self._get_model()
    settings = merge_embedding_settings(self._settings, settings)
    return await model.embed(inputs, input_type=input_type, settings=settings)
```

#### max\_input\_tokens `async`

```
max_input_tokens() -> int | None
```

Get the maximum number of tokens the model can accept as input.

Returns:

Type Description `int | None`

The maximum token count, or `None` if the limit is unknown for this model.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
307
308
309
310
311
312
313
314
```

```
async defmax_input_tokens(self) -> int | None:
"""Get the maximum number of tokens the model can accept as input.

    Returns:
        The maximum token count, or `None` if the limit is unknown for this model.
    """
    model = self._get_model()
    return await model.max_input_tokens()
```

#### count\_tokens `async`

```
count_tokens(text: str) -> int
```

Count the number of tokens in the given text.

Parameters:

Name Type Description Default `text` `str`

The text to tokenize and count.

*required*

Returns:

Type Description `int`

The number of tokens in the text.

Raises:

Type Description `NotImplementedError`

If the model doesn't support token counting.

`UserError`

If the model or tokenizer is not supported.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
```

```
async defcount_tokens(self, text: str) -> int:
"""Count the number of tokens in the given text.

    Args:
        text: The text to tokenize and count.

    Returns:
        The number of tokens in the text.

    Raises:
        NotImplementedError: If the model doesn't support token counting.
        UserError: If the model or tokenizer is not supported.
    """
    model = self._get_model()
    return await model.count_tokens(text)
```

#### embed\_query\_sync

Synchronous version of [`embed_query()`](#pydantic_ai.embeddings.Embedder.embed_query "embed_query            async   ").

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
defembed_query_sync(
    self, query: str | Sequence[str], *, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
"""Synchronous version of [`embed_query()`][pydantic_ai.embeddings.Embedder.embed_query]."""
    return _utils.get_event_loop().run_until_complete(self.embed_query(query, settings=settings))
```

#### embed\_documents\_sync

```
embed_documents_sync(
    documents: str | Sequence[str],
    *,
    settings: EmbeddingSettings | None = None
) -> EmbeddingResult
```

Synchronous version of [`embed_documents()`](#pydantic_ai.embeddings.Embedder.embed_documents "embed_documents            async   ").

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
defembed_documents_sync(
    self, documents: str | Sequence[str], *, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
"""Synchronous version of [`embed_documents()`][pydantic_ai.embeddings.Embedder.embed_documents]."""
    return _utils.get_event_loop().run_until_complete(self.embed_documents(documents, settings=settings))
```

#### embed\_sync

Synchronous version of [`embed()`](#pydantic_ai.embeddings.Embedder.embed "embed            async   ").

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
defembed_sync(
    self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
"""Synchronous version of [`embed()`][pydantic_ai.embeddings.Embedder.embed]."""
    return _utils.get_event_loop().run_until_complete(self.embed(inputs, input_type=input_type, settings=settings))
```

#### max\_input\_tokens\_sync

```
max_input_tokens_sync() -> int | None
```

Synchronous version of [`max_input_tokens()`](#pydantic_ai.embeddings.Embedder.max_input_tokens "max_input_tokens            async   ").

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
defmax_input_tokens_sync(self) -> int | None:
"""Synchronous version of [`max_input_tokens()`][pydantic_ai.embeddings.Embedder.max_input_tokens]."""
    return _utils.get_event_loop().run_until_complete(self.max_input_tokens())
```

#### count\_tokens\_sync

```
count_tokens_sync(text: str) -> int
```

Synchronous version of [`count_tokens()`](#pydantic_ai.embeddings.Embedder.count_tokens "count_tokens            async   ").

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/__init__.py`

```
defcount_tokens_sync(self, text: str) -> int:
"""Synchronous version of [`count_tokens()`][pydantic_ai.embeddings.Embedder.count_tokens]."""
    return _utils.get_event_loop().run_until_complete(self.count_tokens(text))
```

### EmbeddingModel

Bases: `ABC`

Abstract base class for embedding models.

Implement this class to create a custom embedding model. For most use cases, use one of the built-in implementations:

- [`OpenAIEmbeddingModel`](#pydantic_ai.embeddings.openai.OpenAIEmbeddingModel "OpenAIEmbeddingModel            dataclass   ")
- [`CohereEmbeddingModel`](#pydantic_ai.embeddings.cohere.CohereEmbeddingModel "CohereEmbeddingModel            dataclass   ")
- [`GoogleEmbeddingModel`](#pydantic_ai.embeddings.google.GoogleEmbeddingModel "GoogleEmbeddingModel            dataclass   ")
- [`SentenceTransformerEmbeddingModel`](#pydantic_ai.embeddings.sentence_transformers.SentenceTransformerEmbeddingModel "SentenceTransformerEmbeddingModel            dataclass   ")

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
  8
  9
 10
 11
 12
 13
 14
 15
 16
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
```

```
classEmbeddingModel(ABC):
"""Abstract base class for embedding models.

    Implement this class to create a custom embedding model. For most use cases,
    use one of the built-in implementations:

    - [`OpenAIEmbeddingModel`][pydantic_ai.embeddings.openai.OpenAIEmbeddingModel]
    - [`CohereEmbeddingModel`][pydantic_ai.embeddings.cohere.CohereEmbeddingModel]
    - [`GoogleEmbeddingModel`][pydantic_ai.embeddings.google.GoogleEmbeddingModel]
    - [`SentenceTransformerEmbeddingModel`][pydantic_ai.embeddings.sentence_transformers.SentenceTransformerEmbeddingModel]
    """

    _settings: EmbeddingSettings | None = None

    def__init__(
        self,
        *,
        settings: EmbeddingSettings | None = None,
    ) -> None:
"""Initialize the model with optional settings.

        Args:
            settings: Model-specific settings that will be used as defaults for this model.
        """
        self._settings = settings

    @property
    defsettings(self) -> EmbeddingSettings | None:
"""Get the default settings for this model."""
        return self._settings

    @property
    defbase_url(self) -> str | None:
"""The base URL for the provider API, if available."""
        return None

    @property
    @abstractmethod
    defmodel_name(self) -> str:
"""The name of the embedding model."""
        raise NotImplementedError()

    @property
    @abstractmethod
    defsystem(self) -> str:
"""The embedding model provider/system identifier (e.g., 'openai', 'cohere')."""
        raise NotImplementedError()

    @abstractmethod
    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
"""Generate embeddings for the given inputs.

        Args:
            inputs: A single string or sequence of strings to embed.
            input_type: Whether the inputs are queries or documents.
            settings: Optional settings to override the model's defaults.

        Returns:
            An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing
            the embeddings and metadata.
        """
        raise NotImplementedError

    defprepare_embed(
        self, inputs: str | Sequence[str], settings: EmbeddingSettings | None = None
    ) -> tuple[list[str], EmbeddingSettings]:
"""Prepare the inputs and settings for embedding.

        This method normalizes inputs to a list and merges settings.
        Subclasses should call this at the start of their `embed()` implementation.

        Args:
            inputs: A single string or sequence of strings.
            settings: Optional settings to merge with defaults.

        Returns:
            A tuple of (normalized inputs list, merged settings).
        """
        inputs = [inputs] if isinstance(inputs, str) else list(inputs)

        settings = merge_embedding_settings(self._settings, settings) or {}

        return inputs, settings

    async defmax_input_tokens(self) -> int | None:
"""Get the maximum number of tokens that can be input to the model.

        Returns:
            The maximum token count, or `None` if unknown.
        """
        return None  # pragma: no cover

    async defcount_tokens(self, text: str) -> int:
"""Count the number of tokens in the given text.

        Args:
            text: The text to tokenize and count.

        Returns:
            The number of tokens.

        Raises:
            NotImplementedError: If the model doesn't support token counting.
            UserError: If the model or tokenizer is not supported.
        """
        raise NotImplementedError
```

#### \_\_init\__

```
__init__(
    *, settings: EmbeddingSettings | None = None
) -> None
```

Initialize the model with optional settings.

Parameters:

Name Type Description Default `settings` `EmbeddingSettings | None`

Model-specific settings that will be used as defaults for this model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
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
```

```
def__init__(
    self,
    *,
    settings: EmbeddingSettings | None = None,
) -> None:
"""Initialize the model with optional settings.

    Args:
        settings: Model-specific settings that will be used as defaults for this model.
    """
    self._settings = settings
```

#### settings `property`

```
settings: EmbeddingSettings | None
```

Get the default settings for this model.

#### base\_url `property`

The base URL for the provider API, if available.

#### model\_name `abstractmethod` `property`

The name of the embedding model.

#### system `abstractmethod` `property`

The embedding model provider/system identifier (e.g., 'openai', 'cohere').

#### embed `abstractmethod` `async`

Generate embeddings for the given inputs.

Parameters:

Name Type Description Default `inputs` `str | Sequence[str]`

A single string or sequence of strings to embed.

*required* `input_type` `EmbedInputType`

Whether the inputs are queries or documents.

*required* `settings` `EmbeddingSettings | None`

Optional settings to override the model's defaults.

`None`

Returns:

Type Description `EmbeddingResult`

An [`EmbeddingResult`](#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult            dataclass   ") containing

`EmbeddingResult`

the embeddings and metadata.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
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
```

```
@abstractmethod
async defembed(
    self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
) -> EmbeddingResult:
"""Generate embeddings for the given inputs.

    Args:
        inputs: A single string or sequence of strings to embed.
        input_type: Whether the inputs are queries or documents.
        settings: Optional settings to override the model's defaults.

    Returns:
        An [`EmbeddingResult`][pydantic_ai.embeddings.EmbeddingResult] containing
        the embeddings and metadata.
    """
    raise NotImplementedError
```

#### prepare\_embed

Prepare the inputs and settings for embedding.

This method normalizes inputs to a list and merges settings. Subclasses should call this at the start of their `embed()` implementation.

Parameters:

Name Type Description Default `inputs` `str | Sequence[str]`

A single string or sequence of strings.

*required* `settings` `EmbeddingSettings | None`

Optional settings to merge with defaults.

`None`

Returns:

Type Description `tuple[list[str], EmbeddingSettings]`

A tuple of (normalized inputs list, merged settings).

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
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
```

```
defprepare_embed(
    self, inputs: str | Sequence[str], settings: EmbeddingSettings | None = None
) -> tuple[list[str], EmbeddingSettings]:
"""Prepare the inputs and settings for embedding.

    This method normalizes inputs to a list and merges settings.
    Subclasses should call this at the start of their `embed()` implementation.

    Args:
        inputs: A single string or sequence of strings.
        settings: Optional settings to merge with defaults.

    Returns:
        A tuple of (normalized inputs list, merged settings).
    """
    inputs = [inputs] if isinstance(inputs, str) else list(inputs)

    settings = merge_embedding_settings(self._settings, settings) or {}

    return inputs, settings
```

#### max\_input\_tokens `async`

```
max_input_tokens() -> int | None
```

Get the maximum number of tokens that can be input to the model.

Returns:

Type Description `int | None`

The maximum token count, or `None` if unknown.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
async defmax_input_tokens(self) -> int | None:
"""Get the maximum number of tokens that can be input to the model.

    Returns:
        The maximum token count, or `None` if unknown.
    """
    return None  # pragma: no cover
```

#### count\_tokens `async`

```
count_tokens(text: str) -> int
```

Count the number of tokens in the given text.

Parameters:

Name Type Description Default `text` `str`

The text to tokenize and count.

*required*

Returns:

Type Description `int`

The number of tokens.

Raises:

Type Description `NotImplementedError`

If the model doesn't support token counting.

`UserError`

If the model or tokenizer is not supported.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/base.py`

```
102
103
104
105
106
107
108
109
110
111
112
113
114
115
```

```
async defcount_tokens(self, text: str) -> int:
"""Count the number of tokens in the given text.

    Args:
        text: The text to tokenize and count.

    Returns:
        The number of tokens.

    Raises:
        NotImplementedError: If the model doesn't support token counting.
        UserError: If the model or tokenizer is not supported.
    """
    raise NotImplementedError
```

### EmbedInputType `module-attribute`

```
EmbedInputType = Literal['query', 'document']
```

The type of input to the embedding model.

- `'query'`: Text that will be used as a search query
- `'document'`: Text that will be stored and searched against

Some embedding models optimize differently for queries vs documents.

### EmbeddingResult `dataclass`

The result of an embedding operation.

This class contains the generated embeddings along with metadata about the operation, including the original inputs, model information, usage statistics, and timing.

Example:

```
frompydantic_aiimport Embedder

embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    result = await embedder.embed_query('What is AI?')

    # Access embeddings by index
    print(len(result.embeddings[0]))
    #> 1536

    # Access embeddings by original input text
    print(result['What is AI?'] == result.embeddings[0])
    #> True

    # Check usage
    print(f'Tokens used: {result.usage.input_tokens}')
    #> Tokens used: 3
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
```

````
@dataclass
classEmbeddingResult:
"""The result of an embedding operation.

    This class contains the generated embeddings along with metadata about
    the operation, including the original inputs, model information, usage
    statistics, and timing.

    Example:
    ```python
    from pydantic_ai import Embedder

    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        result = await embedder.embed_query('What is AI?')

        # Access embeddings by index
        print(len(result.embeddings[0]))
        #> 1536

        # Access embeddings by original input text
        print(result['What is AI?'] == result.embeddings[0])
        #> True

        # Check usage
        print(f'Tokens used: {result.usage.input_tokens}')
        #> Tokens used: 3
    ```
    """

    embeddings: Sequence[Sequence[float]]
"""The computed embedding vectors, one per input text.

    Each embedding is a sequence of floats representing the text in vector space.
    """

    _: KW_ONLY

    inputs: Sequence[str]
"""The original input texts that were embedded."""

    input_type: EmbedInputType
"""Whether the inputs were embedded as queries or documents."""

    model_name: str
"""The name of the model that generated these embeddings."""

    provider_name: str
"""The name of the provider (e.g., 'openai', 'cohere')."""

    timestamp: datetime = field(default_factory=_now_utc)
"""When the embedding request was made."""

    usage: RequestUsage = field(default_factory=RequestUsage)
"""Token usage statistics for this request."""

    provider_details: dict[str, Any] | None = None
"""Provider-specific details from the response."""

    provider_response_id: str | None = None
"""Unique identifier for this response from the provider, if available."""

    def__getitem__(self, item: int | str) -> Sequence[float]:
"""Get the embedding for an input by index or by the original input text.

        Args:
            item: Either an integer index or the original input string.

        Returns:
            The embedding vector for the specified input.

        Raises:
            IndexError: If the index is out of range.
            ValueError: If the string is not found in the inputs.
        """
        if isinstance(item, str):
            item = self.inputs.index(item)

        return self.embeddings[item]

    defcost(self) -> genai_types.PriceCalculation:
"""Calculate the cost of the embedding request.

        Uses [`genai-prices`](https://github.com/pydantic/genai-prices) for pricing data.

        Returns:
            A price calculation object with `total_price`, `input_price`, and other cost details.

        Raises:
            LookupError: If pricing data is not available for this model/provider.
        """
        assert self.model_name, 'Model name is required to calculate price'
        return calc_price(
            self.usage,
            self.model_name,
            provider_id=self.provider_name,
            genai_request_timestamp=self.timestamp,
        )
````

#### embeddings `instance-attribute`

The computed embedding vectors, one per input text.

Each embedding is a sequence of floats representing the text in vector space.

#### inputs `instance-attribute`

The original input texts that were embedded.

#### input\_type `instance-attribute`

```
input_type: EmbedInputType
```

Whether the inputs were embedded as queries or documents.

#### model\_name `instance-attribute`

The name of the model that generated these embeddings.

#### provider\_name `instance-attribute`

The name of the provider (e.g., 'openai', 'cohere').

#### timestamp `class-attribute` `instance-attribute`

When the embedding request was made.

#### usage `class-attribute` `instance-attribute`

Token usage statistics for this request.

#### provider\_details `class-attribute` `instance-attribute`

Provider-specific details from the response.

#### provider\_response\_id `class-attribute` `instance-attribute`

```
provider_response_id: str | None = None
```

Unique identifier for this response from the provider, if available.

#### \_\_getitem\__

Get the embedding for an input by index or by the original input text.

Parameters:

Name Type Description Default `item` `int | str`

Either an integer index or the original input string.

*required*

Returns:

Type Description `Sequence[float]`

The embedding vector for the specified input.

Raises:

Type Description `IndexError`

If the index is out of range.

`ValueError`

If the string is not found in the inputs.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`

```
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
100
101
```

```
def__getitem__(self, item: int | str) -> Sequence[float]:
"""Get the embedding for an input by index or by the original input text.

    Args:
        item: Either an integer index or the original input string.

    Returns:
        The embedding vector for the specified input.

    Raises:
        IndexError: If the index is out of range.
        ValueError: If the string is not found in the inputs.
    """
    if isinstance(item, str):
        item = self.inputs.index(item)

    return self.embeddings[item]
```

#### cost

```
cost() -> PriceCalculation
```

Calculate the cost of the embedding request.

Uses [`genai-prices`](https://github.com/pydantic/genai-prices) for pricing data.

Returns:

Type Description `PriceCalculation`

A price calculation object with `total_price`, `input_price`, and other cost details.

Raises:

Type Description `LookupError`

If pricing data is not available for this model/provider.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/result.py`

```
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
```

```
defcost(self) -> genai_types.PriceCalculation:
"""Calculate the cost of the embedding request.

    Uses [`genai-prices`](https://github.com/pydantic/genai-prices) for pricing data.

    Returns:
        A price calculation object with `total_price`, `input_price`, and other cost details.

    Raises:
        LookupError: If pricing data is not available for this model/provider.
    """
    assert self.model_name, 'Model name is required to calculate price'
    return calc_price(
        self.usage,
        self.model_name,
        provider_id=self.provider_name,
        genai_request_timestamp=self.timestamp,
    )
```

### EmbeddingSettings

Bases: `TypedDict`

Common settings for configuring embedding models.

These settings apply across multiple embedding model providers. Not all settings are supported by all models - check the specific model's documentation for details.

Provider-specific settings classes (e.g., [`OpenAIEmbeddingSettings`](#pydantic_ai.embeddings.openai.OpenAIEmbeddingSettings "OpenAIEmbeddingSettings"), [`CohereEmbeddingSettings`](#pydantic_ai.embeddings.cohere.CohereEmbeddingSettings "CohereEmbeddingSettings")) extend this with additional provider-prefixed options.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/settings.py`

```
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
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
```

```
classEmbeddingSettings(TypedDict, total=False):
"""Common settings for configuring embedding models.

    These settings apply across multiple embedding model providers.
    Not all settings are supported by all models - check the specific
    model's documentation for details.

    Provider-specific settings classes (e.g.,
    [`OpenAIEmbeddingSettings`][pydantic_ai.embeddings.openai.OpenAIEmbeddingSettings],
    [`CohereEmbeddingSettings`][pydantic_ai.embeddings.cohere.CohereEmbeddingSettings])
    extend this with additional provider-prefixed options.
    """

    dimensions: int
"""The number of dimensions for the output embeddings.

    Supported by:

    * OpenAI
    * Cohere
    * Google
    * Sentence Transformers
    * VoyageAI
    """

    truncate: bool
"""Whether to truncate inputs that exceed the model's context length.

    Defaults to `False`. If `True`, inputs that are too long will be truncated.
    If `False`, an error will be raised for inputs that exceed the context length.

    For more control over truncation, you can use
    [`max_input_tokens()`][pydantic_ai.embeddings.Embedder.max_input_tokens] and
    [`count_tokens()`][pydantic_ai.embeddings.Embedder.count_tokens] to implement
    your own truncation logic.

    Provider-specific truncation settings (e.g., `cohere_truncate`) take precedence
    if specified.

    Supported by:

    * Cohere
    * VoyageAI
    """

    extra_headers: dict[str, str]
"""Extra headers to send to the model.

    Supported by:

    * OpenAI
    * Cohere
    """

    extra_body: object
"""Extra body to send to the model.

    Supported by:

    * OpenAI
    * Cohere
    """
```

#### dimensions `instance-attribute`

The number of dimensions for the output embeddings.

Supported by:

- OpenAI
- Cohere
- Google
- Sentence Transformers
- VoyageAI

#### truncate `instance-attribute`

Whether to truncate inputs that exceed the model's context length.

Defaults to `False`. If `True`, inputs that are too long will be truncated. If `False`, an error will be raised for inputs that exceed the context length.

For more control over truncation, you can use [`max_input_tokens()`](#pydantic_ai.embeddings.Embedder.max_input_tokens "max_input_tokens            async   ") and [`count_tokens()`](#pydantic_ai.embeddings.Embedder.count_tokens "count_tokens            async   ") to implement your own truncation logic.

Provider-specific truncation settings (e.g., `cohere_truncate`) take precedence if specified.

Supported by:

- Cohere
- VoyageAI

Extra headers to send to the model.

Supported by:

- OpenAI
- Cohere

#### extra\_body `instance-attribute`

Extra body to send to the model.

Supported by:

- OpenAI
- Cohere

### merge\_embedding\_settings

```
merge_embedding_settings(
    base: EmbeddingSettings | None,
    overrides: EmbeddingSettings | None,
) -> EmbeddingSettings | None
```

Merge two sets of embedding settings, with overrides taking precedence.

Parameters:

Name Type Description Default `base` `EmbeddingSettings | None`

Base settings (typically from the embedder or model).

*required* `overrides` `EmbeddingSettings | None`

Settings that should override the base (typically per-call settings).

*required*

Returns:

Type Description `EmbeddingSettings | None`

Merged settings, or `None` if both inputs are `None`.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/settings.py`

```
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
```

```
defmerge_embedding_settings(
    base: EmbeddingSettings | None, overrides: EmbeddingSettings | None
) -> EmbeddingSettings | None:
"""Merge two sets of embedding settings, with overrides taking precedence.

    Args:
        base: Base settings (typically from the embedder or model).
        overrides: Settings that should override the base (typically per-call settings).

    Returns:
        Merged settings, or `None` if both inputs are `None`.
    """
    # Note: we may want merge recursively if/when we add non-primitive values
    if base and overrides:
        return base | overrides
    else:
        return base or overrides
```

### OpenAIEmbeddingModelName `module-attribute`

```
OpenAIEmbeddingModelName = str | EmbeddingModel
```

Possible OpenAI embeddings model names.

See the [OpenAI embeddings documentation](https://platform.openai.com/docs/guides/embeddings) for available models.

### OpenAIEmbeddingSettings

Bases: `EmbeddingSettings`

Settings used for an OpenAI embedding model request.

All fields from [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/openai.py`

```
classOpenAIEmbeddingSettings(EmbeddingSettings, total=False):
"""Settings used for an OpenAI embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported.
    """
```

### OpenAIEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

OpenAI embedding model implementation.

This model works with OpenAI's embeddings API and any [OpenAI-compatible providers](https://ai.pydantic.dev/models/openai/#openai-compatible-models).

Example:

```
frompydantic_ai.embeddings.openaiimport OpenAIEmbeddingModel
frompydantic_ai.providers.openaiimport OpenAIProvider

# Using OpenAI directly
model = OpenAIEmbeddingModel('text-embedding-3-small')

# Using an OpenAI-compatible provider
model = OpenAIEmbeddingModel(
    'text-embedding-3-small',
    provider=OpenAIProvider(base_url='https://my-provider.com/v1'),
)
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/openai.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
```

````
@dataclass(init=False)
classOpenAIEmbeddingModel(EmbeddingModel):
"""OpenAI embedding model implementation.

    This model works with OpenAI's embeddings API and any
    [OpenAI-compatible providers](../models/openai.md#openai-compatible-models).

    Example:
    ```python
    from pydantic_ai.embeddings.openai import OpenAIEmbeddingModel
    from pydantic_ai.providers.openai import OpenAIProvider

    # Using OpenAI directly
    model = OpenAIEmbeddingModel('text-embedding-3-small')

    # Using an OpenAI-compatible provider
    model = OpenAIEmbeddingModel(
        'text-embedding-3-small',
        provider=OpenAIProvider(base_url='https://my-provider.com/v1'),
    )
    ```
    """

    _model_name: OpenAIEmbeddingModelName = field(repr=False)
    _provider: Provider[AsyncOpenAI] = field(repr=False)

    def__init__(
        self,
        model_name: OpenAIEmbeddingModelName,
        *,
        provider: OpenAIEmbeddingsCompatibleProvider | Literal['openai'] | Provider[AsyncOpenAI] = 'openai',
        settings: EmbeddingSettings | None = None,
    ):
"""Initialize an OpenAI embedding model.

        Args:
            model_name: The name of the OpenAI model to use.
                See [OpenAI's embedding models](https://platform.openai.com/docs/guides/embeddings)
                for available options.
            provider: The provider to use for authentication and API access. Can be:

                - `'openai'` (default): Uses the standard OpenAI API
                - A provider name string (e.g., `'azure'`, `'deepseek'`)
                - A [`Provider`][pydantic_ai.providers.Provider] instance for custom configuration

                See [OpenAI-compatible providers](../models/openai.md#openai-compatible-models)
                for a list of supported providers.
            settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self._client = provider.client

        super().__init__(settings=settings)

    @property
    defbase_url(self) -> str:
        return str(self._client.base_url)

    @property
    defmodel_name(self) -> OpenAIEmbeddingModelName:
"""The embedding model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The embedding model provider."""
        return self._provider.name

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        settings = cast(OpenAIEmbeddingSettings, settings)

        try:
            response = await self._client.embeddings.create(
                input=inputs,
                model=self.model_name,
                dimensions=settings.get('dimensions') or OMIT,
                extra_headers=settings.get('extra_headers'),
                extra_body=settings.get('extra_body'),
            )
        except APIStatusError as e:
            if (status_code := e.status_code) >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) frome
            raise  # pragma: lax no cover
        except APIConnectionError as e:  # pragma: no cover
            raise ModelAPIError(model_name=self.model_name, message=e.message) frome

        embeddings = [item.embedding for item in response.data]

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=_map_usage(response.usage, self.system, self.base_url, response.model),
            model_name=response.model,
            provider_name=self.system,
        )

    async defmax_input_tokens(self) -> int | None:
        if self.system != 'openai':
            return None

        # https://platform.openai.com/docs/guides/embeddings#embedding-models
        return 8192

    async defcount_tokens(self, text: str) -> int:
        if self.system != 'openai':
            raise UserError(
                'Counting tokens is not supported for non-OpenAI embedding models',
            )
        try:
            encoding = await _utils.run_in_executor(tiktoken.encoding_for_model, self.model_name)
        except KeyError as e:  # pragma: no cover
            raise ValueError(
                f'The embedding model {self.model_name!r} is not supported by tiktoken',
            ) frome
        return len(encoding.encode(text))
````

#### \_\_init\__

```
__init__(
    model_name: OpenAIEmbeddingModelName,
    *,
    provider: (
        OpenAIEmbeddingsCompatibleProvider
        | Literal["openai"]
        | Provider[AsyncOpenAI]
    ) = "openai",
    settings: EmbeddingSettings | None = None
)
```

Initialize an OpenAI embedding model.

Parameters:

Name Type Description Default `model_name` `OpenAIEmbeddingModelName`

The name of the OpenAI model to use. See [OpenAI's embedding models](https://platform.openai.com/docs/guides/embeddings) for available options.

*required* `provider` `OpenAIEmbeddingsCompatibleProvider | Literal['openai'] | Provider[AsyncOpenAI]`

The provider to use for authentication and API access. Can be:

- `'openai'` (default): Uses the standard OpenAI API
- A provider name string (e.g., `'azure'`, `'deepseek'`)
- A [`Provider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider) instance for custom configuration

See [OpenAI-compatible providers](https://ai.pydantic.dev/models/openai/#openai-compatible-models) for a list of supported providers.

`'openai'` `settings` `EmbeddingSettings | None`

Model-specific [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/openai.py`

```
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
100
101
102
```

```
def__init__(
    self,
    model_name: OpenAIEmbeddingModelName,
    *,
    provider: OpenAIEmbeddingsCompatibleProvider | Literal['openai'] | Provider[AsyncOpenAI] = 'openai',
    settings: EmbeddingSettings | None = None,
):
"""Initialize an OpenAI embedding model.

    Args:
        model_name: The name of the OpenAI model to use.
            See [OpenAI's embedding models](https://platform.openai.com/docs/guides/embeddings)
            for available options.
        provider: The provider to use for authentication and API access. Can be:

            - `'openai'` (default): Uses the standard OpenAI API
            - A provider name string (e.g., `'azure'`, `'deepseek'`)
            - A [`Provider`][pydantic_ai.providers.Provider] instance for custom configuration

            See [OpenAI-compatible providers](../models/openai.md#openai-compatible-models)
            for a list of supported providers.
        settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider
    self._client = provider.client

    super().__init__(settings=settings)
```

#### model\_name `property`

```
model_name: OpenAIEmbeddingModelName
```

The embedding model name.

#### system `property`

The embedding model provider.

### LatestCohereEmbeddingModelNames `module-attribute`

```
LatestCohereEmbeddingModelNames = Literal[
    "embed-v4.0",
    "embed-english-v3.0",
    "embed-english-light-v3.0",
    "embed-multilingual-v3.0",
    "embed-multilingual-light-v3.0",
]
```

Latest Cohere embeddings models.

See the [Cohere Embed documentation](https://docs.cohere.com/docs/cohere-embed) for available models and their capabilities.

### CohereEmbeddingModelName `module-attribute`

```
CohereEmbeddingModelName = (
    str | LatestCohereEmbeddingModelNames
)
```

Possible Cohere embeddings model names.

### CohereEmbeddingSettings

Bases: `EmbeddingSettings`

Settings used for a Cohere embedding model request.

All fields from [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus Cohere-specific settings prefixed with `cohere_`.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/cohere.py`

```
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
```

```
classCohereEmbeddingSettings(EmbeddingSettings, total=False):
"""Settings used for a Cohere embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus Cohere-specific settings prefixed with `cohere_`.
    """

    # ALL FIELDS MUST BE `cohere_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    cohere_max_tokens: int
"""The maximum number of tokens to embed."""

    cohere_input_type: CohereEmbedInputType
"""The Cohere-specific input type for the embedding.

    Overrides the standard `input_type` argument. Options include:
    `'search_query'`, `'search_document'`, `'classification'`, `'clustering'`, and `'image'`.
    """

    cohere_truncate: V2EmbedRequestTruncate
"""The truncation strategy to use:

    - `'NONE'` (default): Raise an error if input exceeds max tokens.
    - `'END'`: Truncate the end of the input text.
    - `'START'`: Truncate the start of the input text.

    Note: This setting overrides the standard `truncate` boolean setting when specified.
    """
```

#### cohere\_max\_tokens `instance-attribute`

The maximum number of tokens to embed.

#### cohere\_input\_type `instance-attribute`

```
cohere_input_type: EmbedInputType
```

The Cohere-specific input type for the embedding.

Overrides the standard `input_type` argument. Options include: `'search_query'`, `'search_document'`, `'classification'`, `'clustering'`, and `'image'`.

#### cohere\_truncate `instance-attribute`

```
cohere_truncate: V2EmbedRequestTruncate
```

The truncation strategy to use:

- `'NONE'` (default): Raise an error if input exceeds max tokens.
- `'END'`: Truncate the end of the input text.
- `'START'`: Truncate the start of the input text.

Note: This setting overrides the standard `truncate` boolean setting when specified.

### CohereEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

Cohere embedding model implementation.

This model works with Cohere's embeddings API, which offers multilingual support and various model sizes.

Example:

```
frompydantic_ai.embeddings.cohereimport CohereEmbeddingModel

model = CohereEmbeddingModel('embed-v4.0')
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/cohere.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
```

````
@dataclass(init=False)
classCohereEmbeddingModel(EmbeddingModel):
"""Cohere embedding model implementation.

    This model works with Cohere's embeddings API, which offers
    multilingual support and various model sizes.

    Example:
    ```python
    from pydantic_ai.embeddings.cohere import CohereEmbeddingModel

    model = CohereEmbeddingModel('embed-v4.0')
    ```
    """

    _model_name: CohereEmbeddingModelName = field(repr=False)
    _provider: Provider[AsyncClientV2] = field(repr=False)

    def__init__(
        self,
        model_name: CohereEmbeddingModelName,
        *,
        provider: Literal['cohere'] | Provider[AsyncClientV2] = 'cohere',
        settings: EmbeddingSettings | None = None,
    ):
"""Initialize a Cohere embedding model.

        Args:
            model_name: The name of the Cohere model to use.
                See [Cohere Embed documentation](https://docs.cohere.com/docs/cohere-embed)
                for available models.
            provider: The provider to use for authentication and API access. Can be:

                - `'cohere'` (default): Uses the standard Cohere API
                - A [`CohereProvider`][pydantic_ai.providers.cohere.CohereProvider] instance
                  for custom configuration
            settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self._client = provider.client
        self._v1_client = provider.v1_client if isinstance(provider, CohereProvider) else None

        super().__init__(settings=settings)

    @property
    defbase_url(self) -> str:
"""The base URL for the provider API, if available."""
        return self._provider.base_url

    @property
    defmodel_name(self) -> CohereEmbeddingModelName:
"""The embedding model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The embedding model provider."""
        return self._provider.name

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        settings = cast(CohereEmbeddingSettings, settings)

        cohere_input_type = settings.get(
            'cohere_input_type', 'search_document' if input_type == 'document' else 'search_query'
        )

        request_options: RequestOptions = {}
        if extra_headers := settings.get('extra_headers'):  # pragma: no cover
            request_options['additional_headers'] = extra_headers
        if extra_body := settings.get('extra_body'):  # pragma: no cover
            request_options['additional_body_parameters'] = cast(dict[str, Any], extra_body)

        # Determine truncation strategy: cohere_truncate takes precedence over truncate
        if 'cohere_truncate' in settings:
            truncate = settings['cohere_truncate']
        elif settings.get('truncate'):
            truncate = 'END'
        else:
            truncate = 'NONE'

        try:
            response = await self._client.embed(
                model=self.model_name,
                texts=inputs,
                output_dimension=settings.get('dimensions'),
                input_type=cohere_input_type,
                max_tokens=settings.get('cohere_max_tokens'),
                truncate=truncate,
                request_options=request_options,
            )
        except ApiError as e:
            if (status_code := e.status_code) and status_code >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) frome
            raise ModelAPIError(model_name=self.model_name, message=str(e)) frome  # pragma: no cover

        embeddings = response.embeddings.float_
        if embeddings is None:
            raise UnexpectedModelBehavior(  # pragma: no cover
                'The Cohere embeddings response did not have an `embeddings` field holding a list of floats',
                str(response),
            )

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=_map_usage(response, self.system, self.base_url, self.model_name),
            model_name=self.model_name,
            provider_name=self.system,
            provider_response_id=response.id,
        )

    async defmax_input_tokens(self) -> int | None:
        return _MAX_INPUT_TOKENS.get(self.model_name)

    async defcount_tokens(self, text: str) -> int:
        if self._v1_client is None:
            raise NotImplementedError('Counting tokens requires the Cohere v1 client')
        try:
            result = await self._v1_client.tokenize(
                model=self.model_name,
                text=text,  # Has a max length of 65536 characters
                offline=False,
            )
        except ApiError as e:  # pragma: no cover
            if (status_code := e.status_code) and status_code >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) frome
            raise ModelAPIError(model_name=self.model_name, message=str(e)) frome

        return len(result.tokens)
````

#### \_\_init\__

```
__init__(
    model_name: CohereEmbeddingModelName,
    *,
    provider: (
        Literal["cohere"] | Provider[AsyncClientV2]
    ) = "cohere",
    settings: EmbeddingSettings | None = None
)
```

Initialize a Cohere embedding model.

Parameters:

Name Type Description Default `model_name` `CohereEmbeddingModelName`

The name of the Cohere model to use. See [Cohere Embed documentation](https://docs.cohere.com/docs/cohere-embed) for available models.

*required* `provider` `Literal['cohere'] | Provider[AsyncClientV2]`

The provider to use for authentication and API access. Can be:

- `'cohere'` (default): Uses the standard Cohere API
- A [`CohereProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.cohere.CohereProvider "CohereProvider") instance for custom configuration

`'cohere'` `settings` `EmbeddingSettings | None`

Model-specific [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/cohere.py`

```
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
```

```
def__init__(
    self,
    model_name: CohereEmbeddingModelName,
    *,
    provider: Literal['cohere'] | Provider[AsyncClientV2] = 'cohere',
    settings: EmbeddingSettings | None = None,
):
"""Initialize a Cohere embedding model.

    Args:
        model_name: The name of the Cohere model to use.
            See [Cohere Embed documentation](https://docs.cohere.com/docs/cohere-embed)
            for available models.
        provider: The provider to use for authentication and API access. Can be:

            - `'cohere'` (default): Uses the standard Cohere API
            - A [`CohereProvider`][pydantic_ai.providers.cohere.CohereProvider] instance
              for custom configuration
        settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider
    self._client = provider.client
    self._v1_client = provider.v1_client if isinstance(provider, CohereProvider) else None

    super().__init__(settings=settings)
```

#### base\_url `property`

The base URL for the provider API, if available.

#### model\_name `property`

```
model_name: CohereEmbeddingModelName
```

The embedding model name.

#### system `property`

The embedding model provider.

### LatestGoogleGLAEmbeddingModelNames `module-attribute`

```
LatestGoogleGLAEmbeddingModelNames = Literal[
    "gemini-embedding-001"
]
```

Latest Google Gemini API (GLA) embedding models.

See the [Google Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings) for available models and their capabilities.

### LatestGoogleVertexEmbeddingModelNames `module-attribute`

```
LatestGoogleVertexEmbeddingModelNames = Literal[
    "gemini-embedding-001",
    "text-embedding-005",
    "text-multilingual-embedding-002",
]
```

Latest Google Vertex AI embedding models.

See the [Vertex AI Embeddings documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings) for available models and their capabilities.

### LatestGoogleEmbeddingModelNames `module-attribute`

```
LatestGoogleEmbeddingModelNames = (
    LatestGoogleGLAEmbeddingModelNames
    | LatestGoogleVertexEmbeddingModelNames
)
```

All latest Google embedding models (union of GLA and Vertex AI models).

### GoogleEmbeddingModelName `module-attribute`

```
GoogleEmbeddingModelName = (
    str | LatestGoogleEmbeddingModelNames
)
```

Possible Google embeddings model names.

### GoogleEmbeddingSettings

Bases: `EmbeddingSettings`

Settings used for a Google embedding model request.

All fields from [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus Google-specific settings prefixed with `google_`.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/google.py`

```
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
```

```
classGoogleEmbeddingSettings(EmbeddingSettings, total=False):
"""Settings used for a Google embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus Google-specific settings prefixed with `google_`.
    """

    # ALL FIELDS MUST BE `google_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    google_task_type: str
"""The task type for the embedding.

    Overrides the automatic task type selection based on `input_type`.
    See [Google's task type documentation](https://ai.google.dev/gemini-api/docs/embeddings#task-types)
    for available options.
    """

    google_title: str
"""Optional title for the content being embedded.

    Only applicable when task_type is `RETRIEVAL_DOCUMENT`.
    """
```

#### google\_task\_type `instance-attribute`

The task type for the embedding.

Overrides the automatic task type selection based on `input_type`. See [Google's task type documentation](https://ai.google.dev/gemini-api/docs/embeddings#task-types) for available options.

#### google\_title `instance-attribute`

Optional title for the content being embedded.

Only applicable when task\_type is `RETRIEVAL_DOCUMENT`.

### GoogleEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

Google embedding model implementation.

This model works with Google's embeddings API via the `google-genai` SDK, supporting both the Gemini API (Google AI Studio) and Vertex AI.

Example:

```
frompydantic_ai.embeddings.googleimport GoogleEmbeddingModel
frompydantic_ai.providers.googleimport GoogleProvider

# Using Gemini API (requires GOOGLE_API_KEY env var)
model = GoogleEmbeddingModel('gemini-embedding-001')

# Using Vertex AI
model = GoogleEmbeddingModel(
    'gemini-embedding-001',
    provider=GoogleProvider(vertexai=True, project='my-project', location='us-central1'),
)
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/google.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
```

````
@dataclass(init=False)
classGoogleEmbeddingModel(EmbeddingModel):
"""Google embedding model implementation.

    This model works with Google's embeddings API via the `google-genai` SDK,
    supporting both the Gemini API (Google AI Studio) and Vertex AI.

    Example:
    ```python
    from pydantic_ai.embeddings.google import GoogleEmbeddingModel
    from pydantic_ai.providers.google import GoogleProvider

    # Using Gemini API (requires GOOGLE_API_KEY env var)
    model = GoogleEmbeddingModel('gemini-embedding-001')

    # Using Vertex AI
    model = GoogleEmbeddingModel(
        'gemini-embedding-001',
        provider=GoogleProvider(vertexai=True, project='my-project', location='us-central1'),
    )
    ```
    """

    _model_name: GoogleEmbeddingModelName = field(repr=False)
    _provider: Provider[Client] = field(repr=False)

    def__init__(
        self,
        model_name: GoogleEmbeddingModelName,
        *,
        provider: Literal['google-gla', 'google-vertex'] | Provider[Client] = 'google-gla',
        settings: EmbeddingSettings | None = None,
    ):
"""Initialize a Google embedding model.

        Args:
            model_name: The name of the Google model to use.
                See [Google Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
                for available models.
            provider: The provider to use for authentication and API access. Can be:

                - `'google-gla'` (default): Uses the Gemini API (Google AI Studio)
                - `'google-vertex'`: Uses Vertex AI
                - A [`GoogleProvider`][pydantic_ai.providers.google.GoogleProvider] instance
                  for custom configuration
            settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self._client = provider.client

        super().__init__(settings=settings)

    @property
    defbase_url(self) -> str:
        return self._provider.base_url

    @property
    defmodel_name(self) -> GoogleEmbeddingModelName:
"""The embedding model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The embedding model provider."""
        return self._provider.name

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        settings = cast(GoogleEmbeddingSettings, settings)

        google_task_type = settings.get('google_task_type')
        if google_task_type is None:
            google_task_type = 'RETRIEVAL_DOCUMENT' if input_type == 'document' else 'RETRIEVAL_QUERY'

        config = EmbedContentConfig(
            task_type=google_task_type,
            output_dimensionality=settings.get('dimensions'),
            title=settings.get('google_title'),
        )

        try:
            response = await self._client.aio.models.embed_content(
                model=self._model_name,
                contents=cast(ContentListUnion, inputs),
                config=config,
            )
        except errors.APIError as e:
            if (status_code := e.code) >= 400:
                raise ModelHTTPError(
                    status_code=status_code,
                    model_name=self._model_name,
                    body=cast(object, e.details),  # pyright: ignore[reportUnknownMemberType]
                ) frome
            raise  # pragma: no cover

        embeddings: list[list[float]] = [emb.values for emb in (response.embeddings or []) if emb.values is not None]

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=_map_usage(response, self.system, self.base_url, self._model_name),
            model_name=self._model_name,
            provider_name=self.system,
        )

    async defmax_input_tokens(self) -> int | None:
        return _MAX_INPUT_TOKENS.get(self._model_name)

    async defcount_tokens(self, text: str) -> int:
        try:
            response = await self._client.aio.models.count_tokens(
                model=self._model_name,
                contents=text,
            )
        except errors.APIError as e:
            if (status_code := e.code) >= 400:
                raise ModelHTTPError(
                    status_code=status_code,
                    model_name=self._model_name,
                    body=cast(object, e.details),  # pyright: ignore[reportUnknownMemberType]
                ) frome
            raise  # pragma: no cover

        if response.total_tokens is None:
            raise UnexpectedModelBehavior('Token counting returned no result')  # pragma: no cover
        return response.total_tokens
````

#### \_\_init\__

```
__init__(
    model_name: GoogleEmbeddingModelName,
    *,
    provider: (
        Literal["google-gla", "google-vertex"]
        | Provider[Client]
    ) = "google-gla",
    settings: EmbeddingSettings | None = None
)
```

Initialize a Google embedding model.

Parameters:

Name Type Description Default `model_name` `GoogleEmbeddingModelName`

The name of the Google model to use. See [Google Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings) for available models.

*required* `provider` `Literal['google-gla', 'google-vertex'] | Provider[Client]`

The provider to use for authentication and API access. Can be:

- `'google-gla'` (default): Uses the Gemini API (Google AI Studio)
- `'google-vertex'`: Uses Vertex AI
- A [`GoogleProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.google.GoogleProvider "GoogleProvider") instance for custom configuration

`'google-gla'` `settings` `EmbeddingSettings | None`

Model-specific [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/google.py`

```
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
```

```
def__init__(
    self,
    model_name: GoogleEmbeddingModelName,
    *,
    provider: Literal['google-gla', 'google-vertex'] | Provider[Client] = 'google-gla',
    settings: EmbeddingSettings | None = None,
):
"""Initialize a Google embedding model.

    Args:
        model_name: The name of the Google model to use.
            See [Google Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
            for available models.
        provider: The provider to use for authentication and API access. Can be:

            - `'google-gla'` (default): Uses the Gemini API (Google AI Studio)
            - `'google-vertex'`: Uses Vertex AI
            - A [`GoogleProvider`][pydantic_ai.providers.google.GoogleProvider] instance
              for custom configuration
        settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider
    self._client = provider.client

    super().__init__(settings=settings)
```

#### model\_name `property`

```
model_name: GoogleEmbeddingModelName
```

The embedding model name.

#### system `property`

The embedding model provider.

### LatestVoyageAIEmbeddingModelNames `module-attribute`

```
LatestVoyageAIEmbeddingModelNames = Literal[
    "voyage-4-large",
    "voyage-4",
    "voyage-4-lite",
    "voyage-3-large",
    "voyage-3.5",
    "voyage-3.5-lite",
    "voyage-code-3",
    "voyage-finance-2",
    "voyage-law-2",
    "voyage-code-2",
]
```

Latest VoyageAI embedding models.

See [VoyageAI Embeddings](https://docs.voyageai.com/docs/embeddings) for available models and their capabilities.

### VoyageAIEmbeddingModelName `module-attribute`

```
VoyageAIEmbeddingModelName = (
    str | LatestVoyageAIEmbeddingModelNames
)
```

Possible VoyageAI embedding model names.

### VoyageAIEmbedInputType `module-attribute`

```
VoyageAIEmbedInputType = Literal[
    "query", "document", "none"
]
```

VoyageAI embedding input types.

- `'query'`: For search queries; prepends retrieval-optimized prefix.
- `'document'`: For documents; prepends document retrieval prefix.
- `'none'`: Direct embedding without any prefix.

### VoyageAIEmbeddingSettings

Bases: `EmbeddingSettings`

Settings used for a VoyageAI embedding model request.

All fields from [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus VoyageAI-specific settings prefixed with `voyageai_`.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/voyageai.py`

```
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
```

```
classVoyageAIEmbeddingSettings(EmbeddingSettings, total=False):
"""Settings used for a VoyageAI embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus VoyageAI-specific settings prefixed with `voyageai_`.
    """

    # ALL FIELDS MUST BE `voyageai_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    voyageai_input_type: VoyageAIEmbedInputType
"""The VoyageAI-specific input type for the embedding.

    Overrides the standard `input_type` argument. Options include:
    `'query'`, `'document'`, or `'none'` for direct embedding without prefix.
    """
```

#### voyageai\_input\_type `instance-attribute`

```
voyageai_input_type: VoyageAIEmbedInputType
```

The VoyageAI-specific input type for the embedding.

Overrides the standard `input_type` argument. Options include: `'query'`, `'document'`, or `'none'` for direct embedding without prefix.

### VoyageAIEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

VoyageAI embedding model implementation.

VoyageAI provides state-of-the-art embedding models optimized for retrieval, with specialized models for code, finance, and legal domains.

Example:

```
frompydantic_ai.embeddings.voyageaiimport VoyageAIEmbeddingModel

model = VoyageAIEmbeddingModel('voyage-3.5')
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/voyageai.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
```

````
@dataclass(init=False)
classVoyageAIEmbeddingModel(EmbeddingModel):
"""VoyageAI embedding model implementation.

    VoyageAI provides state-of-the-art embedding models optimized for
    retrieval, with specialized models for code, finance, and legal domains.

    Example:
    ```python
    from pydantic_ai.embeddings.voyageai import VoyageAIEmbeddingModel

    model = VoyageAIEmbeddingModel('voyage-3.5')
    ```
    """

    _model_name: VoyageAIEmbeddingModelName = field(repr=False)
    _provider: Provider[AsyncClient] = field(repr=False)

    def__init__(
        self,
        model_name: VoyageAIEmbeddingModelName,
        *,
        provider: Literal['voyageai'] | Provider[AsyncClient] = 'voyageai',
        settings: EmbeddingSettings | None = None,
    ):
"""Initialize a VoyageAI embedding model.

        Args:
            model_name: The name of the VoyageAI model to use.
                See [VoyageAI models](https://docs.voyageai.com/docs/embeddings)
                for available options.
            provider: The provider to use for authentication and API access. Can be:

                - `'voyageai'` (default): Uses the standard VoyageAI API
                - A [`VoyageAIProvider`][pydantic_ai.providers.voyageai.VoyageAIProvider] instance
                  for custom configuration
            settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
                to use as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider

        super().__init__(settings=settings)

    @property
    defbase_url(self) -> str:
"""The base URL for the provider API."""
        return self._provider.base_url

    @property
    defmodel_name(self) -> VoyageAIEmbeddingModelName:
"""The embedding model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The embedding model provider."""
        return self._provider.name

    async defembed(
        self,
        inputs: str | Sequence[str],
        *,
        input_type: EmbedInputType,
        settings: EmbeddingSettings | None = None,
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        settings = cast(VoyageAIEmbeddingSettings, settings)

        voyageai_input_type: VoyageAIEmbedInputType = settings.get(
            'voyageai_input_type', 'document' if input_type == 'document' else 'query'
        )
        # Convert 'none' string to None for the API
        api_input_type = None if voyageai_input_type == 'none' else voyageai_input_type

        try:
            response = await self._provider.client.embed(
                texts=list(inputs),
                model=self.model_name,
                input_type=api_input_type,
                truncation=settings.get('truncate', False),
                output_dimension=settings.get('dimensions'),
            )
        except VoyageError as e:
            raise ModelAPIError(model_name=self.model_name, message=str(e)) frome

        return EmbeddingResult(
            embeddings=response.embeddings,
            inputs=inputs,
            input_type=input_type,
            usage=_map_usage(response.total_tokens),
            model_name=self.model_name,
            provider_name=self.system,
        )

    async defmax_input_tokens(self) -> int | None:
        return _MAX_INPUT_TOKENS.get(self.model_name)
````

#### \_\_init\__

```
__init__(
    model_name: VoyageAIEmbeddingModelName,
    *,
    provider: (
        Literal["voyageai"] | Provider[AsyncClient]
    ) = "voyageai",
    settings: EmbeddingSettings | None = None
)
```

Initialize a VoyageAI embedding model.

Parameters:

Name Type Description Default `model_name` `VoyageAIEmbeddingModelName`

The name of the VoyageAI model to use. See [VoyageAI models](https://docs.voyageai.com/docs/embeddings) for available options.

*required* `provider` `Literal['voyageai'] | Provider[AsyncClient]`

The provider to use for authentication and API access. Can be:

- `'voyageai'` (default): Uses the standard VoyageAI API
- A [`VoyageAIProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.voyageai.VoyageAIProvider) instance for custom configuration

`'voyageai'` `settings` `EmbeddingSettings | None`

Model-specific [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") to use as defaults for this model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/voyageai.py`

```
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
```

```
def__init__(
    self,
    model_name: VoyageAIEmbeddingModelName,
    *,
    provider: Literal['voyageai'] | Provider[AsyncClient] = 'voyageai',
    settings: EmbeddingSettings | None = None,
):
"""Initialize a VoyageAI embedding model.

    Args:
        model_name: The name of the VoyageAI model to use.
            See [VoyageAI models](https://docs.voyageai.com/docs/embeddings)
            for available options.
        provider: The provider to use for authentication and API access. Can be:

            - `'voyageai'` (default): Uses the standard VoyageAI API
            - A [`VoyageAIProvider`][pydantic_ai.providers.voyageai.VoyageAIProvider] instance
              for custom configuration
        settings: Model-specific [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings]
            to use as defaults for this model.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider(provider)
    self._provider = provider

    super().__init__(settings=settings)
```

#### base\_url `property`

The base URL for the provider API.

#### model\_name `property`

The embedding model name.

#### system `property`

The embedding model provider.

### SentenceTransformersEmbeddingSettings

Bases: `EmbeddingSettings`

Settings used for a Sentence-Transformers embedding model request.

All fields from [`EmbeddingSettings`](#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") are supported, plus Sentence-Transformers-specific settings prefixed with `sentence_transformers_`.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/sentence_transformers.py`

```
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
```

```
classSentenceTransformersEmbeddingSettings(EmbeddingSettings, total=False):
"""Settings used for a Sentence-Transformers embedding model request.

    All fields from [`EmbeddingSettings`][pydantic_ai.embeddings.EmbeddingSettings] are supported,
    plus Sentence-Transformers-specific settings prefixed with `sentence_transformers_`.
    """

    sentence_transformers_device: str
"""Device to run inference on.

    Examples: `'cpu'`, `'cuda'`, `'cuda:0'`, `'mps'` (Apple Silicon).
    """

    sentence_transformers_normalize_embeddings: bool
"""Whether to L2-normalize embeddings.

    When `True`, all embeddings will have unit length, which is useful for
    cosine similarity calculations.
    """

    sentence_transformers_batch_size: int
"""Batch size to use during encoding.

    Larger batches may be faster but require more memory.
    """
```

#### sentence\_transformers\_device `instance-attribute`

```
sentence_transformers_device: str
```

Device to run inference on.

Examples: `'cpu'`, `'cuda'`, `'cuda:0'`, `'mps'` (Apple Silicon).

#### sentence\_transformers\_normalize\_embeddings `instance-attribute`

```
sentence_transformers_normalize_embeddings: bool
```

Whether to L2-normalize embeddings.

When `True`, all embeddings will have unit length, which is useful for cosine similarity calculations.

#### sentence\_transformers\_batch\_size `instance-attribute`

```
sentence_transformers_batch_size: int
```

Batch size to use during encoding.

Larger batches may be faster but require more memory.

### SentenceTransformerEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

Local embedding model using the `sentence-transformers` library.

This model runs embeddings locally on your machine, which is useful for:

- Privacy-sensitive applications where data shouldn't leave your infrastructure
- Reducing API costs for high-volume embedding workloads
- Offline or air-gapped environments

Models are downloaded from Hugging Face on first use. See the [Sentence-Transformers documentation](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html) for available models.

Example:

```
fromsentence_transformersimport SentenceTransformer

frompydantic_ai.embeddings.sentence_transformersimport (
    SentenceTransformerEmbeddingModel,
)

# Using a model name (downloads from Hugging Face)
model = SentenceTransformerEmbeddingModel('all-MiniLM-L6-v2')

# Using an existing SentenceTransformer instance
st_model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformerEmbeddingModel(st_model)
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/sentence_transformers.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
```

````
@dataclass(init=False)
classSentenceTransformerEmbeddingModel(EmbeddingModel):
"""Local embedding model using the `sentence-transformers` library.

    This model runs embeddings locally on your machine, which is useful for:

    - Privacy-sensitive applications where data shouldn't leave your infrastructure
    - Reducing API costs for high-volume embedding workloads
    - Offline or air-gapped environments

    Models are downloaded from Hugging Face on first use.
    See the [Sentence-Transformers documentation](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html)
    for available models.

    Example:
    ```python
    from sentence_transformers import SentenceTransformer

    from pydantic_ai.embeddings.sentence_transformers import (
        SentenceTransformerEmbeddingModel,
    )

    # Using a model name (downloads from Hugging Face)
    model = SentenceTransformerEmbeddingModel('all-MiniLM-L6-v2')

    # Using an existing SentenceTransformer instance
    st_model = SentenceTransformer('all-MiniLM-L6-v2')
    model = SentenceTransformerEmbeddingModel(st_model)
    ```
    """

    _model_name: str = field(repr=False)
    _model: SentenceTransformer | None = field(repr=False, default=None)

    def__init__(self, model: SentenceTransformer | str, *, settings: EmbeddingSettings | None = None) -> None:
"""Initialize a Sentence-Transformers embedding model.

        Args:
            model: The model to use. Can be:

                - A model name from Hugging Face (e.g., `'all-MiniLM-L6-v2'`)
                - A local path to a saved model
                - An existing `SentenceTransformer` instance
            settings: Model-specific
                [`SentenceTransformersEmbeddingSettings`][pydantic_ai.embeddings.sentence_transformers.SentenceTransformersEmbeddingSettings]
                to use as defaults for this model.
        """
        if isinstance(model, str):
            self._model_name = model
        else:
            self._model = deepcopy(model)
            self._model_name = model.model_card_data.model_id or model.model_card_data.base_model or 'unknown'

        super().__init__(settings=settings)

    @property
    defbase_url(self) -> str | None:
"""No base URL — runs locally."""
        return None

    @property
    defmodel_name(self) -> str:
"""The embedding model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The embedding model provider/system identifier."""
        return 'sentence-transformers'

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        settings = cast(SentenceTransformersEmbeddingSettings, settings)

        device = settings.get('sentence_transformers_device', None)
        normalize = settings.get('sentence_transformers_normalize_embeddings', False)
        batch_size = settings.get('sentence_transformers_batch_size', None)
        dimensions = settings.get('dimensions', None)

        model = await self._get_model()
        encode_func = model.encode_query if input_type == 'query' else model.encode_document  # type: ignore[reportUnknownReturnType]

        np_embeddings: np.ndarray[Any, float] = await _utils.run_in_executor(  # type: ignore[reportAssignmentType]
            encode_func,  # type: ignore[reportArgumentType]
            inputs,
            show_progress_bar=False,
            convert_to_numpy=True,
            convert_to_tensor=False,
            device=device,
            normalize_embeddings=normalize,
            truncate_dim=dimensions,
            **{'batch_size': batch_size} if batch_size is not None else {},  # type: ignore[reportArgumentType]
        )
        embeddings = np_embeddings.tolist()

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            model_name=self.model_name,
            provider_name=self.system,
        )

    async defmax_input_tokens(self) -> int | None:
        model = await self._get_model()
        return model.get_max_seq_length()

    async defcount_tokens(self, text: str) -> int:
        model = await self._get_model()
        result: dict[str, torch.Tensor] = await _utils.run_in_executor(
            model.tokenize,  # type: ignore[reportArgumentType]
            [text],
        )
        if 'input_ids' not in result or not isinstance(result['input_ids'], torch.Tensor):  # pragma: no cover
            raise UnexpectedModelBehavior(
                'The SentenceTransformers tokenizer output did not have an `input_ids` field holding a tensor',
                str(result),
            )
        return len(result['input_ids'][0])

    async def_get_model(self) -> SentenceTransformer:
        if self._model is None:
            # This may download the model from Hugging Face, so we do it in a thread
            self._model = await _utils.run_in_executor(SentenceTransformer, self.model_name)  # pragma: no cover
        return self._model
````

#### \_\_init\__

```
__init__(
    model: SentenceTransformer | str,
    *,
    settings: EmbeddingSettings | None = None
) -> None
```

Initialize a Sentence-Transformers embedding model.

Parameters:

Name Type Description Default `model` `SentenceTransformer | str`

The model to use. Can be:

- A model name from Hugging Face (e.g., `'all-MiniLM-L6-v2'`)
- A local path to a saved model
- An existing `SentenceTransformer` instance

*required* `settings` `EmbeddingSettings | None`

Model-specific [`SentenceTransformersEmbeddingSettings`](#pydantic_ai.embeddings.sentence_transformers.SentenceTransformersEmbeddingSettings "SentenceTransformersEmbeddingSettings") to use as defaults for this model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/sentence_transformers.py`

```
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
100
101
102
103
104
105
106
107
```

```
def__init__(self, model: SentenceTransformer | str, *, settings: EmbeddingSettings | None = None) -> None:
"""Initialize a Sentence-Transformers embedding model.

    Args:
        model: The model to use. Can be:

            - A model name from Hugging Face (e.g., `'all-MiniLM-L6-v2'`)
            - A local path to a saved model
            - An existing `SentenceTransformer` instance
        settings: Model-specific
            [`SentenceTransformersEmbeddingSettings`][pydantic_ai.embeddings.sentence_transformers.SentenceTransformersEmbeddingSettings]
            to use as defaults for this model.
    """
    if isinstance(model, str):
        self._model_name = model
    else:
        self._model = deepcopy(model)
        self._model_name = model.model_card_data.model_id or model.model_card_data.base_model or 'unknown'

    super().__init__(settings=settings)
```

#### base\_url `property`

No base URL — runs locally.

#### model\_name `property`

The embedding model name.

#### system `property`

The embedding model provider/system identifier.

### TestEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

A mock embedding model for testing.

This model returns deterministic embeddings (all 1.0 values) and tracks the settings used in the last call via the `last_settings` attribute.

Example:

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddingsimport TestEmbeddingModel

test_model = TestEmbeddingModel()
embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    with embedder.override(model=test_model):
        await embedder.embed_query('test')
        assert test_model.last_settings is not None
```

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/test.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
```

````
@dataclass(init=False)
classTestEmbeddingModel(EmbeddingModel):
"""A mock embedding model for testing.

    This model returns deterministic embeddings (all 1.0 values) and tracks
    the settings used in the last call via the `last_settings` attribute.

    Example:
    ```python
    from pydantic_ai import Embedder
    from pydantic_ai.embeddings import TestEmbeddingModel

    test_model = TestEmbeddingModel()
    embedder = Embedder('openai:text-embedding-3-small')


    async def main():
        with embedder.override(model=test_model):
            await embedder.embed_query('test')
            assert test_model.last_settings is not None
    ```
    """

    # NOTE: Avoid test discovery by pytest.
    __test__ = False

    _model_name: str
"""The model name to report in results."""

    _provider_name: str
"""The provider name to report in results."""

    _dimensions: int
"""The number of dimensions for generated embeddings."""

    last_settings: EmbeddingSettings | None = None
"""The settings used in the most recent embed call."""

    def__init__(
        self,
        model_name: str = 'test',
        *,
        provider_name: str = 'test',
        dimensions: int = 8,
        settings: EmbeddingSettings | None = None,
    ):
"""Initialize the test embedding model.

        Args:
            model_name: The model name to report in results.
            provider_name: The provider name to report in results.
            dimensions: The number of dimensions for the generated embeddings.
            settings: Optional default settings for the model.
        """
        self._model_name = model_name
        self._provider_name = provider_name
        self._dimensions = dimensions
        self.last_settings = None
        super().__init__(settings=settings)

    @property
    defmodel_name(self) -> str:
"""The embedding model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The embedding model provider."""
        return self._provider_name

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        self.last_settings = settings

        dimensions = settings.get('dimensions') or self._dimensions

        return EmbeddingResult(
            embeddings=[[1.0] * dimensions] * len(inputs),
            inputs=inputs,
            input_type=input_type,
            usage=RequestUsage(input_tokens=sum(_estimate_tokens(text) for text in inputs)),
            model_name=self.model_name,
            provider_name=self.system,
            provider_response_id=str(uuid.uuid4()),
        )

    async defmax_input_tokens(self) -> int | None:
        return 1024

    async defcount_tokens(self, text: str) -> int:
        return _estimate_tokens(text)
````

#### \_\_init\__

```
__init__(
    model_name: str = "test",
    *,
    provider_name: str = "test",
    dimensions: int = 8,
    settings: EmbeddingSettings | None = None
)
```

Initialize the test embedding model.

Parameters:

Name Type Description Default `model_name` `str`

The model name to report in results.

`'test'` `provider_name` `str`

The provider name to report in results.

`'test'` `dimensions` `int`

The number of dimensions for the generated embeddings.

`8` `settings` `EmbeddingSettings | None`

Optional default settings for the model.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/test.py`

```
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
```

```
def__init__(
    self,
    model_name: str = 'test',
    *,
    provider_name: str = 'test',
    dimensions: int = 8,
    settings: EmbeddingSettings | None = None,
):
"""Initialize the test embedding model.

    Args:
        model_name: The model name to report in results.
        provider_name: The provider name to report in results.
        dimensions: The number of dimensions for the generated embeddings.
        settings: Optional default settings for the model.
    """
    self._model_name = model_name
    self._provider_name = provider_name
    self._dimensions = dimensions
    self.last_settings = None
    super().__init__(settings=settings)
```

#### last\_settings `class-attribute` `instance-attribute`

```
last_settings: EmbeddingSettings | None = None
```

The settings used in the most recent embed call.

#### model\_name `property`

The embedding model name.

#### system `property`

The embedding model provider.

### WrapperEmbeddingModel `dataclass`

Bases: `EmbeddingModel`

Base class for embedding models that wrap another model.

Use this as a base class to create custom embedding model wrappers that modify behavior (e.g., caching, logging, rate limiting) while delegating to an underlying model.

By default, all methods are passed through to the wrapped model. Override specific methods to customize behavior.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/wrapper.py`

```
15
16
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
```

```
@dataclass(init=False)
classWrapperEmbeddingModel(EmbeddingModel):
"""Base class for embedding models that wrap another model.

    Use this as a base class to create custom embedding model wrappers
    that modify behavior (e.g., caching, logging, rate limiting) while
    delegating to an underlying model.

    By default, all methods are passed through to the wrapped model.
    Override specific methods to customize behavior.
    """

    wrapped: EmbeddingModel
"""The underlying embedding model being wrapped."""

    def__init__(self, wrapped: EmbeddingModel | str):
"""Initialize the wrapper with an embedding model.

        Args:
            wrapped: The model to wrap. Can be an
                [`EmbeddingModel`][pydantic_ai.embeddings.EmbeddingModel] instance
                or a model name string (e.g., `'openai:text-embedding-3-small'`).
        """
        from.import infer_embedding_model

        super().__init__()
        self.wrapped = infer_embedding_model(wrapped) if isinstance(wrapped, str) else wrapped

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        return await self.wrapped.embed(inputs, input_type=input_type, settings=settings)

    async defmax_input_tokens(self) -> int | None:
        return await self.wrapped.max_input_tokens()

    async defcount_tokens(self, text: str) -> int:
        return await self.wrapped.count_tokens(text)

    @property
    defmodel_name(self) -> str:
        return self.wrapped.model_name

    @property
    defsystem(self) -> str:
        return self.wrapped.system

    @property
    defsettings(self) -> EmbeddingSettings | None:
"""Get the settings from the wrapped embedding model."""
        return self.wrapped.settings

    @property
    defbase_url(self) -> str | None:
        return self.wrapped.base_url

    def__getattr__(self, item: str):
        return getattr(self.wrapped, item)  # pragma: no cover
```

#### \_\_init\__

```
__init__(wrapped: EmbeddingModel | str)
```

Initialize the wrapper with an embedding model.

Parameters:

Name Type Description Default `wrapped` `EmbeddingModel | str`

The model to wrap. Can be an [`EmbeddingModel`](#pydantic_ai.embeddings.EmbeddingModel "EmbeddingModel") instance or a model name string (e.g., `'openai:text-embedding-3-small'`).

*required*

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/wrapper.py`

```
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
```

```
def__init__(self, wrapped: EmbeddingModel | str):
"""Initialize the wrapper with an embedding model.

    Args:
        wrapped: The model to wrap. Can be an
            [`EmbeddingModel`][pydantic_ai.embeddings.EmbeddingModel] instance
            or a model name string (e.g., `'openai:text-embedding-3-small'`).
    """
    from.import infer_embedding_model

    super().__init__()
    self.wrapped = infer_embedding_model(wrapped) if isinstance(wrapped, str) else wrapped
```

#### wrapped `instance-attribute`

The underlying embedding model being wrapped.

#### settings `property`

```
settings: EmbeddingSettings | None
```

Get the settings from the wrapped embedding model.

### instrument\_embedding\_model

Instrument an embedding model with OpenTelemetry/logfire.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/instrumented.py`

```
30
31
32
33
34
35
36
37
38
```

```
definstrument_embedding_model(model: EmbeddingModel, instrument: InstrumentationSettings | bool) -> EmbeddingModel:
"""Instrument an embedding model with OpenTelemetry/logfire."""
    if instrument and not isinstance(model, InstrumentedEmbeddingModel):
        if instrument is True:
            instrument = InstrumentationSettings()

        model = InstrumentedEmbeddingModel(model, instrument)

    return model
```

### InstrumentedEmbeddingModel `dataclass`

Bases: `WrapperEmbeddingModel`

Embedding model which wraps another model so that requests are instrumented with OpenTelemetry.

See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.

Source code in `pydantic_ai_slim/pydantic_ai/embeddings/instrumented.py`

```
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
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
```

```
@dataclass(init=False)
classInstrumentedEmbeddingModel(WrapperEmbeddingModel):
"""Embedding model which wraps another model so that requests are instrumented with OpenTelemetry.

    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
    """

    instrumentation_settings: InstrumentationSettings
"""Instrumentation settings for this model."""

    def__init__(
        self,
        wrapped: EmbeddingModel | str,
        options: InstrumentationSettings | None = None,
    ) -> None:
        super().__init__(wrapped)
        self.instrumentation_settings = options or InstrumentationSettings()

    async defembed(
        self, inputs: str | Sequence[str], *, input_type: EmbedInputType, settings: EmbeddingSettings | None = None
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)
        with self._instrument(inputs, input_type, settings) as finish:
            result = await super().embed(inputs, input_type=input_type, settings=settings)
            finish(result)
            return result

    @contextmanager
    def_instrument(
        self,
        inputs: list[str],
        input_type: EmbedInputType,
        settings: EmbeddingSettings | None,
    ) -> Iterator[Callable[[EmbeddingResult], None]]:
        operation = 'embeddings'
        span_name = f'{operation}{self.model_name}'

        inputs_count = len(inputs)

        attributes: dict[str, AttributeValue] = {
            'gen_ai.operation.name': operation,
            **self.model_attributes(self.wrapped),
            'input_type': input_type,
            'inputs_count': inputs_count,
        }

        if settings:
            attributes['embedding_settings'] = json.dumps(self.serialize_any(settings))

        if self.instrumentation_settings.include_content:
            attributes['inputs'] = json.dumps(inputs)

        attributes['logfire.json_schema'] = json.dumps(
            {
                'type': 'object',
                'properties': {
                    'input_type': {'type': 'string'},
                    'inputs_count': {'type': 'integer'},
                    'embedding_settings': {'type': 'object'},
                    **(
                        {'inputs': {'type': ['array']}, 'embeddings': {'type': 'array'}}
                        if self.instrumentation_settings.include_content
                        else {}
                    ),
                },
            }
        )

        record_metrics: Callable[[], None] | None = None
        try:
            with self.instrumentation_settings.tracer.start_as_current_span(span_name, attributes=attributes) as span:

                deffinish(result: EmbeddingResult):
                    # Prepare metric recording closure first so metrics are recorded
                    # even if the span is not recording.
                    provider_name = attributes[GEN_AI_PROVIDER_NAME_ATTRIBUTE]
                    request_model = attributes[GEN_AI_REQUEST_MODEL_ATTRIBUTE]
                    response_model = result.model_name or request_model
                    price_calculation = None

                    def_record_metrics():
                        token_attributes = {
                            GEN_AI_PROVIDER_NAME_ATTRIBUTE: provider_name,
                            'gen_ai.operation.name': operation,
                            GEN_AI_REQUEST_MODEL_ATTRIBUTE: request_model,
                            'gen_ai.response.model': response_model,
                            'gen_ai.token.type': 'input',
                        }
                        tokens = result.usage.input_tokens or 0
                        if tokens:  # pragma: no branch
                            self.instrumentation_settings.tokens_histogram.record(tokens, token_attributes)
                            if price_calculation is not None:
                                self.instrumentation_settings.cost_histogram.record(
                                    float(getattr(price_calculation, 'input_price', 0.0)),
                                    token_attributes,
                                )

                    nonlocal record_metrics
                    record_metrics = _record_metrics

                    if not span.is_recording():
                        return

                    attributes_to_set: dict[str, AttributeValue] = {
                        **result.usage.opentelemetry_attributes(),
                        'gen_ai.response.model': response_model,
                    }

                    try:
                        price_calculation = result.cost()
                    except LookupError:
                        # The cost of this provider/model is unknown, which is common.
                        pass
                    except Exception as e:  # pragma: no cover
                        warnings.warn(
                            f'Failed to get cost from response: {type(e).__name__}: {e}', CostCalculationFailedWarning
                        )
                    else:
                        attributes_to_set['operation.cost'] = float(price_calculation.total_price)

                    embeddings = result.embeddings
                    if embeddings:  # pragma: no branch
                        attributes_to_set['gen_ai.embeddings.dimension.count'] = len(embeddings[0])
                        if self.instrumentation_settings.include_content:
                            attributes['embeddings'] = json.dumps(embeddings)

                    if result.provider_response_id is not None:
                        attributes_to_set['gen_ai.response.id'] = result.provider_response_id

                    span.set_attributes(attributes_to_set)

                yield finish
        finally:
            if record_metrics:  # pragma: no branch
                # Record metrics after the span finishes to avoid duplication.
                record_metrics()

    @staticmethod
    defmodel_attributes(model: EmbeddingModel) -> dict[str, AttributeValue]:
        attributes: dict[str, AttributeValue] = {
            GEN_AI_PROVIDER_NAME_ATTRIBUTE: model.system,
            GEN_AI_REQUEST_MODEL_ATTRIBUTE: model.model_name,
        }
        if base_url := model.base_url:
            try:
                parsed = urlparse(base_url)
            except Exception:  # pragma: no cover
                pass
            else:
                if parsed.hostname:  # pragma: no branch
                    attributes['server.address'] = parsed.hostname
                if parsed.port:
                    attributes['server.port'] = parsed.port  # pragma: no cover

        return attributes

    @staticmethod
    defserialize_any(value: Any) -> str:
        try:
            return ANY_ADAPTER.dump_python(value, mode='json')
        except Exception:  # pragma: no cover
            try:
                return str(value)
            except Exception as e:
                return f'Unable to serialize: {e}'
```

#### instrumentation\_settings `instance-attribute`

Instrumentation settings for this model.