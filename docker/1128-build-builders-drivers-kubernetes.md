---
title: Kubernetes driver
url: https://docs.docker.com/build/builders/drivers/kubernetes/
source: llms
fetched_at: 2026-01-24T14:15:28.533306204-03:00
rendered_js: false
word_count: 1193
summary: This document explains how to use the Kubernetes driver for Docker Buildx to perform container builds within a Kubernetes cluster, covering scaling, resource management, and multi-platform support.
tags:
    - docker-buildx
    - kubernetes-driver
    - buildkit
    - multi-platform
    - container-scaling
    - resource-management
category: guide
---

The Kubernetes driver lets you connect your local development or CI environments to builders in a Kubernetes cluster to allow access to more powerful compute resources, optionally on multiple native architectures.

Run the following command to create a new builder, named `kube`, that uses the Kubernetes driver:

The following table describes the available driver-specific options that you can pass to `--driver-opt`:

ParameterTypeDefaultDescription`image`StringSets the image to use for running BuildKit.`namespace`StringNamespace in current Kubernetes contextSets the Kubernetes namespace.`default-load`Boolean`false`Automatically load images to the Docker Engine image store.`replicas`Integer1Sets the number of Pod replicas to create. See [scaling BuildKit](#scaling-buildkit)`requests.cpu`CPU unitsSets the request CPU value specified in units of Kubernetes CPU. For example `requests.cpu=100m` or `requests.cpu=2``requests.memory`Memory sizeSets the request memory value specified in bytes or with a valid suffix. For example `requests.memory=500Mi` or `requests.memory=4G``requests.ephemeral-storage`Storage sizeSets the request ephemeral-storage value specified in bytes or with a valid suffix. For example `requests.ephemeral-storage=2Gi``limits.cpu`CPU unitsSets the limit CPU value specified in units of Kubernetes CPU. For example `requests.cpu=100m` or `requests.cpu=2``limits.memory`Memory sizeSets the limit memory value specified in bytes or with a valid suffix. For example `requests.memory=500Mi` or `requests.memory=4G``limits.ephemeral-storage`Storage sizeSets the limit ephemeral-storage value specified in bytes or with a valid suffix. For example `requests.ephemeral-storage=100M``buildkit-root-volume-memory`Memory sizeUsing regular file systemMounts `/var/lib/buildkit` on an `emptyDir` memory-backed volume, with `SizeLimit` as the value. For example, `buildkit-root-folder-memory=6G``nodeselector`CSV stringSets the pod's `nodeSelector` label(s). See [node assignment](#node-assignment).`annotations`CSV stringSets additional annotations on the deployments and pods.`labels`CSV stringSets additional labels on the deployments and pods.`tolerations`CSV stringConfigures the pod's taint toleration. See [node assignment](#node-assignment).`serviceaccount`StringSets the pod's `serviceAccountName`.`schedulername`StringSets the scheduler responsible for scheduling the pod.`timeout`Time`120s`Set the timeout limit that determines how long Buildx will wait for pods to be provisioned before a build.`rootless`Boolean`false`Run the container as a non-root user. See [rootless mode](#rootless-mode).`loadbalance`String`sticky`Load-balancing strategy (`sticky` or `random`). If set to `sticky`, the pod is chosen using the hash of the context path.`qemu.install`Boolean`false`Install QEMU emulation for multi platforms support. See [QEMU](#qemu).`qemu.image`String`tonistiigi/binfmt:latest`Sets the QEMU emulation image. See [QEMU](#qemu).

One of the main advantages of the Kubernetes driver is that you can scale the number of builder replicas up and down to handle increased build load. Scaling is configurable using the following driver options:

- `replicas=N`
  
  This scales the number of BuildKit pods to the desired size. By default, it only creates a single pod. Increasing the number of replicas lets you take advantage of multiple nodes in your cluster.
- `requests.cpu`, `requests.memory`, `requests.ephemeral-storage`, `limits.cpu`, `limits.memory`, `limits.ephemeral-storage`
  
  These options allow requesting and limiting the resources available to each BuildKit pod [according to the official Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

For example, to create 4 replica BuildKit pods:

Listing the pods, you get this:

Additionally, you can use the `loadbalance=(sticky|random)` option to control the load-balancing behavior when there are multiple replicas. `random` selects random nodes from the node pool, providing an even workload distribution across replicas. `sticky` (the default) attempts to connect the same build performed multiple times to the same node each time, ensuring better use of local cache.

For more information on scalability, see the options for [`docker buildx create`](https://docs.docker.com/reference/cli/docker/buildx/create/#driver-opt).

The Kubernetes driver allows you to control the scheduling of BuildKit pods using the `nodeSelector` and `tolerations` driver options. You can also set the `schedulername` option if you want to use a custom scheduler altogether.

You can use the `annotations` and `labels` driver options to apply additional metadata to the deployments and pods that's hosting your builders.

The value of the `nodeSelector` parameter is a comma-separated string of key-value pairs, where the key is the node label and the value is the label text. For example: `"nodeselector=kubernetes.io/arch=arm64"`

The `tolerations` parameter is a semicolon-separated list of taints. It accepts the same values as the Kubernetes manifest. Each `tolerations` entry specifies a taint key and the value, operator, or effect. For example: `"tolerations=key=foo,value=bar;key=foo2,operator=exists;key=foo3,effect=NoSchedule"`

These options accept CSV-delimited strings as values. Due to quoting rules for shell commands, you must wrap the values in single quotes. You can even wrap all of `--driver-opt` in single quotes, for example:

The Kubernetes driver has support for creating [multi-platform images](https://docs.docker.com/build/building/multi-platform/), either using QEMU or by leveraging the native architecture of nodes.

### [QEMU](#qemu)

Like the `docker-container` driver, the Kubernetes driver also supports using [QEMU](https://www.qemu.org/) (user mode) to build images for non-native platforms. Include the `--platform` flag and specify which platforms you want to output to.

For example, to build a Linux image for `amd64` and `arm64`:

> QEMU performs full-CPU emulation of non-native platforms, which is much slower than native builds. Compute-heavy tasks like compilation and compression/decompression will likely take a large performance hit.

Using a custom BuildKit image or invoking non-native binaries in builds may require that you explicitly turn on QEMU using the `qemu.install` option when creating the builder:

### [Native](#native)

If you have access to cluster nodes of different architectures, the Kubernetes driver can take advantage of these for native builds. To do this, use the `--append` flag of `docker buildx create`.

First, create your builder with explicit support for a single architecture, for example `amd64`:

This creates a Buildx builder named `kube`, containing a single builder node named `builder-amd64`. Assigning a node name using `--node` is optional. Buildx generates a random node name if you don't provide one.

Note that the Buildx concept of a node isn't the same as the Kubernetes concept of a node. A Buildx node in this case could connect multiple Kubernetes nodes of the same architecture together.

With the `kube` builder created, you can now introduce another architecture into the mix using `--append`. For example, to add `arm64`:

Listing your builders shows both nodes for the `kube` builder:

You can now build multi-arch `amd64` and `arm64` images, by specifying those platforms together in your build command:

You can repeat the `buildx create --append` command for as many architectures that you want to support.

The Kubernetes driver supports rootless mode. For more information on how rootless mode works, and its requirements, refer to the [Rootless Buildkit documentation](https://github.com/moby/buildkit/blob/master/docs/rootless.md).

To turn it on in your cluster, you can use the `rootless=true` driver option:

This will create your pods without `securityContext.privileged`.

Requires Kubernetes version 1.19 or later. Using Ubuntu as the host kernel is recommended.

This guide shows you how to:

- Create a namespace for your Buildx resources
- Create a Kubernetes builder.
- List the available builders
- Build an image using your Kubernetes builders

Prerequisites:

- You have an existing Kubernetes cluster. If you don't already have one, you can follow along by installing [minikube](https://minikube.sigs.k8s.io/docs/).
- The cluster you want to connect to is accessible via the `kubectl` command, with the `KUBECONFIG` environment variable [set appropriately](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/#set-the-kubeconfig-environment-variable) if necessary.

<!--THE END-->

1. Create a `buildkit` namespace.
   
   Creating a separate namespace helps keep your Buildx resources separate from other resources in the cluster.
2. Create a new builder with the Kubernetes driver:
   
   > Remember to specify the namespace in driver options.
3. List available builders using `docker buildx ls`
4. Inspect the running pods created by the build driver with `kubectl`.
   
   The build driver creates the necessary resources on your cluster in the specified namespace (in this case, `buildkit`), while keeping your driver configuration locally.
5. Use your new builder by including the `--builder` flag when running buildx commands. For example: :

That's it: you've now built an image from a Kubernetes pod, using Buildx.

For more information on the Kubernetes driver, see the [buildx reference](https://docs.docker.com/reference/cli/docker/buildx/create/#driver).