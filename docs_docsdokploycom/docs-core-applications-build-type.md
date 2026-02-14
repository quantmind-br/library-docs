---
title: Build Type | Dokploy
url: https://docs.dokploy.com/docs/core/applications/build-type
source: crawler
fetched_at: 2026-02-14T14:12:59.027685-03:00
rendered_js: true
word_count: 995
summary: This document explains the various build methods available in Dokploy, detailing the configuration options for Nixpacks, Railpack, Dockerfile, Buildpacks, and static site deployments.
tags:
    - dokploy
    - build-types
    - nixpacks
    - railpack
    - docker-build
    - deployment-guides
    - buildpacks
category: guide
---

Learn about the different build types available in Dokploy, including Nixpacks, Dockerfile, and Buildpack options.

Dokploy offers three distinct build types for deploying applications, each suited to different development needs and preferences.

### [Nixpacks](#nixpacks)

This is the default build type in Dokploy. When you select Nixpacks, Dokploy builds your application as a Nixpack, which is optimized for ease of use and efficiency.

Nixpacks expose multiples variables to be configured via environment variables. All of these variables are prefixed with `NIXPACKS_`, you can define them in the `Environment Variables` tab.

VariableDescription`NIXPACKS_INSTALL_CMD`Override the install command to use`NIXPACKS_BUILD_CMD`Override the build command to use`NIXPACKS_START_CMD`Override command to run when starting the container`NIXPACKS_PKGS`Add additional [Nix packages](https://search.nixos.org/packages?channel=unstable) to install`NIXPACKS_APT_PKGS`Add additional Apt packages to install (comma delimited)`NIXPACKS_LIBS`Add additional Nix libraries to make available`NIXPACKS_INSTALL_CACHE_DIRS`Add additional directories to cache during the install phase`NIXPACKS_BUILD_CACHE_DIRS`Add additional directories to cache during the build phase`NIXPACKS_NO_CACHE`Disable caching for the build`NIXPACKS_CONFIG_FILE`Location of the Nixpacks configuration file relative to the root of the app`NIXPACKS_DEBIAN`Enable Debian base image, used for supporting OpenSSL 1.1

If you need more manage about nixpacks process, you can create a `nixpacks.toml` file in the root of your application you can read here [Nixpacks Configuration](https://nixpacks.com/docs/configuration/file).

Nixpacks support monorepo such as NX Monorepo, Turborepo, Moon Repo, you can read more about it [here](https://nixpacks.com/docs/providers/node#build).

You can read more about Nixpacks [here](https://nixpacks.com/).

Since Nixpacks have a [static builder](https://nixpacks.com/docs/providers/staticfile) Dokploy expose a field called `Publish Directory` where basically you can specify the directory that you want to publish after the build process is finished, example:

Astro applications after you build it usually create a `dist` directory, so you can specify the `dist` directory as the publish directory and then Dokploy will copy all the files in the `dist` directory to the root of your application, and will use a NGINX Optimized Dockerfile to run your application.

### [Railpack (NEW)](#railpack-new)

Railpack is a new build type optimized and is the successor of Nixpacks.

Railpack exposes multiple Build Variables, you can define them in the `Environment Variables` tab.

NameDescription`RAILPACK_BUILD_CMD`Set the command to run for the build step. This overwrites any commands that come from providers`RAILPACK_START_CMD`Set the command to run when the container starts`RAILPACK_PACKAGES`Install additional Mise packages. In the format `pkg@version`. The latest version is used if not provided.`RAILPACK_BUILD_APT_PACKAGES`Install additional Apt packages during build`RAILPACK_DEPLOY_APT_PACKAGES`Install additional Apt packages in the final image

### [Specifying Railpack Version](#specifying-railpack-version)

Dokploy provides a **Railpack Version** field in the application settings where you can specify a specific version of Railpack to use. This allows you to:

- **Pin to a specific version**: Ensure consistent builds across deployments
- **Use a newer version**: Test or use features from a specific release
- **Stay on a stable version**: Avoid potential issues from automatic updates

**How to use:**

1. Navigate to your application settings
2. Find the **Railpack Version** field
3. Enter the version you want to use (e.g., `0.15.1`)
4. Dokploy will automatically download and use the specified version for your builds

**Example:**

To use Railpack version `0.15.1`, simply enter `0.15.1` in the Railpack Version field.

If you specify an invalid version, Dokploy will show an error. Make sure to use a valid version from the [Railpack releases page](https://github.com/railwayapp/railpack/releases).

You can read more about Railpack [here](https://railpack.com/config/environment-variables).

Railpack supports Nodejs, Python, Go, PHP, Go, StaticFile, Shell Scripts.

### [Dockerfile](#dockerfile)

If your project includes a Dockerfile, you can specify its path. Dokploy will use this Dockerfile to build your application directly, giving you full control over the build environment and dependencies

Dokploy expose 3 Fields to be configured:

- `Dockerfile Path (Required)`: The path to the Dockerfile to use for building the application, eg. If your Dockerfile is in the root of your application you can just specify the `Dockerfile` file.
- `Docker Context Path`: This is where the Dockerfile is located, eg. If your Dockerfile is in the root of your application you can just specify the `.` (dot) character, is basically to tell docker what context will use to build your application, you can read [Dockerfile Context](https://docs.docker.com/build/concepts/context/) for more information.
- `Docker Build Stage`: This is the build stage to use for building the application, eg. If you want to use the `builder` stage you can specify the `builder` stage, read more about build stages [here](https://docs.docker.com/build/building/multi-stage/).

#### [Environment Variables for Dockerfile Builds](#environment-variables-for-dockerfile-builds)

When you enable the Dockerfile build type, two additional fields become available in the **Environment** tab:

- **Build Time Arguments**: Configure [build arguments (ARG)](https://docs.docker.com/build/building/variables/) that are passed to your Dockerfile during the build process. Build arguments allow you to parameterize your Dockerfile, making it more flexible and reusable. For example, you can specify versions of dependencies, feature flags, or other build-time configurations.
- **Build-time Secrets**: Configure [build secrets](https://docs.docker.com/build/building/secrets/) to securely pass sensitive information (such as API tokens, passwords, or SSH keys) to your build process. Unlike build arguments, secrets are not exposed in the final image or build history, making them the recommended way to handle sensitive data during builds.

Build arguments and environment variables are inappropriate for passing secrets, as they persist in the final image. Always use build-time secrets for sensitive information like API tokens or passwords.

### [Buildpack](#buildpack)

Dokploy supports two types of buildpacks:

- **Heroku**: Adapted from Heroku's popular cloud platform, these buildpacks are designed for compatibility and ease of migration, you can optional specify the Heroku Version to use, by default Dokploy will use the 24.
- **Paketo**: Provides cloud-native buildpacks that leverage modern standards and practices for building applications.

By choosing the appropriate build type, you can tailor the deployment process to best fit your application's requirements and your operational preferences.

### [Static](#static)

Static build type is used to server static applications, it will use a NGINX Optimized Dockerfile to run your application.

Dokploy will copy everything from the `Root` directory and will mount it to the `/usr/share/nginx/html` directory, and will use a NGINX Optimized Dockerfile to run your application.

Ensure to use the port `80` when creating a domain.

- For prototyping and development purposes, we recommend using the `Nixpacks` build type.
- For production purposes, we recommend follow this [Production Guide](https://docs.dokploy.com/docs/core/applications/going-production) to have a rock solid deployment.
- For static applications, we recommend using the `Static` build type.