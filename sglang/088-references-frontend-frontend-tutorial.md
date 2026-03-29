---
title: SGLang Frontend Language — SGLang
url: https://docs.sglang.io/references/frontend/frontend_tutorial.html
source: crawler
fetched_at: 2026-02-04T08:48:21.359463713-03:00
rendered_js: false
word_count: 715
summary: This document explains how to use the SGLang frontend language to define structured prompts and manage LLM interactions through a dedicated runtime server.
tags:
    - sglang
    - structured-prompting
    - llm-inference
    - python-api
    - prompt-engineering
category: tutorial
---

## SGLang Frontend Language[#](#SGLang-Frontend-Language "Link to this heading")

SGLang frontend language can be used to define simple and easy prompts in a convenient, structured way.

## Launch A Server[#](#Launch-A-Server "Link to this heading")

Launch the server in your terminal and wait for it to initialize.

```
fromsglangimport assistant_begin, assistant_end
fromsglangimport assistant, function, gen, system, user
fromsglangimport image
fromsglangimport RuntimeEndpoint
fromsglang.lang.apiimport set_default_backend
fromsglang.srt.utilsimport load_image
fromsglang.test.doc_patchimport launch_server_cmd
fromsglang.utilsimport print_highlight, terminate_process, wait_for_server

server_process, port = launch_server_cmd(
    "python -m sglang.launch_server --model-path Qwen/Qwen2.5-7B-Instruct --host 0.0.0.0 --log-level warning"
)

wait_for_server(f"http://localhost:{port}")
print(f"Server started on http://localhost:{port}")
```

```
[2026-02-04 11:27:23] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:23] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:23] INFO utils.py:164: NumExpr defaulting to 16 threads.
```

```
[2026-02-04 11:27:29] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:29] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:29] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:27:31] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:27:31] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:27:38] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:38] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:38] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:38] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:38] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:27:38] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:27:44] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:44] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:44] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:27:44] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:02,  1.21it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:01<00:01,  1.16it/s]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:02<00:00,  1.13it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.18it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.17it/s]

Capturing batches (bs=1 avail_mem=62.73 GB): 100%|██████████| 3/3 [00:00<00:00,  4.51it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
Server started on http://localhost:38850
```

Set the default backend. Note: Besides the local server, you may use also `OpenAI` or other API endpoints.

```
set_default_backend(RuntimeEndpoint(f"http://localhost:{port}"))
```

```
[2026-02-04 11:27:56] Endpoint '/get_model_info' is deprecated and will be removed in a future version. Please use '/model_info' instead.
```

## Basic Usage[#](#Basic-Usage "Link to this heading")

The most simple way of using SGLang frontend language is a simple question answer dialog between a user and an assistant.

```
@function
defbasic_qa(s, question):
    s += system(f"You are a helpful assistant than can answer questions.")
    s += user(question)
    s += assistant(gen("answer", max_tokens=512))
```

```
state = basic_qa("List 3 countries and their capitals.")
print_highlight(state["answer"])
```

**Certainly! Here are three countries along with their respective capitals:**

**1. Japan - Tokyo**  
**2. France - Paris**  
**3. Brazil - Brasília**

## Multi-turn Dialog[#](#Multi-turn-Dialog "Link to this heading")

SGLang frontend language can also be used to define multi-turn dialogs.

```
@function
defmulti_turn_qa(s):
    s += system(f"You are a helpful assistant than can answer questions.")
    s += user("Please give me a list of 3 countries and their capitals.")
    s += assistant(gen("first_answer", max_tokens=512))
    s += user("Please give me another list of 3 countries and their capitals.")
    s += assistant(gen("second_answer", max_tokens=512))
    return s


state = multi_turn_qa()
print_highlight(state["first_answer"])
print_highlight(state["second_answer"])
```

**Sure! Here is a list of three countries along with their capitals:**

**1. \*\*France\** - Paris**  
**2. \*\*Germany\** - Berlin**  
**3. \*\*Italy\** - Rome**

**Certainly! Here is another list of three countries along with their capitals:**

**1. \*\*Spain\** - Madrid**  
**2. \*\*Canada\** - Ottawa**  
**3. \*\*Australia\** - Canberra**

## Control flow[#](#Control-flow "Link to this heading")

You may use any Python code within the function to define more complex control flows.

