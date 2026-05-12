---
title: AMD Quark - vLLM
url: https://docs.vllm.ai/en/latest/features/quantization/quark/
source: sitemap
fetched_at: 2026-05-07T21:14:34.878698506-03:00
rendered_js: false
word_count: 784
summary: This document provides a step-by-step guide on how to use the Quark quantization toolkit to optimize large language models for deployment on AMD GPUs within the vLLM environment.
tags:
    - vllm
    - quantization
    - amd-gpu
    - quark
    - fp8
    - model-optimization
    - llm
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/quark.md "Edit this page")

Quantization can effectively reduce memory and bandwidth usage, accelerate computation and improve throughput while with minimal accuracy loss. vLLM can leverage [Quark](https://quark.docs.amd.com/latest/), the flexible and powerful quantization toolkit, to produce performant quantized models to run on AMD GPUs. Quark has specialized support for quantizing large language models with weight, activation and kv-cache quantization and cutting-edge quantization algorithms like AWQ, GPTQ, Rotation and SmoothQuant.

## Quark Installation[¶](#quark-installation "Permanent link")

Before quantizing models, you need to install Quark. The latest release of Quark can be installed with pip:

You can refer to [Quark installation guide](https://quark.docs.amd.com/latest/install.html) for more installation details.

Additionally, install `vllm` and `lm-evaluation-harness` for evaluation:

```
pipinstallvllm"lm-eval[api]>=0.4.11"
```

## Quantization Process[¶](#quantization-process "Permanent link")

After installing Quark, we will use an example to illustrate how to use Quark. The Quark quantization process can be listed for 5 steps as below:

1. Load the model
2. Prepare the calibration dataloader
3. Set the quantization configuration
4. Quantize the model and export
5. Evaluation in vLLM

### 1. Load the Model[¶](#1-load-the-model "Permanent link")

Quark uses [Transformers](https://huggingface.co/docs/transformers/en/index) to fetch model and tokenizer.

Code

```
fromtransformersimport AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "meta-llama/Llama-2-70b-chat-hf"
MAX_SEQ_LEN = 512

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    dtype="auto",
)
model.eval()

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, model_max_length=MAX_SEQ_LEN)
tokenizer.pad_token = tokenizer.eos_token
```

### 2. Prepare the Calibration Dataloader[¶](#2-prepare-the-calibration-dataloader "Permanent link")

Quark uses the [PyTorch Dataloader](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html) to load calibration data. For more details about how to use calibration datasets efficiently, please refer to [Adding Calibration Datasets](https://quark.docs.amd.com/latest/pytorch/calibration_datasets.html).

Code

```
fromdatasetsimport load_dataset
fromtorch.utils.dataimport DataLoader

BATCH_SIZE = 1
NUM_CALIBRATION_DATA = 512

# Load the dataset and get calibration data.
dataset = load_dataset("mit-han-lab/pile-val-backup", split="validation")
text_data = dataset["text"][:NUM_CALIBRATION_DATA]

tokenized_outputs = tokenizer(
    text_data,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=MAX_SEQ_LEN,
)
calib_dataloader = DataLoader(
    tokenized_outputs['input_ids'],
    batch_size=BATCH_SIZE,
    drop_last=True,
)
```

### 3. Set the Quantization Configuration[¶](#3-set-the-quantization-configuration "Permanent link")

We need to set the quantization configuration, you can check [quark config guide](https://quark.docs.amd.com/latest/pytorch/user_guide_config_description.html) for further details. Here we use FP8 per-tensor quantization on weight, activation, kv-cache and the quantization algorithm is AutoSmoothQuant.

Note

Note the quantization algorithm needs a JSON config file and the config file is located in [Quark Pytorch examples](https://quark.docs.amd.com/latest/pytorch/pytorch_examples.html), under the directory `examples/torch/language_modeling/llm_ptq/models`. For example, AutoSmoothQuant config file for Llama is `examples/torch/language_modeling/llm_ptq/models/llama/autosmoothquant_config.json`.

Code

```
fromquark.torch.quantizationimport (Config, QuantizationConfig,
                                    FP8E4M3PerTensorSpec,
                                    load_quant_algo_config_from_file)

# Define fp8/per-tensor/static spec.
FP8_PER_TENSOR_SPEC = FP8E4M3PerTensorSpec(
    observer_method="min_max",
    is_dynamic=False,
).to_quantization_spec()

# Define global quantization config, input tensors and weight apply FP8_PER_TENSOR_SPEC.
global_quant_config = QuantizationConfig(
    input_tensors=FP8_PER_TENSOR_SPEC,
    weight=FP8_PER_TENSOR_SPEC,
)

# Define quantization config for kv-cache layers, output tensors apply FP8_PER_TENSOR_SPEC.
KV_CACHE_SPEC = FP8_PER_TENSOR_SPEC
kv_cache_layer_names_for_llama = ["*k_proj", "*v_proj"]
kv_cache_quant_config = {
    name: QuantizationConfig(
        input_tensors=global_quant_config.input_tensors,
        weight=global_quant_config.weight,
        output_tensors=KV_CACHE_SPEC,
    )
    for name in kv_cache_layer_names_for_llama
}
layer_quant_config = kv_cache_quant_config.copy()

# Define algorithm config by config file.
LLAMA_AUTOSMOOTHQUANT_CONFIG_FILE = "examples/torch/language_modeling/llm_ptq/models/llama/autosmoothquant_config.json"
algo_config = load_quant_algo_config_from_file(LLAMA_AUTOSMOOTHQUANT_CONFIG_FILE)

EXCLUDE_LAYERS = ["lm_head"]
quant_config = Config(
    global_quant_config=global_quant_config,
    layer_quant_config=layer_quant_config,
    kv_cache_quant_config=kv_cache_quant_config,
    exclude=EXCLUDE_LAYERS,
    algo_config=algo_config,
)
```

### 4. Quantize the Model and Export[¶](#4-quantize-the-model-and-export "Permanent link")

Then we can apply the quantization. After quantizing, we need to freeze the quantized model first before exporting. Note that we need to export model with format of HuggingFace `safetensors`, you can refer to [HuggingFace format exporting](https://quark.docs.amd.com/latest/pytorch/export/quark_export_hf.html) for more exporting format details.

Code

```
importtorch
fromquark.torchimport ModelQuantizer, ModelExporter
fromquark.torch.exportimport ExporterConfig, JsonExporterConfig

# Apply quantization.
quantizer = ModelQuantizer(quant_config)
quant_model = quantizer.quantize_model(model, calib_dataloader)

# Freeze quantized model to export.
freezed_model = quantizer.freeze(model)

# Define export config.
LLAMA_KV_CACHE_GROUP = ["*k_proj", "*v_proj"]
export_config = ExporterConfig(json_export_config=JsonExporterConfig())
export_config.json_export_config.kv_cache_group = LLAMA_KV_CACHE_GROUP

# Model: Llama-2-70b-chat-hf-w-fp8-a-fp8-kvcache-fp8-pertensor-autosmoothquant
EXPORT_DIR = MODEL_ID.split("/")[1] + "-w-fp8-a-fp8-kvcache-fp8-pertensor-autosmoothquant"
exporter = ModelExporter(config=export_config, export_dir=EXPORT_DIR)
with torch.no_grad():
    exporter.export_safetensors_model(
        freezed_model,
        quant_config=quant_config,
        tokenizer=tokenizer,
    )
```

### 5. Evaluation in vLLM[¶](#5-evaluation-in-vllm "Permanent link")

Now, you can load and run the Quark quantized model directly through the LLM entrypoint:

Code

```
fromvllmimport LLM, SamplingParams

# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

# Create an LLM.
llm = LLM(
    model="Llama-2-70b-chat-hf-w-fp8-a-fp8-kvcache-fp8-pertensor-autosmoothquant",
    kv_cache_dtype="fp8",
    quantization="quark",
)
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
print("\nGenerated Outputs:\n" + "-" * 60)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt:    {prompt!r}")
    print(f"Output:    {generated_text!r}")
    print("-" * 60)
```

Or, you can use `lm_eval` to evaluate accuracy:

```
lm_eval--modelvllm\
--model_argspretrained=Llama-2-70b-chat-hf-w-fp8-a-fp8-kvcache-fp8-pertensor-autosmoothquant,kv_cache_dtype='fp8',quantization='quark'\
--tasksgsm8k
```

## Quark Quantization Script[¶](#quark-quantization-script "Permanent link")

In addition to the example of Python API above, Quark also offers a [quantization script](https://quark.docs.amd.com/latest/pytorch/example_quark_torch_llm_ptq.html) to quantize large language models more conveniently. It supports quantizing models with variety of different quantization schemes and optimization algorithms. It can export the quantized model and run evaluation tasks on the fly. With the script, the example above can be:

```
python3quantize_quark.py--model_dirmeta-llama/Llama-2-70b-chat-hf\
--output_dir/path/to/output\
--quant_schemew_fp8_a_fp8\
--kv_cache_dtypefp8\
--quant_algoautosmoothquant\
--num_calib_data512\
--model_exporthf_format\
--tasksgsm8k
```

## Using OCP MX (MXFP4, MXFP6) models[¶](#using-ocp-mx-mxfp4-mxfp6-models "Permanent link")

vLLM supports loading MXFP4 and MXFP6 models quantized offline through AMD Quark, compliant with [Open Compute Project (OCP) specification](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf).

The scheme currently only supports dynamic quantization for activations.

Example usage, after installing the latest AMD Quark release:

```
vllmservefxmarty/qwen_1.5-moe-a2.7b-mxfp4--tensor-parallel-size1
# or, for a model using fp6 activations and fp4 weights:
vllmservefxmarty/qwen1.5_moe_a2.7b_chat_w_fp4_a_fp6_e2m3--tensor-parallel-size1
```

A simulation of the matrix multiplication execution in MXFP4/MXFP6 can be run on devices that do not support OCP MX operations natively (e.g. AMD Instinct MI325, MI300 and MI250), dequantizing weights from FP4/FP6 to half precision on the fly, using a fused kernel. This is useful e.g. to evaluate FP4/FP6 models using vLLM, or alternatively to benefit from the ~2.5-4x memory savings (compared to float16 and bfloat16).

To generate offline models quantized using MXFP4 data type, the easiest approach is to use AMD Quark's [quantization script](https://quark.docs.amd.com/latest/pytorch/example_quark_torch_llm_ptq.html), as an example:

```
pythonquantize_quark.py--model_dirQwen/Qwen1.5-MoE-A2.7B-Chat\
--quant_schemew_mxfp4_a_mxfp4\
--output_dirqwen_1.5-moe-a2.7b-mxfp4\
--skip_evaluation\
--model_exporthf_format\
--group_size32
```

The current integration supports [all combination of FP4, FP6\_E3M2, FP6\_E2M3](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/utils/ocp_mx_utils.py) used for either weights or activations.

## Using Quark Quantized layerwise Auto Mixed Precision (AMP) Models[¶](#using-quark-quantized-layerwise-auto-mixed-precision-amp-models "Permanent link")

vLLM also supports loading layerwise mixed precision model quantized using AMD Quark. Currently, mixed scheme of {MXFP4, FP8} is supported, where FP8 here denotes for FP8 per-tensor scheme. More mixed precision schemes are planned to be supported in a near future, including

- Unquantized Linear and/or MoE layer(s) as an option for each layer, i.e., mixed of {MXFP4, FP8, BF16/FP16}
- MXFP6 quantization extension, i.e., {MXFP4, MXFP6, FP8, BF16/FP16}

Although one can maximize serving throughput using the lowest precision supported on a given device (e.g. MXFP4 for AMD Instinct MI355, FP8 for AMD Instinct MI300), these aggressive schemes can be detrimental to accuracy recovering from quantization on target tasks. Mixed precision allows to strike a balance between maximizing accuracy and throughput.

There are two steps to generate and deploy a mixed precision model quantized with AMD Quark, as shown below.

### 1. Quantize a model using mixed precision in AMD Quark[¶](#1-quantize-a-model-using-mixed-precision-in-amd-quark "Permanent link")

Firstly, the layerwise mixed-precision configuration for a given LLM model is searched and then quantized using AMD Quark. We will provide a detailed tutorial with Quark APIs later.

As examples, we provide some ready-to-use quantized mixed precision model to show the usage in vLLM and the accuracy benefits. They are:

- amd/Llama-2-70b-chat-hf-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8
- amd/Mixtral-8x7B-Instruct-v0.1-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8
- amd/Qwen3-8B-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8

### 2. inference the quantized mixed precision model in vLLM[¶](#2-inference-the-quantized-mixed-precision-model-in-vllm "Permanent link")

Models quantized with AMD Quark using mixed precision can natively be reload in vLLM, and e.g. evaluated using lm-evaluation-harness as follows:

```
lm_eval--modelvllm\
--model_argspretrained=amd/Llama-2-70b-chat-hf-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8,tensor_parallel_size=4,dtype=auto,gpu_memory_utilization=0.8,trust_remote_code=False\
--tasksmmlu\
--batch_sizeauto
```