---
title: How to install Waybar on Arch Linux (step by step) - Waybar
url: https://waybar.org/how-to-install-waybar-on-arch-linux/
source: crawler
fetched_at: 2026-05-11T21:38:48.751157906-03:00
rendered_js: false
word_count: 734
summary: This document provides a comprehensive guide for installing and configuring the Waybar status bar on Arch Linux systems running Wayland.
tags:
    - arch-linux
    - waybar
    - wayland
    - linux-customization
    - status-bar
    - hyprland
    - sway
    - desktop-environment
category: guide
---

Waybar is a modern, lightweight status bar designed specifically for Wayland-based Linux desktops. It has become very popular among Arch Linux users because it works perfectly with minimal and highly customizable setups like Hyprland and Sway. If you are new to Wayland or switching from X11, installing Waybar correctly is an important first step.

This step-by-step guide shows how to install Waybar on Arch Linux, explains basic requirements, and helps beginners avoid common mistakes. By the end of this guide, you will have Waybar installed, running, and ready for customization on your Wayland system.

## What You Need Before Installing Waybar

**Before installing Waybar, make sure:**

- You are using Arch Linux (or Arch-based distro)
- You are logged into a Wayland session
- You already have a Wayland compositor installed

**Common supported compositors:**

- Hyprland
- Sway
- Wayfire

If you are on X11 (for example i3 without Wayland), Waybar will not work.

**Read More:** [**Waybar Config for Hyprland Beginners (Complete Config File + Examples)**](https://waybar.org/waybar-config-for-hyprland-beginners/)

### Step 1: Update Your Arch Linux System

Always start by updating your system to avoid dependency issues:

```
sudo pacman -Syu
```

This ensures you get the latest and most stable Waybar package.

### Step 2: Install Waybar Using Pacman

Waybar is available in the official [Arch](https://en.wikipedia.org/wiki/Arch_Linux) repositories, so installation is easy:

```
sudo pacman -S waybar
```

Pacman will automatically install all required dependencies.

### Step 3: Verify Waybar Installation

After installation, check if Waybar is installed correctly:

```
waybar
```

If Waybar appears on your screen, the installation was successful.

### Step 4: Create Waybar Config Directory

Waybar looks for user configs in this location:

```
~/.config/waybar/
```

Create the folder if it doesn’t exist:

```
mkdir -p ~/.config/waybar
```

### Step 5: Copy Default Config Files

For beginners, starting with default files is the best option:

```
cp /etc/xdg/waybar/config ~/.config/waybar/
cp /etc/xdg/waybar/style.css ~/.config/waybar/
```

These files give you a working bar that you can customize later.

### Step 6: Start Waybar Automatically on Login

To avoid launching Waybar manually every time, add it to your compositor config.

###### **Example for Hyprland:**

```
exec-once = waybar
```

###### **Example for Sway:**

```
exec waybar
```

Now Waybar will start automatically when you log in.

### Step 7: Basic Customization for Beginners

You don’t need advanced skills to customize Waybar.

**Simple examples:**

- Move modules left or right
- Change font size
- Show battery percentage
- Display network status

Make small changes and restart Waybar to see results:

```
pkill waybar && waybar
```

### Step 8: Common Installation Issues and Fixes

**Waybar command not found?**

- Make sure installation completed successfully
- Run which waybar to confirm path

**Waybar starts but shows nothing?**

- Check config file syntax
- Make sure modules are defined correctly

**Battery or network missing?**

- Check module names
- Ensure NetworkManager is running

These are configuration issues, not installation problems.

### Step 9: Why Waybar Is Perfect for Arch Linux

- Official repository support
- Fast updates
- Minimal and lightweight
- Designed for modern Wayland desktops
- Easy to customize over time

Waybar matches Arch Linux’s “build it yourself” philosophy.

### What to Do After Installing Waybar

Once Waybar is installed, you can:

- Add custom modules
- Apply themes
- Optimize performance
- Fix missing icons
- Explore advanced configs

Beginners should start simple and learn step by step.

## Frequently Asked Questions

#### Does Waybar work on X11 window managers?

No. Waybar only works on Wayland. If you are using X11 window managers like i3 (without Wayland), Waybar will not work.

#### Which Wayland compositor is best for Waybar on Arch Linux?

Waybar works best with Hyprland and Sway. These compositors are stable and widely used with Waybar.

#### Do I need to install Waybar from AUR?

No. Waybar is available in the official Arch Linux repositories, so you can install it easily using pacman.

#### Why does Waybar not start after installation?

This usually happens if you are not running a Wayland session or if Waybar is not added to your compositor’s startup configuration.

#### Where is the Waybar config file located?

The user config files are usually located at:  
`~/.config/waybar/`

#### Can beginners customize Waybar easily?

Yes. Beginners can start with the default config and make small changes step by step without advanced Linux knowledge.

#### Is Waybar lightweight and suitable for daily use?

Yes. Waybar is lightweight, fast, and works smoothly on most Arch Linux systems running Wayland.

## Conclusion

Installing Waybar on Arch Linux is simple and beginner-friendly when you follow the correct steps. Most users face issues not because of installation errors, but due to missing configs or running the wrong display server. Once installed, Waybar provides a clean, modern, and customizable status bar that fits perfectly with Wayland-based setups like Hyprland and Sway. By starting with default settings and making small changes over time, you can build a powerful and stable desktop experience.