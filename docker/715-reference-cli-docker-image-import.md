---
title: docker image import
url: https://docs.docker.com/reference/cli/docker/image/import/
source: llms
fetched_at: 2026-01-24T14:36:17.414909887-03:00
rendered_js: false
word_count: 547
summary: This document provides technical specifications and usage instructions for the 'docker image import' command, used to create new Docker images from filesystem archives.
tags:
    - docker-cli
    - image-import
    - container-images
    - filesystem-archives
    - docker-reference
category: reference
---

DescriptionImport the contents from a tarball to create a filesystem imageUsage`docker image import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker import`

You can specify a `URL` or `-` (dash) to take data directly from `STDIN`. The `URL` can point to an archive (.tar, .tar.gz, .tgz, .bzip, .tar.xz, or .txz) containing a filesystem or to an individual file on the Docker host. If you specify an archive, Docker untars it in the container relative to the `/` (root). If you specify an individual file, you must specify the full path within the host. To import from a remote location, specify a `URI` that begins with the `http://` or `https://` protocol.

OptionDefaultDescription[`-c, --change`](#change)Apply Dockerfile instruction to the created image[`-m, --message`](#message)Set commit message for imported image[`--platform`](#platform)API 1.32+ Set platform if server is multi-platform capable

### [Import from a remote location](#import-from-a-remote-location)

This creates a new untagged image.

### [Import from a local file](#import-from-a-local-file)

Import to docker via pipe and `STDIN`.

Import to docker from a local archive.

### [Import from a local directory](#import-from-a-local-directory)

Note the `sudo` in this example – you must preserve the ownership of the files (especially root ownership) during the archiving with tar. If you are not root (or the sudo command) when you tar, then the ownerships might not get preserved.

### [Import with new configurations (-c, --change)](#change)

The `--change` option applies `Dockerfile` instructions to the image that is created. Not all `Dockerfile` instructions are supported; the list of instructions is limited to metadata (configuration) changes. The following `Dockerfile` instructions are supported:

- [`CMD`](https://docs.docker.com/reference/dockerfile/#cmd)
- [`ENTRYPOINT`](https://docs.docker.com/reference/dockerfile/#entrypoint)
- [`ENV`](https://docs.docker.com/reference/dockerfile/#env)
- [`EXPOSE`](https://docs.docker.com/reference/dockerfile/#expose)
- [`HEALTHCHECK`](https://docs.docker.com/reference/dockerfile/#healthcheck)
- [`LABEL`](https://docs.docker.com/reference/dockerfile/#label)
- [`ONBUILD`](https://docs.docker.com/reference/dockerfile/#onbuild)
- [`STOPSIGNAL`](https://docs.docker.com/reference/dockerfile/#stopsignal)
- [`USER`](https://docs.docker.com/reference/dockerfile/#user)
- [`VOLUME`](https://docs.docker.com/reference/dockerfile/#volume)
- [`WORKDIR`](https://docs.docker.com/reference/dockerfile/#workdir)

The following example imports an image from a TAR-file containing a root-filesystem, and sets the `DEBUG` environment-variable in the resulting image:

The `--change` option can be set multiple times to apply multiple `Dockerfile` instructions. The example below sets the `LABEL1` and `LABEL2` labels on the imported image, in addition to the `DEBUG` environment variable from the previous example:

### [Import with a commit message (-m, --message)](#message)

The `--message` (or `-m`) option allows you to set a custom comment in the image's metadata. The following example imports an image from a local archive and sets a custom message.

After importing, the message is set in the "Comment" field of the image's configuration, which is shown when viewing the image's history:

### [When the daemon supports multiple operating systems](#when-the-daemon-supports-multiple-operating-systems)

If the daemon supports multiple operating systems, and the image being imported does not match the default operating system, it may be necessary to add `--platform`. This would be necessary when importing a Linux image into a Windows daemon.

### [Set the platform for the imported image (--platform)](#platform)

The `--platform` option allows you to specify the platform for the imported image. By default, the daemon's native platform is used as platform, but the `--platform` option allows you to override the default, for example, in situations where the imported root filesystem is for a different architecture or operating system.

The platform option takes the `os[/arch[/variant]]` format; for example, `linux/amd64` or `linux/arm64/v8`. Architecture and variant are optional, and default to the daemon's native architecture if omitted.

The following example imports an image from a root-filesystem in `rootfs.tgz`, and sets the image's platform to `linux/amd64`;

After importing the image, the image's platform is set in the image's configuration;