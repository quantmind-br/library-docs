---
title: Kubernetes
url: https://docs.docker.com/desktop/use-desktop/kubernetes/
source: llms
fetched_at: 2026-01-24T14:19:23.80675919-03:00
rendered_js: false
word_count: 1078
summary: This document explains how to enable, configure, and manage local Kubernetes clusters within Docker Desktop, covering provisioning methods like kubeadm and kind, resource monitoring, and advanced configuration.
tags:
    - docker-desktop
    - kubernetes
    - kubeadm
    - kind
    - cluster-management
    - kubectl
    - local-development
category: guide
---

## Explore the Kubernetes view

Docker Desktop includes a standalone Kubernetes server and client, as well as Docker CLI integration, enabling local Kubernetes development and testing directly on your machine.

The Kubernetes server runs as a single or multi-node cluster, within Docker containers. This lightweight setup helps you explore Kubernetes features, test workloads, and work with container orchestration in parallel with other Docker features.

With Docker Desktop version 4.51 and later, you can manage Kubernetes directly from the **Kubernetes** view in the Docker Desktop Dashboard.

1. Open the Docker Desktop Dashboard and select the **Kubernetes** view.
2. Select **Create cluster**.
3. Choose your cluster type:
   
   - **Kubeadm** creates a single-node cluster and the version is set by Docker Desktop.
   - **kind** creates a multi-node cluster and you can set the version and number of nodes. For more detailed information on each cluster type, see [Cluster provisioining method](#cluster-provisioning-method).
4. Optional: Select **Show system containers (advanced)** to view internal containers when using Docker commands.
5. Select **Create**.

This sets up the images required to run the Kubernetes server as containers, and installs the `kubectl` command-line tool on your system at `/usr/local/bin/kubectl` (Mac) or `C:\Program Files\Docker\Docker\resources\bin\kubectl.exe` (Windows). If you installed `kubectl` using Homebrew, or by some other method, and experience conflicts, remove `/usr/local/bin/kubectl`.

> Docker Desktop for Linux does not include `kubectl` by default. You can install it separately by following the [Kubernetes installation guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/). Ensure the `kubectl` binary is installed at `/usr/local/bin/kubectl`.

The following actions are also triggered in the Docker Desktop backend and VM:

- Generation of certificates and cluster configuration
- Download and installation of Kubernetes internal components
- Cluster bootup
- Installation of additional controllers for networking and storage

When Kubernetes is enabled, its status is displayed in the Docker Desktop Dashboard footer and the Docker menu.

You can check which version of Kubernetes you're on with:

### [Cluster provisioning method](#cluster-provisioning-method)

Docker Desktop Kubernetes can be provisioned with either the `kubeadm` or `kind` provisioners.

`kubeadm` is the older provisioner. It supports a single-node cluster, you can't select the kubernetes version, it's slower to provision than `kind`, and it's not supported by [Enhanced Container Isolation](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/) (ECI), meaning that if ECI is enabled the cluster works but it's not protected by ECI.

`kind` is the newer provisioner. It supports multi-node clusters (for a more realistic Kubernetes setup), you can choose the Kubernetes version, it's faster to provision than `kubeadm`, and it's supported by ECI - when ECI is enabled, the Kubernetes cluster runs in unprivileged Docker containers, thus making it more secure.

Feature`kubeadm``kind`Multi-node cluster supportNoYesKubernetes version selectorNoYesSpeed to provision~1 min~30 secondsSupported by ECINoYesWorks with containerd image storeYesYesWorks with Docker image storeYesNo

When a Kubernetes cluster is enabled, the **Kubernetes** view displays a live dashboard view showing:

- A namespace selector at the top
- A real-time list of resources - pods, services, deployments - in the selected namespace
- Automatic updates when resources are created, deleted, or modified

Confirm that your cluster is running:

If kubectl is pointing to another environment, switch to the Docker Desktop context:

> If no contexts appear, try:
> 
> - Running the command in the Command Prompt or PowerShell.
> - Setting the `KUBECONFIG` environment variable to point to your `.kube/config` file.

For more information about `kubectl`, see the [`kubectl` documentation](https://kubernetes.io/docs/reference/kubectl/overview/).

When Kubernetes is enabled:

- Select **Edit cluster** to modify configuration. For example, switch between **kubeadm** and **kind**, or change the number of nodes.
- Select **Stop** to disable the cluster. Progress is displayed, and the **Kubernetes** view returns to the **Create cluster** screen. This stops and removes Kubernetes containers, and also removes the `/usr/local/bin/kubectl` command.

Kubernetes clusters are not automatically upgraded with Docker Desktop updates. To upgrade the cluster, you must manually select **Reset cluster** in the **Kubernetes** settings.

Docker Desktop uses containers to run the Kubernetes control plane. By default, Docker Desktop pulls the associated container images from Docker Hub. The images pulled depend on the [cluster provisioning mode](#cluster-provisioning-method).

For example, in `kind` mode it requires the following images:

In `kubeadm` mode it requires the following images:

The image tags are automatically selected by Docker Desktop based on several factors, including the version of Kubernetes being used. The tags vary for each image and may change between Docker Desktop releases. To stay informed, monitor the Docker Desktop release notes.

To accommodate scenarios where access to Docker Hub is not allowed, admins can configure Docker Desktop to pull the above listed images from a different registry (e.g., a mirror) using the [KubernetesImagesRepository](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/#kubernetes) setting as follows.

An image name can be broken into `[registry[:port]/][namespace/]repository[:tag]` components. The `KubernetesImagesRepository` setting allows users to override the `[registry[:port]/][namespace]` portion of the image's name.

For example, if Docker Desktop Kubernetes is configured in `kind` mode and `KubernetesImagesRepository` is set to `my-registry:5000/kind-images`, then Docker Desktop will pull the images from:

These images should be cloned/mirrored from their respective images in Docker Hub. The tags must also match what Docker Desktop expects.

The recommended approach to set this up is the following:

1. Start Kubernetes using the desired cluster provisioning method: `kubeadm` or `kind`.
2. Once Kubernetes has started, use `docker ps` to view the container images used by Docker Desktop for the Kubernetes control plane.
3. Clone or mirror those images (with matching tags) to your custom registry.
4. Stop the Kubernetes cluster.
5. Configure the `KubernetesImagesRepository` setting to point to your custom registry.
6. Restart Docker Desktop.
7. Verify that the Kubernetes cluster is using the custom registry images using the `docker ps` command.

> The `KubernetesImagesRepository` setting only applies to control plane images used by Docker Desktop to set up the Kubernetes cluster. It has no effect on other Kubernetes pods.

> In Docker Desktop versions 4.43 or earlier, when using `KubernetesImagesRepository` and [Enhanced Container Isolation (ECI)](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/) is enabled, add the following images to the [ECI Docker socket mount image list](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/#enhanced-container-isolation):
> 
> `[imagesRepository]/desktop-cloud-provider-kind:` `[imagesRepository]/desktop-containerd-registry-mirror:`
> 
> These containers mount the Docker socket, so you must add the images to the ECI images list. If not, ECI will block the mount and Kubernetes won't start.

- If Kubernetes fails to start, make sure Docker Desktop is running with enough allocated resources. Check **Settings** &gt; **Resources**.
- If the `kubectl` commands return errors, confirm the context is set to `docker-desktop`You can then try checking the logs of the Kubernetes system containers if you have enabled that setting.
- If you're experiencing cluster issues after updating, reset your Kubernetes cluster. Resetting a Kubernetes cluster can help resolve issues by essentially reverting the cluster to a clean state, and clearing out misconfigurations, corrupted data, or stuck resources that may be causing problems. If the issue still persists, you may need to clean and purge data, and then restart Docker Desktop.