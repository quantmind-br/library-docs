---
title: Fix Waybar not showing battery or network – Common Solutions - Waybar
url: https://waybar.org/fix-waybar-not-showing-battery-or-network/
source: crawler
fetched_at: 2026-05-11T21:38:48.256039852-03:00
rendered_js: false
word_count: 705
summary: A troubleshooting guide for resolving common configuration issues that cause battery and network modules to fail in the Waybar status bar on Wayland desktops.
tags:
    - waybar
    - wayland
    - linux-troubleshooting
    - battery-module
    - network-module
    - configuration-guide
category: guide
---

Fix Waybar not showing battery or network common solutions is a simple guide for beginners using Waybar on Wayland. Many new users notice that the battery or network indicators sometimes do not appear. This usually happens due to small configuration mistakes or missing services.

In this guide, we explain easy, step-by-step solutions that anyone can follow, even without advanced Linux knowledge. Whether you are using Sway, Hyprland, or other Wayland desktops, this article helps you get your battery and network icons back on Waybar quickly, so you can monitor your system without confusion.

## Check Your Config File

[Waybar](https://waybar.org/) only shows what’s listed in its configuration file. Open your config (usually `~/.config/waybar/config)` and make sure you have:

```
"modules-right": ["battery", "network"]
```

- Check spelling carefully
- Ensure the modules are in the right place
- Even one missing comma can stop Waybar from showing modules

### Verify Battery Name

Waybar needs the correct battery name from your system. Most laptops use `BAT0` or `BAT1`.

Check your battery name with:

```
ls /sys/class/power_supply/
```

**Then update your config like this:**

```
"battery": {
  "bat": "BAT0",
  "adapter": "AC"
}
```

Even small mistakes here can hide the battery icon.

### Make Sure Your Network Is Running

The network module usually works with NetworkManager. Check if it is running:

```
systemctl status NetworkManager
```

- If it’s not running, start it with `systemctl start NetworkManager`
- If you use another network tool, configure it in Waybar accordingly

## Restart Waybar After Changes

After updating configs or fixing services, restart Waybar so changes take effect:

```
pkill waybar && waybar
```

This ensures your icons appear correctly.

### Keep It Simple and Start With Defaults

- Don’t try to change too many things at once
- Begin with the default config
- Tweak one module at a time
- This reduces errors and makes troubleshooting easier

### Optional: Add Some Style

Waybar allows CSS styling, but keep it simple as a beginner:

```
"battery": {
  "format": "{capacity}%"
}
```

You can later customize colors or spacing once you are comfortable.

### Debugging Tips

If something still doesn’t work:

- Run Waybar from terminal:

```
waybar -l info
```

- This will show errors or missing modules
- It helps you quickly identify issues without guessing

## Why These Problems Happen

- Beginner misconfiguration
- Modules missing in config
- Wrong battery name
- NetworkManager not running
- Using unsupported compositor

Most problems are small and easy to fix no advanced [Linux](https://en.wikipedia.org/wiki/Linux) skills required.

### Bonus Tip for Beginners

If you are just starting with Waybar:

- Use ready-made configs from waybar.org
- Compare your setup with working examples
- Tweak one thing at a time and test
- Ask in forums if needed always provide your config snippet

## Frequently Asked Questions

#### Why is Waybar not showing the battery icon?

This usually happens because the battery module is missing from the config file or the battery name is incorrect. Checking your system’s battery name and updating the config fixes the issue in most cases.

#### Why is the network module missing in Waybar?

The network module often depends on NetworkManager. If the service is not running or configured properly, Waybar will not display network information.

#### Do I need advanced Linux knowledge to fix this?

No. Most Waybar battery and network issues are caused by small configuration mistakes. Beginners can fix them by following simple step-by-step solutions.

#### Which Wayland compositors work best with Waybar?

Waybar works best with popular Wayland compositors like Hyprland and Sway. Using unsupported or experimental compositors may cause some modules not to appear.

#### Do I need to restart Waybar after making changes?

Yes. Waybar must be restarted after updating the config or system services so that changes can take effect.

#### Can Waybar work without NetworkManager?

Yes, but you need to configure a different network backend manually. For beginners, using NetworkManager is the easiest and most reliable option.

#### Where can I find beginner-friendly Waybar configs?

You can find simple, ready-to-use Waybar configs and easy guides on waybar.org, designed especially for beginners and Wayland users.

## Conclusion

Waybar not showing the battery or network icon is a common problem, especially for beginners using Wayland for the first time. In most cases, the issue is caused by small configuration mistakes, incorrect battery names, or network services not running properly. The good news is that these problems are usually easy to fix by checking your config file, restarting Waybar, and keeping things simple. You don’t need advanced Linux skills to solve this. By following the step-by-step solutions in this guide, you can quickly restore missing icons and enjoy a clean, functional Waybar setup.