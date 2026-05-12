---
title: What modules come built-in with Waybar?
url: https://waybar.org/what-modules-come-built-in-with-waybar/
source: crawler
fetched_at: 2026-05-11T21:38:48.7517452-03:00
rendered_js: false
word_count: 1639
summary: This document provides an overview of the built-in modules available for the Waybar status bar, explaining how they function and can be configured to monitor system resources, time, and window management.
tags:
    - waybar
    - linux-desktop
    - window-manager
    - system-monitoring
    - desktop-customization
    - ui-configuration
category: guide
---

**Waybar** is a highly customizable, lightweight, and modern status bar designed for Linux window managers like Sway, i3, and Hyprland. Its modular architecture allows users to tailor their desktop experience with a sleek, minimalistic interface that displays system information and controls. Built-in modules are the core components that make **Waybar** a powerful tool, offering functionality ranging from system monitoring to workspace management, all without the need for external plugins. This article explores the built-in modules that come with Waybar, providing a comprehensive guide for users looking to enhance their Linux desktop.

The appeal of Waybar lies in its flexibility and ease of configuration, making it a favorite among Linux enthusiasts who value both aesthetics and functionality. Each module serves a specific purpose, such as displaying battery status, CPU usage, or media controls, and can be customized through simple configuration files. By understanding the full range of built-in modules, users can create a status bar that perfectly suits their workflow, whether for productivity, gaming, or creative tasks.

For those new to Waybar or experienced users seeking to optimize their setup, knowing the available modules is essential. This guide dives into the details of each built-in module, explaining their functionality, customization options, and practical applications. From monitoring system resources to integrating with your favorite tools, Waybar’s modules provide a seamless experience. Let’s explore the built-in modules that make Waybar a standout choice for Linux desktops.

## Core System Monitoring Modules

### CPU Module

The CPU module displays real-time CPU usage, helping users monitor system performance. It shows the percentage of CPU load, which is useful for diagnosing bottlenecks or heavy processes. Configurable through Waybar’s JSON-based configuration, users can adjust the format to display usage per core or as an average. This module supports color changes based on thresholds, making it easy to spot high CPU activity. It’s ideal for developers and power users multitasking on resource-intensive applications.

### Memory Module

The memory module tracks RAM usage, providing insights into system memory consumption. Users can configure it to show total memory, used memory, or free memory in a customizable format. Visual indicators like progress bars or color-coded warnings can highlight memory strain. This module is essential for managing memory-heavy tasks like video editing or virtual machines. It ensures users stay informed about their system’s memory status at a glance.

### Disk Module

The disk module monitors storage usage, displaying available or used space on specified drives. Users can configure it to show specific partitions or mount points, with options for percentage or raw data formats. It supports alerts for low disk space, helping prevent storage-related issues. This module is particularly useful for users managing large files or running servers. It keeps disk usage visible and manageable directly from the status bar.

## Time and Date Modules

