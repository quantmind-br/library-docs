---
title: Using Kubernetes - vLLM
url: https://docs.vllm.ai/en/latest/deployment/k8s/
source: sitemap
fetched_at: 2026-05-07T21:11:33.838328053-03:00
rendered_js: false
word_count: 645
summary: This guide provides instructions for deploying vLLM on Kubernetes clusters using CPUs, NVIDIA GPUs, or AMD GPUs, including configuration for storage, secrets, and deployment manifests.
tags:
    - vllm
    - kubernetes
    - llm-deployment
    - containerization
    - gpu-acceleration
    - model-serving
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/k8s.md "Edit this page")

Deploying vLLM on Kubernetes is a scalable and efficient way to serve machine learning models. This guide walks you through deploying vLLM using native Kubernetes.

- [Deployment with CPUs](#deployment-with-cpus)
- [Deployment with GPUs](#deployment-with-gpus)
- [Serving with gRPC](#serving-with-grpc)
- [Troubleshooting](#troubleshooting)
  
  - [Startup Probe or Readiness Probe Failure, container log contains "KeyboardInterrupt: terminated"](#startup-probe-or-readiness-probe-failure-container-log-contains-keyboardinterrupt-terminated)
- [Conclusion](#conclusion)

Alternatively, you can deploy vLLM to Kubernetes using any of the following:

- [Helm](https://docs.vllm.ai/en/latest/deployment/frameworks/helm/)
- [NVIDIA Dynamo](https://docs.vllm.ai/en/latest/deployment/integrations/dynamo/)
- [InftyAI/llmaz](https://docs.vllm.ai/en/latest/deployment/integrations/llmaz/)
- [llm-d](https://docs.vllm.ai/en/latest/deployment/integrations/llm-d/)
- [KAITO](https://docs.vllm.ai/en/latest/deployment/integrations/kaito/)
- [KServe](https://docs.vllm.ai/en/latest/deployment/integrations/kserve/)
- [Kthena](https://docs.vllm.ai/en/latest/deployment/integrations/kthena/)
- [KubeRay](https://docs.vllm.ai/en/latest/deployment/integrations/kuberay/)
- [kubernetes-sigs/lws](https://docs.vllm.ai/en/latest/deployment/frameworks/lws/)
- [meta-llama/llama-stack](https://docs.vllm.ai/en/latest/deployment/integrations/llamastack/)
- [substratusai/kubeai](https://docs.vllm.ai/en/latest/deployment/integrations/kubeai/)
- [vllm-project/AIBrix](https://docs.vllm.ai/en/latest/deployment/integrations/aibrix/)
- [vllm-project/production-stack](https://docs.vllm.ai/en/latest/deployment/integrations/production-stack/)

## Deployment with CPUs[¶](#deployment-with-cpus "Permanent link")

Note

The use of CPUs here is for demonstration and testing purposes only and its performance will not be on par with GPUs.

First, create a Kubernetes PVC and Secret for downloading and storing Hugging Face model:

Config

```
cat<<EOF |kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: vllm-models
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 50Gi
---
apiVersion: v1
kind: Secret
metadata:
  name: hf-token-secret
type: Opaque
stringData:
  token: "REPLACE_WITH_TOKEN"
EOF
```

Here, the `token` field stores your **Hugging Face access token**. For details on how to generate a token, see the [Hugging Face documentation](https://huggingface.co/docs/hub/en/security-tokens).

Next, start the vLLM server as a Kubernetes Deployment and Service.

Note that you will want to configure your vLLM image based on your processor arch:

Config

```
VLLM_IMAGE=public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:latest# use this for x86_64
VLLM_IMAGE=public.ecr.aws/q9t5s3a7/vllm-arm64-cpu-release-repo:latest# use this for arm64
cat<<EOF |kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: vllm
  template:
    metadata:
      labels:
        app.kubernetes.io/name: vllm
    spec:
      containers:
      - name: vllm
        image: $VLLM_IMAGE
        command: ["/bin/sh", "-c"]
        args: [
          "vllm serve meta-llama/Llama-3.2-1B-Instruct"
        ]
        env:
        - name: HF_TOKEN
          valueFrom:
            secretKeyRef:
              name: hf-token-secret
              key: token
        ports:
          - containerPort: 8000
        volumeMounts:
          - name: llama-storage
            mountPath: /root/.cache/huggingface
      volumes:
      - name: llama-storage
        persistentVolumeClaim:
          claimName: vllm-models
---
apiVersion: v1
kind: Service
metadata:
  name: vllm-server
spec:
  selector:
    app.kubernetes.io/name: vllm
  ports:
  - protocol: TCP
    port: 8000
    targetPort: 8000
  type: ClusterIP
EOF
```

We can verify that the vLLM server has started successfully via the logs (this might take a couple of minutes to download the model):

```
kubectllogs-lapp.kubernetes.io/name=vllm
...
INFO:Startedserverprocess[1]
INFO:Waitingforapplicationstartup.
INFO:Applicationstartupcomplete.
INFO:Uvicornrunningonhttp://0.0.0.0:8000(PressCTRL+Ctoquit)
```

## Deployment with GPUs[¶](#deployment-with-gpus "Permanent link")

**Pre-requisite**: Ensure that you have a running [Kubernetes cluster with GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/).

1. Create a PVC, Secret and Deployment for vLLM
   
   PVC is used to store the model cache and it is optional, you can use hostPath or other storage options
   
   Yaml
   
   ```
   apiVersion:v1
   kind:PersistentVolumeClaim
   metadata:
   name:mistral-7b
   namespace:default
   spec:
   accessModes:
   -ReadWriteOnce
   resources:
   requests:
   storage:50Gi
   storageClassName:default
   volumeMode:Filesystem
   ```
   
   Secret is optional and only required for accessing gated models, you can skip this step if you are not using gated models
   
   ```
   apiVersion:v1
   kind:Secret
   metadata:
   name:hf-token-secret
   namespace:default
   type:Opaque
   stringData:
   token:"REPLACE_WITH_TOKEN"
   ```
   
   Next to create the deployment file for vLLM to run the model server. The following example deploys the `Mistral-7B-Instruct-v0.3` model.
   
   Here are two examples for using NVIDIA GPU and AMD GPU.
   
   NVIDIA GPU:
   
   Yaml
   
   ```
   apiVersion:apps/v1
   kind:Deployment
   metadata:
   name:mistral-7b
   namespace:default
   labels:
   app:mistral-7b
   spec:
   replicas:1
   selector:
   matchLabels:
   app:mistral-7b
   template:
   metadata:
   labels:
   app:mistral-7b
   spec:
   volumes:
   -name:cache-volume
   persistentVolumeClaim:
   claimName:mistral-7b
   # vLLM needs to access the host's shared memory for tensor parallel inference.
   -name:shm
   emptyDir:
   medium:Memory
   sizeLimit:"2Gi"
   containers:
   -name:mistral-7b
   image:vllm/vllm-openai:latest
   command:["/bin/sh","-c"]
   args:[
   "vllmservemistralai/Mistral-7B-Instruct-v0.3--trust-remote-code--enable-chunked-prefill--max_num_batched_tokens1024"
   ]
   env:
   -name:HF_TOKEN
   valueFrom:
   secretKeyRef:
   name:hf-token-secret
   key:token
   ports:
   -containerPort:8000
   resources:
   limits:
   cpu:"10"
   memory:20G
   nvidia.com/gpu:"1"
   requests:
   cpu:"2"
   memory:6G
   nvidia.com/gpu:"1"
   volumeMounts:
   -mountPath:/root/.cache/huggingface
   name:cache-volume
   -name:shm
   mountPath:/dev/shm
   livenessProbe:
   httpGet:
   path:/health
   port:8000
   initialDelaySeconds:60
   periodSeconds:10
   readinessProbe:
   httpGet:
   path:/health
   port:8000
   initialDelaySeconds:60
   periodSeconds:5
   ```
   
   AMD GPU:
   
   You can refer to the `deployment.yaml` below if using AMD ROCm GPU like MI300X.
   
   Yaml
   
   ```
   apiVersion:apps/v1
   kind:Deployment
   metadata:
   name:mistral-7b
   namespace:default
   labels:
   app:mistral-7b
   spec:
   replicas:1
   selector:
   matchLabels:
   app:mistral-7b
   template:
   metadata:
   labels:
   app:mistral-7b
   spec:
   volumes:
   # PVC
   -name:cache-volume
   persistentVolumeClaim:
   claimName:mistral-7b
   # vLLM needs to access the host's shared memory for tensor parallel inference.
   -name:shm
   emptyDir:
   medium:Memory
   sizeLimit:"8Gi"
   hostNetwork:true
   hostIPC:true
   containers:
   -name:mistral-7b
   image:rocm/vllm:rocm6.2_mi300_ubuntu20.04_py3.9_vllm_0.6.4
   securityContext:
   seccompProfile:
   type:Unconfined
   runAsGroup:44
   capabilities:
   add:
   -SYS_PTRACE
   command:["/bin/sh","-c"]
   args:[
   "vllmservemistralai/Mistral-7B-v0.3--port8000--trust-remote-code--enable-chunked-prefill--max_num_batched_tokens1024"
   ]
   env:
   -name:HF_TOKEN
   valueFrom:
   secretKeyRef:
   name:hf-token-secret
   key:token
   ports:
   -containerPort:8000
   resources:
   limits:
   cpu:"10"
   memory:20G
   amd.com/gpu:"1"
   requests:
   cpu:"6"
   memory:6G
   amd.com/gpu:"1"
   volumeMounts:
   -name:cache-volume
   mountPath:/root/.cache/huggingface
   -name:shm
   mountPath:/dev/shm
   ```
   
   You can get the full example with steps and sample yaml files from [https://github.com/ROCm/k8s-device-plugin/tree/master/example/vllm-serve](https://github.com/ROCm/k8s-device-plugin/tree/master/example/vllm-serve).
2. Create a Kubernetes Service for vLLM
   
   Next, create a Kubernetes Service file to expose the `mistral-7b` deployment:
   
   Yaml
   
   ```
   apiVersion:v1
   kind:Service
   metadata:
   name:mistral-7b
   namespace:default
   spec:
   ports:
   -name:http-mistral-7b
   port:80
   protocol:TCP
   targetPort:8000
   # The label selector should match the deployment labels & it is useful for prefix caching feature
   selector:
   app:mistral-7b
   sessionAffinity:None
   type:ClusterIP
   ```
3. Deploy and Test
   
   Apply the deployment and service configurations using `kubectl apply -f <filename>`:
   
   ```
   kubectlapply-fdeployment.yaml
   kubectlapply-fservice.yaml
   ```
   
   To test the deployment, run the following `curl` command:
   
   ```
   curlhttp://mistral-7b.default.svc.cluster.local/v1/completions\
   -H"Content-Type: application/json"\
   -d'{
           "model": "mistralai/Mistral-7B-Instruct-v0.3",
           "prompt": "San Francisco is a",
           "max_tokens": 7,
           "temperature": 0
         }'
   ```
   
   If the service is correctly deployed, you should receive a response from the vLLM model.

## Serving with gRPC[¶](#serving-with-grpc "Permanent link")

vLLM can serve models over gRPC instead of HTTP by passing the `--grpc` flag. This requires the optional gRPC dependencies:

When using `--grpc`, the server exposes the standard [gRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) (`grpc.health.v1.Health`), which integrates with Kubernetes [native gRPC probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-grpc-liveness-probe) (available since Kubernetes 1.24).

To deploy with gRPC, change the `vllm serve` command to include `--grpc` and replace `httpGet` probes with `grpc` probes:

```
containers:
-name:mistral-7b
image:vllm/vllm-openai:latest
command:["/bin/sh","-c"]
args:[
"pipinstallvllm[grpc]&&vllmservemistralai/Mistral-7B-Instruct-v0.3--grpc--port50051--trust-remote-code"
]
ports:
-containerPort:50051
livenessProbe:
grpc:
port:50051
initialDelaySeconds:120
periodSeconds:10
readinessProbe:
grpc:
port:50051
initialDelaySeconds:120
periodSeconds:5
```

Note

The gRPC health service checks the engine status on every probe. If the engine is unhealthy or the server is shutting down, the probe returns `NOT_SERVING`.

You can also verify the health service manually with `grpcurl`:

```
grpcurl-plaintextlocalhost:50051grpc.health.v1.Health/Check
```

## Troubleshooting[¶](#troubleshooting "Permanent link")

### Startup Probe or Readiness Probe Failure, container log contains "KeyboardInterrupt: terminated"[¶](#startup-probe-or-readiness-probe-failure-container-log-contains-keyboardinterrupt-terminated "Permanent link")

If the startup or readiness probe failureThreshold is too low for the time needed to start up the server, Kubernetes scheduler will kill the container. A couple of indications that this has happened:

1. container log contains "KeyboardInterrupt: terminated"
2. `kubectl get events` shows message `Container $NAME failed startup probe, will be restarted`

To mitigate, increase the failureThreshold to allow more time for the model server to start serving. You can identify an ideal failureThreshold by removing the probes from the manifest and measuring how much time it takes for the model server to show it's ready to serve.

## Conclusion[¶](#conclusion "Permanent link")

Deploying vLLM with Kubernetes allows for efficient scaling and management of ML models leveraging GPU resources. By following the steps outlined above, you should be able to set up and test a vLLM deployment within your Kubernetes cluster. If you encounter any issues or have suggestions, please feel free to contribute to the documentation.