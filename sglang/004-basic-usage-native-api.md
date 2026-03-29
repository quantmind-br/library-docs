---
title: SGLang Native APIs — SGLang
url: https://docs.sglang.io/basic_usage/native_api.html
source: crawler
fetched_at: 2026-02-04T08:46:43.799826414-03:00
rendered_js: false
word_count: 1647
summary: This document outlines the native server APIs for SGLang Runtime, providing a comprehensive list of endpoints for model interaction and server management alongside instructions for launching and testing the server.
tags:
    - sglang
    - native-apis
    - llm-inference
    - rest-api
    - text-generation
    - server-management
category: api
---

## SGLang Native APIs[#](#SGLang-Native-APIs "Link to this heading")

Apart from the OpenAI compatible APIs, the SGLang Runtime also provides its native server APIs. We introduce the following APIs:

- `/generate` (text generation model)
- `/get_model_info`
- `/get_server_info`
- `/health`
- `/health_generate`
- `/flush_cache`
- `/update_weights`
- `/encode`(embedding model)
- `/v1/rerank`(cross encoder rerank model)
- `/v1/score`(decoder-only scoring)
- `/classify`(reward model)
- `/start_expert_distribution_record`
- `/stop_expert_distribution_record`
- `/dump_expert_distribution_record`
- `/tokenize`
- `/detokenize`
- A full list of these APIs can be found at [http\_server.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/entrypoints/http_server.py)

We mainly use `requests` to test these APIs in the following examples. You can also use `curl`.

## Launch A Server[#](#Launch-A-Server "Link to this heading")

```
fromsglang.test.doc_patchimport launch_server_cmd
fromsglang.utilsimport wait_for_server, print_highlight, terminate_process

server_process, port = launch_server_cmd(
    "python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct --host 0.0.0.0 --log-level warning"
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:26:33] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:33] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:33] INFO utils.py:164: NumExpr defaulting to 16 threads.
```

```
[2026-02-04 11:26:38] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:38] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:38] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:41] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:26:41] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:26:48] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:48] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:48] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:48] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:48] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:48] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:26:54] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:26:54] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:26:54] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:26:54] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.19it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.18it/s]

Capturing batches (bs=1 avail_mem=76.96 GB): 100%|██████████| 3/3 [00:00<00:00,  5.82it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

## Generate (text generation model)[#](#Generate-%28text-generation-model%29 "Link to this heading")

Generate completions. This is similar to the `/v1/completions` in OpenAI API. Detailed parameters can be found in the [sampling parameters](https://docs.sglang.io/basic_usage/sampling_params.html).

```
importrequests

url = f"http://localhost:{port}/generate"
data = {"text": "What is the capital of France?"}

response = requests.post(url, json=data)
print_highlight(response.json())
```

**{'text': ' Paris\\n\\nWhat is the answer? To find the capital of France, I will follow these steps:\\n\\n1. Recall the capital cities of other European countries\\n2. Identify France\\n3. Confirm that Paris is the capital\\n\\nStep 1: I know the capital cities of other European countries,\\nE.g., Rome, London, Madrid, Athens.\\n\\nStep 2: France is one of these European countries.\\nTherefore, we can identify the capital of France.\\n\\nStep 3: In France, the capital is Paris.\\n\\nTherefore, the answer is: Paris is the capital of France.', 'output\_ids': \[12095, 271, 3838, 374, 279, 4226, 30, 2014, 1477, 279, 6722, 315, 9625, 11, 358, 686, 1795, 1493, 7354, 1447, 16, 13, 79540, 279, 6722, 9720, 315, 1008, 7513, 5837, 198, 17, 13, 64547, 9625, 198, 18, 13, 33563, 429, 12095, 374, 279, 6722, 271, 8304, 220, 16, 25, 358, 1414, 279, 6722, 9720, 315, 1008, 7513, 5837, 345, 36, 1302, 2572, 21718, 11, 7148, 11, 24081, 11, 45826, 382, 8304, 220, 17, 25, 9625, 374, 825, 315, 1493, 7513, 5837, 624, 54815, 11, 582, 646, 10542, 279, 6722, 315, 9625, 382, 8304, 220, 18, 25, 758, 9625, 11, 279, 6722, 374, 12095, 382, 54815, 11, 279, 4226, 374, 25, 12095, 374, 279, 6722, 315, 9625, 13, 151643], 'meta\_info': {'id': 'ff84e1ecbeb44d5d8c0a2341ce02336e', 'finish\_reason': {'type': 'stop', 'matched': 151643}, 'prompt\_tokens': 7, 'weight\_version': 'default', 'total\_retractions': 0, 'completion\_tokens': 118, 'cached\_tokens': 0, 'cached\_tokens\_details': None, 'e2e\_latency': 0.26733851432800293, 'response\_sent\_to\_client\_ts': 1770204423.1871605}}**

## Get Model Info[#](#Get-Model-Info "Link to this heading")

Get the information of the model.

- `model_path`: The path/name of the model.
- `is_generation`: Whether the model is used as generation model or embedding model.
- `tokenizer_path`: The path/name of the tokenizer.
- `preferred_sampling_params`: The default sampling params specified via `--preferred-sampling-params`. `None` is returned in this example as we did not explicitly configure it in server args.
- `weight_version`: This field contains the version of the model weights. This is often used to track changes or updates to the model’s trained parameters.
- `has_image_understanding`: Whether the model has image-understanding capability.
- `has_audio_understanding`: Whether the model has audio-understanding capability.
- `model_type`: The model type from the HuggingFace config (e.g., “qwen2”, “llama”).
- `architectures`: The model architectures from the HuggingFace config (e.g., \[“Qwen2ForCausalLM”]).

```
url = f"http://localhost:{port}/get_model_info"

response = requests.get(url)
response_json = response.json()
print_highlight(response_json)
assert response_json["model_path"] == "qwen/qwen2.5-0.5b-instruct"
assert response_json["is_generation"] is True
assert response_json["tokenizer_path"] == "qwen/qwen2.5-0.5b-instruct"
assert response_json["preferred_sampling_params"] is None
assert response_json.keys() == {
    "model_path",
    "is_generation",
    "tokenizer_path",
    "preferred_sampling_params",
    "weight_version",
    "has_image_understanding",
    "has_audio_understanding",
    "model_type",
    "architectures",
}
```

```
[2026-02-04 11:27:03] Endpoint '/get_model_info' is deprecated and will be removed in a future version. Please use '/model_info' instead.
```

**{'model\_path': 'qwen/qwen2.5-0.5b-instruct', 'tokenizer\_path': 'qwen/qwen2.5-0.5b-instruct', 'is\_generation': True, 'preferred\_sampling\_params': None, 'weight\_version': 'default', 'has\_image\_understanding': False, 'has\_audio\_understanding': False, 'model\_type': 'qwen2', 'architectures': \['Qwen2ForCausalLM']}**

## Get Server Info[#](#Get-Server-Info "Link to this heading")

Gets the server information including CLI arguments, token limits, and memory pool sizes.

- Note: `get_server_info` merges the following deprecated endpoints:
  
  - `get_server_args`
  - `get_memory_pool_size`
  - `get_max_total_num_tokens`

```
url = f"http://localhost:{port}/get_server_info"

