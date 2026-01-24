---
title: Store configuration data using Docker Configs
url: https://docs.docker.com/engine/swarm/configs/
source: llms
fetched_at: 2026-01-24T14:25:44.793246798-03:00
rendered_js: false
word_count: 2202
summary: This document explains how to manage non-sensitive configuration data for Docker Swarm services using configs, enabling external storage and management of configuration files separately from container images.
tags:
    - docker-swarm
    - docker-configs
    - container-orchestration
    - service-configuration
    - windows-containers
    - raft-log
    - configuration-management
category: guide
---

Docker swarm service configs allow you to store non-sensitive information, such as configuration files, outside a service's image or running containers. This allows you to keep your images as generic as possible, without the need to bind-mount configuration files into the containers or use environment variables.

Configs operate in a similar way to [secrets](https://docs.docker.com/engine/swarm/secrets/), except that they are not encrypted at rest and are mounted directly into the container's filesystem without the use of RAM disks. Configs can be added or removed from a service at any time, and services can share a config. You can even use configs in conjunction with environment variables or labels, for maximum flexibility. Config values can be generic strings or binary content (up to 500 kb in size).

> Docker configs are only available to swarm services, not to standalone containers. To use this feature, consider adapting your container to run as a service with a scale of 1.

Configs are supported on both Linux and Windows services.

### [Windows support](#windows-support)

Docker includes support for configs on Windows containers, but there are differences in the implementations, which are called out in the examples below. Keep the following notable differences in mind:

- Config files with custom targets are not directly bind-mounted into Windows containers, since Windows does not support non-directory file bind-mounts. Instead, configs for a container are all mounted in `C:\ProgramData\Docker\internal\configs` (an implementation detail which should not be relied upon by applications) within the container. Symbolic links are used to point from there to the desired target of the config within the container. The default target is `C:\ProgramData\Docker\configs`.
- When creating a service which uses Windows containers, the options to specify UID, GID, and mode are not supported for configs. Configs are currently only accessible by administrators and users with `system` access within the container.
- On Windows, create or update a service using `--credential-spec` with the `config://<config-name>` format. This passes the gMSA credentials file directly to nodes before a container starts. No gMSA credentials are written to disk on worker nodes. For more information, refer to [Deploy services to a swarm](https://docs.docker.com/engine/swarm/services/#gmsa-for-swarm).

When you add a config to the swarm, Docker sends the config to the swarm manager over a mutual TLS connection. The config is stored in the Raft log, which is encrypted. The entire Raft log is replicated across the other managers, ensuring the same high availability guarantees for configs as for the rest of the swarm management data.

When you grant a newly-created or running service access to a config, the config is mounted as a file in the container. The location of the mount point within the container defaults to `/<config-name>` in Linux containers. In Windows containers, configs are all mounted into `C:\ProgramData\Docker\configs` and symbolic links are created to the desired location, which defaults to `C:\<config-name>`.

You can set the ownership (`uid` and `gid`) for the config, using either the numerical ID or the name of the user or group. You can also specify the file permissions (`mode`). These settings are ignored for Windows containers.

- If not set, the config is owned by the user running the container command (often `root`) and that user's default group (also often `root`).
- If not set, the config has world-readable permissions (mode `0444`), unless a `umask` is set within the container, in which case the mode is impacted by that `umask` value.

You can update a service to grant it access to additional configs or revoke its access to a given config at any time.

A node only has access to configs if the node is a swarm manager or if it is running service tasks which have been granted access to the config. When a container task stops running, the configs shared to it are unmounted from the in-memory filesystem for that container and flushed from the node's memory.

If a node loses connectivity to the swarm while it is running a task container with access to a config, the task container still has access to its configs, but cannot receive updates until the node reconnects to the swarm.

You can add or inspect an individual config at any time, or list all configs. You cannot remove a config that a running service is using. See [Rotate a config](https://docs.docker.com/engine/swarm/configs/#example-rotate-a-config) for a way to remove a config without disrupting running services.

To update or roll back configs more easily, consider adding a version number or date to the config name. This is made easier by the ability to control the mount point of the config within a given container.

To update a stack, make changes to your Compose file, then re-run `docker stack deploy -c <new-compose-file> <stack-name>`. If you use a new config in that file, your services start using them. Keep in mind that configurations are immutable, so you can't change the file for an existing service. Instead, you create a new config to use a different file

You can run `docker stack rm` to stop the app and take down the stack. This removes any config that was created by `docker stack deploy` with the same stack name. This removes *all* configs, including those not referenced by services and those remaining after a `docker service update --config-rm`.

Use these links to read about specific commands, or continue to the [example about using configs with a service](#advanced-example-use-configs-with-a-nginx-service).

- [`docker config create`](https://docs.docker.com/reference/cli/docker/config/create/)
- [`docker config inspect`](https://docs.docker.com/reference/cli/docker/config/inspect/)
- [`docker config ls`](https://docs.docker.com/reference/cli/docker/config/ls/)
- [`docker config rm`](https://docs.docker.com/reference/cli/docker/config/rm/)

This section includes graduated examples which illustrate how to use Docker configs.

> These examples use a single-engine swarm and unscaled services for simplicity. The examples use Linux containers, but Windows containers also support configs.

### [Defining and using configs in compose files](#defining-and-using-configs-in-compose-files)

The `docker stack` command supports defining configs in a Compose file. However, the `configs` key is not supported for `docker compose`. See [the Compose file reference](https://docs.docker.com/reference/compose-file/legacy-versions/) for details.

### [Simple example: Get started with configs](#simple-example-get-started-with-configs)

This simple example shows how configs work in just a few commands. For a real-world example, continue to [Advanced example: Use configs with a Nginx service](#advanced-example-use-configs-with-a-nginx-service).

1. Add a config to Docker. The `docker config create` command reads standard input because the last argument, which represents the file to read the config from, is set to `-`.
2. Create a `redis` service and grant it access to the config. By default, the container can access the config at `/my-config`, but you can customize the file name on the container using the `target` option.
3. Verify that the task is running without issues using `docker service ps`. If everything is working, the output looks similar to this:
4. Get the ID of the `redis` service task container using `docker ps`, so that you can use `docker container exec` to connect to the container and read the contents of the config data file, which defaults to being readable by all and has the same name as the name of the config. The first command below illustrates how to find the container ID, and the second and third commands use shell completion to do this automatically.
5. Try removing the config. The removal fails because the `redis` service is running and has access to the config.
6. Remove access to the config from the running `redis` service by updating the service.
7. Repeat steps 3 and 4 again, verifying that the service no longer has access to the config. The container ID is different, because the `service update` command redeploys the service.
8. Stop and remove the service, and remove the config from Docker.

### [Simple example: Use configs in a Windows service](#simple-example-use-configs-in-a-windows-service)

This is a very simple example which shows how to use configs with a Microsoft IIS service running on Docker for Windows running Windows containers on Microsoft Windows 10. It is a naive example that stores the webpage in a config.

This example assumes that you have PowerShell installed.

1. Save the following into a new file `index.html`.
2. If you have not already done so, initialize or join the swarm.
3. Save the `index.html` file as a swarm config named `homepage`.
4. Create an IIS service and grant it access to the `homepage` config.
5. Access the IIS service at `http://localhost:8000/`. It should serve the HTML content from the first step.
6. Remove the service and the config.

### [Example: Use a templated config](#example-use-a-templated-config)

To create a configuration in which the content will be generated using a template engine, use the `--template-driver` parameter and specify the engine name as its argument. The template will be rendered when container is created.

1. Save the following into a new file `index.html.tmpl`.
2. Save the `index.html.tmpl` file as a swarm config named `homepage`. Provide parameter `--template-driver` and specify `golang` as template engine.
3. Create a service that runs Nginx and has access to the environment variable HELLO and to the config.
4. Verify that the service is operational: you can reach the Nginx server, and that the correct output is being served.

### [Advanced example: Use configs with a Nginx service](#advanced-example-use-configs-with-a-nginx-service)

This example is divided into two parts. [The first part](#generate-the-site-certificate) is all about generating the site certificate and does not directly involve Docker configs at all, but it sets up [the second part](#configure-the-nginx-container), where you store and use the site certificate as a series of secrets and the Nginx configuration as a config. The example shows how to set options on the config, such as the target location within the container and the file permissions (`mode`).

#### [Generate the site certificate](#generate-the-site-certificate)

Generate a root CA and TLS certificate and key for your site. For production sites, you may want to use a service such as `Let’s Encrypt` to generate the TLS certificate and key, but this example uses command-line tools. This step is a little complicated, but is only a set-up step so that you have something to store as a Docker secret. If you want to skip these sub-steps, you can [use Let's Encrypt](https://letsencrypt.org/getting-started/) to generate the site key and certificate, name the files `site.key` and `site.crt`, and skip to [Configure the Nginx container](#configure-the-nginx-container).

1. Generate a root key.
2. Generate a CSR using the root key.
3. Configure the root CA. Edit a new file called `root-ca.cnf` and paste the following contents into it. This constrains the root CA to only sign leaf certificates and not intermediate CAs.
4. Sign the certificate.
5. Generate the site key.
6. Generate the site certificate and sign it with the site key.
7. Configure the site certificate. Edit a new file called `site.cnf` and paste the following contents into it. This constrains the site certificate so that it can only be used to authenticate a server and can't be used to sign certificates.
8. Sign the site certificate.
9. The `site.csr` and `site.cnf` files are not needed by the Nginx service, but you need them if you want to generate a new site certificate. Protect the `root-ca.key` file.

#### [Configure the Nginx container](#configure-the-nginx-container)

1. Produce a very basic Nginx configuration that serves static files over HTTPS. The TLS certificate and key are stored as Docker secrets so that they can be rotated easily.
   
   In the current directory, create a new file called `site.conf` with the following contents:
2. Create two secrets, representing the key and the certificate. You can store any file as a secret as long as it is smaller than 500 KB. This allows you to decouple the key and certificate from the services that use them. In these examples, the secret name and the file name are the same.
3. Save the `site.conf` file in a Docker config. The first parameter is the name of the config, and the second parameter is the file to read it from.
   
   List the configs:
4. Create a service that runs Nginx and has access to the two secrets and the config. Set the mode to `0440` so that the file is only readable by its owner and that owner's group, not the world.
   
   Within the running containers, the following three files now exist:
   
   - `/run/secrets/site.key`
   - `/run/secrets/site.crt`
   - `/etc/nginx/conf.d/site.conf`
5. Verify that the Nginx service is running.
6. Verify that the service is operational: you can reach the Nginx server, and that the correct TLS certificate is being used.
7. Unless you are going to continue to the next example, clean up after running this example by removing the `nginx` service and the stored secrets and config.

You have now configured a Nginx service with its configuration decoupled from its image. You could run multiple sites with exactly the same image but separate configurations, without the need to build a custom image at all.

### [Example: Rotate a config](#example-rotate-a-config)

To rotate a config, you first save a new config with a different name than the one that is currently in use. You then redeploy the service, removing the old config and adding the new config at the same mount point within the container. This example builds upon the previous one by rotating the `site.conf` configuration file.

1. Edit the `site.conf` file locally. Add `index.php` to the `index` line, and save the file.
2. Create a new Docker config using the new `site.conf`, called `site-v2.conf`.
3. Update the `nginx` service to use the new config instead of the old one.
4. Verify that the `nginx` service is fully re-deployed, using `docker service ps nginx`. When it is, you can remove the old `site.conf` config.
5. To clean up, you can remove the `nginx` service, as well as the secrets and configs.

You have now updated your `nginx` service's configuration without the need to rebuild its image.