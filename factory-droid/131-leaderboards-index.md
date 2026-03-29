---
title: Leaderboards
url: https://docs.factory.ai/leaderboards/index.md
source: llms
fetched_at: 2026-02-05T21:44:53.667220967-03:00
rendered_js: false
word_count: 316
summary: This document presents leaderboards and evaluation benchmarks for AI coding agents, detailing performance results and methodologies across platforms like Terminal Bench and Next.js.
tags:
    - leaderboards
    - benchmarks
    - ai-coding-agents
    - performance-evaluation
    - terminal-bench
    - nextjs-evals
    - software-engineering
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Leaderboards

> Benchmarks and evaluations for AI coding agents

export const nextjsEvalData = [{
  name: "Factory Droid (GPT-5.2)",
  accuracy: 66.0
}, {
  name: "Factory Droid (Claude Opus 4.5)",
  accuracy: 56.0
}, {
  name: "Factory Droid (Claude Sonnet 4.5)",
  accuracy: 50.0
}, {
  name: "Factory Droid (Gemini 3 Pro)",
  accuracy: 46.0
}, {
  name: "Claude Code (Claude Opus 4.5)",
  accuracy: 42.0
}, {
  name: "Cursor (Claude Sonnet 4.5)",
  accuracy: 38.0
}];

export const EloChart = ({data, valueKey = "elo", labelKey = "name", baseline = 1200}) => {
  const values = data.map(d => d[valueKey]);
  const maxDelta = Math.max(...values.map(v => Math.abs(v - baseline)));
  return <div className="space-y-3 my-6 not-prose">
      {data.map((item, idx) => {
    const value = item[valueKey];
    const delta = value - baseline;
    const barWidth = Math.abs(delta) / maxDelta * 40;
    const isAbove = delta >= 0;
    const isDroid = item[labelKey].toLowerCase().includes('droid') || item[labelKey].toLowerCase().includes('factory');
    return <div key={idx}>
            <div className="flex items-center gap-2 mb-1.5">
              <span className="w-6 text-sm font-mono text-zinc-400 dark:text-zinc-500 text-right">
                {idx + 1}
              </span>
              <span className="text-sm font-medium text-zinc-900 dark:text-zinc-100">
                {item[labelKey]}
              </span>
            </div>
            <div className="flex items-center gap-3">
              <div className="w-6" />
              <div className="flex-1 h-7 relative flex items-center">
                <div className="absolute left-1/2 top-0 bottom-0 w-px border-l border-dashed border-zinc-400 dark:border-zinc-500" />
                <div className="absolute top-0 bottom-0 rounded-sm transition-all duration-500" style={{
      width: `${barWidth}%`,
      left: isAbove ? '50%' : `${50 - barWidth}%`,
      background: isDroid ? 'linear-gradient(to right, #f97316, #fb923c)' : isAbove ? 'linear-gradient(to right, #a1a1aa, #d4d4d8)' : 'linear-gradient(to right, #d4d4d8, #a1a1aa)'
    }} />
                <span className="absolute text-xs font-mono text-zinc-600 dark:text-zinc-400" style={{
      left: isAbove ? `${50 + barWidth + 1}%` : `${50 - barWidth - 1}%`,
      transform: isAbove ? 'none' : 'translateX(-100%)'
    }}>
                  {value}
                </span>
              </div>
            </div>
          </div>;
  })}
      <div className="flex items-center gap-3 mt-1">
        <div className="w-6" />
        <div className="flex-1 relative h-4">
          <div className="absolute left-1/2 -translate-x-1/2 text-xs font-mono text-zinc-400 dark:text-zinc-500">
            {baseline}
          </div>
        </div>
      </div>
    </div>;
};

export const agentArenaData = [{
  name: "Factory Droid",
  elo: 1330
}, {
  name: "OpenAI Codex",
  elo: 1301
}, {
  name: "Devin",
  elo: 1263
}, {
  name: "Claude Code",
  elo: 1242
}, {
  name: "Cursor",
  elo: 1120
}, {
  name: "Gemini CLI",
  elo: 937
}];

export const BarChart = ({data, valueKey, labelKey = "name", valueLabel = "Score", maxValue}) => {
  const values = data.map(d => d[valueKey]);
  const topValue = values[0];
  const minValue = Math.min(...values);
  const baselineOffset = topValue - (topValue - minValue) / 0.8 * 1;
  return <div className="space-y-3 my-6 not-prose">
      {data.map((item, idx) => {
    const value = item[valueKey];
    const percentage = (value - baselineOffset) / (topValue - baselineOffset) * 80;
    const isDroid = item[labelKey].toLowerCase().includes('droid') || item[labelKey].toLowerCase().includes('factory');
    return <div key={idx}>
            <div className="flex items-center gap-2 mb-1.5">
              <span className="w-6 text-sm font-mono text-zinc-400 dark:text-zinc-500 text-right">
                {idx + 1}
              </span>
              <span className="text-sm font-medium text-zinc-900 dark:text-zinc-100">
                {item[labelKey]}
              </span>
            </div>
            <div className="flex items-center gap-3">
              <div className="w-6" />
              <div className="flex-1 h-7 relative flex items-center">
                <div className="h-full rounded-sm transition-all duration-500" style={{
      width: `${percentage}%`,
      background: isDroid ? 'linear-gradient(to right, #f97316, #fb923c)' : 'linear-gradient(to right, #a1a1aa, #d4d4d8)'
    }} />
                <span className="ml-2 text-xs font-mono text-zinc-600 dark:text-zinc-400">
                  {typeof value === 'number' && value % 1 !== 0 ? value.toFixed(1) : value}{valueLabel.includes('%') ? '%' : ''}
                </span>
              </div>
            </div>
          </div>;
  })}
    </div>;
};

