---
title: Building in Docker | Camoufox
url: https://camoufox.com/development/docker/
source: sitemap
fetched_at: 2026-03-09T16:48:12.13546-03:00
rendered_js: false
word_count: 66
summary: This document outlines the steps required to build Camoufox patches on non-Linux systems using Docker, including how to build the image and execute the build process for specified targets and architectures.
tags:
    - camoufox
    - docker
    - building
    - compilation
    - cross-platform
category: tutorial
---

To build Camoufox on a non-Linux system you can use Docker.

* * *

1. Create the Docker image containing Firefox's source code:

```bash

docker build -t camoufox-builder .
```

2. Build Camoufox patches to a target platform and architecture:

```bash

docker run -v "$(pwd)/dist:/app/dist" camoufox-builder --target <os> --arch <arch>
```

How can I use my local ~/.mozbuild directory?

If you want to use the host's .mozbuild directory, you can use the following command instead to run the docker:

```bash

docker run \
  -v "$HOME/.mozbuild":/root/.mozbuild:rw,z \
  -v "$(pwd)/dist:/app/dist" \
  camoufox-builder \
  --target <os> \
  --arch <arch>
```

```bash

Options:
  -h, --help            show this help message and exit
  --target {linux,windows,macos} [{linux,windows,macos} ...]
                        Target platforms to build
  --arch {x86_64,arm64,i686} [{x86_64,arm64,i686} ...]
                        Target architectures to build for each platform
  --bootstrap           Bootstrap the build system
  --clean               Clean the build directory before starting

Example:
$ docker run -v "$(pwd)/dist:/app/dist" camoufox-builder --target windows macos linux --arch x86_64 arm64 i686
```

Build artifacts will now appear written under the `dist/` folder.