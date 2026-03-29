---
title: ForgeCode
url: https://forgecode.dev/docs/windows-troubleshooting/
source: sitemap
fetched_at: 2026-03-29T16:30:50.19259-03:00
rendered_js: false
word_count: 338
summary: This document provides troubleshooting steps to resolve vcruntime140.dll errors on Windows by installing the required Microsoft Visual C++ Redistributable packages.
tags:
    - windows-troubleshooting
    - dll-errors
    - visual-cpp
    - system-configuration
    - software-installation
category: guide
---

If you are on Windows and `forge` fails to run, you might have an error about a missing `vcruntime140.dll`. This usually means your system is missing an essential runtime library from Microsoft.

The `vcruntime140.dll` file is part of the **Microsoft Visual C++ Redistributable**, which is required to run many applications, including some of ForgeCode's dependencies.

The solution is to download and install the official package from Microsoft.

### Step 1: Determine Your System Architecture[​](#step-1-determine-your-system-architecture "Direct link to Step 1: Determine Your System Architecture")

First, identify your Windows system architecture:

1. Press `Windows + R` to open the Run dialog.
2. Type `msinfo32` and press Enter.
3. In the System Information window, find the "System Type". It will tell you if you have an **x64**, **x86**, or **ARM64** based PC.

### Step 2: Download the Correct Redistributable[​](#step-2-download-the-correct-redistributable "Direct link to Step 2: Download the Correct Redistributable")

Visit the official Microsoft download page:

[**Latest Supported Visual C++ Redistributable Downloads**](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

Download the correct file(s) for your system:

- **For x64-based PC**: Download `vc_redist.x64.exe`
- **For x86-based PC**: Download `vc_redist.x86.exe`
- **For ARM64-based PC**: Download `vc_redist.arm64.exe`

💡

**Tip:** A 64-bit Windows installation can run both 64-bit and 32-bit applications. To ensure maximum compatibility, it is recommended to install both the `x64` and `x86` redistributables on a 64-bit system.

### Step 3: Install the Redistributable[​](#step-3-install-the-redistributable "Direct link to Step 3: Install the Redistributable")

1. **Run as Administrator**: Right-click the downloaded file(s) and select "Run as administrator".
2. **Accept the License**: Agree to the license terms and click "Install".
3. **Restart if Required**: Restart your computer if prompted after installation.

### Step 4: Verify the Fix[​](#step-4-verify-the-fix "Direct link to Step 4: Verify the Fix")

Return to the command prompt or application where you first saw the error and try running the command again. For example, if you were trying to run `forge --version`, try it again in the same terminal.

If the error is gone, you've fixed the problem!

If installing the redistributable didn't solve the problem, please reach out for more help:

- **Join our [Discord community](https://discord.gg/kRZBPpkgwq)** for real-time support.
- **Check our [GitHub Issues](https://github.com/antinomyhq/forge/issues)** for similar problems.
- **Create a new issue** with your system details and the exact error message.

⚠️

**Security Note:** Always download Visual C++ Redistributables directly from Microsoft's official website. Avoid third-party download sites, which may bundle malware.