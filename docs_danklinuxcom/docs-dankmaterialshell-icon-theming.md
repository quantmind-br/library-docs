---
title: Icon Theming | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/icon-theming
source: sitemap
fetched_at: 2026-01-24T13:33:39.677478402-03:00
rendered_js: false
word_count: 534
summary: This document provides instructions on configuring and installing icon themes for DankMaterialShell across various Qt6 platform themes including GTK, qt6ct, and KDE.
tags:
    - dankmaterialshell
    - qt6
    - icon-theming
    - linux-customization
    - desktop-theming
    - qt6ct
category: configuration
---

```
██╗ ██████╗ ██████╗ ███╗   ██╗███████╗
██║██╔════╝██╔═══██╗████╗  ██║██╔════╝
██║██║     ██║   ██║██╔██╗ ██║███████╗
██║██║     ██║   ██║██║╚██╗██║╚════██║
██║╚██████╗╚██████╔╝██║ ╚████║███████║
╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
```

DankMaterialShell will use the QT6 icon theme system as primary source for application icons. Depending on which platform theme you're using, icons are configured in different locations.

## How Icon Theming Works[​](#how-icon-theming-works "Direct link to How Icon Theming Works")

Qt6 applications, including DankMaterialShell, look for icon themes based on your `QT_QPA_PLATFORMTHEME` setting. Each platform theme reads icon configuration from a different location:

- **gtk3**: Reads from GTK settings (`~/.config/gtk-3.0/settings.ini`)
- **qt6ct**: Reads from qt6ct configuration (`~/.config/qt6ct/qt6ct.conf`)
- **kde**: Reads from KDE Plasma settings (`~/.config/kdeglobals`)

DMS respects these platform-specific configurations and doesn't override your icon theme choices.

### Environment Variable Override[​](#environment-variable-override "Direct link to Environment Variable Override")

You can also set the icon theme directly using the `QS_ICON_THEME` environment variable:

```
exportQS_ICON_THEME=Papirus-Dark
```

This takes precedence over platform theme settings and is useful for testing or when you want DMS to use a different icon theme than your other Qt applications.

## GTK Platform Theme (gtk3)[​](#gtk-platform-theme-gtk3 "Direct link to GTK Platform Theme (gtk3)")

If you're using the GTK passthrough method for Qt theming, icon themes are controlled via GTK settings.

### Configuration[​](#configuration "Direct link to Configuration")

Edit `~/.config/gtk-3.0/settings.ini`:

```
[Settings]
gtk-icon-theme-name=Papirus-Dark
```

**Common icon themes:**

- `Papirus` / `Papirus-Dark`
- `Adwaita`
- `breeze` / `breeze-dark`
- `Tela`
- `Nordzy`

### Installing Icon Themes[​](#installing-icon-themes "Direct link to Installing Icon Themes")

```
# Arch - Papirus
sudo pacman -S papirus-icon-theme

# Arch - Adwaita (usually pre-installed)
sudo pacman -S adwaita-icon-theme

# Flatpak icon themes (available to all apps)
flatpak install flathub org.kde.PaplirusIconTheme
```

## Qt6ct Platform Theme[​](#qt6ct-platform-theme "Direct link to Qt6ct Platform Theme")

When using qt6ct for dedicated Qt control, icon themes are managed through the qt6ct interface or configuration file.

### Configuration via GUI[​](#configuration-via-gui "Direct link to Configuration via GUI")

1. Launch `qt6ct` from your application launcher
2. Navigate to the **Icon Theme** tab
3. Select your preferred icon theme from the list
4. Click **Apply**

### Configuration via File[​](#configuration-via-file "Direct link to Configuration via File")

Edit `~/.config/qt6ct/qt6ct.conf`:

```
[Appearance]
icon_theme=Papirus-Dark
```

## KDE Platform Theme[​](#kde-platform-theme "Direct link to KDE Platform Theme")

If you're using KDE Plasma or the KDE platform theme, icon themes are managed through KDE's configuration system.

### Configuration via File[​](#configuration-via-file-1 "Direct link to Configuration via File")

Edit `~/.config/kdeglobals`:

```
[Icons]
Theme=Papirus-Dark
```

## Installing Icon Themes[​](#installing-icon-themes-1 "Direct link to Installing Icon Themes")

Icon themes can be installed system-wide or per-user.

### System-wide Installation[​](#system-wide-installation "Direct link to System-wide Installation")

```
# Arch
sudo pacman -S papirus-icon-theme
sudo pacman -S breeze-icons
sudo pacman -S adwaita-icon-theme

# Fedora
sudo dnf install papirus-icon-theme
sudo dnf install breeze-icon-theme
sudo dnf install adwaita-icon-theme
```

