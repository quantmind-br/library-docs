---
title: Waybar Config for Hyprland Beginners (Complete Config File + Examples) - Waybar
url: https://waybar.org/waybar-config-for-hyprland-beginners/
source: crawler
fetched_at: 2026-05-11T21:38:47.549505129-03:00
rendered_js: false
word_count: 821
summary: A beginner-friendly guide to configuring the Waybar status bar for the Hyprland compositor, covering file structure, essential modules, and CSS styling.
tags:
    - waybar
    - hyprland
    - wayland
    - linux-customization
    - desktop-environment
    - css-styling
category: guide
---

Waybar is one of the most popular status bars used with Wayland compositors, especially Hyprland. While Waybar is extremely powerful and customizable, many beginners feel confused when it comes to configuring it properly.

The official documentation mainly focuses on technical details, which can feel overwhelming for new users. This guide is designed to help beginners create a simple and practical Waybar config for Hyprland without dealing with confusing technical details.

## What Is Waybar and Why Use It With Hyprland?

[Waybar](https://waybar.org/) is a highly customizable status bar designed specifically for Wayland compositors. Unlike traditional bars, Waybar uses JSON configuration files and CSS styling, giving you full control over layout and appearance.

**Hyprland users prefer Waybar because it integrates smoothly with:**

- Workspaces
- Window titles
- Keyboard layout
- System resources

Waybar is lightweight, fast, and flexible.  
That makes it an ideal choice for both beginners and advanced users.

### Where Is Waybar Config Located?

Before editing anything, you must know where Waybar stores its configuration files.

**For most systems, the default location is:**

```
~/.config/waybar/
```

**Inside this folder, you usually need two main files:**

- config → controls modules and layout
- style.css → controls colors and styling

If the folder does not exist, you can create it manually.

### Basic Folder Structure for Beginners

A clean folder structure helps avoid confusion.

**Recommended structure:**

```
~/.config/waybar/
├── config
├── style.css
└── scripts/
```

The scripts folder is optional but useful later for custom modules.

## Complete Waybar Config File (Beginner Friendly)

Below is a complete, ready-to-copy Waybar config designed for Hyprland beginners.

You can paste this directly into `~/.config/waybar/config.`

```
{
  "layer": "top",
  "position": "top",
  "height": 32,

  "modules-left": ["hyprland/workspaces"],
  "modules-center": ["clock"],
  "modules-right": ["network", "battery", "cpu", "memory", "tray"],

  "hyprland/workspaces": {
    "disable-scroll": true,
    "all-outputs": true
  },

  "clock": {
    "format": "{:%H:%M}",
    "tooltip-format": "{:%A, %d %B %Y}"
  },

  "network": {
    "format-wifi": "  {signalStrength}%",
    "format-ethernet": "󰈀  Connected",
    "format-disconnected": "  Offline"
  },

  "battery": {
    "format": "{capacity}%",
    "format-charging": " {capacity}%",
    "format-full": "  {capacity}%"
  },

  "cpu": {
    "format": "  {usage}%"
  },

  "memory": {
    "format": "  {used}MB"
  },

  "tray": {
    "spacing": 10
  }
}
```

This config covers everything a beginner usually needs.

## Understanding Each Module (Simple Explanation)

### Workspaces Module

The workspace module shows active and inactive [workspaces](https://en.wikipedia.org/wiki/Workspace) from Hyprland.

Why beginners need it:

- Easy switching between apps
- Visual clarity
- Clean desktop workflow

It automatically syncs with Hyprland.

### Clock Module

The clock module displays time in the center of the bar.

**Benefits:**

- Clean look
- Tooltip shows full date
- Highly customizable format

You can change time format anytime.

### Network Module

The network module shows Wi-Fi or Ethernet status.

For beginners, this is extremely useful because:

- You instantly know connection status
- Signal strength is visible
- Offline warnings prevent confusion

### Battery Module

Laptop users benefit the most from this module.

It shows:

- Battery percentage
- Charging state
- Full battery indicator

You can also add warnings for low battery later.

### CPU and Memory Modules

These modules show real-time system usage.

They help beginners:

- Monitor system performance
- Detect heavy applications
- Learn system behavior

They are lightweight and do not slow down the system.

### System Tray

The tray module shows background apps like:

- Network managers
- Bluetooth
- Notifications

This makes Waybar behave like a traditional desktop bar.

## Styling Waybar Using CSS (Basic Example)

Waybar uses CSS for styling, which is very beginner-friendly.

Paste this into `~/.config/waybar/style.css:`

```
* {
  font-family: JetBrainsMono, monospace;
  font-size: 13px;
}

window#waybar {
  background-color: #1e1e2e;
  color: #cdd6f4;
}

#workspaces button {
  padding: 5px;
  color: #cdd6f4;
}

#workspaces button.active {
  background-color: #89b4fa;
  color: #1e1e2e;
}

#clock, #battery, #network, #cpu, #memory {
  padding: 0 10px;
}
```

This gives you a clean and modern look.

### How to Reload Waybar After Changes

After editing config files, you must reload Waybar.

**Simple method:**

```
pkill waybar && waybar
```

Or restart Hyprland session.

### Common Mistakes Beginners Make

Many beginners face problems due to small mistakes.

**Common issues include:**

- Invalid JSON syntax
- Missing commas
- Wrong file names
- CSS errors

Always double-check brackets and commas.

## Frequently Asked Questions

#### Is Waybar hard to configure for beginners?

No, Waybar is not hard if you start with a simple setup.  
Most problems happen because beginners follow GitHub guides that are too technical.  
If you use a basic config file and make small changes step by step, Waybar becomes very easy to use.

#### Do I need coding skills to use Waybar?

No coding skills are required.  
Waybar uses simple text files for configuration.  
You mainly copy and paste examples and edit small values like time format, modules, or colors.

#### Does Waybar work only with Hyprland?

Waybar works best with Hyprland, but it also supports other Wayland compositors like Sway.  
However, Hyprland users get the smoothest experience and better workspace support.

#### Where is the Waybar config file located?

For most systems, the Waybar config file is located at  
`~/.config/waybar/`

Inside this folder, you usually have:

```
config
style.css
```

#### Why is my Waybar not showing after editing the config?

This usually happens because of a small mistake in the config file, such as:

- Missing a comma
- Extra brackets
- Typing errors

Always double-check your file and restart Waybar after making changes.

#### Can I customize Waybar later?

Yes, absolutely.  
You can start with a basic setup and later:

- Add more modules
- Change colors and fonts
- Use custom scripts

Waybar is very flexible, so you can improve it slowly as you learn.

## Conclusion

Waybar might look confusing at first, but once you understand the basics, it becomes very easy to work with. You do not need advanced knowledge or coding skills to create a clean and useful setup. A simple config file, basic styling, and a few common modules are enough for most users. In this guide, you learned where Waybar config files are located, how to use a beginner-friendly config, and how to avoid common mistakes. This approach is much easier than relying on technical GitHub documentation.