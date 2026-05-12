---
title: Configuration | Dank Linux
url: https://danklinux.com/docs/dankgreeter/configuration
source: docs
fetched_at: 2026-04-26T08:38:19.629388828-03:00
rendered_js: false
word_count: 719
summary: This document provides instructions for configuring custom compositors for the DMS greeter and explains how to synchronize greeter themes, wallpapers, and settings with a user's environment.
tags:
    - dms-greeter
    - compositor-configuration
    - theme-sync
    - system-administration
    - linux-login
    - display-manager
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Custom Compositor Configuration

> [!tip]
> Custom compositor configurations allow you to configure displays (resolution, refresh rate, position, etc.) specifically for the greeter.

### niri

1. Create a baseline configuration file at `/etc/greetd/niri.kdl`:

```bash
sudotee /etc/greetd/niri.kdl > /dev/null <<'EOF'
hotkey-overlay {
    skip-at-startup
}
environment {
    DMS_RUN_GREETER "1"
}
gestures {
  hot-corners {
    off
  }
}
layout {
  background-color "#000000"
}
EOF
```

2. Update the command in `/etc/greetd/config.toml` to use this configuration:

```toml
command="dms-greeter --command niri -C /etc/greetd/niri.kdl"
```

3. Edit `/etc/greetd/niri.kdl` however you see fit, the greeter will run under this compositor configuration.

### Hyprland

1. Create a baseline configuration file at `/etc/greetd/hypr.conf`:

```bash
sudotee /etc/greetd/hypr.conf > /dev/null <<'EOF'
env = DMS_RUN_GREETER,1
misc {
    disable_hyprland_logo = true
}
EOF
```

2. Update the command in `/etc/greetd/config.toml` to use this configuration:

```toml
command="dms-greeter --command hyprland -C /etc/greetd/hypr.conf"
```

3. Edit `/etc/greetd/hypr.conf` however you see fit, the greeter will run under this compositor configuration.

### Sway

1. Create a baseline configuration file at `/etc/greetd/sway`:

```bash
sudotee /etc/greetd/sway > /dev/null <<'EOF'
# Sway greeter configuration
# The exec command to launch the greeter is automatically appended by dms-greeter
EOF
```

2. Update the command in `/etc/greetd/config.toml` to use this configuration:

```toml
command="dms-greeter --command sway -C /etc/greetd/sway"
```

3. Edit `/etc/greetd/sway` however you see fit, the greeter will run under this compositor configuration.

### Mango

1. Create a baseline configuration file at `/etc/greetd/mango.conf`:

```bash
sudotee /etc/greetd/mango.conf > /dev/null <<'EOF'
# Mango greeter configuration
EOF
```

2. Update the command in `/etc/greetd/config.toml` to use this configuration:

```toml
command="dms-greeter --command mango -C /etc/greetd/mango.conf"
```

3. Edit `/etc/greetd/mango.conf` however you see fit, the greeter will run under this compositor configuration.

### Miracle WM

1. Create a baseline configuration file at `/etc/greetd/miracle-wm.yaml`:

```bash
sudotee /etc/greetd/miracle-wm.yaml > /dev/null <<'EOF'
# Miracle WM greeter configuration
EOF
```

2. Update the command in `/etc/greetd/config.toml` to use this configuration:

```toml
command="dms-greeter --command miracle-wm -C /etc/greetd/miracle-wm.yaml"
```

3. Edit `/etc/greetd/miracle-wm.yaml` however you see fit, the greeter will run under this compositor configuration.

## Syncing with DMS

Automatically sync the system greeter with the logged in user's wallpaper, themes, fonts, and settings.

### Automatic Sync

Use `dms greeter sync` to set up theme syncing. Available for:

- dankinstall users
- Arch AUR users
- Fedora COPR users

> [!note]
> **NixOS users:** `dms greeter sync` is not available on NixOS. Follow the manual sync steps below.

This will:

- Add your user to the `greeter` group (if needed)
- Set up ACL permissions on parent directories for greeter access
- Configure group permissions on DMS config directories
- Create symlinks to sync settings, wallpapers, and color themes

