---
title: How to Install Waybar on Hyprland (Step-by-Step Guide) - Waybar
url: https://waybar.org/install-waybar-on-hyprland/
source: crawler
fetched_at: 2026-05-11T21:38:47.388603742-03:00
rendered_js: false
word_count: 655
summary: A comprehensive, beginner-friendly guide on installing, configuring, and auto-starting the Waybar status bar within the Hyprland Wayland compositor.
tags:
    - waybar
    - hyprland
    - wayland
    - linux-customization
    - arch-linux
    - desktop-environment
category: guide
---

Waybar is one of the most popular and customizable status bars for Wayland compositors, especially Hyprland. If you are new to Hyprland, setting up Waybar correctly can feel confusing at first. Many users install Hyprland but struggle to get Waybar running or visible on the screen.

This step-by-step guide will show you how to install Waybar on Hyprland properly, start it without errors, and avoid common beginner mistakes. Whether you are using Arch Linux or an Arch-based distro, this guide is written in a simple, beginner-friendly way so you can get Waybar working smoothly.

## What Is Waybar and Why Use It With Hyprland?

Waybar is a highly customizable status bar designed for Wayland. It displays useful system information like:

- Battery status
- Network connection
- Volume
- Clock and date
- Workspaces

Hyprland works perfectly with Waybar, making it the preferred choice for most Hyprland users.

### Step 1: Make Sure Hyprland Is Installed

Before [installing Wayba](https://waybar.org/how-to-install-waybar-on-arch-linux/)r, Hyprland must already be installed and working.

**You should be able to:**

- Log into Hyprland
- See your desktop environment
- Open a terminal

If Hyprland is running properly, you are ready to continue.

### Step 2: Install Waybar on Arch Linux

On Arch Linux or Arch-based systems, install Waybar using pacman:

```
sudo pacman -S waybar
```

This will install Waybar and all required dependencies.

### Step 3: Install Required Fonts (Very Important)

Many users think Waybar is broken when icons do not appear. This usually happens because fonts are missing.

**Install Nerd Fonts:**

```
sudo pacman -S ttf-jetbrains-mono-nerd
```

You can also install Symbols Nerd Font for better icon support.

After installing fonts, log out and log back in.

### Step 4: Create Waybar Config Files

Waybar will not show anything until configuration files exist.

**Create the config directory:**

```
mkdir -p ~/.config/waybar
```

**Create basic config files:**

```
touch ~/.config/waybar/config
touch ~/.config/waybar/style.css
```

Waybar will now know where to load its configuration from.

### Step 5: Start Waybar Manually

Before auto-starting Waybar, test it manually.

**Run:**

```
waybar
```

If Waybar appears at the top of your screen, it means installation was successful.

**If it does not appear, check logs:**

```
waybar -l trace
```

### Step 6: Auto-Start Waybar With Hyprland

To start Waybar automatically every time Hyprland launches, edit your Hyprland config file:

```
~/.config/hypr/hyprland.conf
```

**Add this line:**

```
exec-once = waybar
```

Save the file and restart Hyprland.

### Step 7: Common Problems and Quick Fixes

**Waybar not showing at all**

- Make sure Waybar is installed
- Run `waybar` manually to test
- Check for errors in logs

**Icons not showing**

- Install Nerd Fonts
- Set correct font in `style.css`
- Restart Waybar

**Waybar crashes on startup**

- Check syntax errors in config
- Remove custom modules temporarily
- Test with a minimal config

## Frequently Asked Questions

#### Can I install Waybar on Hyprland as a beginner?

Yes. This guide is designed for beginners and provides step-by-step instructions to install and start Waybar on Hyprland.

#### Do I need a specific Linux distribution to install Waybar?

Waybar works best on Arch Linux or Arch-based distros, but it can also be installed on other distributions with Wayland support.

#### Why is Waybar not showing after installation?

Common reasons include missing fonts, incorrect config paths, or not starting Waybar properly with Hyprland.

#### Do I need Nerd Fonts for Waybar to display icons?

Yes. Installing Nerd Fonts ensures all icons display correctly in your Waybar modules.

#### How do I auto-start Waybar with Hyprland?

Add the line exec-once = waybar in your Hyprland configuration file (~/.config/hypr/hyprland.conf).

#### Can Waybar configuration updates break my setup?

Yes, sometimes updates may affect configs. Always keep backups of your Waybar config files.

#### Can I customize Waybar after installation?

Absolutely. Once installed, you can modify modules, fonts, colors, and icons without breaking the setup if you follow proper steps.

## Conclusion

Installing Waybar on Hyprland is simple when you follow the correct steps. Most problems beginners face are caused by missing fonts, configuration errors, or not starting Waybar properly. By installing Nerd Fonts, setting up the config correctly, and adding Waybar to your Hyprland auto-start, you can enjoy a fully functional and customizable status bar. This guide ensures beginners can get Waybar running quickly and safely, laying the foundation for further customization and optimization.