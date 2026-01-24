---
title: Use provider services
url: https://docs.docker.com/compose/how-tos/provider-services/
source: llms
fetched_at: 2026-01-24T14:18:02.498130163-03:00
rendered_js: false
word_count: 585
summary: This document explains Docker Compose provider services, a feature that integrates external platform capabilities into the application lifecycle. It covers how to define provider services, manage their dependencies, and handle resource provisioning via injected environment variables.
tags:
    - docker-compose
    - provider-services
    - platform-integration
    - infrastructure-as-code
    - lifecycle-management
    - configuration-management
category: guide
---

Requires: Docker Compose [2.36.0](https://github.com/docker/compose/releases/tag/v2.36.0) and later

Docker Compose supports provider services, which allow integration with services whose lifecycles are managed by third-party components rather than by Compose itself.  
This feature enables you to define and utilize platform-specific services without the need for manual setup or direct lifecycle management.

Provider services are a special type of service in Compose that represents platform capabilities rather than containers. They allow you to declare dependencies on specific platform features that your application needs.

When you define a provider service in your Compose file, Compose works with the platform to provision and configure the requested capability, making it available to your application services.

To use a provider service in your Compose file, you need to:

1. Define a service with the `provider` attribute
2. Specify the `type` of provider you want to use
3. Configure any provider-specific options
4. Declare dependencies from your application services to the provider service

Here's a basic example:

Notice the dedicated `provider` attribute in the `database` service. This attribute specifies that the service is managed by a provider and lets you define options specific to that provider type.

The `depends_on` attribute in the `app` service specifies that it depends on the `database` service. This means that the `database` service will be started before the `app` service, allowing the provider information to be injected into the `app` service.

During the `docker compose up` command execution, Compose identifies services relying on providers and works with them to provision the requested capabilities. The provider then populates Compose model with information about how to access the provisioned resource.

This information is passed to services that declare a dependency on the provider service, typically through environment variables. The naming convention for these variables is:

For example, if your provider service is named `database`, your application service might receive environment variables like:

- `DATABASE_URL` with the URL to access the provisioned resource
- `DATABASE_TOKEN` with an authentication token
- Other provider-specific variables

Your application can then use these environment variables to interact with the provisioned resource.

The `type` field in a provider service references the name of either:

1. A Docker CLI plugin (e.g., `docker-model`)
2. A binary available in the user's PATH
3. A path to the binary or script to execute

When Compose encounters a provider service, it looks for a plugin or binary with the specified name to handle the provisioning of the requested capability.

For example, if you specify `type: model`, Compose will look for a Docker CLI plugin named `docker-model` or a binary named `model` in the PATH.

The plugin or binary is responsible for:

1. Interpreting the options provided in the provider service
2. Provisioning the requested capability
3. Returning information about how to access the provisioned resource

This information is then passed to dependent services as environment variables.

> If you're working with AI models in Compose, use the [`models` top-level element](https://docs.docker.com/ai/compose/models-and-compose/) instead.

Using provider services in your Compose applications offers several benefits:

1. Simplified configuration: You don't need to manually configure and manage platform capabilities
2. Declarative approach: You can declare all your application's dependencies in one place
3. Consistent workflow: You use the same Compose commands to manage your entire application, including platform capabilities

If you want to create your own provider to extend Compose with custom capabilities, you can implement a Compose plugin that registers provider types.

For detailed information on how to create and implement your own provider, refer to the [Compose Extensions documentation](https://github.com/docker/compose/blob/main/docs/extension.md).  
This guide explains the extension mechanism that allows you to add new provider types to Compose.

- [Docker Model Runner documentation](https://docs.docker.com/ai/model-runner/)
- [Compose Extensions documentation](https://github.com/docker/compose/blob/main/docs/extension.md)