> [!note]
> After running `dms greeter sync`, log out and log back in for group membership changes to take effect.

### Manual Sync

1. Add your user to the `greeter` group:

```bash
sudo usermod -aG greeter <username>
```

2. Set up ACL permissions on parent directories:

```bash
setfacl -m u:greeter:x ~
setfacl -m u:greeter:x ~/.config
setfacl -m u:greeter:x ~/.local
setfacl -m u:greeter:x ~/.cache
setfacl -m u:greeter:x ~/.local/state
```

3. Set group permissions on DMS config directories:

```bash
sudo chgrp -R greeter ~/.config/DankMaterialShell
sudo chmod -R g+rX ~/.config/DankMaterialShell
sudo chgrp -R greeter ~/.local/state/DankMaterialShell
sudo chmod -R g+rX ~/.local/state/DankMaterialShell
sudo chgrp -R greeter ~/.cache/quickshell
sudo chmod -R g+rX ~/.cache/quickshell
```

4. Create configuration symlinks:

```bash
sudo ln -sf ~/.config/DankMaterialShell/settings.json /var/cache/dms-greeter/settings.json
sudo ln -sf ~/.local/state/DankMaterialShell/session.json /var/cache/dms-greeter/session.json
sudo ln -sf ~/.cache/quickshell/dankshell/dms-colors.json /var/cache/dms-greeter/colors.json
```

> [!note]
> Log out or reboot for group change to take effect.

### Checking Sync Status

Run `dms greeter status` to verify greeter configuration and sync status. Available for all users. Checks:

- Group membership (`greeter` group)
- Cache directory existence
- Configuration symlinks (settings, wallpaper, colors)
- Source file readability

#### Example Output

```text
=== DMS Greeter Status ===
Group Membership:
  ✓ User is in greeter group
Greeter Cache Directory:
  ✓ /var/cache/dms-greeter exists
Configuration Symlinks:
  ✓ Settings: synced correctly
  ✓ Session state: synced correctly
  ✓ Color theme: synced correctly
✓ All checks passed! Greeter is properly configured.
```

### Troubleshooting

If `dms greeter status` shows issues:

- **User not in greeter group**: Run `dms greeter sync`, then log out and back in
- **Symlinks missing or broken**: Re-run `dms greeter sync`
- **ACL permission issues**: Check with `getfacl ~ ~/.config ~/.local ~/.cache ~/.local/state | grep "user:greeter"`, then re-run sync if needed

## Manual Configuration

The greeter uses three main configuration files in `/var/cache/dms-greeter/` (or custom `DMS_GREET_CFG_DIR`):

| File | Purpose |
|---|---|
| `settings.json` | Appearance, behavior, and widget settings |
| `session.json` | Wallpaper configuration |
| `colors.json` | Color scheme configuration |

> [!note]
> These files are read-only by the greeter, not written or updated.

### Colors

Configure colors the same way as described in [[016-docs-dankmaterialshell-custom-themes|DankMaterialShell Custom Themes]].

### Settings

`settings.json` controls the greeter's appearance and behavior.

#### Clock & Time

```json
{
"use24HourClock":true,
"showSeconds":false,
"lockDateFormat":""
}
```

| Key | Default | Description |
|---|---|---|
| `use24HourClock` | `true` | Use 24-hour format (`true`) or 12-hour format (`false`) |
| `showSeconds` | `false` | Display seconds in the clock |
| `lockDateFormat` | `""` | Custom Qt date format string (empty = `Locale.LongFormat`) |

#### Weather

```json
{
"weatherEnabled":true,
"weatherLocation":"New York, NY",
"weatherCoordinates":"40.7128,-74.0060",
"useAutoLocation":false,
"useFahrenheit":false
}
```

| Key | Default | Description |
|---|---|---|
| `weatherEnabled` | `true` | Show weather widget in top-right |
| `weatherLocation` | (none) | Display name for location |
| `weatherCoordinates` | (none) | `"latitude,longitude"` string |
| `useAutoLocation` | `false` | Auto-detect location via IP geolocation |
| `useFahrenheit` | `false` | Use Fahrenheit (`true`) or Celsius (`false`) |

#### Appearance