response = requests.get(url)
print_highlight(response.text)
```

```
[2026-02-04 11:27:03] Endpoint '/get_server_info' is deprecated and will be removed in a future version. Please use '/server_info' instead.
```

**{"model\_path":"qwen/qwen2.5-0.5b-instruct","tokenizer\_path":"qwen/qwen2.5-0.5b-instruct","tokenizer\_mode":"auto","tokenizer\_worker\_num":1,"skip\_tokenizer\_init":false,"load\_format":"auto","model\_loader\_extra\_config":"{}","trust\_remote\_code":false,"context\_length":null,"is\_embedding":false,"enable\_multimodal":null,"revision":null,"model\_impl":"auto","host":"0.0.0.0","port":33809,"fastapi\_root\_path":"","grpc\_mode":false,"skip\_server\_warmup":false,"warmups":null,"nccl\_port":null,"checkpoint\_engine\_wait\_weights\_before\_ready":false,"dtype":"auto","quantization":null,"quantization\_param\_path":null,"kv\_cache\_dtype":"auto","enable\_fp32\_lm\_head":false,"modelopt\_quant":null,"modelopt\_checkpoint\_restore\_path":null,"modelopt\_checkpoint\_save\_path":null,"modelopt\_export\_path":null,"quantize\_and\_serve":false,"rl\_quant\_profile":null,"mem\_fraction\_static":0.841,"max\_running\_requests":128,"max\_queued\_requests":null,"max\_total\_tokens":20480,"chunked\_prefill\_size":8192,"enable\_dynamic\_chunking":false,"max\_prefill\_tokens":16384,"prefill\_max\_requests":null,"schedule\_policy":"fcfs","enable\_priority\_scheduling":false,"abort\_on\_priority\_when\_disabled":false,"schedule\_low\_priority\_values\_first":false,"priority\_scheduling\_preemption\_threshold":10,"schedule\_conservativeness":1.0,"page\_size":1,"swa\_full\_tokens\_ratio":0.8,"disable\_hybrid\_swa\_memory":false,"radix\_eviction\_policy":"lru","enable\_prefill\_delayer":false,"prefill\_delayer\_max\_delay\_passes":30,"prefill\_delayer\_token\_usage\_low\_watermark":null,"prefill\_delayer\_forward\_passes\_buckets":null,"prefill\_delayer\_wait\_seconds\_buckets":null,"device":"cuda","tp\_size":1,"pp\_size":1,"pp\_max\_micro\_batch\_size":null,"pp\_async\_batch\_depth":0,"stream\_interval":1,"stream\_output":false,"random\_seed":107984454,"constrained\_json\_whitespace\_pattern":null,"constrained\_json\_disable\_any\_whitespace":false,"watchdog\_timeout":300,"soft\_watchdog\_timeout":300,"dist\_timeout":null,"download\_dir":null,"model\_checksum":null,"base\_gpu\_id":0,"gpu\_id\_step":1,"sleep\_on\_idle":false,"custom\_sigquit\_handler":null,"log\_level":"warning","log\_level\_http":null,"log\_requests":false,"log\_requests\_level":2,"log\_requests\_format":"text","log\_requests\_target":null,"uvicorn\_access\_log\_exclude\_prefixes":\[],"crash\_dump\_folder":null,"show\_time\_cost":false,"enable\_metrics":false,"enable\_metrics\_for\_all\_schedulers":false,"tokenizer\_metrics\_custom\_labels\_header":"x-custom-labels","tokenizer\_metrics\_allowed\_custom\_labels":null,"extra\_metric\_labels":null,"bucket\_time\_to\_first\_token":null,"bucket\_inter\_token\_latency":null,"bucket\_e2e\_request\_latency":null,"collect\_tokens\_histogram":false,"prompt\_tokens\_buckets":null,"generation\_tokens\_buckets":null,"gc\_warning\_threshold\_secs":0.0,"decode\_log\_interval":40,"enable\_request\_time\_stats\_logging":false,"kv\_events\_config":null,"enable\_trace":false,"otlp\_traces\_endpoint":"localhost:4317","export\_metrics\_to\_file":false,"export\_metrics\_to\_file\_dir":null,"api\_key":null,"admin\_api\_key":null,"served\_model\_name":"qwen/qwen2.5-0.5b-instruct","weight\_version":"default","chat\_template":null,"hf\_chat\_template\_name":null,"completion\_template":null,"file\_storage\_path":"sglang\_storage","enable\_cache\_report":false,"reasoning\_parser":null,"tool\_call\_parser":null,"tool\_server":null,"sampling\_defaults":"model","dp\_size":1,"load\_balance\_method":"round\_robin","dist\_init\_addr":null,"nnodes":1,"node\_rank":0,"json\_model\_override\_args":"{}","preferred\_sampling\_params":null,"enable\_lora":null,"enable\_lora\_overlap\_loading":null,"max\_lora\_rank":null,"lora\_target\_modules":null,"lora\_paths":null,"max\_loaded\_loras":null,"max\_loras\_per\_batch":8,"lora\_eviction\_policy":"lru","lora\_backend":"csgmv","max\_lora\_chunk\_size":16,"attention\_backend":"fa3","decode\_attention\_backend":null,"prefill\_attention\_backend":null,"sampling\_backend":"flashinfer","grammar\_backend":"xgrammar","mm\_attention\_backend":null,"fp8\_gemm\_runner\_backend":"auto","fp4\_gemm\_runner\_backend":"auto","nsa\_prefill\_backend":null,"nsa\_decode\_backend":null,"disable\_flashinfer\_autotune":false,"speculative\_algorithm":null,"speculative\_draft\_model\_path":null,"speculative\_draft\_model\_revision":null,"speculative\_draft\_load\_format":null,"speculative\_num\_steps":null,"speculative\_eagle\_topk":null,"speculative\_num\_draft\_tokens":null,"speculative\_accept\_threshold\_single":1.0,"speculative\_accept\_threshold\_acc":1.0,"speculative\_token\_map":null,"speculative\_attention\_mode":"prefill","speculative\_draft\_attention\_backend":null,"speculative\_moe\_runner\_backend":"auto","speculative\_moe\_a2a\_backend":null,"speculative\_draft\_model\_quantization":null,"speculative\_ngram\_min\_match\_window\_size":1,"speculative\_ngram\_max\_match\_window\_size":12,"speculative\_ngram\_min\_bfs\_breadth":1,"speculative\_ngram\_max\_bfs\_breadth":10,"speculative\_ngram\_match\_type":"BFS","speculative\_ngram\_branch\_length":18,"speculative\_ngram\_capacity":10000000,"enable\_multi\_layer\_eagle":false,"ep\_size":1,"moe\_a2a\_backend":"none","moe\_runner\_backend":"auto","flashinfer\_mxfp4\_moe\_precision":"default","enable\_flashinfer\_allreduce\_fusion":false,"deepep\_mode":"auto","ep\_num\_redundant\_experts":0,"ep\_dispatch\_algorithm":null,"init\_expert\_location":"trivial","enable\_eplb":false,"eplb\_algorithm":"auto","eplb\_rebalance\_num\_iterations":1000,"eplb\_rebalance\_layers\_per\_chunk":null,"eplb\_min\_rebalancing\_utilization\_threshold":1.0,"expert\_distribution\_recorder\_mode":null,"expert\_distribution\_recorder\_buffer\_size":1000,"enable\_expert\_distribution\_metrics":false,"deepep\_config":null,"moe\_dense\_tp\_size":null,"elastic\_ep\_backend":null,"mooncake\_ib\_device":null,"max\_mamba\_cache\_size":null,"mamba\_ssm\_dtype":"float32","mamba\_full\_memory\_ratio":0.9,"mamba\_scheduler\_strategy":"no\_buffer","mamba\_track\_interval":256,"enable\_hierarchical\_cache":false,"hicache\_ratio":2.0,"hicache\_size":0,"hicache\_write\_policy":"write\_through","hicache\_io\_backend":"kernel","hicache\_mem\_layout":"layer\_first","disable\_hicache\_numa\_detect":false,"hicache\_storage\_backend":null,"hicache\_storage\_prefetch\_policy":"best\_effort","hicache\_storage\_backend\_extra\_config":null,"hierarchical\_sparse\_attention\_extra\_config":null,"enable\_lmcache":false,"kt\_weight\_path":null,"kt\_method":"AMXINT4","kt\_cpuinfer":null,"kt\_threadpool\_count":2,"kt\_num\_gpu\_experts":null,"kt\_max\_deferred\_experts\_per\_token":null,"dllm\_algorithm":null,"dllm\_algorithm\_config":null,"enable\_double\_sparsity":false,"ds\_channel\_config\_path":null,"ds\_heavy\_channel\_num":32,"ds\_heavy\_token\_num":256,"ds\_heavy\_channel\_type":"qk","ds\_sparse\_decode\_threshold":4096,"cpu\_offload\_gb":0,"offload\_group\_size":-1,"offload\_num\_in\_group":1,"offload\_prefetch\_step":1,"offload\_mode":"cpu","multi\_item\_scoring\_delimiter":null,"disable\_radix\_cache":false,"cuda\_graph\_max\_bs":4,"cuda\_graph\_bs":\[1,2,4],"disable\_cuda\_graph":false,"disable\_cuda\_graph\_padding":false,"enable\_profile\_cuda\_graph":false,"enable\_cudagraph\_gc":false,"enable\_layerwise\_nvtx\_marker":false,"enable\_nccl\_nvls":false,"enable\_symm\_mem":false,"disable\_flashinfer\_cutlass\_moe\_fp4\_allgather":false,"enable\_tokenizer\_batch\_encode":false,"disable\_tokenizer\_batch\_decode":false,"disable\_outlines\_disk\_cache":false,"disable\_custom\_all\_reduce":false,"enable\_mscclpp":false,"enable\_torch\_symm\_mem":false,"disable\_overlap\_schedule":false,"enable\_mixed\_chunk":false,"enable\_dp\_attention":false,"enable\_dp\_lm\_head":false,"enable\_two\_batch\_overlap":false,"enable\_single\_batch\_overlap":false,"tbo\_token\_distribution\_threshold":0.48,"enable\_torch\_compile":false,"enable\_piecewise\_cuda\_graph":false,"enable\_torch\_compile\_debug\_mode":false,"torch\_compile\_max\_bs":32,"piecewise\_cuda\_graph\_max\_tokens":8192,"piecewise\_cuda\_graph\_tokens":\[4,8,12,16,20,24,28,32,48,64,80,96,112,128,144,160,176,192,208,224,240,256,288,320,352,384,416,448,480,512,576,640,704,768,832,896,960,1024,1280,1536,1792,2048,2304,2560,2816,3072,3328,3584,3840,4096,4608,5120,5632,6144,6656,7168,7680,8192],"piecewise\_cuda\_graph\_compiler":"eager","torchao\_config":"","enable\_nan\_detection":false,"enable\_p2p\_check":false,"triton\_attention\_reduce\_in\_fp32":false,"triton\_attention\_num\_kv\_splits":8,"triton\_attention\_split\_tile\_size":null,"num\_continuous\_decode\_steps":1,"delete\_ckpt\_after\_loading":false,"enable\_memory\_saver":false,"enable\_weights\_cpu\_backup":false,"enable\_draft\_weights\_cpu\_backup":false,"allow\_auto\_truncate":false,"enable\_custom\_logit\_processor":false,"flashinfer\_mla\_disable\_ragged":false,"disable\_shared\_experts\_fusion":false,"disable\_chunked\_prefix\_cache":false,"disable\_fast\_image\_processor":false,"keep\_mm\_feature\_on\_device":false,"enable\_return\_hidden\_states":false,"enable\_return\_routed\_experts":false,"scheduler\_recv\_interval":1,"numa\_node":null,"enable\_deterministic\_inference":false,"rl\_on\_policy\_target":null,"enable\_attn\_tp\_input\_scattered":false,"enable\_nsa\_prefill\_context\_parallel":false,"nsa\_prefill\_cp\_mode":"in-seq-split","enable\_fused\_qk\_norm\_rope":false,"enable\_precise\_embedding\_interpolation":false,"enable\_dynamic\_batch\_tokenizer":false,"dynamic\_batch\_tokenizer\_batch\_size":32,"dynamic\_batch\_tokenizer\_batch\_timeout":0.002,"debug\_tensor\_dump\_output\_folder":null,"debug\_tensor\_dump\_layers":null,"debug\_tensor\_dump\_input\_file":null,"debug\_tensor\_dump\_inject":false,"disaggregation\_mode":"null","disaggregation\_transfer\_backend":"mooncake","disaggregation\_bootstrap\_port":8998,"disaggregation\_decode\_tp":null,"disaggregation\_decode\_dp":null,"disaggregation\_prefill\_pp":1,"disaggregation\_ib\_device":null,"disaggregation\_decode\_enable\_offload\_kvcache":false,"disaggregation\_decode\_enable\_fake\_auto":false,"num\_reserved\_decode\_tokens":512,"disaggregation\_decode\_polling\_interval":1,"encoder\_only":false,"language\_only":false,"encoder\_transfer\_backend":"zmq\_to\_scheduler","encoder\_urls":\[],"custom\_weight\_loader":\[],"weight\_loader\_disable\_mmap":false,"remote\_instance\_weight\_loader\_seed\_instance\_ip":null,"remote\_instance\_weight\_loader\_seed\_instance\_service\_port":null,"remote\_instance\_weight\_loader\_send\_weights\_group\_ports":null,"remote\_instance\_weight\_loader\_backend":"nccl","remote\_instance\_weight\_loader\_start\_seed\_via\_transfer\_engine":false,"enable\_pdmux":false,"pdmux\_config\_path":null,"sm\_group\_num":8,"mm\_max\_concurrent\_calls":32,"mm\_per\_request\_timeout":10.0,"enable\_broadcast\_mm\_inputs\_process":false,"enable\_prefix\_mm\_cache":false,"mm\_enable\_dp\_encoder":false,"mm\_process\_config":{},"limit\_mm\_data\_per\_request":null,"decrypted\_config\_file":null,"decrypted\_draft\_config\_file":null,"forward\_hooks":null,"status":"ready","max\_total\_num\_tokens":20480,"max\_req\_input\_len":20474,"internal\_states":\[{"model\_path":"qwen/qwen2.5-0.5b-instruct","tokenizer\_path":"qwen/qwen2.5-0.5b-instruct","tokenizer\_mode":"auto","tokenizer\_worker\_num":1,"skip\_tokenizer\_init":false,"load\_format":"auto","model\_loader\_extra\_config":"{}","trust\_remote\_code":false,"context\_length":null,"is\_embedding":false,"enable\_multimodal":null,"revision":null,"model\_impl":"auto","host":"0.0.0.0","port":33809,"fastapi\_root\_path":"","grpc\_mode":false,"skip\_server\_warmup":false,"warmups":null,"nccl\_port":null,"checkpoint\_engine\_wait\_weights\_before\_ready":false,"dtype":"auto","quantization":null,"quantization\_param\_path":null,"kv\_cache\_dtype":"auto","enable\_fp32\_lm\_head":false,"modelopt\_quant":null,"modelopt\_checkpoint\_restore\_path":null,"modelopt\_checkpoint\_save\_path":null,"modelopt\_export\_path":null,"quantize\_and\_serve":false,"rl\_quant\_profile":null,"mem\_fraction\_static":0.841,"max\_running\_requests":128,"max\_queued\_requests":null,"max\_total\_tokens":20480,"chunked\_prefill\_size":8192,"enable\_dynamic\_chunking":false,"max\_prefill\_tokens":16384,"prefill\_max\_requests":null,"schedule\_policy":"fcfs","enable\_priority\_scheduling":false,"abort\_on\_priority\_when\_disabled":false,"schedule\_low\_priority\_values\_first":false,"priority\_scheduling\_preemption\_threshold":10,"schedule\_conservativeness":1.0,"page\_size":1,"swa\_full\_tokens\_ratio":0.8,"disable\_hybrid\_swa\_memory":false,"radix\_eviction\_policy":"lru","enable\_prefill\_delayer":false,"prefill\_delayer\_max\_delay\_passes":30,"prefill\_delayer\_token\_usage\_low\_watermark":null,"prefill\_delayer\_forward\_passes\_buckets":null,"prefill\_delayer\_wait\_seconds\_buckets":null,"device":"cuda","tp\_size":1,"pp\_size":1,"pp\_max\_micro\_batch\_size":128,"pp\_async\_batch\_depth":0,"stream\_interval":1,"stream\_output":false,"random\_seed":107984454,"constrained\_json\_whitespace\_pattern":null,"constrained\_json\_disable\_any\_whitespace":false,"watchdog\_timeout":300,"soft\_watchdog\_timeout":300,"dist\_timeout":null,"download\_dir":null,"model\_checksum":null,"base\_gpu\_id":0,"gpu\_id\_step":1,"sleep\_on\_idle":false,"custom\_sigquit\_handler":null,"log\_level":"warning","log\_level\_http":null,"log\_requests":false,"log\_requests\_level":2,"log\_requests\_format":"text","log\_requests\_target":null,"uvicorn\_access\_log\_exclude\_prefixes":\[],"crash\_dump\_folder":null,"show\_time\_cost":false,"enable\_metrics":false,"enable\_metrics\_for\_all\_schedulers":false,"tokenizer\_metrics\_custom\_labels\_header":"x-custom-labels","tokenizer\_metrics\_allowed\_custom\_labels":null,"extra\_metric\_labels":null,"bucket\_time\_to\_first\_token":null,"bucket\_inter\_token\_latency":null,"bucket\_e2e\_request\_latency":null,"collect\_tokens\_histogram":false,"prompt\_tokens\_buckets":null,"generation\_tokens\_buckets":null,"gc\_warning\_threshold\_secs":0.0,"decode\_log\_interval":40,"enable\_request\_time\_stats\_logging":false,"kv\_events\_config":null,"enable\_trace":false,"otlp\_traces\_endpoint":"localhost:4317","export\_metrics\_to\_file":false,"export\_metrics\_to\_file\_dir":null,"api\_key":null,"admin\_api\_key":null,"served\_model\_name":"qwen/qwen2.5-0.5b-instruct","weight\_version":"default","chat\_template":null,"hf\_chat\_template\_name":null,"completion\_template":null,"file\_storage\_path":"sglang\_storage","enable\_cache\_report":false,"reasoning\_parser":null,"tool\_call\_parser":null,"tool\_server":null,"sampling\_defaults":"model","dp\_size":1,"load\_balance\_method":"round\_robin","dist\_init\_addr":null,"nnodes":1,"node\_rank":0,"json\_model\_override\_args":"{}","preferred\_sampling\_params":null,"enable\_lora":null,"enable\_lora\_overlap\_loading":null,"max\_lora\_rank":null,"lora\_target\_modules":null,"lora\_paths":null,"max\_loaded\_loras":null,"max\_loras\_per\_batch":8,"lora\_eviction\_policy":"lru","lora\_backend":"csgmv","max\_lora\_chunk\_size":16,"attention\_backend":"fa3","decode\_attention\_backend":"fa3","prefill\_attention\_backend":"fa3","sampling\_backend":"flashinfer","grammar\_backend":"xgrammar","mm\_attention\_backend":null,"fp8\_gemm\_runner\_backend":"auto","fp4\_gemm\_runner\_backend":"auto","nsa\_prefill\_backend":null,"nsa\_decode\_backend":null,"disable\_flashinfer\_autotune":false,"speculative\_algorithm":null,"speculative\_draft\_model\_path":null,"speculative\_draft\_model\_revision":null,"speculative\_draft\_load\_format":null,"speculative\_num\_steps":null,"speculative\_eagle\_topk":null,"speculative\_num\_draft\_tokens":null,"speculative\_accept\_threshold\_single":1.0,"speculative\_accept\_threshold\_acc":1.0,"speculative\_token\_map":null,"speculative\_attention\_mode":"prefill","speculative\_draft\_attention\_backend":null,"speculative\_moe\_runner\_backend":"auto","speculative\_moe\_a2a\_backend":null,"speculative\_draft\_model\_quantization":null,"speculative\_ngram\_min\_match\_window\_size":1,"speculative\_ngram\_max\_match\_window\_size":12,"speculative\_ngram\_min\_bfs\_breadth":1,"speculative\_ngram\_max\_bfs\_breadth":10,"speculative\_ngram\_match\_type":"BFS","speculative\_ngram\_branch\_length":18,"speculative\_ngram\_capacity":10000000,"enable\_multi\_layer\_eagle":false,"ep\_size":1,"moe\_a2a\_backend":"none","moe\_runner\_backend":"auto","flashinfer\_mxfp4\_moe\_precision":"default","enable\_flashinfer\_allreduce\_fusion":false,"deepep\_mode":"auto","ep\_num\_redundant\_experts":0,"ep\_dispatch\_algorithm":null,"init\_expert\_location":"trivial","enable\_eplb":false,"eplb\_algorithm":"auto","eplb\_rebalance\_num\_iterations":1000,"eplb\_rebalance\_layers\_per\_chunk":null,"eplb\_min\_rebalancing\_utilization\_threshold":1.0,"expert\_distribution\_recorder\_mode":null,"expert\_distribution\_recorder\_buffer\_size":1000,"enable\_expert\_distribution\_metrics":false,"deepep\_config":null,"moe\_dense\_tp\_size":null,"elastic\_ep\_backend":null,"mooncake\_ib\_device":null,"max\_mamba\_cache\_size":null,"mamba\_ssm\_dtype":"float32","mamba\_full\_memory\_ratio":0.9,"mamba\_scheduler\_strategy":"no\_buffer","mamba\_track\_interval":256,"enable\_hierarchical\_cache":false,"hicache\_ratio":2.0,"hicache\_size":0,"hicache\_write\_policy":"write\_through","hicache\_io\_backend":"kernel","hicache\_mem\_layout":"layer\_first","disable\_hicache\_numa\_detect":false,"hicache\_storage\_backend":null,"hicache\_storage\_prefetch\_policy":"best\_effort","hicache\_storage\_backend\_extra\_config":null,"hierarchical\_sparse\_attention\_extra\_config":null,"enable\_lmcache":false,"kt\_weight\_path":null,"kt\_method":"AMXINT4","kt\_cpuinfer":null,"kt\_threadpool\_count":2,"kt\_num\_gpu\_experts":null,"kt\_max\_deferred\_experts\_per\_token":null,"dllm\_algorithm":null,"dllm\_algorithm\_config":null,"enable\_double\_sparsity":false,"ds\_channel\_config\_path":null,"ds\_heavy\_channel\_num":32,"ds\_heavy\_token\_num":256,"ds\_heavy\_channel\_type":"qk","ds\_sparse\_decode\_threshold":4096,"cpu\_offload\_gb":0,"offload\_group\_size":-1,"offload\_num\_in\_group":1,"offload\_prefetch\_step":1,"offload\_mode":"cpu","multi\_item\_scoring\_delimiter":null,"disable\_radix\_cache":false,"cuda\_graph\_max\_bs":4,"cuda\_graph\_bs":\[1,2,4],"disable\_cuda\_graph":false,"disable\_cuda\_graph\_padding":false,"enable\_profile\_cuda\_graph":false,"enable\_cudagraph\_gc":false,"enable\_layerwise\_nvtx\_marker":false,"enable\_nccl\_nvls":false,"enable\_symm\_mem":false,"disable\_flashinfer\_cutlass\_moe\_fp4\_allgather":false,"enable\_tokenizer\_batch\_encode":false,"disable\_tokenizer\_batch\_decode":false,"disable\_outlines\_disk\_cache":false,"disable\_custom\_all\_reduce":false,"enable\_mscclpp":false,"enable\_torch\_symm\_mem":false,"disable\_overlap\_schedule":false,"enable\_mixed\_chunk":false,"enable\_dp\_attention":false,"enable\_dp\_lm\_head":false,"enable\_two\_batch\_overlap":false,"enable\_single\_batch\_overlap":false,"tbo\_token\_distribution\_threshold":0.48,"enable\_torch\_compile":false,"enable\_piecewise\_cuda\_graph":false,"enable\_torch\_compile\_debug\_mode":false,"torch\_compile\_max\_bs":32,"piecewise\_cuda\_graph\_max\_tokens":8192,"piecewise\_cuda\_graph\_tokens":\[4,8,12,16,20,24,28,32,48,64,80,96,112,128,144,160,176,192,208,224,240,256,288,320,352,384,416,448,480,512,576,640,704,768,832,896,960,1024,1280,1536,1792,2048,2304,2560,2816,3072,3328,3584,3840,4096,4608,5120,5632,6144,6656,7168,7680,8192],"piecewise\_cuda\_graph\_compiler":"eager","torchao\_config":"","enable\_nan\_detection":false,"enable\_p2p\_check":false,"triton\_attention\_reduce\_in\_fp32":false,"triton\_attention\_num\_kv\_splits":8,"triton\_attention\_split\_tile\_size":null,"num\_continuous\_decode\_steps":1,"delete\_ckpt\_after\_loading":false,"enable\_memory\_saver":false,"enable\_weights\_cpu\_backup":false,"enable\_draft\_weights\_cpu\_backup":false,"allow\_auto\_truncate":false,"enable\_custom\_logit\_processor":false,"flashinfer\_mla\_disable\_ragged":false,"disable\_shared\_experts\_fusion":false,"disable\_chunked\_prefix\_cache":true,"disable\_fast\_image\_processor":false,"keep\_mm\_feature\_on\_device":false,"enable\_return\_hidden\_states":false,"enable\_return\_routed\_experts":false,"scheduler\_recv\_interval":1,"numa\_node":null,"enable\_deterministic\_inference":false,"rl\_on\_policy\_target":null,"enable\_attn\_tp\_input\_scattered":false,"enable\_nsa\_prefill\_context\_parallel":false,"nsa\_prefill\_cp\_mode":"in-seq-split","enable\_fused\_qk\_norm\_rope":false,"enable\_precise\_embedding\_interpolation":false,"enable\_dynamic\_batch\_tokenizer":false,"dynamic\_batch\_tokenizer\_batch\_size":32,"dynamic\_batch\_tokenizer\_batch\_timeout":0.002,"debug\_tensor\_dump\_output\_folder":null,"debug\_tensor\_dump\_layers":null,"debug\_tensor\_dump\_input\_file":null,"debug\_tensor\_dump\_inject":false,"disaggregation\_mode":"null","disaggregation\_transfer\_backend":"mooncake","disaggregation\_bootstrap\_port":8998,"disaggregation\_decode\_tp":null,"disaggregation\_decode\_dp":null,"disaggregation\_prefill\_pp":1,"disaggregation\_ib\_device":null,"disaggregation\_decode\_enable\_offload\_kvcache":false,"disaggregation\_decode\_enable\_fake\_auto":false,"num\_reserved\_decode\_tokens":512,"disaggregation\_decode\_polling\_interval":1,"encoder\_only":false,"language\_only":false,"encoder\_transfer\_backend":"zmq\_to\_scheduler","encoder\_urls":\[],"custom\_weight\_loader":\[],"weight\_loader\_disable\_mmap":false,"remote\_instance\_weight\_loader\_seed\_instance\_ip":null,"remote\_instance\_weight\_loader\_seed\_instance\_service\_port":null,"remote\_instance\_weight\_loader\_send\_weights\_group\_ports":null,"remote\_instance\_weight\_loader\_backend":"nccl","remote\_instance\_weight\_loader\_start\_seed\_via\_transfer\_engine":false,"enable\_pdmux":false,"pdmux\_config\_path":null,"sm\_group\_num":8,"mm\_max\_concurrent\_calls":32,"mm\_per\_request\_timeout":10.0,"enable\_broadcast\_mm\_inputs\_process":false,"enable\_prefix\_mm\_cache":false,"mm\_enable\_dp\_encoder":false,"mm\_process\_config":{},"limit\_mm\_data\_per\_request":null,"decrypted\_config\_file":null,"decrypted\_draft\_config\_file":null,"forward\_hooks":null,"use\_mla\_backend":false,"last\_gen\_throughput":668.7372670340576,"memory\_usage":{"weight":0.98,"kvcache":0.23,"token\_capacity":20480,"graph":0.07},"effective\_max\_running\_requests\_per\_dp":128}],"version":"0.0.0.dev1+gce02df859"}**

## Health Check[#](#Health-Check "Link to this heading")

- `/health`: Check the health of the server.
- `/health_generate`: Check the health of the server by generating one token.

```
url = f"http://localhost:{port}/health_generate"

