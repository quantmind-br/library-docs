---
title: ForgeCode
url: https://forgecode.dev/releases/2025/September/
source: sitemap
fetched_at: 2026-03-29T14:52:57.533278743-03:00
rendered_js: false
word_count: 863
summary: This document contains release notes detailing bug fixes, feature updates, and maintenance improvements for the ForgeCode CLI tool, including support for new AI models, ZSH integration, database enhancements, and various UI/UX improvements.
tags:
    - bug-fixes
    - feature-updates
    - cli-tool
    - ai-integration
    - zsh-support
    - database-improvements
    - user-interface
    - maintenance-updates
category: reference
---

ForgeCode ranks #1 on TermBench with 81.8% accuracy.[Learn more →](https://forgecode.dev/blog/gpt-5-4-agent-improvements)

Update to latest version !!Get the instructions from the docs

[Get Started](https://forgecode.dev/docs/)

### 🐛 Bug Fixes[​](#-bug-fixes "Direct link to 🐛 Bug Fixes")

- fix: support for STDIN via ZSH [@tusharmath](https://github.com/tusharmath) ([#1606](https://github.com/antinomyhq/forge/pull/1606))
- fix: add only files in system prompt [@laststylebender14](https://github.com/laststylebender14) ([#1608](https://github.com/antinomyhq/forge/pull/1608))

### 🧰 Maintenance[​](#-maintenance "Direct link to 🧰 Maintenance")

- chore: setup default active agent [@tusharmath](https://github.com/tusharmath) ([#1611](https://github.com/antinomyhq/forge/pull/1611))
- refactor: drop prime and parker [@tusharmath](https://github.com/tusharmath) ([#1609](https://github.com/antinomyhq/forge/pull/1609))
- fix: support for STDIN via ZSH [@tusharmath](https://github.com/tusharmath) ([#1606](https://github.com/antinomyhq/forge/pull/1606))

* * *

### 🚀 Features[​](#-features "Direct link to 🚀 Features")

- feat: add OpenAI responses API support for GPT-5 models [@sebyx07](https://github.com/sebyx07) ([#1597](https://github.com/antinomyhq/forge/pull/1597))

### 🐛 Bug Fixes[​](#-bug-fixes-1 "Direct link to 🐛 Bug Fixes")

- fix: many fixes [@tusharmath](https://github.com/tusharmath) ([#1604](https://github.com/antinomyhq/forge/pull/1604))
- fix(zsh): unset user action [@tusharmath](https://github.com/tusharmath) ([#1600](https://github.com/antinomyhq/forge/pull/1600))
- fix(zsh): handle `CTRL+C` better [@tusharmath](https://github.com/tusharmath) ([#1601](https://github.com/antinomyhq/forge/pull/1601))
- fix: sort tools by name [@tusharmath](https://github.com/tusharmath) ([#1599](https://github.com/antinomyhq/forge/pull/1599))

### 🧰 Maintenance[​](#-maintenance-1 "Direct link to 🧰 Maintenance")

- chore: improve ZSH compatibility [@tusharmath](https://github.com/tusharmath) ([#1591](https://github.com/antinomyhq/forge/pull/1591))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-2 "Direct link to 🐛 Bug Fixes")

- fix: rename current\_time to current\_date for consistency [@laststylebender14](https://github.com/laststylebender14) ([#1584](https://github.com/antinomyhq/forge/pull/1584))
- fix: load usage from conversions when used with cli commands [@laststylebender14](https://github.com/laststylebender14) ([#1575](https://github.com/antinomyhq/forge/pull/1575))
- fix: enhance SQLite connection configuration for better concurrency [@laststylebender14](https://github.com/laststylebender14) ([#1583](https://github.com/antinomyhq/forge/pull/1583))

* * *

### 🚀 Features[​](#-features-1 "Direct link to 🚀 Features")

- feat: add ZLE widget to toggle conversation pattern in input buffer [@tusharmath](https://github.com/tusharmath) ([#1571](https://github.com/antinomyhq/forge/pull/1571))

### 🐛 Bug Fixes[​](#-bug-fixes-3 "Direct link to 🐛 Bug Fixes")

- fix: minor ZSH plugin improvements [@tusharmath](https://github.com/tusharmath) ([#1581](https://github.com/antinomyhq/forge/pull/1581))
- fix: load usage from conversation [@laststylebender14](https://github.com/laststylebender14) ([#1574](https://github.com/antinomyhq/forge/pull/1574))
- fix: reset resume on `/new` [@tusharmath](https://github.com/tusharmath) ([#1576](https://github.com/antinomyhq/forge/pull/1576))
- fix: refine wording in research question handling instructions [@tusharmath](https://github.com/tusharmath) ([#1573](https://github.com/antinomyhq/forge/pull/1573))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-4 "Direct link to 🐛 Bug Fixes")

- fix: unexpected tool call failure limits being hit [@tusharmath](https://github.com/tusharmath) ([#1570](https://github.com/antinomyhq/forge/pull/1570))

* * *

### 🚀 Features[​](#-features-2 "Direct link to 🚀 Features")

- feat: show conversation id in `/info` [@tusharmath](https://github.com/tusharmath) ([#1554](https://github.com/antinomyhq/forge/pull/1554))

### 🐛 Bug Fixes[​](#-bug-fixes-5 "Direct link to 🐛 Bug Fixes")

- fix: don't exit on an invalid command [@laststylebender14](https://github.com/laststylebender14) ([#1569](https://github.com/antinomyhq/forge/pull/1569))
- fix: save forked conversations in database. [@laststylebender14](https://github.com/laststylebender14) ([#1568](https://github.com/antinomyhq/forge/pull/1568))

* * *

### 🚀 Features[​](#-features-3 "Direct link to 🚀 Features")

- feat: add support for Vertex AI provider and models [@amitksingh1490](https://github.com/amitksingh1490) ([#1553](https://github.com/antinomyhq/forge/pull/1553))

### 🐛 Bug Fixes[​](#-bug-fixes-6 "Direct link to 🐛 Bug Fixes")

- fix: toolcall error count [@tusharmath](https://github.com/tusharmath) ([#1562](https://github.com/antinomyhq/forge/pull/1562))
- fix: drop reasoning from title generator [@laststylebender14](https://github.com/laststylebender14) ([#1567](https://github.com/antinomyhq/forge/pull/1567))
- fix: update the plugin for append [@tusharmath](https://github.com/tusharmath) ([#1566](https://github.com/antinomyhq/forge/pull/1566))
- fix: performance improvements for compaction [@tusharmath](https://github.com/tusharmath) ([#1565](https://github.com/antinomyhq/forge/pull/1565))
- fix: improve ZSH plugin with support for file tagging and session [@tusharmath](https://github.com/tusharmath) ([#1561](https://github.com/antinomyhq/forge/pull/1561))
- fix: user prompt format [@tusharmath](https://github.com/tusharmath) ([#1560](https://github.com/antinomyhq/forge/pull/1560))
- fix: hide "new task" prompt if running in non-interactive mode [@tusharmath](https://github.com/tusharmath) ([#1552](https://github.com/antinomyhq/forge/pull/1552))

### 🚀 Performance[​](#-performance "Direct link to 🚀 Performance")

- fix: performance improvements for compaction [@tusharmath](https://github.com/tusharmath) ([#1565](https://github.com/antinomyhq/forge/pull/1565))

* * *

### 🚀 Features[​](#-features-4 "Direct link to 🚀 Features")

- feat: add `FORGE_HISTORY_FILE` env variable [@tusharmath](https://github.com/tusharmath) ([#1548](https://github.com/antinomyhq/forge/pull/1548))
- feat: insert `/agent-<agent-name>` aliases [@tusharmath](https://github.com/tusharmath) ([#1547](https://github.com/antinomyhq/forge/pull/1547))
- feat: add line numbers to attachments [@laststylebender14](https://github.com/laststylebender14) ([#1540](https://github.com/antinomyhq/forge/pull/1540))
- fix: improve system prompt for `muse` [@tusharmath](https://github.com/tusharmath) ([#1538](https://github.com/antinomyhq/forge/pull/1538))
- feat: add `FORGE_DUMP_AUTO_OPEN` env variable [@tusharmath](https://github.com/tusharmath) ([#1537](https://github.com/antinomyhq/forge/pull/1537))
- feat: add support for ZAI coding plan [@amitksingh1490](https://github.com/amitksingh1490) ([#1532](https://github.com/antinomyhq/forge/pull/1532))
- feat: persist conversations [@laststylebender14](https://github.com/laststylebender14) ([#1525](https://github.com/antinomyhq/forge/pull/1525))

### 🐛 Bug Fixes[​](#-bug-fixes-7 "Direct link to 🐛 Bug Fixes")

- fix: improve conversation title generation [@tusharmath](https://github.com/tusharmath) ([#1550](https://github.com/antinomyhq/forge/pull/1550))
- fix: add `libsqlite3-sys` dependency to Cargo.toml and Cargo.lock [@amitksingh1490](https://github.com/amitksingh1490) ([#1543](https://github.com/antinomyhq/forge/pull/1543))
- fix: show actual error instead of simple message [@laststylebender14](https://github.com/laststylebender14) ([#1529](https://github.com/antinomyhq/forge/pull/1529))
- fix: show attempt-completion in `/tools` for all agents [@tusharmath](https://github.com/tusharmath) ([#1545](https://github.com/antinomyhq/forge/pull/1545))
- fix: handle duplicated tool names [@tusharmath](https://github.com/tusharmath) ([#1544](https://github.com/antinomyhq/forge/pull/1544))
- fix: GLM caching improvements [@amitksingh1490](https://github.com/amitksingh1490) ([#1541](https://github.com/antinomyhq/forge/pull/1541))
- fix: show banner in interactive mode only [@laststylebender14](https://github.com/laststylebender14) ([#1535](https://github.com/antinomyhq/forge/pull/1535))

### 🧰 Maintenance[​](#-maintenance-2 "Direct link to 🧰 Maintenance")

- chore: disable fetching usage stats from forge [@laststylebender14](https://github.com/laststylebender14) ([#1534](https://github.com/antinomyhq/forge/pull/1534))

* * *

### 🚀 Features[​](#-features-5 "Direct link to 🚀 Features")

- feat: add line number in fs\_read output [@laststylebender14](https://github.com/laststylebender14) ([#1509](https://github.com/antinomyhq/forge/pull/1509))

### 🐛 Bug Fixes[​](#-bug-fixes-8 "Direct link to 🐛 Bug Fixes")

- fix: duplicate mcp tool definition [@tusharmath](https://github.com/tusharmath) ([#1527](https://github.com/antinomyhq/forge/pull/1527))
- fix: match on exact subscription [@laststylebender14](https://github.com/laststylebender14) ([#1519](https://github.com/antinomyhq/forge/pull/1519))
- refactor: simplify conversation and orchestrator [@tusharmath](https://github.com/tusharmath) ([#1513](https://github.com/antinomyhq/forge/pull/1513))

### 🧰 Maintenance[​](#-maintenance-3 "Direct link to 🧰 Maintenance")

- chore: remove unused dependencies [@tusharmath](https://github.com/tusharmath) ([#1528](https://github.com/antinomyhq/forge/pull/1528))
- chore: drop forge\_main\_neo [@tusharmath](https://github.com/tusharmath) ([#1526](https://github.com/antinomyhq/forge/pull/1526))
- feat: add image caching [@laststylebender14](https://github.com/laststylebender14) ([#1442](https://github.com/antinomyhq/forge/pull/1442))
- chore: update reedline version [@laststylebender14](https://github.com/laststylebender14) ([#1524](https://github.com/antinomyhq/forge/pull/1524))
- tests: add tests for reasoning [@laststylebender14](https://github.com/laststylebender14) ([#1505](https://github.com/antinomyhq/forge/pull/1505))
- refactor: simplify conversation and orchestrator [@tusharmath](https://github.com/tusharmath) ([#1513](https://github.com/antinomyhq/forge/pull/1513))

* * *

### 🚀 Features[​](#-features-6 "Direct link to 🚀 Features")

- feat: support for STDIN [@tusharmath](https://github.com/tusharmath) ([#1508](https://github.com/antinomyhq/forge/pull/1508))
- feat: support project specific agents under `{cwd}/.forge/agents` [@tusharmath](https://github.com/tusharmath) ([#1506](https://github.com/antinomyhq/forge/pull/1506))
- feat: add support for providing env variables for shell execution [@tusharmath](https://github.com/tusharmath) ([#1500](https://github.com/antinomyhq/forge/pull/1500))
- feat: enhance agent switch message to include title if available [@tusharmath](https://github.com/tusharmath) ([#1499](https://github.com/antinomyhq/forge/pull/1499))

### 🐛 Bug Fixes[​](#-bug-fixes-9 "Direct link to 🐛 Bug Fixes")

- fix: send reasoning settings to upstream [@laststylebender14](https://github.com/laststylebender14) ([#1501](https://github.com/antinomyhq/forge/pull/1501))
- chore: drop `gh-workflow-tailcall` and use `gh-workflow` directly [@tusharmath](https://github.com/tusharmath) ([#1503](https://github.com/antinomyhq/forge/pull/1503))

### 🧰 Maintenance[​](#-maintenance-4 "Direct link to 🧰 Maintenance")

- chore: add workflow for closing stale issues and PRs [@tusharmath](https://github.com/tusharmath) ([#1502](https://github.com/antinomyhq/forge/pull/1502))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-10 "Direct link to 🐛 Bug Fixes")

- fix: update built-in agent prompt [@tusharmath](https://github.com/tusharmath) ([#1498](https://github.com/antinomyhq/forge/pull/1498))

* * *

### 📝 Documentation[​](#-documentation "Direct link to 📝 Documentation")

- fix: remove fixed models from built-in agents [@tusharmath](https://github.com/tusharmath) ([#1497](https://github.com/antinomyhq/forge/pull/1497))

### 🐛 Bug Fixes[​](#-bug-fixes-11 "Direct link to 🐛 Bug Fixes")

- fix: remove fixed models from built-in agents [@tusharmath](https://github.com/tusharmath) ([#1497](https://github.com/antinomyhq/forge/pull/1497))
- fix: update interaction guidelines and streamline shell command execution instructions [@tusharmath](https://github.com/tusharmath) ([#1496](https://github.com/antinomyhq/forge/pull/1496))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-12 "Direct link to 🐛 Bug Fixes")

- fix: Improved metrics tracking behaviour on fs\_undo [@manthanabc](https://github.com/manthanabc) ([#1489](https://github.com/antinomyhq/forge/pull/1489))
- fix: prevent overwriting existing agent models [@tusharmath](https://github.com/tusharmath) ([#1494](https://github.com/antinomyhq/forge/pull/1494))
- fix: improve compaction focus [@tusharmath](https://github.com/tusharmath) ([#1493](https://github.com/antinomyhq/forge/pull/1493))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-13 "Direct link to 🐛 Bug Fixes")

- fix: show attempt completion in `/tools` command [@tusharmath](https://github.com/tusharmath) ([#1492](https://github.com/antinomyhq/forge/pull/1492))
- fix: add HTTP status code `408` to retry status codes [@tusharmath](https://github.com/tusharmath) ([#1490](https://github.com/antinomyhq/forge/pull/1490))
- fix: adjust indentation for item display in Info struct [@tusharmath](https://github.com/tusharmath) ([#1491](https://github.com/antinomyhq/forge/pull/1491))

* * *

### 🚀 Features[​](#-features-7 "Direct link to 🚀 Features")

- feat: improve tool display format [@tusharmath](https://github.com/tusharmath) ([#1488](https://github.com/antinomyhq/forge/pull/1488))

### 📝 Documentation[​](#-documentation-1 "Direct link to 📝 Documentation")

- fix: update tool description for file read operations [@tusharmath](https://github.com/tusharmath) ([#1487](https://github.com/antinomyhq/forge/pull/1487))

### 🐛 Bug Fixes[​](#-bug-fixes-14 "Direct link to 🐛 Bug Fixes")

- fix: update tool description for file read operations [@tusharmath](https://github.com/tusharmath) ([#1487](https://github.com/antinomyhq/forge/pull/1487))
- refactor: update tool names to remove deprecated prefixes [@tusharmath](https://github.com/tusharmath) ([#1486](https://github.com/antinomyhq/forge/pull/1486))

### 🧰 Maintenance[​](#-maintenance-5 "Direct link to 🧰 Maintenance")

- feat: improve tool display format [@tusharmath](https://github.com/tusharmath) ([#1488](https://github.com/antinomyhq/forge/pull/1488))
- refactor: update tool names to remove deprecated prefixes [@tusharmath](https://github.com/tusharmath) ([#1486](https://github.com/antinomyhq/forge/pull/1486))
- refactor: drop agents from workflow [@tusharmath](https://github.com/tusharmath) ([#1483](https://github.com/antinomyhq/forge/pull/1483))
- refactor: remove operating agents from variables [@tusharmath](https://github.com/tusharmath) ([#1484](https://github.com/antinomyhq/forge/pull/1484))
- chore: rename templates from .hbs to .md [@tusharmath](https://github.com/tusharmath) ([#1482](https://github.com/antinomyhq/forge/pull/1482))
- chore: simplify forge.yaml [@tusharmath](https://github.com/tusharmath) ([#1481](https://github.com/antinomyhq/forge/pull/1481))

* * *

- feat: add HTTP client certificate configuration [@sabiz](https://github.com/sabiz) ([#1472](https://github.com/antinomyhq/forge/pull/1472))

### 🚀 Features[​](#-features-8 "Direct link to 🚀 Features")

- feat: add `/sage` command [@tusharmath](https://github.com/tusharmath) ([#1478](https://github.com/antinomyhq/forge/pull/1478))
- feat: update token summary format [@tusharmath](https://github.com/tusharmath) ([#1477](https://github.com/antinomyhq/forge/pull/1477))

### 🐛 Bug Fixes[​](#-bug-fixes-15 "Direct link to 🐛 Bug Fixes")

- fix: update citation format [@tusharmath](https://github.com/tusharmath) ([#1476](https://github.com/antinomyhq/forge/pull/1476))

### 🧰 Maintenance[​](#-maintenance-6 "Direct link to 🧰 Maintenance")

- feat: add `/sage` command [@tusharmath](https://github.com/tusharmath) ([#1478](https://github.com/antinomyhq/forge/pull/1478))
- chore(deps): bump tracing-subscriber from 0.3.19 to 0.3.20 @[dependabot\[bot\]](https://github.com/apps/dependabot) (#1469)

<!--THE END-->

- [v0.121.1](#v01211)
- [v0.121.0](#v01210)
- [v0.120.1](#v01201)
- [v0.120.0](#v01200)
- [v0.119.1](#v01191)
- [v0.119.0](#v01190)
- [v0.118.0](#v01180)
- [v0.117.0](#v01170)
- [v0.116.0](#v01160)
- [v0.115.0](#v01150)
- [v0.114.4](#v01144)
- [v0.114.3](#v01143)
- [v0.114.2](#v01142)
- [v0.114.1](#v01141)
- [v0.114.0](#v01140)
- [v0.113.0](#v01130)