---
title: Translations
url: https://wiki.hypr.land/Contributing-and-Debugging/Translations/
source: sitemap
fetched_at: 2026-04-26T09:50:00.978127364-03:00
rendered_js: false
word_count: 246
summary: This document provides instructions for contributing translations to the Hyprland ecosystem, detailing how to register language entries and handle conditional translations using C++.
tags:
    - hyprland
    - localization
    - translation
    - contributing
    - open-source
    - c-plus-plus
category: guide
optimized: true
optimized_at: 2026-04-26T10:50:00Z
---

Hyprland ecosystem supports localization. This guide covers contributing translations to Hyprland apps.

## Translation files

Translation files for hyprapps:

- [hyprland](https://github.com/hyprwm/Hyprland/blob/main/src/i18n/Engine.cpp)
- [hyprlauncher](https://github.com/hyprwm/hyprlauncher/blob/main/src/i18n/Engine.cpp)
- [hyprpwcenter](https://github.com/hyprwm/hyprpwcenter/blob/main/src/i18n/Engine.cpp)

> [!info]
> More apps coming — list will be updated.

## Translating

Translations are in C++ but straightforward. Submit via standard GitHub MR.

### Basic translations (unconditional)

```cpp
registerEntry("pl_PL", TXT_KEY_HELLO, "Siemka!");
```

Variables supported:

```cpp
registerEntry("pl_PL", TXT_KEY_HELLO, "Siemka, {name}!");
```

### Conditional translations

For languages where translation changes based on amount (e.g., apple vs apples):

```cpp
registerEntry("pl_PL", TXT_KEY_HELLO, [](const Hyprutils::I18n::translationVarMap& vars) {
    int peopleAmount = std::stoi(vars.at("count"));
    if (peopleAmount == 1)
        return "Mam {count} dziewczynkę anime.";
    int last = peopleAmount % 10;
    int lastTwo = peopleAmount % 100;
    if (last >= 2 && last <= 4 && !(lastTwo >= 12 && lastTwo <= 14))
        return "Mam {count} dziewczynki anime.";
    return "Mam {count} dziewczynek anime.";
});
```

All variables are strings — use `std::stoi` to get integers.

### Fallbacks

Fallback order: `xy_ZT` → `xy_XY` → `xy_ANYTHING` → `global fallback` (usually `en_US`).

Example: translating for `de_DE`, user has `de_AT` → `de_DE` used if `de_AT` missing.

See also: [[088-contributing-and-debugging-tests|Tests]]

#hyprland #localization #translation