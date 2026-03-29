---
title: ForgeCode
url: https://forgecode.dev/docs/npm-troubleshooting/
source: sitemap
fetched_at: 2026-03-29T14:52:06.130448211-03:00
rendered_js: false
word_count: 401
summary: This document provides troubleshooting guidance for common Node.js and npm issues, including permission errors, PATH problems, and installation difficulties across different operating systems.
tags:
    - nodejs
    - npm
    - troubleshooting
    - installation
    - permission-errors
    - windows
    - macos
    - linux
category: guide
---

This guide helps you resolve common Node.js and npm issues. Note: ForgeCode is now installed via `curl -fsSL https://forgecode.dev/cli | sh`, but this guide is useful if you need to troubleshoot Node.js or npm for other reasons.

If you encounter permission errors when installing Node.js packages globally, here are the recommended solutions:

### Solution 1: Use a Node.js Version Manager (Recommended)[​](#solution-1-use-a-nodejs-version-manager-recommended "Direct link to Solution 1: Use a Node.js Version Manager (Recommended)")

Using a Node.js version manager like nvm is the safest and most reliable approach:

**For macOS and Linux:**

**For Windows:**

### Solution 2: Configure npm to Use a Different Directory[​](#solution-2-configure-npm-to-use-a-different-directory "Direct link to Solution 2: Configure npm to Use a Different Directory")

If you prefer not to use a version manager, configure npm to install global packages in your home directory:

### What NOT to Do[​](#what-not-to-do "Direct link to What NOT to Do")

❌ **Never use `sudo npm install -g`** - This can lead to:

- Permission issues with future npm operations
- Security vulnerabilities
- Ownership conflicts with system files
- Difficult-to-debug installation problems

If the `forge` command is not recognized after installation:

### Check Your Installation[​](#check-your-installation "Direct link to Check Your Installation")

### Fix PATH Issues[​](#fix-path-issues "Direct link to Fix PATH Issues")

### Alternative: Use the curl script[​](#alternative-use-the-curl-script "Direct link to Alternative: Use the curl script")

If you continue having PATH issues, you can always reinstall ForgeCode using the curl script:

### Check Your Node.js Version[​](#check-your-nodejs-version "Direct link to Check Your Node.js Version")

ForgeCode requires:

- **Node.js**: Version 16.0 or later
- **npm**: Version 7.0 or later

### Update Node.js[​](#update-nodejs "Direct link to Update Node.js")

If your Node.js version is too old:

**Using nvm (recommended):**

**Direct download:** Visit [nodejs.org](https://nodejs.org/) and download the latest LTS version.

If you encounter strange installation errors, try clearing the npm cache:

### Corporate Networks[​](#corporate-networks "Direct link to Corporate Networks")

If you're behind a corporate firewall:

### Registry Issues[​](#registry-issues "Direct link to Registry Issues")

If you're having trouble reaching the npm registry:

### Windows[​](#windows "Direct link to Windows")

- Ensure you're using Command Prompt or PowerShell as Administrator if needed
- Consider using Windows Subsystem for Linux (WSL) for a more Unix-like environment
- Make sure Windows Defender isn't blocking npm operations

### macOS[​](#macos "Direct link to macOS")

- If using Homebrew-installed Node.js, ensure proper permissions
- Check that Xcode Command Line Tools are installed: `xcode-select --install`

### Linux[​](#linux "Direct link to Linux")

- Ensure you have build tools installed: `sudo apt-get install build-essential` (Ubuntu/Debian)
- Check that you have proper permissions for the installation directory

If you continue to experience issues:

1. **Check our [GitHub Issues](https://github.com/antinomyhq/forge/issues)** for similar problems
2. **Join our [Discord community](https://discord.gg/kRZBPpkgwq)** for real-time help
3. **Create a new issue** with:
   
   - Your operating system and version
   - Node.js and npm versions (`node --version`, `npm --version`)
   - Complete error messages
   - Steps you've already tried

Run this script to gather system information for troubleshooting:

Copy and paste this output when seeking help for faster diagnosis.

- [**Uninstallation Guide**](https://forgecode.dev/docs/uninstallation/) - If you need to completely remove ForgeCode from your system
- [**Installation Guide**](https://forgecode.dev/docs/) - Return to the main installation instructions