---
title: Generate Unit and Security Tests | Guides | Warp
url: https://docs.warp.dev/guides/devops-and-infrastructure/how-to-generate-unit-and-security-tests-to-debug-faster
source: sitemap
fetched_at: 2026-04-29T15:07:11.083633348-03:00
rendered_js: false
word_count: 404
summary: This document provides a comprehensive checklist and methodology for verifying API code through structured unit testing and security validation.
tags:
    - api-testing
    - security-testing
    - unit-testing
    - input-validation
    - authentication-testing
    - authorization-checks
    - vulnerability-assessment
category: guide
optimized: true
optimized_at: 2026-04-29T15:07:11.083633348-03:00
---
Prompt template for generating comprehensive unit tests and security tests after implementing API code.

## 1. Unit Tests Per Function

| Test Type | Description |
|-----------|-------------|
| Happy path | Valid inputs → expected output |
| Edge cases | Empty inputs, nulls, boundary values |
| Error handling | Invalid inputs |
| Return types | Value types and structure |
| Special cases | Empty strings, null/undefined, max values, special characters |

## 2. Security Tests Per Endpoint

### Input Validation

Test malicious payloads in every user input field:

| Attack Type | Payload Examples |
|-------------|------------------|
| SQL Injection | `" ' OR '1' = '1'`, `"1; DROP TABLE users--"`, `"admin'--"` |
| NoSQL Injection | `{"$gt": ""}`, `{"$ne": null}` |
| Command Injection | `; ls -la`, `| whoami`, `$(cat /etc/passwd)` |
| Path Traversal | `../../../etc/passwd`, `..\..\..\windows\system32` |
| XSS | `<script>alert('XSS')</script>`, `javascript:alert(1)` |
| XXE (XML) | `<!DOCTYPE foo [<!ENTITY xxe SYSTEM 'file:///etc/passwd'>]>` |

### Authentication Tests

| Scenario | Expected Response |
|----------|-------------------|
| No token/credentials | 401 |
| Invalid token | 401 |
| Expired token | 401 |
| Valid token for wrong user | 403 |
| Token with insufficient permissions | 403 |

### Authorization Tests

| Scenario | Expected Response |
|----------|-------------------|
| User A accessing User B's data | 403 |
| Regular user accessing admin endpoints | 403 |
| Deleted/disabled user token | 401 |
| All role-based access controls | Working correctly |

### Additional Security Checks

- Rate limiting (100 requests → 429 response)
- Large payload rejection (>1MB unless specified)
- Sensitive data not exposed in errors
- Headers don't leak server info
- CORS properly configured

## 3. Post-Test Verification

| Check | Requirement |
|-------|-------------|
| All unit tests pass | ✓ |
| 100% functions have tests | ✓ |
| All security tests pass | ✓ |
| No SQL/NoSQL injection vulnerabilities | ✓ |
| Authentication properly enforced | ✓ |
| Authorization rules working | ✓ |
| Input validation catches malicious data | ✓ |
| Error messages don't expose sensitive info | ✓ |

## 4. Output Format

Generate 2 test files:

1. `Unit_tests.[ext]` — all functional tests
2. `Security_tests.[ext]` — all security tests

Use simple assertions that show what is tested, expected behavior, and why it matters. Each test verifies ONE thing.

#api-testing #security-testing #vulnerability-assessment
