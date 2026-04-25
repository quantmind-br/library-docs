---
title: Lambda Labs Gpu Cloud — Reserved and on-demand GPU cloud instances for ML training and inference | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-lambda-labs
source: crawler
fetched_at: 2026-04-24T17:01:24.491545908-03:00
rendered_js: false
word_count: 670
summary: This document provides a comprehensive reference guide for using Lambda Labs' GPU cloud, detailing when and how to utilize on-demand instances for Machine Learning training and inference. It covers setup instructions, available hardware, instance configurations, and API/CLI usage.
tags:
    - gpu-cloud
    - mlops
    - lambda-labs
    - training-inference
    - instance-management
    - python-api
category: reference
---

Reserved and on-demand GPU cloud instances for ML training and inference. Use when you need dedicated GPU instances with simple SSH access, persistent filesystems, or high-performance multi-node clusters for large-scale training.

SourceOptional — install with `hermes skills install official/mlops/lambda-labs`Path`optional-skills/mlops/lambda-labs`Version`1.0.0`AuthorOrchestra ResearchLicenseMITDependencies`lambda-cloud-client>=1.0.0`Tags`Infrastructure`, `GPU Cloud`, `Training`, `Inference`, `Lambda Labs`

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Lambda Labs GPU Cloud

Comprehensive guide to running ML workloads on Lambda Labs GPU cloud with on-demand instances and 1-Click Clusters.

## When to use Lambda Labs[​](#when-to-use-lambda-labs "Direct link to When to use Lambda Labs")

**Use Lambda Labs when:**

- Need dedicated GPU instances with full SSH access
- Running long training jobs (hours to days)
- Want simple pricing with no egress fees
- Need persistent storage across sessions
- Require high-performance multi-node clusters (16-512 GPUs)
- Want pre-installed ML stack (Lambda Stack with PyTorch, CUDA, NCCL)

**Key features:**

- **GPU variety**: B200, H100, GH200, A100, A10, A6000, V100
- **Lambda Stack**: Pre-installed PyTorch, TensorFlow, CUDA, cuDNN, NCCL
- **Persistent filesystems**: Keep data across instance restarts
- **1-Click Clusters**: 16-512 GPU Slurm clusters with InfiniBand
- **Simple pricing**: Pay-per-minute, no egress fees
- **Global regions**: 12+ regions worldwide

**Use alternatives instead:**

- **Modal**: For serverless, auto-scaling workloads
- **SkyPilot**: For multi-cloud orchestration and cost optimization
- **RunPod**: For cheaper spot instances and serverless endpoints
- **Vast.ai**: For GPU marketplace with lowest prices

## Quick start[​](#quick-start "Direct link to Quick start")

### Account setup[​](#account-setup "Direct link to Account setup")

