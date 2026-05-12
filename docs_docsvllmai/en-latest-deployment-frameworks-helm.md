---
title: Helm - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/helm/
source: sitemap
fetched_at: 2026-05-07T21:11:46.025765177-03:00
rendered_js: false
word_count: 682
summary: This document provides instructions and configuration details for deploying vLLM applications on a Kubernetes cluster using the Helm package manager.
tags:
    - vllm
    - kubernetes
    - helm-chart
    - deployment
    - infrastructure
    - gpu-orchestration
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/helm.md "Edit this page")

A Helm chart to deploy vLLM for Kubernetes

Helm is a package manager for Kubernetes. It helps automate the deployment of vLLM applications on Kubernetes. With Helm, you can deploy the same framework architecture with different configurations to multiple namespaces by overriding variable values.

This guide will walk you through the process of deploying vLLM with Helm, including the necessary prerequisites, steps for Helm installation and documentation on architecture and values file.

## Prerequisites[¶](#prerequisites "Permanent link")

Before you begin, ensure that you have the following:

- A running Kubernetes cluster
- NVIDIA Kubernetes Device Plugin (`k8s-device-plugin`): This can be found at [https://github.com/NVIDIA/k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)
- Available GPU resources in your cluster
- (Optional) An S3 bucket or other storage with the model weights, if using automatic model download

## Installing the chart[¶](#installing-the-chart "Permanent link")

This guide uses the Helm chart at [examples/online\_serving/chart-helm](https://github.com/vllm-project/vllm/tree/main/examples/online_serving/chart-helm).

To install the chart with the release name `test-vllm`:

```
helmupgrade--install--create-namespace\
--namespace=ns-vllmtest-vllm.\
-fvalues.yaml\
--setsecrets.s3endpoint=$ACCESS_POINT\
--setsecrets.s3bucketname=$BUCKET\
--setsecrets.s3accesskeyid=$ACCESS_KEY\
--setsecrets.s3accesskey=$SECRET_KEY
```

## Uninstalling the chart[¶](#uninstalling-the-chart "Permanent link")

To uninstall the `test-vllm` deployment:

```
helmuninstalltest-vllm--namespace=ns-vllm
```

The command removes all the Kubernetes components associated with the chart **including persistent volumes** and deletes the release.

## Architecture[¶](#architecture "Permanent link")

[![helm deployment architecture](https://docs.vllm.ai/en/latest/assets/deployment/architecture_helm_deployment.png)](https://docs.vllm.ai/en/latest/assets/deployment/architecture_helm_deployment.png)

## Values[¶](#values "Permanent link")

The following table describes configurable parameters of the chart in `values.yaml`:

Key Type Default Description autoscaling object {"enabled":false,"maxReplicas":100,"minReplicas":1,"targetCPUUtilizationPercentage":80} Autoscaling configuration autoscaling.enabled bool false Enable autoscaling autoscaling.maxReplicas int 100 Maximum replicas autoscaling.minReplicas int 1 Minimum replicas autoscaling.targetCPUUtilizationPercentage int 80 Target CPU utilization for autoscaling configs object {} Configmap containerPort int 8000 Container port customObjects list \[] Custom Objects configuration deploymentStrategy object {} Deployment strategy configuration externalConfigs list \[] External configuration extraContainers list \[] Additional containers configuration extraInit object {"modelDownload":{"enabled":true},"initContainers":\[],"pvcStorage":"1Gi"} Additional configuration for init containers extraInit.modelDownload object {"enabled":true} Model download functionality configuration extraInit.modelDownload.enabled bool true Enable automatic model download job and wait container extraInit.modelDownload.image object {"repository":"amazon/aws-cli","tag":"2.6.4","pullPolicy":"IfNotPresent"} Image for model download operations extraInit.modelDownload.waitContainer object {} Wait container configuration (command, args, env) extraInit.modelDownload.downloadJob object {} Download job configuration (command, args, env) extraInit.initContainers list \[] Custom init containers (appended after model download if enabled) extraInit.pvcStorage string "1Gi" Storage size for the PVC extraInit.s3modelpath string "relative\_s3\_model\_path/opt-125m" (Optional) Path of the model on S3 extraInit.awsEc2MetadataDisabled bool true (Optional) Disable AWS EC2 metadata service extraPorts list \[] Additional ports configuration gpuModels list \["TYPE\_GPU\_USED"] Type of gpu used image object {"command":\["vllm","serve","/data/","--served-model-name","opt-125m","--host","0.0.0.0","--port","8000"],"repository":"vllm/vllm-openai","tag":"latest"} Image configuration image.command list \["vllm","serve","/data/","--served-model-name","opt-125m","--host","0.0.0.0","--port","8000"] Container launch command image.repository string "vllm/vllm-openai" Image repository image.tag string "latest" Image tag livenessProbe object {"failureThreshold":3,"httpGet":{"path":"/health","port":8000},"initialDelaySeconds":15,"periodSeconds":10} Liveness probe configuration livenessProbe.failureThreshold int 3 Number of times after which if a probe fails in a row, Kubernetes considers that the overall check has failed: the container is not alive livenessProbe.httpGet object {"path":"/health","port":8000} Configuration of the kubelet http request on the server livenessProbe.httpGet.path string "/health" Path to access on the HTTP server livenessProbe.httpGet.port int 8000 Name or number of the port to access on the container, on which the server is listening livenessProbe.initialDelaySeconds int 15 Number of seconds after the container has started before liveness probe is initiated livenessProbe.periodSeconds int 10 How often (in seconds) to perform the liveness probe maxUnavailablePodDisruptionBudget string "" Disruption Budget Configuration readinessProbe object {"failureThreshold":3,"httpGet":{"path":"/health","port":8000},"initialDelaySeconds":5,"periodSeconds":5} Readiness probe configuration readinessProbe.failureThreshold int 3 Number of times after which if a probe fails in a row, Kubernetes considers that the overall check has failed: the container is not ready readinessProbe.httpGet object {"path":"/health","port":8000} Configuration of the kubelet http request on the server readinessProbe.httpGet.path string "/health" Path to access on the HTTP server readinessProbe.httpGet.port int 8000 Name or number of the port to access on the container, on which the server is listening readinessProbe.initialDelaySeconds int 5 Number of seconds after the container has started before readiness probe is initiated readinessProbe.periodSeconds int 5 How often (in seconds) to perform the readiness probe replicaCount int 1 Number of replicas resources object {"limits":{"cpu":4,"memory":"16Gi","nvidia.com/gpu":1},"requests":{"cpu":4,"memory":"16Gi","nvidia.com/gpu":1}} Resource configuration resources.limits."nvidia.com/gpu" int 1 Number of GPUs used resources.limits.cpu int 4 Number of CPUs resources.limits.memory string "16Gi" CPU memory configuration resources.requests."nvidia.com/gpu" int 1 Number of GPUs used resources.requests.cpu int 4 Number of CPUs resources.requests.memory string "16Gi" CPU memory configuration secrets object {} Secrets configuration serviceName string "" Service name servicePort int 80 Service port labels.environment string test Environment name

## Configuration Examples[¶](#configuration-examples "Permanent link")

### Using S3 Model Download (Default)[¶](#using-s3-model-download-default "Permanent link")

```
extraInit:
modelDownload:
enabled:true
pvcStorage:"10Gi"
s3modelpath:"models/llama-7b"
```

### Using Custom Init Containers Only[¶](#using-custom-init-containers-only "Permanent link")

For use cases like llm-d where you need custom sidecars without model download:

```
extraInit:
modelDownload:
enabled:false
initContainers:
-name:llm-d-routing-proxy
image:ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
imagePullPolicy:IfNotPresent
ports:
-containerPort:8080
name:proxy
securityContext:
runAsUser:1000
restartPolicy:Always
pvcStorage:"10Gi"
```