---
title: Specific Model Examples - vLLM
url: https://docs.vllm.ai/en/latest/models/pooling_models/specific_models/
source: sitemap
fetched_at: 2026-05-07T21:15:04.770532269-03:00
rendered_js: false
word_count: 701
summary: This document provides instructions on using ColBERT and ColQwen late interaction models within vLLM for text and multi-modal reranking, scoring, and token embedding tasks.
tags:
    - vllm
    - colbert
    - colqwen
    - late-interaction
    - reranking
    - multi-modal
    - embedding
    - inference
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/pooling_models/specific_models.md "Edit this page")

## ColBERT Late Interaction Models[¶](#colbert-late-interaction-models "Permanent link")

[ColBERT](https://arxiv.org/abs/2004.12832) (Contextualized Late Interaction over BERT) is a retrieval model that uses per-token embeddings and MaxSim scoring for document ranking. Unlike single-vector embedding models, ColBERT retains token-level representations and computes relevance scores through late interaction, providing better accuracy while being more efficient than cross-encoders.

vLLM supports ColBERT models with multiple encoder backbones:

Architecture Backbone Example HF Models `HF_ColBERT` BERT `answerdotai/answerai-colbert-small-v1`, `colbert-ir/colbertv2.0` [`ColBERTModernBertModel`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colbert/#vllm.model_executor.models.colbert.ColBERTModernBertModel "            ColBERTModernBertModel") ModernBERT `lightonai/GTE-ModernColBERT-v1` [`ColBERTJinaRobertaModel`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colbert/#vllm.model_executor.models.colbert.ColBERTJinaRobertaModel "            ColBERTJinaRobertaModel") Jina XLM-RoBERTa `jinaai/jina-colbert-v2` [`ColBERTLfm2Model`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colbert/#vllm.model_executor.models.colbert.ColBERTLfm2Model "            ColBERTLfm2Model") LFM2 `LiquidAI/LFM2-ColBERT-350M`

**BERT-based ColBERT** models work out of the box:

```
vllmserveanswerdotai/answerai-colbert-small-v1
```

For **non-BERT backbones**, use `--hf-overrides` to set the correct architecture:

```
# ModernBERT backbone
vllmservelightonai/GTE-ModernColBERT-v1\
--hf-overrides'{"architectures": ["ColBERTModernBertModel"]}'

# Jina XLM-RoBERTa backbone
vllmservejinaai/jina-colbert-v2\
--hf-overrides'{"architectures": ["ColBERTJinaRobertaModel"]}'\
--trust-remote-code

# LFM2 backbone
vllmserveLiquidAI/LFM2-ColBERT-350M\
--hf-overrides'{"architectures": ["ColBERTLfm2Model"]}'
```

Then you can use the rerank API:

```
curl-shttp://localhost:8000/rerank-H"Content-Type: application/json"-d'{
    "model": "answerdotai/answerai-colbert-small-v1",
    "query": "What is machine learning?",
    "documents": [
        "Machine learning is a subset of artificial intelligence.",
        "Python is a programming language.",
        "Deep learning uses neural networks."
    ]
}'
```

Or the score API:

```
curl-shttp://localhost:8000/score-H"Content-Type: application/json"-d'{
    "model": "answerdotai/answerai-colbert-small-v1",
    "text_1": "What is machine learning?",
    "text_2": ["Machine learning is a subset of AI.", "The weather is sunny."]
}'
```

You can also get the raw token embeddings using the pooling API with `token_embed` task:

```
curl-shttp://localhost:8000/pooling-H"Content-Type: application/json"-d'{
    "model": "answerdotai/answerai-colbert-small-v1",
    "input": "What is machine learning?",
    "task": "token_embed"
}'
```

An example can be found here: [examples/pooling/score/colbert\_rerank\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/colbert_rerank_online.py)

## ColQwen3 Multi-Modal Late Interaction Models[¶](#colqwen3-multi-modal-late-interaction-models "Permanent link")

ColQwen3 is based on [ColPali](https://arxiv.org/abs/2407.01449), which extends ColBERT's late interaction approach to **multi-modal** inputs. While ColBERT operates on text-only token embeddings, ColPali/ColQwen3 can embed both **text and images** (e.g. PDF pages, screenshots, diagrams) into per-token L2-normalized vectors and compute relevance via MaxSim scoring. ColQwen3 specifically uses Qwen3-VL as its vision-language backbone.

Architecture Backbone Example HF Models `ColQwen3` Qwen3-VL `TomoroAI/tomoro-colqwen3-embed-4b`, `TomoroAI/tomoro-colqwen3-embed-8b` `OpsColQwen3Model` Qwen3-VL `OpenSearch-AI/Ops-Colqwen3-4B`, `OpenSearch-AI/Ops-Colqwen3-8B` `Qwen3VLNemotronEmbedModel` Qwen3-VL `nvidia/nemotron-colembed-vl-4b-v2`, `nvidia/nemotron-colembed-vl-8b-v2`

Start the server:

```
vllmserveTomoroAI/tomoro-colqwen3-embed-4b--max-model-len4096
```

### Text-only scoring and reranking[¶](#text-only-scoring-and-reranking "Permanent link")

Use the `/rerank` API:

```
curl-shttp://localhost:8000/rerank-H"Content-Type: application/json"-d'{
    "model": "TomoroAI/tomoro-colqwen3-embed-4b",
    "query": "What is machine learning?",
    "documents": [
        "Machine learning is a subset of artificial intelligence.",
        "Python is a programming language.",
        "Deep learning uses neural networks."
    ]
}'
```

Or the `/score` API:

```
curl-shttp://localhost:8000/score-H"Content-Type: application/json"-d'{
    "model": "TomoroAI/tomoro-colqwen3-embed-4b",
    "text_1": "What is the capital of France?",
    "text_2": ["The capital of France is Paris.", "Python is a programming language."]
}'
```

### Multi-modal scoring and reranking (text query × image documents)[¶](#multi-modal-scoring-and-reranking-text-query-image-documents "Permanent link")

The `/score` and `/rerank` APIs also accept multi-modal inputs directly. Pass image documents using the `data_1`/`data_2` (for `/score`) or `documents` (for `/rerank`) fields with a `content` list containing `image_url` and `text` parts — the same format used by the OpenAI chat completion API:

Score a text query against image documents:

```
curl-shttp://localhost:8000/score-H"Content-Type: application/json"-d'{
    "model": "TomoroAI/tomoro-colqwen3-embed-4b",
    "data_1": "Retrieve the city of Beijing",
    "data_2": [
        {
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,<BASE64>"}},
                {"type": "text", "text": "Describe the image."}
            ]
        }
    ]
}'
```

Rerank image documents by a text query:

```
curl-shttp://localhost:8000/rerank-H"Content-Type: application/json"-d'{
    "model": "TomoroAI/tomoro-colqwen3-embed-4b",
    "query": "Retrieve the city of Beijing",
    "documents": [
        {
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,<BASE64_1>"}},
                {"type": "text", "text": "Describe the image."}
            ]
        },
        {
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,<BASE64_2>"}},
                {"type": "text", "text": "Describe the image."}
            ]
        }
    ],
    "top_n": 2
}'
```

### Raw token embeddings[¶](#raw-token-embeddings "Permanent link")

You can also get the raw token embeddings using the `/pooling` API with `token_embed` task:

```
curl-shttp://localhost:8000/pooling-H"Content-Type: application/json"-d'{
    "model": "TomoroAI/tomoro-colqwen3-embed-4b",
    "input": "What is machine learning?",
    "task": "token_embed"
}'
```

For **image inputs** via the pooling API, use the chat-style `messages` field:

```
curl-shttp://localhost:8000/pooling-H"Content-Type: application/json"-d'{
    "model": "TomoroAI/tomoro-colqwen3-embed-4b",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,<BASE64>"}},
                {"type": "text", "text": "Describe the image."}
            ]
        }
    ]
}'
```

### Examples[¶](#examples "Permanent link")

- Multi-vector retrieval: [examples/pooling/token\_embed/colqwen3\_token\_embed\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_embed/colqwen3_token_embed_online.py)
- Reranking (text + multi-modal): [examples/pooling/score/colqwen3\_rerank\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/colqwen3_rerank_online.py)

## ColQwen3.5 Multi-Modal Late Interaction Models[¶](#colqwen35-multi-modal-late-interaction-models "Permanent link")

ColQwen3.5 is based on [ColPali](https://arxiv.org/abs/2407.01449), extending ColBERT's late interaction approach to **multi-modal** inputs. It uses the Qwen3.5 hybrid backbone (linear + full attention) and produces per-token L2-normalized vectors for MaxSim scoring.

Architecture Backbone Example HF Models `ColQwen3_5` Qwen3.5 `athrael-soju/colqwen3.5-4.5B`

Start the server:

```
vllmserveathrael-soju/colqwen3.5-4.5B--max-model-len4096
```

Then you can use the rerank endpoint:

```
curl-shttp://localhost:8000/rerank-H"Content-Type: application/json"-d'{
    "model": "athrael-soju/colqwen3.5-4.5B",
    "query": "What is machine learning?",
    "documents": [
        "Machine learning is a subset of artificial intelligence.",
        "Python is a programming language.",
        "Deep learning uses neural networks."
    ]
}'
```

Or the score endpoint:

```
curl-shttp://localhost:8000/score-H"Content-Type: application/json"-d'{
    "model": "athrael-soju/colqwen3.5-4.5B",
    "text_1": "What is the capital of France?",
    "text_2": ["The capital of France is Paris.", "Python is a programming language."]
}'
```

An example can be found here: [examples/pooling/score/colqwen3\_5\_rerank\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/colqwen3_5_rerank_online.py)

## Llama Nemotron Multimodal[¶](#llama-nemotron-multimodal "Permanent link")

### Embedding Model[¶](#embedding-model "Permanent link")

Llama Nemotron VL Embedding models combine the bidirectional Llama embedding backbone (from `nvidia/llama-nemotron-embed-1b-v2`) with SigLIP as the vision encoder to produce single-vector embeddings from text and/or images.

Architecture Backbone Example HF Models `LlamaNemotronVLModel` Bidirectional Llama + SigLIP `nvidia/llama-nemotron-embed-vl-1b-v2`

Start the server:

```
vllmservenvidia/llama-nemotron-embed-vl-1b-v2\
--trust-remote-code\
--chat-templateexamples/pooling/embed/template/nemotron_embed_vl.jinja
```

Note

The chat template bundled with this model's tokenizer is not suitable for the embeddings API. Use the provided override template above when serving with the `messages`-based (chat-style) embeddings API.

The override template uses the message `role` to automatically prepend the appropriate prefix: set `role` to `"query"` for queries (prepends `query:`) or `"document"` for passages (prepends `passage:`). Any other role omits the prefix.

Embed text queries:

```
curl-shttp://localhost:8000/v1/embeddings-H"Content-Type: application/json"-d'{
    "model": "nvidia/llama-nemotron-embed-vl-1b-v2",
    "messages": [
        {
            "role": "query",
            "content": [
                {"type": "text", "text": "What is machine learning?"}
            ]
        }
    ]
}'
```

Embed images via the chat-style `messages` field:

```
curl-shttp://localhost:8000/v1/embeddings-H"Content-Type: application/json"-d'{
    "model": "nvidia/llama-nemotron-embed-vl-1b-v2",
    "messages": [
        {
            "role": "document",
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,<BASE64>"}},
                {"type": "text", "text": "Describe the image."}
            ]
        }
    ]
}'
```

### Reranker Model[¶](#reranker-model "Permanent link")

Llama Nemotron VL reranker models combine the same bidirectional Llama + SigLIP backbone with a sequence-classification head for cross-encoder scoring and reranking.

Architecture Backbone Example HF Models [`LlamaNemotronVLForSequenceClassification`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/nemotron_vl/#vllm.model_executor.models.nemotron_vl.LlamaNemotronVLForSequenceClassification "            LlamaNemotronVLForSequenceClassification") Bidirectional Llama + SigLIP `nvidia/llama-nemotron-rerank-vl-1b-v2`

Start the server:

```
vllmservenvidia/llama-nemotron-rerank-vl-1b-v2\
--runnerpooling\
--trust-remote-code\
--chat-templateexamples/pooling/score/template/nemotron-vl-rerank.jinja
```

Note

The chat template bundled with this checkpoint's tokenizer is not suitable for the Score/Rerank APIs. Use the provided override template when serving: `examples/pooling/score/template/nemotron-vl-rerank.jinja`.

Score a text query against an image document:

```
curl-shttp://localhost:8000/score-H"Content-Type: application/json"-d'{
    "model": "nvidia/llama-nemotron-rerank-vl-1b-v2",
    "data_1": "Find diagrams about autonomous robots",
    "data_2": [
        {
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,<BASE64>"}},
                {"type": "text", "text": "Robotics workflow diagram."}
            ]
        }
    ]
}'
```

Rerank image documents by a text query:

```
curl-shttp://localhost:8000/rerank-H"Content-Type: application/json"-d'{
    "model": "nvidia/llama-nemotron-rerank-vl-1b-v2",
    "query": "Find diagrams about autonomous robots",
    "documents": [
        {
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,<BASE64_1>"}},
                {"type": "text", "text": "Robotics workflow diagram."}
            ]
        },
        {
            "content": [
                {"type": "image_url", "image_url": {"url": "data:image/png;base64,<BASE64_2>"}},
                {"type": "text", "text": "General skyline photo."}
            ]
        }
    ],
    "top_n": 2
}'
```

## BAAI/bge-m3[¶](#baaibge-m3 "Permanent link")

The `BAAI/bge-m3` model comes with extra weights for sparse and colbert embeddings but unfortunately in its `config.json` the architecture is declared as `XLMRobertaModel`, which makes `vLLM` load it as a vanilla ROBERTA model without the extra weights. To load the full model weights, override its architecture like this:

```
vllmserveBAAI/bge-m3--hf-overrides'{"architectures": ["BgeM3EmbeddingModel"]}'
```

Then you obtain the sparse embeddings like this:

```
curl-shttp://localhost:8000/pooling-H"Content-Type: application/json"-d'{
     "model": "BAAI/bge-m3",
     "task": "token_classify",
     "input": ["What is BGE M3?", "Definition of BM25"]
}'
```

Due to limitations in the output schema, the output consists of a list of token scores for each token for each input. This means that you'll have to call `/tokenize` as well to be able to pair tokens with scores. Refer to the tests in `tests/models/language/pooling/test_bge_m3.py` to see how to do that.

You can obtain the colbert embeddings like this:

```
curl-shttp://localhost:8000/pooling-H"Content-Type: application/json"-d'{
     "model": "BAAI/bge-m3",
     "task": "token_embed",
     "input": ["What is BGE M3?", "Definition of BM25"]
}'
```