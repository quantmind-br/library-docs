---
title: Contributing to the Registry | Dank Linux
url: https://danklinux.com/docs/contributing-registry
source: sitemap
fetched_at: 2026-01-24T13:35:06.477509749-03:00
rendered_js: false
word_count: 415
summary: This document provides comprehensive instructions and JSON schemas for contributing plugins and themes to the DankMaterialShell registry.
tags:
    - dankmaterialshell
    - plugin-contribution
    - theme-submission
    - json-schema
    - registry-management
    - contribution-guide
category: guide
---

```
██████╗ ███████╗ ██████╗ ██╗███████╗████████╗██████╗ ██╗   ██╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝
██████╔╝█████╗  ██║  ███╗██║███████╗   ██║   ██████╔╝ ╚████╔╝
██╔══██╗██╔══╝  ██║   ██║██║╚════██║   ██║   ██╔══██╗  ╚██╔╝
██║  ██║███████╗╚██████╔╝██║███████║   ██║   ██║  ██║   ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝
```

Thank you for contributing to the DankMaterialShell registry! This guide covers how to submit plugins and themes to the [dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry) repository.

## Contributing a Plugin[​](#contributing-a-plugin "Direct link to Contributing a Plugin")

### How to Add Your Plugin[​](#how-to-add-your-plugin "Direct link to How to Add Your Plugin")

1. **Fork the repository**
   
   - Go to [AvengeMedia/dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry) and click Fork
2. **Create a new JSON file** in the `plugins/` directory:
   
   ```
   plugins/{github-username}-{plugin-name}.json
   ```
   
   - Use lowercase letters
   - Separate words with hyphens
   - Examples: `daniel-42-z-powerusage.json`, `rochacbruno-worldclock.json`
3. **Fill in your plugin information** using this schema:

```
{
"id":"pluginId",
"name":"PluginName",
"capabilities":["dankbar-widget"],
"category":"monitoring",
"repo":"https://github.com/yourusername/your-plugin-repo",
"path":"optional/path/in/monorepo",
"author":"Your Name",
"description":"Brief description of what your plugin does",
"dependencies":["dependency1","dependency2"],
"compositors":["niri","hyprland"],
"distro":["any"],
"screenshot":"https://url/to/screenshot.png"
}
```

### Plugin Field Descriptions[​](#plugin-field-descriptions "Direct link to Plugin Field Descriptions")

FieldRequiredDescription`id`YesUnique identifier in camelCase (e.g., `worldClock`). Must match your `plugin.json``name`YesDisplay name. Must match your `plugin.json``capabilities`YesArray like `["dankbar-widget"]``category`YesOne of: `monitoring`, `utilities`, `appearance`, `system`, etc.`repo`YesFull GitHub URL to your plugin repository`path`NoSubdirectory path if plugin is in a monorepo`author`YesYour name or GitHub username`description`YesClear, concise description of the plugin's purpose`dependencies`YesArray of dependencies, use `[]` if none`compositors`YesSupported compositors: `["niri", "hyprland"]`, `["any"]``distro`YesSupported distributions: `["any"]`, `["fedora"]`, `["arch"]`, etc.`screenshot`NoDirect URL to a screenshot image

Important

The `id` and `name` fields **must exactly match** the corresponding fields in your plugin repository's `plugin.json` file.

4. **Validate your plugin locally**:

```
python3 .github/generate.py --validate
python3 .github/validate_links.py
```

5. **Submit a Pull Request**

* * *

## Contributing a Theme[​](#contributing-a-theme "Direct link to Contributing a Theme")

### How to Add Your Theme[​](#how-to-add-your-theme "Direct link to How to Add Your Theme")

1. **Fork the repository**
   
   - Go to [AvengeMedia/dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry) and click Fork
2. **Create a new folder** in the `themes/` directory:
   
   ```
   themes/{theme-id}/theme.json
   ```
   
   - Use lowercase letters and hyphens for the folder name
   - Examples: `tokyonight/`, `gruvbox-dark/`, `catppuccin-mocha/`
3. **Create your `theme.json`** with this schema:

```
{
"id":"themeId",
"name":"Theme Name",
"version":"1.0.0",
"author":"Your Name",
"description":"Brief description of your theme",
"dark":{
"primary":"#7aa2f7",
"primaryText":"#16161e",
"primaryContainer":"#7dcfff",
"secondary":"#bb9af7",
"surface":"#1a1b26",
"surfaceText":"#73daca",
"surfaceVariant":"#2f3549",
"surfaceVariantText":"#cbccd1",
"surfaceTint":"#7aa2f7",
"background":"#16161e",
"backgroundText":"#d5d6db",
"outline":"#787c99",
"surfaceContainer":"#2f3549",
"surfaceContainerHigh":"#444b6a",
"error":"#f7768e",
"warning":"#ff9e64",
"info":"#7dcfff"
},
"light":{
"primary":"#2e7de9",
"primaryText":"#d0d5e3",
"primaryContainer":"#007197",
"secondary":"#9854f1",
"surface":"#e1e2e7",
"surfaceText":"#387068",
"surfaceVariant":"#c4c8da",
"surfaceVariantText":"#1a1b26",
"surfaceTint":"#2e7de9",
"background":"#cbccd1",
"backgroundText":"#1a1b26",
"outline":"#4c505e",
"surfaceContainer":"#dfe0e5",
"surfaceContainerHigh":"#9699a3",
"error":"#f52a65",
"warning":"#b15c00",
"info":"#007197"
}
}
```

### Theme Metadata Fields[​](#theme-metadata-fields "Direct link to Theme Metadata Fields")

FieldRequiredDescription`id`YesUnique identifier in camelCase (e.g., `tokyoNight`, `gruvboxDark`)`name`YesDisplay name of your theme`version`YesSemver version (e.g., `1.0.0`)`author`YesYour name or username`description`YesBrief description of the theme

### Theme Color Fields[​](#theme-color-fields "Direct link to Theme Color Fields")

Both `dark` and `light` objects require these color properties:

FieldDescription`primary`Primary accent color`primaryText`Text color on primary backgrounds`primaryContainer`Container using primary color`secondary`Secondary accent color`surface`Main surface/card background`surfaceText`Text on surfaces`surfaceVariant`Alternative surface color`surfaceVariantText`Text on variant surfaces`surfaceTint`Tint overlay color`background`App background color`backgroundText`Text on background`outline`Border/divider color`surfaceContainer`Container background`surfaceContainerHigh`Elevated container background`error`Error state color`warning`Warning state color`info`Info state color

For more details on how these colors are used, see [Custom Themes](https://danklinux.com/docs/dankmaterialshell/custom-themes).

4. **Validate your theme locally**:

```
python3 .github/validate_themes.py
python3 .github/generate.py --validate
```

5. **Submit a Pull Request**
   
   - Commit only your `theme.json` file (previews are auto-generated)
   - A preview will be generated and posted as a comment on your PR
   - After merge, the preview SVG will be committed automatically

* * *

## Guidelines[​](#guidelines "Direct link to Guidelines")

### For Plugins[​](#for-plugins "Direct link to For Plugins")

- Keep descriptions concise and informative
- Ensure your repository has proper documentation
- Test that your plugin works with the specified compositors and distros
- Include a screenshot when possible

### For Themes[​](#for-themes "Direct link to For Themes")

- All color values must be 6-digit hex codes (e.g., `#7aa2f7`)
- Both `dark` and `light` variants are required
- The `id` must be camelCase (starts lowercase, alphanumeric only)
- Version must follow semver format (`X.Y.Z`)
- Test your colors for readability and contrast

## Questions?[​](#questions "Direct link to Questions?")

If you have questions about the contribution process, please [open an issue](https://github.com/AvengeMedia/dms-plugin-registry/issues) in the registry repository.