```
@function
deftool_use(s, question):
    s += assistant(
        "To answer this question: "
        + question
        + ". I need to use a "
        + gen("tool", choices=["calculator", "search engine"])
        + ". "
    )

    if s["tool"] == "calculator":
        s += assistant("The math expression is: " + gen("expression"))
    elif s["tool"] == "search engine":
        s += assistant("The key word to search is: " + gen("word"))


state = tool_use("What is 2 * 2?")
print_highlight(state["tool"])
print_highlight(state["expression"])
```

**2 * 2.**

**You don't need a calculator for this problem, but I can compute it for you.**

**2 * 2 = 4**

## Parallelism[#](#Parallelism "Link to this heading")

Use `fork` to launch parallel prompts. Because `sgl.gen` is non-blocking, the for loop below issues two generation calls in parallel.

```
@function
deftip_suggestion(s):
    s += assistant(
        "Here are two tips for staying healthy: "
        "1. Balanced Diet. 2. Regular Exercise.\n\n"
    )

    forks = s.fork(2)
    for i, f in enumerate(forks):
        f += assistant(
            f"Now, expand tip {i+1} into a paragraph:\n"
            + gen("detailed_tip", max_tokens=256, stop="\n\n")
        )

    s += assistant("Tip 1:" + forks[0]["detailed_tip"] + "\n")
    s += assistant("Tip 2:" + forks[1]["detailed_tip"] + "\n")
    s += assistant(
        "To summarize the above two tips, I can say:\n" + gen("summary", max_tokens=512)
    )


state = tip_suggestion()
print_highlight(state["summary"])
```

**1. \*\*Balanced Diet\*\*: Eating a variety of nutritious foods ensures that your body receives all the necessary vitamins, minerals, and nutrients it needs. Focus on fruits, vegetables, whole grains, lean proteins, and healthy fats while limiting processed foods, sugars, and saturated fats. Staying hydrated is also crucial.**

**2. \*\*Regular Exercise\*\*: Engage in at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity each week, plus strength training exercises at least two days a week. Choose activities you enjoy to keep exercise sustainable and enjoyable.**

**This combination of a balanced diet and regular exercise is a great foundation for maintaining overall health and well-being.**

## Constrained Decoding[#](#Constrained-Decoding "Link to this heading")

Use `regex` to specify a regular expression as a decoding constraint. This is only supported for local models.

```
@function
defregular_expression_gen(s):
    s += user("What is the IP address of the Google DNS servers?")
    s += assistant(
        gen(
            "answer",
            temperature=0,
            regex=r"((25[0-5]|2[0-4]\d|[01]?\d\d?).){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)",
        )
    )


state = regular_expression_gen()
print_highlight(state["answer"])
```

Use `regex` to define a `JSON` decoding schema.

```
character_regex = (
r"""\{\n"""
    + r"""    "name": "[\w\d\s]{1,16}",\n"""
    + r"""    "house": "(Gryffindor|Slytherin|Ravenclaw|Hufflepuff)",\n"""
    + r"""    "blood status": "(Pure-blood|Half-blood|Muggle-born)",\n"""
    + r"""    "occupation": "(student|teacher|auror|ministry of magic|death eater|order of the phoenix)",\n"""
    + r"""    "wand": \{\n"""
    + r"""        "wood": "[\w\d\s]{1,16}",\n"""
    + r"""        "core": "[\w\d\s]{1,16}",\n"""
    + r"""        "length": [0-9]{1,2}\.[0-9]{0,2}\n"""
    + r"""    \},\n"""
    + r"""    "alive": "(Alive|Deceased)",\n"""
    + r"""    "patronus": "[\w\d\s]{1,16}",\n"""
    + r"""    "bogart": "[\w\d\s]{1,16}"\n"""
    + r"""\}"""
)


@function
defcharacter_gen(s, name):
    s += user(
        f"{name} is a character in Harry Potter. Please fill in the following information about this character."
    )
    s += assistant(gen("json_output", max_tokens=256, regex=character_regex))


state = character_gen("Harry Potter")
print_highlight(state["json_output"])
```

**{**  
**"name": "Harry Potter",**  
**"house": "Gryffindor",**  
**"blood status": "Half-blood",**  
**"occupation": "student",**  
**"wand": {**  
**"wood": "Willow",**  
**"core": "Tail hair of a G",**  
**"length": 11.0**  
**},**  
**"alive": "Alive",**  
**"patronus": "Stag",**  
**"bogart": "Dementors"**  
**}**

## Batching[#](#Batching "Link to this heading")

Use `run_batch` to run a batch of prompts.

