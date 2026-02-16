#!/bin/bash
cd /Users/diogo/dev/library-docs/sketchybar

# 1. Introduction & Overview
mv "SketchyBar.md" "001-SketchyBar.md"

# 2. Quick Start & Installation
mv "SketchyBar-setup.md" "002-SketchyBar-setup.md"

# 3. Features
mv "SketchyBar-features.md" "003-SketchyBar-features.md"

# 4. Concepts & Fundamentals
mv "SketchyBar-config-types.md" "004-SketchyBar-config-types.md"

# 5-8. Configuration (Bar, Items, Reloading, Popups)
mv "SketchyBar-config-bar.md" "005-SketchyBar-config-bar.md"
mv "SketchyBar-config-items.md" "006-SketchyBar-config-items.md"
mv "SketchyBar-config-reloading.md" "007-SketchyBar-config-reloading.md"
mv "SketchyBar-config-popups.md" "008-SketchyBar-config-popups.md"

# 9-10. Reference (Components, Querying)
mv "SketchyBar-config-components.md" "009-SketchyBar-config-components.md"
mv "SketchyBar-config-querying.md" "010-SketchyBar-config-querying.md"

# 11-13. Advanced Topics (Animations, Events, Tricks)
mv "SketchyBar-config-animations.md" "011-SketchyBar-config-animations.md"
mv "SketchyBar-config-events.md" "012-SketchyBar-config-events.md"
mv "SketchyBar-config-tricks.md" "013-SketchyBar-config-tricks.md"

# 14-15. Meta & Resources (Credits, Search)
mv "SketchyBar-credits.md" "014-SketchyBar-credits.md"
mv "SketchyBar-search.md" "015-SketchyBar-search.md"

echo "File renaming complete!"
