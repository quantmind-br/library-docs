#!/bin/bash
# Rename script for Klipper documentation organization
# This script renames all documentation files with sequential numbering

cd /Users/diogo/dev/library-docs/klipper

# Introduction & Overview (001-004)
mv "docs-README.md" "001-docs-README.md"
mv "docs-Overview.md" "002-docs-Overview.md"
mv "docs-index.md" "003-docs-index.md"
mv "docs-Installation.md" "004-docs-Installation.md"

# Concepts & Fundamentals (005-007)
mv "docs-Code-Overview.md" "005-docs-Code-Overview.md"
mv "docs-Kinematics.md" "006-docs-Kinematics.md"
mv "docs-Features.md" "007-docs-Features.md"

# Configuration Reference (008-010)
mv "docs-Config-Reference.md" "008-docs-Config-Reference.md"
mv "docs-Config-checks.md" "009-docs-Config-checks.md"
mv "docs-Slicers.md" "010-docs-Slicers.md"

# Calibration & Probing (011-015)
mv "docs-Bed-Level.md" "011-docs-Bed-Level.md"
mv "docs-Bed-Mesh.md" "012-docs-Bed-Mesh.md"
mv "docs-Probe-Calibrate.md" "013-docs-Probe-Calibrate.md"
mv "docs-Manual-Level.md" "014-docs-Manual-Level.md"
mv "docs-Delta-Calibrate.md" "015-docs-Delta-Calibrate.md"

# Hardware Setup (016-019)
mv "docs-BLTouch.md" "016-docs-BLTouch.md"
mv "docs-Beaglebone.md" "017-docs-Beaglebone.md"
mv "docs-RPi-microcontroller.md" "018-docs-RPi-microcontroller.md"
mv "docs-TMC-Drivers.md" "019-docs-TMC-Drivers.md"

# Communication & Protocols (020-025)
mv "docs-API-Server.md" "020-docs-API-Server.md"
mv "docs-Protocol.md" "021-docs-Protocol.md"
mv "docs-CANBUS.md" "022-docs-CANBUS.md"
mv "docs-CANBUS-protocol.md" "023-docs-CANBUS-protocol.md"
mv "docs-CANBUS-Troubleshooting.md" "024-docs-CANBUS-Troubleshooting.md"
mv "docs-MCU-Commands.md" "025-docs-MCU-Commands.md"

# Advanced Tuning (026-031)
mv "docs-Measuring-Resonances.md" "026-docs-Measuring-Resonances.md"
mv "docs-Resonance-Compensation.md" "027-docs-Resonance-Compensation.md"
mv "docs-Pressure-Advance.md" "028-docs-Pressure-Advance.md"
mv "docs-Rotation-Distance.md" "029-docs-Rotation-Distance.md"
mv "docs-Skew-Correction.md" "030-docs-Skew-Correction.md"
mv "docs-Config-Changes.md" "031-docs-Config-Changes.md"

# Automation & Macros (032-033)
mv "docs-Command-Templates.md" "032-docs-Command-Templates.md"
mv "docs-Debugging.md" "033-docs-Debugging.md"

# Firmware & Deployment (034-037)
mv "docs-Bootloaders.md" "034-docs-Bootloaders.md"
mv "docs-Bootloader-Entry.md" "035-docs-Bootloader-Entry.md"
mv "docs-SDCard-Updates.md" "036-docs-SDCard-Updates.md"
mv "docs-Releases.md" "037-docs-Releases.md"

# Advanced Hardware Modules (038-046)
mv "docs-Exclude-Object.md" "038-docs-Exclude-Object.md"
mv "docs-Endstop-Phase.md" "039-docs-Endstop-Phase.md"
mv "docs-Eddy-Probe.md" "040-docs-Eddy-Probe.md"
mv "docs-Axis-Twist-Compensation.md" "041-docs-Axis-Twist-Compensation.md"
mv "docs-Multi-MCU-Homing.md" "042-docs-Multi-MCU-Homing.md"
mv "docs-Load-Cell.md" "043-docs-Load-Cell.md"
mv "docs-Hall-Filament-Width-Sensor.md" "044-docs-Hall-Filament-Width-Sensor.md"
mv "docs-TSL1401CL-Filament-Width-Sensor.md" "045-docs-TSL1401CL-Filament-Width-Sensor.md"
mv "docs-Using-PWM-Tools.md" "046-docs-Using-PWM-Tools.md"

# Reference (047-048)
mv "docs-Benchmarks.md" "047-docs-Benchmarks.md"
mv "docs-Status-Reference.md" "048-docs-Status-Reference.md"

# Support & Community (049-052)
mv "docs-FAQ.md" "049-docs-FAQ.md"
mv "docs-Contact.md" "050-docs-Contact.md"
mv "docs-OctoPrint.md" "051-docs-OctoPrint.md"
mv "docs-G-Codes.md" "052-docs-G-Codes.md"

# Meta & Resources (053-056)
mv "docs-CONTRIBUTING.md" "053-docs-CONTRIBUTING.md"
mv "docs-Sponsors.md" "054-docs-Sponsors.md"
mv "docs-Packaging.md" "055-docs-Packaging.md"
mv "docs-Example-Configs.md" "056-docs-Example-Configs.md"

echo "Rename complete!"
ls -1 *.md | head -60
