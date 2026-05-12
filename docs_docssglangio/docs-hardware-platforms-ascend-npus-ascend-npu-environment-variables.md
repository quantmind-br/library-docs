---
title: Environment Variables - SGLang Documentation
url: https://docs.sglang.io/docs/hardware-platforms/ascend-npus/ascend_npu_environment_variables
source: sitemap
fetched_at: 2026-05-11T05:48:42.42637557-03:00
rendered_js: false
word_count: 358
summary: This document lists environment variables used to configure the runtime behavior of SGLang and DeepEP on Ascend NPU hardware.
tags:
    - sglang
    - ascend-npu
    - deepep
    - environment-variables
    - runtime-configuration
    - model-performance
category: reference
---

- [Directly Used in SGLang](#directly-used-in-sglang)
- [Used in DeepEP Ascend](#used-in-deepep-ascend)
- [Others](#others)

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang supports various environment variables related to Ascend NPU that can be used to configure its runtime behavior. This document provides a list of commonly used environment variables and aims to stay updated over time.

## Directly Used in SGLang

Environment VariableDescriptionDefault Value`SGLANG_NPU_USE_MLAPO`Adopts the `MLAPO` fusion operator in attention &lt;br/&gt; preprocessing stage of the MLA model.`false``SGLANG_USE_FIA_NZ`Reshapes KV Cache for FIA NZ format.&lt;br/&gt; `SGLANG_USE_FIA_NZ` must be enabled with `SGLANG_NPU_USE_MLAPO``false``SGLANG_NPU_USE_MULTI_STREAM`Enable dual-stream computation of shared experts &lt;br/&gt; and routing experts in DeepSeek models.&lt;br/&gt; Enable dual-stream computation in DeepSeek NSA Indexer.`false``SGLANG_NPU_DISABLE_ACL_FORMAT_WEIGHT`Disable cast model weight tensor to a specific NPU &lt;br/&gt; ACL format.`false``SGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK`The maximum number of dispatched tokens on each rank.`128`

## Used in DeepEP Ascend

Environment VariableDescriptionDefault Value`DEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS`Enable ant-moving function in dispatch stage. Indicates &lt;br/&gt; the number of tokens transmitted per round on each rank.`8192``DEEPEP_NORMAL_LONG_SEQ_ROUND`Enable ant-moving function in dispatch stage. Indicates &lt;br/&gt; the number of rounds transmitted on each rank.`1``DEEPEP_NORMAL_COMBINE_ENABLE_LONG_SEQ`Enable ant-moving function in combine stage. &lt;br/&gt; The value `0` means disabled.`0``MOE_ENABLE_TOPK_NEG_ONE`Needs to be enabled when the expert ID to be processed by &lt;br/&gt; DEEPEP contains -1.`0``DEEP_NORMAL_MODE_USE_INT8_QUANT`Quantizes x to int8 and returns (tensor, scales) in dispatch operator.`0`

## Others

Environment VariableDescriptionDefault Value`TASK_QUEUE_ENABLE`Used to control the optimization level of the dispatch queue&lt;br/&gt; about the task\_queue operator. [Detail](https://www.hiascend.com/document/detail/zh/Pytorch/730/comref/Envvariables/docs/zh/environment_variable_reference/TASK_QUEUE_ENABLE.md)`1``INF_NAN_MODE_ENABLE`Controls whether the chip uses saturation mode or INF\_NAN mode. [Detail](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/800alpha001/apiref/envref/envref_07_0056.html)`1``STREAMS_PER_DEVICE`Configures the maximum number of streams for the stream pool. [Detail](https://www.hiascend.com/document/detail/zh/Pytorch/720/comref/Envvariables/Envir_041.html)`32``PYTORCH_NPU_ALLOC_CONF`Controls the behavior of the cache allocator. &lt;br/&gt;This variable changes memory usage and may cause performance fluctuations. [Detail](https://www.hiascend.com/document/detail/zh/Pytorch/700/comref/Envvariables/Envir_012.html)`ASCEND_MF_STORE_URL`The address of config store in MemFabric during PD separation, &lt;br/&gt;which is generally set to the IP address of the P primary node&lt;br/&gt; with an arbitrary port number.`ASCEND_LAUNCH_BLOCKING`Controls whether synchronous mode is enabled during operator execution. [Detail](https://www.hiascend.com/document/detail/zh/Pytorch/710/comref/Envvariables/Envir_006.html)`0``HCCL_OP_EXPANSION_MODE`Configures the expansion position for communication algorithm scheduling. [Detail](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/800alpha001/apiref/envref/envref_07_0094.html)`HCCL_BUFFSIZE`Controls the size of the buffer area for shared data between two NPUs. &lt;br/&gt;The unit is MB, and the value must be greater than or equal to 1. [Detail](https://www.hiascend.com/document/detail/zh/Pytorch/60RC3/ptmoddevg/trainingmigrguide/performance_tuning_0047.html)`200``HCCL_SOCKET_IFNAME`Configures the name of the network card used by the Host &lt;br/&gt;during HCCL initialization. [Detail](https://www.hiascend.com/document/detail/zh/canncommercial/81RC1/apiref/envvar/envref_07_0075.html)`GLOO_SOCKET_IFNAME`Configures the network interface name for GLOO communication.