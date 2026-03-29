---
title: OpenAI APIs - Vision — SGLang
url: https://docs.sglang.io/basic_usage/openai_api_vision.html
source: crawler
fetched_at: 2026-02-04T08:47:29.157249989-03:00
rendered_js: false
word_count: 488
summary: This tutorial explains how to use SGLang's OpenAI-compatible vision APIs to serve and query vision language models locally. It provides instructions for launching the server and sending multimodal requests via cURL.
tags:
    - sglang
    - vision-language-models
    - openai-api
    - vlm
    - inference
    - multimodal
category: tutorial
---

## OpenAI APIs - Vision[#](#OpenAI-APIs---Vision "Link to this heading")

SGLang provides OpenAI-compatible APIs to enable a smooth transition from OpenAI services to self-hosted local models. A complete reference for the API is available in the [OpenAI API Reference](https://platform.openai.com/docs/guides/vision). This tutorial covers the vision APIs for vision language models.

SGLang supports various vision language models such as Llama 3.2, LLaVA-OneVision, Qwen2.5-VL, Gemma3 and [more](https://docs.sglang.io/supported_models/multimodal_language_models.html).

As an alternative to the OpenAI API, you can also use the [SGLang offline engine](https://github.com/sgl-project/sglang/blob/main/examples/runtime/engine/offline_batch_inference_vlm.py).

## Launch A Server[#](#Launch-A-Server "Link to this heading")

Launch the server in your terminal and wait for it to initialize.

```
fromsglang.test.doc_patchimport launch_server_cmd
fromsglang.utilsimport wait_for_server, print_highlight, terminate_process

vision_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model-path Qwen/Qwen2.5-VL-7B-Instruct --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:26:47] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:47] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:47] INFO utils.py:164: NumExpr defaulting to 16 threads.
```

```
[2026-02-04 11:26:52] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:52] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:52] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:54] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:26:54] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:26:57] Ignore import error when loading sglang.srt.multimodal.processors.glm4v: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:26:57] Ignore import error when loading sglang.srt.multimodal.processors.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:26:57] Ignore import error when loading sglang.srt.multimodal.processors.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
[2026-02-04 11:27:01] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:01] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:01] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:27:01] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:01] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:01] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:27:07] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:07] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:07] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:27:07] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  20% Completed | 1/5 [00:02<00:08,  2.17s/it]
Loading safetensors checkpoint shards:  40% Completed | 2/5 [00:03<00:04,  1.62s/it]
Loading safetensors checkpoint shards:  60% Completed | 3/5 [00:06<00:04,  2.13s/it]
Loading safetensors checkpoint shards:  80% Completed | 4/5 [00:08<00:02,  2.17s/it]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:09<00:00,  1.69s/it]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:09<00:00,  1.84s/it]

Capturing batches (bs=1 avail_mem=61.33 GB): 100%|██████████| 3/3 [00:00<00:00,  3.28it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

## Using cURL[#](#Using-cURL "Link to this heading")

Once the server is up, you can send test requests using curl or requests.

```
importsubprocess

curl_command = f"""
curl -s http://localhost:{port}/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -d '{{
    "model": "Qwen/Qwen2.5-VL-7B-Instruct",
    "messages": [
{{
        "role": "user",
        "content": [
{{
            "type": "text",
            "text": "What’s in this image?"
}},
{{
            "type": "image_url",
            "image_url": {{
              "url": "https://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true"
}}
}}
        ]
}}
    ],
    "max_tokens": 300
}}'
"""

response = subprocess.check_output(curl_command, shell=True).decode()
print_highlight(response)


response = subprocess.check_output(curl_command, shell=True).decode()
print_highlight(response)
```

**{"id":"40b7a4cb274c4e678a8ffb62ec27424f","object":"chat.completion","created":1770204448,"model":"Qwen/Qwen2.5-VL-7B-Instruct","choices":\[{"index":0,"message":{"role":"assistant","content":"The image shows a man standing on the back of a yellow taxi, using an iron to iron a pair of blue jeans. The taxi is parked on a city street, and there are other taxis and buildings in the background. The man appears to be balancing on the taxi's rear bumper while ironing the jeans.","reasoning\_content":null,"tool\_calls":null},"logprobs":null,"finish\_reason":"stop","matched\_stop":151645}],"usage":{"prompt\_tokens":307,"total\_tokens":371,"completion\_tokens":64,"prompt\_tokens\_details":null,"reasoning\_tokens":0},"metadata":{"weight\_version":"default"}}**

**{"id":"6ffa3696eee748d6b2cfbb70b6e6358b","object":"chat.completion","created":1770204449,"model":"Qwen/Qwen2.5-VL-7B-Instruct","choices":\[{"index":0,"message":{"role":"assistant","content":"The image shows a man standing on the back of a yellow taxi, using an iron to iron a pair of blue jeans. The taxi is parked on a city street, and there are other taxis and buildings in the background. The man appears to be balancing on the taxi's rear bumper while ironing the jeans.","reasoning\_content":null,"tool\_calls":null},"logprobs":null,"finish\_reason":"stop","matched\_stop":151645}],"usage":{"prompt\_tokens":307,"total\_tokens":371,"completion\_tokens":64,"prompt\_tokens\_details":null,"reasoning\_tokens":0},"metadata":{"weight\_version":"default"}}**

## Using Python Requests[#](#Using-Python-Requests "Link to this heading")

```
importrequests

url = f"http://localhost:{port}/v1/chat/completions"

data = {
    "model": "Qwen/Qwen2.5-VL-7B-Instruct",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true"
                    },
                },
            ],
        }
    ],
    "max_tokens": 300,
}

