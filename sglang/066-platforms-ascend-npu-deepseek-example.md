---
title: DeepSeek examples — SGLang
url: https://docs.sglang.io/platforms/ascend_npu_deepseek_example.html
source: crawler
fetched_at: 2026-02-04T08:48:15.38431022-03:00
rendered_js: false
word_count: 173
summary: This document provides configuration instructions and command-line parameters for deploying DeepSeek-V3 models on Huawei Atlas NPU hardware using SGLang, covering both mixed and disaggregated prefill-decode modes.
tags:
    - deepseek-v3
    - sglang
    - ascend-npu
    - atlas-800i-a3
    - distributed-inference
    - model-deployment
    - npu-optimization
category: configuration
---

## Contents

## DeepSeek examples[#](#deepseek-examples "Link to this heading")

## Running DeepSeek-V3[#](#running-deepseek-v3 "Link to this heading")

### Running DeepSeek in PD mixed mode on 1 x Atlas 800I A3.[#](#running-deepseek-in-pd-mixed-mode-on-1-x-atlas-800i-a3 "Link to this heading")

W4A8 Model weights could be found [here](https://modelers.cn/models/Modelers_Park/DeepSeek-R1-0528-w4a8).

```
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32

#Deepep communication settings
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=32
exportHCCL_BUFFSIZE=1600

#spec overlap
exportSGLANG_ENABLE_SPEC_V2=1
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1

#npu acceleration operator
exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_USE_FIA_NZ=1

python3-msglang.launch_server\
--model-path${MODEL_PATH}\
--tp16\
--trust-remote-code\
--attention-backendascend\
--devicenpu\
--quantizationmodelslim\
--watchdog-timeout9000\
--cuda-graph-bs816242832\
--mem-fraction-static0.68\
--max-running-requests128\
--context-length8188\
--disable-radix-cache\
--chunked-prefill-size-1\
--max-prefill-tokens16384\
--moe-a2a-backenddeepep\
--deepep-modeauto\
--enable-dp-attention\
--dp-size4\
--enable-dp-lm-head\
--speculative-algorithmNEXTN\
--speculative-num-steps3\
--speculative-eagle-topk1\
--speculative-num-draft-tokens4\
--dtypebfloat16
```

### Running DeepSeek with PD disaggregation mode on 2 x Atlas 800I A3.[#](#running-deepseek-with-pd-disaggregation-mode-on-2-x-atlas-800i-a3 "Link to this heading")

W4A8 Model weights could be found [here](https://modelers.cn/models/Modelers_Park/DeepSeek-R1-0528-w4a8).

1. Prefill:

```
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32

#memfabric config store
exportASCEND_MF_STORE_URL="tcp://<PREFILL_HOST_IP>:<PORT>"

#Deepep communication settings
exportDEEP_NORMAL_MODE_USE_INT8_QUANT=1
exportHCCL_BUFFSIZE=1536

#npu acceleration operator
exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_USE_FIA_NZ=1
exportTASK_QUEUE_ENABLE=2

python-msglang.launch_server\
--model-path${MODEL_PATH}\
--host$PREFILL_HOST_IP\
--port8000\
--disaggregation-modeprefill\
--disaggregation-bootstrap-port8996\
--disaggregation-transfer-backendascend\
--trust-remote-code\
--nnodes1\
--node-rank0\
--tp-size16\
--mem-fraction-static0.6\
--attention-backendascend\
--devicenpu\
--quantizationmodelslim\
--load-balance-methodround_robin\
--max-running-requests8\
--context-length8192\
--disable-radix-cache\
--chunked-prefill-size-1\
--max-prefill-tokens28680\
--moe-a2a-backenddeepep\
--deepep-modenormal\
--speculative-algorithmNEXTN\
--speculative-num-steps3\
--speculative-eagle-topk1\
--speculative-num-draft-tokens4\
--dp-size2\
--enable-dp-attention\
--disable-shared-experts-fusion\
--dtypebfloat16
```

2. Decode:

```
exportPYTORCH_NPU_ALLOC_CONF=expandable_segments:True
exportSTREAMS_PER_DEVICE=32

#memfabric config store
exportASCEND_MF_STORE_URL="tcp://<PREFILL_HOST_IP>:<PORT>"

#Deepep communication settings
exportHCCL_BUFFSIZE=720
exportSGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=88

#spec overlap
exportSGLANG_ENABLE_SPEC_V2=1
exportSGLANG_ENABLE_OVERLAP_PLAN_STREAM=1

#npu acceleration operator
unsetTASK_QUEUE_ENABLE
exportSGLANG_NPU_USE_MLAPO=1
exportSGLANG_USE_FIA_NZ=1
exportENABLE_MOE_NZ=1

# suggest max-running-requests <= max-cuda-graph-bs * dp_size, Because when this value is exceeded, performance will significantly degrade.
python-msglang.launch_server\
--model-path${MODEL_PATH}\
--disaggregation-modedecode\
--host$DECODE_HOST_IP\
--port8001\
--trust-remote-code\
--nnodes1\
--node-rank0\
--tp-size16\
--dp-size16\
--mem-fraction-static0.8\
--max-running-requests352\
--attention-backendascend\
--devicenpu\
--quantizationmodelslim\
--prefill-round-robin-balance\
--moe-a2a-backenddeepep\
--enable-dp-attention\
--deepep-modelow_latency\
--enable-dp-lm-head\
--cuda-graph-bs810121416182022\
--disaggregation-transfer-backendascend\
--watchdog-timeout9000\
--context-length8192\
--speculative-algorithmNEXTN\
--speculative-num-steps3\
--speculative-eagle-topk1\
--speculative-num-draft-tokens4\
--disable-shared-experts-fusion\
--dtypebfloat16\
--tokenizer-worker-num4
```

3. SGLang Model Gateway (former Router)

```
python-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://<PREFILL_HOST_IP>:80008996\
--decodehttp://<DECODE_HOST_IP>:8001\
--host127.0.0.1\
--port6688
```

### Running DeepSeek with PD disaggregation on 4 x Atlas 800I A3.[#](#running-deepseek-with-pd-disaggregation-on-4-x-atlas-800i-a3 "Link to this heading")

W8A8 Model weights could be found [here](https://modelers.cn/models/State_Cloud/Deepseek-R1-bf16-hfd-w8a8).

1. Prefill & Decode:

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

2. SGLang Model Gateway (former Router):

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

### test gsm8k[#](#test-gsm8k "Link to this heading")

```
fromtypesimport SimpleNamespace
fromsglang.test.few_shot_gsm8kimport run_eval

defgsm8k():
    args = SimpleNamespace(
        num_shots=5,
        data_path=None,
        num_questions=200,
        max_new_tokens=512,
        parallel=32,
        host=f"http://127.0.0.1",
        port=6688,
    )
    metrics = run_eval(args)
    print(f"{metrics=}")
    print(f"{metrics['accuracy']=}")
if __name__ == "__main__":
    gsm8k()
```