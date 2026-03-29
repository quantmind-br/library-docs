---
title: Test your deployment
url: https://docs.docker.com/guides/angular/deploy/
source: llms
fetched_at: 2026-01-24T14:08:25.538596542-03:00
rendered_js: false
word_count: 644
summary: This guide provides step-by-step instructions for deploying and testing a containerized Angular application on a local Kubernetes cluster using Docker Desktop.
tags:
    - angular
    - kubernetes
    - docker-desktop
    - kubectl
    - containerization
    - local-deployment
category: tutorial
---

## Test your Angular deployment

Before you begin, make sure you’ve completed the following:

- Complete all the previous sections of this guide, starting with [Containerize Angular application](https://docs.docker.com/guides/angular/containerize/).
- [Enable Kubernetes](https://docs.docker.com/desktop/use-desktop/kubernetes/#enable-kubernetes) in Docker Desktop.

> **New to Kubernetes?**  
> Visit the [Kubernetes basics tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/) to get familiar with how clusters, pods, deployments, and services work.

* * *

This section guides you through deploying your containerized Angular application locally using [Docker Desktop’s built-in Kubernetes](https://docs.docker.com/desktop/kubernetes/). Running your app in a local Kubernetes cluster closely simulates a real production environment, enabling you to test, validate, and debug your workloads with confidence before promoting them to staging or production.

* * *

Follow these steps to define your deployment configuration:

1. In the root of your project, create a new file named: angular-sample-kubernetes.yaml
2. Open the file in your IDE or preferred text editor.
3. Add the following configuration, and be sure to replace `{DOCKER_USERNAME}` and `{DOCKERHUB_PROJECT_NAME}` with your actual Docker Hub username and repository name from the previous [Automate your builds with GitHub Actions](https://docs.docker.com/guides/angular/configure-github-actions/).

This manifest defines two key Kubernetes resources, separated by `---`:

- Deployment Deploys a single replica of your Angular application inside a pod. The pod uses the Docker image built and pushed by your GitHub Actions CI/CD workflow  
  (refer to [Automate your builds with GitHub Actions](https://docs.docker.com/guides/angular/configure-github-actions/)).  
  The container listens on port `8080`, which is typically used by [Nginx](https://nginx.org/en/docs/) to serve your production Angular app.
- Service (NodePort) Exposes the deployed pod to your local machine.  
  It forwards traffic from port `30001` on your host to port `8080` inside the container.  
  This lets you access the application in your browser at [http://localhost:30001](http://localhost:30001).

> To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

* * *

Follow these steps to deploy your containerized Angular app into a local Kubernetes cluster and verify that it’s running correctly.

### [Step 1. Apply the Kubernetes configuration](#step-1-apply-the-kubernetes-configuration)

In your terminal, navigate to the directory where your `angular-sample-kubernetes.yaml` file is located, then deploy the resources using:

If everything is configured properly, you’ll see confirmation that both the Deployment and the Service were created:

This confirms that both the Deployment and the Service were successfully created and are now running inside your local cluster.

### [Step 2. Check the Deployment status](#step-2-check-the-deployment-status)

Run the following command to check the status of your deployment:

You should see output similar to the following:

This confirms that your pod is up and running with one replica available.

### [Step 3. Verify the Service exposure](#step-3-verify-the-service-exposure)

Check if the NodePort service is exposing your app to your local machine:

You should see something like:

This output confirms that your app is available via NodePort on port 30001.

### [Step 4. Access your app in the browser](#step-4-access-your-app-in-the-browser)

Open your browser and navigate to [http://localhost:30001](http://localhost:30001).

You should see your production-ready Angular Sample application running — served by your local Kubernetes cluster.

### [Step 5. Clean up Kubernetes resources](#step-5-clean-up-kubernetes-resources)

Once you're done testing, you can delete the deployment and service using:

Expected output:

This ensures your cluster stays clean and ready for the next deployment.

* * *

In this section, you learned how to deploy your Angular application to a local Kubernetes cluster using Docker Desktop. This setup allows you to test and debug your containerized app in a production-like environment before deploying it to the cloud.

What you accomplished:

- Created a Kubernetes Deployment and NodePort Service for your Angular app
- Used `kubectl apply` to deploy the application locally
- Verified the app was running and accessible at `http://localhost:30001`
- Cleaned up your Kubernetes resources after testing

* * *

Explore official references and best practices to sharpen your Kubernetes deployment workflow:

- [Kubernetes documentation](https://kubernetes.io/docs/home/) – Learn about core concepts, workloads, services, and more.
- [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/use-desktop/kubernetes/) – Use Docker Desktop’s built-in Kubernetes support for local testing and development.
- [`kubectl` CLI reference](https://kubernetes.io/docs/reference/kubectl/) – Manage Kubernetes clusters from the command line.
- [Kubernetes Deployment resource](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) – Understand how to manage and scale applications using Deployments.
- [Kubernetes Service resource](https://kubernetes.io/docs/concepts/services-networking/service/) – Learn how to expose your application to internal and external traffic.