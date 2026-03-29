---
title: Deploy your app
url: https://docs.docker.com/guides/nodejs/deploy/
source: llms
fetched_at: 2026-01-24T14:10:55.588582346-03:00
rendered_js: false
word_count: 634
summary: This tutorial explains how to deploy a containerized Node.js application and PostgreSQL database to Kubernetes using Docker Desktop, covering security, auto-scaling, and high availability.
tags:
    - nodejs
    - kubernetes
    - docker-desktop
    - deployment
    - postgresql
    - containerization
    - devops
category: tutorial
---

## Deploy your Node.js application

- Complete all the previous sections of this guide, starting with [Containerize a Node.js application](https://docs.docker.com/guides/nodejs/containerize/).
- [Turn on Kubernetes](https://docs.docker.com/desktop/use-desktop/kubernetes/#enable-kubernetes) in Docker Desktop.

In this section, you'll learn how to deploy your containerized Node.js application to Kubernetes using Docker Desktop. This deployment uses production-ready configurations including security hardening, auto-scaling, persistent storage, and high availability features.

You'll deploy a complete stack including:

- Node.js Todo application with 3 replicas.
- PostgreSQL database with persistent storage.
- Auto-scaling based on CPU and memory usage.
- Ingress configuration for external access.
- Security settings.

Create a new file called `nodejs-sample-kubernetes.yaml` in your project root:

Before deploying, you need to customize the deployment file for your environment:

1. **Image reference**: Replace `your-username` with your GitHub username or Docker Hub username:
2. **Domain name**: Replace `yourdomain.com` with your actual domain in two places:
3. **Database password** (optional): The default password is already base64 encoded. To change it:
   
   Then update the Secret:
4. **Storage class**: Adjust based on your cluster (current: `standard`)

The deployment file creates a complete application stack with multiple components working together.

### [Architecture](#architecture)

The deployment includes:

- **Node.js application**: Runs 3 replicas of your containerized Todo app
- **PostgreSQL database**: Single instance with 10Gi of persistent storage
- **Services**: Kubernetes services handle load balancing across application replicas
- **Ingress**: External access through an ingress controller with SSL/TLS support

### [Security](#security)

The deployment uses several security features:

- Containers run as a non-root user (UID 1001)
- Read-only root filesystem prevents unauthorized writes
- Linux capabilities are dropped to minimize attack surface
- Sensitive data like database passwords are stored in Kubernetes secrets

### [High availability](#high-availability)

To keep your application running reliably:

- Three application replicas ensure service continues if one pod fails
- Pod disruption budget maintains at least one available pod during updates
- Rolling updates allow zero-downtime deployments
- Health checks on the `/health` endpoint ensure only healthy pods receive traffic

### [Auto-scaling](#auto-scaling)

The Horizontal Pod Autoscaler scales your application based on resource usage:

- Scales between 1 and 5 replicas automatically
- Triggers scaling when CPU usage exceeds 70%
- Triggers scaling when memory usage exceeds 80%
- Resource limits: 256Mi-512Mi memory, 250m-500m CPU per pod

### [Data persistence](#data-persistence)

PostgreSQL data is stored persistently:

- 10Gi persistent volume stores database files
- Database initializes automatically on first startup
- Data persists across pod restarts and updates

### [Step 1: Deploy to Kubernetes](#step-1-deploy-to-kubernetes)

Deploy your application to the local Kubernetes cluster:

You should see output confirming all resources were created:

### [Step 2: Verify the deployment](#step-2-verify-the-deployment)

Check that your deployments are running:

Expected output:

Verify your services are created:

Expected output:

Check that persistent storage is working:

Expected output:

### [Step 3: Access your application](#step-3-access-your-application)

For local testing, use port forwarding to access your application:

Open your browser and visit [http://localhost:8080](http://localhost:8080) to see your Todo application running in Kubernetes.

### [Step 4: Test the deployment](#step-4-test-the-deployment)

Test that your application is working correctly:

1. **Add some todos** through the web interface
2. **Check application pods**:
3. **View application logs**:
4. **Check database connectivity**:
5. **Monitor auto-scaling**:

### [Step 5: Clean up](#step-5-clean-up)

When you're done testing, remove the deployment:

You've deployed your containerized Node.js application to Kubernetes. You learned how to:

- Create a comprehensive Kubernetes deployment file with security hardening
- Deploy a multi-tier application (Node.js + PostgreSQL) with persistent storage
- Configure auto-scaling, health checks, and high availability features
- Test and monitor your deployment locally using Docker Desktop's Kubernetes

Your application is now running in a production-like environment with enterprise-grade features including security contexts, resource management, and automatic scaling.

* * *

Explore official references and best practices to sharpen your Kubernetes deployment workflow:

- [Kubernetes documentation](https://kubernetes.io/docs/home/) – Learn about core concepts, workloads, services, and more.
- [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/use-desktop/kubernetes/) – Use Docker Desktop's built-in Kubernetes support for local testing and development.
- [`kubectl` CLI reference](https://kubernetes.io/docs/reference/kubectl/) – Manage Kubernetes clusters from the command line.
- [Kubernetes Deployment resource](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) – Understand how to manage and scale applications using Deployments.
- [Kubernetes Service resource](https://kubernetes.io/docs/concepts/services-networking/service/) – Learn how to expose your application to internal and external traffic.