---
title: ForgeCode
url: https://forgecode.dev/releases/2025/July/
source: sitemap
fetched_at: 2026-03-29T14:52:47.490173052-03:00
rendered_js: false
word_count: 1183
summary: This document contains release notes and changelog entries for the ForgeCode project, detailing bug fixes, new features, maintenance updates, and documentation improvements across multiple releases.
tags:
    - changelog
    - bug-fixes
    - features
    - maintenance
    - documentation
    - releases
category: reference
---

ForgeCode ranks #1 on TermBench with 81.8% accuracy.[Learn more →](https://forgecode.dev/blog/gpt-5-4-agent-improvements)

Update to latest version !!Get the instructions from the docs

[Get Started](https://forgecode.dev/docs/)

### 🐛 Bug Fixes[​](#-bug-fixes "Direct link to 🐛 Bug Fixes")

- fix: improve error message handling [@tusharmath](https://github.com/tusharmath) ([#1302](https://github.com/antinomyhq/forge/pull/1302))
- fix: use antinomy domain [@tusharmath](https://github.com/tusharmath) ([#1300](https://github.com/antinomyhq/forge/pull/1300))

### 🧰 Maintenance[​](#-maintenance "Direct link to 🧰 Maintenance")

- refactor: move common event parsing logic outside [@tusharmath](https://github.com/tusharmath) ([#1303](https://github.com/antinomyhq/forge/pull/1303))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-1 "Direct link to 🐛 Bug Fixes")

- fix: support TLS version configuration via env variables [@tusharmath](https://github.com/tusharmath) ([#1299](https://github.com/antinomyhq/forge/pull/1299))

* * *

### 🚀 Features[​](#-features "Direct link to 🚀 Features")

- fix: integrate JSON repair [@ssddOnTop](https://github.com/ssddOnTop) ([#1292](https://github.com/antinomyhq/forge/pull/1292))
- feat: added info command (#1273) [@manthanabc](https://github.com/manthanabc) ([#1275](https://github.com/antinomyhq/forge/pull/1275))

### 📝 Documentation[​](#-documentation "Direct link to 📝 Documentation")

- fix: update tool use formatting rules to clarify JSON structure [@amitksingh1490](https://github.com/amitksingh1490) ([#1291](https://github.com/antinomyhq/forge/pull/1291))

### 🐛 Bug Fixes[​](#-bug-fixes-2 "Direct link to 🐛 Bug Fixes")

- fix: sort the models based on the names [@Achyutha](https://github.com/Achyutha) ([#1284](https://github.com/antinomyhq/forge/pull/1284))
- fix: integrate JSON repair [@ssddOnTop](https://github.com/ssddOnTop) ([#1292](https://github.com/antinomyhq/forge/pull/1292))

### 🧰 Maintenance[​](#-maintenance-1 "Direct link to 🧰 Maintenance")

- fix: consolidate HTTP client implementations and use TLS configurators [@tusharmath](https://github.com/tusharmath) ([#1288](https://github.com/antinomyhq/forge/pull/1288))

* * *

### 🚀 Features[​](#-features-1 "Direct link to 🚀 Features")

- feat: Support for `/retry` [@jayantpranjal0](https://github.com/jayantpranjal0) ([#1262](https://github.com/antinomyhq/forge/pull/1262))

### 🐛 Bug Fixes[​](#-bug-fixes-3 "Direct link to 🐛 Bug Fixes")

- fix: mcp `ToolName` sanitization [@tusharmath](https://github.com/tusharmath) ([#1274](https://github.com/antinomyhq/forge/pull/1274))
- fix: add `Cross.toml` for build environment configuration [@ssddOnTop](https://github.com/ssddOnTop) ([#1272](https://github.com/antinomyhq/forge/pull/1272))

### 🧰 Maintenance[​](#-maintenance-2 "Direct link to 🧰 Maintenance")

- refactor: simplify tracking logic [@tusharmath](https://github.com/tusharmath) ([#1276](https://github.com/antinomyhq/forge/pull/1276))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-4 "Direct link to 🐛 Bug Fixes")

- fix: update error element to `tool_call_error` in templates [@tusharmath](https://github.com/tusharmath) ([#1254](https://github.com/antinomyhq/forge/pull/1254))
- Revert "fix: drop reasoning normalizer" [@laststylebender14](https://github.com/laststylebender14) ([#1245](https://github.com/antinomyhq/forge/pull/1245))
- fix: show usage information [@ssddOnTop](https://github.com/ssddOnTop) ([#1250](https://github.com/antinomyhq/forge/pull/1250))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-5 "Direct link to 🐛 Bug Fixes")

- fix: update provider state after successful login [@ssddOnTop](https://github.com/ssddOnTop) ([#1234](https://github.com/antinomyhq/forge/pull/1234))
- fix: enhance path formatting for display [@ssddOnTop](https://github.com/ssddOnTop) ([#1233](https://github.com/antinomyhq/forge/pull/1233))

### 🧰 Maintenance[​](#-maintenance-3 "Direct link to 🧰 Maintenance")

- chore: add `cached_tokens` usage to tracing [@jayantpranjal0](https://github.com/jayantpranjal0) ([#1200](https://github.com/antinomyhq/forge/pull/1200))
- chore: add FORGE\_SUPPRESS\_RETRY\_ERRORS env variable to hide retry error [@ssddOnTop](https://github.com/ssddOnTop) ([#1231](https://github.com/antinomyhq/forge/pull/1231))

* * *

### 🚀 Features[​](#-features-2 "Direct link to 🚀 Features")

- feat: use fuzzy find in autocomplete [@ssddOnTop](https://github.com/ssddOnTop) ([#1214](https://github.com/antinomyhq/forge/pull/1214))

### 🐛 Bug Fixes[​](#-bug-fixes-6 "Direct link to 🐛 Bug Fixes")

- fix: use custom binary file detector [@laststylebender14](https://github.com/laststylebender14) ([#1225](https://github.com/antinomyhq/forge/pull/1225))
- fix: drop reasoning normalizer [@laststylebender14](https://github.com/laststylebender14) ([#1216](https://github.com/antinomyhq/forge/pull/1216))
- fix: use cross for musl build [@ssddOnTop](https://github.com/ssddOnTop) ([#1210](https://github.com/antinomyhq/forge/pull/1210))

### 🧰 Maintenance[​](#-maintenance-4 "Direct link to 🧰 Maintenance")

- chore: rename provider to openai [@tusharmath](https://github.com/tusharmath) ([#1199](https://github.com/antinomyhq/forge/pull/1199))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-7 "Direct link to 🐛 Bug Fixes")

- fix: ensure reasoning config is dropped [@tusharmath](https://github.com/tusharmath) ([#1198](https://github.com/antinomyhq/forge/pull/1198))

* * *

### 🚀 Features[​](#-features-3 "Direct link to 🚀 Features")

- fix: remove reasoning tokens after compaction [@tusharmath](https://github.com/tusharmath) ([#1196](https://github.com/antinomyhq/forge/pull/1196))
- feat: support for current working directory [@tusharmath](https://github.com/tusharmath) ([#1174](https://github.com/antinomyhq/forge/pull/1174))

### 🧰 Maintenance[​](#-maintenance-5 "Direct link to 🧰 Maintenance")

- feat: support for current working directory [@tusharmath](https://github.com/tusharmath) ([#1174](https://github.com/antinomyhq/forge/pull/1174))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-8 "Direct link to 🐛 Bug Fixes")

- fix: use actual usage data for compaction [@tusharmath](https://github.com/tusharmath) ([#1176](https://github.com/antinomyhq/forge/pull/1176))
- fix: update binary extensions [@tusharmath](https://github.com/tusharmath) ([#1193](https://github.com/antinomyhq/forge/pull/1193))
- fix: always skip searching through binary files in fs\_search [@laststylebender14](https://github.com/laststylebender14) ([#1187](https://github.com/antinomyhq/forge/pull/1187))
- fix: add support for viewing MCP responses [@tusharmath](https://github.com/tusharmath) ([#1175](https://github.com/antinomyhq/forge/pull/1175))
- fix: update token reporting logic in ForgePrompt [@tusharmath](https://github.com/tusharmath) ([#1179](https://github.com/antinomyhq/forge/pull/1179))
- fix: drop hickory dns resolver [@laststylebender14](https://github.com/laststylebender14) ([#1190](https://github.com/antinomyhq/forge/pull/1190))
- fix: change default option to continue in confirmation prompt [@laststylebender14](https://github.com/laststylebender14) ([#1186](https://github.com/antinomyhq/forge/pull/1186))

### 🧰 Maintenance[​](#-maintenance-6 "Direct link to 🧰 Maintenance")

- chore: add label for OnlyDust Wave Hackathon [@amitksingh1490](https://github.com/amitksingh1490) ([#1191](https://github.com/antinomyhq/forge/pull/1191))

* * *

### 📝 Documentation[​](#-documentation-1 "Direct link to 📝 Documentation")

- doc: update the setting name (max\_tool\_failure\_per\_turn) [@laststylebender14](https://github.com/laststylebender14) ([#1154](https://github.com/antinomyhq/forge/pull/1154))

### 🐛 Bug Fixes[​](#-bug-fixes-9 "Direct link to 🐛 Bug Fixes")

- fix: use ranges in file attachments [@tusharmath](https://github.com/tusharmath) ([#1162](https://github.com/antinomyhq/forge/pull/1162))
- fix: use `hickory-dns` resolver instead of Gai [@laststylebender14](https://github.com/laststylebender14) ([#1130](https://github.com/antinomyhq/forge/pull/1130))
- fix: signature is not required for summarization [@laststylebender14](https://github.com/laststylebender14) ([#1158](https://github.com/antinomyhq/forge/pull/1158))
- fix: skip binary files while searching [@laststylebender14](https://github.com/laststylebender14) ([#1157](https://github.com/antinomyhq/forge/pull/1157))

### 🧰 Maintenance[​](#-maintenance-7 "Direct link to 🧰 Maintenance")

- chore(deps): update strum monorepo to v0.27.2 @[renovate\[bot\]](https://github.com/apps/renovate) (#1145)

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-10 "Direct link to 🐛 Bug Fixes")

- fix: kimi2 tool call errors [@ssddOnTop](https://github.com/ssddOnTop) ([#1144](https://github.com/antinomyhq/forge/pull/1144))
- fix: use search directory for relative paths in search results instead of CWD [@tusharmath](https://github.com/tusharmath) ([#1139](https://github.com/antinomyhq/forge/pull/1139))

### 🧰 Maintenance[​](#-maintenance-8 "Direct link to 🧰 Maintenance")

- chore: add forge\_main\_neo [@tusharmath](https://github.com/tusharmath) ([#998](https://github.com/antinomyhq/forge/pull/998))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-11 "Direct link to 🐛 Bug Fixes")

- fix: file search invalid utf8 issue [@ssddOnTop](https://github.com/ssddOnTop) ([#1132](https://github.com/antinomyhq/forge/pull/1132))

### 🧰 Maintenance[​](#-maintenance-9 "Direct link to 🧰 Maintenance")

- refactor: consolidate inquire select functionality into select module [@echozyr2001](https://github.com/echozyr2001) ([#1128](https://github.com/antinomyhq/forge/pull/1128))
- chore: log file update stats [@laststylebender14](https://github.com/laststylebender14) ([#1118](https://github.com/antinomyhq/forge/pull/1118))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-12 "Direct link to 🐛 Bug Fixes")

- fix: handle tool calls from Kimi2 [@tusharmath](https://github.com/tusharmath) ([#1121](https://github.com/antinomyhq/forge/pull/1121))

### 🧰 Maintenance[​](#-maintenance-10 "Direct link to 🧰 Maintenance")

- chore: update edition to 2024 [@tusharmath](https://github.com/tusharmath) ([#1125](https://github.com/antinomyhq/forge/pull/1125))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-13 "Direct link to 🐛 Bug Fixes")

- fix: replace tracker error logging with tracing [@tusharmath](https://github.com/tusharmath) ([#1117](https://github.com/antinomyhq/forge/pull/1117))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-14 "Direct link to 🐛 Bug Fixes")

- fix: scripts for `npx` for Windows

* * *

### 🛠️ Refactors[​](#%EF%B8%8F-refactors "Direct link to 🛠️ Refactors")

- refactor: consolidate `forge_api_url` usage @tusharmath, @autofix-ci\[bot] (#1104)

### 🐛 Bug Fixes[​](#-bug-fixes-15 "Direct link to 🐛 Bug Fixes")

- fix: output reasoning tokens only if supported by model [@laststylebender14](https://github.com/laststylebender14) ([#1105](https://github.com/antinomyhq/forge/pull/1105))
- fix: update HTTP-Referer header to point to the new forgecode.dev URL [@amitksingh1490](https://github.com/amitksingh1490) ([#1080](https://github.com/antinomyhq/forge/pull/1080))
- fix: improve LLM caching [@tusharmath](https://github.com/tusharmath) ([#1088](https://github.com/antinomyhq/forge/pull/1088))
- fix: use `max_completion_tokens` instead of `max_tokens` for open-ai compatible providers [@laststylebender14](https://github.com/laststylebender14) ([#1086](https://github.com/antinomyhq/forge/pull/1086))
- fix: use blocking thread to readline [@tusharmath](https://github.com/tusharmath) ([#1085](https://github.com/antinomyhq/forge/pull/1085))

### 🧰 Maintenance[​](#-maintenance-11 "Direct link to 🧰 Maintenance")

- fix: share release builds between channels [@tusharmath](https://github.com/tusharmath) ([#1114](https://github.com/antinomyhq/forge/pull/1114))
- fix: regenerate binaries on publish [@laststylebender14](https://github.com/laststylebender14) ([#1113](https://github.com/antinomyhq/forge/pull/1113))
- chore: remove `forge_domain` direct dependency on crates [@tusharmath](https://github.com/tusharmath) ([#1084](https://github.com/antinomyhq/forge/pull/1084))
- chore: update labels.yml [@ssddOnTop](https://github.com/ssddOnTop) ([#1082](https://github.com/antinomyhq/forge/pull/1082))
- chore: add permissions to GitHub Label Sync workflow [@ssddOnTop](https://github.com/ssddOnTop) ([#1078](https://github.com/antinomyhq/forge/pull/1078))
- chore: add GitHub Label Sync workflow and related tests [@ssddOnTop](https://github.com/ssddOnTop) ([#1077](https://github.com/antinomyhq/forge/pull/1077))

### 📝 Documentation[​](#-documentation-2 "Direct link to 📝 Documentation")

- docs: update readme for `max_requests_per_turn` and `tool_max_failure_limit` [@laststylebender14](https://github.com/laststylebender14) ([#1027](https://github.com/antinomyhq/forge/pull/1027))

* * *

### 📝 Documentation[​](#-documentation-3 "Direct link to 📝 Documentation")

- docs: update readme for `max_requests_per_turn` and `tool_max_failure_limit` [@laststylebender14](https://github.com/laststylebender14) ([#1027](https://github.com/antinomyhq/forge/pull/1027))

### 🐛 Bug Fixes[​](#-bug-fixes-16 "Direct link to 🐛 Bug Fixes")

- fix: update HTTP-Referer header to point to the new forgecode.dev URL [@amitksingh1490](https://github.com/amitksingh1490) ([#1080](https://github.com/antinomyhq/forge/pull/1080))
- fix: improve LLM caching [@tusharmath](https://github.com/tusharmath) ([#1088](https://github.com/antinomyhq/forge/pull/1088))
- fix: use `max_completion_tokens` instead of `max_tokens` for open-ai compatible providers [@laststylebender14](https://github.com/laststylebender14) ([#1086](https://github.com/antinomyhq/forge/pull/1086))
- fix: use blocking thread to readline [@tusharmath](https://github.com/tusharmath) ([#1085](https://github.com/antinomyhq/forge/pull/1085))

### 🧰 Maintenance[​](#-maintenance-12 "Direct link to 🧰 Maintenance")

- chore: remove forge\_domain direct dependency on crates [@tusharmath](https://github.com/tusharmath) ([#1084](https://github.com/antinomyhq/forge/pull/1084))
- chore: update labels.yml [@ssddOnTop](https://github.com/ssddOnTop) ([#1082](https://github.com/antinomyhq/forge/pull/1082))
- chore: add permissions to GitHub Label Sync workflow [@ssddOnTop](https://github.com/ssddOnTop) ([#1078](https://github.com/antinomyhq/forge/pull/1078))
- chore: add GitHub label sync workflow and related tests [@ssddOnTop](https://github.com/ssddOnTop) ([#1077](https://github.com/antinomyhq/forge/pull/1077))

* * *

### 🚀 Features[​](#-features-4 "Direct link to 🚀 Features")

- chore: integrate `provider_auth_id` [@ssddOnTop](https://github.com/ssddOnTop) ([#1072](https://github.com/antinomyhq/forge/pull/1072))
- feat(provider): implement model caching with cache-first pattern [@tusharmath](https://github.com/tusharmath) ([#1071](https://github.com/antinomyhq/forge/pull/1071))
- feat: enhance conversation compaction with per-trigger thresholds and turn-end support [@tusharmath](https://github.com/tusharmath) ([#1068](https://github.com/antinomyhq/forge/pull/1068))
- feat: add x.ai provider support with API integration [@amitksingh1490](https://github.com/amitksingh1490) ([#1066](https://github.com/antinomyhq/forge/pull/1066))

### 🐛 Bug Fixes[​](#-bug-fixes-17 "Direct link to 🐛 Bug Fixes")

- fix: reasoning with compaction [@laststylebender14](https://github.com/laststylebender14) ([#1059](https://github.com/antinomyhq/forge/pull/1059))
- fix: `/dump` Errors when there's no `ConversationId` [@Achyutha](https://github.com/Achyutha) ([#1065](https://github.com/antinomyhq/forge/pull/1065))
- fix: increase default connect timeout [@ssddOnTop](https://github.com/ssddOnTop) ([#1070](https://github.com/antinomyhq/forge/pull/1070))
- fix: run chat request and compaction in parallel [@ssddOnTop](https://github.com/ssddOnTop) ([#1067](https://github.com/antinomyhq/forge/pull/1067))

### 🧰 Maintenance[​](#-maintenance-13 "Direct link to 🧰 Maintenance")

- chore: integrate `provider_auth_id` [@ssddOnTop](https://github.com/ssddOnTop) ([#1072](https://github.com/antinomyhq/forge/pull/1072))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-18 "Direct link to 🐛 Bug Fixes")

- fix: update default `read_timeout` to 5 minutes [@tusharmath](https://github.com/tusharmath) ([#1064](https://github.com/antinomyhq/forge/pull/1064))
- fix: cache posthog client [@tusharmath](https://github.com/tusharmath) ([#1063](https://github.com/antinomyhq/forge/pull/1063))
- fix: remove auto compaction after each turn [@tusharmath](https://github.com/tusharmath) ([#1062](https://github.com/antinomyhq/forge/pull/1062))

* * *

### 🐛 Bug Fixes[​](#-bug-fixes-19 "Direct link to 🐛 Bug Fixes")

- fix: error tracing before exiting [@amitksingh1490](https://github.com/amitksingh1490) ([#1058](https://github.com/antinomyhq/forge/pull/1058))
- fix: add JSON parse error handling to retry logic [@ssddOnTop](https://github.com/ssddOnTop) ([#1056](https://github.com/antinomyhq/forge/pull/1056))
- fix: use `auth_provider_id` instead of `email` [@ssddOnTop](https://github.com/ssddOnTop) ([#1054](https://github.com/antinomyhq/forge/pull/1054))
- fix: panic while writing app config without parent dirs [@ssddOnTop](https://github.com/ssddOnTop) ([#1057](https://github.com/antinomyhq/forge/pull/1057))
- fix: add new line when appending [@laststylebender14](https://github.com/laststylebender14) ([#1052](https://github.com/antinomyhq/forge/pull/1052))
- fix(deps): update rust crate thiserror to v2 @[renovate\[bot\]](https://github.com/apps/renovate) (#1043)

### 🧰 Maintenance[​](#-maintenance-14 "Direct link to  🧰 Maintenance")

- chore: add login event [@ssddOnTop](https://github.com/ssddOnTop) ([#1035](https://github.com/antinomyhq/forge/pull/1035))

* * *

- Update README.md [@amitksingh1490](https://github.com/amitksingh1490) ([#1036](https://github.com/antinomyhq/forge/pull/1036))

### 🐛 Bug Fixes[​](#-bug-fixes-20 "Direct link to 🐛 Bug Fixes")

- fix: resolve login error by ensuring provider initialization in UI state [@ssddOnTop](https://github.com/ssddOnTop) ([#1049](https://github.com/antinomyhq/forge/pull/1049))
- fix: add environment variable support for HTTP connect timeouts [@tusharmath](https://github.com/tusharmath) ([#1046](https://github.com/antinomyhq/forge/pull/1046))
- fix: update login terminology for consistency in commands and UI messages [@tusharmath](https://github.com/tusharmath) ([#1034](https://github.com/antinomyhq/forge/pull/1034))

### 🧰 Maintenance[​](#-maintenance-15 "Direct link to 🧰 Maintenance")

- chore(deps): update rust crate syn to v2.0.104 @[renovate\[bot\]](https://github.com/apps/renovate) (#1042)
- chore(deps): update rust crate anyhow to v1.0.98 @[renovate\[bot\]](https://github.com/apps/renovate) (#1041)

* * *

### 🚀 Features[​](#-features-5 "Direct link to 🚀 Features")

- feat: display reasoning tokens [@laststylebender14](https://github.com/laststylebender14) ([#1025](https://github.com/antinomyhq/forge/pull/1025))
- feat: implement tool failure limit in orchestrator [@laststylebender14](https://github.com/laststylebender14) ([#1024](https://github.com/antinomyhq/forge/pull/1024))
- feat: ask if user wish to continue or not on `max_request_per_turn` [@laststylebender14](https://github.com/laststylebender14) ([#1014](https://github.com/antinomyhq/forge/pull/1014))
- feat: implement login and logout functionality [@ssddOnTop](https://github.com/ssddOnTop) ([#838](https://github.com/antinomyhq/forge/pull/838))
- feat: add replace-all variant to patch tool [@laststylebender14](https://github.com/laststylebender14) ([#1011](https://github.com/antinomyhq/forge/pull/1011))

### 🐛 Bug Fixes[​](#-bug-fixes-21 "Direct link to 🐛 Bug Fixes")

- fix: remove Rust toolchain update step from CI jobs and add rust-toolchain [@amitksingh1490](https://github.com/amitksingh1490) ([#1032](https://github.com/antinomyhq/forge/pull/1032))
- refactor: correct limit [@tusharmath](https://github.com/tusharmath) ([#1030](https://github.com/antinomyhq/forge/pull/1030))
- fix: stop spinner after login completion [@ssddOnTop](https://github.com/ssddOnTop) ([#1029](https://github.com/antinomyhq/forge/pull/1029))
- fix: ask agent to self reflect on errors [@laststylebender14](https://github.com/laststylebender14) ([#1023](https://github.com/antinomyhq/forge/pull/1023))
- fix: add citation rule for code references in prompts [@laststylebender14](https://github.com/laststylebender14) ([#1017](https://github.com/antinomyhq/forge/pull/1017))
- fix: read larger chunks whenever possible [@laststylebender14](https://github.com/laststylebender14) ([#1009](https://github.com/antinomyhq/forge/pull/1009))
- fix: report more readable errors back to LLM [@laststylebender14](https://github.com/laststylebender14) ([#1016](https://github.com/antinomyhq/forge/pull/1016))
- chore: add tracker for panic hook [@tusharmath](https://github.com/tusharmath) ([#1022](https://github.com/antinomyhq/forge/pull/1022))
- fix: display retry events on cli [@laststylebender14](https://github.com/laststylebender14) ([#1010](https://github.com/antinomyhq/forge/pull/1010))
- fix: replace panic with proper error handling in API key resolution [@echozyr2001](https://github.com/echozyr2001) ([#1013](https://github.com/antinomyhq/forge/pull/1013))

### 🧰 Maintenance[​](#-maintenance-16 "Direct link to 🧰 Maintenance")

- chore: use standard ignore filters in walker [@laststylebender14](https://github.com/laststylebender14) ([#1015](https://github.com/antinomyhq/forge/pull/1015))
- chore: add `Requesty` as a Provider [@Thibault00](https://github.com/Thibault00) ([#1018](https://github.com/antinomyhq/forge/pull/1018))

<!--THE END-->

- [v0.104.2](#v01042)
- [v0.104.1](#v01041)
- [v0.104.0](#v01040)
- [v0.103.0](#v01030)
- [v0.102.2](#v01022)
- [v0.102.1](#v01021)
- [v0.102.0](#v01020)
- [v0.101.1](#v01011)
- [v0.101.0](#v01010)
- [v0.100.8](#v01008)
- [v0.100.7](#v01007)
- [v0.100.6](#v01006)
- [v0.100.5](#v01005)
- [v0.100.4](#v01004)
- [v0.100.3](#v01003)
- [v0.100.2](#v01002)
- [v0.100.1](#v01001)
- [v0.100.0](#v01000)
- [v0.99.0](#v0990)
- [v0.98.3](#v0983)
- [v0.98.2](#v0982)
- [v0.98.1](#v0981)
- [v0.98.0](#v0980)