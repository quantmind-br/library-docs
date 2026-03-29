---
title: Embeddings - Pydantic AI
url: https://ai.pydantic.dev/embeddings/
source: sitemap
fetched_at: 2026-01-22T22:23:23.776555908-03:00
rendered_js: false
word_count: 1088
summary: This document explains how to use the Pydantic AI embedding interface to generate vector representations of text, manage different providers, and handle embedding results for tasks like semantic search and RAG.
tags:
    - pydantic-ai
    - embeddings
    - vector-embeddings
    - semantic-search
    - rag
    - openai
    - google-gemini
category: guide
---

Embeddings are vector representations of text that capture semantic meaning. They're essential for building:

- **Semantic search** — Find documents based on meaning, not just keyword matching
- **RAG (Retrieval-Augmented Generation)** — Retrieve relevant context for your AI agents
- **Similarity detection** — Find similar documents, detect duplicates, or cluster content
- **Classification** — Use embeddings as features for downstream ML models

Pydantic AI provides a unified interface for generating embeddings across multiple providers.

## Quick Start

The [`Embedder`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder "Embedder            dataclass   ") class is the high-level interface for generating embeddings:

embeddings\_quickstart.py

```
frompydantic_aiimport Embedder

embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    # Embed a search query
    result = await embedder.embed_query('What is machine learning?')
    print(f'Embedding dimensions: {len(result.embeddings[0])}')
    #> Embedding dimensions: 1536

    # Embed multiple documents at once
    docs = [
        'Machine learning is a subset of AI.',
        'Deep learning uses neural networks.',
        'Python is a programming language.',
    ]
    result = await embedder.embed_documents(docs)
    print(f'Embedded {len(result.embeddings)} documents')
    #> Embedded 3 documents
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

Queries vs Documents

Some embedding models optimize differently for queries and documents. Use [`embed_query()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.embed_query "embed_query            async   ") for search queries and [`embed_documents()`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.Embedder.embed_documents "embed_documents            async   ") for content you're indexing.

## Embedding Result

All embed methods return an [`EmbeddingResult`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingResult "EmbeddingResult            dataclass   ") containing the embeddings along with useful metadata.

For convenience, you can access embeddings either by index (`result[0]`) or by the original input text (`result['Hello world']`).

embedding\_result.py

```
frompydantic_aiimport Embedder

embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    result = await embedder.embed_query('Hello world')

    # Access embeddings - each is a sequence of floats
    embedding = result.embeddings[0]  # By index via .embeddings
    embedding = result[0]  # Or directly via __getitem__
    embedding = result['Hello world']  # Or by original input text
    print(f'Dimensions: {len(embedding)}')
    #> Dimensions: 1536

    # Check usage
    print(f'Tokens used: {result.usage.input_tokens}')
    #> Tokens used: 2

    # Calculate cost (requires `genai-prices` to have pricing data for the model)
    cost = result.cost()
    print(f'Cost: ${cost.total_price:.6f}')
    #> Cost: $0.000000
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## Providers

### OpenAI

[`OpenAIEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.openai.OpenAIEmbeddingModel "OpenAIEmbeddingModel            dataclass   ") works with OpenAI's embeddings API and any [OpenAI-compatible provider](https://ai.pydantic.dev/models/openai/#openai-compatible-models).

#### Install

To use OpenAI embedding models, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `openai` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[openai]"
```

```
uvadd"pydantic-ai-slim[openai]"
```

#### Configuration

To use `OpenAIEmbeddingModel` with the OpenAI API, go to [platform.openai.com](https://platform.openai.com/) and follow your nose until you find the place to generate an API key. Once you have the API key, you can set it as an environment variable:

```
exportOPENAI_API_KEY='your-api-key'
```

You can then use the model:

openai\_embeddings.py

```
frompydantic_aiimport Embedder

embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 1536
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

