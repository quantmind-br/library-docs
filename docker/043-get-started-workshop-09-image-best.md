---
title: 'Part 8: Image-building best practices'
url: https://docs.docker.com/get-started/workshop/09_image_best/
source: llms
fetched_at: 2026-01-24T14:08:04.290925158-03:00
rendered_js: false
word_count: 648
summary: This document explains how to optimize Docker image builds by leveraging layer caching and implementing multi-stage builds to improve performance and reduce image size.
tags:
    - docker-images
    - layer-caching
    - multi-stage-builds
    - dockerfile-optimization
    - container-performance
category: guide
---

Using the `docker image history` command, you can see the command that was used to create each layer within an image.

1. Use the `docker image history` command to see the layers in the `getting-started` image you created.
   
   You should get output that looks something like the following.
   
   Each of the lines represents a layer in the image. The display here shows the base at the bottom with the newest layer at the top. Using this, you can also quickly see the size of each layer, helping diagnose large images.
2. You'll notice that several of the lines are truncated. If you add the `--no-trunc` flag, you'll get the full output.

Now that you've seen the layering in action, there's an important lesson to learn to help decrease build times for your container images. Once a layer changes, all downstream layers have to be recreated as well.

Look at the following Dockerfile you created for the getting started app.

Going back to the image history output, you see that each command in the Dockerfile becomes a new layer in the image. You might remember that when you made a change to the image, the yarn dependencies had to be reinstalled. It doesn't make much sense to ship around the same dependencies every time you build.

To fix it, you need to restructure your Dockerfile to help support the caching of the dependencies. For Node-based applications, those dependencies are defined in the `package.json` file. You can copy only that file in first, install the dependencies, and then copy in everything else. Then, you only recreate the yarn dependencies if there was a change to the `package.json`.

1. Update the Dockerfile to copy in the `package.json` first, install dependencies, and then copy everything else in.
2. Build a new image using `docker build`.
   
   You should see output like the following.
3. Now, make a change to the `src/static/index.html` file. For example, change the `<title>` to "The Awesome Todo App".
4. Build the Docker image now using `docker build -t getting-started .` again. This time, your output should look a little different.
   
   First off, you should notice that the build was much faster. And, you'll see that several steps are using previously cached layers. Pushing and pulling this image and updates to it will be much faster as well.

Multi-stage builds are an incredibly powerful tool to help use multiple stages to create an image. There are several advantages for them:

- Separate build-time dependencies from runtime dependencies
- Reduce overall image size by shipping only what your app needs to run

### [Maven/Tomcat example](#maventomcat-example)

When building Java-based applications, you need a JDK to compile the source code to Java bytecode. However, that JDK isn't needed in production. Also, you might be using tools like Maven or Gradle to help build the app. Those also aren't needed in your final image. Multi-stage builds help.

In this example, you use one stage (called `build`) to perform the actual Java build using Maven. In the second stage (starting at `FROM tomcat`), you copy in files from the `build` stage. The final image is only the last stage being created, which can be overridden using the `--target` flag.

### [React example](#react-example)

When building React applications, you need a Node environment to compile the JS code (typically JSX), SASS stylesheets, and more into static HTML, JS, and CSS. If you aren't doing server-side rendering, you don't even need a Node environment for your production build. You can ship the static resources in a static nginx container.

In the previous Dockerfile example, it uses the `node:lts` image to perform the build (maximizing layer caching) and then copies the output into an nginx container.

In this section, you learned a few image building best practices, including layer caching and multi-stage builds.

Related information:

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/)

In the next section, you'll learn about additional resources you can use to continue learning about containers.

[What next](https://docs.docker.com/get-started/workshop/10_what_next/)