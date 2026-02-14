#!/bin/bash
cd /Users/diogo/dev/library-docs/camoufox

# Category 1: Introduction & Overview (001)
mv "index.md" "001-introduction.md"

# Category 2: Quick Start & Installation (002)
mv "python-installation.md" "002-installation.md"

# Category 3: Core Concepts (003-004)
mv "stealth.md" "003-stealth-overview.md"
mv "features.md" "004-features-list.md"

# Category 4: Fingerprint Configuration (005-010)
mv "fingerprint.md" "005-fingerprint-injection.md"
mv "fingerprint-miscellaneous.md" "006-fingerprint-miscellaneous.md"
mv "fingerprint-cursor-movement.md" "007-fingerprint-cursor-movement.md"
mv "fingerprint-addons.md" "008-fingerprint-addons.md"
mv "fingerprint-fonts.md" "009-fingerprint-fonts.md"

# Category 5: Python Usage & Guides (010-017)
mv "python.md" "010-python-interface.md"
mv "python-usage.md" "011-python-usage.md"
mv "python-config.md" "012-python-config.md"
mv "python-browserforge.md" "013-python-browserforge.md"
mv "python-geoip.md" "014-python-geoip.md"
mv "python-virtual-display.md" "015-python-virtual-display.md"
mv "python-main-world-eval.md" "016-python-main-world-eval.md"
mv "python-remote-server.md" "017-python-remote-server.md"

# Category 6: Reference & Research (018-019)
mv "webgl-research.md" "018-webgl-research.md"

# Category 7: Development & Build (019-024)
mv "development.md" "019-development-overview.md"
mv "development-overview.md" "020-build-system.md"
mv "development-buildcli.md" "021-building-cli.md"
mv "development-docker.md" "022-building-docker.md"
mv "development-tools.md" "023-development-tools.md"
mv "development-workflow.md" "024-leak-debugging.md"

# Category 8: Other Resources (025)
mv "tests-buttonclick.md" "025-random-button-clicker.md"

echo "File renaming complete!"