[**Waybar**](https://waybar.org/) time and date modules provide essential information with extensive customization options. These modules allow users to display clocks, calendars, and time zones in formats that suit their preferences. They integrate seamlessly with Waybar’s minimalist design, offering both functionality and style. Here are the key sub-modules available:

- **Clock Module**: Displays the current time, configurable for 12 or 24-hour formats.
- **Calendar Module**: Shows the date, with options for custom formats or pop-up calendars.
- **Timezone Module**: Tracks multiple time zones, perfect for remote workers or travelers.

### Clock Module

The clock module shows the current time, supporting various formats like 12-hour or 24-hour displays. Users can customize fonts, colors, and time formats via Waybar’s configuration file. It also supports tooltips for additional details, such as seconds or milliseconds. This module is perfect for users who need a reliable, glanceable time display. It integrates smoothly with other Waybar modules for a cohesive look.

### Calendar Module

The calendar module displays the current date, with options to show day, month, or year in custom formats. Users can enable pop-up calendars for quick date reference or scheduling. It supports localization for different languages and date conventions. This module is ideal for productivity-focused setups, keeping important date information accessible. Customization options ensure it matches the user’s desktop theme.

### Timezone Module

The timezone module allows users to monitor multiple time zones simultaneously. It’s configurable to display specific time zones with custom labels, such as “NYC” or “Tokyo.” Users can set formats to show time differences or full timestamps. This module is invaluable for remote workers collaborating across regions. It ensures time-sensitive tasks are managed efficiently within Waybar’s interface.

## Workspace and Window Management Modules

### Workspaces Module

The workspaces module displays and manages virtual desktops or workspaces in window managers like Sway or i3. Users can switch between workspaces directly from the bar, with icons or labels indicating active workspaces. It supports custom styling for active, inactive, or urgent workspaces. This module enhances productivity by streamlining workspace navigation. It’s a must-have for users managing multiple projects or applications simultaneously.

### Window Module

The window module shows the title or icon of the currently focused window. It’s configurable to display only specific applications or truncate long titles for clarity. Users can customize its appearance to match their desktop theme. This module helps users keep track of active applications in dynamic workflows. It’s particularly useful for multitasking environments with frequent window switches.

### Mode Module

The mode module displays the current mode of the window manager, such as resize or move modes in Sway. It’s customizable to show specific modes with unique icons or text. This module provides quick feedback on window manager states, improving usability. It’s ideal for users who frequently adjust window layouts. The module ensures seamless interaction with window manager functionality.

## Power and Battery Modules

Waybar’s power and battery modules provide critical information for laptop and portable device users. These modules monitor battery status, power consumption, and system power states. They offer customizable alerts and formats to suit different needs. Key sub-modules include:

- **Battery Module**: Tracks battery percentage and charging status.
- **Power Menu Module**: Provides quick access to power options like shutdown or reboot.
- **Backlight Module**: Controls screen brightness directly from the bar.

### Battery Module

The battery module displays the current battery percentage and charging status. Users can set thresholds for low-battery warnings, with visual cues like color changes or icons. It supports multiple batteries for devices with dual-battery systems. This module is crucial for laptop users managing power on the go. Customization ensures it blends seamlessly with Waybar’s aesthetic.

### Power Menu Module

The power menu module offers quick access to system power options, such as shutdown, reboot, or suspend. Users can configure it to show specific commands or integrate with tools like systemd. It supports custom icons or text for each action. This module simplifies system management from the status bar. It’s perfect for users seeking efficient power control.

### Backlight Module

The backlight module allows users to [**monitor**](https://waybar.org/what-is-waybar/) and adjust screen brightness directly from Waybar. It displays the current brightness level as a percentage or slider. Users can configure key bindings for quick adjustments. This module is ideal for optimizing visibility in different lighting conditions. It enhances user comfort during extended desktop sessions.

## Network and Connectivity Modules

Waybar’s network and connectivity modules keep users informed about their internet and device connections. These modules display real-time network status, signal strength, and connection details. They are highly configurable for different network setups. The key sub-modules include:

- **Network Module**: Monitors Wi-Fi and Ethernet connections.
- **Bluetooth Module**: Displays Bluetooth device status and controls.
- **VPN Module**: Tracks VPN connection status and details.

### Network Module

The network module shows the status of Wi-Fi or Ethernet connections, including signal strength and network name. It supports custom formats for displaying upload/download speeds or IP addresses. Users can set alerts for connection drops or weak signals. This module is essential for users relying on stable internet for work or streaming. It ensures network issues are quickly identified.

### Bluetooth Module

The bluetooth module displays connected Bluetooth devices and their status. Users can configure it to show device names, battery levels, or connection states. It supports quick toggles for enabling/disabling Bluetooth. This module is perfect for users with wireless peripherals like headphones or keyboards. It simplifies Bluetooth management within Waybar’s interface.

### VPN Module

The VPN module monitors active VPN connections, displaying connection status or server details. It’s configurable to show specific VPN protocols or connection times. Users can set custom icons for connected or disconnected states. This module is vital for privacy-conscious users or those working remotely. It keeps VPN status visible and accessible.

## Media and Audio Modules

### Mpris Module

The mpris module integrates with media players supporting the MPRIS protocol, such as Spotify or VLC. It displays track information, playback status, and control buttons for play, pause, or skip. Users can customize the layout to show artist names or album art. This module enhances media workflows by providing direct control from Waybar. It’s ideal for music enthusiasts or multitaskers.

### Pulseaudio Module

The pulseaudio module monitors and controls audio output and input devices. It displays the current volume level and mute status, with options for sliders or percentage displays. Users can configure key bindings for volume adjustments. This module is essential for managing audio during calls or media playback. It ensures seamless audio control within the status bar.

### Idle Inhibitor Module

The idle inhibitor module displays the status of idle prevention, useful for keeping the screen active during presentations or video playback. It supports toggles to enable or disable idle inhibition. Users can customize its appearance with icons or text. This module is perfect for users needing uninterrupted screen activity. It integrates smoothly with Waybar’s functionality.

## Conclusion

Waybar’s built-in modules offer a robust set of tools for Linux users, blending functionality with customization. From system monitoring to media controls, these modules cater to diverse needs, enhancing desktop efficiency. Their flexibility allows users to craft a status bar that aligns with their workflow and aesthetic preferences. By leveraging Waybar’s modules, users can create a tailored, powerful desktop experience that elevates productivity and system awareness.