response = requests.get(url)
print_highlight(response.text)
```

```
url = f"http://localhost:{port}/health"

response = requests.get(url)
print_highlight(response.text)
```

## Flush Cache[#](#Flush-Cache "Link to this heading")

Flush the radix cache. It will be automatically triggered when the model weights are updated by the `/update_weights` API.

```
url = f"http://localhost:{port}/flush_cache"

response = requests.post(url)
print_highlight(response.text)
```

**Cache flushed.**  
**Please check backend logs for more details. (When there are running or waiting requests, the operation will not be performed.)**

## Update Weights From Disk[#](#Update-Weights-From-Disk "Link to this heading")

Update model weights from disk without restarting the server. Only applicable for models with the same architecture and parameter size.

SGLang support `update_weights_from_disk` API for continuous evaluation during training (save checkpoint to disk and update weights from disk).

```
# successful update with same architecture and size

url = f"http://localhost:{port}/update_weights_from_disk"
data = {"model_path": "qwen/qwen2.5-0.5b-instruct"}

response = requests.post(url, json=data)
print_highlight(response.text)
assert response.json()["success"] is True
assert response.json()["message"] == "Succeeded to update model weights."
```

```
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.70it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.70it/s]

```

**{"success":true,"message":"Succeeded to update model weights.","num\_paused\_requests":0}**

```
# failed update with different parameter size or wrong name

