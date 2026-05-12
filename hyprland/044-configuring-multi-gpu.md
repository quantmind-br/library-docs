---
title: Multi-GPU
url: https://wiki.hypr.land/Configuring/Multi-GPU/
source: sitemap
fetched_at: 2026-04-26T09:49:26.551824289-03:00
rendered_js: false
word_count: 562
summary: Configure Hyprland for multi-GPU systems by identifying device paths and setting AQ_DRM_DEVICES for GPU selection and monitor output.
tags:
    - hyprland
    - multi-gpu
    - drm
    - linux-configuration
    - udev-rules
    - gpu-passthrough
    - hardware-acceleration
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Multi-GPU setups allow using one GPU for Hyprland rendering (windows, animations) and another for hardware-accelerated applications. Common in gaming laptops, GPU-passthrough hosts, and systems with multiple GPUs.

## Detecting GPUs[](#detecting-gpus)

List PCI display controllers:

```plain
lspci -d ::03xx
01:00.0 VGA compatible controller: NVIDIA Corporation TU117M [GeForce GTX 1650 Mobile / Max-Q] (rev a1)
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne [Radeon Vega Series / Radeon Vega Mobile Series] (rev c6)
```

Two GPUs detected: dedicated NVIDIA GTX 1650 and integrated AMD Cezanne.

Check DRI device paths:

```plain
ls -l /dev/dri/by-path
lrwxrwxrwx 1 root root  8 Jul 14 15:45 pci-0000:01:00.0-card -> ../card0
lrwxrwxrwx 1 root root 13 Jul 14 15:45 pci-0000:01:00.0-render -> ../renderD128
lrwxrwxrwx 1 root root  8 Jul 14 15:45 pci-0000:06:00.0-card -> ../card1
lrwxrwxrwx 1 root root 13 Jul 14 15:45 pci-0000:06:00.0-render -> ../renderD129
```

The AMD card path is `pci-0000:06:00.0-card`. Do **not** use `card1` — it is dynamically assigned at boot and changes.

## Telling Hyprland which GPU to use[](#telling-hyprland-which-gpu-to-use)

Set `AQ_DRM_DEVICES` to a `:`-separated list of card paths, in priority order:

```ini
env = AQ_DRM_DEVICES,/dev/dri/card0:/dev/dri/card1
```

`card0` is the primary renderer; if unavailable, `card1` becomes primary.

> [!note]
> Laptops should prefer the integrated GPU to preserve battery life. Desktop setups with GPUs of different power ratings should assign the appropriate one as primary.

> [!warning]
> External monitors connected to a secondary card require that card to be listed in `AQ_DRM_DEVICES`, though it does not need to be primary.

uwsm users should export `AQ_DRM_DEVICES` in `~/.config/uwsm/env-hyprland` instead:

```bash
export AQ_DRM_DEVICES="/dev/dri/card0:/dev/dri/card1"
```

## Creating consistent device paths[](#creating-consistent-device-paths-for-specific-cards)

`/dev/dri/card*` paths change periodically, and colons in card paths conflict with `AQ_DRM_DEVICES` separators. Use udev rules for reliable symlinks.

Create `/etc/udev/rules.d/amd-igpu-dev-path.rules`:

```sh
SYMLINK_NAME="amd-igpu"
RULE_PATH="/etc/udev/rules.d/amd-igpu-dev-path.rules"
AMD_IGPU_ID=$(lspci -d ::03xx | grep 'AMD' | cut -f1 -d' ')
UDEV_RULE="$(cat <<EOF
KERNEL=="card*", \
KERNELS=="0000:$AMD_IGPU_ID", \
SUBSYSTEM=="drm", \
SUBSYSTEMS=="pci", \
SYMLINK+="dri/$SYMLINK_NAME"
EOF
)"
echo "$UDEV_RULE" | sudo tee "$RULE_PATH"
```

Reload udev rules:

```sh
sudo udevadm control --reload
sudo udevadm trigger
```

Verify the symlink:

```console
$ ls -l /dev/dri/amd-igpu
lrwxrwxrwx 1 root root 5 /dev/dri/amd-igpu -> card1
```

The symlink automatically updates if the card changes. Use in `AQ_DRM_DEVICES`:

```ini
env = AQ_DRM_DEVICES, /dev/dri/amd-igpu
```