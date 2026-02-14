---
title: Usage | Camoufox
url: https://camoufox.com/python/usage/#parameters-list
source: crawler
fetched_at: 2026-02-14T14:05:41.856688-03:00
rendered_js: true
word_count: 581
summary: This document provides a detailed reference for Camoufox initialization parameters, covering configuration options for browser fingerprinting, geolocation, and stealth features.
tags:
    - camoufox
    - playwright-integration
    - browser-fingerprinting
    - stealth-browsing
    - python-api
    - configuration-reference
category: reference
---

Camoufox is fully compatible with your existing Playwright code. You only have to change your browser initialization:

```

from camoufox.sync_api import Camoufox

with Camoufox() as browser:
    page = browser.new_page()
    page.goto("https://example.com")
```

* * *

## [#](#parameters-list)Parameters List

**All Playwright Firefox launch options are accepted, along with the following:**

* * *

## [#](#device-rotation)Device Rotation

Camoufox will generate device information for you based on the following parameters.

**Type:** `Optional[ListOrString]`

Operating system to use for the fingerprint generation. Can be `"windows"`, `"macos"`, `"linux"`, or a list to randomly choose from. By default, Camoufox will randomly choose from a list of all three.

```

# Use a specific OS
with Camoufox(os="windows") as browser:
    ...

# Randomly choose from a list of OS
with Camoufox(os=["windows", "macos", "linux"]) as browser:
    ...
```

**Type:** `Optional[List[str]]`

Fonts to load into Camoufox, in addition to the default fonts for the target `os`. Takes a list of font family names that are installed on the system.

Fonts & font fingerprinting

../../fingerprint/fonts/

```

custom_fonts = ["Arial", "Helvetica", "Times New Roman"]
with Camoufox(fonts=custom_fonts) as browser:
    ...
```

**Type:** `Optional[Screen]`

Constrains the screen dimensions of the generated fingerprint. Takes a `browserforge.fingerprints.Screen` instance.

```

from browserforge.fingerprints import Screen

constrains = Screen(max_width=1920, max_height=1080)
with Camoufox(screen=constrains) as browser:
...
```

**Type:** `Optional[Tuple[str, str]]`

Use a specific WebGL vendor/renderer pair. Passed as a tuple of (vendor, renderer). The vendor & renderer combination must be supported for the target `os` or this will cause leaks.

