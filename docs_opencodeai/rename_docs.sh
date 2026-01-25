#!/bin/bash
set -e

# Category 1: Introduction & Overview (001-002)
mv "index.md" "001-index.md" 2>/dev/null || true
mv "docs.md" "002-docs.md" 2>/dev/null || true

# Category 2: Release Notes (003)
mv "docs-1-0.md" "003-docs-1-0.md" 2>/dev/null || true

# Category 3: Interfaces & Usage (004-009)
mv "docs-tui.md" "004-docs-tui.md" 2>/dev/null || true
mv "docs-cli.md" "005-docs-cli.md" 2>/dev/null || true
mv "docs-ide.md" "006-docs-ide.md" 2>/dev/null || true
mv "docs-web.md" "007-docs-web.md" 2>/dev/null || true
mv "docs-acp.md" "008-docs-acp.md" 2>/dev/null || true
mv "docs-keybinds.md" "009-docs-keybinds.md" 2>/dev/null || true

# Category 4: Configuration (010-020)
mv "docs-config.md" "010-docs-config.md" 2>/dev/null || true
mv "docs-providers.md" "011-docs-providers.md" 2>/dev/null || true
mv "docs-models.md" "012-docs-models.md" 2>/dev/null || true
mv "docs-modes.md" "013-docs-modes.md" 2>/dev/null || true
mv "docs-permissions.md" "014-docs-permissions.md" 2>/dev/null || true
mv "docs-rules.md" "015-docs-rules.md" 2>/dev/null || true
mv "docs-formatters.md" "016-docs-formatters.md" 2>/dev/null || true
mv "docs-lsp.md" "017-docs-lsp.md" 2>/dev/null || true
mv "docs-network.md" "018-docs-network.md" 2>/dev/null || true
mv "docs-themes.md" "019-docs-themes.md" 2>/dev/null || true

# Category 5: Features & Capabilities (020-027)
mv "docs-agents.md" "020-docs-agents.md" 2>/dev/null || true
mv "docs-commands.md" "021-docs-commands.md" 2>/dev/null || true
mv "docs-skills.md" "022-docs-skills.md" 2>/dev/null || true
mv "docs-tools.md" "023-docs-tools.md" 2>/dev/null || true
mv "docs-custom-tools.md" "024-docs-custom-tools.md" 2>/dev/null || true
mv "docs-plugins.md" "025-docs-plugins.md" 2>/dev/null || true
mv "docs-mcp-servers.md" "026-docs-mcp-servers.md" 2>/dev/null || true
mv "docs-share.md" "027-docs-share.md" 2>/dev/null || true

# Category 6: Integrations (028-029)
mv "docs-github.md" "028-docs-github.md" 2>/dev/null || true
mv "docs-gitlab.md" "029-docs-gitlab.md" 2>/dev/null || true

# Category 7: API & SDK (030-031)
mv "docs-sdk.md" "030-docs-sdk.md" 2>/dev/null || true
mv "docs-server.md" "031-docs-server.md" 2>/dev/null || true

# Category 8: Enterprise & Zen (032-035)
mv "docs-enterprise.md" "032-docs-enterprise.md" 2>/dev/null || true
mv "enterprise.md" "033-enterprise.md" 2>/dev/null || true
mv "docs-zen.md" "034-docs-zen.md" 2>/dev/null || true
mv "zen.md" "035-zen.md" 2>/dev/null || true

# Category 9: Reference & Resources (036-038)
mv "docs-ecosystem.md" "036-docs-ecosystem.md" 2>/dev/null || true
mv "brand.md" "037-brand.md" 2>/dev/null || true
mv "docs-troubleshooting.md" "038-docs-troubleshooting.md" 2>/dev/null || true

echo "Rename complete!"
