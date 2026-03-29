---
title: Use an image in Kubernetes
url: https://docs.docker.com/dhi/how-to/k8s/
source: llms
fetched_at: 2026-01-24T14:20:47.096229221-03:00
rendered_js: false
word_count: 169
summary: This document provides instructions for authenticating and using Docker Hardened Images within a Kubernetes cluster by creating image pull secrets and verifying the configuration.
tags:
    - kubernetes
    - docker-hardened-images
    - image-pull-secrets
    - container-security
    - authentication
    - registry-secrets
category: tutorial
---

## Use a Docker Hardened Image in Kubernetes

Table of contents

* * *

## [Authentication](#authentication)

To be able to use Docker Hardened Images in Kubernetes, you need to create a Kubernetes secret for pulling images from your mirror or internal registry.

> Note
> 
> You need to create this secret in each Kubernetes namespace that uses a DHI.

Create a secret using a Personal Access Token (PAT). Ensure the token has at least read-only access to public repositories. For Docker Hardened Images replace `<registry server>` with `dhi.io`. If you are using a mirrored repository, replace it with your mirror's registry server, such as `docker.io` for Docker Hub.

```
$ kubectl create -n <kubernetes namespace> secret docker-registry <secret name> --docker-server=<registry server> \
        --docker-username=<registry user> --docker-password=<access token> \
        --docker-email=<registry email>
```

To tests the secrets use the following command:

```
kubectl apply --wait -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: dhi-test
  namespace: <kubernetes namespace>
spec:
  containers:
  - name: test
    image: bash:5
    command: [ "sh", "-c", "echo 'Hello from DHI in Kubernetes!'" ]
  imagePullSecrets:
  - name: <secret name>
EOF
```

Get the status of the pod by running:

```
$ kubectl get -n <kubernetes namespace> pods/dhi-test
```

The command should return the following result:

```
NAME       READY   STATUS      RESTARTS     AGE
dhi-test   0/1     Completed   ...          ...
```

If instead, the result is the following, there might be an issue with your secret.

```
NAME       READY   STATUS         RESTARTS   AGE
dhi-test   0/1     ErrImagePull   0          ...
```

Verify the output of the pod by running, which should return `Hello from DHI in Kubernetes!`

```
kubectl logs -n <kubernetes namespace> pods/dhi-test
```

After a successful test, the test pod can be deleted with the following command:

```
$ kubectl delete -n <kubernetes namespace> pods/dhi-test
```