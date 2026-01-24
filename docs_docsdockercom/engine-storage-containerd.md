---
title: containerd image store
url: https://docs.docker.com/engine/storage/containerd/
source: llms
fetched_at: 2026-01-24T14:25:33.471313857-03:00
rendered_js: false
word_count: 675
summary: This document explains how to enable and manage the containerd image store in Docker Engine, detailing its benefits, disk space implications, and manual or automatic migration processes.
tags:
    - docker-engine
    - containerd
    - image-store
    - snapshotters
    - storage-drivers
    - container-runtime
    - migration
category: guide
---

## containerd image store with Docker Engine

The containerd image store is the default storage backend for Docker Engine 29.0 and later on fresh installations. If you upgraded from an earlier version, your daemon continues using the legacy graph drivers (overlay2) until you enable the containerd image store.

containerd, the industry-standard container runtime, uses snapshotters instead of classic storage drivers for storing image and container data.

> The containerd image store is not available when using user namespace remapping (`userns-remap`). See [moby#47377](https://github.com/moby/moby/issues/47377) for details.

The containerd image store uses snapshotters to manage how image layers are stored and accessed on the filesystem. This differs from the classic graph drivers like overlay2.

The containerd image store enables:

- Building and storing multi-platform images locally. With classic storage drivers, you need external builders for multi-platform images.
- Working with images that include attestations (provenance, SBOM). These use image indices that the classic store doesn't support.
- Running Wasm containers. The containerd image store supports WebAssembly workloads.
- Using advanced snapshotters. containerd supports pluggable snapshotters that provide features like lazy-pulling of images (stargz) or peer-to-peer image distribution (nydus, dragonfly).

For most users, switching to the containerd image store is transparent. The storage backend changes, but your workflows remain the same.

The containerd image store uses more disk space than the legacy storage drivers for the same images. This is because containerd stores images in both compressed and uncompressed formats, while the legacy drivers stored only the uncompressed layers.

When you pull an image, containerd keeps the compressed layers (as received from the registry) and also extracts them to disk. This dual storage means each layer occupies more space. The compressed format enables faster pulls and pushes, but requires additional disk capacity.

This difference is particularly noticeable with multiple images sharing the same base layers. With legacy storage drivers, shared base layers were stored once locally, and reused images that depended on them. With containerd, each image stores its own compressed version of shared layers, even though the uncompressed layers are still de-duplicated through snapshotters. The compressed storage adds overhead proportional to the number of images using those layers.

If disk space is constrained, consider the following:

- Regularly prune unused images with `docker image prune`
- Use `docker system df` to monitor disk usage
- [Configure the data directory](https://docs.docker.com/engine/daemon/#configure-the-data-directory-location) to use a partition with adequate space

If you're upgrading from an earlier Docker Engine version, you need to manually enable the containerd image store.

> Switching storage backends temporarily hides images and containers created with the other backend. Your data remains on disk. To access the old images again, switch back to your previous storage configuration.

Add the following configuration to your `/etc/docker/daemon.json` file:

Save the file and restart the daemon:

After restarting the daemon, verify you're using the containerd image store:

Docker Engine uses the `overlayfs` containerd snapshotter by default.

> When you enable the containerd image store, existing images and containers from the overlay2 driver remain on disk but become hidden. They reappear if you switch back to overlay2. To use your existing images with the containerd image store, push them to a registry first, or use `docker save` to export them.

Docker Engine includes an experimental feature that can automatically switch to the containerd image store under certain conditions. **This feature is experimental**. It's provided for those who want to test it, but [starting fresh](#enable-containerd-image-store-on-docker-engine) is the recommended approach.

> The automatic migration feature is experimental and may not work reliably in all scenarios. Create backups before attempting to use it.

To enable automatic migration, add the `containerd-migration` feature to your `/etc/docker/daemon.json`:

You can also set the `DOCKER_MIGRATE_SNAPSHOTTER_THRESHOLD` environment variable to make the daemon switch automatically if you have no containers and your image count is at or below the threshold. For systemd:

Add:

If you have no running or stopped containers and 5 or fewer images, the daemon switches to the containerd image store on restart. Your overlay2 data remains on disk but becomes hidden.

To learn more about the containerd image store and its capabilities in Docker Desktop, see [containerd image store on Docker Desktop](https://docs.docker.com/desktop/features/containerd/).