url = f"http://localhost:{port}/update_weights_from_disk"
data = {"model_path": "qwen/qwen2.5-0.5b-instruct-wrong"}

response = requests.post(url, json=data)
response_json = response.json()
print_highlight(response_json)
assert response_json["success"] is False
assert response_json["message"] == (
    "Failed to get weights iterator: "
    "qwen/qwen2.5-0.5b-instruct-wrong"
    " (repository not found)."
)
```

```
[2026-02-04 11:27:05] Failed to get weights iterator: qwen/qwen2.5-0.5b-instruct-wrong (repository not found).
```

**{'success': False, 'message': 'Failed to get weights iterator: qwen/qwen2.5-0.5b-instruct-wrong (repository not found).', 'num\_paused\_requests': 0}**

```
terminate_process(server_process)
```

## Encode (embedding model)[#](#Encode-%28embedding-model%29 "Link to this heading")

Encode text into embeddings. Note that this API is only available for [embedding models](https://docs.sglang.io/basic_usage/openai_api_embeddings.html) and will raise an error for generation models. Therefore, we launch a new server to server an embedding model.

```
embedding_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model-path Alibaba-NLP/gte-Qwen2-1.5B-instruct \
    --host 0.0.0.0 --is-embedding --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:27:11] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:11] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:11] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:27:13] INFO model_config.py:1130: Downcasting torch.float32 to torch.float16.
