---
title: Fine-tuning Embedding Models with Unsloth Guide
url: https://unsloth.ai/docs/basics/embedding-finetuning.md
source: llms
fetched_at: 2026-04-27T18:15:01.151740492-03:00
rendered_js: false
word_count: 807
summary: This document serves as a guide explaining how fine-tuning embedding models improves retrieval and RAG performance by aligning model vectors with specific domain needs. It details the features, workflow, benefits (speed/memory savings), and deployment methods of using Unsloth for these tasks.
tags:
    - embedding-models
    - unsloth
    - fine-tuning
    - rag
    - sentence-transformers
    - lora
    - performance
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Fine-tuning Embedding Models with Unsloth Guide

Fine-tuning embedding models aligns vectors with your domain's notion of similarity, improving search, RAG, clustering, and recommendations. E.g. "Google launches Pixel 10" vs "Qwen releases Qwen3" — similar as "Tech" but not semantically similar.

[Unsloth](https://github.com/unslothai/unsloth) trains embedding, classifier, BERT, and reranker models **~1.8-3.3x faster** with 20% less memory and 2x longer context than other Flash Attention 2 implementations — no accuracy loss. EmbeddingGemma-300M runs on **3GB VRAM**. Trained models deploy anywhere: transformers, LangChain, Ollama, vLLM, llama.cpp, etc.

Uses [SentenceTransformers](https://github.com/huggingface/sentence-transformers) for compatible models (Qwen3-Embedding, BERT, etc.). Even without a notebook/upload, the model is still supported.

## Free Fine-Tuning Notebooks

| Model | Link |
|---|---|
| EmbeddingGemma (300M) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/EmbeddingGemma_\(300M\).ipynb) |
| Qwen3-Embedding 4B | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_Embedding_\(4B\).ipynb) |
| Qwen3-Embedding 0.6B | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_Embedding_\(0_6B\).ipynb) |
| BGE M3 | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/BGE_M3.ipynb) |
| ModernBERT (classification) | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/bert_classification.ipynb) |
| All-MiniLM-L6-v2 | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/All_MiniLM_L6_v2.ipynb) |
| ModernBERT-large | [Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/bert_classification.ipynb) |

**Notable community models:**
- `tomaarsen/miriad-4.4M-split` — medical Q&A and biomedical papers
- `electroglyph/technical` — technical text (docs, specs, engineering)

All uploaded models: [HuggingFace collection](https://huggingface.co/collections/unsloth/embedding-models)

## Unsloth Features

- LoRA/QLoRA or full fine-tuning without pipeline changes
- Best support for encoder-only `SentenceTransformer` models (with `modules.json`)
- Cross-encoder models train properly under fallback path
- Supports `transformers v5`
- Limited support for models without `modules.json` (auto-assigns default pooling)
- Custom additions for MPNet/DistilBERT via patched gradient checkpointing

## Fine-Tuning Workflow

Centered around `FastSentenceTransformer`.

### Save/Push Methods

| Method | Action |
|---|---|
| `save_pretrained()` | Saves LoRA adapters locally |
| `save_pretrained_merged()` | Saves merged model locally |
| `push_to_hub()` | Pushes LoRA adapters to HuggingFace |
| `push_to_hub_merged()` | Pushes merged model to HuggingFace |

> [!important] Inference loading requires `for_inference=True`

```python
model = FastSentenceTransformer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2",
    for_inference=True,
)
```

For HuggingFace auth, run `hf auth login` in the same virtualenv before calling hub methods — no token argument needed.

## Inference and Deploy Anywhere

Works with: transformers, LangChain, Weaviate, sentence-transformers, TEI, vLLM, llama.cpp, custom embedding APIs, pgvector, FAISS, and any RAG framework. No lock-in.

```python
# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("<your-unsloth-finetuned-model")

query = "Which planet is known as the Red Planet?"
documents = [
    "Venus is often called Earth's twin because of its similar size and proximity.",
    "Mars, known for its reddish appearance, is often referred to as the Red Planet.",
    "Jupiter, the largest planet in our solar system, has a prominent red spot.",
    "Saturn, famous for its rings, is sometimes mistaken for the Red Planet."
]

# 2. Encode via encode_query and encode_document to automatically use the right prompts, if needed
query_embedding = model.encode_query(query)
document_embedding = model.encode_document(documents)
print(query_embedding.shape, document_embedding.shape)

# 3. Compute similarity, e.g. via the built-in similarity helper function
similarity = model.similarity(query_embedding, document_embedding)
print(similarity)
```

## Benchmarks

Consistently **1.8-3.3x faster** across embedding models and sequence lengths (128 to 2048+). EmbeddingGemma-300M QLoRA on **3GB VRAM**, LoRA on 6GB VRAM.

- **4bit QLoRA vs SentenceTransformers + FA2**: 1.8x to 2.6x faster
- **16bit LoRA vs SentenceTransformers + FA2**: 1.2x to 3.3x faster

## Supported Models

```
Alibaba-NLP/gte-modernbert-base
BAAI/bge-large-en-v1.5
BAAI/bge-m3
BAAI/bge-reranker-v2-m3
Qwen/Qwen3-Embedding-0.6B
answerdotai/ModernBERT-base
answerdotai/ModernBERT-large
google/embeddinggemma-300m
intfloat/e5-large-v2
intfloat/multilingual-e5-large-instruct
mixedbread-ai/mxbai-embed-large-v1
sentence-transformers/all-MiniLM-L6-v2
sentence-transformers/all-mpnet-base-v2
Snowflake/snowflake-arctic-embed-l-v2.0
```

Most [common models](https://huggingface.co/models?library=sentence-transformers) are supported. Request unsupported encoder-only models via [GitHub issue](https://github.com/unslothai/unsloth/issues).

#embedding-models #unsloth #fine-tuning #rag #sentence-transformers #lora
