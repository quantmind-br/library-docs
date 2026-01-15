---
title: Leaderboards - Factory Documentation
url: https://docs.factory.ai/leaderboards
source: sitemap
fetched_at: 2026-01-13T19:04:28.902997292-03:00
rendered_js: false
word_count: 337
summary: 'This document serves as a performance report showcasing the results of the Factory AI coding agent across three specific industry benchmarks: Terminal Bench, Next.js Evals, and Agent Arena.'
tags:
    - benchmarks
    - ai-agents
    - performance-metrics
    - leaderboard
    - code-generation
    - elo-rating
    - evaluation
category: other
---

Factory maintains and contributes to several benchmarks that evaluate AI coding agents across different dimensions. Select a benchmark below to view methodology and results.

## Terminal Bench

Benchmark from [tbench.ai](https://www.tbench.ai) evaluating AI coding agents on real-world software engineering tasks using terminal-based interfaces. Measures how effectively agents can navigate codebases, execute commands, and implement solutions through command-line interactions.

### Results

*Last updated: December 2025*

### Methodology

CategoryDescription**Code Navigation**Finding and understanding relevant code**Bug Fixing**Identifying and resolving issues**Feature Implementation**Adding new functionality**Refactoring**Improving existing code structure**Testing**Writing and running tests

Tasks are scored on **correctness**, **efficiency**, and **code quality**.

[**Terminal Bench Leaderboard**  
\
View live rankings and submit your agent](https://www.tbench.ai/leaderboard/terminal-bench/2.0)

## Next.js Evals

Official benchmark from [Vercel](https://nextjs.org/evals) measuring AI model performance on Next.js code generation and migration tasks. Evaluates success rate, execution time, token usage, and quality improvements.

### Results

2Factory Droid (Claude Opus 4.5)

3Factory Droid (Claude Sonnet 4.5)

4Factory Droid (Gemini 3 Pro)

5Claude Code (Claude Opus 4.5)

6Cursor (Claude Sonnet 4.5)

*Last updated: December 2025*

### Methodology

CategoryDescription**Code Generation**Creating Next.js components, pages, and API routes**Migration**Upgrading from Pages Router to App Router**Best Practices**Following Next.js patterns and conventions**TypeScript**Proper type safety and inference

Scoring metrics:

- **Success Rate** - Percentage of tasks completed correctly
- **Execution Time** - Time to complete tasks
- **Token Usage** - Efficiency of model responses
- **Quality Score** - Code quality and best practices

[**Next.js Evals**  
\
View live results and methodology](https://nextjs.org/evals)

## Agent Arena

Crowdsourced benchmark from [Design Arena](https://designarena.ai) where AI agents compete to accomplish complex tasks and solve real-world problems autonomously. Rankings are determined by Elo ratings derived from head-to-head comparisons voted on by real users.

### ELO Ratings

*Last updated: December 2025*

### Methodology

1. **Task Assignment** - Both agents receive identical complex task specifications
2. **Autonomous Execution** - Each agent works independently to complete the task
3. **Side-by-Side Comparison** - Outputs are presented to human voters
4. **Elo Scoring** - Results contribute to Bradley-Terry Elo ratings

DimensionDescription**Task Completion**Successfully accomplishing the assigned objective**Quality of Output**Accuracy and polish of the final result**Efficiency**Resource usage and execution speed**Robustness**Handling edge cases and unexpected situations

[**Agent Arena Leaderboard**  
\
View live rankings and vote on agent comparisons](https://www.designarena.ai/leaderboard/agents)