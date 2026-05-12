---
title: Token Embed - vLLM
url: https://docs.vllm.ai/en/latest/examples/pooling/token_embed/
source: sitemap
fetched_at: 2026-05-07T21:13:32.95614369-03:00
rendered_js: false
word_count: 332
summary: This document provides a guide and code example for using the vLLM Pooling API to perform multi-vector retrieval with the ColQwen3 model, demonstrating how to generate embeddings and compute cross-modal MaxSim scores.
tags:
    - vllm
    - pooling-api
    - multi-vector-retrieval
    - colqwen3
    - multimodal
    - maxsim
    - embedding-generation
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/token_embed.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/pooling/token\_embed](https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_embed).

## Colqwen3 Token Embed Online[¶](#colqwen3-token-embed-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501

"""
Example online usage of Pooling API for ColQwen3 multi-vector retrieval.

ColQwen3 is a multi-modal late interaction model based on Qwen3-VL that
produces per-token embeddings (320-dim, L2-normalized) for both text and
image inputs. Similarity is computed via MaxSim scoring.

This example mirrors the official TomoroAI inference code
(https://huggingface.co/TomoroAI/tomoro-colqwen3-embed-4b) but uses the
vLLM serving API instead of local HuggingFace model loading.

Start the server with:
    vllm serve TomoroAI/tomoro-colqwen3-embed-4b --max-model-len 4096

Then run this script:
    python colqwen3_token_embed_online.py
"""

importargparse
fromioimport BytesIO

importnumpyasnp
importpybase64asbase64
importrequests
fromPILimport Image

# ── Helpers ─────────────────────────────────────────────────


defpost_http_request(payload: dict, api_url: str) -> requests.Response:
    headers = {"User-Agent": "Test Client"}
    return requests.post(api_url, headers=headers, json=payload)


defload_image(url: str) -> Image.Image:
"""Download an image from URL (handles Wikimedia 403)."""
    for hdrs in ({}, {"User-Agent": "Mozilla/5.0 (compatible; ColQwen3-demo/1.0)"}):
        resp = requests.get(url, headers=hdrs, timeout=10)
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


defcompute_maxsim(q_emb: np.ndarray, d_emb: np.ndarray) -> float:
"""Compute ColBERT-style MaxSim score between query and document."""
    sim = q_emb @ d_emb.T
    return float(sim.max(axis=-1).sum())


# ── Encode functions ────────────────────────────────────────


defencode_queries(texts: list[str], model: str, api_url: str) -> list[np.ndarray]:
"""Encode text queries → list of multi-vector embeddings."""
    resp = post_http_request({"model": model, "input": texts}, api_url)
    return [np.array(item["data"]) for item in resp.json()["data"]]


defencode_images(image_urls: list[str], model: str, api_url: str) -> list[np.ndarray]:
"""Encode image documents → list of multi-vector embeddings.

    Images are sent via the chat-style `messages` field so that the
    vLLM multimodal processor handles them correctly.
    """
    embeddings = []
    for url in image_urls:
        print(f"  Loading: {url.split('/')[-1]}...")
        image = load_image(url)
        image_uri = encode_image_base64(image)
        resp = post_http_request(
            {
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "image_url", "image_url": {"url": image_uri}},
                            {"type": "text", "text": "Describe the image."},
                        ],
                    }
                ],
            },
            api_url,
        )
        result = resp.json()
        if resp.status_code != 200 or "data" not in result:
            print(f"    Error ({resp.status_code}): {str(result)[:200]}")
            continue
        embeddings.append(np.array(result["data"][0]["data"]))
    return embeddings


# ── Main ────────────────────────────────────────────────────


defparse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument(
        "--model",
        type=str,
        default="TomoroAI/tomoro-colqwen3-embed-4b",
    )
    return parser.parse_args()


