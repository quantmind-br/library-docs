---
title: Quickstart
url: https://docs.docker.com/docker-hub/quickstart/
source: llms
fetched_at: 2026-01-24T14:21:28.494761823-03:00
rendered_js: false
word_count: 1141
summary: This guide provides a quickstart for using Docker Hub to find, run, and customize container images, as well as pushing them to shared repositories.
tags:
    - docker-hub
    - container-images
    - docker-desktop
    - docker-cli
    - image-repository
    - docker-push
    - docker-run
category: tutorial
---

## Docker Hub quickstart

Docker Hub provides a vast library of pre-built images and resources, accelerating development workflows and reducing setup time. You can build upon pre-built images from Docker Hub and then use repositories to share and distribute your own images with your team or millions of other developers.

This guide shows you how to find and run a pre-built image. It then walks you through creating a custom image and sharing it through Docker Hub.

- [Download and install Docker](https://docs.docker.com/get-started/get-docker/)
- A verified [Docker](https://app.docker.com/signup) account

You can search for content in Docker Hub itself, in the Docker Desktop Dashboard, or by using the CLI.

To search or browse for content on Docker Hub:

1. Navigate to the [Docker Hub Explore page](https://hub.docker.com/explore).
   
   On the **Explore** page, you can browse by catalog or category, or use the search to quickly find content.
2. Under **Categories**, select **Web servers**.
   
   After the results are displayed, you can further filter the results using the filters on the left side of the page.
3. In the filters, select **Docker Official Image**.
   
   Filtering by Trusted Content ensures that you see only high-quality, secure images curated by Docker and verified publishing partners.
4. In the results, select the **nginx** image.
   
   Selecting the image opens the image's page where you can learn more about how to use the image. On the page, you'll also find the `docker pull` command to pull the image.

<!--THE END-->

1. Open the Docker Desktop Dashboard.
2. Select the **Docker Hub** view.
   
   In the **Docker Hub** view, you can browse by catalog or category, or use the search to quickly find content.
3. Leave the search box empty and then select **Search**.
   
   The search results are shown with additional filters now next to the search box.
4. Select the search filter icon, and then select **Docker Official Image** and **Web Servers**.
5. In the results, select the **nginx** image.

<!--THE END-->

1. Open a terminal window.
   
   > The Docker Desktop Dashboard contains a built-in terminal. At the bottom of the Dashboard, select **&gt;_ Terminal** to open it.
2. In the terminal, run the following command.
   
   Unlike the Docker Hub and Docker Desktop interfaces, you can't browse by category using the `docker search` command. For more details about the command, see [docker search](https://docs.docker.com/reference/cli/docker/search/).

Now that you've found an image, it's time to pull and run it on your device.

You can run images from Docker Hub using the CLI or Docker Desktop Dashboard.

1. In the Docker Desktop Dashboard, select the **nginx** image in the **Docker Hub** view. For more details, see [Step 1: Find an image in Docker Hub's library](#step-1-find-an-image-in-docker-hubs-library).
2. On the **nginx** screen, select **Run**.
   
   If the image doesn't exist on your device, it is automatically pulled from Docker Hub. Pulling the image may take a few seconds or minutes depending on your connection. After the image has been pulled, a window appears in Docker Desktop and you can specify run options.
3. In the **Host port** option, specify `8080`.
4. Select **Run**.
   
   The container logs appear after the container starts.
5. Select the **8080:80** link to open the server, or visit [http://localhost:8080](http://localhost:8080) in your web browser.
6. In the Docker Desktop Dashboard, select the **Stop** button to stop the container.

<!--THE END-->

1. Open a terminal window.
   
   > The Docker Desktop Dashboard contains a built-in terminal. At the bottom of the Dashboard, select **&gt;_ Terminal** to open it.
2. In your terminal, run the following command to pull and run the Nginx image.
   
   The `docker run` command automatically pulls and runs the image without the need to run `docker pull` first. To learn more about the command and its options, see the [`docker run` CLI reference](https://docs.docker.com/reference/cli/docker/container/run/). After running the command, you should see output similar to the following.
3. Visit [http://localhost:8080](http://localhost:8080) to view the default Nginx page and verify that the container is running.
4. In the terminal, press Ctrl+C to stop the container.

You've now run a web server without any set up or configuration. Docker Hub provides instant access to pre-built, ready-to-use container images, letting you quickly pull and run applications without needing to install or configure software manually. With Docker Hub's vast library of images, you can experiment with and deploy applications effortlessly, boosting productivity and making it easy to try out new tools, set up development environments, or build on top of existing software.

You can also extend images from Docker Hub, letting you quickly build and customize your own images to suit specific needs.

1. Create a [Dockerfile](https://docs.docker.com/reference/dockerfile/) to specify your application:
   
   This Dockerfile extends the Nginx image from Docker Hub to create a simple website. With just a few lines, you can easily set up, customize, and share a static website using Docker.
2. Run the following command to build your image. Replace `<YOUR-USERNAME>` with your Docker ID.
   
   This command builds your image and tags it so that Docker understands which repository to push it to in Docker Hub. To learn more about the command and its options, see the [`docker build` CLI reference](https://docs.docker.com/reference/cli/docker/buildx/build/). After running the command, you should see output similar to the following.
3. Run the following command to test your image. Replace `<YOUR-USERNAME>` with your Docker ID.
4. Visit [http://localhost:8080](http://localhost:8080) to view the page. You should see `Hello world from Docker!`.
5. In the terminal, press CTRL+C to stop the container.
6. Sign in to Docker Desktop. You must be signed in before pushing an image to Docker Hub.
7. Run the following command to push your image to Docker Hub. Replace `<YOUR-USERNAME>` with your Docker ID.
   
   > You must be signed in to Docker Hub through Docker Desktop or the command line, and you must also name your images correctly, as per the above steps.
   
   The command pushes the image to Docker Hub and automatically creates the repository if it doesn't exist. To learn more about the command, see the [`docker push` CLI reference](https://docs.docker.com/reference/cli/docker/image/push/). After running the command, you should see output similar to the following.

Now that you've created a repository and pushed your image, it's time to view your repository and explore its options.

You can view your Docker Hub repositories in the Docker Hub or Docker Desktop interface.

1. Go to [Docker Hub](https://hub.docker.com) and sign in.
   
   After signing in, you should be on the **Repositories** page. If not, then go to the [**Repositories**](https://hub.docker.com/repositories/) page.
2. Find the **nginx-custom** repository and select that row.
   
   After selecting the repository, you should see more details and options for your repository.

<!--THE END-->

1. Sign in to Docker Desktop.
2. Select the **Images** view.
3. Select the **Hub repositories** tab.
   
   A list of your Docker Hub repositories appears.
4. Find the **nginx-custom** repository, hover over the row, and then select **View in Hub**.
   
   Docker Hub opens and you are able to view more details about the image.

You've now verified that your repository exists on Docker Hub, and you've discovered more options for it. View the next steps to learn more about some of these options.

Add [repository information](https://docs.docker.com/docker-hub/repos/manage/information/) to help users find and use your image.