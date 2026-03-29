import json
import os
from datetime import datetime


def organize_docs():
    metadata_path = "/home/diogo/dev/library-docs/gemini-cli/metadata.json"
    base_dir = "/home/diogo/dev/library-docs/gemini-cli"

    with open(metadata_path, "r") as f:
        metadata = json.load(f)

    unique_docs = {}
    for doc in metadata["documents"]:
        orig_path = doc.get("original_file_path")
        if not orig_path:
            curr_path = doc["file_path"]
            if len(curr_path) > 4 and curr_path[3] == "-":
                orig_path = curr_path[4:]
            else:
                orig_path = curr_path

        if orig_path not in unique_docs:
            unique_docs[orig_path] = doc

    categories = {
        "01-Getting Started": [
            "index.md",
            "docs.md",
            "docs-get-started.md",
            "docs-get-started-installation.md",
            "docs-get-started-authentication.md",
            "docs-get-started-examples.md",
            "docs-get-started-gemini-3.md",
            "docs-cli-tutorials-skills-getting-started.md",
            "docs-extensions-getting-started-extensions.md",
        ],
        "02-Guides & Tutorials": [
            "docs-cli-tutorials.md",
            "docs-hooks-writing-hooks.md",
            "docs-hooks-best-practices.md",
            "docs-cli-themes.md",
            "docs-cli-keyboard-shortcuts.md",
            "docs-cli-session-management.md",
        ],
        "03-API Reference": [
            "docs-cli.md",
            "docs-cli-commands.md",
            "docs-cli-settings.md",
            "docs-cli-model.md",
            "docs-tools.md",
            "docs-tools-file-system.md",
            "docs-tools-shell.md",
            "docs-tools-web-search.md",
            "docs-tools-web-fetch.md",
            "docs-tools-memory.md",
            "docs-tools-todos.md",
            "docs-tools-mcp-server.md",
            "docs-hooks-reference.md",
            "docs-ide-integration-ide-companion-spec.md",
            "docs-cli-gemini-md.md",
            "docs-cli-gemini-ignore.md",
        ],
        "04-Architecture & Concepts": [
            "docs-architecture.md",
            "docs-core.md",
            "docs-core-policy-engine.md",
            "docs-core-tools-api.md",
            "docs-core-memport.md",
            "docs-npm.md",
            "docs-cli-token-caching.md",
        ],
        "05-Configuration": [
            "docs-get-started-configuration.md",
            "docs-get-started-configuration-v1.md",
            "docs-cli-system-prompt.md",
            "docs-cli-trusted-folders.md",
        ],
        "06-Advanced Features": [
            "docs-cli-checkpointing.md",
            "docs-cli-sandbox.md",
            "docs-cli-headless.md",
            "docs-cli-custom-commands.md",
            "docs-cli-skills.md",
            "docs-cli-enterprise.md",
            "docs-cli-telemetry.md",
            "docs-extensions.md",
            "docs-extensions-extension-releasing.md",
            "docs-hooks.md",
            "docs-ide-integration.md",
            "docs-cli-authentication.md",
        ],
        "07-Development & Contributing": [
            "docs-contributing.md",
            "docs-integration-tests.md",
            "docs-issue-and-pr-automation.md",
            "docs-releases.md",
            "docs-changelogs.md",
            "docs-changelogs-releases.md",
            "docs-changelogs-latest.md",
            "docs-changelogs-preview.md",
        ],
        "08-Support & Troubleshooting": [
            "docs-faq.md",
            "docs-troubleshooting.md",
            "docs-quota-and-pricing.md",
            "docs-tos-privacy.md",
            "docs-cli-uninstall.md",
        ],
    }

    organized_docs = []
    current_num = 1
    accounted_paths = set()

    for cat_name, file_list in categories.items():
        for f_path in file_list:
            if f_path in unique_docs:
                doc = unique_docs[f_path]
                doc["organization_category"] = cat_name
                doc["sequence_number"] = current_num
                doc["new_file_path"] = f"{current_num:03d}-{f_path}"
                organized_docs.append(doc)
                accounted_paths.add(f_path)
                current_num += 1

    for f_path, doc in unique_docs.items():
        if f_path not in accounted_paths:
            doc["organization_category"] = "09-Other"
            doc["sequence_number"] = current_num
            doc["new_file_path"] = f"{current_num:03d}-{f_path}"
            organized_docs.append(doc)
            current_num += 1

    for doc in organized_docs:
        old_file_path = os.path.join(base_dir, doc["file_path"])
        new_file_path = os.path.join(base_dir, doc["new_file_path"])

        if os.path.exists(old_file_path):
            if old_file_path != new_file_path:
                temp_path = new_file_path + ".tmp"
                os.rename(old_file_path, temp_path)
                doc["temp_path"] = temp_path

    for doc in organized_docs:
        if "temp_path" in doc:
            os.rename(doc["temp_path"], os.path.join(base_dir, doc["new_file_path"]))
        doc["file_path"] = doc["new_file_path"]
        if "new_file_path" in doc:
            del doc["new_file_path"]
        if "temp_path" in doc:
            del doc["temp_path"]

    metadata["documents"] = organized_docs
    metadata["total_documents"] = len(organized_docs)
    metadata["organized_at"] = datetime.now().isoformat()
    metadata["organization_strategy"] = "Universal Category Detection"

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    index_content = "# Gemini CLI Documentation Index\n\n"
    index_content += (
        "Comprehensive guide organized by Universal Category Detection patterns.\n\n"
    )

    current_cat = ""
    for doc in organized_docs:
        if doc["organization_category"] != current_cat:
            current_cat = doc["organization_category"]
            index_content += f"## {current_cat}\n\n"

        title = doc.get("title") or doc["file_path"]
        summary = doc.get("summary", "No summary available.")
        index_content += f"- **[{title}]({doc['file_path']})**\n"
        index_content += f"  {summary}\n\n"

    with open(os.path.join(base_dir, "000-index.md"), "w") as f:
        f.write(index_content)


if __name__ == "__main__":
    organize_docs()