response = requests.post(url, json=data)
print_highlight(response.text)
```

**{"id":"6f4d0814fdba44779b88700c0880d2d8","object":"chat.completion","created":1770204450,"model":"Qwen/Qwen2.5-VL-7B-Instruct","choices":\[{"index":0,"message":{"role":"assistant","content":"The image shows a man standing on the back of a yellow taxi, using an iron to iron a pair of blue jeans. The taxi is parked on a city street, and there are other taxis and buildings in the background. The man appears to be balancing on the taxi's rear bumper while ironing the jeans.","reasoning\_content":null,"tool\_calls":null},"logprobs":null,"finish\_reason":"stop","matched\_stop":151645}],"usage":{"prompt\_tokens":307,"total\_tokens":371,"completion\_tokens":64,"prompt\_tokens\_details":null,"reasoning\_tokens":0},"metadata":{"weight\_version":"default"}}**

## Using OpenAI Python Client[#](#Using-OpenAI-Python-Client "Link to this heading")

```
fromopenaiimport OpenAI

client = OpenAI(base_url=f"http://localhost:{port}/v1", api_key="None")

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-VL-7B-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in this image?",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true"
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print_highlight(response.choices[0].message.content)
```

**The image shows a man standing on the back of a yellow taxi, using an iron to iron a piece of clothing. The taxi is parked on a city street, and there are other taxis and buildings in the background. The man appears to be balancing on the taxi's rear bumper while ironing, which is an unusual and somewhat humorous scene.**

## Multiple-Image Inputs[#](#Multiple-Image-Inputs "Link to this heading")

The server also supports multiple images and interleaved text and images if the model supports it.

```
fromopenaiimport OpenAI

client = OpenAI(base_url=f"http://localhost:{port}/v1", api_key="None")

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-VL-7B-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true",
                    },
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://raw.githubusercontent.com/sgl-project/sglang/main/assets/logo.png",
                    },
                },
                {
                    "type": "text",
                    "text": "I have two very different images. They are not related at all. "
                    "Please describe the first image in one sentence, and then describe the second image in another sentence.",
                },
            ],
        }
    ],
    temperature=0,
)

print_highlight(response.choices[0].message.content)
```

**The first image shows a man ironing clothes on the back of a yellow taxi in an urban setting. The second image is a stylized logo featuring the letters "SGL" in orange with a book and a computer icon as part of the design.**

```
terminate_process(vision_process)
```