---
title: Docker volume plugins
url: https://docs.docker.com/engine/extend/plugins_volume/
source: llms
fetched_at: 2026-01-24T14:23:25.821705924-03:00
rendered_js: false
word_count: 826
summary: This document provides a technical specification and API reference for building and integrating Docker volume plugins with external storage systems.
tags:
    - docker-engine
    - volume-plugins
    - api-specification
    - storage-drivers
    - container-storage
category: api
---

Docker Engine volume plugins enable Engine deployments to be integrated with external storage systems such as Amazon EBS, and enable data volumes to persist beyond the lifetime of a single Docker host. See the [plugin documentation](https://docs.docker.com/engine/extend/legacy_plugins/) for more information.

### [1.13.0](#1130)

- If used as part of the v2 plugin architecture, mountpoints that are part of paths returned by the plugin must be mounted under the directory specified by `PropagatedMount` in the plugin configuration ([#26398](https://github.com/docker/docker/pull/26398))

### [1.12.0](#1120)

- Add `Status` field to `VolumeDriver.Get` response ([#21006](https://github.com/docker/docker/pull/21006))
- Add `VolumeDriver.Capabilities` to get capabilities of the volume driver ([#22077](https://github.com/docker/docker/pull/22077))

### [1.10.0](#1100)

- Add `VolumeDriver.Get` which gets the details about the volume ([#16534](https://github.com/docker/docker/pull/16534))
- Add `VolumeDriver.List` which lists all volumes owned by the driver ([#16534](https://github.com/docker/docker/pull/16534))

### [1.8.0](#180)

- Initial support for volume driver plugins ([#14659](https://github.com/docker/docker/pull/14659))

To give a container access to a volume, use the `--volume` and `--volume-driver` flags on the `docker container run` command. The `--volume` (or `-v`) flag accepts a volume name and path on the host, and the `--volume-driver` flag accepts a driver type.

### [`--volume`](#--volume)

The `--volume` (or `-v`) flag takes a value that is in the format `<volume_name>:<mountpoint>`. The two parts of the value are separated by a colon (`:`) character.

- The volume name is a human-readable name for the volume, and cannot begin with a `/` character. It is referred to as `volume_name` in the rest of this topic.
- The `Mountpoint` is the path on the host (v1) or in the plugin (v2) where the volume has been made available.

### [`volumedriver`](#volumedriver)

Specifying a `volumedriver` in conjunction with a `volumename` allows you to use plugins such as [Flocker](https://github.com/ScatterHQ/flocker) to manage volumes external to a single host, such as those on EBS.

The container creation endpoint (`/containers/create`) accepts a `VolumeDriver` field of type `string` allowing to specify the name of the driver. If not specified, it defaults to `"local"` (the default driver for local volumes).

If a plugin registers itself as a `VolumeDriver` when activated, it must provide the Docker Daemon with writeable paths on the host filesystem. The Docker daemon provides these paths to containers to consume. The Docker daemon makes the volumes available by bind-mounting the provided paths into the containers.

> Volume plugins should *not* write data to the `/var/lib/docker/` directory, including `/var/lib/docker/volumes`. The `/var/lib/docker/` directory is reserved for Docker.

### [`/VolumeDriver.Create`](#volumedrivercreate)

Request:

Instruct the plugin that the user wants to create a volume, given a user specified volume name. The plugin does not need to actually manifest the volume on the filesystem yet (until `Mount` is called). `Opts` is a map of driver specific options passed through from the user request.

Response:

Respond with a string error if an error occurred.

### [`/VolumeDriver.Remove`](#volumedriverremove)

Request:

Delete the specified volume from disk. This request is issued when a user invokes `docker rm -v` to remove volumes associated with a container.

Response:

Respond with a string error if an error occurred.

### [`/VolumeDriver.Mount`](#volumedrivermount)

Request:

Docker requires the plugin to provide a volume, given a user specified volume name. `Mount` is called once per container start. If the same `volume_name` is requested more than once, the plugin may need to keep track of each new mount request and provision at the first mount request and deprovision at the last corresponding unmount request.

`ID` is a unique ID for the caller that is requesting the mount.

Response:

- v1
- v2

`Mountpoint` is the path on the host (v1) or in the plugin (v2) where the volume has been made available.

`Err` is either empty or contains an error string.

### [`/VolumeDriver.Path`](#volumedriverpath)

Request:

Request the path to the volume with the given `volume_name`.

Response:

- v1
- v2

Respond with the path on the host (v1) or inside the plugin (v2) where the volume has been made available, and/or a string error if an error occurred.

`Mountpoint` is optional. However, the plugin may be queried again later if one is not provided.

### [`/VolumeDriver.Unmount`](#volumedriverunmount)

Request:

Docker is no longer using the named volume. `Unmount` is called once per container stop. Plugin may deduce that it is safe to deprovision the volume at this point.

`ID` is a unique ID for the caller that is requesting the mount.

Response:

Respond with a string error if an error occurred.

### [`/VolumeDriver.Get`](#volumedriverget)

Request:

Get info about `volume_name`.

Response:

- v1
- v2

Respond with a string error if an error occurred. `Mountpoint` and `Status` are optional.

### [/VolumeDriver.List](#volumedriverlist)

Request:

Get the list of volumes registered with the plugin.

Response:

- v1
- v2

Respond with a string error if an error occurred. `Mountpoint` is optional.

### [/VolumeDriver.Capabilities](#volumedrivercapabilities)

Request:

Get the list of capabilities the driver supports.

The driver is not required to implement `Capabilities`. If it is not implemented, the default values are used.

Response:

Supported scopes are `global` and `local`. Any other value in `Scope` will be ignored, and `local` is used. `Scope` allows cluster managers to handle the volume in different ways. For instance, a scope of `global`, signals to the cluster manager that it only needs to create the volume once instead of on each Docker host. More capabilities may be added in the future.