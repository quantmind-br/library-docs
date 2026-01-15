#!/usr/bin/env python3
"""
Organization script for Gemini CLI documentation.
Renames files with sequential numeric prefixes based on logical category order.
"""

import json
import os
from pathlib import Path
from datetime import datetime

# Read metadata
with open('metadata.json', 'r') as f:
    metadata = json.load(f)

# Define document organization with order
# Format: (file_path, new_number, category_name)
organization = [
    # Category 1: Introduction & Overview (001-005)
    ("index.md", 1, "Introduction & Overview"),
    ("docs.md", 2, "Introduction & Overview"),

    # Category 2: Getting Started (003-015)
    ("docs-get-started.md", 3, "Getting Started"),
    ("docs-get-started-installation.md", 4, "Getting Started"),
    ("docs-get-started-authentication.md", 5, "Getting Started"),
    ("docs-get-started-configuration.md", 6, "Getting Started"),
    ("docs-get-started-configuration-v1.md", 7, "Getting Started"),
    ("docs-get-started-examples.md", 8, "Getting Started"),
    ("docs-get-started-gemini-3.md", 9, "Getting Started"),

    # Category 3: CLI Core Features (010-030)
    ("docs-cli.md", 10, "CLI Core Features"),
    ("docs-cli-commands.md", 11, "CLI Core Features"),
    ("docs-cli-settings.md", 12, "CLI Core Features"),
    ("docs-cli-model.md", 13, "CLI Core Features"),
    ("docs-cli-themes.md", 14, "CLI Core Features"),
    ("docs-cli-keyboard-shortcuts.md", 15, "CLI Core Features"),
    ("docs-cli-session-management.md", 16, "CLI Core Features"),

    # Category 4: CLI Advanced Features (017-035)
    ("docs-cli-checkpointing.md", 17, "CLI Advanced Features"),
    ("docs-cli-sandbox.md", 18, "CLI Advanced Features"),
    ("docs-cli-headless.md", 19, "CLI Advanced Features"),
    ("docs-cli-custom-commands.md", 20, "CLI Advanced Features"),
    ("docs-cli-skills.md", 21, "CLI Advanced Features"),
    ("docs-cli-enterprise.md", 22, "CLI Advanced Features"),
    ("docs-cli-trusted-folders.md", 23, "CLI Advanced Features"),
    ("docs-cli-system-prompt.md", 24, "CLI Advanced Features"),
    ("docs-cli-token-caching.md", 25, "CLI Advanced Features"),
    ("docs-cli-telemetry.md", 26, "CLI Advanced Features"),
    ("docs-cli-tutorials.md", 27, "CLI Advanced Features"),
    ("docs-cli-uninstall.md", 28, "CLI Advanced Features"),
    ("docs-cli-gemini-md.md", 29, "CLI Advanced Features"),
    ("docs-cli-gemini-ignore.md", 30, "CLI Advanced Features"),
    ("docs-cli-authentication.md", 31, "CLI Advanced Features"),
    ("docs-cli-tutorials-skills-getting-started.md", 32, "CLI Advanced Features"),

    # Category 5: Core Architecture (033-040)
    ("docs-architecture.md", 33, "Core Architecture"),
    ("docs-core.md", 34, "Core Architecture"),
    ("docs-core-policy-engine.md", 35, "Core Architecture"),
    ("docs-core-tools-api.md", 36, "Core Architecture"),
    ("docs-core-memport.md", 37, "Core Architecture"),

    # Category 6: Tools (038-050)
    ("docs-tools.md", 38, "Tools"),
    ("docs-tools-file-system.md", 39, "Tools"),
    ("docs-tools-shell.md", 40, "Tools"),
    ("docs-tools-web-search.md", 41, "Tools"),
    ("docs-tools-web-fetch.md", 42, "Tools"),
    ("docs-tools-memory.md", 43, "Tools"),
    ("docs-tools-todos.md", 44, "Tools"),
    ("docs-tools-mcp-server.md", 45, "Tools"),

    # Category 7: Extensions (046-053)
    ("docs-extensions.md", 46, "Extensions"),
    ("docs-extensions-getting-started-extensions.md", 47, "Extensions"),
    ("docs-extensions-extension-releasing.md", 48, "Extensions"),

    # Category 8: Hooks (049-055)
    ("docs-hooks.md", 49, "Hooks"),
    ("docs-hooks-writing-hooks.md", 50, "Hooks"),
    ("docs-hooks-best-practices.md", 51, "Hooks"),
    ("docs-hooks-reference.md", 52, "Hooks"),

    # Category 9: IDE Integration (053-057)
    ("docs-ide-integration.md", 53, "IDE Integration"),
    ("docs-ide-integration-ide-companion-spec.md", 54, "IDE Integration"),

    # Category 10: NPM & Testing (055-060)
    ("docs-npm.md", 55, "Development & Testing"),
    ("docs-integration-tests.md", 56, "Development & Testing"),
    ("docs-issue-and-pr-automation.md", 57, "Development & Testing"),
    ("docs-contributing.md", 58, "Development & Testing"),

    # Category 11: Releases & Changelogs (059-070)
    ("docs-releases.md", 59, "Releases & Changelogs"),
    ("docs-changelogs.md", 60, "Releases & Changelogs"),
    ("docs-changelogs-releases.md", 61, "Releases & Changelogs"),
    ("docs-changelogs-latest.md", 62, "Releases & Changelogs"),
    ("docs-changelogs-preview.md", 63, "Releases & Changelogs"),

    # Category 12: Reference & Meta (064-080)
    ("docs-faq.md", 64, "Reference & Meta"),
    ("docs-troubleshooting.md", 65, "Reference & Meta"),
    ("docs-quota-and-pricing.md", 66, "Reference & Meta"),
    ("docs-tos-privacy.md", 67, "Reference & Meta"),
]

