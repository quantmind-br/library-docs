---
title: ZeroClaw i18n Coverage and Structure
date: 2026-05-05T00:00:00Z
url: https://github.com/openagen/zeroclaw/blob/master/docs/maintainers/i18n-coverage.md
source: git
fetched_at: 2026-05-02T14:51:40.61061266-03:00
rendered_js: false
word_count: 440
summary: This document outlines the directory structure, coverage status, and procedural guidelines for maintaining localized documentation within the ZeroClaw project.
tags:
    - i18n
    - documentation-standards
    - localization-guide
    - project-structure
    - translation-workflow
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# ZeroClaw i18n Coverage and Structure

Defines localization structure and tracks current coverage.

Last refreshed: **February 21, 2026**

## Canonical Layout

Use these i18n paths:

- Root language landing: `README.<locale>.md`
- Full localized docs tree: `docs/i18n/<locale>/...`
- Optional compatibility shims at docs root:
  - `docs/README.<locale>.md`
  - `docs/commands-reference.<locale>.md`
  - `docs/config-reference.<locale>.md`
  - `docs/troubleshooting.<locale>.md`

## Locale Coverage Matrix

| Locale | Root README | Canonical Docs Hub | Commands Ref | Config Ref | Troubleshooting | Status |
|---|---|---|---|---|---|---|
| `en` | `README.md` | `docs/README.md` | `docs/commands-reference.md` | `docs/config-reference.md` | `docs/troubleshooting.md` | Source of truth |
| `zh-CN` | `README.zh-CN.md` | `docs/README.zh-CN.md` | - | - | - | Hub-level localized |
| `ja` | `README.ja.md` | `docs/README.ja.md` | - | - | - | Hub-level localized |
| `ru` | `README.ru.md` | `docs/README.ru.md` | - | - | - | Hub-level localized |
| `fr` | `README.fr.md` | `docs/README.fr.md` | - | - | - | Hub-level localized |
| `vi` | `README.vi.md` | `docs/i18n/vi/README.md` | `docs/i18n/vi/commands-reference.md` | `docs/i18n/vi/config-reference.md` | `docs/i18n/vi/troubleshooting.md` | Full tree localized |

## Root README Completeness

Not all root READMEs are full translations of `README.md`:

| Locale | Style | Approximate Coverage |
|---|---|---|
| `en` | Full source | 100% |
| `zh-CN` | Hub-style entry point | ~26% |
| `ja` | Hub-style entry point | ~26% |
| `ru` | Hub-style entry point | ~26% |
| `fr` | Near-complete translation | ~90% |
| `vi` | Near-complete translation | ~90% |

Hub-style entry points provide quick-start orientation and language navigation but do not replicate full English README content.

## Collection Index i18n

Localized `README.md` files under collection directories currently exist only for English and Vietnamese. Collection index localization for other locales is deferred.

## Localization Rules

- Keep technical identifiers in English:
  - CLI command names
  - config keys
  - API paths
  - trait/type identifiers
- Prefer concise, operator-oriented localization over literal translation
- Update "Last refreshed" dates when localized pages change
- Ensure every localized hub has "Other languages" section

## Adding a New Locale

1. Create `README.<locale>.md`
2. Create canonical docs tree under `docs/i18n/<locale>/` (at least `README.md`, `commands-reference.md`, `config-reference.md`, `troubleshooting.md`)
3. Add locale links to:
   - Root language nav in every `README*.md`
   - Localized hubs line in `docs/README.md`
   - "Other languages" section in every `docs/README*.md`
   - Language entry section in `docs/SUMMARY.md`
4. Optionally add docs-root shim files for backward compatibility
5. Update this file and run link validation

## Review Checklist

- Links resolve for all localized entry files
- No locale references stale filenames (e.g., `README.vn.md`)
- TOC (`docs/SUMMARY.md`) and docs hub (`docs/README.md`) include the locale

#i18n #documentation-standards #localization-guide #project-structure #translation-workflow