1. Create account at [https://lambda.ai](https://lambda.ai)
2. Add payment method
3. Generate API key from dashboard
4. Add SSH key (required before launching instances)

### Launch via console[​](#launch-via-console "Direct link to Launch via console")

1. Go to [https://cloud.lambda.ai/instances](https://cloud.lambda.ai/instances)
2. Click "Launch instance"
3. Select GPU type and region
4. Choose SSH key
5. Optionally attach filesystem
6. Launch and wait 3-15 minutes

### Connect via SSH[​](#connect-via-ssh "Direct link to Connect via SSH")

```bash
# Get instance IP from console
ssh ubuntu@<INSTANCE-IP>

# Or with specific key
ssh-i ~/.ssh/lambda_key ubuntu@<INSTANCE-IP>
```

## GPU instances[​](#gpu-instances "Direct link to GPU instances")

### Available GPUs[​](#available-gpus "Direct link to Available GPUs")

GPUVRAMPrice/GPU/hrBest ForB200 SXM6180 GB$4.99Largest models, fastest trainingH100 SXM80 GB$2.99-3.29Large model trainingH100 PCIe80 GB$2.49Cost-effective H100GH20096 GB$1.49Single-GPU large modelsA100 80GB80 GB$1.79Production trainingA100 40GB40 GB$1.29Standard trainingA1024 GB$0.75Inference, fine-tuningA600048 GB$0.80Good VRAM/price ratioV10016 GB$0.55Budget training

### Instance configurations[​](#instance-configurations "Direct link to Instance configurations")

```text
8x GPU: Best for distributed training (DDP, FSDP)
4x GPU: Large models, multi-GPU training
2x GPU: Medium workloads
1x GPU: Fine-tuning, inference, development
```

### Launch times[​](#launch-times "Direct link to Launch times")

- Single-GPU: 3-5 minutes
- Multi-GPU: 10-15 minutes

## Lambda Stack[​](#lambda-stack "Direct link to Lambda Stack")

All instances come with Lambda Stack pre-installed:

```bash
# Included software
- Ubuntu 22.04 LTS
- NVIDIA drivers (latest)
- CUDA 12.x
- cuDNN 8.x
- NCCL (for multi-GPU)
- PyTorch (latest)
- TensorFlow (latest)
- JAX
- JupyterLab
```

### Verify installation[​](#verify-installation "Direct link to Verify installation")

```bash
# Check GPU
nvidia-smi

# Check PyTorch
python -c"import torch; print(torch.cuda.is_available())"

# Check CUDA version
nvcc --version
```

## Python API[​](#python-api "Direct link to Python API")

### Installation[​](#installation "Direct link to Installation")

```bash
pip install lambda-cloud-client
```

### Authentication[​](#authentication "Direct link to Authentication")

```python
import os
import lambda_cloud_client

# Configure with API key
configuration = lambda_cloud_client.Configuration(
    host="https://cloud.lambdalabs.com/api/v1",
    access_token=os.environ["LAMBDA_API_KEY"]
)
```

### List available instances[​](#list-available-instances "Direct link to List available instances")

```python
with lambda_cloud_client.ApiClient(configuration)as api_client:
    api = lambda_cloud_client.DefaultApi(api_client)

# Get available instance types
    types = api.instance_types()
for name, info in types.data.items():
print(f"{name}: {info.instance_type.description}")
```

### Launch instance[​](#launch-instance "Direct link to Launch instance")

```python
from lambda_cloud_client.models import LaunchInstanceRequest

request = LaunchInstanceRequest(
    region_name="us-west-1",
    instance_type_name="gpu_1x_h100_sxm5",
    ssh_key_names=["my-ssh-key"],
    file_system_names=["my-filesystem"],# Optional
    name="training-job"
)

response = api.launch_instance(request)
instance_id = response.data.instance_ids[0]
print(f"Launched: {instance_id}")
```

### List running instances[​](#list-running-instances "Direct link to List running instances")

```python
instances = api.list_instances()
for instance in instances.data:
print(f"{instance.name}: {instance.ip} ({instance.status})")
```

### Terminate instance[​](#terminate-instance "Direct link to Terminate instance")

```python
from lambda_cloud_client.models import TerminateInstanceRequest

request = TerminateInstanceRequest(
    instance_ids=[instance_id]
)
api.terminate_instance(request)
```

### SSH key management[​](#ssh-key-management "Direct link to SSH key management")

```python
from lambda_cloud_client.models import AddSshKeyRequest

# Add SSH key
request = AddSshKeyRequest(
    name="my-key",
    public_key="ssh-rsa AAAA..."
)
api.add_ssh_key(request)

# List keys
keys = api.list_ssh_keys()

# Delete key
api.delete_ssh_key(key_id)
```

## CLI with curl[​](#cli-with-curl "Direct link to CLI with curl")

### List instance types[​](#list-instance-types "Direct link to List instance types")

```bash
curl-u$LAMBDA_API_KEY:\
  https://cloud.lambdalabs.com/api/v1/instance-types | jq
```

### Launch instance[​](#launch-instance-1 "Direct link to Launch instance")

```bash
curl-u$LAMBDA_API_KEY:\
-X POST https://cloud.lambdalabs.com/api/v1/instance-operations/launch \
-H"Content-Type: application/json"\
-d'{
    "region_name": "us-west-1",
    "instance_type_name": "gpu_1x_h100_sxm5",
    "ssh_key_names": ["my-key"]
  }'| jq
```

### Terminate instance[​](#terminate-instance-1 "Direct link to Terminate instance")

```bash
curl-u$LAMBDA_API_KEY:\
-X POST https://cloud.lambdalabs.com/api/v1/instance-operations/terminate \
-H"Content-Type: application/json"\
-d'{"instance_ids": ["<INSTANCE-ID>"]}'| jq
```

## Persistent storage[​](#persistent-storage "Direct link to Persistent storage")

### Filesystems[​](#filesystems "Direct link to Filesystems")

Filesystems persist data across instance restarts:

```bash
# Mount location
/lambda/nfs/<FILESYSTEM_NAME>

# Example: save checkpoints
python train.py --checkpoint-dir /lambda/nfs/my-storage/checkpoints
```

### Create filesystem[​](#create-filesystem "Direct link to Create filesystem")

1. Go to Storage in Lambda console
2. Click "Create filesystem"
3. Select region (must match instance region)
4. Name and create

### Attach to instance[​](#attach-to-instance "Direct link to Attach to instance")

Filesystems must be attached at instance launch time:

- Via console: Select filesystem when launching
- Via API: Include `file_system_names` in launch request

### Best practices[​](#best-practices "Direct link to Best practices")

```bash
# Store on filesystem (persists)
/lambda/nfs/storage/
  ├── datasets/
  ├── checkpoints/
  ├── models/
  └── outputs/

# Local SSD (faster, ephemeral)
/home/ubuntu/
  └── working/  # Temporary files
```

## SSH configuration[​](#ssh-configuration "Direct link to SSH configuration")

### Add SSH key[​](#add-ssh-key "Direct link to Add SSH key")

```bash
# Generate key locally
ssh-keygen -t ed25519 -f ~/.ssh/lambda_key

# Add public key to Lambda console
# Or via API
```

### Multiple keys[​](#multiple-keys "Direct link to Multiple keys")

```bash
# On instance, add more keys
echo'ssh-rsa AAAA...'>> ~/.ssh/authorized_keys
```

### Import from GitHub[​](#import-from-github "Direct link to Import from GitHub")

```bash
# On instance
ssh-import-id gh:username
```

### SSH tunneling[​](#ssh-tunneling "Direct link to SSH tunneling")

```bash
# Forward Jupyter
ssh-L8888:localhost:8888 ubuntu@<IP>

# Forward TensorBoard
ssh-L6006:localhost:6006 ubuntu@<IP>

# Multiple ports
ssh-L8888:localhost:8888 -L6006:localhost:6006 ubuntu@<IP>
```

## JupyterLab[​](#jupyterlab "Direct link to JupyterLab")

### Launch from console[​](#launch-from-console "Direct link to Launch from console")

1. Go to Instances page
2. Click "Launch" in Cloud IDE column
3. JupyterLab opens in browser

### Manual access[​](#manual-access "Direct link to Manual access")

```bash
# On instance
jupyter lab --ip=0.0.0.0 --port=8888

# From local machine with tunnel
ssh-L8888:localhost:8888 ubuntu@<IP>
# Open http://localhost:8888
```

## Training workflows[​](#training-workflows "Direct link to Training workflows")

### Single-GPU training[​](#single-gpu-training "Direct link to Single-GPU training")

```bash
# SSH to instance
ssh ubuntu@<IP>

# Clone repo
git clone https://github.com/user/project
cd project

# Install dependencies
pip install-r requirements.txt

# Train
python train.py --epochs100 --checkpoint-dir /lambda/nfs/storage/checkpoints
```

### Multi-GPU training (single node)[​](#multi-gpu-training-single-node "Direct link to Multi-GPU training (single node)")

```python
# train_ddp.py
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

defmain():
    dist.init_process_group("nccl")
    rank = dist.get_rank()
    device = rank % torch.cuda.device_count()

    model = MyModel().to(device)
    model = DDP(model, device_ids=[device])

# Training loop...

if __name__ =="__main__":
    main()
```

```bash
# Launch with torchrun (8 GPUs)
torchrun --nproc_per_node=8 train_ddp.py
```

### Checkpoint to filesystem[​](#checkpoint-to-filesystem "Direct link to Checkpoint to filesystem")

```python
import os

checkpoint_dir ="/lambda/nfs/my-storage/checkpoints"
os.makedirs(checkpoint_dir, exist_ok=True)

# Save checkpoint
torch.save({
'epoch': epoch,
'model_state_dict': model.state_dict(),
'optimizer_state_dict': optimizer.state_dict(),
'loss': loss,
},f"{checkpoint_dir}/checkpoint_{epoch}.pt")
```

## 1-Click Clusters[​](#1-click-clusters "Direct link to 1-Click Clusters")

### Overview[​](#overview "Direct link to Overview")

High-performance Slurm clusters with:

- 16-512 NVIDIA H100 or B200 GPUs
- NVIDIA Quantum-2 400 Gb/s InfiniBand
- GPUDirect RDMA at 3200 Gb/s
- Pre-installed distributed ML stack

### Included software[​](#included-software "Direct link to Included software")

- Ubuntu 22.04 LTS + Lambda Stack
- NCCL, Open MPI
- PyTorch with DDP and FSDP
- TensorFlow
- OFED drivers

### Storage[​](#storage "Direct link to Storage")

- 24 TB NVMe per compute node (ephemeral)
- Lambda filesystems for persistent data

### Multi-node training[​](#multi-node-training "Direct link to Multi-node training")

```bash
# On Slurm cluster
srun --nodes=4 --ntasks-per-node=8 --gpus-per-node=8\
  torchrun --nnodes=4--nproc_per_node=8\
--rdzv_backend=c10d --rdzv_endpoint=$MASTER_ADDR:29500 \
  train.py
```

## Networking[​](#networking "Direct link to Networking")

### Bandwidth[​](#bandwidth "Direct link to Bandwidth")

- Inter-instance (same region): up to 200 Gbps
- Internet outbound: 20 Gbps max

### Firewall[​](#firewall "Direct link to Firewall")

- Default: Only port 22 (SSH) open
- Configure additional ports in Lambda console
- ICMP traffic allowed by default

### Private IPs[​](#private-ips "Direct link to Private IPs")

```bash
# Find private IP
ip addr show |grep'inet '
```

## Common workflows[​](#common-workflows "Direct link to Common workflows")

### Workflow 1: Fine-tuning LLM[​](#workflow-1-fine-tuning-llm "Direct link to Workflow 1: Fine-tuning LLM")

```bash
# 1. Launch 8x H100 instance with filesystem

# 2. SSH and setup
ssh ubuntu@<IP>
pip install transformers accelerate peft

# 3. Download model to filesystem
python -c"
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-hf')
model.save_pretrained('/lambda/nfs/storage/models/llama-2-7b')
"

# 4. Fine-tune with checkpoints on filesystem
accelerate launch --num_processes8 train.py \
--model_path /lambda/nfs/storage/models/llama-2-7b \
--output_dir /lambda/nfs/storage/outputs \
--checkpoint_dir /lambda/nfs/storage/checkpoints
```

### Workflow 2: Batch inference[​](#workflow-2-batch-inference "Direct link to Workflow 2: Batch inference")

```bash
# 1. Launch A10 instance (cost-effective for inference)

# 2. Run inference
python inference.py \
--model /lambda/nfs/storage/models/fine-tuned \
--input /lambda/nfs/storage/data/inputs.jsonl \
--output /lambda/nfs/storage/data/outputs.jsonl
```

## Cost optimization[​](#cost-optimization "Direct link to Cost optimization")

### Choose right GPU[​](#choose-right-gpu "Direct link to Choose right GPU")

TaskRecommended GPULLM fine-tuning (7B)A100 40GBLLM fine-tuning (70B)8x H100InferenceA10, A6000DevelopmentV100, A10Maximum performanceB200

### Reduce costs[​](#reduce-costs "Direct link to Reduce costs")

1. **Use filesystems**: Avoid re-downloading data
2. **Checkpoint frequently**: Resume interrupted training
3. **Right-size**: Don't over-provision GPUs
4. **Terminate idle**: No auto-stop, manually terminate

### Monitor usage[​](#monitor-usage "Direct link to Monitor usage")

- Dashboard shows real-time GPU utilization
- API for programmatic monitoring

## Common issues[​](#common-issues "Direct link to Common issues")

IssueSolutionInstance won't launchCheck region availability, try different GPUSSH connection refusedWait for instance to initialize (3-15 min)Data lost after terminateUse persistent filesystemsSlow data transferUse filesystem in same regionGPU not detectedReboot instance, check drivers

## References[​](#references "Direct link to References")

- [**Advanced Usage**](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/lambda-labs/references/advanced-usage.md) - Multi-node training, API automation
- [**Troubleshooting**](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/lambda-labs/references/troubleshooting.md) - Common issues and solutions

## Resources[​](#resources "Direct link to Resources")

- **Documentation**: [https://docs.lambda.ai](https://docs.lambda.ai)
- **Console**: [https://cloud.lambda.ai](https://cloud.lambda.ai)
- **Pricing**: [https://lambda.ai/instances](https://lambda.ai/instances)
- **Support**: [https://support.lambdalabs.com](https://support.lambdalabs.com)
- **Blog**: [https://lambda.ai/blog](https://lambda.ai/blog)