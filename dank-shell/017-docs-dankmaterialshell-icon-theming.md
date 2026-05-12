---
title: Icon Theming | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/icon-theming
source: sitemap
fetched_at: 2026-04-26T08:39:01.622330631-03:00
rendered_js: false
word_count: 648
summary: This guide explains how to configure and manage icon themes for DankMaterialShell applications by integrating with Qt6 platform themes like GTK, qt6ct, and KDE.
tags:
    - dankmaterialshell
    - qt6
    - icon-themes
    - theming
    - linux-desktop
    - customization
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Version: 1.4

DankMaterialShell uses the Qt6 icon theme system as the primary source for application icons. Icon themes are configured differently depending on your platform theme.

## How Icon Theming Works

Qt6 applications look for icon themes based on your `QT_QPA_PLATFORMTHEME` setting:

- **gtk3**: Reads from GTK settings (`~/.config/gtk-3.0/settings.ini`)
- **qt6ct**: Reads from qt6ct configuration (`~/.config/qt6ct/qt6ct.conf`)
- **kde**: Reads from KDE Plasma settings (`~/.config/kdeglobals`)

### Environment Variable Override

Set the icon theme directly using `QS_ICON_THEME`:

```bash
export QS_ICON_THEME=Papirus-Dark
```

This takes precedence over platform theme settings.

## GTK Platform Theme (gtk3)

If using GTK passthrough for Qt theming, icon themes are controlled via GTK settings.

Edit `~/.config/gtk-3.0/settings.ini`:

```ini
[Settings]
gtk-icon-theme-name=Papirus-Dark
```

**Common icon themes:** Papirus, Papirus-Dark, Adwaita, breeze, breeze-dark, Tela, Nordzy

**Installing Icon Themes:**

```bash
# Arch - Papirus
sudo pacman -S papirus-icon-theme
# Arch - Adwaita
sudo pacman -S adwaita-icon-theme
# Flatpak icon themes
flatpak install flathub org.kde.PaplirusIconTheme
```

## Qt6ct Platform Theme

When using qt6ct for dedicated Qt control, icon themes are managed through the qt6ct interface or configuration file.

### Configuration via GUI

1. Launch `qt6ct` from your application launcher
2. Navigate to the **Icon Theme** tab
3. Select your preferred icon theme
4. Click **Apply**

### Configuration via File

Edit `~/.config/qt6ct/qt6ct.conf`:

```ini
[Appearance]
icon_theme=Papirus-Dark
```

## KDE Platform Theme

If using KDE Plasma or the KDE platform theme, icon themes are managed through KDE's configuration system.

Edit `~/.config/kdeglobals`:

```ini
[Icons]
Theme=Papirus-Dark
```

## Installing Icon Themes

### System-wide Installation

```bash
# Arch
sudo pacman -S papirus-icon-theme breeze-icons adwaita-icon-theme
# Fedora
sudo dnf install papirus-icon-theme breeze-icon-theme adwaita-icon-theme
```

### Per-user Installation

Download icon themes and extract to `~/.local/share/icons/`:

```bash
mkdir -p ~/.local/share/icons
cd ~/.local/share/icons
tar xf ~/Downloads/Papirus-Dark.tar.gz
```

### Flatpak Icon Themes

```bash
# List available icon theme extensions
flatpak search icon
# Install Papirus for Flatpak apps
flatpak install flathub org.kde.PaplirusIconTheme
```

## Verifying Your Configuration

Check which platform theme you're currently using:

```bash
echo $QT_QPA_PLATFORMTHEME
```

> [!tip]
> DankInstall users: `QT_QPA_PLATFORMTHEME=gtk3` is set in `~/.config/environment.d/90-dms.conf`. Override per-service with `systemctl --user edit dms`.

> [!note]
> This variable must be exposed to the `dms` process. Manual setups typically set it in the compositor config, a custom environment.d file, or via `systemctl --user edit dms`.

Verify icon theme for each configuration:

```bash
# GTK configuration
cat ~/.config/gtk-3.0/settings.ini | grep icon-theme
# qt6ct configuration
cat ~/.config/qt6ct/qt6ct.conf | grep icon_theme
# KDE configuration
cat ~/.config/kdeglobals | grep -A1 "\[Icons\]"
```

## Common Icon Theme Recommendations

**Material Design Style:** Papirus / Papirus-Dark (most popular, excellent coverage), Tela (modern, colorful)

**Gnome or KDE Style:** Adwaita (GNOME's default, clean), breeze (KDE's default, professional)

## Troubleshooting

### Icons not changing

Qt applications cache icon information and need to be relaunched:

```bash
dms restart
```

### Missing icons

Install a fallback theme:

```bash
# Arch
sudo pacman -S adwaita-icon-theme hicolor-icon-theme
# Fedora
sudo dnf install adwaita-icon-theme hicolor-icon-theme
```

### Wrong theme being used

Verify that your platform theme environment variable matches your configuration:

```bash
echo $QT_QPA_PLATFORMTHEME
```

If you change `QT_QPA_PLATFORMTHEME`, restart your compositor session.

### qt6ct shows no themes

Check that icon themes are installed in the correct location:

```bash
ls /usr/share/icons/
ls ~/.local/share/icons/
```

### Flatpak apps using different icons

Install icon themes via Flatpak:

```bash
flatpak install flathub org.kde.PaplirusIconTheme
```

## Platform Theme Comparison

| Feature | GTK3 | qt6ct | KDE |
|---------|------|-------|-----|
| **Configuration File** | `~/.config/gtk-3.0/settings.ini` | `~/.config/qt6ct/qt6ct.conf` | `~/.config/kdeglobals` |
| **GUI Tool** | GNOME Settings, nwg-look | `qt6ct` | System Settings |
| **Best For** | GTK-heavy desktops | Mixed Qt/GTK | KDE Plasma users |
| **Icon Cache** | GTK icon cache | Qt icon cache | KDE icon cache |

## Related Documentation

- [[062-docs-dankmaterialshell-application-themes|Application Theming]] - Configure color themes for GTK and Qt apps
- [[016-docs-dankmaterialshell-custom-themes|Custom Themes]] - Create custom DMS themes