[2026-02-04 11:27:14] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:27:14] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:27:20] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:20] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:20] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:27:20] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:20] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:20] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:27:26] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:26] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:26] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:27:26] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:01<00:01,  1.05s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:01<00:00,  1.21it/s]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:01<00:00,  1.16it/s]

```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
# successful encode for embedding model

url = f"http://localhost:{port}/encode"
data = {"model": "Alibaba-NLP/gte-Qwen2-1.5B-instruct", "text": "Once upon a time"}

response = requests.post(url, json=data)
response_json = response.json()
print_highlight(f"Text embedding (first 10): {response_json['embedding'][:10]}")
```

**Text embedding (first 10): \[-0.00023102760314941406, -0.04986572265625, -0.0032711029052734375, 0.011077880859375, -0.0140533447265625, 0.0159912109375, -0.01441192626953125, 0.0059051513671875, -0.0228424072265625, 0.0272979736328125]**

```
terminate_process(embedding_process)
```

## v1/rerank (cross encoder rerank model)[#](#v1/rerank-%28cross-encoder-rerank-model%29 "Link to this heading")

Rerank a list of documents given a query using a cross-encoder model. Note that this API is only available for cross encoder model like [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) with `attention-backend` `triton` and `torch_native`.

```
reranker_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model-path BAAI/bge-reranker-v2-m3 \
    --host 0.0.0.0 --disable-radix-cache --chunked-prefill-size -1 --attention-backend triton --is-embedding --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:27:40] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:40] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:40] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:27:42] INFO model_config.py:1130: Downcasting torch.float32 to torch.float16.
[2026-02-04 11:27:42] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:27:43] No HuggingFace chat template found
[2026-02-04 11:27:49] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:49] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:49] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:27:49] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:27:49] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:27:49] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:27:54] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:54] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:54] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:27:55] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.88s/it]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.88s/it]

```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
# compute rerank scores for query and documents

url = f"http://localhost:{port}/v1/rerank"
data = {
    "model": "BAAI/bge-reranker-v2-m3",
    "query": "what is panda?",
    "documents": [
        "hi",
        "The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.",
    ],
}

response = requests.post(url, json=data)
response_json = response.json()
for item in response_json:
    print_highlight(f"Score: {item['score']:.2f} - Document: '{item['document']}'")
```

**Score: 5.26 - Document: 'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.'**

**Score: -8.19 - Document: 'hi'**

```
terminate_process(reranker_process)
```

## v1/score (decoder-only scoring)[#](#v1/score-%28decoder-only-scoring%29 "Link to this heading")

Compute token probabilities for specified tokens given a query and items. This is useful for classification tasks, scoring responses, or computing log-probabilities.

Parameters:

- `query`: Query text
- `items`: Item text(s) to score
- `label_token_ids`: Token IDs to compute probabilities for
- `apply_softmax`: Whether to apply softmax to get normalized probabilities (default: False)
- `item_first`: Whether items come first in concatenation order (default: False)
- `model`: Model name

The response contains `scores` - a list of probability lists, one per item, each in the order of `label_token_ids`.

```
score_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct \
    --host 0.0.0.0 --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:28:09] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:09] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:09] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:28:11] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:28:11] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:28:18] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:18] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:18] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:28:18] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:18] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:18] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:28:24] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:28:24] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:28:24] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:28:24] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.98it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.97it/s]