See [OpenAI's embedding models](https://platform.openai.com/docs/guides/embeddings) for available models.

#### Dimension Control

OpenAI's `text-embedding-3-*` models support dimension reduction via the `dimensions` setting:

openai\_dimensions.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddingsimport EmbeddingSettings

embedder = Embedder(
    'openai:text-embedding-3-small',
    settings=EmbeddingSettings(dimensions=256),
)


async defmain():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 256
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

#### OpenAI-Compatible Providers

Since [`OpenAIEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.openai.OpenAIEmbeddingModel "OpenAIEmbeddingModel            dataclass   ") uses the same provider system as [`OpenAIChatModel`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIChatModel "OpenAIChatModel            dataclass   "), you can use it with any [OpenAI-compatible provider](https://ai.pydantic.dev/models/openai/#openai-compatible-models):

openai\_compatible\_embeddings.py

```
# Using Azure OpenAI
fromopenaiimport AsyncAzureOpenAI

frompydantic_aiimport Embedder
frompydantic_ai.embeddings.openaiimport OpenAIEmbeddingModel
frompydantic_ai.providers.openaiimport OpenAIProvider

azure_client = AsyncAzureOpenAI(
    azure_endpoint='https://your-resource.openai.azure.com',
    api_version='2024-02-01',
    api_key='your-azure-key',
)
model = OpenAIEmbeddingModel(
    'text-embedding-3-small',
    provider=OpenAIProvider(openai_client=azure_client),
)
embedder = Embedder(model)


# Using any OpenAI-compatible API
model = OpenAIEmbeddingModel(
    'your-model-name',
    provider=OpenAIProvider(
        base_url='https://your-provider.com/v1',
        api_key='your-api-key',
    ),
)
embedder = Embedder(model)
```

For providers with dedicated provider classes (like [`OllamaProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.ollama.OllamaProvider) or [`AzureProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.azure.AzureProvider "AzureProvider")), you can use the shorthand syntax:

```
frompydantic_aiimport Embedder

embedder = Embedder('azure:text-embedding-3-small')
embedder = Embedder('ollama:nomic-embed-text')
```

See [OpenAI-compatible Models](https://ai.pydantic.dev/models/openai/#openai-compatible-models) for the full list of supported providers.

### Google

[`GoogleEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.GoogleEmbeddingModel "GoogleEmbeddingModel            dataclass   ") works with Google's embedding models via the Gemini API (Google AI Studio) or Vertex AI.

#### Install

To use Google embedding models, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `google` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[google]"
```

```
uvadd"pydantic-ai-slim[google]"
```

#### Configuration

To use `GoogleEmbeddingModel` with the Gemini API, go to [aistudio.google.com](https://aistudio.google.com/) and generate an API key. Once you have the API key, you can set it as an environment variable:

```
exportGOOGLE_API_KEY='your-api-key'
```

You can then use the model:

google\_embeddings.py

```
frompydantic_aiimport Embedder

embedder = Embedder('google-gla:gemini-embedding-001')


async defmain():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 3072
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

See the [Google Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings) for available models.

##### Vertex AI

To use Google's embedding models via Vertex AI instead of the Gemini API, use the `google-vertex` provider prefix:

google\_vertex\_embeddings.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddings.googleimport GoogleEmbeddingModel
frompydantic_ai.providers.googleimport GoogleProvider

# Using provider prefix
embedder = Embedder('google-vertex:gemini-embedding-001')

# Or with explicit provider configuration
model = GoogleEmbeddingModel(
    'gemini-embedding-001',
    provider=GoogleProvider(vertexai=True, project='my-project', location='us-central1'),
)
embedder = Embedder(model)
```

See the [Google provider documentation](https://ai.pydantic.dev/models/google/#vertex-ai-enterprisecloud) for more details on Vertex AI authentication options, including application default credentials, service accounts, and API keys.

#### Dimension Control

Google's embedding models support dimension reduction via the `dimensions` setting:

google\_dimensions.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddingsimport EmbeddingSettings

embedder = Embedder(
    'google-gla:gemini-embedding-001',
    settings=EmbeddingSettings(dimensions=768),
)


async defmain():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 768
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

#### Google-Specific Settings

Google models support additional settings via [`GoogleEmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.google.GoogleEmbeddingSettings "GoogleEmbeddingSettings"):

google\_settings.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddings.googleimport GoogleEmbeddingSettings

embedder = Embedder(
    'google-gla:gemini-embedding-001',
    settings=GoogleEmbeddingSettings(
        dimensions=768,
        google_task_type='SEMANTIC_SIMILARITY',  # Optimize for similarity comparison
    ),
)
```

See [Google's task type documentation](https://ai.google.dev/gemini-api/docs/embeddings#task-types) for available task types. By default, `embed_query()` uses `RETRIEVAL_QUERY` and `embed_documents()` uses `RETRIEVAL_DOCUMENT`.

### Cohere

[`CohereEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.cohere.CohereEmbeddingModel "CohereEmbeddingModel            dataclass   ") provides access to Cohere's embedding models, which offer multilingual support and various model sizes.

