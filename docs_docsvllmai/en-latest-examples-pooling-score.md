---
title: Score - vLLM
url: https://docs.vllm.ai/en/latest/examples/pooling/score/
source: sitemap
fetched_at: 2026-05-07T21:13:31.590898022-03:00
rendered_js: false
word_count: 2007
summary: This document provides code examples for using vLLM's rerank and score endpoints with various models, including Cohere-compatible clients, ColBERT, and multi-modal encoders.
tags:
    - vllm
    - reranking
    - scoring
    - api-integration
    - colbert
    - text-retrieval
    - machine-learning
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/score.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/pooling/score](https://github.com/vllm-project/vllm/tree/main/examples/pooling/score).

## Cohere Rerank Client[¶](#cohere-rerank-client "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Example of using the OpenAI entrypoint's rerank API which is compatible with
the Cohere SDK: https://github.com/cohere-ai/cohere-python
Note that `pip install cohere` is needed to run this example.

run: vllm serve BAAI/bge-reranker-base
"""

importcohere
fromcohereimport Client, ClientV2

model = "BAAI/bge-reranker-base"

query = "What is the capital of France?"

documents = [
    "The capital of France is Paris",
    "Reranking is fun!",
    "vLLM is an open-source framework for fast AI serving",
]


defcohere_rerank(
    client: Client | ClientV2, model: str, query: str, documents: list[str]
) -> dict:
    return client.rerank(model=model, query=query, documents=documents)


defmain():
    # cohere v1 client
    cohere_v1 = cohere.Client(base_url="http://localhost:8000", api_key="sk-fake-key")
    rerank_v1_result = cohere_rerank(cohere_v1, model, query, documents)
    print("-" * 50)
    print("rerank_v1_result:\n", rerank_v1_result)
    print("-" * 50)

    # or the v2
    cohere_v2 = cohere.ClientV2("sk-fake-key", base_url="http://localhost:8000")
    rerank_v2_result = cohere_rerank(cohere_v2, model, query, documents)
    print("rerank_v2_result:\n", rerank_v2_result)
    print("-" * 50)


if __name__ == "__main__":
    main()
```

## Colbert Rerank Online[¶](#colbert-rerank-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Example of using ColBERT late interaction models for reranking and scoring.

ColBERT (Contextualized Late Interaction over BERT) uses per-token embeddings
and MaxSim scoring for document reranking, providing better accuracy than
single-vector models while being more efficient than cross-encoders.

vLLM supports ColBERT with multiple encoder backbones. Start the server
with one of the following:

    # BERT backbone (works out of the box)
    vllm serve answerdotai/answerai-colbert-small-v1

    # ModernBERT backbone
    vllm serve lightonai/GTE-ModernColBERT-v1 \
        --hf-overrides '{"architectures": ["ColBERTModernBertModel"]}'

    # Jina XLM-RoBERTa backbone
    vllm serve jinaai/jina-colbert-v2 \
        --hf-overrides '{"architectures": ["ColBERTJinaRobertaModel"]}' \
        --trust-remote-code

Then run this script:
    python colbert_rerank_online.py
"""

importjson

importrequests

# Change this to match the model you started the server with
MODEL = "answerdotai/answerai-colbert-small-v1"
BASE_URL = "http://127.0.0.1:8000"

headers = {"accept": "application/json", "Content-Type": "application/json"}

documents = [
    "Machine learning is a subset of artificial intelligence.",
    "Python is a programming language.",
    "Deep learning uses neural networks for complex tasks.",
    "The weather today is sunny.",
]


defrerank_example():
"""Use the /rerank endpoint to rank documents by query relevance."""
    print("=== Rerank Example ===")

    data = {
        "model": MODEL,
        "query": "What is machine learning?",
        "documents": documents,
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)
    result = response.json()
    print(json.dumps(result, indent=2))

    print("\nRanked documents (most relevant first):")
    for item in result["results"]:
        doc_idx = item["index"]
        score = item["relevance_score"]
        print(f"  Score {score:.4f}: {documents[doc_idx]}")


defscore_example():
"""Use the /score endpoint for pairwise query-document scoring."""
    print("\n=== Score Example ===")

    data = {
        "model": MODEL,
        "text_1": "What is machine learning?",
        "text_2": [
            "Machine learning is a subset of AI.",
            "The weather is sunny.",
        ],
    }

    response = requests.post(f"{BASE_URL}/score", headers=headers, json=data)
    result = response.json()
    print(json.dumps(result, indent=2))


defmain():
    rerank_example()
    score_example()


if __name__ == "__main__":
    main()
```

## Colmodernvbert Rerank Online[¶](#colmodernvbert-rerank-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Example of using ColModernVBERT late interaction model for reranking.

ColModernVBERT is a multi-modal ColBERT-style model combining a SigLIP
vision encoder with a ModernBERT text encoder. It produces per-token
embeddings and uses MaxSim scoring for retrieval and reranking.
Supports both text and image inputs.

Start the server with:
    vllm serve ModernVBERT/colmodernvbert-merged --max-model-len 8192

Then run this script:
    python colmodernvbert_rerank_online.py
"""

importrequests

MODEL = "ModernVBERT/colmodernvbert-merged"
BASE_URL = "http://127.0.0.1:8000"

headers = {"accept": "application/json", "Content-Type": "application/json"}

IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/300px-PNG_transparency_demonstration_1.png"  # noqa: E501


defrerank_text():
"""Text-only reranking via /rerank endpoint."""
    print("=" * 60)
    print("1. Text reranking (/rerank)")
    print("=" * 60)

    data = {
        "model": MODEL,
        "query": "What is machine learning?",
        "documents": [
            "Machine learning is a subset of artificial intelligence.",
            "Python is a programming language.",
            "Deep learning uses neural networks for complex tasks.",
            "The weather today is sunny.",
        ],
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("\n  Ranked documents (most relevant first):")
        for item in result["results"]:
            doc_idx = item["index"]
            score = item["relevance_score"]
            print(f"    [{score:.4f}] {data['documents'][doc_idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defscore_text():
"""Text-only scoring via /score endpoint."""
    print()
    print("=" * 60)
    print("2. Text scoring (/score)")
    print("=" * 60)

    query = "What is the capital of France?"
    documents = [
        "The capital of France is Paris.",
        "Berlin is the capital of Germany.",
        "Python is a programming language.",
    ]

    data = {
        "model": MODEL,
        "text_1": query,
        "text_2": documents,
    }

    response = requests.post(f"{BASE_URL}/score", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(f"\n  Query: {query}\n")
        for item in result["data"]:
            idx = item["index"]
            score = item["score"]
            print(f"    Doc {idx} (score={score:.4f}): {documents[idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defscore_text_top_n():
"""Text reranking with top_n filtering via /rerank endpoint."""
    print()
    print("=" * 60)
    print("3. Text reranking with top_n=2 (/rerank)")
    print("=" * 60)

    data = {
        "model": MODEL,
        "query": "What is the capital of France?",
        "documents": [
            "The capital of France is Paris.",
            "Berlin is the capital of Germany.",
            "Python is a programming language.",
            "The Eiffel Tower is in Paris.",
        ],
        "top_n": 2,
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(f"\n  Top {data['top_n']} results:")
        for item in result["results"]:
            doc_idx = item["index"]
            score = item["relevance_score"]
            print(f"    [{score:.4f}] {data['documents'][doc_idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defrerank_multimodal():
"""Multimodal reranking with text and image documents via /rerank."""
    print()
    print("=" * 60)
    print("4. Multimodal reranking: text query vs image document (/rerank)")
    print("=" * 60)

    data = {
        "model": MODEL,
        "query": "A colorful logo with transparency",
        "documents": [
            {"content": [{"type": "image_url", "image_url": {"url": IMAGE_URL}}]},
            "Python is a programming language.",
            "The weather today is sunny.",
        ],
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("\n  Ranked documents (most relevant first):")
        labels = ["[image]", "Python doc", "Weather doc"]
        for item in result["results"]:
            doc_idx = item["index"]
            score = item["relevance_score"]
            print(f"    [{score:.4f}] {labels[doc_idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defmain():
    rerank_text()
    score_text()
    score_text_top_n()
    rerank_multimodal()


if __name__ == "__main__":
    main()
```

## Colqwen3 5 Rerank Online[¶](#colqwen3-5-rerank-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Example of using ColQwen3.5 late interaction model for reranking.

ColQwen3.5 is a multi-modal ColBERT-style model based on Qwen3.5.
It produces per-token embeddings and uses MaxSim scoring for retrieval
and reranking. Supports both text and image inputs.

Start the server with:
    vllm serve athrael-soju/colqwen3.5-4.5B --max-model-len 4096

Then run this script:
    python colqwen3_5_rerank_online.py
"""

importrequests

MODEL = "athrael-soju/colqwen3.5-4.5B"
BASE_URL = "http://127.0.0.1:8000"

headers = {"accept": "application/json", "Content-Type": "application/json"}


defrerank_text():
"""Text-only reranking via /rerank endpoint."""
    print("=" * 60)
    print("1. Text reranking (/rerank)")
    print("=" * 60)

    data = {
        "model": MODEL,
        "query": "What is machine learning?",
        "documents": [
            "Machine learning is a subset of artificial intelligence.",
            "Python is a programming language.",
            "Deep learning uses neural networks for complex tasks.",
            "The weather today is sunny.",
        ],
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("\n  Ranked documents (most relevant first):")
        for item in result["results"]:
            doc_idx = item["index"]
            score = item["relevance_score"]
            print(f"    [{score:.4f}] {data['documents'][doc_idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defscore_text():
"""Text-only scoring via /score endpoint."""
    print()
    print("=" * 60)
    print("2. Text scoring (/score)")
    print("=" * 60)

    query = "What is the capital of France?"
    documents = [
        "The capital of France is Paris.",
        "Berlin is the capital of Germany.",
        "Python is a programming language.",
    ]

    data = {
        "model": MODEL,
        "text_1": query,
        "text_2": documents,
    }

    response = requests.post(f"{BASE_URL}/score", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(f"\n  Query: {query}\n")
        for item in result["data"]:
            idx = item["index"]
            score = item["score"]
            print(f"    Doc {idx} (score={score:.4f}): {documents[idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defscore_text_top_n():
"""Text reranking with top_n filtering via /rerank endpoint."""
    print()
    print("=" * 60)
    print("3. Text reranking with top_n=2 (/rerank)")
    print("=" * 60)

    data = {
        "model": MODEL,
        "query": "What is the capital of France?",
        "documents": [
            "The capital of France is Paris.",
            "Berlin is the capital of Germany.",
            "Python is a programming language.",
            "The Eiffel Tower is in Paris.",
        ],
        "top_n": 2,
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(f"\n  Top {data['top_n']} results:")
        for item in result["results"]:
            doc_idx = item["index"]
            score = item["relevance_score"]
            print(f"    [{score:.4f}] {data['documents'][doc_idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defmain():
    rerank_text()
    score_text()
    score_text_top_n()


if __name__ == "__main__":
    main()
```

## Colqwen3 Rerank Online[¶](#colqwen3-rerank-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501
"""
Example of using ColQwen3 late interaction model for reranking and scoring.

ColQwen3 is a multi-modal ColBERT-style model based on Qwen3-VL.
It produces per-token embeddings and uses MaxSim scoring for retrieval
and reranking. Supports both text and image inputs.

Start the server with:
    vllm serve TomoroAI/tomoro-colqwen3-embed-4b --max-model-len 50000

Then run this script:
    python colqwen3_rerank_online.py
"""

fromioimport BytesIO

importpybase64asbase64
importrequests
fromPILimport Image

MODEL = "TomoroAI/tomoro-colqwen3-embed-4b"
BASE_URL = "http://127.0.0.1:8000"

headers = {"accept": "application/json", "Content-Type": "application/json"}

# ── Image helpers ──────────────────────────────────────────


defload_image(url: str) -> Image.Image:
"""Download an image from URL (handles Wikimedia 403)."""
    for hdrs in (
        {},
        {"User-Agent": "Mozilla/5.0 (compatible; ColQwen3-demo/1.0)"},
    ):
        resp = requests.get(url, headers=hdrs, timeout=15)
        if resp.status_code == 403:
            continue
        resp.raise_for_status()
        return Image.open(BytesIO(resp.content)).convert("RGB")
    raise RuntimeError(f"Could not fetch image from {url}")


defencode_image_base64(image: Image.Image) -> str:
"""Encode a PIL image to a base64 data URI."""
    buf = BytesIO()
    image.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


defmake_image_content(image_url: str, text: str = "Describe the image.") -> dict:
"""Build a ScoreMultiModalParam dict from an image URL."""
    image = load_image(image_url)
    return {
        "content": [
            {
                "type": "image_url",
                "image_url": {"url": encode_image_base64(image)},
            },
            {"type": "text", "text": text},
        ]
    }


# ── Sample image URLs ─────────────────────────────────────

IMAGE_URLS = {
    "beijing": "https://upload.wikimedia.org/wikipedia/commons/6/61/Beijing_skyline_at_night.JPG",
    "london": "https://upload.wikimedia.org/wikipedia/commons/4/49/London_skyline.jpg",
    "singapore": "https://upload.wikimedia.org/wikipedia/commons/2/27/Singapore_skyline_2022.jpg",
}

# ── Text-only examples ────────────────────────────────────


defrerank_text():
"""Text-only reranking via /rerank endpoint."""
    print("=" * 60)
    print("1. Text reranking (/rerank)")
    print("=" * 60)

    data = {
        "model": MODEL,
        "query": "What is machine learning?",
        "documents": [
            "Machine learning is a subset of artificial intelligence.",
            "Python is a programming language.",
            "Deep learning uses neural networks for complex tasks.",
            "The weather today is sunny.",
        ],
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("\n  Ranked documents (most relevant first):")
        for item in result["results"]:
            doc_idx = item["index"]
            score = item["relevance_score"]
            print(f"    [{score:.4f}] {data['documents'][doc_idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defscore_text():
"""Text-only scoring via /score endpoint."""
    print()
    print("=" * 60)
    print("2. Text scoring (/score)")
    print("=" * 60)

    query = "What is the capital of France?"
    documents = [
        "The capital of France is Paris.",
        "Berlin is the capital of Germany.",
        "Python is a programming language.",
    ]

    data = {
        "model": MODEL,
        "text_1": query,
        "text_2": documents,
    }

    response = requests.post(f"{BASE_URL}/score", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(f"\n  Query: {query}\n")
        for item in result["data"]:
            idx = item["index"]
            score = item["score"]
            print(f"    Doc {idx} (score={score:.4f}): {documents[idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defscore_text_top_n():
"""Text reranking with top_n filtering via /rerank endpoint."""
    print()
    print("=" * 60)
    print("3. Text reranking with top_n=2 (/rerank)")
    print("=" * 60)

    data = {
        "model": MODEL,
        "query": "What is the capital of France?",
        "documents": [
            "The capital of France is Paris.",
            "Berlin is the capital of Germany.",
            "Python is a programming language.",
            "The Eiffel Tower is in Paris.",
        ],
        "top_n": 2,
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(f"\n  Top {data['top_n']} results:")
        for item in result["results"]:
            doc_idx = item["index"]
            score = item["relevance_score"]
            print(f"    [{score:.4f}] {data['documents'][doc_idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


# ── Multi-modal examples (text query × image documents) ──


defscore_text_vs_images():
"""Score a text query against image documents via /score."""
    print()
    print("=" * 60)
    print("4. Multi-modal scoring: text query vs image docs (/score)")
    print("=" * 60)

    query = "Retrieve the city of Beijing"
    labels = list(IMAGE_URLS.keys())
    print(f"\n  Loading {len(labels)} images...")
    image_contents = [make_image_content(IMAGE_URLS[name]) for name in labels]

    data = {
        "model": MODEL,
        "data_1": query,
        "data_2": image_contents,
    }

    response = requests.post(f"{BASE_URL}/score", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(f'\n  Query: "{query}"\n')
        for item in result["data"]:
            idx = item["index"]
            print(f"    Doc {idx} [{labels[idx]}] score={item['score']:.4f}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


defrerank_text_vs_images():
"""Rerank image documents by a text query via /rerank."""
    print()
    print("=" * 60)
    print("5. Multi-modal reranking: text query vs image docs (/rerank)")
    print("=" * 60)

    query = "Retrieve the city of London"
    labels = list(IMAGE_URLS.keys())
    print(f"\n  Loading {len(labels)} images...")
    image_contents = [make_image_content(IMAGE_URLS[name]) for name in labels]

    data = {
        "model": MODEL,
        "query": query,
        "documents": image_contents,
        "top_n": 2,
    }

    response = requests.post(f"{BASE_URL}/rerank", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print(f'\n  Query: "{query}"')
        print(f"  Top {data['top_n']} results:\n")
        for item in result["results"]:
            idx = item["index"]
            print(f"    [{item['relevance_score']:.4f}] {labels[idx]}")
    else:
        print(f"  Request failed: {response.status_code}")
        print(f"  {response.text[:300]}")


# ── Main ──────────────────────────────────────────────────


defmain():
    # Text-only
    rerank_text()
    score_text()
    score_text_top_n()

    # Multi-modal (text query × image documents)
    score_text_vs_images()
    rerank_text_vs_images()


if __name__ == "__main__":
    main()
```

## Convert Model To Seq Cls[¶](#convert-model-to-seq-cls "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501

"""
Script to convert Large Language Models (LLMs) to Sequence Classification models.
This is particularly useful for converting reranker models that use next-token
prediction to a sequence classification format for compatibility with standard
classification and rerank pipelines.

Usage examples:
- For BAAI/bge-reranker-v2-gemma:
  python convert_model_to_seq_cls.py --model_name BAAI/bge-reranker-v2-gemma \
    --classifier_from_tokens '["Yes"]' --method no_post_processing \
    --path ./bge-reranker-v2-gemma-seq-cls

- For mxbai-rerank-v2:
  python convert_model_to_seq_cls.py --model_name mixedbread-ai/mxbai-rerank-base-v2 \
    --classifier_from_tokens '["0", "1"]' --method from_2_way_softmax \
    --path ./mxbai-rerank-base-v2-seq-cls

- For Qwen3-Reranker:
  python convert_model_to_seq_cls.py --model_name Qwen/Qwen3-Reranker-0.6B \
    --classifier_from_tokens '["no", "yes"]' --method from_2_way_softmax \
    --path ./Qwen3-Reranker-0.6B-seq-cls

Note: For BAAI/bge-reranker-v2-gemma, "Yes" and "yes" are different tokens.
"""

importargparse
importjson

importtorch
importtransformers


deffrom_2_way_softmax(causal_lm, seq_cls_model, tokenizer, tokens, device):
"""
    This method extracts the difference between weights for 'true' and 'false' tokens
    from the language model head to create a single classification weight vector.

    Args:
        causal_lm: The original causal language model
        seq_cls_model: The target sequence classification model
        tokenizer: Model tokenizer
        tokens: List of two tokens representing [false_token, true_token]
        device: Target device (cpu/cuda)

    Reference: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/discussions/3
    """
    assert len(tokens) == 2, (
        "Method requires exactly two tokens for binary classification"
    )

    # Get the language model head weights (vocabulary_size x hidden_size)
    lm_head_weights = causal_lm.lm_head.weight

    # Convert token strings to their corresponding token IDs
    false_id = tokenizer.convert_tokens_to_ids(tokens[0])
    true_id = tokenizer.convert_tokens_to_ids(tokens[1])

    # Compute the classification weight as the difference between true and false token weights
    # This follows the approach in: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/discussions/3
    score_weight = lm_head_weights[true_id].to(device).to(
        torch.float32
    ) - lm_head_weights[false_id].to(device).to(torch.float32)

    # Copy the computed weights to the sequence classification model
    with torch.no_grad():
        seq_cls_model.score.weight.copy_(score_weight.unsqueeze(0))
        if seq_cls_model.score.bias is not None:
            seq_cls_model.score.bias.zero_()


defno_post_processing(causal_lm, seq_cls_model, tokenizer, tokens, device):
"""
    Directly use token weights from the language model head for classification.

    This method maps each classification label directly to a corresponding token
    in the vocabulary without additional transformation.

    Args:
        causal_lm: The original causal language model
        seq_cls_model: The target sequence classification model
        tokenizer: Model tokenizer
        tokens: List of tokens representing class labels
        device: Target device (cpu/cuda)
    """
    # Get the language model head weights (vocabulary_size x hidden_size)
    lm_head_weights = causal_lm.lm_head.weight

    # Convert all tokens to their corresponding token IDs
    token_ids = [tokenizer.convert_tokens_to_ids(t) for t in tokens]

    # Extract weights for the specific tokens (num_tokens x hidden_size)
    score_weight = lm_head_weights[token_ids].to(device)

    # Copy the weights to the sequence classification model
    with torch.no_grad():
        seq_cls_model.score.weight.copy_(score_weight)
        if seq_cls_model.score.bias is not None:
            seq_cls_model.score.bias.zero_()


method_map = {
    function.__name__: function for function in [from_2_way_softmax, no_post_processing]
}


defconverting(
    model_name, classifier_from_tokens, path, method, use_sep_token=False, device="cpu"
):
"""
    Main conversion function to transform a CausalLM model to SequenceClassification.

    Args:
        model_name: Name or path of the pretrained model
        classifier_from_tokens: List of tokens used for classification
        path: Output path to save the converted model
        method: Conversion method ('from_2_way_softmax' or 'no_post_processing')
        use_sep_token: Whether to use separating token in the sequence classification model
        device: Device to load the model on ('cpu' or 'cuda')
    """
    assert method in method_map, f"Unknown method: {method}"

    # Determine number of labels based on conversion method
    if method == "from_2_way_softmax":
        assert len(classifier_from_tokens) == 2
        num_labels = 1
    else:
        num_labels = len(classifier_from_tokens)

    # Load tokenizer and original causal language model
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    causal_lm = transformers.AutoModelForCausalLM.from_pretrained(
        model_name, device_map=device
    )

    # Load an empty sequence classification model with the same architecture
    seq_cls_model = transformers.AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=num_labels,
        ignore_mismatched_sizes=True,
        device_map=device,
    )

    # Apply the selected conversion method to transfer weights
    method_map[method](
        causal_lm, seq_cls_model, tokenizer, classifier_from_tokens, device
    )

    # Configure separating token settings
    # Note: `llm as reranker` defaults to not using separating token.
    seq_cls_model.config.use_sep_token = use_sep_token
    seq_cls_model.config.sep_token_id = tokenizer.sep_token_id

    # Save the converted model and tokenizer
    seq_cls_model.save_pretrained(path)
    tokenizer.save_pretrained(path)


defparse_args():
    parser = argparse.ArgumentParser(
        description="Converting *ForCausalLM models to "
        "*ForSequenceClassification models."
    )
    parser.add_argument(
        "--model_name",
        type=str,
        default="BAAI/bge-reranker-v2-gemma",
        help="HuggingFace model name or local path",
    )
    parser.add_argument(
        "--classifier_from_tokens",
        type=str,
        default='["Yes"]',
        help="JSON string of tokens used for classification labels",
    )
    parser.add_argument(
        "--method",
        type=str,
        default="no_post_processing",
        help="Conversion method to use",
    )
    parser.add_argument(
        "--use-sep-token",
        action="store_true",
        help="Enable separating token in the sequence classification model",
    )
    parser.add_argument(
        "--path",
        type=str,
        default="./bge-reranker-v2-gemma-seq-cls",
        help="Output directory to save the converted model",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    converting(
        model_name=args.model_name,
        classifier_from_tokens=json.loads(args.classifier_from_tokens),
        method=args.method,
        use_sep_token=args.use_sep_token,
        path=args.path,
    )
```

## Qwen3 Reranker Offline[¶](#qwen3-reranker-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501

"""
What is the difference between the official original version and one
that has been converted into a sequence classification model?

Qwen3-Reranker is a language model that doing reranker by using the
logits of "no" and "yes" tokens.
This requires computing logits for all 151,669 tokens in the vocabulary,
making it inefficient and incompatible with vLLM's score() API.

A conversion method has been proposed to transform the original model into a
sequence classification model. This converted model:
1. Is significantly more efficient
2. Fully supports vLLM's score() API
3. Simplifies initialization parameters
Reference: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/discussions/3
Reference: https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/convert_model_to_seq_cls.py

For the converted model, initialization would simply be:
llm = LLM(model="tomaarsen/Qwen3-Reranker-0.6B-seq-cls", runner="pooling")

This example demonstrates loading the ORIGINAL model with special overrides
to make it compatible with vLLM's score API.
"""

frompathlibimport Path

fromvllmimport LLM

model_name = "Qwen/Qwen3-Reranker-0.6B"


defget_llm() -> LLM:
"""
    Initializes and returns the LLM model for Qwen3-Reranker.

    Returns:
        LLM: Configured vLLM instance for reranking tasks.

    Note:
        This function loads the ORIGINAL Qwen3-Reranker model with specific
        overrides to make it compatible with vLLM's score API.
    """
    return LLM(
        # Specify the original model from HuggingFace
        model=model_name,
        # Use pooling runner for score task
        runner="pooling",
        # HuggingFace model configuration overrides required for compatibility
        hf_overrides={
            # Manually route to sequence classification architecture
            # This tells vLLM to use Qwen3ForSequenceClassification instead of
            # the default Qwen3ForCausalLM
            "architectures": ["Qwen3ForSequenceClassification"],
            # Specify which token logits to extract from the language model head
            # The original reranker uses "no" and "yes" token logits for scoring
            "classifier_from_token": ["no", "yes"],
            # Enable special handling for original Qwen3-Reranker models
            # This flag triggers conversion logic that transforms the two token
            # vectors into a single classification vector
            "is_original_qwen3_reranker": True,
        },
    )


defmain() -> None:
    # Load the Jinja template for formatting query-document pairs
    # The template ensures proper formatting for the reranker model
    template_home = Path(__file__).parent / "template"
    template_path = "qwen3_reranker.jinja"
    chat_template = (template_home / template_path).read_text()

    # Sample queries for testing the reranker
    queries = [
        "What is the capital of China?",
        "Explain gravity",
    ]

    # Corresponding documents to be scored against each query
    documents = [
        "The capital of China is Beijing.",
        "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.",
    ]

    # Initialize the LLM model with the original Qwen3-Reranker configuration
    llm = get_llm()

    # Compute relevance scores for each query-document pair
    # The score() method returns a relevance score for each pair
    # Higher scores indicate better relevance
    outputs = llm.score(queries, documents, chat_template=chat_template)

    # Extract and print the relevance scores from the outputs
    # Each output contains a score representing query-document relevance
    print("-" * 30)
    print("Relevance scores:", [output.outputs.score for output in outputs])
    print("-" * 30)


if __name__ == "__main__":
    main()
```

## Qwen3 Reranker Online[¶](#qwen3-reranker-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501
"""
What is the difference between the official original version and one
that has been converted into a sequence classification model?

Qwen3-Reranker is a language model that doing reranker by using the
logits of "no" and "yes" tokens.
This requires computing logits for all 151,669 tokens in the vocabulary,
making it inefficient and incompatible with vLLM's score() API.

A conversion method has been proposed to transform the original model into a
sequence classification model. This converted model:
1. Is significantly more efficient
2. Fully supports vLLM's score() API
3. Simplifies initialization parameters
Reference: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/discussions/3
Reference: https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/convert_model_to_seq_cls.py

For the converted model, initialization would simply be:
    vllm serve tomaarsen/Qwen3-Reranker-0.6B-seq-cls --runner pooling --chat-template examples/pooling/score/template/qwen3_reranker.jinja

This example demonstrates loading the ORIGINAL model with special overrides
to make it compatible with vLLM's score API.
    vllm serve Qwen/Qwen3-Reranker-0.6B --runner pooling --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' --chat-template examples/pooling/score/template/qwen3_reranker.jinja
"""

importjson

importrequests

# URL of the vLLM server's score endpoint
# Default vLLM server runs on localhost port 8000
url = "http://127.0.0.1:8000/score"

# HTTP headers for the request
headers = {"accept": "application/json", "Content-Type": "application/json"}

# Example queries & documents
queries = [
    "What is the capital of China?",
    "Explain gravity",
]
documents = [
    "The capital of China is Beijing.",
    "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.",
]

# Request payload for the score API
data = {
    "model": "Qwen/Qwen3-Reranker-0.6B",
    "queries": queries,
    "documents": documents,
}


defmain():
"""Main function to send a score request to the vLLM server.

    This function sends a POST request to the /score endpoint with
    the query and documents, then prints the relevance scores.
    """
    # Send POST request to the vLLM server's score endpoint
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful!")
        # Pretty print the JSON response containing relevance scores
        # The response includes scores for each document's relevance to the query
        print(json.dumps(response.json(), indent=2))
    else:
        # Handle request failure
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    main()
```

## Rerank API Online[¶](#rerank-api-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Example of using the OpenAI entrypoint's rerank API which is compatible with
Jina and Cohere https://jina.ai/reranker

run: vllm serve BAAI/bge-reranker-base
"""

importjson

importrequests

url = "http://127.0.0.1:8000/rerank"

headers = {"accept": "application/json", "Content-Type": "application/json"}

data = {
    "model": "BAAI/bge-reranker-base",
    "query": "What is the capital of France?",
    "documents": [
        "The capital of Brazil is Brasilia.",
        "The capital of France is Paris.",
        "Horses and cows are both animals",
    ],
}


defmain():
    response = requests.post(url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        print("Request successful!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    main()
```

## Score API Online[¶](#score-api-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Example online usage of Score API.

Run `vllm serve <model> --runner pooling` to start up the server in vLLM.
"""

importargparse
importpprint

importrequests


defpost_http_request(prompt: dict, api_url: str) -> requests.Response:
    headers = {"User-Agent": "Test Client"}
    response = requests.post(api_url, headers=headers, json=prompt)
    return response


defparse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--model", type=str, default="BAAI/bge-reranker-v2-m3")
    return parser.parse_args()


defmain(args):
    api_url = f"http://{args.host}:{args.port}/score"
    model_name = args.model

    queries = "What is the capital of Brazil?"
    documents = "The capital of Brazil is Brasilia."
    prompt = {"model": model_name, "queries": queries, "documents": documents}
    score_response = post_http_request(prompt=prompt, api_url=api_url)
    print("\nPrompt when queries and documents are both strings:")
    pprint.pprint(prompt)
    print("\nScore Response:")
    pprint.pprint(score_response.json())

    queries = "What is the capital of France?"
    documents = [
        "The capital of Brazil is Brasilia.",
        "The capital of France is Paris.",
    ]
    prompt = {"model": model_name, "queries": queries, "documents": documents}
    score_response = post_http_request(prompt=prompt, api_url=api_url)
    print("\nPrompt when queries is string and documents is a list:")
    pprint.pprint(prompt)
    print("\nScore Response:")
    pprint.pprint(score_response.json())

    queries = ["What is the capital of Brazil?", "What is the capital of France?"]
    documents = [
        "The capital of Brazil is Brasilia.",
        "The capital of France is Paris.",
    ]
    prompt = {"model": model_name, "queries": queries, "documents": documents}
    score_response = post_http_request(prompt=prompt, api_url=api_url)
    print("\nPrompt when queries and documents are both lists:")
    pprint.pprint(prompt)
    print("\nScore Response:")
    pprint.pprint(score_response.json())


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Template - Bge-Reranker-V2-Gemma[¶](#template-bge-reranker-v2-gemma "Permanent link")

```
A: {{ (messages | selectattr("role", "eq", "query") | first).content }}
B: {{ (messages | selectattr("role", "eq", "document") | first).content }}
Given a query A and a passage B, determine whether the passage contains an answer to the query by providing a prediction of either 'Yes' or 'No'.
```

## Template - Mxbai Rerank V2[¶](#template-mxbai-rerank-v2 "Permanent link")

```
<|im_start|>system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.<|im_end|>
<|im_start|>user
query: {{ (messages | selectattr("role", "eq", "query") | first).content }}
document: {{ (messages | selectattr("role", "eq", "document") | first).content }}
You are a search relevance expert who evaluates how well documents match search queries. For each query-document pair, carefully analyze the semantic relationship between them, then provide your binary relevance judgment (0 for not relevant, 1 for relevant).
Relevance:<|im_end|>
<|im_start|>assistant
```

## Template - Nemotron-Rerank[¶](#template-nemotron-rerank "Permanent link")

```
question:{{ (messages | selectattr("role", "eq", "query") | first).content }}

 passage:{{ (messages | selectattr("role", "eq", "document") | first).content }}
```

## Template - Nemotron-Vl-Rerank[¶](#template-nemotron-vl-rerank "Permanent link")

```
{%- set query_msg = (messages | selectattr('role', 'equalto', 'query') | list | first) -%}
{%- set doc_msg   = (messages | selectattr('role', 'equalto', 'document') | list | first) -%}

{%- set q = query_msg['content'] -%}
{%- set d = doc_msg['content'] -%}

{# If the doc contains <image> anywhere, hoist a single <image> to the front #}
{%- set has_image = ("<image>" in d) -%}
{%- set d_clean = d | replace("<image>", "") -%}
{%- set q_clean = q | replace("<image>", "") -%}

{%- if has_image -%}<image>{{ " " }}{%- endif -%}
question:{{ q_clean }}{{ " " }}
{{ " " }}
{{ " " }}passage:{{ d_clean }}
```

## Template - Qwen3 Reranker[¶](#template-qwen3-reranker "Permanent link")

```
<|im_start|>system
Judge whether the Document meets the requirements based on the Query and the Instruct provided. Note that the answer can only be "yes" or "no".<|im_end|>
<|im_start|>user
<Instruct>: {{ messages | selectattr("role", "eq", "system") | map(attribute="content") | first | default("Given a web search query, retrieve relevant passages that answer the query") }}
<Query>: {{ messages | selectattr("role", "eq", "query") | map(attribute="content") | first }}
<Document>: {{ messages | selectattr("role", "eq", "document") | map(attribute="content") | first }}<|im_end|>
<|im_start|>assistant
<think>

</think>
```

## Template - Qwen3 Vl Reranker[¶](#template-qwen3-vl-reranker "Permanent link")

```
<|im_start|>system
Judge whether the Document meets the requirements based on the Query and the Instruct provided. Note that the answer can only be "yes" or "no".<|im_end|>
<|im_start|>user
<Instruct>: {{
    messages
    | selectattr("role", "eq", "system")
    | map(attribute="content")
    | first
    | default("Given a search query, retrieve relevant candidates that answer the query.")
}}<Query>:{{
    messages
    | selectattr("role", "eq", "query")
    | map(attribute="content")
    | first
}}
<Document>:{{
    messages
    | selectattr("role", "eq", "document")
    | map(attribute="content")
    | first
}}<|im_end|>
<|im_start|>assistant
```

## Using Template Offline[¶](#using-template-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501
fromargparseimport Namespace
frompathlibimport Path
fromtypingimport Any

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defparse_args():
"""Parse command line arguments for the reranking example.

    This function sets up the argument parser with default values
    specific to reranking models, including the model name and
    runner type.
    """
    parser = FlexibleArgumentParser()
    # Add all EngineArgs command line arguments to the parser
    parser = EngineArgs.add_cli_args(parser)

    # Set default values specific to this reranking example
    # These defaults ensure the script works out-of-the-box for reranking tasks
    parser.set_defaults(
        model="nvidia/llama-nemotron-rerank-1b-v2",  # Default reranking model
        runner="pooling",  # Required for cross-encoder/reranking models
        trust_remote_code=True,  # Allow loading models with custom code
    )
    return parser.parse_args()


defget_chat_template(model: str) -> str:
"""Load the appropriate chat template for the specified model.

    Reranking models require specific prompt templates to format
    query-document pairs correctly. This function maps model names
    to their corresponding template files.
    """
    # Directory containing all chat template files
    template_home = Path(__file__).parent / "template"

    # Mapping from model names to their corresponding template files
    # Each reranking model has its own specific prompt format
    model_name_to_template_path_map = {
        "BAAI/bge-reranker-v2-gemma": "bge-reranker-v2-gemma.jinja",
        "Qwen/Qwen3-Reranker-0.6B": "qwen3_reranker.jinja",
        "Qwen/Qwen3-Reranker-4B": "qwen3_reranker.jinja",
        "Qwen/Qwen3-Reranker-8B": "qwen3_reranker.jinja",
        "tomaarsen/Qwen3-Reranker-0.6B-seq-cls": "qwen3_reranker.jinja",
        "tomaarsen/Qwen3-Reranker-4B-seq-cls": "qwen3_reranker.jinja",
        "tomaarsen/Qwen3-Reranker-8B-seq-cls": "qwen3_reranker.jinja",
        "mixedbread-ai/mxbai-rerank-base-v2": "mxbai_rerank_v2.jinja",
        "mixedbread-ai/mxbai-rerank-large-v2": "mxbai_rerank_v2.jinja",
        "nvidia/llama-nemotron-rerank-1b-v2": "nemotron-rerank.jinja",
    }

    # Get the template filename for the specified model
    template_path = model_name_to_template_path_map.get(model)

    if template_path is None:
        raise ValueError(f"This demo does not support model name: {model}.")

    # Read and return the template content
    return (template_home / template_path).read_text()


defget_hf_overrides(model: str) -> dict[str, Any]:
"""Convert Large Language Models (LLMs) to Sequence Classification models.

    note:
        Some reranking models require special configuration overrides to work
        correctly with vLLM's score API.
        Reference: https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/qwen3_reranker_offline.py
        Reference: https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/convert_model_to_seq_cls.py
    """

    model_name_to_hf_overrides_map = {
        "BAAI/bge-reranker-v2-gemma": {
            "architectures": ["GemmaForSequenceClassification"],
            "classifier_from_token": ["Yes"],
            "method": "no_post_processing",
        },
        "Qwen/Qwen3-Reranker-0.6B": {
            "architectures": ["Qwen3ForSequenceClassification"],
            "classifier_from_token": ["no", "yes"],
            "is_original_qwen3_reranker": True,
        },
        "Qwen/Qwen3-Reranker-4B": {
            "architectures": ["Qwen3ForSequenceClassification"],
            "classifier_from_token": ["no", "yes"],
            "is_original_qwen3_reranker": True,
        },
        "Qwen/Qwen3-Reranker-8B": {
            "architectures": ["Qwen3ForSequenceClassification"],
            "classifier_from_token": ["no", "yes"],
            "is_original_qwen3_reranker": True,
        },
        "tomaarsen/Qwen3-Reranker-0.6B-seq-cls": {},
        "tomaarsen/Qwen3-Reranker-4B-seq-cls": {},
        "tomaarsen/Qwen3-Reranker-8B-seq-cls": {},
        "mixedbread-ai/mxbai-rerank-base-v2": {
            "architectures": ["Qwen2ForSequenceClassification"],
            "classifier_from_token": ["0", "1"],
            "method": "from_2_way_softmax",
        },
        "mixedbread-ai/mxbai-rerank-large-v2": {
            "architectures": ["Qwen2ForSequenceClassification"],
            "classifier_from_token": ["0", "1"],
            "method": "from_2_way_softmax",
        },
        "nvidia/llama-nemotron-rerank-1b-v2": {},
    }

    hf_overrides = model_name_to_hf_overrides_map.get(model)

    if hf_overrides is None:
        raise ValueError(f"This demo does not support model name: {model}.")

    return hf_overrides


defmain(args: Namespace):
"""Main execution function for the reranking example."""

    # Get the overrides for the specified model
    args.hf_overrides = get_hf_overrides(args.model)

    # Initialize the LLM with all provided arguments
    llm = LLM(**vars(args))

    # Example query for demonstration
    query = "how much protein should a female eat?"

    # Example documents to be reranked based on relevance to the query
    documents = [
        "As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
        "Definition of summit for English Language Learners. : 1  the highest point of a mountain : the top of a mountain. : 2  the highest level. : 3  a meeting or series of meetings between the leaders of two or more governments.",
        "Calorie intake should not fall below 1,200 a day in women or 1,500 a day in men, except under the supervision of a health professional.",
    ]

    # Load the appropriate chat template for the selected model
    # The template formats query-document pairs for the reranking model
    chat_template = get_chat_template(args.model)

    # Score documents based on relevance to the query
    # The score method returns relevance scores for each document
    outputs = llm.score(query, documents, chat_template=chat_template)

    # Display the relevance scores
    # Higher scores indicate more relevant documents
    print("-" * 30)
    print([output.outputs.score for output in outputs])
    print("-" * 30)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Using Template Online[¶](#using-template-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501
"""
Example of using the rerank API with template.

This script demonstrates how to interact with a vLLM server running
a reranking model via the REST API.
Before running this script, start the vLLM server with one of the
supported reranking models using the commands below.

note:
    Some reranking models require special configuration overrides to work correctly
    with vLLM's score API.
    Reference: https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/qwen3_reranker_online.py
    Reference: https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/convert_model_to_seq_cls.py

run:
    vllm serve BAAI/bge-reranker-v2-gemma --hf_overrides '{"architectures": ["GemmaForSequenceClassification"],"classifier_from_token": ["Yes"],"method": "no_post_processing"}' --chat-template examples/pooling/score/template/bge-reranker-v2-gemma.jinja
    vllm serve tomaarsen/Qwen3-Reranker-0.6B-seq-cls --chat-template examples/pooling/score/template/qwen3_reranker.jinja
    vllm serve mixedbread-ai/mxbai-rerank-base-v2 --hf_overrides '{"architectures": ["Qwen2ForSequenceClassification"],"classifier_from_token": ["0", "1"], "method": "from_2_way_softmax"}' --chat-template examples/pooling/score/template/mxbai_rerank_v2.jinja
    vllm serve nvidia/llama-nemotron-rerank-1b-v2 --runner pooling --trust-remote-code --chat-template examples/pooling/score/template/nemotron-rerank.jinja
    vllm serve Qwen/Qwen3-Reranker-0.6B --runner pooling --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' --chat-template examples/pooling/score/template/qwen3_reranker.jinja
"""

importjson

importrequests

# URL of the vLLM server's rerank endpoint
# Default vLLM server runs on localhost port 8000
url = "http://127.0.0.1:8000/rerank"

# HTTP headers for the request
headers = {"accept": "application/json", "Content-Type": "application/json"}

# Example query & documents
query = "how much protein should a female eat?"
documents = [
    "As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
    "Definition of summit for English Language Learners. : 1  the highest point of a mountain : the top of a mountain. : 2  the highest level. : 3  a meeting or series of meetings between the leaders of two or more governments.",
    "Calorie intake should not fall below 1,200 a day in women or 1,500 a day in men, except under the supervision of a health professional.",
]

# Request payload for the rerank API
data = {
    "model": "nvidia/llama-nemotron-rerank-1b-v2",  # Model to use for reranking
    "query": query,  # The query to score documents against
    "documents": documents,  # List of documents to be scored
}


defmain():
"""Main function to send a rerank request to the vLLM server.

    This function sends a POST request to the /rerank endpoint with
    the query and documents, then prints the relevance scores.
    """
    # Send POST request to the vLLM server's rerank endpoint
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful!")
        # Pretty print the JSON response containing relevance scores
        # The response includes scores for each document's relevance to the query
        print(json.dumps(response.json(), indent=2))
    else:
        # Handle request failure
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    main()
```

## Vision Rerank API Online[¶](#vision-rerank-api-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501

"""
Example Python client for multimodal rerank API which is compatible with
Jina and Cohere https://jina.ai/reranker

Run `vllm serve <model> --runner pooling` to start up the server in vLLM.
e.g.
    vllm serve jinaai/jina-reranker-m0 --runner pooling

    vllm serve Qwen/Qwen3-VL-Reranker-2B \
        --runner pooling \
        --max-model-len 4096 \
        --hf_overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \
        --chat-template examples/pooling/score/template/qwen3_vl_reranker.jinja
"""

importargparse
importpprint

importrequests

fromvllm.multimodal.utilsimport encode_image_url, fetch_image

query = "A woman playing with her dog on a beach at sunset."
document = (
    "A woman shares a joyful moment with her golden retriever on a sun-drenched beach at sunset, "
    "as the dog offers its paw in a heartwarming display of companionship and trust."
)
image_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"
video_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/draw.mp4"
documents = [
    {
        "type": "text",
        "text": document,
    },
    {
        "type": "image_url",
        "image_url": {"url": image_url},
    },
    {
        "type": "image_url",
        "image_url": {"url": encode_image_url(fetch_image(image_url))},
    },
    {
        "type": "video_url",
        "video_url": {"url": video_url},
    },
]


defparse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    return parser.parse_args()


defmain(args):
    base_url = f"http://{args.host}:{args.port}"
    models_url = base_url + "/v1/models"
    rerank_url = base_url + "/rerank"

    response = requests.get(models_url)
    model = response.json()["data"][0]["id"]

    print("Query: string & Document: list of string")
    prompt = {"model": model, "query": query, "documents": [document]}
    response = requests.post(rerank_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: text")
    prompt = {"model": model, "query": query, "documents": {"content": [documents[0]]}}
    response = requests.post(rerank_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: image url")
    prompt = {
        "model": model,
        "query": query,
        "documents": {"content": [documents[1]]},
    }
    response = requests.post(rerank_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: image base64")
    prompt = {
        "model": model,
        "query": query,
        "documents": {"content": [documents[2]]},
    }
    response = requests.post(rerank_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: video url")
    prompt = {
        "model": model,
        "query": query,
        "documents": {"content": [documents[3]]},
    }
    response = requests.post(rerank_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: text + image url")
    prompt = {
        "model": model,
        "query": query,
        "documents": {"content": [documents[0], documents[1]]},
    }
    response = requests.post(rerank_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: list")
    prompt = {
        "model": model,
        "query": query,
        "documents": [
            document,
            {"content": [documents[0]]},
            {"content": [documents[1]]},
            {"content": [documents[0], documents[1]]},
        ],
    }
    response = requests.post(rerank_url, json=prompt)
    pprint.pprint(response.json())


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Vision Reranker Offline[¶](#vision-reranker-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This example shows how to use vLLM for running offline inference with
vision language reranker models for multimodal scoring tasks.

Vision language rerankers score the relevance between a text query and
multimodal documents (text + images/videos).
"""

fromargparseimport Namespace
fromcollections.abcimport Callable
frompathlibimport Path
fromtypingimport NamedTuple

fromvllmimport LLM, EngineArgs
fromvllm.multimodal.utilsimport encode_image_url, fetch_image
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser

TEMPLATE_HOME = Path(__file__).parent / "template"


query = "A woman playing with her dog on a beach at sunset."
document = (
    "A woman shares a joyful moment with her golden retriever on a sun-drenched "
    "beach at sunset, as the dog offers its paw in a heartwarming display of "
    "companionship and trust."
)
image_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"
video_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/draw.mp4"
documents = [
    {
        "type": "text",
        "text": document,
    },
    {
        "type": "image_url",
        "image_url": {"url": image_url},
    },
    {
        "type": "image_url",
        "image_url": {"url": encode_image_url(fetch_image(image_url))},
    },
    {
        "type": "video_url",
        "video_url": {"url": video_url},
    },
]


classRerankModelData(NamedTuple):
    engine_args: EngineArgs
    chat_template: str | None = None
    modality: set[str] = {}


defrun_jinavl_reranker() -> RerankModelData:
    engine_args = EngineArgs(
        model="jinaai/jina-reranker-m0",
        runner="pooling",
        max_model_len=32768,
        trust_remote_code=True,
        mm_processor_kwargs={
            "min_pixels": 3136,
            "max_pixels": 602112,
        },
    )
    return RerankModelData(engine_args=engine_args, modality={"image"})


defrun_qwen3_vl_reranker() -> RerankModelData:
    engine_args = EngineArgs(
        model="Qwen/Qwen3-VL-Reranker-2B",
        runner="pooling",
        max_model_len=16384,
        # HuggingFace model configuration overrides required for compatibility
        hf_overrides={
            # Manually route to sequence classification architecture
            # This tells vLLM to use Qwen3VLForSequenceClassification instead of
            # the default Qwen3VLForConditionalGeneration
            "architectures": ["Qwen3VLForSequenceClassification"],
            # Specify which token logits to extract from the language model head
            # The original reranker uses "no" and "yes" token logits for scoring
            "classifier_from_token": ["no", "yes"],
            # Enable special handling for original Qwen3-Reranker models
            # This flag triggers conversion logic that transforms the two token
            # vectors into a single classification vector
            "is_original_qwen3_reranker": True,
        },
    )
    chat_template_path = "qwen3_vl_reranker.jinja"
    chat_template = (TEMPLATE_HOME / chat_template_path).read_text()
    return RerankModelData(
        engine_args=engine_args,
        chat_template=chat_template,
        modality={"image", "video"},
    )


model_example_map: dict[str, Callable[[], RerankModelData]] = {
    "jinavl_reranker": run_jinavl_reranker,
    "qwen3_vl_reranker": run_qwen3_vl_reranker,
}


defparse_args():
    parser = FlexibleArgumentParser(
        description="Demo on using vLLM for offline inference with "
        "vision language reranker models for multimodal scoring tasks."
    )
    parser.add_argument(
        "--model-name",
        "-m",
        type=str,
        default="jinavl_reranker",
        choices=model_example_map.keys(),
        help="The name of the reranker model.",
    )
    return parser.parse_args()


defmain(args: Namespace):
    # Run the selected reranker model
    model_request = model_example_map[args.model_name]()
    engine_args = model_request.engine_args

    llm = LLM.from_engine_args(engine_args)

    print("Query: string & Document: string")
    outputs = llm.score(query, document)
    print("Relevance scores:", [output.outputs.score for output in outputs])

    print("Query: string & Document: text")
    outputs = llm.score(
        query, {"content": [documents[0]]}, chat_template=model_request.chat_template
    )
    print("Relevance scores:", [output.outputs.score for output in outputs])

    print("Query: string & Document: image url")
    outputs = llm.score(
        query, {"content": [documents[1]]}, chat_template=model_request.chat_template
    )
    print("Relevance scores:", [output.outputs.score for output in outputs])

    print("Query: string & Document: image base64")
    outputs = llm.score(
        query, {"content": [documents[2]]}, chat_template=model_request.chat_template
    )
    print("Relevance scores:", [output.outputs.score for output in outputs])

    if "video" in model_request.modality:
        print("Query: string & Document: video url")
        outputs = llm.score(
            query,
            {"content": [documents[3]]},
            chat_template=model_request.chat_template,
        )
        print("Relevance scores:", [output.outputs.score for output in outputs])

    print("Query: string & Document: text + image url")
    outputs = llm.score(
        query,
        {"content": [documents[0], documents[1]]},
        chat_template=model_request.chat_template,
    )
    print("Relevance scores:", [output.outputs.score for output in outputs])

    print("Query: string & Document: list")
    outputs = llm.score(
        query,
        [
            document,
            {"content": [documents[0]]},
            {"content": [documents[1]]},
            {"content": [documents[0], documents[1]]},
        ],
        chat_template=model_request.chat_template,
    )
    print("Relevance scores:", [output.outputs.score for output in outputs])


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Vision Score API Online[¶](#vision-score-api-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501

"""
Example online usage of Score API.

Run `vllm serve <model> --runner pooling` to start up the server in vLLM.
e.g.
    vllm serve jinaai/jina-reranker-m0 --runner pooling

    vllm serve Qwen/Qwen3-VL-Reranker-2B \
        --runner pooling \
        --max-model-len 4096 \
        --hf_overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \
        --chat-template examples/pooling/score/template/qwen3_vl_reranker.jinja
"""

importargparse
importpprint

importrequests

fromvllm.multimodal.utilsimport encode_image_url, fetch_image

query = "A woman playing with her dog on a beach at sunset."
document = (
    "A woman shares a joyful moment with her golden retriever on a sun-drenched beach at sunset, "
    "as the dog offers its paw in a heartwarming display of companionship and trust."
)
image_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"
video_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/draw.mp4"
documents = [
    {
        "type": "text",
        "text": document,
    },
    {
        "type": "image_url",
        "image_url": {"url": image_url},
    },
    {
        "type": "image_url",
        "image_url": {"url": encode_image_url(fetch_image(image_url))},
    },
    {
        "type": "video_url",
        "video_url": {"url": video_url},
    },
]


defparse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    return parser.parse_args()


defmain(args):
    base_url = f"http://{args.host}:{args.port}"
    models_url = base_url + "/v1/models"
    score_url = base_url + "/score"

    response = requests.get(models_url)
    model = response.json()["data"][0]["id"]

    print("Query: string & Document: string")
    prompt = {"model": model, "queries": query, "documents": document}
    response = requests.post(score_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: text")
    prompt = {
        "model": model,
        "queries": query,
        "documents": {"content": [documents[0]]},
    }
    response = requests.post(score_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: image url")
    prompt = {
        "model": model,
        "queries": query,
        "documents": {"content": [documents[1]]},
    }
    response = requests.post(score_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: image base64")
    prompt = {
        "model": model,
        "queries": query,
        "documents": {"content": [documents[2]]},
    }
    response = requests.post(score_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: video url")
    prompt = {
        "model": model,
        "queries": query,
        "documents": {"content": [documents[3]]},
    }
    response = requests.post(score_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: text + image url")
    prompt = {
        "model": model,
        "queries": query,
        "documents": {"content": [documents[0], documents[1]]},
    }
    response = requests.post(score_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: string & Document: list")
    prompt = {
        "model": model,
        "queries": query,
        "documents": [
            document,
            {"content": [documents[0]]},
            {"content": [documents[1]]},
            {"content": [documents[0], documents[1]]},
        ],
    }
    response = requests.post(score_url, json=prompt)
    pprint.pprint(response.json())

    print("Query: list & Document: list")
    data = [
        document,
        {"content": [documents[0]]},
        {"content": [documents[1]]},
        {"content": [documents[0], documents[1]]},
    ]
    prompt = {
        "model": model,
        "queries": data,
        "documents": data,
    }
    response = requests.post(score_url, json=prompt)
    pprint.pprint(response.json())


if __name__ == "__main__":
    args = parse_args()
    main(args)
```