defmain(args):
    pooling_url = f"http://{args.host}:{args.port}/pooling"
    score_url = f"http://{args.host}:{args.port}/score"
    model = args.model

    # Same sample data as the official TomoroAI example
    queries = [
        "Retrieve the city of Singapore",
        "Retrieve the city of Beijing",
        "Retrieve the city of London",
    ]
    image_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/2/27/Singapore_skyline_2022.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/6/61/Beijing_skyline_at_night.JPG",
        "https://upload.wikimedia.org/wikipedia/commons/4/49/London_skyline.jpg",
    ]

    # ── 1) Text query embeddings ────────────────────────────
    print("=" * 60)
    print("1. Encode text queries (multi-vector)")
    print("=" * 60)
    query_embeddings = encode_queries(queries, model, pooling_url)
    for i, emb in enumerate(query_embeddings):
        norm = float(np.linalg.norm(emb[0]))
        print(f'  Query {i}: {emb.shape}  (L2 norm: {norm:.4f})  "{queries[i]}"')

    # ── 2) Image document embeddings ────────────────────────
    print()
    print("=" * 60)
    print("2. Encode image documents (multi-vector)")
    print("=" * 60)
    doc_embeddings = encode_images(image_urls, model, pooling_url)
    for i, emb in enumerate(doc_embeddings):
        print(f"  Doc {i}:   {emb.shape}{image_urls[i].split('/')[-1]}")

    # ── 3) Cross-modal MaxSim scoring ───────────────────────
    if doc_embeddings:
        print()
        print("=" * 60)
        print("3. Cross-modal MaxSim scores (text queries × image docs)")
        print("=" * 60)
        # Header
        print(f"{'':>35s}", end="")
        for j in range(len(doc_embeddings)):
            print(f"  Doc {j:>2d}", end="")
        print()
        # Score matrix
        for i, q_emb in enumerate(query_embeddings):
            print(f"  {queries[i]:<33s}", end="")
            for j, d_emb in enumerate(doc_embeddings):
                score = compute_maxsim(q_emb, d_emb)
                print(f"  {score:6.2f}", end="")
            print()

    # ── 4) Text-only /score endpoint ────────────────────────
    print()
    print("=" * 60)
    print("4. Text-only late interaction scoring (/score endpoint)")
    print("=" * 60)
    text_query = "What is the capital of France?"
    text_docs = [
        "The capital of France is Paris.",
        "Berlin is the capital of Germany.",
        "Python is a programming language.",
    ]
    resp = post_http_request(
        {"model": model, "text_1": text_query, "text_2": text_docs},
        score_url,
    )
    print(f'  Query: "{text_query}"\n')
    for item in resp.json()["data"]:
        idx = item["index"]
        print(f"  Doc {idx} (score={item['score']:.4f}): {text_docs[idx]}")


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Jina Embeddings V4 Offline[¶](#jina-embeddings-v4-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

importtorch

fromvllmimport LLM
fromvllm.configimport PoolerConfig
fromvllm.inputsimport TextPrompt
fromvllm.multimodal.utilsimport fetch_image


defmain():
    # Initialize model
    model = LLM(
        model="jinaai/jina-embeddings-v4-vllm-text-matching",
        pooler_config=PoolerConfig(task="token_embed"),
        runner="pooling",
        max_model_len=1024,
        gpu_memory_utilization=0.8,
    )

    # Create text prompts
    text1 = "Ein wunderschöner Sonnenuntergang am Strand"
    text1_prompt = TextPrompt(prompt=f"Query: {text1}")

    text2 = "浜辺に沈む美しい夕日"
    text2_prompt = TextPrompt(prompt=f"Query: {text2}")

    # Create image prompt
    image = fetch_image(
        "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/eskimo.jpg"  # noqa: E501
    )
    image_prompt = TextPrompt(
        prompt="<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>Describe the image.<|im_end|>\n",  # noqa: E501
        multi_modal_data={"image": image},
    )

    # Encode all prompts
    prompts = [text1_prompt, text2_prompt, image_prompt]
    outputs = model.encode(prompts, pooling_task="token_embed")

    defget_embeddings(outputs):
        VISION_START_TOKEN_ID, VISION_END_TOKEN_ID = 151652, 151653

        embeddings = []
        for output in outputs:
            if VISION_START_TOKEN_ID in output.prompt_token_ids:
                # Gather only vision tokens
                img_start_pos = torch.where(
                    torch.tensor(output.prompt_token_ids) == VISION_START_TOKEN_ID
                )[0][0]
                img_end_pos = torch.where(
                    torch.tensor(output.prompt_token_ids) == VISION_END_TOKEN_ID
                )[0][0]
                embeddings_tensor = output.outputs.data.detach().clone()[
                    img_start_pos : img_end_pos + 1
                ]
            else:
                # Use all tokens for text-only prompts
                embeddings_tensor = output.outputs.data.detach().clone()

            # Pool and normalize embeddings
            pooled_output = (
                embeddings_tensor.sum(dim=0, dtype=torch.float32)
                / embeddings_tensor.shape[0]
            )
            embeddings.append(torch.nn.functional.normalize(pooled_output, dim=-1))
        return embeddings

    embeddings = get_embeddings(outputs)

    for embedding in embeddings:
        print(embedding.shape)


if __name__ == "__main__":
    main()
```

## Jina Reranker V3 Offline[¶](#jina-reranker-v3-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501

importtorch.nn.functionalasF

fromvllmimport LLM

query = "What are the health benefits of green tea?"
documents = [
    "Green tea contains antioxidants called catechins that may help reduce inflammation and protect cells from damage.",
    "El precio del café ha aumentado un 20% este año debido a problemas en la cadena de suministro.",
    "Studies show that drinking green tea regularly can improve brain function and boost metabolism.",
    "Basketball is one of the most popular sports in the United States.",
    "绿茶富含儿茶素等抗氧化剂，可以降低心脏病风险，还有助于控制体重。",
    "Le thé vert est riche en antioxydants et peut améliorer la fonction cérébrale.",
]


defmain():
    # Initialize model
    llm = LLM(
        model="jinaai/jina-reranker-v3",
        runner="pooling",
    )

    # Generate scores.
    outputs = llm.score(query, documents)

    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for document, output in zip(documents, outputs):
        score = output.outputs.score
        print(f"Pair: {[query,document]!r}\nScore: {score}")
        print("-" * 60)

    # Generate embeddings.
    # The JinaForRanking model concatenates docs first, then query.
    # Let's stay consistent with this novel design.
    outputs = llm.encode(documents + [query], pooling_task="token_embed")
    embeds = outputs[0].outputs.data.float()

    doc_embeds = embeds[:-1]
    query_embeds = embeds[-1]

    scores = F.cosine_similarity(query_embeds, doc_embeds)

    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for document, score in zip(documents, scores):
        print(f"Pair: {[query,document]!r}\nScore: {score}")
        print("-" * 60)


if __name__ == "__main__":
    main()
```

## Multi Vector Retrieval Offline[¶](#multi-vector-retrieval-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromargparseimport Namespace

fromvllmimport LLM, EngineArgs
fromvllm.configimport PoolerConfig
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defparse_args():
    parser = FlexibleArgumentParser()
    parser = EngineArgs.add_cli_args(parser)
    # Set example specific arguments
    parser.set_defaults(
        model="BAAI/bge-m3",
        pooler_config=PoolerConfig(task="token_embed"),
        runner="pooling",
        enforce_eager=True,
    )
    return parser.parse_args()


defmain(args: Namespace):
    # Sample prompts.
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]

    # Create an LLM.
    # You should pass runner="pooling" for embedding models
    llm = LLM(**vars(args))

    # Generate embedding for each token. The output is a list of PoolingRequestOutput.
    outputs = llm.encode(prompts, pooling_task="token_embed")

    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for prompt, output in zip(prompts, outputs):
        multi_vector = output.outputs.data
        print(multi_vector.shape)

    query = "What is the capital of France?"
    documents = [
        "The capital of Brazil is Brasilia.",
        "The capital of France is Paris.",
    ]
    # Generate scores.
    outputs = llm.score(query, documents)
    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for document, output in zip(documents, outputs):
        score = output.outputs.score
        print(f"Pair: {[query,document]!r}\nScore: {score}")
        print("-" * 60)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Multi Vector Retrieval Online[¶](#multi-vector-retrieval-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

"""
Example online usage of Pooling API for multi vector retrieval.

Run `vllm serve <model> --runner pooling`
to start up the server in vLLM. e.g.

vllm serve BAAI/bge-m3 --pooler-config.task token_embed
"""

importargparse
importpprint

importrequests
importtorch


defpost_http_request(prompt: dict, api_url: str) -> requests.Response:
    headers = {"User-Agent": "Test Client"}
    response = requests.post(api_url, headers=headers, json=prompt)
    return response


defparse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--model", type=str, default="BAAI/bge-m3")

    return parser.parse_args()


defmain(args):
    pooling_url = f"http://{args.host}:{args.port}/pooling"
    score_url = f"http://{args.host}:{args.port}/score"
    model_name = args.model

    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    prompt = {"model": model_name, "input": prompts}

    pooling_response = post_http_request(prompt=prompt, api_url=pooling_url)
    for output in pooling_response.json()["data"]:
        multi_vector = torch.tensor(output["data"])
        print(multi_vector.shape)

    queries = "What is the capital of France?"
    documents = [
        "The capital of Brazil is Brasilia.",
        "The capital of France is Paris.",
    ]
    prompt = {"model": model_name, "queries": queries, "documents": documents}
    score_response = post_http_request(prompt=prompt, api_url=score_url)
    print("\nPrompt when queries is string and documents is a list:")
    pprint.pprint(prompt)
    print("\nScore Response:")
    pprint.pprint(score_response.json())


if __name__ == "__main__":
    args = parse_args()
    main(args)
```