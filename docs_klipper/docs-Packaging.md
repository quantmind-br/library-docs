---
title: Packaging
url: https://github.com/Klipper3d/klipper/blob/master/docs/Packaging.md
source: git
fetched_at: 2026-02-17T13:03:37.739315-03:00
rendered_js: false
word_count: 176
summary: This document provides technical instructions for packaging Klipper, detailing requirements for C module compilation, Python pre-compilation, and versioning without git.
tags:
    - klipper
    - packaging-guide
    - python-compilation
    - c-modules
    - versioning
    - linux-distribution
category: guide
---

# Packaging Klipper

Klipper is somewhat of a packaging anomaly among python programs, as it doesn't
use setuptools to build and install. Some notes regarding how best to package it
are as follows:

## C modules

Klipper uses a C module to handle some kinematics calculations more quickly.
This module needs to be compiled at packaging time to avoid introducing a
runtime dependency on a compiler. To compile the C module, run `python2
klippy/chelper/__init__.py`.

## Compiling python code

Many distributions have a policy of compiling all python code before packaging
to improve startup time. You can do this by running `python2 -m compileall
klippy`.

## Versioning

If you are building a package of Klipper from git, it is usual practice not to
ship a .git directory, so the versioning must be handled without git.  To do
this, use the script shipped in `scripts/make_version.py` which should be run as
follows: `python2 scripts/make_version.py YOURDISTRONAME > klippy/.version`.

## Sample packaging script

klipper-git is packaged for Arch Linux, and has a PKGBUILD (package build
script) available at [Arch User Repository](https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=klipper-git).
