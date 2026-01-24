---
title: Face detection with TensorFlow.js
url: https://docs.docker.com/guides/tensorflowjs/
source: llms
fetched_at: 2026-01-24T14:12:03.955291126-03:00
rendered_js: false
word_count: 1732
summary: This guide explains how to containerize a TensorFlow.js face detection application using Docker, covering image building, container deployment, and real-time development.
tags:
    - tensorflow-js
    - docker
    - face-detection
    - containerization
    - machine-learning
    - web-development
category: guide
---

This guide introduces the seamless integration of TensorFlow.js with Docker to perform face detection. In this guide, you'll explore how to:

- Run a containerized TensorFlow.js application using Docker.
- Implement face detection in a web application with TensorFlow.js.
- Construct a Dockerfile for a TensorFlow.js web application.
- Use Docker Compose for real-time application development and updates.
- Share your Docker image on Docker Hub to facilitate deployment and extend reach.

> **Acknowledgment**
> 
> Docker would like to thank [Harsh Manvar](https://github.com/harsh4870) for his contribution to this guide.

- You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
- You have a [Git client](https://git-scm.com/downloads). The examples in this guide use a command-line based Git client, but you can use any client.

[TensorFlow.js](https://www.tensorflow.org/js) is an open-source JavaScript library for machine learning that enables you to train and deploy ML models in the browser or on Node.js. It supports creating new models from scratch or using pre-trained models, facilitating a wide range of ML applications directly in web environments. TensorFlow.js offers efficient computation, making sophisticated ML tasks accessible to web developers without deep ML expertise.

- Environment consistency and simplified deployment: Docker packages TensorFlow.js applications and their dependencies into containers, ensuring consistent runs across all environments and simplifying deployment.
- Efficient development and easy scaling: Docker enhances development efficiency with features like hot reloading and facilitates easy scaling of - TensorFlow.js applications using orchestration tools like Kubernetes.
- Isolation and enhanced security: Docker isolates TensorFlow.js applications in secure environments, minimizing conflicts and security vulnerabilities while running applications with limited permissions.

In a terminal, clone the sample application using the following command.

After cloning the application, you'll notice the application has a `Dockerfile`. This Dockerfile lets you build and run the application locally with nothing more than Docker.

Before you run the application as a container, you must build it into an image. Run the following command inside the `TensorJS-Face-Detection` directory to build an image named `face-detection-tensorjs`.

The command builds the application into an image. Depending on your network connection, it can take several minutes to download the necessary components the first time you run the command.

To run the image as a container, run the following command in a terminal.

The command runs the container and maps port 80 in the container to port 80 on your system.

Once the application is running, open a web browser and access the application at [http://localhost:80](http://localhost:80). You may need to grant access to your webcam for the application.

In the web application, you can change the backend to use one of the following:

- WASM
- WebGL
- CPU

To stop the application, press `ctrl`+`c` in the terminal.

The sample application performs real-time face detection using [MediaPipe](https://developers.google.com/mediapipe/), a comprehensive framework for building multimodal machine learning pipelines. It's specifically using the BlazeFace model, a lightweight model for detecting faces in images.

In the context of TensorFlow.js or similar web-based machine learning frameworks, the WASM, WebGL, and CPU backends can be used to execute operations. Each of these backends utilizes different resources and technologies available in modern browsers and has its strengths and limitations. The following sections are a brief breakdown of the different backends.

### [WASM](#wasm)

WebAssembly (WASM) is a low-level, assembly-like language with a compact binary format that runs at near-native speed in web browsers. It allows code written in languages like C/C++ to be compiled into a binary that can be executed in the browser.

It's a good choice when high performance is required, and either the WebGL backend is not supported or you want consistent performance across all devices without relying on the GPU.

### [WebGL](#webgl)

WebGL is a browser API that allows for GPU-accelerated usage of physics and image processing and effects as part of the web page canvas.

WebGL is well-suited for operations that are parallelizable and can significantly benefit from GPU acceleration, such as matrix multiplications and convolutions commonly found in deep learning models.

### [CPU](#cpu)

The CPU backend uses pure JavaScript execution, utilizing the device's central processing unit (CPU). This backend is the most universally compatible and serves as a fallback when neither WebGL nor WASM backends are available or suitable.

Explore the purpose of each file and their contents in the following sections.

### [The index.html file](#the-indexhtml-file)

The `index.html` file serves as the frontend for the web application that utilizes TensorFlow.js for real-time face detection from the webcam video feed. It incorporates several technologies and libraries to facilitate machine learning directly in the browser. It uses several TensorFlow.js libraries, including:

- tfjs-core and tfjs-converter for core TensorFlow.js functionality and model conversion.
- tfjs-backend-webgl, tfjs-backend-cpu, and the tf-backend-wasm script for different computational backend options that TensorFlow.js can use for processing. These backends allow the application to perform machine learning tasks efficiently by leveraging the user's hardware capabilities.
- The BlazeFace library, a TensorFlow model for face detection.

It also uses the following additional libraries:

- dat.GUI for creating a graphical interface to interact with the application's settings in real-time, such as switching between TensorFlow.js backends.
- Stats.min.js for displaying performance metrics (like FPS) to monitor the application's efficiency during operation.

### [The index.js file](#the-indexjs-file)

The `index.js` file conducts the facial detection logic. It demonstrates several advanced concepts in web development and machine learning integration. Here's a breakdown of some of its key components and functionalities:

- Stats.js: The script starts by creating a Stats instance to monitor and display the frame rate (FPS) of the application in real time. This is helpful for performance analysis, especially when testing the impact of different TensorFlow.js backends on the application's speed.
- TensorFlow.js: The application allows users to switch between different computation backends (wasm, webgl, and cpu) for TensorFlow.js through a graphical interface provided by dat.GUI. Changing the backend can affect performance and compatibility depending on the device and browser. The addFlagLabels function dynamically checks and displays whether SIMD (Single Instruction, Multiple Data) and multithreading are supported, which are relevant for performance optimization in the wasm backend.
- setupCamera function: Initializes the user's webcam using the MediaDevices Web API. It configures the video stream to not include audio and to use the front-facing camera (facingMode: 'user'). Once the video metadata is loaded, it resolves a promise with the video element, which is then used for face detection.
- BlazeFace: The core of this application is the renderPrediction function, which performs real-time face detection using the BlazeFace model, a lightweight model for detecting faces in images. The function calls model.estimateFaces on each animation frame to detect faces from the video feed. For each detected face, it draws a red rectangle around the face and blue dots for facial landmarks on a canvas overlaying the video.

### [The tf-backend-wasm.js file](#the-tf-backend-wasmjs-file)

The `tf-backend-wasm.js` file is part of the [TensorFlow.js library](https://github.com/tensorflow/tfjs/tree/master/tfjs-backend-wasm). It contains initialization logic for the TensorFlow.js WASM backend, some utilities for interacting with the WASM binaries, and functions to set custom paths for the WASM binaries.

### [The tfjs-backend-wasm-simd.wasm file](#the-tfjs-backend-wasm-simdwasm-file)

The `tfjs-backend-wasm-simd.wasm` file is part of the [TensorFlow.js library](https://github.com/tensorflow/tfjs/tree/master/tfjs-backend-wasm). It's a WASM binary that's used for the WebAssembly backend, specifically optimized to utilize SIMD (Single Instruction, Multiple Data) instructions.

In a Docker-based project, the Dockerfile serves as the foundational asset for building your application's environment.

A Dockerfile is a text file that instructs Docker how to create an image of your application's environment. An image contains everything you want and need when running application, such as files, packages, and tools.

The following is the Dockerfile for this project.

This Dockerfile defines an image that serves static content using Nginx from an Alpine Linux base image.

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, networks, and volumes. In this case, the application isn't a multi-container application, but Docker Compose has other useful features for development, like [Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

The sample application doesn't have a Compose file yet. To create a Compose file, in the `TensorJS-Face-Detection` directory, create a text file named `compose.yaml` and then add the following contents.

This Compose file defines a service that is built using the Dockerfile in the same directory. It maps port 80 on the host to port 80 in the container. It also has a `develop` subsection with the `watch` attribute that defines a list of rules that control automatic service updates based on local file changes. For more details about the Compose instructions, see the [Compose file reference](https://docs.docker.com/reference/compose-file/).

Save the changes to your `compose.yaml` file and then run the following command to run the application.

Once the application is running, open a web browser and access the application at [http://localhost:80](http://localhost:80). You may need to grant access to your webcam for the application.

Now you can make changes to the source code and see the changes automatically reflected in the container without having to rebuild and rerun the container.

Open the `index.js` file and update the landmark points to be green instead of blue on line 83.

Save the changes to the `index.js` file and then refresh the browser page. The landmark points should now appear green.

To stop the application, press `ctrl`+`c` in the terminal.

Publishing your Docker image on Docker Hub streamlines deployment processes for others, enabling seamless integration into diverse projects. It also promotes the adoption of your containerized solutions, broadening their impact across the developer ecosystem. To share your image:

1. [Sign up](https://www.docker.com/pricing?utm_source=docker&utm_medium=webreferral&utm_campaign=docs_driven_upgrade) or sign in to [Docker Hub](https://hub.docker.com).
2. Rebuild your image to include the changes to your application. This time, prefix the image name with your Docker ID. Docker uses the name to determine which repository to push it to. Open a terminal and run the following command in the `TensorJS-Face-Detection` directory. Replace `YOUR-USER-NAME` with your Docker ID.
3. Run the following `docker push` command to push the image to Docker Hub. Replace `YOUR-USER-NAME` with your Docker ID.
4. Verify that you pushed the image to Docker Hub.
   
   1. Go to [Docker Hub](https://hub.docker.com).
   2. Select **My Hub** &gt; **Repositories**.
   3. View the **Last pushed** time for your repository.

Other users can now download and run your image using the `docker run` command. They need to replace `YOUR-USER-NAME` with your Docker ID.

This guide demonstrated leveraging TensorFlow.js and Docker for face detection in web applications. It highlighted the ease of running containerized TensorFlow.js applications, and developing with Docker Compose for real-time code changes. Additionally, it covered how sharing your Docker image on Docker Hub can streamline deployment for others, enhancing the application's reach within the developer community.

Related information:

- [TensorFlow.js website](https://www.tensorflow.org/js)
- [MediaPipe website](https://developers.google.com/mediapipe/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Docker CLI reference](https://docs.docker.com/reference/cli/docker/)
- [Docker Blog: Accelerating Machine Learning with TensorFlow.js](https://www.docker.com/blog/accelerating-machine-learning-with-tensorflow-js-using-pretrained-models-and-docker/)