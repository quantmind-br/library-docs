#!/bin/bash
cd /home/diogo/dev/library-docs/zellij

# Category 1: Introduction & Overview (001-003)
mv "index.md" "001-index.md"
mv "about.md" "002-about.md"
mv "screenshots.md" "003-screenshots.md"

# Category 2: Tutorials - Index & Screencasts (004-005)
mv "tutorials.md" "004-tutorials.md"
mv "screencasts.md" "005-screencasts.md"

# Category 3: Tutorials - Specific (006-014)
mv "tutorials-basic-functionality.md" "006-tutorials-basic-functionality.md"
mv "tutorials-session-management.md" "007-tutorials-session-management.md"
mv "tutorials-layouts.md" "008-tutorials-layouts.md"
mv "tutorials-filepicker.md" "009-tutorials-filepicker.md"
mv "tutorials-stacked-resize.md" "010-tutorials-stacked-resize.md"
mv "tutorials-colliding-keybindings.md" "011-tutorials-colliding-keybindings.md"
mv "tutorials-web-client.md" "012-tutorials-web-client.md"
mv "tutorials-developing-a-rust-plugin.md" "013-tutorials-developing-a-rust-plugin.md"

# Category 4: News/Changelog - Index (014)
mv "news.md" "014-news.md"

# Category 5: News/Changelog - Releases (newest to oldest) (015-029)
mv "news-web-client-multiple-pane-actions.md" "015-news-web-client-multiple-pane-actions.md"
mv "news-stacked-resize-pinned-panes.md" "016-news-stacked-resize-pinned-panes.md"
mv "news-colliding-keybinds-plugin-manager.md" "017-news-colliding-keybinds-plugin-manager.md"
mv "news-welcome-screen-pipes-filepicker.md" "018-news-welcome-screen-pipes-filepicker.md"
mv "news-session-resurrection-ui-components.md" "019-news-session-resurrection-ui-components.md"
mv "news-session-manager-protobuffs.md" "020-news-session-manager-protobuffs.md"
mv "news-stacked-panes-swap-layouts.md" "021-news-stacked-panes-swap-layouts.md"
mv "news-config-command-layouts.md" "022-news-config-command-layouts.md"
mv "news-sixel-search-statusbar.md" "023-news-sixel-search-statusbar.md"
mv "news-edit-scrollback-compact.md" "024-news-edit-scrollback-compact.md"
mv "news-floating-panes-tmux-mode.md" "025-news-floating-panes-tmux-mode.md"
mv "news-multiplayer-sessions.md" "026-news-multiplayer-sessions.md"
mv "news-new-ui.md" "027-news-new-ui.md"
mv "news-new-plugin-system.md" "028-news-new-plugin-system.md"
mv "news-beta.md" "029-news-beta.md"

# Category 6: Reference & Meta (030-033)
mv "roadmap.md" "030-roadmap.md"
mv "categories.md" "031-categories.md"
mv "tags.md" "032-tags.md"
mv "series.md" "033-series.md"

echo "Rename complete!"
