#!/usr/bin/env python3
import os
import glob

files = [
    "199-contributing-doc-template.md",
    "200-contributing-docs-contract.md",
    "201-contributing-extension-examples.md",
    "202-contributing-langgraph-integration.md",
    "203-contributing-pr-discipline.md",
    "204-contributing-pr-workflow.md",
    "205-contributing-release-process.md",
    "206-contributing-reviewer-playbook.md",
    "207-contributing-testing-telegram.md"
]

for f in files:
    path = os.path.join("/home/diogo/dev/library-docs/zeroclaw", f)
    if os.path.exists(path):
        print(f"EXISTS: {f} - {os.path.getsize(path)} bytes")
    else:
        print(f"MISSING: {f}")

print("\nAll .md files in directory:")
for md in glob.glob("/home/diogo/dev/library-docs/zeroclaw/*.md"):
    print(f"  {os.path.basename(md)}")