export const terminalBenchData = [{
  name: "Factory Droid",
  model: "Claude Opus 4.5",
  accuracy: 63.1
}, {
  name: "OpenAI Codex CLI",
  model: "GPT-5.1-Codex-Max",
  accuracy: 60.4
}, {
  name: "Warp",
  model: "Claude Opus 4.5",
  accuracy: 59.1
}, {
  name: "OpenHands",
  model: "Gemini 3 Pro",
  accuracy: 43.8
}, {
  name: "Anthropic Claude Code",
  model: "Gemini 3 Pro",
  accuracy: 40.1
}];

Factory maintains and contributes to several benchmarks that evaluate AI coding agents across different dimensions. Select a benchmark below to view methodology and results.

<Tabs>
  <Tab title="Terminal Bench" icon="terminal">
    ## Terminal Bench

    Benchmark from [tbench.ai](https://www.tbench.ai) evaluating AI coding agents on real-world software engineering tasks using terminal-based interfaces. Measures how effectively agents can navigate codebases, execute commands, and implement solutions through command-line interactions.

    ### Results

    <BarChart data={terminalBenchData} valueKey="accuracy" valueLabel="%" maxValue={100} />

    *Last updated: December 2025*

    ### Methodology

    | Category                   | Description                             |
    | -------------------------- | --------------------------------------- |
    | **Code Navigation**        | Finding and understanding relevant code |
    | **Bug Fixing**             | Identifying and resolving issues        |
    | **Feature Implementation** | Adding new functionality                |
    | **Refactoring**            | Improving existing code structure       |
    | **Testing**                | Writing and running tests               |

    Tasks are scored on **correctness**, **efficiency**, and **code quality**.

    <Card title="Terminal Bench Leaderboard" icon="trophy" href="https://www.tbench.ai/leaderboard/terminal-bench/2.0">
      View live rankings and submit your agent
    </Card>
  </Tab>

  <Tab title="NextJS" icon="react">
    ## Next.js Evals

    Official benchmark from [Vercel](https://nextjs.org/evals) measuring AI model performance on Next.js code generation and migration tasks. Evaluates success rate, execution time, token usage, and quality improvements.

    ### Results

    <BarChart data={nextjsEvalData} valueKey="accuracy" valueLabel="%" maxValue={100} />

    *Last updated: December 2025*

    ### Methodology

    | Category            | Description                                        |
    | ------------------- | -------------------------------------------------- |
    | **Code Generation** | Creating Next.js components, pages, and API routes |
    | **Migration**       | Upgrading from Pages Router to App Router          |
    | **Best Practices**  | Following Next.js patterns and conventions         |
    | **TypeScript**      | Proper type safety and inference                   |

    Scoring metrics:

    * **Success Rate** - Percentage of tasks completed correctly
    * **Execution Time** - Time to complete tasks
    * **Token Usage** - Efficiency of model responses
    * **Quality Score** - Code quality and best practices

    <Card title="Next.js Evals" icon="trophy" href="https://nextjs.org/evals">
      View live results and methodology
    </Card>
  </Tab>

  <Tab title="Agent Arena" icon="robot">
    ## Agent Arena

    Crowdsourced benchmark from [Design Arena](https://designarena.ai) where AI agents compete to accomplish complex tasks and solve real-world problems autonomously. Rankings are determined by Elo ratings derived from head-to-head comparisons voted on by real users.

    ### ELO Ratings

    <EloChart data={agentArenaData} baseline={1200} />

    *Last updated: December 2025*

    ### Methodology

    1. **Task Assignment** - Both agents receive identical complex task specifications
    2. **Autonomous Execution** - Each agent works independently to complete the task
    3. **Side-by-Side Comparison** - Outputs are presented to human voters
    4. **Elo Scoring** - Results contribute to Bradley-Terry Elo ratings

    | Dimension             | Description                                       |
    | --------------------- | ------------------------------------------------- |
    | **Task Completion**   | Successfully accomplishing the assigned objective |
    | **Quality of Output** | Accuracy and polish of the final result           |
    | **Efficiency**        | Resource usage and execution speed                |
    | **Robustness**        | Handling edge cases and unexpected situations     |

    <Card title="Agent Arena Leaderboard" icon="trophy" href="https://www.designarena.ai/leaderboard/agents">
      View live rankings and vote on agent comparisons
    </Card>
  </Tab>
</Tabs>