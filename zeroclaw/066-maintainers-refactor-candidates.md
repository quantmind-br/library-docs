---
title: Refactor candidates
date: 2026-05-05T00:00:00Z
optimized: true
tags:
  - rust
  - code-quality
  - refactoring
  - technical-debt
  - error-handling
  - best-practices
  - code-audit
---

# Refactor Candidates

Các file source lớn nhất trong `src/`, xếp hạng theo mức độ nghiêm trọng. Mỗi file làm nhiều việc trong một file, gây hại cho khả năng đọc, khả năng test, và tần suất conflict merge.

| File | Lines | Vấn đề |
|---|---|---|
| `config/schema.rs` | 7,647 | Mọi struct config cho toàn bộ hệ thống trong một file |
| `onboard/wizard.rs` | 7,200 | Toàn bộ flow onboarding trong một function-like blob |
| `channels/mod.rs` | 6,591 | Channel factory + shared logic + tất cả wiring |
| `agent/loop_.rs` | 5,599 | Toàn bộ vòng lặp orchestration agent |
| `channels/telegram.rs` | 4,606 | Một channel impl không nên lớn như vậy |
| `providers/mod.rs` | 2,903 | Provider factory + shared conversion logic |
| `gateway/mod.rs` | 2,777 | HTTP server setup + middleware + routing |

---

## Ghi chú bổ sung

- `tools/mod.rs` (635 lines) có function factory `all_tools_with_runtime()` 13 tham số sẽ tệ hơn khi số lượng tools tăng. Cân nhắc pattern registry/builder.
- `security/policy.rs` (2,338 lines) trộn lẫn policy definition, action tracking, và validation — có thể tách theo concern.
- `providers/compatible.rs` (2,892 lines) và `providers/gemini.rs` (2,142 lines) lớn cho implementation provider đơn lẻ — có thể đang trộn lẫn HTTP client logic, response parsing, và tool conversion.

### Module sai vị trí: `channels/tts.rs` → `tools/`