Check [here](https://camoufox.com/webgl-research/) for a list of Camoufox's supported vendor & renderer combinations.

```

with Camoufox(
    webgl_config=("Apple", "Apple M1, or similar"),
    os="macos",
) as browser:
    ...
```

**Type:** `Optional[Dict[str, Any]]`

If needed, individual Camoufox config properties can be overridden by passing them as a dictionary to the `config` parameter. This can be used to enable features that have not yet been implemented into the Python library.

* * *

## [#](#configuration)Configuration

Extra feature configuration and quality of life options.

**Type:** `Optional[Union[bool, float]]`

Humanize the cursor movement. Takes either `True`, or the MAX duration in seconds of the cursor movement. The cursor typically takes up to 1.5 seconds to move across the window.

Cursor movement info & demo

../../fingerprint/cursor-movement/

```

# Enable humanization with default settings
with Camoufox(humanize=True) as browser:
    ...

# Set a custom max duration for cursor movement
with Camoufox(humanize=2.0) as browser:
    ...
```

**Type:** `Optional[Union[bool, Literal['virtual']]]`

Whether to run the browser in headless mode. Defaults to False. If you are running linux, passing 'virtual' will use Xvfb.

Virtual Display

../virtual-display/

```

# Run in headless mode
with Camoufox(headless=True) as browser:
    ...

# Run in headless mode on linux
with Camoufox(headless="virtual") as browser:
    ...
```

**Type:** `Optional[List[str]]`

List of Firefox addons to use. Must be paths to extracted addons.

To load an `.xpi` file, rename it to a `.zip` file, extract it, and pass the extracted folder.

```

addons = ["/path/to/addon1", "/path/to/addon2"]
with Camoufox(addons=addons) as browser:
    ...
```

**Type:** `Optional[List[DefaultAddons]]`

Exclude the default addons. Passed as a list of `camoufox.DefaultAddons` enums.

Default addons

../../fingerprint/addons/#default-addons

**Type:** `Optional[Tuple[int, int]]`

Set the window size in (width, height) pixels. This will also set the `window.screenX` and `window.screenY` properties to position the window at the center of the generated screen.

```

with Camoufox(window=(1282, 955)) as browser:
    ...
```

**Type:** `Optional[bool]`

Whether to inject scripts into the main world when prefixed with `mw:`

```

with Camoufox(main_world_eval=True) as browser:
    page = browser.new_page()
    page.goto("https://example.com")
    # Modify the DOM
    page.evaluate("mw:document.querySelector('h1').remove()")
```

See more info

../main-world-eval/

**Type:** `Optional[bool]`

Whether to cache previous pages, requests, etc. Disabled by default as it uses more memory.

```

with Camoufox(enable_cache=True) as browser:
    ...
```

**Type:** `Optional[bool]`

Whether to create a persistent context. Requires `user_data_dir`.

```

with Camoufox(
    persistent_context=True,
    user_data_dir='/path/to/profile/dir',
) as context:
    ...
```

* * *

## [#](#location--language)Location & Language

Prevent proxy detection by matching your geolocation & locale with your target IP. This will populate the [Geolocation & Intl](https://camoufox.com/python/geoip/) properties for you.

**Type:** `Optional[Union[str, bool]]`

Calculates longitude, latitude, timezone, country, & locale based on the IP address. Pass the target IP address to use, or `True` to find the IP address automatically.

Geolocation & Proxies

../geoip/

```

# Use a specific IP address
with Camoufox(geoip="203.0.113.0", proxy=...) as browser:
    ...

# Automatically find the IP address
with Camoufox(geoip=True, proxy=...) as browser:
    ...
```

**Type:** `Optional[Union[str, List[str]]]`

Locale(s) to use in Camoufox. Can be a list of strings, or a single string separated by a comma. The first locale in the list will be used for the Intl API.

```

# Use a single locale
with Camoufox(locale="en-US") as browser:
    ...

# Generate a language based on the distribution of speakers the US
with Camoufox(locale="US") as browser:
    ...

# Use multiple accepted locales
with Camoufox(locale=["en-US", "fr-FR", "de-DE"]) as browser:
    ...
with Camoufox(locale="en-US,fr-FR,de-DE") as browser:
    ...
```

* * *

## [#](#toggles)Toggles

Shortcuts for common Firefox preferences and security toggles.

**Type:** `Optional[bool]`

Blocks all requests to images. This can help save your proxy usage.

```

with Camoufox(block_images=True) as browser:
    ...
```

**Type:** `Optional[bool]`

Blocks WebRTC entirely.

```

with Camoufox(block_webrtc=True) as browser:
    ...
```

**Type:** `Optional[bool]`

Whether to block WebGL. To prevent leaks, only use this for special cases.

```

with Camoufox(block_webgl=True) as browser:
    ...
```

**Type:** `Optional[bool]`

Disables the Cross-Origin-Opener-Policy (COOP). This allows elements in `cross-origin` iframes, such as the Turnstile checkbox, to be clicked.

```

# Cloudflare turnstile example
with Camoufox(disable_coop=True, window=(1280, 720)) as browser:
    page = browser.new_page()
    page.goto('https://nopecha.com/demo/cloudflare')
    page.wait_for_load_state(state="domcontentloaded")
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(5000)  # 5 seconds
    page.mouse.click(210, 290)
    ...
```

* * *

## [#](#more-usage-docs)More Usage Docs

Geolocation & Proxies

../geoip/

Virtual Display

../virtual-display/

Remote Server

../remote-server/