---
title: Test your deployment
url: https://docs.docker.com/guides/rust/deploy/
source: llms
fetched_at: 2026-01-24T14:11:55.058679832-03:00
rendered_js: false
word_count: 378
summary: This guide explains how to deploy a Rust application and a PostgreSQL database to a local Kubernetes environment using Docker Desktop for development and testing. It covers creating YAML manifests for deployments and services and using kubectl to manage the application lifecycle.
tags:
    - kubernetes
    - docker-desktop
    - rust
    - local-development
    - container-orchestration
    - kubectl
    - deployment-manifest
category: tutorial
---

## [Prerequisites](#prerequisites)

- Complete the previous sections of this guide, starting with [Develop your Rust application](https://docs.docker.com/guides/rust/develop/).
- [Turn on Kubernetes](https://docs.docker.com/desktop/use-desktop/kubernetes/#enable-kubernetes) in Docker Desktop.

## [Overview](#overview)

In this section, you'll learn how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine. This lets you to test and debug your workloads on Kubernetes locally before deploying.

## [Create a Kubernetes YAML file](#create-a-kubernetes-yaml-file)

In your `docker-rust-postgres` directory, create a file named `docker-rust-kubernetes.yaml`. Open the file in an IDE or text editor and add the following contents. Replace `DOCKER_USERNAME/REPO_NAME` with your Docker username and the name of the repository that you created in [Configure CI/CD for your Rust application](https://docs.docker.com/guides/rust/configure-ci-cd/).

```
apiVersion:apps/v1kind:Deploymentmetadata:labels:service:servername:servernamespace:defaultspec:replicas:1selector:matchLabels:service:serverstrategy:{}template:metadata:labels:service:serverspec:initContainers:- name:wait-for-dbimage:busybox:1.28command:["sh","-c",'until nc -zv db 5432; do echo "waiting for db"; sleep 2; done;',]containers:- image:DOCKER_USERNAME/REPO_NAMEname:serverimagePullPolicy:Alwaysports:- containerPort:8000hostPort:5000protocol:TCPenv:- name:ADDRESSvalue:0.0.0.0:8000- name:PG_DBNAMEvalue:example- name:PG_HOSTvalue:db- name:PG_PASSWORDvalue:mysecretpassword- name:PG_USERvalue:postgres- name:RUST_LOGvalue:debugresources:{}restartPolicy:Alwaysstatus:{}---apiVersion:apps/v1kind:Deploymentmetadata:labels:service:dbname:dbnamespace:defaultspec:replicas:1selector:matchLabels:service:dbstrategy:type:Recreatetemplate:metadata:labels:service:dbspec:containers:- env:- name:POSTGRES_DBvalue:example- name:POSTGRES_PASSWORDvalue:mysecretpassword- name:POSTGRES_USERvalue:postgresimage:postgres:18name:dbports:- containerPort:5432protocol:TCPresources:{}restartPolicy:Alwaysstatus:{}---apiVersion:v1kind:Servicemetadata:labels:service:servername:servernamespace:defaultspec:type:NodePortports:- name:"5000"port:5000targetPort:8000nodePort:30001selector:service:serverstatus:loadBalancer:{}---apiVersion:v1kind:Servicemetadata:labels:service:dbname:dbnamespace:defaultspec:ports:- name:"5432"port:5432targetPort:5432selector:service:dbstatus:loadBalancer:{}
```

In this Kubernetes YAML file, there are four objects, separated by the `---`. In addition to a Service and Deployment for the database, the other two objects are:

- A Deployment, describing a scalable group of identical pods. In this case, you'll get just one replica, or copy of your pod. That pod, which is described under `template`, has just one container in it. The container is created from the image built by GitHub Actions in [Configure CI/CD for your Rust application](https://docs.docker.com/guides/rust/configure-ci-cd/).
- A NodePort service, which will route traffic from port 30001 on your host to port 5000 inside the pods it routes to, allowing you to reach your app from the network.

To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

## [Deploy and check your application](#deploy-and-check-your-application)

1. In a terminal, navigate to `docker-rust-postgres` and deploy your application to Kubernetes.
   
   ```
   $ kubectl apply -f docker-rust-kubernetes.yaml
   ```
   
   You should see output that looks like the following, indicating your Kubernetes objects were created successfully.
   
   ```
   deployment.apps/server created
   deployment.apps/db created
   service/server created
   service/db created
   ```
2. Make sure everything worked by listing your deployments.
   
   ```
   $ kubectl get deployments
   ```
   
   Your deployment should be listed as follows:
   
   ```
   NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
   db       1/1     1            1           2m21s
   server   1/1     1            1           2m21s
   ```
   
   This indicates all of the pods you asked for in your YAML are up and running. Do the same check for your services.
   
   You should get output like the following.
   
   ```
   NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
   db           ClusterIP   10.105.167.81    <none>        5432/TCP         109s
   kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          9d
   server       NodePort    10.101.235.213   <none>        5000:30001/TCP   109s
   ```
   
   In addition to the default `kubernetes` service, you can see your `service-entrypoint` service, accepting traffic on port 30001/TCP.
3. In a terminal, curl the service.
   
   ```
   $ curl http://localhost:30001/users
   [{"id":1,"login":"root"}]
   ```
4. Run the following command to tear down your application.
   
   ```
   $ kubectl delete -f docker-rust-kubernetes.yaml
   ```

## [Summary](#summary)

In this section, you learned how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine.

Related information:

- [Kubernetes documentation](https://kubernetes.io/docs/home/)
- [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/use-desktop/kubernetes/)
- [Swarm mode overview](https://docs.docker.com/engine/swarm/)