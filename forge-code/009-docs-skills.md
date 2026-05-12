---
title: "Skills in ForgeCode"
url: https://forgecode.dev/docs/skills/
source: sitemap
fetched_at: 2026-04-30T14:09:18.794992314-03:00
rendered_js: false
word_count: 139
summary: "Define reusable workflows as skills in ForgeCode to automate repetitive tasks."
tags:
  - workflow-automation
  - forgecode
  - skill-management
  - task-automation
  - configuration-guide
category: guide
optimized: true
---
# Skills in ForgeCode

> **TL;DR**
> Skills are reusable workflows in `SKILL.md` files. Place them in project, agent, or global directories.

## Skill Locations

| Location | Scope | Path |
|----------|-------|------|
| Project | Team | `.forge/skills/<skill-name>/SKILL.md` |
| Agents | User | `~/.agents/skills/<skill-name>/SKILL.md` |
| Global | User | `~/forge/skills/<skill-name>/SKILL.md` |

> **Precedence**: Project > Agents > Global > Built-in.

## Creating Skills

1. **Describe the workflow** to ForgeCode:
   ```plaintext
   Create a skill for generating release notes. Include steps for changelog parsing, version bumping, and Git tagging.
   ```

2. **Review/Adjust** the generated `SKILL.md`.

3. **Place** in the correct directory.

## Example: Release Notes Skill
```markdown
# Release Notes Skill

## Steps
1. Parse `CHANGELOG.md` for new entries.
2. Bump version in `package.json`.
3. Create Git tag.

## Scripts
- `parse_changelog.sh`
- `bump_version.py`
```

## Compatibility
- **Claude Code**: Copy skills directly; no conversion needed.

## Management
- **List skills**: `:skill`
- **Generate**: Ask ForgeCode to create a `SKILL.md` for your workflow.

## Best Practices
- **Detail**: Include steps, scripts, and edge cases.
- **Placement**: Use project skills for team workflows, global for personal reuse.