# Build mapping and track unique files
rename_map = {}
file_to_category = {}
seen_files = set()

for file_path, number, category in organization:
    if file_path in seen_files:
        # Handle duplicates by adding suffix
        suffix = 1
        while f"{file_path}_{suffix}" in seen_files:
            suffix += 1
        new_name = f"{number:03d}-{file_path}_{suffix}"
        seen_files.add(f"{file_path}_{suffix}")
    else:
        new_name = f"{number:03d}-{file_path}"
        seen_files.add(file_path)

    rename_map[file_path] = new_name
    file_to_category[file_path] = (number, category)

# Handle files not explicitly listed
for doc in metadata['documents']:
    file_path = doc['file_path']
    if file_path not in rename_map:
        # Find next available number
        used_numbers = {v[0] for v in file_to_category.values()}
        next_num = max(used_numbers) + 1 if used_numbers else 1
        while next_num in used_numbers:
            next_num += 1

        rename_map[file_path] = f"{next_num:03d}-{file_path}"
        file_to_category[file_path] = (next_num, "Other")

# Generate bash script
bash_script = """#!/bin/bash
# Auto-generated rename script for Gemini CLI documentation
# Generated: {timestamp}

cd "{dir}"

""".format(timestamp=datetime.now().isoformat(), dir=os.getcwd())

for old_name, new_name in sorted(rename_map.items(), key=lambda x: x[1]):
    if os.path.exists(old_name):
        bash_script += f'mv "{old_name}" "{new_name}"\n'

bash_script += '\necho "Rename complete: {} files renamed"\n'.format(len(rename_map))

# Write bash script
with open('rename_docs.sh', 'w') as f:
    f.write(bash_script)

os.chmod('rename_docs.sh', 0o755)

# Generate updated metadata
updated_metadata = metadata.copy()
updated_metadata['organization'] = {
    "method": "sequential-numbering",
    "organized_at": datetime.now().isoformat(),
    "total_files": len(rename_map),
    "categories": sorted(set(cat for _, cat in file_to_category.values()))
}

# Update document paths
for doc in updated_metadata['documents']:
    old_path = doc['file_path']
    if old_path in rename_map:
        doc['original_file_path'] = old_path
        doc['file_path'] = rename_map[old_path]
        if old_path in file_to_category:
            doc['organization_category'] = file_to_category[old_path][1]
            doc['sequence_number'] = file_to_category[old_path][0]

# Write updated metadata
with open('metadata_updated.json', 'w') as f:
    json.dump(updated_metadata, f, indent=2)

print(f"✓ Generated rename script: rename_docs.sh")
print(f"✓ Generated updated metadata: metadata_updated.json")
print(f"✓ Total files to rename: {len(rename_map)}")
print(f"\nTo execute renaming, run: ./rename_docs.sh")
