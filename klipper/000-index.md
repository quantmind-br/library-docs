---
description: Auto-generated documentation index for Klipper 3D printer firmware
generated: 2026-02-17T13:05:01-03:00
source: https://github.com/Klipper3d/klipper
total_docs: 56
categories: 13
---

# Klipper 3D Printer Firmware Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://github.com/Klipper3d/klipper |
| **Generated** | 2026-02-17T13:05:01-03:00 |
| **Total Documents** | 56 |
| **Categories** | 13 |
| **Organization Method** | Sequential numbering by learning path |

---

## Document Index

### 1. Introduction & Overview (001-004)

Getting started with Klipper - start here for orientation

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-docs-README.md` | README | Introductory landing page for Klipper documentation | klipper, 3d-printing, firmware, introduction |
| 002 | `002-docs-Overview.md` | Overview | Central navigation hub for installation, configuration, and developer sections | documentation-index, installation-guide, configuration-reference |
| 003 | `003-docs-index.md` | Index | Introduction to Klipper architecture with installation links | firmware, micro-controller, installation-guide |
| 004 | `004-docs-Installation.md` | Installation | Complete guide for installing Klipper firmware | firmware-installation, linux-host, mcu-flashing |

### 2. Concepts & Fundamentals (005-007)

Understanding Klipper's architecture and internal mechanics

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 005 | `005-docs-Code-Overview.md` | Code Overview | Architectural overview with directory structure and threading models | klipper-architecture, source-code-layout, python-host-software |
| 006 | `006-docs-Kinematics.md` | Kinematics | Motion system internals - acceleration, look-ahead, step generation | motion-planning, kinematics, acceleration-control |
| 007 | `007-docs-Features.md` | Features | Technical capabilities overview - precision, performance, hardware versatility | motion-control, stepper-precision, input-shaping |

### 3. Configuration Reference (008-010)

Configuration files and printer setup

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 008 | `008-docs-Config-Reference.md` | Config Reference | Detailed configuration parameters for MCUs, pins, and motion settings | configuration-reference, mcu-config, pin-formatting |
| 009 | `009-docs-Config-checks.md` | Config checks | Post-installation diagnostics for pin settings and hardware verification | hardware-verification, stepper-motors, pid-tuning |
| 010 | `010-docs-Slicers.md` | Slicers | Tips for optimizing Cura and Slic3r with Klipper | slicer-configuration, g-code, pressure-advance |

### 4. Calibration & Probing (011-015)

Bed leveling and probe calibration procedures

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 011 | `011-docs-Bed-Level.md` | Bed Level | Paper test method for Z-height calibration | bed-leveling, calibration, paper-test, z-offset |
| 012 | `012-docs-Bed-Mesh.md` | Bed Mesh | Mesh compensation for bed surface irregularities | bed-mesh, auto-leveling, mesh-interpolation |
| 013 | `013-docs-Probe-Calibrate.md` | Probe Calibrate | X, Y, Z offset calibration for automatic Z probes | probe-calibration, z-offset, bltouch |
| 014 | `014-docs-Manual-Level.md` | Manual Level | Z endstop calibration and manual bed leveling | bed-leveling, z-endstop-calibration, bed-screws |
| 015 | `015-docs-Delta-Calibrate.md` | Delta Calibrate | Basic and enhanced delta printer calibration | delta-calibration, delta-printer, calibration-guide |

### 5. Hardware Setup (016-019)

Hardware-specific installation and configuration

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 016 | `016-docs-BLTouch.md` | BLTouch | Connecting, configuring, and testing BL-Touch sensors | bl-touch, z-probe, hardware-setup, troubleshooting |
| 017 | `017-docs-Beaglebone.md` | Beaglebone | Installing Klipper on Beaglebone with PRU cores | beaglebone, pru-firmware, linux-mcu |
| 018 | `018-docs-RPi-microcontroller.md` | RPi microcontroller | Configuring Raspberry Pi as secondary MCU | raspberry-pi, secondary-mcu, gpio-configuration |
| 019 | `019-docs-TMC-Drivers.md` | TMC Drivers | Configuring Trinamic stepper drivers - current tuning, sensorless homing | tmc-drivers, stepper-motors, sensorless-homing |

### 6. Communication & Protocols (020-025)

APIs, protocols, and communication interfaces

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 020 | `020-docs-API-Server.md` | API Server | JSON-RPC API for printer control via Unix domain socket | api-server, json-rpc, printer-control |
| 021 | `021-docs-Protocol.md` | Protocol | Low-level RPC messaging protocol between host and MCU | rpc-protocol, binary-encoding, message-framing |
| 022 | `022-docs-CANBUS.md` | CANBUS | Setting up CAN bus communication | can-bus, hardware-setup, usb-to-can |
| 023 | `023-docs-CANBUS-protocol.md` | CANBUS protocol | CAN bus communication protocol specification | can-bus, communication-protocol |
| 024 | `024-docs-CANBUS-Troubleshooting.md` | CANBUS Troubleshooting | Diagnosing and resolving CAN bus issues | canbus, troubleshooting, debug-tools |
| 025 | `025-docs-MCU-Commands.md` | MCU Commands | Low-level micro-controller commands reference | mcu-commands, microcontroller-protocol, low-level-api |

### 7. Advanced Tuning (026-031)

Print quality optimization techniques

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 026 | `026-docs-Measuring-Resonances.md` | Measuring Resonances | Accelerometer setup for measuring printer resonances | accelerometer, input-shaper, resonance-compensation |
| 027 | `027-docs-Resonance-Compensation.md` | Resonance Compensation | Input shaping configuration for ringing reduction | input-shaping, resonance-compensation, tuning-guide |
| 028 | `028-docs-Pressure-Advance.md` | Pressure Advance | Tuning pressure advance to minimize oozing and blobbing | pressure-advance, extruder-calibration |
| 029 | `029-docs-Rotation-Distance.md` | Rotation Distance | Calculating rotation_distance for stepper motors | stepper-motors, rotation-distance, extruder-calibration |
| 030 | `030-docs-Skew-Correction.md` | Skew Correction | Software-based skew correction for dimensional accuracy | skew-correction, calibration |
| 031 | `031-docs-Config-Changes.md` | Config Changes | Non-backwards compatible configuration changes log | configuration-changes, breaking-changes, deprecations |

### 8. Automation & Macros (032-033)

G-code macros and debugging tools

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 032 | `032-docs-Command-Templates.md` | Command Templates | Jinja2 templates for G-code macro configuration | gcode-macro, jinja2-templates, macro-parameters |
| 033 | `033-docs-Debugging.md` | Debugging | Debugging tools, regression testing, motion analysis | debugging, regression-testing, motion-analysis |

### 9. Firmware & Deployment (034-037)

Bootloaders, flashing, and software updates

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 034 | `034-docs-Bootloaders.md` | Bootloaders | Flashing bootloaders and firmware to microcontrollers | bootloader, firmware-flashing, avrdude |
| 035 | `035-docs-Bootloader-Entry.md` | Bootloader Entry | Methods for rebooting MCU into bootloader | bootloader, serial-communication, canbus |
| 036 | `036-docs-SDCard-Updates.md` | SDCard Updates | Remote firmware updates via SD card | firmware-update, sd-card-flashing |
| 037 | `037-docs-Releases.md` | Releases | Changelog with version history and feature updates | release-notes, changelog, version-history |

### 10. Advanced Hardware Modules (038-046)

Specialized sensors and hardware modules

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 038 | `038-docs-Exclude-Object.md` | Exclude Object | Cancel specific components of multi-part prints | exclude-object, g-code, print-management |
| 039 | `039-docs-Endstop-Phase.md` | Endstop Phase | Stepper phase-adjusted endstop for improved homing | endstop-phase, trinamic-drivers, homing-precision |
| 040 | `040-docs-Eddy-Probe.md` | Eddy Probe | Configuring eddy current inductive probes | eddy-current, inductive-probe, z-probe |
| 041 | `041-docs-Axis-Twist-Compensation.md` | Axis Twist Compensation | Correcting probe errors from rail twists | axis-twist-compensation, bed-leveling |
| 042 | `042-docs-Multi-MCU-Homing.md` | Multi MCU Homing | Homing across multiple microcontrollers | multi-mcu-homing, endstops, z-probe |
| 043 | `043-docs-Load-Cell.md` | Load Cell | Force measurement and nozzle contact probing | load-cell, calibration, probing |
| 044 | `044-docs-Hall-Filament-Width-Sensor.md` | Hall Filament Width Sensor | Hall-effect filament width sensor | filament-sensor, hall-effect, extrusion-control |
| 045 | `045-docs-TSL1401CL-Filament-Width-Sensor.md` | TSL1401CL Filament Width Sensor | TSL1401CL-based filament width sensor | filament-width-sensor, tsl1401cl |
| 046 | `046-docs-Using-PWM-Tools.md` | Using PWM Tools | PWM-based tools (lasers, spindles) control | pwm-control, laser-setup, spindle-control |

### 11. Reference (047-048)

Technical references and benchmarks

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 047 | `047-docs-Benchmarks.md` | Benchmarks | MCU stepping rate benchmarking methodology | benchmarks, micro-controller, step-rate |
| 048 | `048-docs-Status-Reference.md` | Status Reference | Printer status information and object fields | status-reference, macro-variables, api-fields |

### 12. Support & Community (049-052)

Help, community resources, and troubleshooting

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 049 | `049-docs-FAQ.md` | FAQ | Frequently asked questions and common issues | faq, troubleshooting, hardware-requirements |
| 050 | `050-docs-Contact.md` | Contact | Support channels, bug reporting, community links | klipper-support, bug-reporting, community-channels |
| 051 | `051-docs-OctoPrint.md` | OctoPrint | Installing OctoPrint as Klipper frontend | octoprint, octopi, kiauh |
| 052 | `052-docs-G-Codes.md` | G Codes | Complete G-Code command reference | g-code, firmware-commands, motion-control |

### 13. Meta & Resources (053-056)

Community contribution and project resources

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 053 | `053-docs-CONTRIBUTING.md` | CONTRIBUTING | Contribution process and pull request workflow | contributing, pull-request, code-review |
| 054 | `054-docs-Sponsors.md` | Sponsors | Official sponsors and key developers | sponsors, developers, donations |
| 055 | `055-docs-Packaging.md` | Packaging | Technical packaging instructions | packaging-guide, python-compilation |
| 056 | `056-docs-Example-Configs.md` | Example Configs | Guidelines for contributing printer configs | configuration-files, contributing-guidelines |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Installation** | 001-004, 051 |
| **Configuration** | 008-010 |
| **Calibration** | 011-015, 028-030 |
| **Hardware** | 016-019, 040-046 |
| **Communication** | 020-025 |
| **Debugging** | 033, 049-050 |
| **Firmware** | 034-037 |
| **Reference** | 007, 025, 047-048, 052 |

### By Concept

| Concept | Files |
|---------|-------|
| **Bed Leveling** | 011, 012, 013, 014, 015, 041 |
| **Probes** | 013, 016, 040, 041 |
| **Stepper Motors** | 019, 029, 039 |
| **CAN Bus** | 022, 023, 024 |
| **API/Protocol** | 020, 021, 025 |
| **Input Shaping** | 026, 027 |
| **Filament Sensors** | 044, 045 |
| **MCUs** | 017, 018, 025, 034-037 |

---

## Learning Path

### Level 1: Foundation (001-004)
- Start with **001-004** for introduction and installation
- Understand Klipper's basic architecture

### Level 2: Core Understanding (005-010)
- Study **005-007** for concepts and architecture
- Configure printer with **008-010**

### Level 3: Calibration (011-015)
- Master bed leveling with **011-015**
- Understand probe calibration

### Level 4: Hardware Setup (016-019, 038-046)
- Configure hardware with **016-019**
- Explore specialized modules **038-046**

### Level 5: Communication (020-025)
- Learn APIs and protocols **020-025**
- Understand communication layers

### Level 6: Advanced Tuning (026-033)
- Optimize print quality **026-031**
- Automate with macros **032-033**

### Level 7: Deployment (034-037)
- Manage firmware updates **034-037**

### Level 8: Reference (047-056)
- Consult reference docs **047-048, 052**
- Get help with **049-050**
- Contribute back **053-056**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression.*
