---
title: Building in Docker | Camoufox
url: https://camoufox.com/development/docker/
source: crawler
fetched_at: 2026-02-14T14:05:31.759206-03:00
rendered_js: true
word_count: 66
summary: This document provides instructions for building Camoufox on non-Linux systems using Docker, covering image creation, cross-platform compilation, and volume mounting.
tags:
    - camoufox
    - docker
    - build-process
    - cross-platform
    - compilation
category: guide
---

To build Camoufox on a non-Linux system you can use Docker.

* * *

1. Create the Docker image containing Firefox's source code:

```

docker build -t camoufox-builder .
```

2. Build Camoufox patches to a target platform and architecture:

```

docker run -v "$(pwd)/dist:/app/dist" camoufox-builder --target <os> --arch <arch>
```

How can I use my local ~/.mozbuild directory?

If you want to use the host's .mozbuild directory, you can use the following command instead to run the docker:

```

docker run \
  -v "$HOME/.mozbuild":/root/.mozbuild:rw,z \
  -v "$(pwd)/dist:/app/dist" \
  camoufox-builder \
  --target <os> \
  --arch <arch>
```

```

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