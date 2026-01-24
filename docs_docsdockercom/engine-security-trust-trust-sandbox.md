---
title: Play in a content trust sandbox
url: https://docs.docker.com/engine/security/trust/trust_sandbox/
source: llms
fetched_at: 2026-01-24T14:25:31.731892913-03:00
rendered_js: false
word_count: 878
summary: This document explains how to set up and use a local sandbox environment to experiment with Docker Content Trust and image signing without affecting production data. It covers configuring a mock environment using Docker Compose, including a private registry and a Notary server.
tags:
    - docker-content-trust
    - notary-server
    - image-signing
    - security-sandbox
    - docker-compose
    - container-security
category: tutorial
---

This page explains how to set up and use a sandbox for experimenting with trust. The sandbox allows you to configure and try trust operations locally without impacting your production images.

Before working through this sandbox, you should have read through the [trust overview](https://docs.docker.com/engine/security/trust/).

These instructions assume you are running in Linux or macOS. You can run this sandbox on a local machine or on a virtual machine. You need to have privileges to run docker commands on your local machine or in the VM.

This sandbox requires you to install two Docker tools: Docker Engine &gt;= 1.10.0 and Docker Compose &gt;= 1.6.0. To install the Docker Engine, choose from the [list of supported platforms](https://docs.docker.com/engine/install/). To install Docker Compose, see the [detailed instructions here](https://docs.docker.com/compose/install/).

If you are just using trust out-of-the-box you only need your Docker Engine client and access to the Docker Hub. The sandbox mimics a production trust environment, and sets up these additional components.

ContainerDescriptiontrustsandboxA container with the latest version of Docker Engine and with some preconfigured certificates. This is your sandbox where you can use the `docker` client to test trust operations.Registry serverA local registry service.Notary serverThe service that does all the heavy-lifting of managing trust

This means you run your own content trust (Notary) server and registry. If you work exclusively with the Docker Hub, you would not need these components. They are built into the Docker Hub for you. For the sandbox, however, you build your own entire, mock production environment.

Within the `trustsandbox` container, you interact with your local registry rather than the Docker Hub. This means your everyday image repositories are not used. They are protected while you play.

When you play in the sandbox, you also create root and repository keys. The sandbox is configured to store all the keys and files inside the `trustsandbox` container. Since the keys you create in the sandbox are for play only, destroying the container destroys them as well.

By using a `docker-in-docker` image for the `trustsandbox` container, you also don't pollute your real Docker daemon cache with any images you push and pull. The images are stored in an anonymous volume attached to this container, and can be destroyed after you destroy the container.

In this section, you use Docker Compose to specify how to set up and link together the `trustsandbox` container, the Notary server, and the Registry server.

1. Create a new `trustsandbox` directory and change into it.
2. Create a file called `compose.yaml` with your favorite editor. For example, using vim:
3. Add the following to the new file.
4. Save and close the file.
5. Run the containers on your local system.
   
   The first time you run this, the `docker-in-docker`, Notary server, and registry images are downloaded from Docker Hub.

Now that everything is setup, you can go into your `trustsandbox` container and start testing Docker content trust. From your host machine, obtain a shell in the `trustsandbox` container.

### [Test some trust operations](#test-some-trust-operations)

Now, pull some images from within the `trustsandbox` container.

1. Download a `docker` image to test with.
2. Tag it to be pushed to your sandbox registry:
3. Enable content trust.
4. Identify the trust server.
   
   This step is only necessary because the sandbox is using its own server. Normally, if you are using the Docker Public Hub this step isn't necessary.
5. Pull the test image.
   
   You see an error, because this content doesn't exist on the `notaryserver` yet.
6. Push and sign the trusted image.
   
   Because you are pushing this repository for the first time, Docker creates new root and repository keys and asks you for passphrases with which to encrypt them. If you push again after this, it only asks you for repository passphrase so it can decrypt the key and sign again.
7. Try pulling the image you just pushed:

### [Test with malicious images](#test-with-malicious-images)

What happens when data is corrupted and you try to pull it when trust is enabled? In this section, you go into the `sandboxregistry` and tamper with some data. Then, you try and pull it.

1. Leave the `trustsandbox` shell and container running.
2. Open a new interactive terminal from your host, and obtain a shell into the `sandboxregistry` container.
3. List the layers for the `test/trusttest` image you pushed:
4. Change into the registry storage for one of those layers (this is in a different directory):
5. Add malicious data to one of the `trusttest` layers:
6. Go back to your `trustsandbox` terminal.
7. List the `trusttest` image.
8. Remove the `trusttest:latest` image from your local cache.
   
   Docker does not re-download images that it already has cached, but you want Docker to attempt to download the tampered image from the registry and reject it because it is invalid.
9. Pull the image again. This downloads the image from the registry, because you don't have it cached.
   
   The pull did not complete because the trust system couldn't verify the image.

Now, you have a full Docker content trust sandbox on your local system, feel free to play with it and see how it behaves. If you find any security issues with Docker, feel free to send us an email at [security@docker.com](mailto:security@docker.com).

When you are done, and want to clean up all the services you've started and any anonymous volumes that have been created, just run the following command in the directory where you've created your Docker Compose file: