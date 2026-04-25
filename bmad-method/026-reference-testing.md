---
title: Testing Options
url: https://docs.bmad-method.org/reference/testing/
source: sitemap
fetched_at: 2026-04-08T11:31:33.371927508-03:00
rendered_js: false
word_count: 658
summary: 'This document compares two testing approaches within BMad: a built-in QA workflow for quick test generation suitable for smaller projects, and the advanced Test Architect (TEA) module designed for enterprise-grade strategy, traceability, and complex domain needs.'
tags:
    - qa-workflow
    - test-strategy
    - enterprise-testing
    - api-testing
    - e2e-tests
    - bmad-method
    - module-comparison
category: guide
---

BMad provides two testing paths: a built-in QA workflow for fast test generation and an installable Test Architect module for enterprise-grade test strategy.

## Which Should You Use?

[Section titled “Which Should You Use?”](#which-should-you-use)

FactorBuilt-in QATEA Module**Best for**Small-medium projects, quick coverageLarge projects, regulated or complex domains**Setup**Nothing to install — included in BMMInstall separately via `npx bmad-method install`**Approach**Generate tests fast, iterate laterPlan first, then generate with traceability**Test types**API and E2E testsAPI, E2E, ATDD, NFR, and more**Strategy**Happy path + critical edge casesRisk-based prioritization (P0-P3)**Workflow count**1 (Automate)9 (design, ATDD, automate, review, trace, and others)

## Built-in QA Workflow

[Section titled “Built-in QA Workflow”](#built-in-qa-workflow)

The built-in QA workflow (`bmad-qa-generate-e2e-tests`) is part of the BMM (Agile suite) module, available through the Developer agent. It generates working tests quickly using your project’s existing test framework — no configuration or additional installation required.

**Trigger:** `QA` (via the Developer agent) or `bmad-qa-generate-e2e-tests`

The QA workflow (Automate) walks through five steps:

1. **Detect test framework** — scans `package.json` and existing test files for your framework (Jest, Vitest, Playwright, Cypress, or any standard runner). If none exists, analyzes the project stack and suggests one.
2. **Identify features** — asks what to test or auto-discovers features in the codebase.
3. **Generate API tests** — covers status codes, response structure, happy path, and 1-2 error cases.
4. **Generate E2E tests** — covers user workflows with semantic locators and visible-outcome assertions.
5. **Run and verify** — executes the generated tests and fixes failures immediately.

The workflow produces a test summary saved to your project’s implementation artifacts folder.

Generated tests follow a “simple and maintainable” philosophy:

- **Standard framework APIs only** — no external utilities or custom abstractions
- **Semantic locators** for UI tests (roles, labels, text rather than CSS selectors)
- **Independent tests** with no order dependencies
- **No hardcoded waits or sleeps**
- **Clear descriptions** that read as feature documentation

### When to Use Built-in QA

[Section titled “When to Use Built-in QA”](#when-to-use-built-in-qa)

- Quick test coverage for a new or existing feature
- Beginner-friendly test automation without advanced setup
- Standard test patterns that any developer can read and maintain
- Small-medium projects where comprehensive test strategy is unnecessary

## Test Architect (TEA) Module

[Section titled “Test Architect (TEA) Module”](#test-architect-tea-module)

TEA is a standalone module that provides an expert agent (Murat) and nine structured workflows for enterprise-grade testing. It goes beyond test generation into test strategy, risk-based planning, quality gates, and requirements traceability.

- **Documentation:** [TEA Module Docs](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)
- **Install:** `npx bmad-method install` and select the TEA module
- **npm:** [`bmad-method-test-architecture-enterprise`](https://www.npmjs.com/package/bmad-method-test-architecture-enterprise)

### What TEA Provides

[Section titled “What TEA Provides”](#what-tea-provides)

WorkflowPurposeTest DesignCreate a comprehensive test strategy tied to requirementsATDDAcceptance-test-driven development with stakeholder criteriaAutomateGenerate tests with advanced patterns and utilitiesTest ReviewValidate test quality and coverage against strategyTraceabilityMap tests back to requirements for audit and complianceNFR AssessmentEvaluate non-functional requirements (performance, security)CI SetupConfigure test execution in continuous integration pipelinesFramework ScaffoldingSet up test infrastructure and project structureRelease GateMake data-driven go/no-go release decisions

TEA also supports P0-P3 risk-based prioritization and optional integrations with Playwright Utils and MCP tooling.

- Projects that require requirements traceability or compliance documentation
- Teams that need risk-based test prioritization across many features
- Enterprise environments with formal quality gates before release
- Complex domains where test strategy must be planned before tests are written
- Projects that have outgrown the built-in QA’s single-workflow approach

## How Testing Fits into Workflows

[Section titled “How Testing Fits into Workflows”](#how-testing-fits-into-workflows)

The QA Automate workflow appears in Phase 4 (Implementation) of the BMad Method workflow map. It is designed to run **after a full epic is complete** — once all stories in an epic have been implemented and code-reviewed. A typical sequence:

1. For each story in the epic: implement with Dev (`DS`), then validate with Code Review (`CR`)
2. After the epic is complete: generate tests with `QA` (via the Developer agent) or TEA’s Automate workflow
3. Run retrospective (`bmad-retrospective`) to capture lessons learned

The built-in QA workflow works directly from source code without loading planning documents (PRD, architecture). TEA workflows can integrate with upstream planning artifacts for traceability.

For more on where testing fits in the overall process, see the [Workflow Map](https://docs.bmad-method.org/reference/workflow-map/).