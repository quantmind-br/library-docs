---
title: TSL1401CL Filament Width Sensor
url: https://github.com/Klipper3d/klipper/blob/master/docs/TSL1401CL_Filament_Width_Sensor.md
source: git
fetched_at: 2026-02-17T13:04:05.475506-03:00
rendered_js: false
word_count: 123
summary: This document explains the functionality and configuration of the TSL1401CL-based filament width sensor for automatic extrusion multiplier adjustment.
tags:
    - filament-width-sensor
    - tsl1401cl
    - analog-sensor
    - 3d-printing
    - extrusion-control
    - hardware-module
category: guide
---

# TSL1401CL filament width sensor

This document describes Filament Width Sensor host module. Hardware used
for developing this host module is based on TSL1401CL linear sensor array
but it can work with any sensor array that has analog output. You can find
designs at [Thingiverse](https://www.thingiverse.com/search?q=filament%20width%20sensor).

To use a sensor array as a filament width sensor, read
[Config Reference](Config_Reference.md#tsl1401cl_filament_width_sensor) and
[G-Code documentation](G-Codes.md#hall_filament_width_sensor).

## How does it work?

Sensor generates analog output based on calculated filament width. Output
voltage always equals to detected filament width (Ex. 1.65v, 1.70v, 3.0v).
Host module monitors voltage changes and adjusts extrusion multiplier.

## Note:

Sensor readings done with 10 mm intervals by default. If necessary you are
free to change this setting by editing ***MEASUREMENT_INTERVAL_MM*** parameter
in **filament_width_sensor.py** file.