Capturing batches (bs=1 avail_mem=60.60 GB): 100%|██████████| 3/3 [00:00<00:00,  5.56it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
# Score the probability of different completions given a query
query = "The capital of France is"
items = ["Paris", "London", "Berlin"]

url = f"http://localhost:{port}/v1/score"
data = {
    "model": "qwen/qwen2.5-0.5b-instruct",
    "query": query,
    "items": items,
    "label_token_ids": [9454, 2753],  # e.g. "Yes" and "No" token ids
    "apply_softmax": True,  # Normalize probabilities to sum to 1
}

response = requests.post(url, json=data)
response_json = response.json()

# Display scores for each item
for item, scores in zip(items, response_json["scores"]):
    print_highlight(f"Item '{item}': probabilities = {[f'{s:.4f}'forsinscores]}")
```

**Item 'Paris': probabilities = \['0.0237', '0.9763']**

**Item 'London': probabilities = \['0.0284', '0.9716']**

**Item 'Berlin': probabilities = \['0.0637', '0.9363']**

```
terminate_process(score_process)
```

## Classify (reward model)[#](#Classify-%28reward-model%29 "Link to this heading")

SGLang Runtime also supports reward models. Here we use a reward model to classify the quality of pairwise generations.

```
# Note that SGLang now treats embedding models and reward models as the same type of models.
# This will be updated in the future.

reward_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model-path Skywork/Skywork-Reward-Llama-3.1-8B-v0.2 --host 0.0.0.0 --is-embedding --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:28:39] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:39] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:39] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:28:42] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:28:42] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:28:49] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:49] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:49] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:28:49] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:28:49] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:28:49] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:28:55] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:28:55] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:28:55] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:28:55] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:06<00:18,  6.07s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:12<00:12,  6.24s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:17<00:05,  5.50s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:17<00:00,  3.44s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:17<00:00,  4.33s/it]

```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
fromtransformersimport AutoTokenizer

PROMPT = (
    "What is the range of the numeric output of a sigmoid node in a neural network?"
)

RESPONSE1 = "The output of a sigmoid node is bounded between -1 and 1."
RESPONSE2 = "The output of a sigmoid node is bounded between 0 and 1."

CONVS = [
    [{"role": "user", "content": PROMPT}, {"role": "assistant", "content": RESPONSE1}],
    [{"role": "user", "content": PROMPT}, {"role": "assistant", "content": RESPONSE2}],
]

tokenizer = AutoTokenizer.from_pretrained("Skywork/Skywork-Reward-Llama-3.1-8B-v0.2")
prompts = tokenizer.apply_chat_template(CONVS, tokenize=False, return_dict=False)

url = f"http://localhost:{port}/classify"
data = {"model": "Skywork/Skywork-Reward-Llama-3.1-8B-v0.2", "text": prompts}

responses = requests.post(url, json=data).json()
for response in responses:
    print_highlight(f"reward: {response['embedding'][0]}")
```

```
terminate_process(reward_process)
```

## Capture expert selection distribution in MoE models[#](#Capture-expert-selection-distribution-in-MoE-models "Link to this heading")

SGLang Runtime supports recording the number of times an expert is selected in a MoE model run for each expert in the model. This is useful when analyzing the throughput of the model and plan for optimization.

*Note: We only print out the first 10 lines of the csv below for better readability. Please adjust accordingly if you want to analyze the results more deeply.*

```
expert_record_server_process, port = launch_server_cmd(
    "python3 -m sglang.launch_server --model-path Qwen/Qwen1.5-MoE-A2.7B --host 0.0.0.0 --expert-distribution-recorder-mode stat --log-level warning"
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:29:25] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:29:25] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:29:25] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:29:28] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:29:28] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:29:34] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:29:34] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:29:34] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:29:34] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:29:34] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:29:34] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:29:40] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:29:40] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:29:40] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:29:40] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/8 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  12% Completed | 1/8 [00:02<00:18,  2.71s/it]
Loading safetensors checkpoint shards:  25% Completed | 2/8 [00:04<00:13,  2.19s/it]
Loading safetensors checkpoint shards:  38% Completed | 3/8 [00:07<00:11,  2.37s/it]
Loading safetensors checkpoint shards:  50% Completed | 4/8 [00:09<00:09,  2.38s/it]
Loading safetensors checkpoint shards:  62% Completed | 5/8 [00:12<00:07,  2.54s/it]
Loading safetensors checkpoint shards:  75% Completed | 6/8 [00:15<00:05,  2.65s/it]
Loading safetensors checkpoint shards:  88% Completed | 7/8 [00:18<00:02,  2.74s/it]
Loading safetensors checkpoint shards: 100% Completed | 8/8 [00:18<00:00,  2.05s/it]
Loading safetensors checkpoint shards: 100% Completed | 8/8 [00:18<00:00,  2.34s/it]

Capturing batches (bs=4 avail_mem=47.76 GB):   0%|          | 0/3 [00:00<?, ?it/s][2026-02-04 11:30:00] Using default MoE kernel config. Performance might be sub-optimal! Config file not found at /public_sglang_ci/runner-l1-thj6s-gpu-1/_work/sglang/sglang/python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=60,N=1408,device_name=NVIDIA_H100_80GB_HBM3.json, you can create them with https://github.com/sgl-project/sglang/tree/main/benchmark/kernels/fused_moe_triton
[2026-02-04 11:30:00] Using MoE kernel config with down_moe=False. Performance might be sub-optimal! Config file not found at /public_sglang_ci/runner-l1-thj6s-gpu-1/_work/sglang/sglang/python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=60,N=1408,device_name=NVIDIA_H100_80GB_HBM3_down.json, you can create them with https://github.com/sgl-project/sglang/tree/main/benchmark/kernels/fused_moe_triton
Capturing batches (bs=1 avail_mem=47.65 GB): 100%|██████████| 3/3 [00:02<00:00,  1.07it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
response = requests.post(f"http://localhost:{port}/start_expert_distribution_record")
print_highlight(response)

url = f"http://localhost:{port}/generate"
data = {"text": "What is the capital of France?"}

response = requests.post(url, json=data)
print_highlight(response.json())

response = requests.post(f"http://localhost:{port}/stop_expert_distribution_record")
print_highlight(response)

response = requests.post(f"http://localhost:{port}/dump_expert_distribution_record")
print_highlight(response)
```

**{'text': ' The capital of France is Paris.', 'output\_ids': \[576, 6722, 315, 9625, 374, 12095, 13, 151643], 'meta\_info': {'id': 'fa4a971ee88e44cdbc8906ecb8e1186e', 'finish\_reason': {'type': 'stop', 'matched': 151643}, 'prompt\_tokens': 7, 'weight\_version': 'default', 'total\_retractions': 0, 'completion\_tokens': 8, 'cached\_tokens': 0, 'cached\_tokens\_details': None, 'e2e\_latency': 0.11526823043823242, 'response\_sent\_to\_client\_ts': 1770204609.1116006}}**

```
terminate_process(expert_record_server_process)
```

## Tokenize/Detokenize Example (Round Trip)[#](#Tokenize/Detokenize-Example-%28Round-Trip%29 "Link to this heading")

This example demonstrates how to use the /tokenize and /detokenize endpoints together. We first tokenize a string, then detokenize the resulting IDs to reconstruct the original text. This workflow is useful when you need to handle tokenization externally but still leverage the server for detokenization.

