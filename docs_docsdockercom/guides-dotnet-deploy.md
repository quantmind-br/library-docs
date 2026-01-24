---
title: Test your deployment
url: https://docs.docker.com/guides/dotnet/deploy/
source: llms
fetched_at: 2026-01-24T14:04:35.684416913-03:00
rendered_js: false
word_count: 390
summary: This document provides a step-by-step guide on how to deploy a containerized .NET application and its database to a local Kubernetes cluster using Docker Desktop.
tags:
    - kubernetes
    - docker-desktop
    - dotnet
    - deployment
    - kubectl
    - yaml-configuration
    - local-development
category: tutorial
---

## [Prerequisites](#prerequisites)

- Complete all the previous sections of this guide, starting with [Containerize a .NET application](https://docs.docker.com/guides/dotnet/containerize/).
- [Turn on Kubernetes](https://docs.docker.com/desktop/use-desktop/kubernetes/#enable-kubernetes) in Docker Desktop.

## [Overview](#overview)

In this section, you'll learn how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine. This allows you to test and debug your workloads on Kubernetes locally before deploying.

## [Create a Kubernetes YAML file](#create-a-kubernetes-yaml-file)

In your `docker-dotnet-sample` directory, create a file named `docker-dotnet-kubernetes.yaml`. Open the file in an IDE or text editor and add the following contents. Replace `DOCKER_USERNAME/REPO_NAME` with your Docker username and the name of the repository that you created in [Configure CI/CD for your .NET application](https://docs.docker.com/guides/dotnet/configure-ci-cd/).

```
apiVersion:apps/v1kind:Deploymentmetadata:labels:service:servername:servernamespace:defaultspec:replicas:1selector:matchLabels:service:serverstrategy:{}template:metadata:labels:service:serverspec:initContainers:- name:wait-for-dbimage:busybox:1.28command:["sh","-c",'until nc -zv db 5432; do echo "waiting for db"; sleep 2; done;',]containers:- image:DOCKER_USERNAME/REPO_NAMEname:serverimagePullPolicy:Alwaysports:- containerPort:8080hostPort:8080protocol:TCPresources:{}restartPolicy:Alwaysstatus:{}---apiVersion:apps/v1kind:Deploymentmetadata:labels:service:dbname:dbnamespace:defaultspec:replicas:1selector:matchLabels:service:dbstrategy:type:Recreatetemplate:metadata:labels:service:dbspec:containers:- env:- name:POSTGRES_DBvalue:example- name:POSTGRES_PASSWORDvalue:exampleimage:postgres:18name:dbports:- containerPort:5432protocol:TCPresources:{}restartPolicy:Alwaysstatus:{}---apiVersion:v1kind:Servicemetadata:labels:service:servername:servernamespace:defaultspec:type:NodePortports:- name:"8080"port:8080targetPort:8080nodePort:30001selector:service:serverstatus:loadBalancer:{}---apiVersion:v1kind:Servicemetadata:labels:service:dbname:dbnamespace:defaultspec:ports:- name:"5432"port:5432targetPort:5432selector:service:dbstatus:loadBalancer:{}
```

In this Kubernetes YAML file, there are four objects, separated by the `---`. In addition to a Service and Deployment for the database, the other two objects are:

- A Deployment, describing a scalable group of identical pods. In this case, you'll get just one replica, or copy of your pod. That pod, which is described under `template`, has just one container in it. The container is created from the image built by GitHub Actions in [Configure CI/CD for your .NET application](https://docs.docker.com/guides/dotnet/configure-ci-cd/).
- A NodePort service, which will route traffic from port 30001 on your host to port 8080 inside the pods it routes to, allowing you to reach your app from the network.

To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

## [Deploy and check your application](#deploy-and-check-your-application)

1. In a terminal, navigate to the `docker-dotnet-sample` directory and deploy your application to Kubernetes.
   
   ```
   $ kubectl apply -f docker-dotnet-kubernetes.yaml
   ```
   
   You should see output that looks like the following, indicating your Kubernetes objects were created successfully.
   
   ```
   deployment.apps/db created
   service/db created
   deployment.apps/server created
   service/server created
   ```
2. Make sure everything worked by listing your deployments.
   
   ```
   $ kubectl get deployments
   ```
   
   Your deployment should be listed as follows:
   
   ```
   NAME     READY   UP-TO-DATE   AVAILABLE   AGE
   db       1/1     1            1           76s
   server   1/1     1            1           76s
   ```
   
   This indicates all of the pods are up and running. Do the same check for your services.
   
   You should get output like the following.
   
   ```
   NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
   db           ClusterIP   10.96.156.90    <none>        5432/TCP         2m8s
   kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          164m
   server       NodePort    10.102.94.225   <none>        8080:30001/TCP   2m8s
   ```
   
   In addition to the default `kubernetes` service, you can see your `server` service and `db` service. The `server` service is accepting traffic on port 30001/TCP.
3. Open a browser and visit your app at `localhost:30001`. You should see your application.
4. Run the following command to tear down your application.
   
   ```
   $ kubectl delete -f docker-dotnet-kubernetes.yaml
   ```

## [Summary](#summary)

In this section, you learned how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine.

Related information:

- [Kubernetes documentation](https://kubernetes.io/docs/home/)
- [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/use-desktop/kubernetes/)
- [Swarm mode overview](https://docs.docker.com/engine/swarm/)