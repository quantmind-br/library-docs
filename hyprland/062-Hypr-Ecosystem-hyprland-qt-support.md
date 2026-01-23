---
title: hyprland-qt-support
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprland-qt-support/
source: sitemap
fetched_at: 2026-01-22T22:15:55.998712001-03:00
rendered_js: false
word_count: 44
summary: This document explains how to configure the QML style for Hyprland-based Qt6 applications, detailing the available styling variables and configuration file location.
tags:
    - hyprland
    - qt6
    - qml-style
    - configuration
    - ui-customization
    - hyprland-qt-support
category: configuration
---

[hyprland-qt-support](https://github.com/hyprwm/hyprland-qt-support) provides a QML style for hypr* qt6 apps.

## Configuration[](#configuration)

The config file is located in `~/.config/hypr/application-style.conf`.

VariableDescriptionTypeDefault`roundness`How much to round UI elements.int \[0 .. 3]`1``border_width`How wide the border should be around UI elements.int \[0 - 3]`1``reduce_motion`Reduce motion of elements (transitions, hover effects, etc).bool`false`