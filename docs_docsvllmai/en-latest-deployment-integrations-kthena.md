---
title: Kthena - vLLM
url: https://docs.vllm.ai/en/latest/deployment/integrations/kthena/
source: sitemap
fetched_at: 2026-05-07T21:12:01.720443115-03:00
rendered_js: false
word_count: 394
summary: This guide provides instructions for deploying a multi-node vLLM inference service on Kubernetes using the Kthena platform and Volcano for gang scheduling.
tags:
    - kubernetes
    - vllm
    - kthena
    - volcano
    - llm-inference
    - multi-node-deployment
    - model-serving
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/integrations/kthena.md "Edit this page")

[**Kthena**](https://github.com/volcano-sh/kthena) is a Kubernetes-native LLM inference platform that transforms how organizations deploy and manage Large Language Models in production. Built with declarative model lifecycle management and intelligent request routing, it provides high performance and enterprise-grade scalability for LLM inference workloads.

This guide shows how to deploy a production-grade, **multi-node vLLM** service on Kubernetes.

We’ll:

- Install the required components (Kthena + Volcano).
- Deploy a multi-node vLLM model via Kthena’s `ModelServing` CR.
- Validate the deployment.

* * *

## 1. Prerequisites[¶](#1-prerequisites "Permanent link")

You need:

- A Kubernetes cluster with **GPU nodes**.
- `kubectl` access with cluster-admin or equivalent permissions.
- **Volcano** installed for gang scheduling.
- **Kthena** installed with the `ModelServing` CRD available.
- A valid **Hugging Face token** if loading models from Hugging Face Hub.

### 1.1 Install Volcano[¶](#11-install-volcano "Permanent link")

```
helmrepoaddvolcano-shhttps://volcano-sh.github.io/helm-charts
helmrepoupdate
helminstallvolcanovolcano-sh/volcano-nvolcano-system--create-namespace
```

This provides the gang-scheduling and network topology features used by Kthena.

### 1.2 Install Kthena[¶](#12-install-kthena "Permanent link")

```
helminstallkthenaoci://ghcr.io/volcano-sh/charts/kthena--versionv0.1.0--namespacekthena-system--create-namespace
```

- The `kthena-system` namespace is created.
- Kthena controllers and CRDs, including `ModelServing`, are installed and healthy.

Validate:

```
kubectlgetcrd|grepmodelserving
```

You should see:

```
modelservings.workload.serving.volcano.sh   ...
```

* * *

## 2. The Multi-Node vLLM `ModelServing` Example[¶](#2-the-multi-node-vllm-modelserving-example "Permanent link")

Kthena provides an example manifest to deploy a **multi-node vLLM cluster running Llama**. Conceptually this is equivalent to the vLLM production stack Helm deployment, but expressed with `ModelServing`.

A simplified version of the example (`llama-multinode`) looks like:

- `spec.replicas: 1` – one `ServingGroup` (one logical model deployment).
- `roles`:
  
  - `entryTemplate` – defines **leader** pods that run:
    
    - vLLM’s **multi-node cluster bootstrap script** (Ray cluster).
    - vLLM **OpenAI-compatible API server**.
  - `workerTemplate` – defines **worker** pods that join the leader’s Ray cluster.

Key points from the example YAML:

- **Image**: `vllm/vllm-openai:latest` (matches upstream vLLM images).
- **Command** (leader):

```
command:
-sh
--c
->
bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=2;
python3 -m vllm.entrypoints.openai.api_server
--port 8080
--model meta-llama/Llama-3.1-405B-Instruct
--tensor-parallel-size 8
--pipeline-parallel-size 2
```

- **Command** (worker):

```
command:
-sh
--c
->
bash /vllm-workspace/examples/online_serving/multi-node-serving.sh worker --ray_address=$(ENTRY_ADDRESS)
```

* * *

## 3. Deploying Multi-Node llama vLLM via Kthena[¶](#3-deploying-multi-node-llama-vllm-via-kthena "Permanent link")

### 3.1 Prepare the Manifest[¶](#31-prepare-the-manifest "Permanent link")

**Recommended**: use a Secret instead of a raw env var:

```
kubectlcreatesecretgenerichf-token\
-ndefault\
--from-literal=HUGGING_FACE_HUB_TOKEN='<your-token>'
```

### 3.2 Apply the `ModelServing`[¶](#32-apply-the-modelserving "Permanent link")

```
cat<<EOF | kubectl apply -f -
apiVersion: workload.serving.volcano.sh/v1alpha1
kind: ModelServing
metadata:
  name: llama-multinode
  namespace: default
spec:
  schedulerName: volcano
  replicas: 1  # group replicas
  template:
    restartGracePeriodSeconds: 60
    gangPolicy:
      minRoleReplicas:
        405b: 1
    roles:
      - name: 405b
        replicas: 2
        entryTemplate:
          spec:
            containers:
              - name: leader
                image: vllm/vllm-openai:latest
                env:
                  - name: HUGGING_FACE_HUB_TOKEN
                    valueFrom:
                      secretKeyRef:
                        name: hf-token
                        key: HUGGING_FACE_HUB_TOKEN
                command:
                  - sh
                  - -c
                  - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=2; 
                    python3 -m vllm.entrypoints.openai.api_server --port 8080 --model meta-llama/Llama-3.1-405B-Instruct --tensor-parallel-size 8 --pipeline-parallel-size 2"
                resources:
                  limits:
                    nvidia.com/gpu: "8"
                    memory: 1124Gi
                    ephemeral-storage: 800Gi
                  requests:
                    ephemeral-storage: 800Gi
                    cpu: 125
                ports:
                  - containerPort: 8080
                readinessProbe:
                  tcpSocket:
                    port: 8080
                  initialDelaySeconds: 15
                  periodSeconds: 10
                volumeMounts:
                  - mountPath: /dev/shm
                    name: dshm
            volumes:
            - name: dshm
              emptyDir:
                medium: Memory
                sizeLimit: 15Gi
        workerReplicas: 1
        workerTemplate:
          spec:
            containers:
              - name: worker
                image: vllm/vllm-openai:latest
                command:
                  - sh
                  - -c
                  - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh worker --ray_address=$(ENTRY_ADDRESS)"
                resources:
                  limits:
                    nvidia.com/gpu: "8"
                    memory: 1124Gi
                    ephemeral-storage: 800Gi
                  requests:
                    ephemeral-storage: 800Gi
                    cpu: 125
                env:
                  - name: HUGGING_FACE_HUB_TOKEN
                    valueFrom:
                      secretKeyRef:
                        name: hf-token
                        key: HUGGING_FACE_HUB_TOKEN
                volumeMounts:
                  - mountPath: /dev/shm
                    name: dshm   
            volumes:
            - name: dshm
              emptyDir:
                medium: Memory
                sizeLimit: 15Gi
EOF
```

Kthena will:

- Create a `ModelServing` object.
- Derive a `PodGroup` for Volcano gang scheduling.
- Create the leader and worker pods for each `ServingGroup` and `Role`.

* * *

## 4. Verifying the Deployment[¶](#4-verifying-the-deployment "Permanent link")

### 4.1 Check ModelServing Status[¶](#41-check-modelserving-status "Permanent link")

Use the snippet from the Kthena docs:

```
kubectlgetmodelserving-oyaml|grepstatus-A10
```

You should see something like:

```
status:
availableReplicas:1
conditions:
-type:Available
status:"True"
reason:AllGroupsReady
message:All Serving groups are ready
-type:Progressing
status:"False"
...
replicas:1
updatedReplicas:1
```

### 4.2 Check Pods[¶](#42-check-pods "Permanent link")

List pods for your deployment:

```
kubectlgetpod-owide-lmodelserving.volcano.sh/name=llama-multinode
```

Example output (from docs):

```
NAMESPACE   NAME                          READY   STATUS    RESTARTS   AGE   IP            NODE           ...
default     llama-multinode-0-405b-0-0    1/1     Running   0          15m   10.244.0.56   192.168.5.12   ...
default     llama-multinode-0-405b-0-1    1/1     Running   0          15m   10.244.0.58   192.168.5.43   ...
default     llama-multinode-0-405b-1-0    1/1     Running   0          15m   10.244.0.57   192.168.5.58   ...
default     llama-multinode-0-405b-1-1    1/1     Running   0          15m   10.244.0.53   192.168.5.36   ...
```

Pod name pattern:

- `llama-multinode-<group-idx>-<role-name>-<replica-idx>-<ordinal>`.

The first number indicates `ServingGroup`. The second (`405b`) is the `Role`. The remaining indices identify the pod within the role.

* * *

## 6. Accessing the vLLM OpenAI-Compatible API[¶](#6-accessing-the-vllm-openai-compatible-api "Permanent link")

Expose the entry via a Service:

```
apiVersion:v1
kind:Service
metadata:
name:llama-multinode-openai
namespace:default
spec:
selector:
modelserving.volcano.sh/name:llama-multinode
modelserving.volcano.sh/entry:"true"
# optionally further narrow to leader role if you label it
ports:
-name:http
port:80
targetPort:8080
type:ClusterIP
```

Port-forward from your local machine:

```
kubectlport-forwardsvc/llama-multinode-openai30080:80-ndefault
```

Then:

- List models:

```
curl-shttp://localhost:30080/v1/models
```

- Send a completion request (mirroring vLLM production stack docs):

```
curl-XPOSThttp://localhost:30080/v1/completions\
-H"Content-Type: application/json"\
-d'{
    "model": "meta-llama/Llama-3.1-405B-Instruct",
    "prompt": "Once upon a time,",
    "max_tokens": 10
  }'
```

You should see an OpenAI-style response from vLLM.

* * *

## 7. Clean Up[¶](#7-clean-up "Permanent link")

To remove the deployment and its resources:

```
kubectldeletemodelservingllama-multinode-ndefault
```

If you’re done with the entire stack:

```
helmuninstallkthena-nkthena-system# or your Kthena release name
helmuninstallvolcano-nvolcano-system
```