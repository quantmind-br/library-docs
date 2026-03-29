---
description: Auto-generated documentation index for OSX-KVM
generated: "2026-02-04T12:10:56Z"
source: https://github.com/kholia/OSX-KVM
total_docs: 11
categories: 5
---

# OSX-KVM Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence for running macOS on Linux using KVM/QEMU.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://github.com/kholia/OSX-KVM |
| **Generated** | 2026-02-04T12:10:56Z |
| **Total Documents** | 11 |
| **Categories** | Introduction & Overview, Installation Guides, Configuration & Tutorials, Advanced Topics, Reference & Meta |

---

## Document Index

### 1. Introduction & Overview (001-002)
*Foundation documents providing comprehensive overview of macOS virtualization on Linux using QEMU/KVM and OpenCore bootloader.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-README.md` | README | Comprehensive guide for running macOS as a VM on Linux using QEMU/KVM with hardware requirements, installation, and GPU passthrough | macos-virtualization, qemu-kvm, hackintosh-setup, linux-host, opencore-boot, virtual-machine |
| 002 | `002-OpenCore-README.md` | README | Technical notes and resource links for installing macOS Catalina/Big Sur on Linux using OpenCore with boot image generation instructions | macos-virtualization, opencore, kvm, hackintosh, ubuntu, qemu-config |

### 2. Installation Guides (003-004)
*Step-by-step installation procedures for different scenarios and platforms.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-run-offline.md` | Run offline | Step-by-step instructions for offline macOS Ventura installation without a macOS host using OpenCore and custom ISO | macos-installation, opencore, offline-install, ventura, virtualization, iso-creation |
| 004 | `004-UNRAID.md` | UNRAID | Walkthrough for manually configuring macOS VM on Unraid including file preparation, XML configuration, EFI partitioning, and hardware passthrough | unraid, osx-kvm, macos-virtualization, opencore, qemu-kvm, hackintosh, vm-configuration |

### 3. Configuration & Tutorials (005-007)
*Practical guides for configuring macOS VMs for development and advanced use cases.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 005 | `005-Xcode-Tutorial.md` | Xcode Tutorial | Instructions for connecting physical iOS devices to virtualized macOS for Xcode development using USB passthrough or network sharing via Raspberry Pi | macos-virtualization, xcode-development, usb-passthrough, ios-testing, raspberry-pi, usb-redirection |
| 006 | `006-notes.md` | Notes | Comprehensive troubleshooting and configuration guide covering App Store connectivity, screen resolution, and GPU passthrough for hardware acceleration | macos-virtualization, opencore-config, gpu-passthrough, troubleshooting, kvm-qemu, vfio-setup, system-configuration |
| 007 | `007-resources-README.md` | README | Instructions for using idadif.py script to apply differential patch files to macOS kernel binary | macos-kernel, binary-patching, idadif-py, kernel-patching, system-modification |

### 4. Advanced Topics (008)
*Advanced techniques for bypassing virtualization detection and enabling restricted macOS features.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 008 | `008-reversing-notes.md` | Reversing notes | Explains enabling macOS Content Caching feature on VM by bypassing VMM detection through kernel patching or hypervisor configuration changes | macos, virtual-machine, content-caching, kernel-patching, qemu, vmm-detection, hypervisor-configuration |

### 5. Reference & Meta (009-011)
*Reference materials, legal considerations, and project acknowledgments.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 009 | `009-References.md` | References | List of external resources and links for installing, configuring, and troubleshooting macOS as a guest OS in KVM/QEMU environments | macos, kvm, qemu, virtualization, opencore, pci-passthrough, virtual-machines |
| 010 | `010-macOS-Cloud.md` | MacOS Cloud | Notes regarding activities that violate hardware-related terms of the macOS End User License Agreement (EULA) | macos-eula, hardware-compliance, licensing-agreement, legal-restrictions |
| 011 | `011-CREDITS.md` | CREDITS | Comprehensive list of contributors and external resources supporting development including documentation improvements, technical fixes, and core script development | credits, contributors, open-source, project-acknowledgments, virtualization, macos-kvm |

---

## Quick Search by Topics

| Topic | Files | Description |
|-------|-------|-------------|
| **Installation** | 001-004 | Initial setup and installation procedures for macOS VMs |
| **Configuration** | 005-007 | Post-install configuration including Xcode, troubleshooting, and kernel patching |
| **GPU/Passthrough** | 001, 004, 006 | GPU passthrough, hardware acceleration, and VFIO setup |
| **Advanced** | 007-008 | Kernel patching, VMM detection bypass, and system modification |
| **Reference** | 009-011 | External resources, EULA considerations, and credits |

## Quick Search by Concepts

| Concept | Files |
|---------|-------|
| **OpenCore Bootloader** | 001, 002, 003, 004 |
| **QEMU/KVM Virtualization** | 001, 002, 004, 006, 008, 009 |
| **GPU Passthrough** | 001, 004, 006 |
| **Kernel Patching** | 007, 008 |
| **USB/Device Passthrough** | 004, 005 |
| **Troubleshooting** | 006 |
| **Platform-Specific** | 002 (Ubuntu), 004 (Unraid) |

---

## Learning Path

### Level 1: Foundation (Start Here)
**Begin with these documents to understand the project:**
- Read **001-README.md** for comprehensive overview of macOS virtualization on Linux
- Review **002-OpenCore-README.md** for OpenCore-specific technical notes and boot configuration

### Level 2: Installation
**Install macOS on your Linux system:**
- Follow **003-run-offline.md** for offline macOS Ventura installation (recommended for most users)
- Use **004-UNRAID.md** if you're running Unraid as your host OS

### Level 3: Configuration & Development
**Configure your VM for specific use cases:**
- Set up Xcode development with **005-Xcode-Tutorial.md** for iOS device testing
- Configure GPU passthrough and resolve issues with **006-notes.md**
- Apply kernel patches if needed with **007-resources-README.md**

### Level 4: Advanced Usage
**Master advanced virtualization techniques:**
- Enable restricted macOS features with **008-reversing-notes.md** (Content Caching, VMM bypass)

### Level 5: Reference & Support
**Consult additional resources:**
- Explore external documentation with **009-References.md**
- Review legal considerations in **010-macOS-Cloud.md**
- Acknowledge contributors in **011-CREDITS.md**

---

## File Organization

Files are numbered sequentially following a logical learning progression:

```
001-002  : Introduction & Overview (Start here)
003-004  : Installation Guides
005-007  : Configuration & Tutorials
008      : Advanced Topics
009-011  : Reference & Meta
```

### Category Breakdown

1. **Introduction & Overview** (2 files)
   - Main project README with comprehensive setup guide
   - OpenCore-specific technical documentation

2. **Installation Guides** (2 files)
   - Offline installation for macOS Ventura
   - Unraid-specific configuration guide

3. **Configuration & Tutorials** (3 files)
   - Xcode development with iOS device passthrough
   - Troubleshooting and GPU configuration
   - Kernel patching instructions

4. **Advanced Topics** (1 file)
   - VMM detection bypass and Content Caching

5. **Reference & Meta** (3 files)
   - External resources and documentation links
   - EULA and legal considerations
   - Project credits and acknowledgments

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the OSX-KVM documentation structure.*

**Usage Example:**
```bash
# Start with the main README
cat 001-README.md

# Then follow the installation guide
cat 003-run-offline.md

# Configure GPU passthrough
cat 006-notes.md

# Enable advanced features
cat 008-reversing-notes.md
```