### Per-user Installation[​](#per-user-installation "Direct link to Per-user Installation")

Download icon themes and extract to `~/.local/share/icons/`:

```
# Example: Installing from a downloaded archive
mkdir-p ~/.local/share/icons
cd ~/.local/share/icons
tar xf ~/Downloads/Papirus-Dark.tar.gz
```

### Flatpak Icon Themes[​](#flatpak-icon-themes "Direct link to Flatpak Icon Themes")

Flatpak applications use icon themes from the Flatpak runtime:

```
# List available icon theme extensions
flatpak search icon

# Install Papirus for Flatpak apps
flatpak install flathub org.kde.PaplirusIconTheme
```

## Verifying Your Configuration[​](#verifying-your-configuration "Direct link to Verifying Your Configuration")

Check which platform theme you're currently using:

```
echo$QT_QPA_PLATFORMTHEME
```

DankInstall Users

dankinstall sets `QT_QPA_PLATFORMTHEME=gtk3` in `~/.config/environment.d/90-dms.conf`. Check this file to see your current setting.

note

This variable must be exposed to the `dms` process. dankinstall users have this in `~/.config/environment.d/90-dms.conf`. Manual setups typically set it in the compositor config or a custom environment.d file.

Check icon theme for each configuration:

```
# GTK configuration
cat ~/.config/gtk-3.0/settings.ini |grep icon-theme

# qt6ct configuration
cat ~/.config/qt6ct/qt6ct.conf |grep icon_theme

# KDE configuration
cat ~/.config/kdeglobals |grep-A1"\[Icons\]"
```

## Common Icon Theme Recommendations[​](#common-icon-theme-recommendations "Direct link to Common Icon Theme Recommendations")

### Material Design Style[​](#material-design-style "Direct link to Material Design Style")

- **Papirus** / **Papirus-Dark**: Most popular, excellent coverage
- **Tela**: Modern, colorful icons with good app coverage

### Gnome or KDE Style[​](#gnome-or-kde-style "Direct link to Gnome or KDE Style")

- **Adwaita**: GNOME's default, clean and simple
- **breeze**: KDE's default, professional appearance

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Icons not changing[​](#icons-not-changing "Direct link to Icons not changing")

Make sure you've restarted applications after changing icon themes. Qt applications cache icon information and need to be relaunched.

```
# Restart DMS to apply icon theme changes
dms restart
```

### Missing icons[​](#missing-icons "Direct link to Missing icons")

Some applications might show missing icons if the theme doesn't include all required icons. Install a fallback theme:

```
# Arch
sudo pacman -S adwaita-icon-theme hicolor-icon-theme

# Fedora
sudo dnf install adwaita-icon-theme hicolor-icon-theme
```

### Wrong theme being used[​](#wrong-theme-being-used "Direct link to Wrong theme being used")

Verify that your platform theme environment variable matches your configuration:

```
# Check current setting
echo$QT_QPA_PLATFORMTHEME
```

If you change `QT_QPA_PLATFORMTHEME`, you must restart your compositor session for the change to take effect.

### qt6ct shows no themes[​](#qt6ct-shows-no-themes "Direct link to qt6ct shows no themes")

If qt6ct shows an empty icon theme list, check that icon themes are installed in the correct location:

```
# Check system icon themes
ls /usr/share/icons/

# Check user icon themes
ls ~/.local/share/icons/
```

### Flatpak apps using different icons[​](#flatpak-apps-using-different-icons "Direct link to Flatpak apps using different icons")

Flatpak applications run in a sandboxed environment and may not see your system icon themes. Install icon themes via Flatpak:

```
flatpak install flathub org.kde.PaplirusIconTheme
```

## Platform Theme Comparison[​](#platform-theme-comparison "Direct link to Platform Theme Comparison")

FeatureGTK3qt6ctKDE**Configuration File**`~/.config/gtk-3.0/settings.ini``~/.config/qt6ct/qt6ct.conf``~/.config/kdeglobals`**GUI Tool**GNOME Settings, nwg-look`qt6ct`System Settings**Best For**GTK-heavy desktopsMixed Qt/GTKKDE Plasma users**Icon Cache**GTK icon cacheQt icon cacheKDE icon cache

- [Application Theming](https://danklinux.com/docs/dankmaterialshell/application-themes): Configure color themes for GTK and Qt apps
- [Custom Themes](https://danklinux.com/docs/dankmaterialshell/custom-themes): Create custom DMS themes