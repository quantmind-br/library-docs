---
title: GTK OpenGL Context - Help
url: https://ghostty.org/docs/help/gtk-opengl-context
source: crawler
fetched_at: 2026-03-10T06:35:58.639366-03:00
rendered_js: true
word_count: 546
summary: This document explains troubleshooting steps for the Ghostty error where it fails to start due to being unable to acquire an OpenGL context from GTK, which is typically caused by environment or driver issues.
tags:
    - ghostty
    - opengl
    - gtk
    - context-error
    - troubleshooting
    - driver-issues
category: guide
---

In some situations, Ghostty may fail to start with an error about being "unable to acquire an OpenGL context". This page adds more details about this error and how to resolve it.

The Ghostty GTK application uses OpenGL for rendering. To render with OpenGL, Ghostty needs to first acquire an "OpenGL context" from GTK. This gives us the namespace to execute OpenGL commands.

In rare situations, GTK may be unable to provide Ghostty with an OpenGL context. When this happens, Ghostty is unable to render anything and must show this error.

This is **always an environment issue**. GTK provides Ghostty with the OpenGL context, and there isn't generally anything Ghostty itself can do to resolve this directly. It is usually an issue regarding a library, driver, or OS package version. This page will attempt to provide some assistance in tracking down the issue.

If you want to try to get Ghostty working quickly, try the following.

1. **Install a [binary package](https://ghostty.org/docs/install/binary).** If you're building from source, try using a binary package instead. Binary packages tend to be built in a more controlled environment that works with a specific distribution and its libraries.
2. **Check your GPU drivers.** GPU drivers are a common cause of OpenGL issues. Try updating or downgrading your GPU drivers, especially if you're using proprietary drivers.
3. **Build Ghostty from source using only system packages.** If you're using the Nix development environment to build Ghostty, try building it from source using only system packages. See the [build from source](https://ghostty.org/docs/install/build) instructions to do this (but ignore the "Building with Nix" section).

> This section purposely avoids any detail in understanding the root cause of this issue. If you want to better understand the root cause, please read below this section.

A common cause of this error is mismatched library versions. The balance between GTK, [Mesa](https://mesa3d.org/), libX11/libwayland, and the kernel is a fragile one.

**The first most common cause of this error is using the Nix development environment to build Ghostty.** We recommend this environment for development, but it does pin various versions of these libraries and they may be incompatible with your global system. **To fix: try to build Ghostty using only system dependency packages, or Ghostty itself from a system package.** You can follow the [build from source](https://ghostty.org/docs/install/build) instructions to do this (but ignore the "Building with Nix" section)

**Another common cause is outdated system packages.** Linux distributions tend to handle this fragile balance for you, so the try to update your entire system (or, specifically the packages above, at least). This often brings your system back into a coherent state that allows Ghostty to work.

**Check your GPU drivers.** Try updating or downgrading your GPU drivers. We've had many cases where GPU driver changes have broken OpenGL in GTK.

- [Mesa 25.2.0 Regression](https://gitlab.freedesktop.org/mesa/mesa/-/issues/13719). Ghostty doesn't bundle a libwayland client library, but building Ghostty from source with the Nix development environment will use a different libwayland client library than the system one.
- [GTK4 + Nvidia + X11](https://gitlab.gnome.org/GNOME/gtk/-/issues/4950). I don't know the exact combination required to trigger this, but it seems in certain scenarios, the mixture of GTK4 (required by Ghostty), Nvidia, and X11 can cause this issue. Changing driver versions or changing to Wayland can resolve this.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/help/gtk-opengl-context.mdx)

- [Quick Fixes](#quick-fixes)
- [Mismatched Library Versions](#mismatched-library-versions)
- [Known Historical Causes](#known-historical-causes)