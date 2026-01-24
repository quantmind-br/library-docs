---
title: Build images
url: https://docs.docker.com/guides/rust/build-images/
source: llms
fetched_at: 2026-01-24T14:11:53.877532276-03:00
rendered_js: false
word_count: 788
summary: This guide explains how to containerize a Rust application using Docker by initializing project files, building images, and managing image tags.
tags:
    - rust
    - docker
    - docker-init
    - docker-build
    - image-tagging
    - containerization
category: guide
---

## Build your Rust image

- You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
- You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

This guide walks you through building your first Rust image. An image includes everything needed to run an application - the code or binary, runtime, dependencies, and any other file system objects required.

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

Now that you have an application, you can use `docker init` to create a Dockerfile for it. Inside the `docker-rust-hello` directory, run the `docker init` command. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. Refer to the following example to answer the prompts from `docker init` and use the same answers for your prompts.

You should now have the following new files in your `docker-rust-hello` directory:

- Dockerfile
- .dockerignore
- compose.yaml
- README.Docker.md

For building an image, only the Dockerfile is necessary. Open the Dockerfile in your favorite IDE or text editor and see what it contains. To learn more about Dockerfiles, see the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/).

When you run `docker init`, it also creates a [`.dockerignore`](https://docs.docker.com/reference/dockerfile/#dockerignore-file) file. Use the `.dockerignore` file to specify patterns and paths that you don't want copied into the image in order to keep the image as small as possible. Open up the `.dockerignore` file in your favorite IDE or text editor and see what's inside already.

Now that you’ve created the Dockerfile, you can build the image. To do this, use the `docker build` command. The `docker build` command builds Docker images from a Dockerfile and a context. A build's context is the set of files located in the specified PATH or URL. The Docker build process can access any of the files located in this context.

The build command optionally takes a `--tag` flag. The tag sets the name of the image and an optional tag in the format `name:tag`. If you don't pass a tag, Docker uses "latest" as its default tag.

Build the Docker image.

You should see output like the following.

To see a list of images you have on your local machine, you have two options. One is to use the Docker CLI and the other is to use [Docker Desktop](https://docs.docker.com/desktop/use-desktop/images/). As you are working in the terminal already, take a look at listing images using the CLI.

To list images, run the `docker images` command.

You should see at least one image listed, including the image you just built `docker-rust-image:latest`.

As mentioned earlier, an image name is made up of slash-separated name components. Name components may contain lowercase letters, digits, and separators. A separator can include a period, one or two underscores, or one or more dashes. A name component may not start or end with a separator.

An image is made up of a manifest and a list of layers. Don't worry too much about manifests and layers at this point other than a "tag" points to a combination of these artifacts. You can have multiple tags for an image. Create a second tag for the image you built and take a look at its layers.

To create a new tag for the image you built, run the following command.

The `docker tag` command creates a new tag for an image. It doesn't create a new image. The tag points to the same image and is just another way to reference the image.

Now, run the `docker images` command to see a list of the local images.

You can see that two images start with `docker-rust-image`. You know they're the same image because if you take a look at the `IMAGE ID` column, you can see that the values are the same for the two images.

Remove the tag you just created. To do this, use the `rmi` command. The `rmi` command stands for remove image.

Note that the response from Docker tells you that Docker didn't remove the image, but only "untagged" it. You can check this by running the `docker images` command.

Docker removed the image tagged with `:v1.0.0`, but the `docker-rust-image:latest` tag is available on your machine.

This section showed how you can use `docker init` to create a Dockerfile and .dockerignore file for a Rust application. It then showed you how to build an image. And finally, it showed you how to tag an image and list all images.

Related information:

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore file](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [docker init CLI reference](https://docs.docker.com/reference/cli/docker/init/)
- [docker build CLI reference](https://docs.docker.com/reference/cli/docker/buildx/build/)

In the next section learn how to run your image as a container.