```json
{
"currentThemeName":"blue",
"customThemeFile":"",
"matugenScheme":"scheme-tonal-spot",
"iconTheme":"System Default",
"fontFamily":"Inter Variable",
"fontWeight":400,
"fontScale":1.0,
"cornerRadius":12,
"widgetBackgroundColor":"sch",
"surfaceBase":"s",
"animationSpeed":2
}
```

| Key | Default | Description |
|---|---|---|
| `currentThemeName` | `"blue"` | Built-in theme name (`"blue"`, `"red"`, `"green"`, etc.) |
| `customThemeFile` | `""` | Path to custom matugen JSON theme file |
| `matugenScheme` | `"scheme-tonal-spot"` | Matugen color scheme variant |
| `iconTheme` | `"System Default"` | Icon theme name for DankIcon fallbacks |
| `fontFamily` | `"Inter Variable"` | Primary font family |
| `fontWeight` | `400` | Font weight (`400` = normal, `700` = bold) |
| `fontScale` | `1.0` | Font size multiplier |
| `cornerRadius` | `12` | Corner radius in pixels for UI elements |
| `widgetBackgroundColor` | `"sch"` | Widget background scheme (`"sch"`, `"s"`, `"sv"`) |
| `surfaceBase` | `"s"` | Surface base color scheme (`"s"`, `"sv"`, `"sb"`) |
| `animationSpeed` | `2` | Animation speed (`0` = fastest, `4` = slowest) |

#### Complete Example

`/var/cache/dms-greeter/settings.json`:

```json
{
"use24HourClock":true,
"showSeconds":false,
"lockDateFormat":"",
"lockScreenShowPowerActions":true,
"useFahrenheit":false,
"weatherLocation":"New York, NY",
"weatherCoordinates":"40.7128,-74.0060",
"useAutoLocation":false,
"weatherEnabled":true,
"currentThemeName":"blue",
"customThemeFile":"",
"matugenScheme":"scheme-tonal-spot",
"nightModeEnabled":false,
"iconTheme":"System Default",
"fontFamily":"Inter Variable",
"fontWeight":400,
"fontScale":1.0,
"cornerRadius":12,
"widgetBackgroundColor":"sch",
"surfaceBase":"s",
"animationSpeed":2
}
```

### Wallpapers

`session.json` controls wallpaper settings.

#### Basic Configuration

```json
{
"wallpaperPath":"/path/to/wallpaper.jpg",
"wallpaperFillMode":"PreserveAspectCrop"
}
```

| Key | Default | Description |
|---|---|---|
| `wallpaperPath` | (none) | Default wallpaper for all monitors |
| `wallpaperFillMode` | `"PreserveAspectCrop"` | Qt fill mode |

Fill modes:

- `"PreserveAspectCrop"` — Crop to fill (default)
- `"PreserveAspectFit"` — Fit within bounds
- `"Stretch"` — Stretch to fill

#### Per-Monitor Wallpapers

```json
{
"wallpaperPath":"/path/to/default.jpg",
"wallpaperFillMode":"PreserveAspectCrop",
"monitorWallpapers":{
"DP-1":"/path/to/monitor1-wallpaper.jpg",
"DP-2":"/path/to/monitor2-wallpaper.jpg",
"HDMI-A-1":"#1a1a1a"
}
}
```

| Key | Description |
|---|---|
| `monitorWallpapers` | Per-monitor wallpaper overrides |

Monitor names come from `niri msg outputs` or `hyprctl monitors`. Value formats:

- File paths: `/path/to/image.jpg`
- Solid colors: `#RRGGBB` format
- Wallpaper Engine: `we:workshop_id` format

#### Complete Example

`/var/cache/dms-greeter/session.json`:

```json
{
"wallpaperPath":"/usr/share/backgrounds/default.jpg",
"wallpaperFillMode":"PreserveAspectCrop",
"monitorWallpapers":{
"DP-1":"/home/user/Pictures/wallpaper-main.png",
"DP-2":"#2e3440",
"HDMI-A-1":"/home/user/Pictures/wallpaper-side.jpg"
}
}
```

#dms-greeter #compositor-configuration #theme-sync #system-administration
