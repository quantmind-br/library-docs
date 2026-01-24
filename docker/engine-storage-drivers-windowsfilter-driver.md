---
title: windowsfilter storage driver
url: https://docs.docker.com/engine/storage/drivers/windowsfilter-driver/
source: llms
fetched_at: 2026-01-24T14:25:39.92333248-03:00
rendered_js: false
word_count: 154
summary: This document provides an overview of the windowsfilter storage driver for Docker on Windows, explaining its requirements and how to configure storage limits and data locations.
tags:
    - docker-windows
    - storage-driver
    - windowsfilter
    - ntfs
    - docker-configuration
category: guide
---

The windowsfilter storage driver is the default storage driver for Docker Engine on Windows. The windowsfilter driver uses Windows-native file system layers to for storing Docker layers and volume data on disk. The windowsfilter storage driver only works on file systems formatted with NTFS.

## [Configure the windowsfilter storage driver](#configure-the-windowsfilter-storage-driver)

For most use case, no configuring the windowsfilter storage driver is not necessary.

The default storage limit for Docker Engine on Windows is 127GB. To use a different storage size, set the `size` option for the windowsfilter storage driver. See [windowsfilter options](https://docs.docker.com/reference/cli/dockerd/#windowsfilter-options).

Data is stored on the Docker host in `image` and `windowsfilter` subdirectories within `C:\ProgramData\docker` by default. You can change the storage location by configuring the `data-root` option in the [Daemon configuration file](https://docs.docker.com/reference/cli/dockerd/#on-windows):

```
{
  "data-root": "d:\\docker"
}
```

You must restart the daemon for the configuration change to take effect.

## [Additional information](#additional-information)

For more information about how container storage works on Windows, refer to Microsoft's [Containers on Windows documentation](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-storage).