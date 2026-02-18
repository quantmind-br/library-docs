#!/bin/bash
# ZeroClaw Documentation Organization Script
# Sequential numbering following logical learning progression

cd /Users/diogo/dev/library-docs/zeroclaw

# Category 1: Introduction & Overview (001-005)
mv "docs-README.md" "001-docs-README.md"
mv "docs-README.ja.md" "002-docs-README.ja.md"
mv "docs-README.ru.md" "003-docs-README.ru.md"
mv "docs-README.zh-CN.md" "004-docs-README.zh-CN.md"
mv "docs-SUMMARY.md" "005-docs-SUMMARY.md"

# Category 2: Quick Start & Installation (006-007)
mv "docs-getting-started-README.md" "006-docs-getting-started-README.md"
mv "docs-one-click-bootstrap.md" "007-docs-one-click-bootstrap.md"

# Category 3: Tutorials & How-To (008-009)
mv "docs-langgraph-integration.md" "008-docs-langgraph-integration.md"
mv "docs-adding-boards-and-tools.md" "009-docs-adding-boards-and-tools.md"

# Category 4: Configuration & Settings (010-013)
mv "docs-config-reference.md" "010-docs-config-reference.md"
mv "docs-custom-providers.md" "011-docs-custom-providers.md"
mv "docs-actions-source-policy.md" "012-docs-actions-source-policy.md"
mv "docs-zai-glm-setup.md" "013-docs-zai-glm-setup.md"

# Category 5: Providers & Features (014)
mv "docs-providers-reference.md" "014-docs-providers-reference.md"

# Category 6: Concepts & Design (015-020)
mv "docs-hardware-peripherals-design.md" "015-docs-hardware-peripherals-design.md"
mv "docs-agnostic-security.md" "016-docs-agnostic-security.md"
mv "docs-audit-logging.md" "017-docs-audit-logging.md"
mv "docs-frictionless-security.md" "018-docs-frictionless-security.md"
mv "docs-sandboxing.md" "019-docs-sandboxing.md"
mv "docs-resource-limits.md" "020-docs-resource-limits.md"

# Category 7: Integration & Connection (021-022)
mv "docs-mattermost-setup.md" "021-docs-mattermost-setup.md"
mv "docs-network-deployment.md" "022-docs-network-deployment.md"

# Category 8: API & CLI Reference (023-026)
mv "docs-commands-reference.md" "023-docs-commands-reference.md"
mv "docs-channels-reference.md" "024-docs-channels-reference.md"
mv "docs-ci-map.md" "025-docs-ci-map.md"
mv "docs-reference-README.md" "026-docs-reference-README.md"

# Category 9: Hardware Datasheets & Reference (027-029)
mv "docs-datasheets-arduino-uno.md" "027-docs-datasheets-arduino-uno.md"
mv "docs-datasheets-esp32.md" "028-docs-datasheets-esp32.md"
mv "docs-datasheets-nucleo-f401re.md" "029-docs-datasheets-nucleo-f401re.md"

# Category 10: Operations & Deployment (030-033)
mv "docs-arduino-uno-q-setup.md" "030-docs-arduino-uno-q-setup.md"
mv "docs-nucleo-setup.md" "031-docs-nucleo-setup.md"
mv "docs-operations-README.md" "032-docs-operations-README.md"
mv "docs-operations-runbook.md" "033-docs-operations-runbook.md"

# Category 11: Security (034-035)
mv "docs-security-README.md" "034-docs-security-README.md"
mv "docs-security-roadmap.md" "035-docs-security-roadmap.md"

# Category 12: Automation & Workflow (036-037)
mv "docs-pr-workflow.md" "036-docs-pr-workflow.md"
mv "docs-reviewer-playbook.md" "037-docs-reviewer-playbook.md"

# Category 13: Troubleshooting & Support (038)
mv "docs-troubleshooting.md" "038-docs-troubleshooting.md"

# Category 14: Meta & Resources (039-043)
mv "docs-contributing-README.md" "039-docs-contributing-README.md"
mv "docs-project-README.md" "040-docs-project-README.md"
mv "docs-docs-inventory.md" "041-docs-docs-inventory.md"
mv "docs-hardware-README.md" "042-docs-hardware-README.md"
mv "docs-project-triage-snapshot-2026-02-18.md" "043-docs-project-triage-snapshot-2026-02-18.md"

echo "Rename completed successfully"
