---
title: Common challenges and questions
url: https://docs.docker.com/guides/testcontainers-cloud/common-questions/
source: llms
fetched_at: 2026-01-24T14:12:09.91306913-03:00
rendered_js: false
word_count: 463
summary: This document provides an overview of Testcontainers Cloud through a series of frequently asked questions, covering its features, integration steps, and benefits over local environments.
tags:
    - testcontainers-cloud
    - integration-testing
    - ci-cd
    - cloud-computing
    - docker
    - test-automation
category: reference
---

### [How is Testcontainers Cloud different from the open-source Testcontainers framework?](#how-is-testcontainers-cloud-different-from-the-open-source-testcontainers-framework)

While the open-source Testcontainers is a library that provides a lightweight APIs for bootstrapping local development and test dependencies with real services wrapped in Docker containers, Testcontainers Cloud provides a cloud runtime for these containers. This reduces the resource strain on local environments and provides more scalability, especially in CI/CD workflows, that enables consistent Testcontainers experience across the organization.

### [What types of containers can I run with Testcontainers Cloud?](#what-types-of-containers-can-i-run-with-testcontainers-cloud)

Testcontainers Cloud supports any containers you would typically use with the Testcontainers framework, including databases (PostgreSQL, MySQL, MongoDB), message brokers (Kafka, RabbitMQ), and other services required for integration testing.

### [Do I need to change my existing test code to use Testcontainers Cloud?](#do-i-need-to-change-my-existing-test-code-to-use-testcontainers-cloud)

No, you don't need to change your existing test code. Testcontainers Cloud integrates seamlessly with the open-source Testcontainers framework. Once the cloud configuration is set up, it automatically manages the containers in the cloud without requiring code changes.

### [How do I integrate Testcontainers Cloud into my project?](#how-do-i-integrate-testcontainers-cloud-into-my-project)

To integrate Testcontainers Cloud, you need to install the Testcontainers Desktop app and select run with Testcontainers Cloud option in the menu. In CI you’ll need to add a workflow step that downloads Testcontainers Cloud agent. No code changes are required beyond enabling Cloud runtime via the Testcontainers Desktop app locally or installing Testcontainers Cloud agent in CI.

### [Can I use Testcontainers Cloud in a CI/CD pipeline?](#can-i-use-testcontainers-cloud-in-a-cicd-pipeline)

Yes, Testcontainers Cloud is designed to work efficiently in CI/CD pipelines. It helps reduce build times and resource bottlenecks by offloading containers that you spin up with Testcontainers library to the cloud, making it a perfect fit for continuous testing environments.

### [What are the benefits of using Testcontainers Cloud?](#what-are-the-benefits-of-using-testcontainers-cloud)

The key benefits include reduced resource usage on local machines and CI servers, scalability (run more containers without performance degradation), consistent testing environments, centralized monitoring, ease of CI configuration with removed security concerns of running Docker-in-Docker or a privileged daemon.

### [Does Testcontainers Cloud support all programming languages?](#does-testcontainers-cloud-support-all-programming-languages)

Testcontainers Cloud supports any language that works with the open-source Testcontainers libraries, including Java, Python, Node.js, Go, and others. As long as your project uses Testcontainers, it can be offloaded to Testcontainers Cloud.

### [How is container cleanup handled in Testcontainers Cloud?](#how-is-container-cleanup-handled-in-testcontainers-cloud)

While Testcontainers library automatically handles container lifecycle management, Testcontainers Cloud manages the allocated cloud worker lifetime. This means that containers are spun up, monitored, and cleaned up after tests are completed by Testcontainers library, and the worker where these containers have being running will be removed automatically after the ~35 min idle period by Testcontainers Cloud. This approach frees developers from manually managing containers and associated cloud resources.

### [Is there a free tier or pricing model for Testcontainers Cloud?](#is-there-a-free-tier-or-pricing-model-for-testcontainers-cloud)

Pricing details for Testcontainers Cloud can be found on the [pricing page](https://testcontainers.com/cloud/pricing/).