```
tokenizer_free_server_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:30:15] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:30:15] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:30:15] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:30:17] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:30:17] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:30:17] server_args=ServerArgs(model_path='qwen/qwen2.5-0.5b-instruct', tokenizer_path='qwen/qwen2.5-0.5b-instruct', tokenizer_mode='auto', tokenizer_worker_num=1, skip_tokenizer_init=False, load_format='auto', model_loader_extra_config='{}', trust_remote_code=False, context_length=None, is_embedding=False, enable_multimodal=None, revision=None, model_impl='auto', host='127.0.0.1', port=33129, fastapi_root_path='', grpc_mode=False, skip_server_warmup=False, warmups=None, nccl_port=None, checkpoint_engine_wait_weights_before_ready=False, dtype='auto', quantization=None, quantization_param_path=None, kv_cache_dtype='auto', enable_fp32_lm_head=False, modelopt_quant=None, modelopt_checkpoint_restore_path=None, modelopt_checkpoint_save_path=None, modelopt_export_path=None, quantize_and_serve=False, rl_quant_profile=None, mem_fraction_static=0.841, max_running_requests=128, max_queued_requests=None, max_total_tokens=20480, chunked_prefill_size=8192, enable_dynamic_chunking=False, max_prefill_tokens=16384, prefill_max_requests=None, schedule_policy='fcfs', enable_priority_scheduling=False, abort_on_priority_when_disabled=False, schedule_low_priority_values_first=False, priority_scheduling_preemption_threshold=10, schedule_conservativeness=1.0, page_size=1, swa_full_tokens_ratio=0.8, disable_hybrid_swa_memory=False, radix_eviction_policy='lru', enable_prefill_delayer=False, prefill_delayer_max_delay_passes=30, prefill_delayer_token_usage_low_watermark=None, prefill_delayer_forward_passes_buckets=None, prefill_delayer_wait_seconds_buckets=None, device='cuda', tp_size=1, pp_size=1, pp_max_micro_batch_size=None, pp_async_batch_depth=0, stream_interval=1, stream_output=False, random_seed=619097222, constrained_json_whitespace_pattern=None, constrained_json_disable_any_whitespace=False, watchdog_timeout=300, soft_watchdog_timeout=300, dist_timeout=None, download_dir=None, model_checksum=None, base_gpu_id=0, gpu_id_step=1, sleep_on_idle=False, custom_sigquit_handler=None, log_level='info', log_level_http=None, log_requests=False, log_requests_level=2, log_requests_format='text', log_requests_target=None, uvicorn_access_log_exclude_prefixes=[], crash_dump_folder=None, show_time_cost=False, enable_metrics=False, enable_metrics_for_all_schedulers=False, tokenizer_metrics_custom_labels_header='x-custom-labels', tokenizer_metrics_allowed_custom_labels=None, extra_metric_labels=None, bucket_time_to_first_token=None, bucket_inter_token_latency=None, bucket_e2e_request_latency=None, collect_tokens_histogram=False, prompt_tokens_buckets=None, generation_tokens_buckets=None, gc_warning_threshold_secs=0.0, decode_log_interval=40, enable_request_time_stats_logging=False, kv_events_config=None, enable_trace=False, otlp_traces_endpoint='localhost:4317', export_metrics_to_file=False, export_metrics_to_file_dir=None, api_key=None, admin_api_key=None, served_model_name='qwen/qwen2.5-0.5b-instruct', weight_version='default', chat_template=None, hf_chat_template_name=None, completion_template=None, file_storage_path='sglang_storage', enable_cache_report=False, reasoning_parser=None, tool_call_parser=None, tool_server=None, sampling_defaults='model', dp_size=1, load_balance_method='round_robin', dist_init_addr=None, nnodes=1, node_rank=0, json_model_override_args='{}', preferred_sampling_params=None, enable_lora=None, enable_lora_overlap_loading=None, max_lora_rank=None, lora_target_modules=None, lora_paths=None, max_loaded_loras=None, max_loras_per_batch=8, lora_eviction_policy='lru', lora_backend='csgmv', max_lora_chunk_size=16, attention_backend='fa3', decode_attention_backend=None, prefill_attention_backend=None, sampling_backend='flashinfer', grammar_backend='xgrammar', mm_attention_backend=None, fp8_gemm_runner_backend='auto', fp4_gemm_runner_backend='auto', nsa_prefill_backend=None, nsa_decode_backend=None, disable_flashinfer_autotune=False, speculative_algorithm=None, speculative_draft_model_path=None, speculative_draft_model_revision=None, speculative_draft_load_format=None, speculative_num_steps=None, speculative_eagle_topk=None, speculative_num_draft_tokens=None, speculative_accept_threshold_single=1.0, speculative_accept_threshold_acc=1.0, speculative_token_map=None, speculative_attention_mode='prefill', speculative_draft_attention_backend=None, speculative_moe_runner_backend='auto', speculative_moe_a2a_backend=None, speculative_draft_model_quantization=None, speculative_ngram_min_match_window_size=1, speculative_ngram_max_match_window_size=12, speculative_ngram_min_bfs_breadth=1, speculative_ngram_max_bfs_breadth=10, speculative_ngram_match_type='BFS', speculative_ngram_branch_length=18, speculative_ngram_capacity=10000000, enable_multi_layer_eagle=False, ep_size=1, moe_a2a_backend='none', moe_runner_backend='auto', flashinfer_mxfp4_moe_precision='default', enable_flashinfer_allreduce_fusion=False, deepep_mode='auto', ep_num_redundant_experts=0, ep_dispatch_algorithm=None, init_expert_location='trivial', enable_eplb=False, eplb_algorithm='auto', eplb_rebalance_num_iterations=1000, eplb_rebalance_layers_per_chunk=None, eplb_min_rebalancing_utilization_threshold=1.0, expert_distribution_recorder_mode=None, expert_distribution_recorder_buffer_size=1000, enable_expert_distribution_metrics=False, deepep_config=None, moe_dense_tp_size=None, elastic_ep_backend=None, mooncake_ib_device=None, max_mamba_cache_size=None, mamba_ssm_dtype='float32', mamba_full_memory_ratio=0.9, mamba_scheduler_strategy='no_buffer', mamba_track_interval=256, enable_hierarchical_cache=False, hicache_ratio=2.0, hicache_size=0, hicache_write_policy='write_through', hicache_io_backend='kernel', hicache_mem_layout='layer_first', disable_hicache_numa_detect=False, hicache_storage_backend=None, hicache_storage_prefetch_policy='best_effort', hicache_storage_backend_extra_config=None, hierarchical_sparse_attention_extra_config=None, enable_lmcache=False, kt_weight_path=None, kt_method='AMXINT4', kt_cpuinfer=None, kt_threadpool_count=2, kt_num_gpu_experts=None, kt_max_deferred_experts_per_token=None, dllm_algorithm=None, dllm_algorithm_config=None, enable_double_sparsity=False, ds_channel_config_path=None, ds_heavy_channel_num=32, ds_heavy_token_num=256, ds_heavy_channel_type='qk', ds_sparse_decode_threshold=4096, cpu_offload_gb=0, offload_group_size=-1, offload_num_in_group=1, offload_prefetch_step=1, offload_mode='cpu', multi_item_scoring_delimiter=None, disable_radix_cache=False, cuda_graph_max_bs=4, cuda_graph_bs=[1, 2, 4], disable_cuda_graph=False, disable_cuda_graph_padding=False, enable_profile_cuda_graph=False, enable_cudagraph_gc=False, enable_layerwise_nvtx_marker=False, enable_nccl_nvls=False, enable_symm_mem=False, disable_flashinfer_cutlass_moe_fp4_allgather=False, enable_tokenizer_batch_encode=False, disable_tokenizer_batch_decode=False, disable_outlines_disk_cache=False, disable_custom_all_reduce=False, enable_mscclpp=False, enable_torch_symm_mem=False, disable_overlap_schedule=False, enable_mixed_chunk=False, enable_dp_attention=False, enable_dp_lm_head=False, enable_two_batch_overlap=False, enable_single_batch_overlap=False, tbo_token_distribution_threshold=0.48, enable_torch_compile=False, enable_piecewise_cuda_graph=False, enable_torch_compile_debug_mode=False, torch_compile_max_bs=32, piecewise_cuda_graph_max_tokens=8192, piecewise_cuda_graph_tokens=[4, 8, 12, 16, 20, 24, 28, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 288, 320, 352, 384, 416, 448, 480, 512, 576, 640, 704, 768, 832, 896, 960, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816, 3072, 3328, 3584, 3840, 4096, 4608, 5120, 5632, 6144, 6656, 7168, 7680, 8192], piecewise_cuda_graph_compiler='eager', torchao_config='', enable_nan_detection=False, enable_p2p_check=False, triton_attention_reduce_in_fp32=False, triton_attention_num_kv_splits=8, triton_attention_split_tile_size=None, num_continuous_decode_steps=1, delete_ckpt_after_loading=False, enable_memory_saver=False, enable_weights_cpu_backup=False, enable_draft_weights_cpu_backup=False, allow_auto_truncate=False, enable_custom_logit_processor=False, flashinfer_mla_disable_ragged=False, disable_shared_experts_fusion=False, disable_chunked_prefix_cache=False, disable_fast_image_processor=False, keep_mm_feature_on_device=False, enable_return_hidden_states=False, enable_return_routed_experts=False, scheduler_recv_interval=1, numa_node=None, enable_deterministic_inference=False, rl_on_policy_target=None, enable_attn_tp_input_scattered=False, enable_nsa_prefill_context_parallel=False, nsa_prefill_cp_mode='in-seq-split', enable_fused_qk_norm_rope=False, enable_precise_embedding_interpolation=False, enable_dynamic_batch_tokenizer=False, dynamic_batch_tokenizer_batch_size=32, dynamic_batch_tokenizer_batch_timeout=0.002, debug_tensor_dump_output_folder=None, debug_tensor_dump_layers=None, debug_tensor_dump_input_file=None, debug_tensor_dump_inject=False, disaggregation_mode='null', disaggregation_transfer_backend='mooncake', disaggregation_bootstrap_port=8998, disaggregation_decode_tp=None, disaggregation_decode_dp=None, disaggregation_prefill_pp=1, disaggregation_ib_device=None, disaggregation_decode_enable_offload_kvcache=False, disaggregation_decode_enable_fake_auto=False, num_reserved_decode_tokens=512, disaggregation_decode_polling_interval=1, encoder_only=False, language_only=False, encoder_transfer_backend='zmq_to_scheduler', encoder_urls=[], custom_weight_loader=[], weight_loader_disable_mmap=False, remote_instance_weight_loader_seed_instance_ip=None, remote_instance_weight_loader_seed_instance_service_port=None, remote_instance_weight_loader_send_weights_group_ports=None, remote_instance_weight_loader_backend='nccl', remote_instance_weight_loader_start_seed_via_transfer_engine=False, enable_pdmux=False, pdmux_config_path=None, sm_group_num=8, mm_max_concurrent_calls=32, mm_per_request_timeout=10.0, enable_broadcast_mm_inputs_process=False, enable_prefix_mm_cache=False, mm_enable_dp_encoder=False, mm_process_config={}, limit_mm_data_per_request=None, decrypted_config_file=None, decrypted_draft_config_file=None, forward_hooks=None)
[2026-02-04 11:30:18] Watchdog TokenizerManager initialized.
[2026-02-04 11:30:18] Using default HuggingFace chat template with detected content format: string
[2026-02-04 11:30:23] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:30:23] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:30:23] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:30:23] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:30:23] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:30:23] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:30:26] Watchdog DetokenizerManager initialized.
[2026-02-04 11:30:26] Init torch distributed begin.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:30:26] Init torch distributed ends. elapsed=0.26 s, mem usage=0.09 GB
[2026-02-04 11:30:26] MOE_RUNNER_BACKEND is not initialized, the backend will be automatically selected
[2026-02-04 11:30:29] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:30:29] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:30:29] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:30:29] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
[2026-02-04 11:30:29] Load weight begin. avail mem=78.43 GB
[2026-02-04 11:30:29] Found local HF snapshot for qwen/qwen2.5-0.5b-instruct at /hf_home/hub/models--qwen--qwen2.5-0.5b-instruct/snapshots/7ae557604adf67be50417f59c2c2f167def9a775; skipping download.
[2026-02-04 11:30:29] No model.safetensors.index.json found in remote.
[2026-02-04 11:30:29] Beginning to load weights
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.76it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.76it/s]

[2026-02-04 11:30:29] Loading weights took 0.20 seconds
[2026-02-04 11:30:29] Load weight end. elapsed=0.38 s, type=Qwen2ForCausalLM, dtype=torch.bfloat16, avail mem=77.45 GB, mem usage=0.98 GB.
[2026-02-04 11:30:29] Using KV cache dtype: torch.bfloat16
[2026-02-04 11:30:29] KV Cache is allocated. #tokens: 20480, K size: 0.12 GB, V size: 0.12 GB
[2026-02-04 11:30:29] Memory pool end. avail mem=77.12 GB
[2026-02-04 11:30:29] Init attention backend begin.
[2026-02-04 11:30:29] Init attention backend end. elapsed=0.03 s
[2026-02-04 11:30:29] Capture cuda graph begin. This can take up to several minutes. avail mem=77.02 GB
[2026-02-04 11:30:29] Capture cuda graph bs [1, 2, 4]
Capturing batches (bs=1 avail_mem=76.96 GB): 100%|██████████| 3/3 [00:00<00:00,  5.84it/s]
[2026-02-04 11:30:30] Capture cuda graph end. Time elapsed: 1.01 s. mem usage=0.07 GB. avail mem=76.95 GB.
[2026-02-04 11:30:31] max_total_num_tokens=20480, chunked_prefill_size=8192, max_prefill_tokens=16384, max_running_requests=128, context_len=32768, available_gpu_mem=76.95 GB
[2026-02-04 11:30:31] INFO:     Started server process [1780921]
[2026-02-04 11:30:31] INFO:     Waiting for application startup.
[2026-02-04 11:30:31] Using default chat sampling params from model generation config: {'repetition_penalty': 1.1, 'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
[2026-02-04 11:30:31] Using default chat sampling params from model generation config: {'repetition_penalty': 1.1, 'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
[2026-02-04 11:30:31] INFO:     Application startup complete.
[2026-02-04 11:30:31] INFO:     Uvicorn running on http://127.0.0.1:33129 (Press CTRL+C to quit)
[2026-02-04 11:30:32] INFO:     127.0.0.1:54992 - "GET /v1/models HTTP/1.1" 200 OK
[2026-02-04 11:30:32] INFO:     127.0.0.1:55008 - "GET /model_info HTTP/1.1" 200 OK
[2026-02-04 11:30:33] Prefill batch, #new-seq: 1, #new-token: 6, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0, input throughput (token/s): 0.00, cuda graph: False
[2026-02-04 11:30:33] INFO:     127.0.0.1:55012 - "POST /generate HTTP/1.1" 200 OK
[2026-02-04 11:30:33] The server is fired up and ready to roll!
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
importrequests
fromsglang.utilsimport print_highlight

base_url = f"http://localhost:{port}"
tokenize_url = f"{base_url}/tokenize"
detokenize_url = f"{base_url}/detokenize"

model_name = "qwen/qwen2.5-0.5b-instruct"
input_text = "SGLang provides efficient tokenization endpoints."
print_highlight(f"Original Input Text:\n'{input_text}'")

# --- tokenize the input text ---
tokenize_payload = {
    "model": model_name,
    "prompt": input_text,
    "add_special_tokens": False,
}
try:
    tokenize_response = requests.post(tokenize_url, json=tokenize_payload)
    tokenize_response.raise_for_status()
    tokenization_result = tokenize_response.json()
    token_ids = tokenization_result.get("tokens")

    if not token_ids:
        raise ValueError("Tokenization returned empty tokens.")

    print_highlight(f"\nTokenized Output (IDs):\n{token_ids}")
    print_highlight(f"Token Count: {tokenization_result.get('count')}")
    print_highlight(f"Max Model Length: {tokenization_result.get('max_model_len')}")

    # --- detokenize the obtained token IDs ---
    detokenize_payload = {
        "model": model_name,
        "tokens": token_ids,
        "skip_special_tokens": True,
    }

    detokenize_response = requests.post(detokenize_url, json=detokenize_payload)
    detokenize_response.raise_for_status()
    detokenization_result = detokenize_response.json()
    reconstructed_text = detokenization_result.get("text")

    print_highlight(f"\nDetokenized Output (Text):\n'{reconstructed_text}'")

    if input_text == reconstructed_text:
        print_highlight(
            "\nRound Trip Successful: Original and reconstructed text match."
        )
    else:
        print_highlight(
            "\nRound Trip Mismatch: Original and reconstructed text differ."
        )

except requests.exceptions.RequestException as e:
    print_highlight(f"\nHTTP Request Error: {e}")
except Exception as e:
    print_highlight(f"\nAn error occurred: {e}")
```

**Original Input Text:**  
**'SGLang provides efficient tokenization endpoints.'**

```
[2026-02-04 11:30:37] INFO:     127.0.0.1:34162 - "POST /tokenize HTTP/1.1" 200 OK
```

**Tokenized Output (IDs):**  
**\[50, 3825, 524, 5707, 11050, 3950, 2022, 36342, 13]**

```
[2026-02-04 11:30:37] INFO:     127.0.0.1:34166 - "POST /detokenize HTTP/1.1" 200 OK
```

**Detokenized Output (Text):**  
**'SGLang provides efficient tokenization endpoints.'**

**Round Trip Successful: Original and reconstructed text match.**

```
terminate_process(tokenizer_free_server_process)
```