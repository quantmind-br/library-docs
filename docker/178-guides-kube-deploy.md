---
title: Deploy to Kubernetes
url: https://docs.docker.com/guides/kube-deploy/
source: llms
fetched_at: 2026-01-24T14:10:38.838660771-03:00
rendered_js: false
word_count: 734
summary: This document explains how to deploy a containerized application to a local Kubernetes environment using Docker Desktop. It guides users through creating Kubernetes YAML manifests to define deployments and services for managing application workloads.
tags:
    - docker-desktop
    - kubernetes-deployment
    - kubernetes-service
    - yaml-manifest
    - container-orchestration
    - local-development
category: tutorial
---

- Download and install Docker Desktop as described in [Get Docker](https://docs.docker.com/get-started/get-docker/).
- Work through containerizing an application in [Part 2](https://docs.docker.com/get-started/workshop/02_our_app/).
- Make sure that Kubernetes is turned on in Docker Desktop: If Kubernetes isn't running, follow the instructions in [Orchestration](https://docs.docker.com/guides/orchestration/) to finish setting it up.

Now that you've demonstrated that the individual components of your application run as stand-alone containers, it's time to arrange for them to be managed by an orchestrator like Kubernetes. Kubernetes provides many tools for scaling, networking, securing and maintaining your containerized applications, above and beyond the abilities of containers themselves.

In order to validate that your containerized application works well on Kubernetes, you'll use Docker Desktop's built in Kubernetes environment right on your development machine to deploy your application, before handing it off to run on a full Kubernetes cluster in production. The Kubernetes environment created by Docker Desktop is *fully featured*, meaning it has all the Kubernetes features your app will enjoy on a real cluster, accessible from the convenience of your development machine.

All containers in Kubernetes are scheduled as pods, which are groups of co-located containers that share some resources. Furthermore, in a realistic application you almost never create individual pods. Instead, most of your workloads are scheduled as deployments, which are scalable groups of pods maintained automatically by Kubernetes. Lastly, all Kubernetes objects can and should be described in manifests called Kubernetes YAML files. These YAML files describe all the components and configurations of your Kubernetes app, and can be used to create and destroy your app in any Kubernetes environment.

You already wrote a basic Kubernetes YAML file in the Orchestration overview part of this tutorial. Now, you can write a slightly more sophisticated YAML file to run and manage your Todo app, the container `getting-started` image created in [Part 2](https://docs.docker.com/get-started/workshop/02_our_app/) of the Quickstart tutorial. Place the following in a file called `bb.yaml`:

In this Kubernetes YAML file, there are two objects, separated by the `---`:

- A `Deployment`, describing a scalable group of identical pods. In this case, you'll get just one `replica`, or copy of your pod, and that pod (which is described under the `template:` key) has just one container in it, based off of your `getting-started` image from the previous step in this tutorial.
- A `NodePort` service, which will route traffic from port 30001 on your host to port 3000 inside the pods it routes to, allowing you to reach your Todo app from the network.

Also, notice that while Kubernetes YAML can appear long and complicated at first, it almost always follows the same pattern:

- The `apiVersion`, which indicates the Kubernetes API that parses this object
- The `kind` indicating what sort of object this is
- Some `metadata` applying things like names to your objects
- The `spec` specifying all the parameters and configurations of your object.

<!--THE END-->

1. In a terminal, navigate to where you created `bb.yaml` and deploy your application to Kubernetes:
   
   You should see output that looks like the following, indicating your Kubernetes objects were created successfully:
2. Make sure everything worked by listing your deployments:
   
   if all is well, your deployment should be listed as follows:
   
   This indicates all one of the pods you asked for in your YAML are up and running. Do the same check for your services:
   
   In addition to the default `kubernetes` service, we see our `bb-entrypoint` service, accepting traffic on port 30001/TCP.
3. Open a browser and visit your Todo app at `localhost:30001`. You should see your Todo application, the same as when you ran it as a stand-alone container in [Part 2](https://docs.docker.com/get-started/workshop/02_our_app/) of the tutorial.
4. Once satisfied, tear down your application:

At this point, you have successfully used Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine. You can now add other components to your app and taking advantage of all the features and power of Kubernetes, right on your own machine.

In addition to deploying to Kubernetes, you have also described your application as a Kubernetes YAML file. This simple text file contains everything you need to create your application in a running state. You can check it in to version control and share it with your colleagues. This let you distribute your applications to other clusters (like the testing and production clusters that probably come after your development environments).

Further documentation for all new Kubernetes objects used in this article are available here:

- [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/)
- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)