#### Install

To use Cohere embedding models, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `cohere` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[cohere]"
```

```
uvadd"pydantic-ai-slim[cohere]"
```

#### Configuration

To use `CohereEmbeddingModel`, go to [dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys) and follow your nose until you find the place to generate an API key. Once you have the API key, you can set it as an environment variable:

```
exportCO_API_KEY='your-api-key'
```

You can then use the model:

cohere\_embeddings.py

```
frompydantic_aiimport Embedder

embedder = Embedder('cohere:embed-v4.0')


async defmain():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 1024
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

See the [Cohere Embed documentation](https://docs.cohere.com/docs/cohere-embed) for available models.

#### Cohere-Specific Settings

Cohere models support additional settings via [`CohereEmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.cohere.CohereEmbeddingSettings "CohereEmbeddingSettings"):

cohere\_settings.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddings.cohereimport CohereEmbeddingSettings

embedder = Embedder(
    'cohere:embed-v4.0',
    settings=CohereEmbeddingSettings(
        dimensions=512,
        cohere_truncate='END',  # Truncate long inputs instead of erroring
        cohere_max_tokens=256,  # Limit tokens per input
    ),
)
```

### VoyageAI

[`VoyageAIEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.voyageai.VoyageAIEmbeddingModel "VoyageAIEmbeddingModel            dataclass   ") provides access to VoyageAI's embedding models, which are optimized for retrieval with specialized models for code, finance, and legal domains.

#### Install

To use VoyageAI embedding models, you need to install `pydantic-ai-slim` with the `voyageai` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[voyageai]"
```

```
uvadd"pydantic-ai-slim[voyageai]"
```

#### Configuration

To use `VoyageAIEmbeddingModel`, go to [dash.voyageai.com](https://dash.voyageai.com/) to generate an API key. Once you have the API key, you can set it as an environment variable:

```
exportVOYAGE_API_KEY='your-api-key'
```

You can then use the model:

voyageai\_embeddings.py

```
frompydantic_aiimport Embedder

embedder = Embedder('voyageai:voyage-3.5')


async defmain():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 1024
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

See the [VoyageAI Embeddings documentation](https://docs.voyageai.com/docs/embeddings) for available models.

#### VoyageAI-Specific Settings

VoyageAI models support additional settings via [`VoyageAIEmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.voyageai.VoyageAIEmbeddingSettings "VoyageAIEmbeddingSettings"):

voyageai\_settings.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddings.voyageaiimport VoyageAIEmbeddingSettings

embedder = Embedder(
    'voyageai:voyage-3.5',
    settings=VoyageAIEmbeddingSettings(
        dimensions=512,  # Reduce output dimensions
        voyageai_input_type='document',  # Override input type for all requests
    ),
)
```

### Sentence Transformers (Local)

[`SentenceTransformerEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.sentence_transformers.SentenceTransformerEmbeddingModel "SentenceTransformerEmbeddingModel            dataclass   ") runs embeddings locally using the [sentence-transformers](https://www.sbert.net/) library. This is ideal for:

- **Privacy** — Data never leaves your infrastructure
- **Cost** — No API charges for high-volume workloads
- **Offline use** — No internet connection required after model download

#### Install

To use Sentence Transformers embedding models, you need to install `pydantic-ai-slim` with the `sentence-transformers` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[sentence-transformers]"
```

```
uvadd"pydantic-ai-slim[sentence-transformers]"
```

#### Usage

sentence\_transformers\_embeddings.py

```
frompydantic_aiimport Embedder

# Model is downloaded from Hugging Face on first use
embedder = Embedder('sentence-transformers:all-MiniLM-L6-v2')


async defmain():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 384
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

See the [Sentence-Transformers pretrained models](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html) documentation for available models.

#### Device Selection

Control which device to use for inference:

sentence\_transformers\_device.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddings.sentence_transformersimport (
    SentenceTransformersEmbeddingSettings,
)

embedder = Embedder(
    'sentence-transformers:all-MiniLM-L6-v2',
    settings=SentenceTransformersEmbeddingSettings(
        sentence_transformers_device='cuda',  # Use GPU
        sentence_transformers_normalize_embeddings=True,  # L2 normalize
    ),
)
```

#### Using an Existing Model Instance

If you need more control over model initialization:

sentence\_transformers\_instance.py

```
fromsentence_transformersimport SentenceTransformer

frompydantic_aiimport Embedder
frompydantic_ai.embeddings.sentence_transformersimport (
    SentenceTransformerEmbeddingModel,
)

# Create and configure the model yourself
st_model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

# Wrap it for use with Pydantic AI
model = SentenceTransformerEmbeddingModel(st_model)
embedder = Embedder(model)
```

## Settings

[`EmbeddingSettings`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingSettings "EmbeddingSettings") provides common configuration options that work across providers:

- `dimensions`: Reduce the output embedding dimensions (supported by OpenAI, Google, Cohere, VoyageAI)
- `truncate`: When `True`, truncate input text that exceeds the model's context length instead of raising an error (supported by Cohere, VoyageAI)

Settings can be specified at the embedder level (applied to all calls) or per-call:

embedding\_settings.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddingsimport EmbeddingSettings

# Default settings for all calls
embedder = Embedder(
    'openai:text-embedding-3-small',
    settings=EmbeddingSettings(dimensions=512),
)


async defmain():
    # Override for a specific call
    result = await embedder.embed_query(
        'Hello world',
        settings=EmbeddingSettings(dimensions=256),
    )
    print(len(result.embeddings[0]))
    #> 256
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## Token Counting

You can check token counts before embedding to avoid exceeding model limits:

token\_counting.py

```
frompydantic_aiimport Embedder

embedder = Embedder('openai:text-embedding-3-small')


async defmain():
    text = 'Hello world, this is a test.'

    # Count tokens in text
    token_count = await embedder.count_tokens(text)
    print(f'Tokens: {token_count}')
    #> Tokens: 7

    # Check model's maximum input tokens (returns None if unknown)
    max_tokens = await embedder.max_input_tokens()
    print(f'Max tokens: {max_tokens}')
    #> Max tokens: 1024
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## Testing

Use [`TestEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.TestEmbeddingModel "TestEmbeddingModel            dataclass   ") for testing without making API calls:

testing\_embeddings.py

```
frompydantic_aiimport Embedder
frompydantic_ai.embeddingsimport TestEmbeddingModel


async deftest_my_rag_system():
    embedder = Embedder('openai:text-embedding-3-small')
    test_model = TestEmbeddingModel()

    with embedder.override(model=test_model):
        result = await embedder.embed_query('test query')

        # TestEmbeddingModel returns deterministic embeddings
        assert result.embeddings[0] == [1.0] * 8

        # Check what settings were used
        assert test_model.last_settings is not None
```

## Instrumentation

Enable OpenTelemetry instrumentation for debugging and monitoring:

instrumented\_embeddings.py

```
importlogfire

frompydantic_aiimport Embedder

logfire.configure()

# Instrument a specific embedder
embedder = Embedder('openai:text-embedding-3-small', instrument=True)

# Or instrument all embedders globally
Embedder.instrument_all()
```

See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more details on using Logfire with Pydantic AI.

## Building Custom Embedding Models

To integrate a custom embedding provider, subclass [`EmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.EmbeddingModel "EmbeddingModel"):

custom\_embedding\_model.py

```
fromcollections.abcimport Sequence

frompydantic_ai.embeddingsimport EmbeddingModel, EmbeddingResult, EmbeddingSettings
frompydantic_ai.embeddings.resultimport EmbedInputType


classMyCustomEmbeddingModel(EmbeddingModel):
    @property
    defmodel_name(self) -> str:
        return 'my-custom-model'

    @property
    defsystem(self) -> str:
        return 'my-provider'

    async defembed(
        self,
        inputs: str | Sequence[str],
        *,
        input_type: EmbedInputType,
        settings: EmbeddingSettings | None = None,
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)

        # Call your embedding API here
        embeddings = [[0.1, 0.2, 0.3] for _ in inputs]  # Placeholder

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            model_name=self.model_name,
            provider_name=self.system,
        )
```

Use [`WrapperEmbeddingModel`](https://ai.pydantic.dev/api/embeddings/#pydantic_ai.embeddings.WrapperEmbeddingModel "WrapperEmbeddingModel            dataclass   ") if you want to wrap an existing model to add custom behavior like caching or logging.