```
@function
deftext_qa(s, question):
    s += user(question)
    s += assistant(gen("answer", stop="\n"))


states = text_qa.run_batch(
    [
        {"question": "What is the capital of the United Kingdom?"},
        {"question": "What is the capital of France?"},
        {"question": "What is the capital of Japan?"},
    ],
    progress_bar=True,
)

for i, state in enumerate(states):
    print_highlight(f"Answer {i+1}: {states[i]['answer']}")
```

```
100%|██████████| 3/3 [00:00<00:00, 34.92it/s]
```

**Answer 1: The capital of the United Kingdom is London.**

**Answer 2: The capital of France is Paris.**

**Answer 3: The capital of Japan is Tokyo.**

## Streaming[#](#Streaming "Link to this heading")

Use `stream` to stream the output to the user.

```
@function
deftext_qa(s, question):
    s += user(question)
    s += assistant(gen("answer", stop="\n"))


state = text_qa.run(
    question="What is the capital of France?", temperature=0.1, stream=True
)

for out in state.text_iter():
    print(out, end="", flush=True)
```

```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
What is the capital of France?<|im_end|>
<|im_start|>assistant
The capital of France is Paris.<|im_end|>
```

## Complex Prompts[#](#Complex-Prompts "Link to this heading")

You may use `{system|user|assistant}_{begin|end}` to define complex prompts.

```
@function
defchat_example(s):
    s += system("You are a helpful assistant.")
    # Same as: s += s.system("You are a helpful assistant.")

    with s.user():
        s += "Question: What is the capital of France?"

    s += assistant_begin()
    s += "Answer: " + gen("answer", max_tokens=100, stop="\n")
    s += assistant_end()


state = chat_example()
print_highlight(state["answer"])
```

**The capital of France is Paris.**

```
terminate_process(server_process)
```

## Multi-modal Generation[#](#Multi-modal-Generation "Link to this heading")

You may use SGLang frontend language to define multi-modal prompts. See [here](https://docs.sglang.io/supported_models/generative_models.html) for supported models.

```
server_process, port = launch_server_cmd(
    "python -m sglang.launch_server --model-path Qwen/Qwen2.5-VL-7B-Instruct --host 0.0.0.0 --log-level warning"
)

wait_for_server(f"http://localhost:{port}")
print(f"Server started on http://localhost:{port}")
```

```
[2026-02-04 11:28:06] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:06] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:06] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:28:09] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:28:09] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:28:12] Ignore import error when loading sglang.srt.multimodal.processors.glm4v: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:28:12] Ignore import error when loading sglang.srt.multimodal.processors.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:28:12] Ignore import error when loading sglang.srt.multimodal.processors.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
[2026-02-04 11:28:15] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:15] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:15] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:28:15] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:15] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:15] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:28:23] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:28:23] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:28:23] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:28:23] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  20% Completed | 1/5 [00:00<00:03,  1.08it/s]
Loading safetensors checkpoint shards:  40% Completed | 2/5 [00:01<00:02,  1.09it/s]
Loading safetensors checkpoint shards:  60% Completed | 3/5 [00:02<00:01,  1.08it/s]
Loading safetensors checkpoint shards:  80% Completed | 4/5 [00:03<00:00,  1.12it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:03<00:00,  1.46it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:03<00:00,  1.27it/s]

Capturing batches (bs=1 avail_mem=59.19 GB): 100%|██████████| 3/3 [00:01<00:00,  2.91it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
Server started on http://localhost:37477
```

```
set_default_backend(RuntimeEndpoint(f"http://localhost:{port}"))
```

```
[2026-02-04 11:28:37] Endpoint '/get_model_info' is deprecated and will be removed in a future version. Please use '/model_info' instead.
```

Ask a question about an image.

```
@function
defimage_qa(s, image_file, question):
    s += user(image(image_file) + question)
    s += assistant(gen("answer", max_tokens=256))


image_url = "https://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true"
image_bytes, _ = load_image(image_url)
state = image_qa(image_bytes, "What is in the image?")
print_highlight(state["answer"])
```

**The image shows a man ironing clothes while standing on the back of a yellow SUV. The SUV appears to be a luggage rack or cargo carry vehicle modified for this purpose, hence the term "Ironing SUV." The setting seems to be an urban street, possibly in a city with yellow taxis in the background. The man is wearing a yellow shirt and appears to be engaged in ironing the clothes that are laid out on a stand attached to the back of the SUV.**

```
terminate_process(server_process)
```