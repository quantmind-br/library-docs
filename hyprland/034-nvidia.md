---
title: Nvidia
url: https://wiki.hypr.land/Nvidia/
source: sitemap
fetched_at: 2026-04-26T09:48:25.694665142-03:00
rendered_js: false
word_count: 1459
summary: This document provides a guide for configuring Nvidia graphics drivers and hardware acceleration to ensure compatibility and performance when using Hyprland on Wayland.
tags:
    - nvidia
    - hyprland
    - wayland
    - linux
    - graphics-drivers
    - kernel-modules
    - gpu-acceleration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Foreword

There is no *official* Hyprland support for Nvidia hardware. Many users have had success with the instructions on this page — read everything before asking for help.

Three potential driver setups exist:

1. **Proprietary Drivers** — entirely proprietary Nvidia drivers
2. **Open Drivers** — proprietary drivers with open source kernel modules (recommended for Turing/Ampere architectures, 16xx/20xx series and later)
3. **Nouveau** — clean-room open source implementation (lower performance, best for older cards)

For maximum performance with newer cards, use setup 1 or 2. If neither proprietary setup works, Nouveau may succeed, especially for [older cards](https://wiki.archlinux.org/title/NVIDIA#Unsupported_drivers).

> [!warning]
> For Nvidia 50xx series (5090, 5080, etc.) or newer, open source kernel modules are **REQUIRED** when using proprietary drivers.

According to [Nvidia](https://developer.nvidia.com/blog/nvidia-transitions-fully-towards-open-source-gpu-kernel-modules/), open source kernel modules are recommended for Turing and Ampere architectures. Try both if your card supports both.

## Proprietary driver setup

On Arch and Arch-based distros, use the DKMS variety for multi-kernel support:

| Driver | Package | Notes |
|--------|---------|-------|
| Proprietary | `nvidia-dkms` | Fully proprietary |
| Open kernel modules | `nvidia-open-dkms` | Open source kernel modules |

DKMS packages require kernel headers (e.g. `linux-zen-headers` for the Zen kernel).

### Further installation

Install these packages:

- `nvidia-utils`: userspace graphics drivers (also `lib32-nvidia-utils` for multilib gaming)
- `egl-wayland` (`libnvidia-egl-wayland1` on Ubuntu): EGL/Wayland compatibility

### Early KMS, modeset and fbdev

Since Nvidia driver version 570.86.16, `fbdev` is enabled by default when `modeset` is enabled. Enable `modeset` via `/etc/modprobe.d/nvidia.conf`:

```
options nvidia_drm modeset=1
```

On Arch, this is already done. On NixOS, enabled by default on driver versions after 535.

Enable early KMS by adding modules to `/etc/mkinitcpio.conf`:

```
MODULES=(... nvidia nvidia_modeset nvidia_uvm nvidia_drm ...)
```

Rebuild initramfs: `sudo mkinitcpio -P`, then reboot.

> [!warning]
> Early KMS may break resuming from hibernation. If affected, disable early KMS.

> [!warning]
> Electron/Chromium apps may stall for up to a minute on hybrid graphics systems (Intel iGPU + Nvidia dGPU) after boot. Load `i915` module **before** Nvidia modules to fix:

```
MODULES=(i915 nvidia nvidia_modeset nvidia_uvm nvidia_drm ...)
```

Verify DRM: `cat /sys/module/nvidia_drm/parameters/modeset` returns `Y`.

More info in the [Arch NVIDIA wiki](https://wiki.archlinux.org/title/NVIDIA#DRM_kernel_mode_setting).

### Environment variables

```ini
env = LIBVA_DRIVER_NAME,nvidia
env = __GLX_VENDOR_LIBRARY_NAME,nvidia
```

### Finishing up

Install packages for native Wayland app support. See [[002-getting-started-master-tutorial|https://wiki.hypr.land/Getting-Started/Master-Tutorial/#force-apps-to-use-wayland]].

Reboot, then launch Hyprland.

### Flickering in Electron / CEF apps

Electron and CEF apps flicker because they run in XWayland by default and don't use the `syncobj` protocol.

Enable native Wayland for Electron apps:

```ini
env = ELECTRON_OZONE_PLATFORM_HINT,auto
```

Confirmed working on Vesktop, VSCodium, Obsidian, and others.

Launch Electron/CEF apps with these flags:

```sh
--enable-features=UseOzonePlatform --ozone-platform=wayland
```

For Spotify, use `spotify-launcher` (AUR on Arch) instead of `spotify`, then configure in `~/.config/spotify-launcher.conf`:

```sh
[spotify]
extra_arguments = ["--enable-features=UseOzonePlatform", "--ozone-platform=wayland"]
```

On NixOS, set `NIXOS_OZONE_WL=1` to auto-configure Electron/CEF apps.

> [!info]
> As of Electron 35/Chromium 134, the `syncobj` protocol is supported and resolves all flickering. Manually enable with `--enable-features=WaylandLinuxDrmSyncobj`.

### VA-API hardware video acceleration

Hardware video acceleration on Nvidia + Wayland is possible with [nvidia-vaapi-driver](https://github.com/elFarto/nvidia-vaapi-driver). On Arch, install `libva-nvidia-driver` from official repos.

See the driver README for Firefox configuration. Chromium support is experimental.

### Other issues

#### Multi-monitor with hybrid graphics

On hybrid graphics devices, switch to discrete-only mode:

1. Remove `optimus-manager` (disabling the service does not suffice)
2. Change BIOS from hybrid to discrete graphics

#### Multi-GPU not working for monitors attached to Nvidia GPU

Nvidia lacks important Multi-GPU features. Try these workarounds:

1. Change primary GPU with `AQ_DRM_DEVICES` environment variable — see [[044-configuring-multi-gpu|https://wiki.hypr.land/Configuring/Multi-GPU/#telling-hyprland-which-gpu-to-use]]
2. Set `AQ_FORCE_LINEAR_BLIT=0` to skip forcing linear modifiers on Multi-GPU buffers

This may slow rendering to secondary monitors, but is better than no secondary monitor.

#### Flickering in XWayland games

XWayland games may flicker or present frames out-of-order due to lack of implicit sync and/or flaky explicit sync in newer drivers.

Fixes:

1. Install latest `xorg-xwayland` (≥24.1), `wayland-protocols` (≥1.34), and Nvidia driver (≥555) for explicit sync support
2. If GPU is no longer supported by 555+, install older 535xx drivers — available on Arch via [AUR packages](https://aur.archlinux.org/packages?O=0&K=535xx)

#### Suspend/wakeup issues

On Arch and NixOS, the services `nvidia-suspend.service`, `nvidia-hibernate.service`, and `nvidia-resume.service` are already set up. For others, enable them manually.

Add `nvidia.NVreg_PreserveVideoMemoryAllocations=1` to kernel parameters.

On NixOS:

```nix
{
  hardware.nvidia.powerManagement.enable = true;
}
```

> [!warning]
> [Early KMS](#early-kms-modeset-and-fbdev) may break resuming from hibernation. Disable if affected.

> [!warning]
> Suspend/wakeup issues should be resolved on the Nvidia open driver. If still broken, try the fully proprietary one.

## Still having issues?

Join the [Hyprland Discord](https://discord.gg/hQ9XvMUjjr) and ask in `#hyprland-nvidia`.
