---
title: Application Theming | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/application-themes
source: sitemap
fetched_at: 2026-04-26T08:38:33.81530567-03:00
rendered_js: false
word_count: 1138
summary: This document explains how to configure and customize DankMaterialShell's automatic theme generation for native applications using the matugen engine, including instructions for custom templates and integration with GTK and Qt applications.
tags:
    - dankmaterialshell
    - matugen
    - theming
    - linux-customization
    - gtk-integration
    - qt-integration
    - configuration
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Application Theming

Version: 1.4

DankMaterialShell automatically generates theme files for native applications when matugen is enabled. Files are created on wallpaper changes and theme switches.

## Disabling Matugen

Set `DMS_DISABLE_MATUGEN=1` or `true` before launching to disable theme generation entirely.

## Custom Matugen Templates

Add custom matugen templates to theme additional applications. Templates must use absolute paths under `[config]`. DMS executes these alongside built-in templates.

See the [matugen wiki](https://github.com/InioX/matugen/wiki/Configuration) for full configuration and templating options.

Create or edit `~/.config/matugen/config.toml`:

```toml
[config]
[templates.mytemplate]
input_path='/home/username/.config/matugen/templates/mytemplate.toml'
output_path='/home/username/.local/share/mytemplate/themes/matugen.toml'

[templates.myapp]
input_path='/home/username/.config/matugen/templates/myapp.conf'
output_path='/home/username/.config/myapp/colors.conf'
```

### Available Template Variables

Templates have access to all standard [matugen color keywords](https://github.com/InioX/matugen/wiki/Configuration#colors), plus the full `dank16` palette for terminal and editor theming.

#### dank16 Color Structure

dank16 colors use a variant structure matching the material color system:

```
{{dank16.color0.default.hex}}
{{dank16.color0.dark.hex}}
{{dank16.color0.light.hex}}
```

| Variant | Use Case |
|---|---|
| `.default` | Mode-aware colors (recommended) |
| `.dark` | Always dark, regardless of system mode |
| `.light` | Always light, regardless of system mode |

Each variant includes `hex` and `hex_stripped` values.

#### Terminal Templates

Use `.default` variants for terminal templates. The **Terminals - Always use Dark Theme** setting automatically substitutes `.default` with `.dark` at build time for kitty, alacritty, ghostty, foot, wezterm.

Example kitty template using both matugen colors and dank16:

```text
cursor                {{colors.on_surface.default.hex}}
cursor_text_color     {{colors.on_surface_variant.default.hex}}
foreground            {{colors.on_surface.default.hex}}
background            {{colors.background.default.hex}}
selection_foreground  {{colors.on_secondary.default.hex}}
selection_background  {{colors.secondary_fixed_dim.default.hex}}
url_color             {{colors.primary.default.hex}}
color0   {{dank16.color0.default.hex}}
color1   {{dank16.color1.default.hex}}
color2   {{dank16.color2.default.hex}}
color3   {{dank16.color3.default.hex}}
color4   {{dank16.color4.default.hex}}
color5   {{dank16.color5.default.hex}}
color6   {{dank16.color6.default.hex}}
color7   {{dank16.color7.default.hex}}
color8   {{dank16.color8.default.hex}}
color9   {{dank16.color9.default.hex}}
color10  {{dank16.color10.default.hex}}
color11  {{dank16.color11.default.hex}}
color12  {{dank16.color12.default.hex}}
color13  {{dank16.color13.default.hex}}
color14  {{dank16.color14.default.hex}}
color15  {{dank16.color15.default.hex}}
```

#### Migration

Update custom matugen templates from the old format:

```diff
- {{dank16.color0.hex}}
+ {{dank16.color0.default.hex}}
```

> [!warning]
> - Use absolute paths, not relative paths like `./templates/`
> - All template definitions must be under the `[config]` section
> - Templates regenerate on wallpaper changes and theme switches

## Generated Files

When matugen is enabled, theme files are always generated regardless of the "Apply GTK/Qt Themes" toggle:

- `~/.config/gtk-3.0/dank-colors.css`
- `~/.config/gtk-4.0/dank-colors.css`
- `~/.config/qt5ct/colors/matugen.conf`
- `~/.config/qt6ct/colors/matugen.conf`

The "Apply GTK/Qt Themes" toggles only control whether DMS manages the symlinks.

## GTK Applications

### Install Prerequisites

```bash
# Arch
sudo pacman -S adw-gtk-theme
# Fedora
sudo dnf install adw-gtk3-theme
```

### Enable via Settings

1. Open **Settings > Theme & Colors**
2. Toggle **Apply GTK Themes**

This creates symlinks from `dank-colors.css` to `gtk.css`, enabling dynamic theming for GTK 3 and GTK 4.

### Manual Integration

To use DMS colors with your own GTK theme:

```css
/* In ~/.config/gtk-3.0/gtk.css or gtk-4.0/gtk.css */
@import url("dank-colors.css");
```

## Qt Applications

Qt theming offers two approaches: GTK passthrough or dedicated Qt control.

> [!tip] Systemd / DankInstall Users
> Set environment variables in `~/.config/environment.d/90-dms.conf`. For example, to switch to qt6ct:
> ```ini
> QT_QPA_PLATFORMTHEME=qt6ct
> ```
> Log out and back in for changes to take effect.
> Alternatively, run `systemctl --user edit dms` and add `Environment=QT_QPA_PLATFORMTHEME=qt6ct` under `[Service]`. This only affects DMS and apps it launches, whereas `90-dms.conf` applies to all user sessions.

### Option 1: GTK Passthrough (Simple)

Best for users who primarily run GTK applications. Qt apps use the GTK theme. Default for dankinstall setups.

**niri:**
```kdl
environment {
  QT_QPA_PLATFORMTHEME "gtk3"
  QT_QPA_PLATFORMTHEME_QT6 "gtk3"
}
```

**Hyprland:**
```conf
env = QT_QPA_PLATFORMTHEME,gtk3
env = QT_QPA_PLATFORMTHEME_QT6,gtk3
```

### Option 2: Dedicated Qt Control (Advanced)

Provides better Qt integration and more styling control.

**Install qt6ct:**

```bash
# Arch
paru -S qt6ct-kde
# Fedora
sudo dnf install qt6ct
# Other distributions: https://www.opencode.net/trialuser/qt6ct
```

**Configure Environment:**

For systemd/dankinstall users, edit `~/.config/environment.d/90-dms.conf`:
```ini
QT_QPA_PLATFORMTHEME=qt6ct
```

> [!warning] KDE/Plasma Users
> Setting `QT_QPA_PLATFORMTHEME` in `environment.d` will break KDE/Plasma sessions. Use `systemctl --user edit dms` instead:
> ```bash
> systemctl --user edit dms
> ```
> Add under `[Service]`:
> ```ini
> [Service]
> Environment=QT_QPA_PLATFORMTHEME=qt6ct
> ```
> Then run `systemctl --user restart dms.service`

Otherwise, add to your compositor config:

**niri:**
```kdl
environment {
  QT_QPA_PLATFORMTHEME "qt6ct"
  QT_QPA_PLATFORMTHEME_QT6 "qt6ct"
}
```

**Hyprland:**
```conf
env = QT_QPA_PLATFORMTHEME,qt6ct
env = QT_QPA_PLATFORMTHEME_QT6,qt6ct
```

**Enable Qt Theming:**

1. Log out and back in (or restart compositor)
2. Open **Settings > Theme & Colors**
3. Toggle **Apply Qt Themes**

### Dolphin File Manager

Dolphin requires `qt6ct-kde` (not standard `qt6ct`) for proper color theming.

**With qt6ct-kde installed:**

Set color scheme to **Dank Shell (matugen)** in qt6ct's Appearance tab under KColorScheme.

**Alternative (if qt6ct-kde unavailable):**

Create `~/.config/dolphinrc`:
```ini
[UiSettings]
ColorScheme=DankMatugen
```

## Firefox

Firefox has two theme integration options: Material Fox or Pywalfox.

### Option 1: Material Fox (Chrome-like with Dynamic Colors)

Firefox uses GTK3 theming but a separate matugen CSS is generated for Material Fox integration.

**Enable Custom Styles in Firefox:**

Navigate to `about:config` and set:
- `toolkit.legacyuserprofilecustomizations.stylesheets` = `true`
- `svg.context-properties.content.enabled` = `true`

Create new boolean property:
- `userChrome.theme-material` = `true`

**Install Material Fox Theme:**

```bash
# Find Firefox profile directory
export PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name "*.default-release" | head -n 1)
# Download and extract theme
curl -L -o "$PROFILE_DIR/chrome.zip" https://github.com/edelvarden/material-fox-updated/releases/download/v2.0.0/chrome.zip
unzip -o "$PROFILE_DIR/chrome.zip" -d "$PROFILE_DIR"
rm "$PROFILE_DIR/chrome.zip"
```

**Link Dynamic Colors:**

```bash
export PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name "*.default-release" | head -n 1)
rm -f "$PROFILE_DIR/chrome/theme-material-blue.css"
ln -sf ~/.config/DankMaterialShell/firefox.css "$PROFILE_DIR/chrome/theme-material-blue.css"
```

Restart Firefox to apply.

### Option 2: Pywalfox

```bash
# Arch
paru -S python-pywalfox
# Other distributions: https://github.com/Frewacom/pywalfox
```

Install the [Pywalfox extension](https://addons.mozilla.org/firefox/addon/pywalfox/) from Firefox Add-ons.

**Enable DMS Colors:**

```bash
ln -sf ~/.cache/wal/dank-pywalfox.json ~/.cache/wal/colors.json
```

Restart DMS to generate the palette, then enable Pywalfox in the browser.

### Zen Browser

Zen Browser handles theming differently — Pywalfox and Firefox theme extensions no longer work. Theming is controlled via `userChrome.css`.

DMS generates `~/.config/DankMaterialShell/zen.css` automatically. Link it to your Zen profile:

```bash
# Find default profile directory
export PROFILE_DIR=$(find ~/.zen -maxdepth 1 -type d -name "*.Default Profile" | head -n 1)
mkdir -p "$PROFILE_DIR/chrome"
ln -sf ~/.config/DankMaterialShell/zen.css "$PROFILE_DIR/chrome/userChrome.css"
```

> [!note] Theming must be enabled in Zen browser for `userChrome.css` changes to take effect. Open `about:config` and enable `toolkit.legacyUserProfileCustomizations.stylesheets`. Restart your browser.

### Browser Tips

- Keep userChrome/userContent overrides under version control
- Disable conflicting theme extensions when using DMS-managed colors

## Editors

Editors use `dank16` and matugen to produce a colorful, theme-honoring template with contrast.

### VSCode / Codium / Cursor / Windsurf

Install from the VS Code Marketplace by searching "DMS - Dank Material Shell Theme", or manually:

```bash
wget https://github.com/AvengeMedia/DankMaterialShell/raw/refs/heads/master/quickshell/matugen/dms-theme.vsix
code --install-extension dms-theme.vsix
# or: codium / cursor / windsurf --install-extension ...
```

**Activate:** Open command palette (`Ctrl+Shift+P`), select **Preferences: Color Theme**, choose **Dynamic Base16 DankShell** (or **DMS - Dank Material Shell** in 1.2).

**Trigger colors:** Restart DMS or change wallpaper/theme to generate dynamic colors.

## Terminal Applications

Terminal editors use a custom `dank16` algorithm alongside matugen to generate a palette that honors the theme while providing 16 ansi colors.

### Ghostty

```bash
echo "theme = dankcolors" >> ~/.config/ghostty/config
```

Optional - disable excessive notifications:

```bash
echo "app-notifications = no-clipboard-copy,no-config-reload" >> ~/.config/ghostty/config
```

### kitty

```bash
echo "include dank-tabs.conf" >> ~/.config/kitty/kitty.conf
echo "include dank-theme.conf" >> ~/.config/kitty/kitty.conf
```

> [!tip] If you customized the kitty theme, kitty may save `dark-theme.auto.conf`, `light-theme.auto.conf`, `no-preference-theme.auto.conf` in `~/.config/kitty`. Delete them to make the theme take effect.

### foot

foot requires absolute paths. Edit `~/.config/foot/foot.ini`:

```ini
[main]
include=/home/<USERNAME>/.config/foot/dank-colors.ini
```

### alacritty

Add the alacritty theme to your imports section in `~/.config/alacritty/alacritty.toml`:

```toml
[general]
import = [
    "~/.config/alacritty/dank-theme.toml"
]
```

Reload or restart the terminal.

## Troubleshooting

| Problem | Solution |
|---|---|
| GTK apps not themed | Verify `adw-gtk-theme` is installed; check symlinks `ls -la ~/.config/gtk-3.0/gtk.css`; ensure "Apply GTK Themes" is toggled |
| Qt apps not themed | Verify environment variables in compositor config; restart compositor; check `qt6ct` is installed (Option 2); ensure "Apply Qt Themes" is toggled |
| Firefox theme not working | Verify `about:config` settings; check theme files exist in profile; try disabling other Firefox theme extensions; restart Firefox |
| Terminal colors not updating | Verify config lines added to terminal config; check theme files exist in `~/.config/DankMaterialShell/`; restart terminal |

#matugen #theming #gtk-integration #qt-integration
