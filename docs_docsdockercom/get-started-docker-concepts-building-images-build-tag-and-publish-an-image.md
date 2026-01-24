---
title: Build, tag, and publish an image
url: https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/
source: llms
fetched_at: 2026-01-24T14:02:17.514968148-03:00
rendered_js: false
word_count: 855
summary: This document explains how to build images from a Dockerfile, apply structured naming tags, and publish the results to a container registry.
tags:
    - docker-build
    - image-tagging
    - container-registry
    - docker-hub
    - dockerfile
    - containerization
category: guide
---

In this guide, you will learn the following:

- Building images - the process of building an image based on a `Dockerfile`
- Tagging images - the process of giving an image a name, which also determines where the image can be distributed
- Publishing images - the process to distribute or share the newly created image using a container registry

### [Building images](#building-images)

Most often, images are built using a Dockerfile. The most basic `docker build` command might look like the following:

The final `.` in the command provides the path or URL to the [build context](https://docs.docker.com/build/concepts/context/#what-is-a-build-context). At this location, the builder will find the `Dockerfile` and other referenced files.

When you run a build, the builder pulls the base image, if needed, and then runs the instructions specified in the Dockerfile.

With the previous command, the image will have no name, but the output will provide the ID of the image. As an example, the previous command might produce the following output:

With the previous output, you could start a container by using the referenced image:

That name certainly isn't memorable, which is where tagging becomes useful.

### [Tagging images](#tagging-images)

Tagging images is the method to provide an image with a memorable name. However, there is a structure to the name of an image. A full image name has the following structure:

- `HOST`: The optional registry hostname where the image is located. If no host is specified, Docker's public registry at `docker.io` is used by default.
- `PORT_NUMBER`: The registry port number if a hostname is provided
- `PATH`: The path of the image, consisting of slash-separated components. For Docker Hub, the format follows `[NAMESPACE/]REPOSITORY`, where namespace is either a user's or organization's name. If no namespace is specified, `library` is used, which is the namespace for Docker Official Images.
- `TAG`: A custom, human-readable identifier that's typically used to identify different versions or variants of an image. If no tag is specified, `latest` is used by default.

Some examples of image names include:

- `nginx`, equivalent to `docker.io/library/nginx:latest`: this pulls an image from the `docker.io` registry, the `library` namespace, the `nginx` image repository, and the `latest` tag.
- `docker/welcome-to-docker`, equivalent to `docker.io/docker/welcome-to-docker:latest`: this pulls an image from the `docker.io` registry, the `docker` namespace, the `welcome-to-docker` image repository, and the `latest` tag
- `ghcr.io/dockersamples/example-voting-app-vote:pr-311`: this pulls an image from the GitHub Container Registry, the `dockersamples` namespace, the `example-voting-app-vote` image repository, and the `pr-311` tag

To tag an image during a build, add the `-t` or `--tag` flag:

If you've already built an image, you can add another tag to the image by using the [`docker image tag`](https://docs.docker.com/engine/reference/commandline/image_tag/) command:

### [Publishing images](#publishing-images)

Once you have an image built and tagged, you're ready to push it to a registry. To do so, use the [`docker push`](https://docs.docker.com/engine/reference/commandline/image_push/) command:

Within a few seconds, all of the layers for your image will be pushed to the registry.

> **Requiring authentication**
> 
> Before you're able to push an image to a repository, you will need to be authenticated. To do so, simply use the [docker login](https://docs.docker.com/engine/reference/commandline/login/) command.

In this hands-on guide, you will build a simple image using a provided Dockerfile and push it to Docker Hub.

### [Set up](#set-up)

1. Get the sample application.
   
   If you have Git, you can clone the repository for the sample application. Otherwise, you can download the sample application. Choose one of the following options.
   
   Use the following command in a terminal to clone the sample application repository.
2. [Download and install](https://www.docker.com/products/docker-desktop/) Docker Desktop.
3. If you don't have a Docker account yet, [create one now](https://hub.docker.com/). Once you've done that, sign in to Docker Desktop using that account.

### [Build an image](#build-an-image)

Now that you have a repository on Docker Hub, it's time for you to build an image and push it to the repository.

1. Using a terminal in the root of the sample app repository, run the following command. Replace `YOUR_DOCKER_USERNAME` with your Docker Hub username:
   
   As an example, if your username is `mobywhale`, you would run the command:
2. Once the build has completed, you can view the image by using the following command:
   
   The command will produce output similar to the following:
3. You can actually view the history (or how the image was created) by using the [docker image history](https://docs.docker.com/reference/cli/docker/image/history/) command:
   
   You'll then see output similar to the following:
   
   This output shows the layers of the image, highlighting the layers you added and those that were inherited from your base image.

### [Push the image](#push-the-image)

Now that you have an image built, it's time to push the image to a registry.

1. Push the image using the [docker push](https://docs.docker.com/reference/cli/docker/image/push/) command:
   
   If you receive a `requested access to the resource is denied`, make sure you are both logged in and that your Docker username is correct in the image tag.
   
   After a moment, your image should be pushed to Docker Hub.

To learn more about building, tagging, and publishing images, visit the following resources:

- [What is a build context?](https://docs.docker.com/build/concepts/context/#what-is-a-build-context)
- [docker build reference](https://docs.docker.com/engine/reference/commandline/image_build/)
- [docker image tag reference](https://docs.docker.com/engine/reference/commandline/image_tag/)
- [docker push reference](https://docs.docker.com/engine/reference/commandline/image_push/)
- [What is a registry?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/)

Now that you have learned about building and publishing images, it's time to learn how to speed up the build process using the Docker build cache.

[Using the build cache](https://docs.docker.com/get-started/docker-concepts/building-images/using-the-build-cache/)