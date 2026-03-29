---
title: Xcode Tutorial
url: https://github.com/kholia/OSX-KVM/blob/master/Xcode-Tutorial.md
source: git
fetched_at: 2026-02-04T11:38:59.409844499-03:00
rendered_js: false
word_count: 381
summary: This document provides instructions for connecting physical iOS devices to a virtualized macOS environment for development and testing using Xcode. It covers methods for hardware redirection, including USB passthrough and network-based sharing via a Raspberry Pi.
tags:
    - macos-virtualization
    - xcode-development
    - usb-passthrough
    - ios-testing
    - raspberry-pi
    - usb-redirection
category: guide
---

### Developing on Virtualized macOS

1. Install Xcode from the Apple App Store or from the [Apple developer website](https://developers.apple.com).

2. Create an Xcode project as usual.

3. Connect the `Apple Device` (called `iPhone` from now on) to the macOS VM.
   This can be done in two ways:

   Method 1: Use USB passthrough technique to connect an entire USB controller
   (to which `iPhone` is connected) to the macOS VM. This method is covered in
   these [notes](notes.md#usb-passthrough-notes).

   If USB passthrough is not an option, use `Method 2`.

   Method 2. You can use the [USB Network Gate](https://www.eltima.com/products/usb-over-ethernet/)
   software to pass USB devices to macOS VMs over the network (LAN / Wi-Fi).

   ![USB Network Gate - USB over Ethernet Sharing Software](https://www.eltima.com/imgnew/products/usb-over-ethernet/illustrationShare.png)

   This software comes with a free trial and supports a wide variety of
   operating systems. If your operating system is not supported directly, you can
   deploy this software on a Raspberry Pi.

   Once you have it installed on the host computer (the one with the USB device
   that you will be sharing), you can install it on the macOS VM. Make sure to
   allow the extension in `System Preferences > Security & Privacy` and reboot.

   Once that is finished, you can open up `USB Network Gate` on the client
   (macOS VM) and click `Add Server` and type in the IP address of the Raspberry Pi
   or other device (to which the `iPhone` is connected). Finally, you have to
   trust the computer on your `iPhone`, and it should be completely set up!

   At this point, the `iPhone` should work as usual - showing up in
   Finder, Xcode, etc.

4. At this point, the macOS VM has an Xcode project and has access to the
   `iPhone`. Continue using Xcode as usual to build, deploy, and test the Xcode
   project.


### Setup USB Network Gate on Raspberry Pi

These steps were tested on RPi 3B+ running `Raspberry Pi OS with desktop
(August 20th 2020)`.

```
sudo apt update
sudo apt upgrade -y

sudo reboot

sudo apt install raspberrypi-kernel-headers

wget https://cdn.electronic.us/products/usb-over-ethernet/linux/download/eveusb_armv7l.deb

sudo apt install ./eveusb_armv7l.deb
```

To get proper VNC resolution (for headless systems), insert the following lines
in `/boot/config.txt` on the RPi system.

```
dtparam=audio=on  # note: existing line
hdmi_force_hotplug=1
hdmi_group=2
hdmi_mode=82
```

Enable VNC on the RPi system using the `sudo raspi-config nonint do_vnc 0`
command.
