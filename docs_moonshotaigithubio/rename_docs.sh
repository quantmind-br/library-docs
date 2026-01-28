#!/bin/bash
# Documentation reorganization script
# Generated: 2026-01-28
# Total files: 26

cd /home/diogo/dev/library-docs/docs_moonshotaigithubio

# 1. Getting Started (001)
mv "kimi-cli-en-guides-getting-started.md" "001-kimi-cli-en-guides-getting-started.md"

# 2. Core Guides (002-006)
mv "kimi-cli-en-guides-interaction.md" "002-kimi-cli-en-guides-interaction.md"
mv "kimi-cli-en-guides-sessions.md" "003-kimi-cli-en-guides-sessions.md"
mv "kimi-cli-en-guides-integrations.md" "004-kimi-cli-en-guides-integrations.md"
mv "kimi-cli-en-guides-ides.md" "005-kimi-cli-en-guides-ides.md"
mv "kimi-cli-en-guides-use-cases.md" "006-kimi-cli-en-guides-use-cases.md"

# 3. Configuration (007-011)
mv "kimi-cli-en-configuration-config-files.md" "007-kimi-cli-en-configuration-config-files.md"
mv "kimi-cli-en-configuration-env-vars.md" "008-kimi-cli-en-configuration-env-vars.md"
mv "kimi-cli-en-configuration-overrides.md" "009-kimi-cli-en-configuration-overrides.md"
mv "kimi-cli-en-configuration-providers.md" "010-kimi-cli-en-configuration-providers.md"
mv "kimi-cli-en-configuration-data-locations.md" "011-kimi-cli-en-configuration-data-locations.md"

# 4. Customization (012-016)
mv "kimi-cli-en-customization-agents.md" "012-kimi-cli-en-customization-agents.md"
mv "kimi-cli-en-customization-skills.md" "013-kimi-cli-en-customization-skills.md"
mv "kimi-cli-en-customization-mcp.md" "014-kimi-cli-en-customization-mcp.md"
mv "kimi-cli-en-customization-print-mode.md" "015-kimi-cli-en-customization-print-mode.md"
mv "kimi-cli-en-customization-wire-mode.md" "016-kimi-cli-en-customization-wire-mode.md"

# 5. Reference (017-023)
mv "kimi-cli-en-reference-keyboard.md" "017-kimi-cli-en-reference-keyboard.md"
mv "kimi-cli-en-reference-slash-commands.md" "018-kimi-cli-en-reference-slash-commands.md"
mv "kimi-cli-en-reference-kimi-command.md" "019-kimi-cli-en-reference-kimi-command.md"
mv "kimi-cli-en-reference-kimi-info.md" "020-kimi-cli-en-reference-kimi-info.md"
mv "kimi-cli-en-reference-kimi-term.md" "021-kimi-cli-en-reference-kimi-term.md"
mv "kimi-cli-en-reference-kimi-mcp.md" "022-kimi-cli-en-reference-kimi-mcp.md"
mv "kimi-cli-en-reference-kimi-acp.md" "023-kimi-cli-en-reference-kimi-acp.md"

# 6. FAQ & Support (024)
mv "kimi-cli-en-faq.md" "024-kimi-cli-en-faq.md"

# 7. Release Notes (025-026)
mv "kimi-cli-en-release-notes-breaking-changes.md" "025-kimi-cli-en-release-notes-breaking-changes.md"
mv "kimi-cli-en-release-notes-changelog.md" "026-kimi-cli-en-release-notes-changelog.md"

echo "Renaming complete!"
