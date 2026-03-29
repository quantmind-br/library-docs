import json
import os
from datetime import datetime


def organize_codex():
    base_dir = "/home/diogo/dev/library-docs/codex"
    metadata_path = os.path.join(base_dir, "metadata.json")

    with open(metadata_path, "r") as f:
        metadata = json.load(f)

    cat_order = [
        "01-Introduction & Overview",
        "02-Authentication & Security",
        "03-Configuration & Settings",
        "04-Tutorials & How-To",
        "05-Concepts & Fundamentals",
        "06-API & Reference",
        "07-Advanced Topics",
        "08-Automation & Workflow",
        "09-Meta & Resources",
    ]

    doc_to_cat = {
        "codex-llms.txt.md": "01-Introduction & Overview",
        "codex-overview.md": "01-Introduction & Overview",
        "codex-auth.md": "02-Authentication & Security",
        "codex-security.md": "02-Authentication & Security",
        "codex-cloud-internet-access.md": "03-Configuration & Settings",
        "codex-config-basic.md": "03-Configuration & Settings",
        "codex-config-sample.md": "03-Configuration & Settings",
        "codex-config-advanced.md": "03-Configuration & Settings",
        "codex-ide-settings.md": "03-Configuration & Settings",
        "codex-rules.md": "03-Configuration & Settings",
        "codex-cloud-environments.md": "03-Configuration & Settings",
        "codex-quickstart.md": "04-Tutorials & How-To",
        "codex-ide.md": "04-Tutorials & How-To",
        "codex-guides-agents-md.md": "04-Tutorials & How-To",
        "codex-cli.md": "04-Tutorials & How-To",
        "codex-cli-features.md": "04-Tutorials & How-To",
        "codex-cli-slash-commands.md": "04-Tutorials & How-To",
        "codex-ide-features.md": "04-Tutorials & How-To",
        "codex-cloud.md": "04-Tutorials & How-To",
        "codex-prompting.md": "04-Tutorials & How-To",
        "codex-custom-prompts.md": "04-Tutorials & How-To",
        "codex-workflows.md": "04-Tutorials & How-To",
        "codex-windows.md": "04-Tutorials & How-To",
        "codex-skills-create-skill.md": "04-Tutorials & How-To",
        "codex-guides-agents-sdk.md": "04-Tutorials & How-To",
        "codex-guides-build-ai-native-engineering-team.md": "04-Tutorials & How-To",
        "codex-mcp.md": "05-Concepts & Fundamentals",
        "codex-config-reference.md": "06-API & Reference",
        "codex-cli-reference.md": "06-API & Reference",
        "codex-ide-commands.md": "06-API & Reference",
        "codex-ide-slash-commands.md": "06-API & Reference",
        "codex-models.md": "06-API & Reference",
        "codex-sdk.md": "06-API & Reference",
        "codex-integrations-slack.md": "07-Advanced Topics",
        "codex-integrations-github.md": "07-Advanced Topics",
        "codex-integrations-linear.md": "07-Advanced Topics",
        "codex-skills.md": "07-Advanced Topics",
        "codex-noninteractive.md": "07-Advanced Topics",
        "codex-enterprise.md": "07-Advanced Topics",
        "codex-github-action.md": "08-Automation & Workflow",
        "codex-feature-maturity.md": "09-Meta & Resources",
        "codex-pricing.md": "09-Meta & Resources",
        "codex-open-source.md": "09-Meta & Resources",
        "codex-llms-full.txt.md": "09-Meta & Resources",
    }

    # Group documents by category
    docs_by_cat = {cat: [] for cat in cat_order}
    for doc in metadata["documents"]:
        orig_path = doc.get("original_file_path")
        if not orig_path:
            curr_path = doc["file_path"]
            if len(curr_path) > 4 and curr_path[3] == "-":
                orig_path = curr_path[4:]
            else:
                orig_path = curr_path

        cat = doc_to_cat.get(orig_path, "09-Meta & Resources")
        docs_by_cat[cat].append((orig_path, doc))

    # Sort within categories by original sequence number or filename
    new_docs = []
    current_num = 1

    for cat in cat_order:
        # Sort docs within category for consistent ordering
        docs_by_cat[cat].sort(key=lambda x: x[0])
        for orig_path, doc in docs_by_cat[cat]:
            new_file_path = f"{current_num:03d}-{orig_path}"
            doc["organization_category"] = cat
            doc["detected_category"] = cat.split("-", 1)[1]
            doc["file_path"] = new_file_path
            doc["original_file_path"] = orig_path
            new_docs.append(doc)
            current_num += 1

    # Rename files
    # First, list all files in directory to avoid renaming non-md files or missing files
    all_files = os.listdir(base_dir)
    doc_files = [f for f in all_files if f.endswith(".md") and f != "000-index.md"]

    # Map old paths to docs
    old_to_doc = {}
    for doc in metadata["documents"]:
        old_to_doc[doc["file_path"]] = doc

    # We need to perform the rename carefully
    # Step 1: Rename to temporary names to avoid collisions
    for doc in new_docs:
        # Find the actual old file path (might be already prefixed)
        old_path = None
        for f in doc_files:
            if f.endswith(doc["original_file_path"]):
                old_path = f
                break

        if old_path:
            src = os.path.join(base_dir, old_path)
            dst = os.path.join(base_dir, f"tmp_{doc['file_path']}")
            os.rename(src, dst)
            doc["tmp_path"] = f"tmp_{doc['file_path']}"

    # Step 2: Rename from temporary names to final names
    for doc in new_docs:
        if "tmp_path" in doc:
            src = os.path.join(base_dir, doc["tmp_path"])
            dst = os.path.join(base_dir, doc["file_path"])
            os.rename(src, dst)
            del doc["tmp_path"]

    # Update metadata
    metadata["documents"] = new_docs
    metadata["total_documents"] = len(new_docs)
    metadata["organization"] = {
        "method": "Universal Category Detection",
        "organized_at": datetime.now().isoformat(),
        "total_files": len(new_docs),
        "categories": [cat.split("-", 1)[1] for cat in cat_order],
    }
    metadata["strategy"] = "Universal Category Detection"

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    # Create 000-index.md
    index_content = "# Codex Documentation Index\n\n"
    index_content += "| Info | Value |\n"
    index_content += "| :--- | :--- |\n"
    index_content += f"| **Generated At** | {metadata['generated_at']} |\n"
    index_content += "| **Strategy** | Universal Category Detection |\n"
    index_content += f"| **Total Documents** | {metadata['total_documents']} |\n\n"

    index_content += (
        "Comprehensive guide organized by Universal Category Detection patterns.\n\n"
    )

    current_cat = ""
    for doc in new_docs:
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
    organize_codex()