`channels/tts.rs` (642 lines, merge trong PR #2994) là hệ thống tổng hợp TTS multi-provider. Nó không phải là channel — không implement `Channel` hoặc cung cấp giao diện messaging hai chiều. TTS là khả năng agent gọi để sản xuất audio output, phù hợp trait `Tool` (`src/tools/traits.rs`). Nó nên được di chuyển đến `src/tools/tts.rs` với implementation `Tool` tương ứng, và các loại config nên được tách khỏi section `channels` của `schema.rs` vào namespace config `[tools.tts]`. Tính đến lúc merge, module không được tích hợp vào bất kỳ code gọi nào (re-exports là `#[allow(unused_imports)]`), nên di chuyển này có tác động runtime bằng 0.

---

## Best Practices Audit Findings

Findings từ review best practices Rust/Python tổng quát (không theo quy ước project cụ thể).

### Critical: `.unwrap()` trong code production (~2,800 instances)

`.unwrap()` xuất hiện trong I/O paths, serialization, và modules nhạy cảm bảo mật ngoài test code. Ví dụ:

```rust
// cost/tracker.rs
writeln!(file, "{}", serde_json::to_string(&old_record).unwrap()).unwrap();
file.sync_all().unwrap();
```

Best practice Rust: dùng `.context("msg")?` hoặc handle errors tường minh. Mỗi unwrap là potential panic runtime trên transient failures.

### Critical: `panic!` trong paths production (28+ instances)

Providers, pairing, và routing CLI dùng `panic!` thay vì trả về errors:

```rust
// providers/bedrock.rs
panic!("Expected ToolResult block");
// security/pairing.rs
panic!("Generated 10 pairs of codes and all were collisions — CSPRNG failure");
```

Nên là `bail!()` hoặc variants error có type — panics không recoverable và crash process.

### Critical: Suppression global clippy (32+ lints)

`main.rs` và `lib.rs` suppress `too_many_lines`, `similar_names`, `dead_code`, `missing_errors_doc`, và nhiều lints khác ở level crate. Điều này ẩn đi violations mới khi chúng tích lũy. Best practice: suppress per-function với comment justification, không toàn cục.

### High: Swallowing errors im lặng (`let _ = ...` trên Results, 30+ instances)

Gateway, WebSocket, và skill sync paths discard `Result` values im lặng:

```rust
let _ = state.event_tx.send(serde_json::json!({...})).await;
let _ = sender.send(Message::Text(err.to_string().into())).await;
let _ = mark_open_skills_synced(&repo_dir);
```

Ít nhất nên `tracing::warn!` khi thất bại. Drops im lặng làm debug phân tán gần như không thể.

### High: God struct — `Config` với 30+ fields

Mọi subsystem cần bất kỳ config đều phải giữ toàn bộ struct `Config`, tạo coupling ngầm và setup test phình to. Best practice: truyền slices config hẹp hoặc objects config bounded trait.

### High: Code bảo mật không cô lập

Shell command validation (300+ lines parsing quote-aware), webhook signature verification, và pairing logic nhúng trong files đa mục đích lớn thay vì modules cô lập. Điều này làm audit bảo mật phức tạp và tăng risk regression từ thay đổi không liên quan.

### Medium: `.clone()` quá mức (~1,227 instances)

Paths refresh token/auth clone structs lớn mỗi nhánh. Hot paths như token access có thể dùng `Cow<'_>` hoặc `Arc` thay vì clone đầy đủ.

### Medium: Độ sâu test — chủ yếu smoke tests

193 modules test tồn tại (tốt coverage cấu trúc), nhưng hầu hết chỉ assertions giá trị đơn giản. Thiếu:

- Property-based testing cho parsers/validators
- Integration tests cho flows multi-module
- Fuzz testing cho shell command parser (security surface)
- Mock-based tests cho paths network-dependent

### Medium: Count dependencies (82 direct)

Project claim tối ưu size là mục tiêu (`opt-level = "z"`, `lto = "fat"`) trong khi tích lũy deps nặng optional như `matrix-sdk` (full E2EE crypto) và `probe-rs` (50+ transitive deps). Sự căng thẳng giữa mục tiêu size và breadth feature chưa được giải quyết.

### Low: `unsafe` không có safety comments

Hai instances trong `src/service/mod.rs` cho `libc::getuid()` — không có comment `// SAFETY:`. Có thể dùng wrapper an toàn của crate `nix` thay thế.

### Low: Chất lượng code Python

Thư mục con `python/` có minimal type hints, không docstrings trên functions quan trọng, và không tests tham số hóa. Không nhất quán với side Rust's rigor.

### Low: `rustfmt.toml` tối thiểu

Chỉ set `edition = "2021"`. Với project size này, cấu hình `max_width`, `imports_granularity`, `group_imports` sẽ enforce consistency khi contributor tăng.

### Đã giải quyết: Hardening bảo mật CI/CD (P1/P2)

~~Third-party actions pin vào tags mutable; workflows release grant write permissions rộng; không job gate composite cho branch protection; tools bảo mật compile từ source mỗi PR.~~

**Đã fix trong nhánh `cicd-best-practices`:**
- Tất cả actions third-party SHA-pin (P1)
- Permissions workflows release scoped per-job (P1)
- Job composite `Gate` thêm vào checks PR (P2)
- Tools bảo mật cài qua binaries pre-built (P2)

---

## Khuyến nghị ưu tiên

1. **Thay thế unwraps/panics trong code non-test** bằng propagation error phù hợp — impact ổn định cao nhất.
2. **Tách modules god** — tách orchestration runtime khỏi `channels/mod.rs`, cô lập parsing bảo mật, chia nhỏ `Config` thành sub-configs.
3. **Bỏ suppression global clippy** — fix violations riêng lẻ hoặc thêm `#[allow]` per-item với lý do.
4. **Thay thế `let _ =` trên Results** bằng ít nhất `tracing::warn!` logging.
5. **Thêm property/fuzz tests** cho security-surface parsers (shell command validation, webhook signatures).

---

## Refactorings cấu trúc bị hoãn

Thay đổi hoãn từ đợt cleanup project. Mỗi entry bao gồm lý do và phạm vi.

### Đổi tên `src/sop/` → `src/runbooks/`

**Tại sao:** "SOP" là thuật ngữ chuyên ngành nặng và không truyền đạt chức năng module. "Runbooks" là thuật ngữ industry-standard cho procedures tự động trigger-driven với gates approval.

**Phạm vi:** Đổi tên module (`src/sop/` → `src/runbooks/`), cập nhật config keys (`[sop]` → `[runbooks]`), subcommand CLI (`zeroclaw sop` → `zeroclaw runbook`), tất cả types internal (`Sop*` → `Runbook*`), docs (`docs/sop/` → matching new structure), và references trong CLAUDE.md.

### Consolidate i18n docs vào `docs/i18n/<locale>/`

**Tại sao:** Translations tiếng Việt hiện tại tồn tại ở ba nơi: `docs/i18n/vi/` (canonical per CLAUDE.md), `docs/vi/` (duplicate cũ 17 files lệch), và `docs/*.vi.md` (5 files suffix scattered). Locales khác (zh-CN, ja, ru, fr) có SUMMARY + README files scattered trong root `docs/`.

**Kế hoạch:**
- Giữ `docs/i18n/vi/` là canonical; xóa `docs/vi/` (duplicate cũ)
- Di chuyển `docs/*.vi.md` files vào `docs/i18n/vi/` tại paths matching
- Di chuyển `docs/SUMMARY.*.md` và `docs/README.*.md` vào `docs/i18n/<locale>/`
- Tạo `docs/i18n/{zh-CN,ja,ru,fr}/` directories với README + SUMMARY của chúng
- Root `README.*.md` files giữ nguyên (convention GitHub)
- Cập nhật cấu trúc internal `docs/i18n/vi/` mirror layout docs tiếng Anh sau khi restructure tiếng Anh land

### TODO: Fuzz testing — nâng cấp stubs lên coverage thực

**Trạng thái hiện tại:** 5 fuzz targets tồn tại trong `fuzz/fuzz_targets/`, nhưng chỉ `fuzz_command_validation` test code ZeroClaw thực. 4 targets khác (`fuzz_config_parse`, `fuzz_tool_params`, `fuzz_webhook_payload`, `fuzz_provider_response`) chỉ fuzz `serde_json::from_str::<Value>` hoặc `toml::from_str::<Value>` — chúng test internals crate third-party, không logic ZeroClaw.

**Wire existing stubs vào paths code thực:**

- `fuzz_config_parse`: deserialize vào `Config`, không `toml::Value`
- `fuzz_tool_params`: truyền qua validation input `Tool::execute` thực
- `fuzz_webhook_payload`: chạy qua verification signature webhook + parsing body
- `fuzz_provider_response`: parse vào types response provider thực (Anthropic, OpenAI, v.v.)

**Thêm targets missing cho security surfaces:**

- Shell command parser (quote-aware parsing, vượt `validate_command_execution`)
- Credential scrubbing (`scrub_credentials` — đã có panic UTF-8 boundary trong #3024)
- Pairing code generation/validation
- Domain matcher
- Prompt guard scoring
- Leak detector regex

**Cải tiến infrastructure:**

- Thêm seed corpora (`fuzz/corpus/<target>/`) với inputs known-good và edge-case; commit vào repo
- Cân nhắc derive `Arbitrary` cho fuzzing có cấu trúc thay vì `&[u8]` raw
- Setup CI fuzzing scheduled (nightly/weekly) — OSS-Fuzz free cho projects open-source
- Dùng `cargo fuzz coverage <target>` để generate reports lcov từ runs corpus và track paths code fuzzer thực sự đạt tới
- Track crash artifacts (`fuzz/artifacts/<target>/`) như issues

### TODO: Test infrastructure follow-ups từ nhánh `e2e-testing`

Issues identified trong review chất lượng của work restructure test.

**1. ~~Pattern attribute `#[path]` trong files runner~~ (đã giải quyết)**

~~Files runner dùng attributes `#[path]` như workaround cho E0761.~~ Đã fix: files runner đổi tên thành `test_component.rs` v.v., directories dùng `mod.rs` standard. `Cargo.toml` entries `[[test]]` cập nhật match. Commands `cargo test --test component` không đổi.

**2. Infrastructure chết: `TestChannel`, `TraceLlmProvider`, fixtures trace, `verify_expects()`**

Đã xây dựng như scaffolding nhưng không consumers:
- `tests/support/mock_channel.rs` (`TestChannel`) — planned cho system tests driven by channel, nhưng agent không có public API loop driven by channel, nên system tests dùng `agent.turn()` trực tiếp.
- `tests/support/mock_provider.rs` (`TraceLlmProvider`) — replay JSON fixture traces, nhưng không test nào load hoặc run fixture.
- `tests/fixtures/traces/*.json` (3 files) — không test nào load.
- `tests/support/assertions.rs` (`verify_expects()`) — không bao giờ gọi.

Hoặc viết tests exercise infrastructure này hoặc xóa nó để tránh confusion code chết.

**3. Gateway component tests overlap với `whatsapp_webhook_security.rs` hiện có**

`tests/component/gateway.rs` có 6 tests verification HMAC signature cho `verify_whatsapp_signature()` — cùng function được test bởi 8 tests trong `tests/component/whatsapp_webhook_security.rs`. Chỉ 3 tests gateway constants (`MAX_BODY_SIZE`, `REQUEST_TIMEOUT_SECS`, `RATE_LIMIT_WINDOW_SECS`) cung cấp coverage thực sự mới. Cân nhắc consolidate signature tests vào một file hoặc xóa duplicates khỏi `gateway.rs`.

**4. Security component tests chỉ config — không coverage hành vi**

10 tests security chỉ validate config defaults và serialization TOML (`AutonomyConfig::default()`, `SecretsConfig`, round-trips). Chúng không test security *behavior* (policy enforcement, credential scrubbing, rate limiting action) vì `src/security/` là `pub(crate)`. Test `security_config_debug_does_not_leak_api_key` là no-op — nó check leak nhưng không assertion failure (chỉ comment). Để có coverage hành vi thực, hoặc:
- Làm functions bảo mật mục tiêu `pub` cho test (ví dụ `scrub_credentials`, `SecurityPolicy::evaluate`)
- Thêm `#[cfg(test)] pub` escape hatches trong `src/security/`
- Viết unit tests in-crate trong `src/security/tests.rs` thay thế

**5. `pub(crate)` visibility chặn integration testing của subsystems quan trọng**

Modules `security` và `gateway` dùng visibility `pub(crate)`, ngăn tests integration exercise logic core như `SecurityPolicy`, `GatewayRateLimiter`, và `IdempotencyStore`. Điều này buộc component tests mới test chỉ qua surface API public hẹp (config structs, một function signature, constants). Cân nhắc liệu types bảo mật quan trọng có nên expose interface public test-only hoặc liệu tests này thuộc unit tests in-crate.

### TODO: Thông báo release tự động — tích hợp Twitter/X

**Trạng thái hiện tại:** Chỉ releases trên GitHub. Không cross-posting tự động tới channels social.

**Kế hoạch:**

- Thêm `.github/workflows/release-tweet.yml` trigger trên `release: [published]`
- Dùng `nearform-actions/github-action-notify-twitter` (OAuth 1.0a, v1.1 API) hoặc `curl` trực tiếp X API v2 với signing OAuth
- Template tweet: release tag, one-line summary, link tới GitHub release
- Bỏ prereleases (`if: "!github.event.release.prerelease"`)

**Secrets required (Settings > Secrets > Actions):**

- `TWITTER_API_KEY`, `TWITTER_API_KEY_SECRET`
- `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`

**Cân nhắc:**

- Review chống lại `docs/contributing/actions-source-policy.md` — pin action third-party tới SHA commit hoặc vendor
- Free tier X: 1,500 tweets/tháng (đủ cho releases)
- Truncate release body tới 280 chars nếu bao gồm highlights trong tweet

---

## Tài liệu liên quan

- [[120-maintainers-docs-inventory|Docs inventory]] — Danh sách docs chi tiết.
- [[065-maintainers-i18n-coverage|i18n coverage]] — Coverage internationalization.
