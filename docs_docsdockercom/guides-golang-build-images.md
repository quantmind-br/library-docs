---
title: Build images
url: https://docs.docker.com/guides/golang/build-images/
source: llms
fetched_at: 2026-01-24T14:10:20.483993668-03:00
rendered_js: false
word_count: 1982
summary: This tutorial explains how to containerize a Go application by writing a Dockerfile and building a container image from scratch.
tags:
    - docker
    - golang
    - dockerfile
    - containerization
    - image-building
    - go-development
category: tutorial
---

## Build your Go image

In this section you're going to build a container image. The image includes everything you need to run your application – the compiled application binary file, the runtime, the libraries, and all other resources required by your application.

To complete this tutorial, you need the following:

- Docker running locally. Follow the [instructions to download and install Docker](https://docs.docker.com/desktop/).
- An IDE or a text editor to edit files. [Visual Studio Code](https://code.visualstudio.com/) is a free and popular choice but you can use anything you feel comfortable with.
- A Git client. This guide uses a command-line based `git` client, but you are free to use whatever works for you.
- A command-line terminal application. The examples shown in this module are from the Linux shell, but they should work in PowerShell, Windows Command Prompt, or OS X Terminal with minimal, if any, modifications.

The example application is a caricature of a microservice. It is purposefully trivial to keep focus on learning the basics of containerization for Go applications.

The application offers two HTTP endpoints:

- It responds with a string containing a heart symbol (`<3`) to requests to `/`.
- It responds with `{"Status" : "OK"}` JSON to a request to `/health`.

It responds with HTTP error 404 to any other request.

The application listens on a TCP port defined by the value of environment variable `PORT`. The default value is `8080`.

The application is stateless.

The complete source code for the application is on GitHub: [github.com/docker/docker-gs-ping](https://github.com/docker/docker-gs-ping). You are encouraged to fork it and experiment with it as much as you like.

To continue, clone the application repository to your local machine:

The application's `main.go` file is straightforward, if you are familiar with Go:

To build a container image with Docker, a `Dockerfile` with build instructions is required.

Begin your `Dockerfile` with the (optional) parser directive line that instructs BuildKit to interpret your file according to the grammar rules for the specified version of the syntax.

You then tell Docker what base image you would like to use for your application:

Docker images can be inherited from other images. Therefore, instead of creating your own base image from scratch, you can use the official Go image that already has all necessary tools and libraries to compile and run a Go application.

> If you are curious about creating your own base images, you can check out the following section of this guide: [creating base images](https://docs.docker.com/build/building/base-images/#create-a-base-image). Note, however, that this isn't necessary to continue with your task at hand.

Now that you have defined the base image for your upcoming container image, you can begin building on top of it.

To make things easier when running the rest of your commands, create a directory inside the image that you're building. This also instructs Docker to use this directory as the default destination for all subsequent commands. This way you don't have to type out full file paths in the `Dockerfile`, the relative paths will be based on this directory.

Usually the very first thing you do once you’ve downloaded a project written in Go is to install the modules necessary to compile it. Note, that the base image has the toolchain already, but your source code isn't in it yet.

So before you can run `go mod download` inside your image, you need to get your `go.mod` and `go.sum` files copied into it. Use the `COPY` command to do this.

In its simplest form, the `COPY` command takes two parameters. The first parameter tells Docker what files you want to copy into the image. The last parameter tells Docker where you want that file to be copied to.

Copy the `go.mod` and `go.sum` file into your project directory `/app` which, owing to your use of `WORKDIR`, is the current directory (`./`) inside the image. Unlike some modern shells that appear to be indifferent to the use of trailing slash (`/`), and can figure out what the user meant (most of the time), Docker's `COPY` command is quite sensitive in its interpretation of the trailing slash.

> If you'd like to familiarize yourself with the trailing slash treatment by the `COPY` command, see [Dockerfile reference](https://docs.docker.com/reference/dockerfile/#copy). This trailing slash can cause issues in more ways than you can imagine.

Now that you have the module files inside the Docker image that you are building, you can use the `RUN` command to run the command `go mod download` there as well. This works exactly the same as if you were running `go` locally on your machine, but this time these Go modules will be installed into a directory inside the image.

At this point, you have a Go toolchain version 1.19.x and all your Go dependencies installed inside the image.

The next thing you need to do is to copy your source code into the image. You’ll use the `COPY` command just like you did with your module files before.

This `COPY` command uses a wildcard to copy all files with `.go` extension located in the current directory on the host (the directory where the `Dockerfile` is located) into the current directory inside the image.

Now, to compile your application, use the familiar `RUN` command:

This should be familiar. The result of that command will be a static application binary named `docker-gs-ping` and located in the root of the filesystem of the image that you are building. You could have put the binary into any other place you desire inside that image, the root directory has no special meaning in this regard. It's just convenient to use it to keep the file paths short for improved readability.

Now, all that is left to do is to tell Docker what command to run when your image is used to start a container.

You do this with the `CMD` command:

Here's the complete `Dockerfile`:

The `Dockerfile` may also contain comments. They always begin with a `#` symbol, and must be at the beginning of a line. Comments are there for your convenience to allow documenting your `Dockerfile`.

There is also a concept of Dockerfile directives, such as the `syntax` directive you added. The directives must always be at the very top of the `Dockerfile`, so when adding comments, make sure that the comments follow after any directives that you may have used:

Now that you've created your `Dockerfile`, build an image from it. The `docker build` command creates Docker images from the `Dockerfile` and a context. A build context is the set of files located in the specified path or URL. The Docker build process can access any of the files located in the context.

The build command optionally takes a `--tag` flag. This flag is used to label the image with a string value, which is easy for humans to read and recognize. If you don't pass a `--tag`, Docker will use `latest` as the default value.

Build your first Docker image.

The build process will print some diagnostic messages as it goes through the build steps. The following is just an example of what these messages may look like.

Your exact output will vary, but provided there aren't any errors, you should see the word `FINISHED` in the first line of output. This means Docker has successfully built your image named `docker-gs-ping`.

To see the list of images you have on your local machine, you have two options. One is to use the CLI and the other is to use [Docker Desktop](https://docs.docker.com/desktop/). Since you're currently working in the terminal, take a look at listing images with the CLI.

To list images, run the `docker image ls`command (or the `docker images` shorthand):

Your exact output may vary, but you should see the `docker-gs-ping` image with the `latest` tag. Because you didn't specify a custom tag when you built your image, Docker assumed that the tag would be `latest`, which is a special value.

An image name is made up of slash-separated name components. Name components may contain lowercase letters, digits, and separators. A separator is defined as a period, one or two underscores, or one or more dashes. A name component may not start or end with a separator.

An image is made up of a manifest and a list of layers. In simple terms, a tag points to a combination of these artifacts. You can have multiple tags for the image and, in fact, most images have multiple tags. Create a second tag for the image you built and take a look at its layers.

Use the `docker image tag` (or `docker tag` shorthand) command to create a new tag for your image. This command takes two arguments; the first argument is the source image, and the second is the new tag to create. The following command creates a new `docker-gs-ping:v1.0` tag for the `docker-gs-ping:latest` you built:

The Docker `tag` command creates a new tag for the image. It doesn't create a new image. The tag points to the same image and is just another way to reference the image.

Now run the `docker image ls` command again to see the updated list of local images:

You can see that you have two images that start with `docker-gs-ping`. You know they're the same image because if you look at the `IMAGE ID` column, you can see that the values are the same for the two images. This value is a unique identifier Docker uses internally to identify the image.

Remove the tag that you just created. To do this, you’ll use the `docker image rm` command, or the shorthand `docker rmi` (which stands for "remove image"):

Notice that the response from Docker tells you that the image hasn't been removed but only untagged.

Verify this by running the following command:

You will see that the tag `v1.0` is no longer in the list of images kept by your Docker instance.

The tag `v1.0` has been removed but you still have the `docker-gs-ping:latest` tag available on your machine, so the image is there.

You may have noticed that your `docker-gs-ping` image weighs in at over a gigabyte, which is a lot for a tiny compiled Go application. You may also be wondering what happened to the full suite of Go tools, including the compiler, after you had built your image.

The answer is that the full toolchain is still there, in the container image. Not only this is inconvenient because of the large file size, but it may also present a security risk when the container is deployed.

These two issues can be solved by using [multi-stage builds](https://docs.docker.com/build/building/multi-stage/).

In a nutshell, a multi-stage build can carry over the artifacts from one build stage into another, and every build stage can be instantiated from a different base image.

Thus, in the following example, you are going to use a full-scale official Go image to build your application. Then you'll copy the application binary into another image whose base is very lean and doesn't include the Go toolchain or other optional components.

The `Dockerfile.multistage` in the sample application's repository has the following content:

Since you have two Dockerfiles now, you have to tell Docker what Dockerfile you'd like to use to build the image. Tag the new image with `multistage`. This tag (like any other, apart from `latest`) has no special meaning for Docker, it's just something you chose.

Comparing the sizes of `docker-gs-ping:multistage` and `docker-gs-ping:latest` you see a few orders-of-magnitude difference.

This is so because the ["distroless"](https://github.com/GoogleContainerTools/distroless) base image that you have used in the second stage of the build is very barebones and is designed for lean deployments of static binaries.

There's much more to multi-stage builds, including the possibility of multi-architecture builds, so feel free to check out [multi-stage builds](https://docs.docker.com/build/building/multi-stage/). This is, however, not essential for your progress here.

In this module, you met your example application and built and container image for it.

In the next module, you’ll take a look at how to run your image as a container.