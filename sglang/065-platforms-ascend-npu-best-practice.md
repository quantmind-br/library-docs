---
title: Best Practice on Ascend NPU — SGLang
url: https://docs.sglang.io/platforms/ascend_npu_best_practice.html
source: crawler
fetched_at: 2026-02-04T08:48:11.46330615-03:00
rendered_js: false
word_count: 1605
summary: This document provides optimal configuration settings and deployment best practices for running DeepSeek R1 models on Huawei Ascend NPU hardware using SGLang. It details environment setup, prefill-decode separation, and benchmarking procedures for various performance requirements.
tags:
    - ascend-npu
    - deepseek-r1
    - sglang
    - model-deployment
    - performance-tuning
    - hardware-acceleration
    - inference-optimization
    - huawei-atlas
category: configuration
---

This section describes the best practice data of mainstream LLM models such as DeepSeek and Qwen on the Ascend Npu. If you encounter issues or have any questions, please [open an issue](https://github.com/sgl-project/sglang/issues).

## Optimal Configuration[#](#optimal-configuration "Link to this heading")

### DeepSeek R1 High Performance 50ms 1[#](#deepseek-r1-high-performance-50ms-1 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 32Card

DeployMode: PD Separation

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#model-deployment "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000
exportSGLANG_SET_CPU_AFFINITY=1
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32

exportASCEND_MF_STORE_URL="tcp://your prefill ip1:24669"

P_IP=('your prefill ip1''your prefill ip2')

D_IP=('your decode ip1''your decode ip2')

MODEL_PATH=xxx

exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_USE_FIA_NZ=1

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`
echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"
# prefill
foriin"${!P_IP[@]}";
do
if[["$LOCAL_HOST1"=="${P_IP[$i]}"||"$LOCAL_HOST2"=="${P_IP[$i]}"]];
then
echo"${P_IP[$i]}"
exportHCCL_BUFFSIZE=1536
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportTASK_QUEUE_ENABLE=2

exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modeprefill--host${P_IP[$i]}\
--port8000--disaggregation-bootstrap-port$((8998+$i))--trust-remote-code--nnodes1--node-rank0\
--tp-size16--mem-fraction-static0.81--attention-backendascend--devicenpu--quantizationmodelslim\
--disaggregation-transfer-backendascend--max-running-requests8--context-length8192--disable-radix-cache\
--chunked-prefill-size-1--max-prefill-tokens28680--moe-a2a-backenddeepep--deepep-modenormal\
--speculative-algorithmNEXTN--speculative-num-steps1--speculative-eagle-topk1--speculative-num-draft-tokens2\
--dp-size2--enable-dp-attention--disable-shared-experts-fusion--dtypebfloat16--enable-attn-tp-input-scattered
NODE_RANK=$i
break
fi
done

# decode
foriin"${!D_IP[@]}";
do
if[["$LOCAL_HOST1"=="${D_IP[$i]}"||"$LOCAL_HOST2"=="${D_IP[$i]}"]];
then
echo"${D_IP[$i]}"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportHCCL_BUFFSIZE=650
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=78
exportTASK_QUEUE_ENABLE=1
exportSGLANG_SCHEDULER_SKIP_ALL_GATHER=1
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modedecode--host${D_IP[$i]}\
--port8001--trust-remote-code--dist-init-addr${D_IP[0]}:5000--nnodes2--node-rank$i--tp-size32--dp-size32\
--mem-fraction-static0.815--max-running-requests832--attention-backendascend--devicenpu--quantizationmodelslim\
--moe-a2a-backenddeepep--enable-dp-attention--deepep-modelow_latency--enable-dp-lm-head--moe-dense-tp1\
--cuda-graph-bs1214161820222426--disaggregation-transfer-backendascend--watchdog-timeout9000--context-length8192\
--speculative-algorithmNEXTN--speculative-num-steps2--speculative-eagle-topk1--speculative-num-draft-tokens3\
--tokenizer-worker-num4--prefill-round-robin-balance--disable-shared-experts-fusion--dtypebfloat16\
--load-balance-methoddecode_round_robin
NODE_RANK=$i
break
fi
done
```

```
exportSGLANG_DP_ROUND_ROBIN=1
python-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://P_IP:80008998\
--prefillhttp://P_IP:80008999\
--decodehttp://D_IP:8001\
--host127.0.0.1\
--port6688\
--mini-lb
```

#### Benchmark[#](#benchmark "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6688--max-concurrency768--random-input-len3500--random-output-len1500--num-prompts3072--random-range-ratio1--request-rate16
```

### DeepSeek R1 Low Latency 20ms 1[#](#deepseek-r1-low-latency-20ms-1 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 32Card

DeployMode: PD Separation

DataSets: 6K1.6K

TPOT: 20ms

#### Model Deployment[#](#id3 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000
exportSGLANG_SET_CPU_AFFINITY=1
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32
exportASCEND_MF_STORE_URL="tcp://your prefill ip1:24669"

P_IP=('your prefill ip1''your prefill ip2')

D_IP=('your decode ip1''your decode ip2')

MODEL_PATH=xxx

exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_USE_FIA_NZ=1

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`
echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"
# prefill
foriin"${!P_IP[@]}";
do
if[["$LOCAL_HOST1"=="${P_IP[$i]}"||"$LOCAL_HOST2"=="${P_IP[$i]}"]];
then
echo"${P_IP[$i]}"
exportHCCL_BUFFSIZE=1536
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportTASK_QUEUE_ENABLE=2

exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modeprefill--host${P_IP[$i]}\
--port8000--disaggregation-bootstrap-port$((8998+$i))--trust-remote-code--nnodes1--node-rank0\
--tp-size16--mem-fraction-static0.81--attention-backendascend--devicenpu--quantizationmodelslim\
--disaggregation-transfer-backendascend--max-running-requests4--context-length8192--disable-radix-cache\
--chunked-prefill-size-1--max-prefill-tokens28680--moe-a2a-backenddeepep--deepep-modenormal\
--speculative-algorithmNEXTN--speculative-num-steps1--speculative-eagle-topk1--speculative-num-draft-tokens2\
--dp-size2--enable-dp-attention--disable-shared-experts-fusion--dtypebfloat16--enable-attn-tp-input-scattered
NODE_RANK=$i
break
fi
done

# decode
foriin"${!D_IP[@]}";
do
if[["$LOCAL_HOST1"=="${D_IP[$i]}"||"$LOCAL_HOST2"=="${D_IP[$i]}"]];
then
echo"${D_IP[$i]}"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportHCCL_BUFFSIZE=650
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=12
exportTASK_QUEUE_ENABLE=1
exportSGLANG_SCHEDULER_SKIP_ALL_GATHER=1
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modedecode--host${D_IP[$i]}\
--port8001--trust-remote-code--dist-init-addrDIP1:5000--nnodes2--node-rank$i--tp-size32--dp-size16\
--mem-fraction-static0.75--max-running-requests32--attention-backendascend--devicenpu--quantizationmodelslim\
--moe-a2a-backenddeepep--enable-dp-attention--deepep-modelow_latency--enable-dp-lm-head--moe-dense-tp1\
--cuda-graph-bs246--disaggregation-transfer-backendascend--watchdog-timeout9000--context-length8192\
--speculative-algorithmNEXTN--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--tokenizer-worker-num4--prefill-round-robin-balance--disable-shared-experts-fusion--dtypebfloat16\
--load-balance-methoddecode_round_robin
NODE_RANK=$i
break
fi
done
```

```
exportSGLANG_DP_ROUND_ROBIN=1
python-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://P_IP:80008998\
--prefillhttp://P_IP:80008999\
--decodehttp://D_IP:8001\
--host127.0.0.1\
--port6688\
--mini-lb
```

#### Benchmark[#](#id4 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6688--max-concurrency32--random-input-len6000--random-output-len1600--num-prompts32--random-range-ratio1
```

### DeepSeek R1 Low Latency 20ms 2[#](#deepseek-r1-low-latency-20ms-2 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 32Card

DeployMode: PD Separation

DataSets: 3.9K1K

TPOT: 20ms

#### Model Deployment[#](#id5 "Link to this heading")

Please Turn to [DeepSeek R1 Low Latency 20ms](#deepseek-r1-low-latency-20ms-1)

#### Benchmark[#](#id6 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6688--max-concurrency768--random-input-len3900--random-output-len1000--num-prompts768--random-range-ratio1--request-rate16
```

### DeepSeek R1 Low Latency 20ms 3[#](#deepseek-r1-low-latency-20ms-3 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 32Card

DeployMode: PD Separation

DataSets: 3.5K1.5K

TPOT: 20ms

#### Model Deployment[#](#id7 "Link to this heading")

Please Turn to [DeepSeek R1 Low Latency 20ms](#deepseek-r1-low-latency-20ms-1)

#### Benchmark[#](#id8 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6688--max-concurrency768--random-input-len3500--random-output-len1500--num-prompts768--random-range-ratio1--request-rate16
```

### DeepSeek R1 Low Latency 20ms 4[#](#deepseek-r1-low-latency-20ms-4 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 32Card

DeployMode: PD Separation

DataSets: 3.5K1K

TPOT: 20ms

#### Model Deployment[#](#id9 "Link to this heading")

Please Turn to [DeepSeek R1 Low Latency 20ms](#deepseek-r1-low-latency-20ms-1)

#### Benchmark[#](#id10 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6688--max-concurrency768--random-input-len3500--random-output-len1000--num-prompts768--random-range-ratio1--request-rate16
```

### DeepSeek R1 High Performance 50ms 2[#](#deepseek-r1-high-performance-50ms-2 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 8Card

DeployMode: PD Mixed

DataSets: 2K2K

TPOT: 50ms

#### Model Deployment[#](#id11 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32
exportSGLANG_SCHEDULER_DECREASE_PREFILL_IDLE=1

exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo

exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=64
exportHCCL_BUFFSIZE=1600
exportDEEPEP_NORMAL_LONG_SEQ_ROUND=10
exportDEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS=512

MODEL_PATH=xxx

exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_ENABLE_SPEC_V2=1
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_USE_FIA_NZ=1
exportENABLE_MOE_NZ=1

python3-msglang.launch_server--model-path${MODEL_PATH}\
--tp16\
--trust-remote-code\
--attention-backendascend\
--devicenpu\
--quantizationmodelslim\
--watchdog-timeout9000\
--host127.0.0.1--port6699\
--cuda-graph-bs4816\
--mem-fraction-static0.74\
--max-running-requests256\
--disable-radix-cache--chunked-prefill-size-1--max-prefill-tokens1500\
--moe-a2a-backenddeepep--deepep-modeauto\
--enable-dp-attention--dp-size16--enable-dp-lm-head\
--speculative-algorithmNEXTN--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--dtypebfloat16
```

#### Benchmark[#](#id12 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6699--max-concurrency256--random-input-len2048--random-output-len2048--num-prompts1024--random-range-ratio1
```

### DeepSeek R1 High Performance 50ms 3[#](#deepseek-r1-high-performance-50ms-3 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 16Card

DeployMode: PD Separation

DataSets: 2K2K

TPOT: 50ms

#### Model Deployment[#](#id13 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32

exportASCEND_MF_STORE_URL="tcp://your prefill ip1:24667"

P_IP=('your prefill ip1')

D_IP=('your decode ip1')

MODEL_PATH=xxx

exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_USE_FIA_NZ=1
exportENABLE_MOE_NZ=1

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`
echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

# prefill
foriin"${!P_IP[@]}";
do
if[["$LOCAL_HOST1"=="${P_IP[$i]}"||"$LOCAL_HOST2"=="${P_IP[$i]}"]];
then
echo"${P_IP[$i]}"
exportHCCL_BUFFSIZE=1536
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportTASK_QUEUE_ENABLE=2

exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modeprefill--host${P_IP[$i]}\
--port8000--disaggregation-bootstrap-port$((8998+$i))--trust-remote-code--nnodes1--node-rank0\
--tp-size16--mem-fraction-static0.6--attention-backendascend--devicenpu--quantizationmodelslim\
--disaggregation-transfer-backendascend--max-running-requests8--context-length8192--disable-radix-cache\
--chunked-prefill-size32768--max-prefill-tokens28680--moe-a2a-backenddeepep--deepep-modenormal\
--speculative-algorithmNEXTN--speculative-num-steps1--speculative-eagle-topk1--speculative-num-draft-tokens2\
--dp-size2--enable-dp-attention--disable-shared-experts-fusion--dtypebfloat16
NODE_RANK=$i
break
fi
done

# decode
foriin"${!D_IP[@]}";
do
if[["$LOCAL_HOST1"=="${D_IP[$i]}"||"$LOCAL_HOST2"=="${D_IP[$i]}"]];
then
echo"${D_IP[$i]}"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportHCCL_BUFFSIZE=720
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=96
exportTASK_QUEUE_ENABLE=1
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modedecode--host${D_IP[$i]}\
--port8001--trust-remote-code--nnodes1--node-rank0--tp-size16--dp-size16\
--mem-fraction-static0.8--max-running-requests384--attention-backendascend--devicenpu--quantizationmodelslim\
--moe-a2a-backenddeepep--enable-dp-attention--deepep-modelow_latency--enable-dp-lm-head\
--cuda-graph-bs81012141618202224--disaggregation-transfer-backendascend--watchdog-timeout9000--context-length8192\
--speculative-algorithmNEXTN--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--prefill-round-robin-balance--disable-shared-experts-fusion--dtypebfloat16--tokenizer-worker-num4\
--load-balance-methoddecode_round_robin
NODE_RANK=$i
break
fi
done
```

```
exportSGLANG_DP_ROUND_ROBIN=1
python-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://P_IP:80008998\
--decodehttp://D_IP:8001\
--host127.0.0.1\
--port6688\
--mini-lb
```

#### Benchmark[#](#id14 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6688--max-concurrency400--random-input-len2048--random-output-len2048--num-prompts3200--random-range-ratio1--request-rate8
```

### DeepSeek R1 High Performance 50ms 4[#](#deepseek-r1-high-performance-50ms-4 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 8Card

DeployMode: PD Mixed

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id15 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

exportSTREAMS_PER_DEVICE=32
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportSGLANG_SCHEDULER_DECREASE_PREFILL_IDLE=1
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=36
exportHCCL_BUFFSIZE=1600
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_ENABLE_SPEC_V2=1
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_USE_FIA_NZ=1
exportENABLE_MOE_NZ=1

MODEL_PATH=xxx

python3-msglang.launch_server--model-path${MODEL_PATH}\
--tp16\
--trust-remote-code\
--attention-backendascend\
--devicenpu\
--quantizationmodelslim\
--watchdog-timeout9000\
--host127.0.0.1--port6699\
--cuda-graph-bs81624283236\
--mem-fraction-static0.71\
--max-running-requests144\
--context-length8188--disable-radix-cache--chunked-prefill-size-1--max-prefill-tokens9000\
--moe-a2a-backenddeepep--deepep-modeauto\
--enable-dp-attention--dp-size4--enable-dp-lm-head\
--speculative-algorithmNEXTN--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--dtypebfloat16
```

#### Benchmark[#](#id16 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6699--max-concurrency144--random-input-len3500--random-output-len1500--num-prompts576--random-range-ratio1
```

### DeepSeek R1 High Performance 50ms 5[#](#deepseek-r1-high-performance-50ms-5 "Link to this heading")

Model: Deepseek R1

Hardware: Atlas 800I A3 16Card

DeployMode: PD Separation

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id17 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32

exportASCEND_MF_STORE_URL="tcp://your prefill ip1:24667"

P_IP=('your prefill ip1')

D_IP=('your decode ip1')

MODEL_PATH=xxx

exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_USE_FIA_NZ=1
exportENABLE_MOE_NZ=1

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`
echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

# prefill
foriin"${!P_IP[@]}";
do
if[["$LOCAL_HOST1"=="${P_IP[$i]}"||"$LOCAL_HOST2"=="${P_IP[$i]}"]];
then
echo"${P_IP[$i]}"
exportHCCL_BUFFSIZE=1536
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportTASK_QUEUE_ENABLE=2

exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modeprefill--host${P_IP[$i]}\
--port8000--disaggregation-bootstrap-port$((8998+$i))--trust-remote-code--nnodes1--node-rank0\
--tp-size16--mem-fraction-static0.6--attention-backendascend--devicenpu--quantizationmodelslim\
--disaggregation-transfer-backendascend--max-running-requests8--context-length8192--disable-radix-cache\
--chunked-prefill-size-1--max-prefill-tokens28680--moe-a2a-backenddeepep--deepep-modenormal\
--speculative-algorithmNEXTN--speculative-num-steps1--speculative-eagle-topk1--speculative-num-draft-tokens2\
--dp-size2--enable-dp-attention--disable-shared-experts-fusion--dtypebfloat16
NODE_RANK=$i
break
fi
done

# decode
foriin"${!D_IP[@]}";
do
if[["$LOCAL_HOST1"=="${D_IP[$i]}"||"$LOCAL_HOST2"=="${D_IP[$i]}"]];
then
echo"${D_IP[$i]}"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportHCCL_BUFFSIZE=720
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=96
exportTASK_QUEUE_ENABLE=1
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modedecode--host${D_IP[$i]}\
--port8001--trust-remote-code--nnodes1--node-rank0--tp-size16--dp-size16\
--mem-fraction-static0.8--max-running-requests384--attention-backendascend--devicenpu--quantizationmodelslim\
--moe-a2a-backenddeepep--enable-dp-attention--deepep-modelow_latency--enable-dp-lm-head\
--cuda-graph-bs81012141618202224--disaggregation-transfer-backendascend--watchdog-timeout9000--context-length8192\
--speculative-algorithmNEXTN--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--prefill-round-robin-balance--disable-shared-experts-fusion--dtypebfloat16--tokenizer-worker-num4\
--load-balance-methoddecode_round_robin
NODE_RANK=$i
break
fi
done
```

```
exportSGLANG_DP_ROUND_ROBIN=1
python-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://P_IP:80008998\
--decodehttp://D_IP:8001\
--host127.0.0.1\
--port6688\
--mini-lb
```

#### Benchmark[#](#id18 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6688--max-concurrency384--random-input-len3500--random-output-len1500--num-prompts1536--random-range-ratio1
```

### Deepseek V32 Low Latency 30ms[#](#deepseek-v32-low-latency-30ms "Link to this heading")

Model: Deepseek V3.2

Hardware: Atlas 800I A3 32Card

DeployMode: PD Separation

DataSets: 64K3K

TPOT: 30ms

#### Model Deployment[#](#id19 "Link to this heading")

Deploy Prefill Instance

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING

source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportLD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api/lib/:${LD_LIBRARY_PATH}
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32

exportHCCL_BUFFSIZE=1024
exportDEEPEP_NORMAL_LONG_SEQ_ROUND=5
exportDEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS=512

MODEL_PATH=xxx

exportSGLANG_NPU_USE_MLAPO=1
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportSGLANG_NPU_USE_MULTI_STREAM=1
exportHCCL_OP_EXPANSION_MODE=AIV

IPs=('your prefill ip1''your prefill ip2')

# get IP in current node
LOCAL_HOST=`hostname-I|awk-F" "'{print$1}'`
echo"LOCAL_HOST = "${LOCAL_HOST}
# get node index
foriin"${!IPs[@]}";
do
echo"LOCAL_HOST=${LOCAL_HOST}, IPs[${i}]=${IPs[$i]}"
if["$LOCAL_HOST"=="${IPs[$i]}"];then
echo"Node Rank : ${i}"
VC_TASK_INDEX=$i
break
fi
done

IFNAMES=('xxx''xxx')

exportHCCL_SOCKET_IFNAME=${IFNAMES[$VC_TASK_INDEX]}
exportGLOO_SOCKET_IFNAME=${HCCL_SOCKET_IFNAME}
echo"HCCL_SOCKET_IFNAME : ${HCCL_SOCKET_IFNAME}"
nnodes=${#IPs[@]}
tp_size=`expr16\*${nnodes}`
exportASCEND_MF_STORE_URL=tcp://${IPs[0]}:24667

python3-msglang.launch_server--model-path${MODEL_PATH}\
--tp$tp_size\
--trust-remote-code\
--attention-backendascend\
--devicenpu\
--watchdog-timeout9000\
--host${IPs[$VC_TASK_INDEX]}--port8000\
--mem-fraction-static0.73\
--disable-radix-cache--chunked-prefill-size-1--max-prefill-tokens68000\
--max-running-requests1\
--moe-a2a-backenddeepep--deepep-modenormal\
--quantizationmodelslim\
--disaggregation-transfer-backendascend\
--disaggregation-modeprefill\
--disable-cuda-graph\
--nnodes$nnodes--node-rank$VC_TASK_INDEX\
--disaggregation-bootstrap-port8995\
--enable-nsa-prefill-context-parallel--moe-dense-tp-size1\
--speculative-algorithmNEXTN--speculative-num-steps1--speculative-eagle-topk1--speculative-num-draft-tokens2\
--dist-init-addr${IPs[0]}:10000
```

Deploy Decode Instance

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportLD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api/lib/:${LD_LIBRARY_PATH}
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH
exportASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32

MODEL_PATH=xxx

exportSGLANG_NPU_USE_MULTI_STREAM=1
exportSGLANG_NPU_USE_MLAPO=1
exportHCCL_OP_EXPANSION_MODE=AIV
exportSGLANG_SCHEDULER_SKIP_ALL_GATHER=1
exportTASK_QUEUE_ENABLE=0
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

IPs=('your decode ip1''your decode ip2')

exportprefill_ip=yourprefillip1
# get IP in current node
LOCAL_HOST=`hostname-I|awk-F" "'{print$1}'`
echo"LOCAL_HOST = "${LOCAL_HOST}
# get node index
foriin"${!IPs[@]}";
do
echo"LOCAL_HOST=${LOCAL_HOST}, IPs[${i}]=${IPs[$i]}"
if["$LOCAL_HOST"=="${IPs[$i]}"];then
echo"Node Rank : ${i}"
VC_TASK_INDEX=$i
break
fi
done

IFNAMES=('xxx''xxx')

exportHCCL_SOCKET_IFNAME=${IFNAMES[$VC_TASK_INDEX]}
exportGLOO_SOCKET_IFNAME=${HCCL_SOCKET_IFNAME}
nnodes=${#IPs[@]}
tp_size=`expr16\*${nnodes}`
exportASCEND_MF_STORE_URL=tcp://${prefill_ip}:24667

CHUNKED_SIZE=65536
DP=8
exportHCCL_BUFFSIZE=400
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=8

python3-msglang.launch_server--model-path${MODEL_PATH}\
--tp$tp_size\
--dp${DP}\
--ep$tp_size\
--moe-dense-tp-size1\
--enable-dp-attention\
--enable-dp-lm-head\
--trust-remote-code\
--attention-backendascend\
--devicenpu\
--watchdog-timeout9000\
--host${IPs[$VC_TASK_INDEX]}--port8001\
--mem-fraction-static0.79\
--disable-radix-cache\
--chunked-prefill-size-1--max-prefill-tokens68000\
--max-running-requests32\
--cuda-graph-max-bs4\
--moe-a2a-backenddeepep\
--deepep-modelow_latency\
--quantizationmodelslim\
--speculative-algorithmNEXTN--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--disaggregation-transfer-backendascend\
--disaggregation-modedecode\
--prefill-round-robin-balance\
--load-balance-methodround_robin\
--nnodes$nnodes--node-rank$VC_TASK_INDEX\
--dist-init-addr${IPs[0]}:10000--load-balance-methoddecode_round_robin
```

```
exportSGLANG_DP_ROUND_ROBIN=1
python-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://PIP1:80008995\
--decodehttp://DIP1:8001\
--host127.0.0.1\
--port6688\
--mini-lb
```

#### Benchmark[#](#id20 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6688--max-concurrency32--random-input-len64000--random-output-len3000--num-prompts64--random-range-ratio1
```

### Qwen3 235B High Throughput 50ms 1[#](#qwen3-235b-high-throughput-50ms-1 "Link to this heading")

Model: Qwen3 235B

Hardware: Atlas 800I A3 24Card

DeployMode: PD Separation

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id21 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING

source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=16

MODEL_PATH=xxx
exportASCEND_MF_STORE_URL="tcp://your prefill ip1:24667"
P_IP=('your prefill ip1')
D_IP=('your decode ip1''your decode ip2')
exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportSGLANG_DP_ROUND_ROBIN=1

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"


foriin"${!P_IP[@]}";
do
if[["$LOCAL_HOST1"=="${P_IP[$i]}"||"$LOCAL_HOST2"=="${P_IP[$i]}"]];
then
echo"${P_IP[$i]}"
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportDEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS=1024
exportDEEPEP_NORMAL_LONG_SEQ_ROUND=16
exportHCCL_BUFFSIZE=4300
exportTASK_QUEUE_ENABLE=2
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportSTREAMS_PER_DEVICE=32
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1

# P节点
python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modeprefill\
--host${P_IP[$i]}--port8000--disaggregation-bootstrap-port8995--trust-remote-code\
--nnodes1--node-rank$i--tp-size16--dp-size16--mem-fraction-static0.6\
--disable-radix-cache\
--attention-backendascend--devicenpu--quantizationmodelslim--disaggregation-transfer-backendascend\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--speculative-draft-model-quantizationunquant\
--max-running-requests128--chunked-prefill-size262144--max-prefill-tokens262144\
--enable-dp-attention\
--moe-a2a-backenddeepep--deepep-modenormal--dtypebfloat16
NODE_RANK=$i
break
fi
done


foriin"${!D_IP[@]}";
do
if[["$LOCAL_HOST1"=="${D_IP[$i]}"||"$LOCAL_HOST2"=="${D_IP[$i]}"]];
then
echo"${D_IP[$i]}"
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=24
exportHCCL_BUFFSIZE=512
exportHCCL_SOCKET_IFNAME=data0.3001
exportGLOO_SOCKET_IFNAME=data0.3001
exportSTREAMS_PER_DEVICE=32

python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modedecode\
--host${D_IP[$i]}--port8001--trust-remote-code\
--nnodes2--node-rank$i--tp-size32--dp-size32--mem-fraction-static0.83--max-running-requests768\
--attention-backendascend--devicenpu--quantizationmodelslim--enable-dp-attention\
--moe-a2a-backendascend_fuseep--cuda-graph-bs68121518202224\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-draft-model-quantizationunquant\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--dist-init-addrxxx:5000\
--disaggregation-transfer-backendascend--watchdog-timeout9000--context-length8192\
--prefill-round-robin-balance--enable-dp-lm-head--dtypebfloat16--tokenizer-worker-num4\
--load-balance-methoddecode_round_robin
NODE_RANK=$i
break
fi
done
```

```
exportSGLANG_DP_ROUND_ROBIN=1
python-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://PIP:80008995\
--decodehttp://DIP:8001\
--host127.0.0.1\
--port6688\
--mini-lb
```

#### Benchmark[#](#id22 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang-oai--host127.0.0.1--port7239--max-concurrency860--random-input-len3500--random-output-len1500--num-prompts3440--random-range-ratio1
```

### Qwen3 235B High Throughput 50ms 2[#](#qwen3-235b-high-throughput-50ms-2 "Link to this heading")

Model: Qwen3 235B

Hardware: Atlas 800I A3 8Card

DeployMode: PD Mixed

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id23 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=1600
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportSGLANG_SCHEDULER_DECREASE_PREFILL_IDLE=2

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7439--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests272--context-length8192--dtypebfloat16\
--chunked-prefill-size32768--max-prefill-tokens32768\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--disable-radix-cache--moe-a2a-backenddeepep--deepep-modeauto--speculative-draft-model-quantizationunquant\
--tp16--dp-size16--enable-dp-attention--enable-dp-lm-head--mem-fraction-static0.8--cuda-graph-bs346810121314151617
```

#### Benchmark[#](#id24 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency272--random-input-len3500--random-output-len1500--num-prompts1088--random-range-ratio1
```

### Qwen3-235B Atlas 800I A3-8Card PD Mixed 2K-2K 100ms[#](#qwen3-235b-atlas-800i-a3-8card-pd-mixed-2k-2k-100ms "Link to this heading")

Model: Qwen3 235B

Hardware: Atlas 800I A3 8Card

DeployMode: PD Mixed

DataSets: 2K2K

TPOT: 100ms

#### Model Deployment[#](#id25 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=1200
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7439--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests576--context-length8192--dtypebfloat16\
--chunked-prefill-size32768--max-prefill-tokens458880\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--disable-radix-cache--moe-a2a-backenddeepep--deepep-modeauto--speculative-draft-model-quantizationunquant\
--tp16--dp-size16--enable-dp-attention--enable-dp-lm-head--mem-fraction-static0.81--cuda-graph-bs81620243236
```

#### Benchmark[#](#id26 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency576--random-input-len2000--random-output-len2000--num-prompts576--random-range-ratio1
```

### Qwen3 235B High Throughput 50ms 3[#](#qwen3-235b-high-throughput-50ms-3 "Link to this heading")

Model: Qwen3 235B

Hardware: Atlas 800I A3 8Card

DeployMode: PD Mixed

DataSets: 2K2K

TPOT: 50ms

#### Model Deployment[#](#id27 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=2100
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7439--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests480--context-length8192--dtypebfloat16\
--chunked-prefill-size-1--max-prefill-tokens4096--speculative-draft-model-quantizationunquant\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--disable-radix-cache--moe-a2a-backenddeepep--deepep-modeauto\
--tp16--dp-size16--enable-dp-attention--enable-dp-lm-head--mem-fraction-static0.75--cuda-graph-bs68101215182830
```

#### Benchmark[#](#id28 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency480--random-input-len2048--random-output-len2048--num-prompts480--random-range-ratio1
```

### Qwen3 235B High Throughput 50ms 4[#](#qwen3-235b-high-throughput-50ms-4 "Link to this heading")

Model: Qwen3 235B

Hardware: Atlas 800I A3 16Card

DeployMode: PD Mixed

DataSets: 2K2K

TPOT: 50ms

#### Model Deployment[#](#id29 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=1600
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
exportHCCL_OP_EXPANSION_MODE="AIV"

MIX_IP=('IP1''IP2')

foriin"${!MIX_IP[@]}";
do
if[["$LOCAL_HOST1"=="${MIX_IP[$i]}"||"$LOCAL_HOST2"=="${MIX_IP[$i]}"]];
then
echo"${MIX_IP[$i]}"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path${MODEL_PATH}\
--host127.0.0.1--port7439--trust-remote-code\
--nnodes2--node-rank$i--tp-size32--dp-size32--mem-fraction-static0.8--max-running-requests768\
--attention-backendascend--devicenpu--quantizationmodelslim--enable-dp-attention\
--moe-a2a-backenddeepep--deepep-modeauto--cuda-graph-bs6810121824\
--dist-init-addr${MIX_IP[0]}:5000--chunked-prefill-size131072--max-prefill-tokens458880\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx--speculative-draft-model-quantization=unquant\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--context-length8192--disable-radix-cache\
--enable-dp-lm-head--dtypebfloat16
NODE_RANK=$i
break
fi
done
```

#### Benchmark[#](#id30 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency768--random-input-len2000--random-output-len2000--num-prompts768--random-range-ratio1
```

### Qwen3 235B Low Latency 10ms[#](#qwen3-235b-low-latency-10ms "Link to this heading")

Model: Qwen3 235B

Hardware: Atlas 800I A3 8Card

DeployMode: PD Mixed

DataSets: 11K1K

TPOT: 10ms

#### Model Deployment[#](#id31 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=1600
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7439--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests1--dtypebfloat16\
--chunked-prefill-size-1--max-prefill-tokens16384--speculative-draft-model-quantizationunquant\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps4--speculative-eagle-topk1--speculative-num-draft-tokens5\
--disable-radix-cache--enable-dp-lm-head\
--tp16--mem-fraction-static0.78--cuda-graph-bs1
```

#### Benchmark[#](#id32 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency1--random-input-len11000--random-output-len1000--num-prompts1--random-range-ratio1
```

### Qwen3 32B Low Latency 18ms[#](#qwen3-32b-low-latency-18ms "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A3 4Card

DeployMode: PD Mixed

DataSets: 6K1.5K

TPOT: 18ms

#### Model Deployment[#](#id33 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7439--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu\
--max-running-requests32\
--disable-radix-cache\
--chunked-prefill-size24576--max-prefill-tokens65536\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps4--speculative-eagle-topk1--speculative-num-draft-tokens5\
--tp-size8--mem-fraction-static0.72--cuda-graph-bs8162432--dtypebfloat16
```

#### Benchmark[#](#id34 "Link to this heading")

We tested it based on the GSM8K dataset.

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency32--random-output-len1500--random-input-len6000--num-prompts32--random-range-ratio1
```

### Qwen3 32B Low Latency 11ms[#](#qwen3-32b-low-latency-11ms "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A3 4Card

DeployMode: PD Mixed

DataSets: 4K1.5K

TPOT: 11ms

#### Model Deployment[#](#id35 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7339--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu\
--max-running-requests1\
--disable-radix-cache\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps4--speculative-eagle-topk1--speculative-num-draft-tokens5\
--chunked-prefill-size24576--max-prefill-tokens65536\
--tp-size8--mem-fraction-static0.72--cuda-graph-bs1--dtypebfloat16
```

#### Benchmark[#](#id36 "Link to this heading")

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7239--random-range-ratio1--max-concurrency1--random-output-len1500--random-input-len4096--num-prompts4
```

### Qwen3 32B Low Latency 12ms[#](#qwen3-32b-low-latency-12ms "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A3 8Card

DeployMode: PD Mixed

DataSets: 18K4K

TPOT: 12ms

#### Model Deployment[#](#id37 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7339--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu\
--max-running-requests1\
--disable-radix-cache--speculative-draft-model-quantizationunquant\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps4--speculative-eagle-topk1--speculative-num-draft-tokens5\
--chunked-prefill-size-1--max-prefill-tokens65536\
--tp-size16--mem-fraction-static0.72--cuda-graph-bs1--dtypebfloat16
```

#### Benchmark[#](#id38 "Link to this heading")

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7339--random-range-ratio1--max-concurrency1--random-output-len18000--random-input-len4000--num-prompts1
```

### Qwen3 32B High Throughput 50ms 1[#](#qwen3-32b-high-throughput-50ms-1 "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A3 2Card

DeployMode: PD Mixed

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id39 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH


MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7239--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests78\
--disable-radix-cache--speculative-draft-model-quantizationunquant\
--chunked-prefill-size65536--max-prefill-tokens65536\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--tp-size4--mem-fraction-static0.7--cuda-graph-bs163264687278--dtypebfloat16
```

#### Benchmark[#](#id40 "Link to this heading")

We tested it based on the GSM8K dataset.

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7239--max-concurrency78--random-output-len1500--random-input-len3500--num-prompts312--random-range-ratio1
```

### Qwen3 32B High Throughput 50ms 2[#](#qwen3-32b-high-throughput-50ms-2 "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A3 2Card

DeployMode: PD Mixed

DataSets: 2K2K

TPOT: 50ms

#### Model Deployment[#](#id41 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7239--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests120\
--disable-radix-cache--speculative-draft-model-quantizationunquant\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--chunked-prefill-size-1--max-prefill-tokens49152\
--tp-size4--mem-fraction-static0.7--cuda-graph-bs54606672788490108114120--dtypebfloat16
```

#### Benchmark[#](#id42 "Link to this heading")

We tested it based on the GSM8K dataset.

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7239--max-concurrency120--random-output-len2000--random-input-len2000--num-prompts480--random-range-ratio1
```

### Qwen3 32B High Throughput 50ms 3[#](#qwen3-32b-high-throughput-50ms-3 "Link to this heading")

Model: Qwen3 30B

Hardware: Atlas 800I A3 1Card

DeployMode: PD Mixed

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id43 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportDISABLE_EAGLE3_QUANT=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7239--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests192\
--disable-radix-cache\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--chunked-prefill-size-1--max-prefill-tokens32768\
--tp-size2--mem-fraction-static0.86--cuda-graph-bs428896132144156172178192--dtypebfloat16
```

#### Benchmark[#](#id44 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7239--max-concurrency156--random-input-len3500--random-output-len1500--num-prompts624--random-range-ratio1
```

### Qwen3 480B High Throughput 50ms 1[#](#qwen3-480b-high-throughput-50ms-1 "Link to this heading")

Model: Qwen3 480B

Hardware: Atlas 800I A3 24Card

DeployMode: PD Separation

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id45 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING

source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=16

MODEL_PATH=xxx
exportASCEND_MF_STORE_URL="tcp://PIP:24667"
P_IP=('PIP')
D_IP=('DIP1''DIP2')
exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"


foriin"${!P_IP[@]}";
do
if[["$LOCAL_HOST1"=="${P_IP[$i]}"||"$LOCAL_HOST2"=="${P_IP[$i]}"]];
then
echo"${P_IP[$i]}"
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportDEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS=1024
exportDEEPEP_NORMAL_LONG_SEQ_ROUND=16
exportHCCL_BUFFSIZE=4300
exportTASK_QUEUE_ENABLE=2
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportSTREAMS_PER_DEVICE=32
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1

python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modeprefill\
--host${P_IP[$i]}--port8000--disaggregation-bootstrap-port8995--trust-remote-code\
--nnodes1--node-rank$i--tp-size16--dp-size2--mem-fraction-static0.6\
--disable-radix-cache\
--attention-backendascend--devicenpu--quantizationmodelslim--disaggregation-transfer-backendascend\
--max-running-requests128--chunked-prefill-size65536--max-prefill-tokens262144\
--enable-dp-attention\
--moe-a2a-backenddeepep--deepep-modenormal--dtypebfloat16
NODE_RANK=$i
break
fi
done

foriin"${!D_IP[@]}";
do
if[["$LOCAL_HOST1"=="${D_IP[$i]}"||"$LOCAL_HOST2"=="${D_IP[$i]}"]];
then
echo"${D_IP[$i]}"
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=72
exportHCCL_BUFFSIZE=512
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
exportSTREAMS_PER_DEVICE=32

python-msglang.launch_server--model-path${MODEL_PATH}--disaggregation-modedecode\
--host${D_IP[$i]}--port8001--trust-remote-code\
--nnodes2--node-rank$i--tp-size32--dp-size4--mem-fraction-static0.73--max-running-requests384\
--attention-backendascend--devicenpu--quantizationmodelslim--enable-dp-attention\
--moe-a2a-backendascend_fuseep--cuda-graph-bs163248566472808896\
--dist-init-addrDIP1:5000\
--disaggregation-transfer-backendascend--watchdog-timeout9000--context-length8192\
--prefill-round-robin-balance--enable-dp-lm-head--dtypebfloat16--tokenizer-worker-num4--load-balance-methoddecode_round_robin
NODE_RANK=$i
break
fi
done
```

```
exportSGLANG_DP_ROUND_ROBIN=1
python-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://PIP:80008995\
--decodehttp://DIP:8001\
--host127.0.0.1\
--port6688\
--mini-lb
```

#### Benchmark[#](#id46 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7239--max-concurrency410--random-input-len3500--random-output-len1500--num-prompts1640--random-range-ratio1--request-rate8
```

### Qwen3 480B High Throughput 50ms 2[#](#qwen3-480b-high-throughput-50ms-2 "Link to this heading")

Model: Qwen3 480B

Hardware: Atlas 800I A3 16Card

DeployMode: PD Mixed

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id47 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=16

exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=1800
exportHCCL_SOCKET_IFNAME=xxx
exportGLOO_SOCKET_IFNAME=xxx
exportHCCL_OP_EXPANSION_MODE="AIV"

MIX_IP=('IP1''IP2')

foriin"${!MIX_IP[@]}";
do
if[["$LOCAL_HOST1"=="${MIX_IP[$i]}"||"$LOCAL_HOST2"=="${MIX_IP[$i]}"]];
then
echo"${MIX_IP[$i]}"

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7439--trust-remote-code--nnodes2--node-rank$i\
--dist-init-addr141.61.133.128:5000\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests288--context-length8192--dtypebfloat16\
--chunked-prefill-size114688--max-prefill-tokens458880\
--disable-radix-cache--moe-a2a-backenddeepep--deepep-modeauto\
--tp32--dp-size4--enable-dp-attention--enable-dp-lm-head--mem-fraction-static0.7--cuda-graph-bs566472
NODE_RANK=$i
break
fi
done
```

#### Benchmark[#](#id48 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency288--random-input-len3500--random-output-len1500--num-prompts1152--random-range-ratio1--request-rate20
```

### Qwen3 480B High Throughput 50ms 3[#](#qwen3-480b-high-throughput-50ms-3 "Link to this heading")

Model: Qwen3 480B

Hardware: Atlas 800I A3 8Card

DeployMode: PD Mixed

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id49 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=2100
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7439--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests80--context-length8192--dtypebfloat16\
--chunked-prefill-size28672--max-prefill-tokens458880\
--disable-radix-cache--moe-a2a-backenddeepep--deepep-modeauto--enable-dp-attention--enable-dp-lm-head\
--tp16--dp-size4--mem-fraction-static0.7--cuda-graph-bs162024
```

#### Benchmark[#](#id50 "Link to this heading")

```
python-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency80--random-input-len3500--random-output-len1500--num-prompts320--random-range-ratio1
```

### Qwen3 Next High Throughput 50ms[#](#qwen3-next-high-throughput-50ms "Link to this heading")

Model: Qwen3 Next

Hardware: Atlas 800I A3 2Card

DeployMode: PD Mixed

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id51 "Link to this heading")

```
exportcann_path=/usr/local/Ascend/ascend-toolkit/latest
source/usr/local/Ascend/driver/bin/setenv.bash
source${cann_path}/../set_env.sh
source${cann_path}/../../nnal/atb/set_env.sh
source${cann_path}/opp/vendors/customize/bin/set_env.bash
exportASCEND_HOME_PATH=${cann_path}
source/usr/local/Ascend/8.5.0/bisheng_toolkit/set_env.sh

echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo

exportHCCL_OP_EXPANSION_MODE=AIV
exportHCCL_ALGO="level0:NA;level1:ring"

exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=20
exportHCCL_BUFFSIZE=2000

python-msglang.launch_server\
--model-path/mnt/share/weight/Qwen3-Next-80B-A3B-Instruct-W8A8-3\
--host127.0.0.1\
--port6699\
--tp-size4\
--devicenpu\
--attention-backendascend\
--mem-fraction-static0.685\
--max-running-requests80\
--watchdog-timeout3600\
--disable-radix-cache\
--cuda-graph-bs80\
--max-prefill-tokens28672--max-total-tokens450560\
--moe-a2a-backenddeepep--deepep-modeauto\
--quantizationmodelslim\
--chunked-prefill-size-1
```

#### Benchmark[#](#id52 "Link to this heading")

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port6699--max-concurrency80--random-output-len1536--random-input-len3584--num-prompts160--random-range-ratio1
```

### Qwen3 32B A2 Low Latency 18ms[#](#qwen3-32b-a2-low-latency-18ms "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A2 8Card

DeployMode: PD Mixed

DataSets: 6K1.5K

TPOT: 18ms

#### Model Deployment[#](#id53 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7439--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests32\
--disable-radix-cache\
--chunked-prefill-size24576--max-prefill-tokens65536\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps4--speculative-eagle-topk1--speculative-num-draft-tokens5\
--tp-size8--mem-fraction-static0.72--cuda-graph-bs8162432--dtypebfloat16
```

#### Benchmark[#](#id54 "Link to this heading")

We tested it based on the GSM8K dataset.

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7439--max-concurrency32--random-output-len1500--random-input-len6000--num-prompts32--random-range-ratio1
```

### Qwen3 32B A2 Low Latency 11ms[#](#qwen3-32b-a2-low-latency-11ms "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A2 8Card

DeployMode: PD Mixed

DataSets: 4K1.5K

TPOT: 11ms

#### Model Deployment[#](#id55 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportDISABLE_EAGLE3_QUANT=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7339--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu\
--max-running-requests32\
--disable-radix-cache\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps4--speculative-eagle-topk1--speculative-num-draft-tokens5\
--chunked-prefill-size-1--max-prefill-tokens65536\
--tp-size8--mem-fraction-static0.72--cuda-graph-bs1461218243032--dtypebfloat16
```

#### Benchmark[#](#id56 "Link to this heading")

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7339--random-range-ratio1--max-concurrency1--random-output-len1500--random-input-len4096--num-prompts4
```

### Qwen3 32B A2 High Throughput 50ms 1[#](#qwen3-32b-a2-high-throughput-50ms-1 "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A2 8Card

DeployMode: PD Mixed

DataSets: 3.5K1.5K

TPOT: 50ms

#### Model Deployment[#](#id57 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1

unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7239--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests78\
--disable-radix-cache--speculative-draft-model-quantizationunquant\
--chunked-prefill-size-1--max-prefill-tokens65536\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4\
--tp-size4--mem-fraction-static0.72--cuda-graph-bs148163264687278--dtypebfloat16--base-gpu-id4
```

#### Benchmark[#](#id58 "Link to this heading")

We tested it based on the GSM8K dataset.

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7239--max-concurrency78--random-output-len1500--random-input-len3500--num-prompts312--random-range-ratio1
```

### Qwen3 32B A2 High Throughput 50ms 2[#](#qwen3-32b-a2-high-throughput-50ms-2 "Link to this heading")

Model: Qwen3 32B

Hardware: Atlas 800I A2 8Card

DeployMode: PD Mixed

DataSets: 2K2K

TPOT: 50ms

#### Model Deployment[#](#id59 "Link to this heading")

```
echoperformance|tee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl-wvm.swappiness=0
sysctl-wkernel.numa_balancing=0
sysctl-wkernel.sched_migration_cost_ns=50000

exportSGLANG_SET_CPU_AFFINITY=1
unsethttps_proxy
unsethttp_proxy
unsetHTTPS_PROXY
unsetHTTP_PROXY
unsetASCEND_LAUNCH_BLOCKING
source/usr/local/Ascend/ascend-toolkit/set_env.sh
source/usr/local/Ascend/nnal/atb/set_env.sh
source/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/bin/set_env.bash
exportPATH=/usr/local/Ascend/8.5.0/compiler/bishengir/bin:$PATH

MODEL_PATH=xxx

exportSGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

LOCAL_HOST1=`hostname-I|awk-F" "'{print$1}'`
LOCAL_HOST2=`hostname-I|awk-F" "'{print$2}'`

echo"${LOCAL_HOST1}"
echo"${LOCAL_HOST2}"

exportHCCL_BUFFSIZE=400
exportHCCL_SOCKET_IFNAME=lo
exportGLOO_SOCKET_IFNAME=lo
exportHCCL_OP_EXPANSION_MODE="AIV"
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
exportSGLANG_ENABLE_SPEC_V2=1
exportDISABLE_EAGLE3_QUANT=1

python-msglang.launch_server--model-path$MODEL_PATH\
--host127.0.0.1--port7239--trust-remote-code--nnodes1--node-rank0\
--attention-backendascend--devicenpu--quantizationmodelslim\
--max-running-requests120\
--disable-radix-cache\
--speculative-algorithmEAGLE3--speculative-draft-model-pathxxx\
--speculative-num-steps3--speculative-eagle-topk1--speculative-num-draft-tokens4--speculative-draft-model-quantizationunquant\
--chunked-prefill-size-1--max-prefill-tokens49152--base-gpu-id4\
--tp-size4--mem-fraction-static0.7--cuda-graph-bs54606672788490108114120--dtypebfloat16
```

#### Benchmark[#](#id60 "Link to this heading")

We tested it based on the GSM8K dataset.

```
python3-msglang.bench_serving--dataset-namerandom--backendsglang--host127.0.0.1--port7239--max-concurrency120--random-output-len2000--random-input-len2000--num-prompts120--random-range-ratio1
```