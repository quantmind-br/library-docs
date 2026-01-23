---
title: /skills - Anthropic Skills API | liteLLM
url: https://docs.litellm.ai/docs/skills
source: sitemap
fetched_at: 2026-01-21T19:54:50.927552547-03:00
rendered_js: false
word_count: 414
summary: This document explains how to create, manage, and use reusable AI capabilities via the Anthropic Skills API using the LiteLLM Python SDK and LiteLLM Proxy.
tags:
    - litellm
    - anthropic-skills
    - python-sdk
    - api-proxy
    - skills-management
    - llm-routing
category: guide
---

FeatureSupportedCost Tracking✅Logging✅Load Balancing✅Supported Providers`anthropic`

tip

LiteLLM follows the [Anthropic Skills API](https://docs.anthropic.com/en/docs/build-with-claude/skills) for creating, managing, and using reusable AI capabilities.

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Quick Start - Create a Skill[​](#quick-start---create-a-skill "Direct link to Quick Start - Create a Skill")

create\_skill.py

```
from litellm import create_skill
import zipfile
import os

# Create a SKILL.md file
skill_content ="""---
name: test-skill
description: A custom skill for data analysis
---

# Test Skill

This skill helps with data analysis tasks.
"""

# Create skill directory and SKILL.md
os.makedirs("test-skill", exist_ok=True)
withopen("test-skill/SKILL.md","w")as f:
    f.write(skill_content)

# Create a zip file
with zipfile.ZipFile("test-skill.zip","w")as zipf:
    zipf.write("test-skill/SKILL.md","test-skill/SKILL.md")

# Create the skill
response = create_skill(
    display_title="My Custom Skill",
    files=[open("test-skill.zip","rb")],
    custom_llm_provider="anthropic",
    api_key="sk-ant-..."
)

print(f"Skill created: {response.id}")
```

### List Skills[​](#list-skills "Direct link to List Skills")

list\_skills.py

```
from litellm import list_skills

response = list_skills(
    custom_llm_provider="anthropic",
    api_key="sk-ant-...",
    limit=20
)

for skill in response.data:
print(f"{skill.display_title}: {skill.id}")
```

### Get Skill Details[​](#get-skill-details "Direct link to Get Skill Details")

get\_skill.py

```
from litellm import get_skill

skill = get_skill(
    skill_id="skill_01...",
    custom_llm_provider="anthropic",
    api_key="sk-ant-..."
)

print(f"Skill: {skill.display_title}")
print(f"Description: {skill.description}")
```

### Delete a Skill[​](#delete-a-skill "Direct link to Delete a Skill")

delete\_skill.py

```
from litellm import delete_skill

response = delete_skill(
    skill_id="skill_01...",
    custom_llm_provider="anthropic",
    api_key="sk-ant-..."
)

print(f"Deleted: {response.id}")
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

async\_skills.py

```
from litellm import acreate_skill, alist_skills, aget_skill, adelete_skill
import asyncio

asyncdefmanage_skills():
# Create skill
withopen("test-skill.zip","rb")as f:
        skill =await acreate_skill(
            display_title="My Async Skill",
            files=[f],
            custom_llm_provider="anthropic",
            api_key="sk-ant-..."
)

# List skills
    skills =await alist_skills(
        custom_llm_provider="anthropic",
        api_key="sk-ant-..."
)

# Get skill
    skill_detail =await aget_skill(
        skill_id=skill.id,
        custom_llm_provider="anthropic",
        api_key="sk-ant-..."
)

# Delete skill (if no versions exist)
# await adelete_skill(
#     skill_id=skill.id,
#     custom_llm_provider="anthropic",
#     api_key="sk-ant-..."
# )

asyncio.run(manage_skills())
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

LiteLLM provides Anthropic-compatible `/skills` endpoints for managing skills.

### Authentication[​](#authentication "Direct link to Authentication")

There are two ways to authenticate Skills API requests:

**Option 1: Use Default ANTHROPIC\_API\_KEY**

Set the `ANTHROPIC_API_KEY` environment variable. Requests without a `model` parameter will use this default key.

config.yaml

```
# No model_list needed - uses env var
# ANTHROPIC_API_KEY=sk-ant-...
```

```
# Request will use ANTHROPIC_API_KEY from environment
curl "http://0.0.0.0:4000/v1/skills?beta=true" \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

**Option 2: Specify Model for Credential Selection**

Define multiple models in your config and use the `model` parameter to specify which credentials to use.

config.yaml

```
model_list:
-model_name: claude-sonnet
litellm_params:
model: anthropic/claude-3-5-sonnet-20241022
api_key: os.environ/ANTHROPIC_API_KEY
```

Start litellm

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

All examples below work with **either** authentication option (default env key or model-based routing).

#### Create Skill[​](#create-skill "Direct link to Create Skill")

You can upload either a ZIP file or directly upload the SKILL.md file:

**Option 1: Upload ZIP file**

create\_skill\_zip.sh

```
curl "http://0.0.0.0:4000/v1/skills?beta=true" \
  -X POST \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "display_title=My Skill" \
  -F "files[]=@test-skill.zip"
```

**Option 2: Upload SKILL.md directly**

create\_skill\_md.sh

```
curl "http://0.0.0.0:4000/v1/skills?beta=true" \
  -X POST \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "display_title=My Skill" \
  -F "files[]=@test-skill/SKILL.md;filename=test-skill/SKILL.md"
```

#### List Skills[​](#list-skills-1 "Direct link to List Skills")

list\_skills.sh

```
curl "http://0.0.0.0:4000/v1/skills?beta=true" \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

#### Get Skill[​](#get-skill "Direct link to Get Skill")

get\_skill.sh

```
curl "http://0.0.0.0:4000/v1/skills/skill_01abc?beta=true" \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

#### Delete Skill[​](#delete-skill "Direct link to Delete Skill")

delete\_skill.sh

```
curl "http://0.0.0.0:4000/v1/skills/skill_01abc?beta=true" \
  -X DELETE \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

### Model-Based Routing (Multi-Account)[​](#model-based-routing-multi-account "Direct link to Model-Based Routing (Multi-Account)")

If you have multiple Anthropic accounts, you can use model-based routing to specify which account to use:

config.yaml

```
model_list:
-model_name: claude-team-a
litellm_params:
model: anthropic/claude-3-5-sonnet-20241022
api_key: os.environ/ANTHROPIC_API_KEY_TEAM_A

-model_name: claude-team-b
litellm_params:
model: anthropic/claude-3-5-sonnet-20241022
api_key: os.environ/ANTHROPIC_API_KEY_TEAM_B
```

Then route to specific accounts using the `model` parameter:

**Create Skill with Routing**

create\_with\_routing.sh

```
# Route to Team A - using ZIP file
curl "http://0.0.0.0:4000/v1/skills?beta=true" \
  -X POST \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "model=claude-team-a" \
  -F "display_title=Team A Skill" \
  -F "files[]=@test-skill.zip"

# Route to Team B - using direct SKILL.md upload
curl "http://0.0.0.0:4000/v1/skills?beta=true" \
  -X POST \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "model=claude-team-b" \
  -F "display_title=Team B Skill" \
  -F "files[]=@test-skill/SKILL.md;filename=test-skill/SKILL.md"
```

**List Skills with Routing**

list\_with\_routing.sh

```
# List Team A skills
curl "http://0.0.0.0:4000/v1/skills?beta=true&model=claude-team-a" \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"

# List Team B skills
curl "http://0.0.0.0:4000/v1/skills?beta=true&model=claude-team-b" \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

**Get Skill with Routing**

get\_with\_routing.sh

```
# Get skill from Team A
curl "http://0.0.0.0:4000/v1/skills/skill_01abc?beta=true&model=claude-team-a" \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"

# Get skill from Team B
curl "http://0.0.0.0:4000/v1/skills/skill_01xyz?beta=true&model=claude-team-b" \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

**Delete Skill with Routing**

delete\_with\_routing.sh

```
# Delete skill from Team A
curl "http://0.0.0.0:4000/v1/skills/skill_01abc?beta=true&model=claude-team-a" \
  -X DELETE \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"

# Delete skill from Team B
curl "http://0.0.0.0:4000/v1/skills/skill_01xyz?beta=true&model=claude-team-b" \
  -X DELETE \
  -H "X-Api-Key: sk-1234" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

## **SKILL.md Format**[​](#skillmd-format "Direct link to skillmd-format")

Skills require a `SKILL.md` file with YAML frontmatter:

SKILL.md

```
---
name: test-skill
description: A brief description of what this skill does
license: MIT
allowed-tools:
- computer_20250124
- text_editor_20250124
---

# Test Skill

Detailed instructions for Claude on how to use this skill.

## Usage

Examples and best practices...
```

### YAML Frontmatter Requirements[​](#yaml-frontmatter-requirements "Direct link to YAML Frontmatter Requirements")

FieldRequiredDescription`name`YesSkill identifier (lowercase, numbers, hyphens only). Must match the directory name.`description`YesBrief description of the skill`license`NoLicense type (e.g., MIT, Apache-2.0)`allowed-tools`NoList of Claude tools this skill can use`metadata`NoAdditional custom metadata

**Important:** The `name` field must exactly match your skill directory name. For example, if your directory is `test-skill`, the frontmatter must have `name: test-skill`.

### File Structure[​](#file-structure "Direct link to File Structure")

**Option 1: ZIP file structure**

Skills must be packaged with a top-level directory matching the skill name:

```
test-skill.zip
└── test-skill/         # Top-level folder (name must match skill name in SKILL.md)
    └── SKILL.md        # Required skill definition file
```

All files must be in the same top-level directory, and `SKILL.md` must be at the root of that directory.

**Option 2: Direct SKILL.md upload**

When uploading `SKILL.md` directly (without creating a ZIP), you must include the skill directory path in the filename parameter to preserve the required structure:

```
# The filename parameter must include the skill directory path
-F "files[]=@test-skill/SKILL.md;filename=test-skill/SKILL.md"
```

This tells the API that `SKILL.md` belongs to the `test-skill` directory.

**Important Requirements:**

- The folder name (in ZIP or filename path) **must exactly match** the `name` field in SKILL.md frontmatter
- `SKILL.md` must be in the root of the skill directory (not in a subdirectory)
- All additional files must be in the same skill directory

## **Response Format**[​](#response-format "Direct link to response-format")

### Skill Object[​](#skill-object "Direct link to Skill Object")

```
{
"id":"skill_01abc123",
"type":"skill",
"name":"my-skill",
"display_title":"My Custom Skill",
"description":"A brief description",
"created_at":"2025-01-15T10:30:00.000Z",
"updated_at":"2025-01-15T10:30:00.000Z",
"latest_version_id":"skillver_01xyz789"
}
```

### List Skills Response[​](#list-skills-response "Direct link to List Skills Response")

```
{
"data":[
{
"id":"skill_01abc",
"type":"skill",
"name":"skill-one",
"display_title":"Skill One",
"description":"First skill"
},
{
"id":"skill_02def",
"type":"skill",
"name":"skill-two",
"display_title":"Skill Two",
"description":"Second skill"
}
],
"has_more":false,
"first_id":"skill_01abc",
"last_id":"skill_02def"
}
```

## **Supported Providers**[​](#supported-providers "Direct link to supported-providers")

ProviderLink to UsageAnthropic[Usage](#quick-start---create-a-skill)