import re

files = [
    '041-i18n-vi-operations-runbook.md',
    '042-i18n-vi-pr-workflow.md',
    '043-i18n-vi-proxy-agent-playbook.md',
    '044-i18n-vi-release-process.md',
    '045-i18n-vi-reviewer-playbook.md'
]

for filename in files:
    with open(f'/home/diogo/dev/library-docs/zeroclaw/{filename}', 'r', encoding='utf-8') as f:
        content = f.read()
        # Remove code blocks for word count
        content_no_code = re.sub(r'```[^`]*```', '', content, flags=re.DOTALL)
        words = len(content_no_code.split())
        print(f"{filename}: {words} words")
