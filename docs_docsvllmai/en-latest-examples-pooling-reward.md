---
title: Reward - vLLM
url: https://docs.vllm.ai/en/latest/examples/pooling/reward/
source: sitemap
fetched_at: 2026-05-07T21:13:30.190626306-03:00
rendered_js: false
word_count: 263
summary: This document demonstrates how to utilize vLLM for reward modeling in both offline and online environments, covering both sequence-level and token-level classification tasks.
tags:
    - vllm
    - reward-models
    - pooling
    - offline-inference
    - online-serving
    - classification
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/reward.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/pooling/reward](https://github.com/vllm-project/vllm/tree/main/examples/pooling/reward).

## Sequence Reward Offline[¶](#sequence-reward-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

"""
Example offline usage of sequence reward models.

The key distinction between sequence classification and token classification
lies in their output granularity: sequence classification produces a single
result for an entire input sequence, whereas token classification yields a
result for each individual token within the sequence.
"""

fromargparseimport Namespace

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser
fromvllm.utils.print_utilsimport print_embeddings


defparse_args():
    parser = FlexibleArgumentParser()
    parser = EngineArgs.add_cli_args(parser)
    # Set example specific arguments
    parser.set_defaults(
        model="Skywork/Skywork-Reward-V2-Qwen3-0.6B",
        runner="pooling",
        enforce_eager=True,
        max_model_len=1024,
        trust_remote_code=True,
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
    # You should pass runner="pooling" for reward models
    llm = LLM(**vars(args))

    # Generate rewards. The output is a list of PoolingRequestOutput.
    # Use pooling_task="classify" for sequence reward models.
    outputs = llm.encode(prompts, pooling_task="classify")

    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for prompt, output in zip(prompts, outputs):
        rewards = output.outputs.data
        print(f"Prompt: {prompt!r}")
        print_embeddings(rewards.tolist(), prefix="Reward")
        print("-" * 60)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Sequence Reward Online[¶](#sequence-reward-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Example online usage of sequence reward models.

Run `vllm serve <model> --runner pooling`
to start up the server in vLLM. e.g.

vllm serve Skywork/Skywork-Reward-V2-Qwen3-0.6B

The key distinction between sequence classification and token classification
lies in their output granularity: sequence classification produces a single
result for an entire input sequence, whereas token classification yields a
result for each individual token within the sequence.
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

    return parser.parse_args()


defmain(args):
    base_url = f"http://{args.host}:{args.port}"
    models_url = base_url + "/v1/models"
    pooing_url = base_url + "/pooling"

    response = requests.get(models_url)
    model = response.json()["data"][0]["id"]

    # Input like Completions API
    prompt = {"model": model, "input": "vLLM is great!"}
    pooling_response = post_http_request(prompt=prompt, api_url=pooing_url)
    print("-" * 50)
    print("Pooling Response:")
    pprint.pprint(pooling_response.json())
    print("-" * 50)

    # Input like Chat API
    prompt = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": "vLLM is great!"}],
            }
        ],
    }
    pooling_response = post_http_request(prompt=prompt, api_url=pooing_url)
    print("Pooling Response:")
    pprint.pprint(pooling_response.json())
    print("-" * 50)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Token Reward Offline[¶](#token-reward-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

"""
Example offline usage of token reward models.

The key distinction between sequence classification and token classification
lies in their output granularity: sequence classification produces a single
result for an entire input sequence, whereas token classification yields a
result for each individual token within the sequence.
"""

fromargparseimport Namespace

fromvllmimport LLM, EngineArgs
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser
fromvllm.utils.print_utilsimport print_embeddings


defparse_args():
    parser = FlexibleArgumentParser()
    parser = EngineArgs.add_cli_args(parser)
    # Set example specific arguments
    parser.set_defaults(
        model="internlm/internlm2-1_8b-reward",
        runner="pooling",
        enforce_eager=True,
        max_model_len=1024,
        trust_remote_code=True,
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
    # You should pass runner="pooling" for reward models
    llm = LLM(**vars(args))

    # Generate rewards. The output is a list of PoolingRequestOutput.
    outputs = llm.encode(prompts, pooling_task="token_classify")

    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for prompt, output in zip(prompts, outputs):
        rewards = output.outputs.data
        print(f"Prompt: {prompt!r}")
        print_embeddings(rewards.tolist(), prefix="Reward")
        print("-" * 60)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Token Reward Online[¶](#token-reward-online "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Example online usage of token reward models.

Run `vllm serve <model> --runner pooling`
to start up the server in vLLM. e.g.

vllm serve internlm/internlm2-1_8b-reward --trust-remote-code

The key distinction between sequence classification and token classification
lies in their output granularity: sequence classification produces a single
result for an entire input sequence, whereas token classification yields a
result for each individual token within the sequence.
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

    return parser.parse_args()


defmain(args):
    base_url = f"http://{args.host}:{args.port}"
    models_url = base_url + "/v1/models"
    pooing_url = base_url + "/pooling"

    response = requests.get(models_url)
    model = response.json()["data"][0]["id"]

    # Input like Completions API
    prompt = {"model": model, "input": "vLLM is great!"}
    pooling_response = post_http_request(prompt=prompt, api_url=pooing_url)
    print("-" * 50)
    print("Pooling Response:")
    pprint.pprint(pooling_response.json())
    print("-" * 50)

    # Input like Chat API
    prompt = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": "vLLM is great!"}],
            }
        ],
    }
    pooling_response = post_http_request(prompt=prompt, api_url=pooing_url)
    print("Pooling Response:")
    pprint.pprint(pooling_response.json())
    print("-" * 50)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```