#!/bin/bash
cd /Users/diogo/dev/library-docs/yasb

# Organize documentation files with sequential numbering

# Category 1: Introduction & Overview
mv "index.md" "001-index.md"

# Category 2: Installation
mv "installation.md" "002-installation.md"

# Category 3: Configuration
mv "configuration.md" "003-configuration.md"

# Category 4: Keybindings
mv "keybindings.md" "004-keybindings.md"

# Category 5: Styling
mv "styling.md" "005-styling.md"

# Category 6: Widget Development
mv "writing-widget.md" "006-writing-widget.md"

# Category 7: CLI Reference
mv "cli.md" "007-cli.md"

# Category 8: Contributing
mv "contributing.md" "008-contributing.md"

# Category 9: FAQ & Troubleshooting
mv "faq.md" "009-faq.md"

echo "Files renamed successfully"
