---
title: docker login
url: https://docs.docker.com/reference/cli/docker/login/
source: llms
fetched_at: 2026-01-24T14:36:41.953140643-03:00
rendered_js: false
word_count: 1151
summary: This document provides a comprehensive guide to the docker login command, explaining how to authenticate to registries and manage credentials using various storage backends and helpers.
tags:
    - docker-cli
    - authentication
    - docker-login
    - credential-management
    - docker-registry
    - container-security
category: reference
---

DescriptionAuthenticate to a registryUsage`docker login [OPTIONS] [SERVER]`

Authenticate to a registry.

You can authenticate to any public or private registry for which you have credentials. Authentication may be required for pulling and pushing images. Other commands, such as `docker scout` and `docker build`, may also require authentication to access subscription-only features or data related to your Docker organization.

Authentication credentials are stored in the configured [credential store](#credential-stores). If you use Docker Desktop, credentials are automatically saved to the native keychain of your operating system. If you're not using Docker Desktop, you can configure the credential store in the Docker configuration file, which is located at `$HOME/.docker/config.json` on Linux or `%USERPROFILE%/.docker/config.json` on Windows. If you don't configure a credential store, Docker stores credentials in the `config.json` file in a base64-encoded format. This method is less secure than configuring and using a credential store.

`docker login` also supports [credential helpers](#credential-helpers) to help you handle credentials for specific registries.

### [Authentication methods](#authentication-methods)

You can authenticate to a registry using a username and access token or password. Docker Hub also supports a web-based sign-in flow, which signs you in to your Docker account without entering your password. For Docker Hub, the `docker login` command uses a device code flow by default, unless the `--username` flag is specified. The device code flow is a secure way to sign in. See [Authenticate to Docker Hub using device code](#authenticate-to-docker-hub-with-web-based-login).

### [Credential stores](#credential-stores)

The Docker Engine can keep user credentials in an external credential store, such as the native keychain of the operating system. Using an external store is more secure than storing credentials in the Docker configuration file.

To use a credential store, you need an external helper program to interact with a specific keychain or external store. Docker requires the helper program to be in the client's host `$PATH`.

You can download the helpers from the `docker-credential-helpers` [releases page](https://github.com/docker/docker-credential-helpers/releases). Helpers are available for the following credential stores:

- D-Bus Secret Service
- Apple macOS keychain
- Microsoft Windows Credential Manager
- [pass](https://www.passwordstore.org/)

With Docker Desktop, the credential store is already installed and configured for you. Unless you want to change the credential store used by Docker Desktop, you can skip the following steps.

#### [Configure the credential store](#configure-the-credential-store)

You need to specify the credential store in `$HOME/.docker/config.json` to tell the Docker Engine to use it. The value of the config property should be the suffix of the program to use (i.e. everything after `docker-credential-`). For example, to use `docker-credential-osxkeychain`:

If you are currently logged in, run `docker logout` to remove the credentials from the file and run `docker login` again.

#### [Default behavior](#default-behavior)

By default, Docker looks for the native binary on each of the platforms, i.e. `osxkeychain` on macOS, `wincred` on Windows, and `pass` on Linux. A special case is that on Linux, Docker will fall back to the `secretservice` binary if it cannot find the `pass` binary. If none of these binaries are present, it stores the base64-encoded credentials in the `config.json` configuration file.

#### [Credential helper protocol](#credential-helper-protocol)

Credential helpers can be any program or script that implements the credential helper protocol. This protocol is inspired by Git, but differs in the information shared.

The helpers always use the first argument in the command to identify the action. There are only three possible values for that argument: `store`, `get`, and `erase`.

The `store` command takes a JSON payload from the standard input. That payload carries the server address, to identify the credential, the username, and either a password or an identity token.

If the secret being stored is an identity token, the Username should be set to `<token>`.

The `store` command can write error messages to `STDOUT` that the Docker Engine will show if there was an issue.

The `get` command takes a string payload from the standard input. That payload carries the server address that the Docker Engine needs credentials for. This is an example of that payload: `https://index.docker.io/v1`.

The `get` command writes a JSON payload to `STDOUT`. Docker reads the user name and password from this payload:

The `erase` command takes a string payload from `STDIN`. That payload carries the server address that the Docker Engine wants to remove credentials for. This is an example of that payload: `https://index.docker.io/v1`.

The `erase` command can write error messages to `STDOUT` that the Docker Engine will show if there was an issue.

### [Credential helpers](#credential-helpers)

Credential helpers are similar to [credential stores](#credential-stores), but act as the designated programs to handle credentials for specific registries. The default credential store will not be used for operations concerning credentials of the specified registries.

#### [Configure credential helpers](#configure-credential-helpers)

If you are currently logged in, run `docker logout` to remove the credentials from the default store.

Credential helpers are specified in a similar way to `credsStore`, but allow for multiple helpers to be configured at a time. Keys specify the registry domain, and values specify the suffix of the program to use (i.e. everything after `docker-credential-`). For example:

OptionDefaultDescription`-p, --password`Password or Personal Access Token (PAT)[`--password-stdin`](#password-stdin)Take the Password or Personal Access Token (PAT) from stdin[`-u, --username`](#username)Username

### [Authenticate to Docker Hub with web-based login](#authenticate-to-docker-hub-with-web-based-login)

By default, the `docker login` command authenticates to Docker Hub, using a device code flow. This flow lets you authenticate to Docker Hub without entering your password. Instead, you visit a URL in your web browser, enter a code, and authenticate.

After entering the code in your browser, you are authenticated to Docker Hub using the account you're currently signed in with on the Docker Hub website or in Docker Desktop. If you aren't signed in, you are prompted to sign in after entering the device code.

### [Authenticate to a self-hosted registry](#authenticate-to-a-self-hosted-registry)

If you want to authenticate to a self-hosted registry you can specify this by adding the server name.

By default, the `docker login` command assumes that the registry listens on port 443 or 80. If the registry listens on a different port, you can specify it by adding the port number to the server name.

> Registry addresses should not include URL path components, only the hostname and (optionally) the port. Registry addresses with URL path components may result in an error. For example, `docker login registry.example.com/foo/` is incorrect, while `docker login registry.example.com` is correct.
> 
> The exception to this rule is the Docker Hub registry, which may use the `/v1/` path component in the address for historical reasons.

### [Authenticate to a registry with a username and password](#username)

To authenticate to a registry with a username and password, you can use the `--username` or `-u` flag. The following example authenticates to Docker Hub with the username `moby`. The password is entered interactively.

### [Provide a password using STDIN (--password-stdin)](#password-stdin)

To run the `docker login` command non-interactively, you can set the `--password-stdin` flag to provide a password through `STDIN`. Using `STDIN` prevents the password from ending up in the shell's history, or log-files.

The following example reads a password from a file, and passes it to the `docker login` command using `STDIN`: