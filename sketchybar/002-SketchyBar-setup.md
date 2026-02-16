---
title: Setup | SketchyBar
url: https://felixkratz.github.io/SketchyBar/setup
source: github_pages
fetched_at: 2026-02-15T21:17:34.234325-03:00
rendered_js: false
word_count: 334
summary: This document provides comprehensive instructions for installing, configuring, and uninstalling SketchyBar on macOS, including prerequisite settings and font setup.
tags:
    - sketchybar
    - macos-customization
    - installation-guide
    - homebrew
    - plugin-setup
    - desktop-utilities
category: guide
---

## Installation[​](#installation "Direct link to heading")

### Prerequisite[​](#prerequisite "Direct link to heading")

SketchyBar will only work properly with the system setting "Displays have separate Spaces" turned on (the default setting). The option is located in *System Settings* -&gt; *Desktop & Dock* -&gt; *Displays have separate Spaces*.

### Brew Install[​](#brew-install "Direct link to heading")

```
brew tap FelixKratz/formulae
brew install sketchybar
```

Copy the example configuration and make it executable:

```
mkdir -p ~/.config/sketchybar/plugins
cp$(brew --prefix)/share/sketchybar/examples/sketchybarrc ~/.config/sketchybar/sketchybarrc
cp -r $(brew --prefix)/share/sketchybar/examples/plugins/ ~/.config/sketchybar/plugins/
```

The default configuration is intentionally sparse, so if you are looking for something more sophisticated as a starting point, you might want to look at [this discussion](https://github.com/FelixKratz/SketchyBar/discussions/47).

Run the bar automatically at startup:

```
brew services start sketchybar
```

or in the command line with verbose output:

It is possible to run sketchybar with a custom config file path (i.e. something else than `$HOME/.config/sketchybar/sketchybarrc`) via:

```
sketchybar --config <path>
```

### Fonts[​](#fonts "Direct link to heading")

The default sketchybar font is the Hack Nerd Font:

```
brew install --cask font-hack-nerd-font
```

if you experience missing icons you might need to install it. Any font of your liking can be used in sketchybar.

If you want to load fonts from a non standard directory, you can use

```
sketchybar --load-font <path>
```

to load a font file from any `<path>`.

### Plugins[​](#plugins "Direct link to heading")

When you use/create additional plugins, make sure that they are made executable via

```
chmod +x name/of/plugin.sh
```

If you run sketchybar from the command line directly with the command `sketchybar` you will see all outputs and error messages from your scripts.

The default plugin folder is located in `~/.config/sketchybar/plugins`. Plugins need to be referenced with absolute paths because relative paths will not be resolved correctly. Have a look at the [discussion](https://github.com/FelixKratz/SketchyBar/discussions/12) for plugins and share your own if you want to. You should of course vet the code from all plugins before executing them to make sure they are not harming your computer.

### Hiding the original macOS bar[​](#hiding-the-original-macos-bar "Direct link to heading")

### Compile from source[​](#compile-from-source "Direct link to heading")

It is easy to compile the project from source:

- Install Xcode commandline tools:

<!--THE END-->

- Clone the repository:

```
git clone https://github.com/FelixKratz/SketchyBar.git
```

- In the sketchybar folder run:

This will generate a universal binary with arm64 and x86 instructions. It is possible to generate an arm64/x86 only binary via `make arm64` or `make x86`. Compiling on older macOS (pre Big Sur) versions should always be done via `make x86`.

## Uninstall[​](#uninstall "Direct link to heading")

Uninstall via `brew`:

```
brew uninstall sketchybar
brew untap FelixKratz/formulae
```