---
title: Test your deployment
url: https://docs.docker.com/guides/cpp/deploy/
source: llms
fetched_at: 2026-01-24T14:03:42.000654417-03:00
rendered_js: false
word_count: 375
summary: This document explains how to deploy a containerized C++ application to a local Kubernetes environment using Docker Desktop and kubectl.
tags:
    - kubernetes
    - docker-desktop
    - cpp
    - container-deployment
    - kubectl
    - local-development
    - yaml-configuration
category: tutorial
---

## [Prerequisites](#prerequisites)

- Complete all the previous sections of this guide, starting with [Containerize a C++ application](https://docs.docker.com/guides/cpp/containerize/).
- [Turn on Kubernetes](https://docs.docker.com/desktop/use-desktop/kubernetes/#enable-kubernetes) in Docker Desktop.

## [Overview](#overview)

In this section, you'll learn how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine. This allows you to test and debug your workloads on Kubernetes locally before deploying.

## [Create a Kubernetes YAML file](#create-a-kubernetes-yaml-file)

In your `c-plus-plus-docker` directory, create a file named `docker-kubernetes.yml`. Open the file in an IDE or text editor and add the following contents. Replace `DOCKER_USERNAME/REPO_NAME` with your Docker username and the name of the repository that you created in [Configure CI/CD for your C++ application](https://docs.docker.com/guides/cpp/configure-ci-cd/).

```
apiVersion:apps/v1kind:Deploymentmetadata:name:docker-c-plus-plus-demonamespace:defaultspec:replicas:1selector:matchLabels:service:ok-apitemplate:metadata:labels:service:ok-apispec:containers:- name:ok-api-serviceimage:DOCKER_USERNAME/REPO_NAMEimagePullPolicy:Always---apiVersion:v1kind:Servicemetadata:name:service-entrypointnamespace:defaultspec:type:NodePortselector:service:ok-apiports:- port:8080targetPort:8080nodePort:30001
```

In this Kubernetes YAML file, there are two objects, separated by the `---`:

- A Deployment, describing a scalable group of identical pods. In this case, you'll get just one replica, or copy of your pod. That pod, which is described under `template`, has just one container in it. The container is created from the image built by GitHub Actions in [Configure CI/CD for your C++ application](https://docs.docker.com/guides/cpp/configure-ci-cd/).
- A NodePort service, which will route traffic from port 30001 on your host to port 8080 inside the pods it routes to, allowing you to reach your app from the network.

To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

## [Deploy and check your application](#deploy-and-check-your-application)

1. In a terminal, navigate to `c-plus-plus-docker` and deploy your application to Kubernetes.
   
   ```
   $ kubectl apply -f docker-kubernetes.yml
   ```
   
   You should see output that looks like the following, indicating your Kubernetes objects were created successfully.
   
   ```
   deployment.apps/docker-c-plus-plus-demo created
   service/service-entrypoint created
   ```
2. Make sure everything worked by listing your deployments.
   
   ```
   $ kubectl get deployments
   ```
   
   Your deployment should be listed as follows:
   
   ```
   NAME                     READY   UP-TO-DATE   AVAILABLE    AGE
   docker-c-plus-plus-demo   1/1     1            1           10s
   ```
   
   This indicates all one of the pods you asked for in your YAML are up and running. Do the same check for your services.
   
   You should get output like the following.
   
   ```
   NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
   kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          88m
   service-entrypoint   NodePort    10.105.145.223   <none>        8080:30001/TCP   83s
   ```
   
   In addition to the default `kubernetes` service, you can see your `service-entrypoint` service, accepting traffic on port 30001/TCP.
3. In a browser, visit the following address. You should see the message `{"Status" : "OK"}`.
4. Run the following command to tear down your application.
   
   ```
   $ kubectl delete -f docker-kubernetes.yml
   ```

## [Summary](#summary)

In this section, you learned how to use Docker Desktop to deploy your C++ application to a fully-featured Kubernetes environment on your development machine.

Related information:

- [Kubernetes documentation](https://kubernetes.io/docs/home/)
- [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/use-desktop/kubernetes/)
- [Swarm mode overview](https://docs.docker.com/engine/swarm/)