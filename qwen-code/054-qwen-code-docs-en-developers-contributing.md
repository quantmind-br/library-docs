---
title: How to Contribute
url: https://qwenlm.github.io/qwen-code-docs/en/developers/contributing
source: github_pages
fetched_at: 2026-04-09T09:04:33.495927371-03:00
rendered_js: true
word_count: 1269
summary: This document serves as a comprehensive guide for contributors detailing required processes for submitting code patches, including strict guidelines on creating pull requests, and outlines the complete development workflow covering setup, building, testing, linting, and documentation updates.
tags:
    - contribution-process
    - pull-request-guidelines
    - development-workflow
    - testing-guide
    - coding-conventions
    - setup-guide
category: guide
---

We would love to accept your patches and contributions to this project.

## Contribution Process[](#contribution-process)

### Code Reviews[](#code-reviews)

All submissions, including submissions by project members, require review. We use [GitHub pull requests](https://docs.github.com/articles/about-pull-requests)  for this purpose.

### Pull Request Guidelines[](#pull-request-guidelines)

To help us review and merge your PRs quickly, please follow these guidelines. PRs that do not meet these standards may be closed.

#### 1. Link to an Existing Issue[](#1-link-to-an-existing-issue)

All PRs should be linked to an existing issue in our tracker. This ensures that every change has been discussed and is aligned with the project’s goals before any code is written.

- **For bug fixes:** The PR should be linked to the bug report issue.
- **For features:** The PR should be linked to the feature request or proposal issue that has been approved by a maintainer.

If an issue for your change doesn’t exist, please **open one first** and wait for feedback before you start coding.

#### 2. Keep It Small and Focused[](#2-keep-it-small-and-focused)

We favor small, atomic PRs that address a single issue or add a single, self-contained feature.

- **Do:** Create a PR that fixes one specific bug or adds one specific feature.
- **Don’t:** Bundle multiple unrelated changes (e.g., a bug fix, a new feature, and a refactor) into a single PR.

Large changes should be broken down into a series of smaller, logical PRs that can be reviewed and merged independently.

#### 3. Use Draft PRs for Work in Progress[](#3-use-draft-prs-for-work-in-progress)

If you’d like to get early feedback on your work, please use GitHub’s **Draft Pull Request** feature. This signals to the maintainers that the PR is not yet ready for a formal review but is open for discussion and initial feedback.

#### 4. Ensure All Checks Pass[](#4-ensure-all-checks-pass)

Before submitting your PR, ensure that all automated checks are passing by running `npm run preflight`. This command runs all tests, linting, and other style checks.

#### 5. Update Documentation[](#5-update-documentation)

If your PR introduces a user-facing change (e.g., a new command, a modified flag, or a change in behavior), you must also update the relevant documentation in the `/docs` directory.

#### 6. Write Clear Commit Messages and a Good PR Description[](#6-write-clear-commit-messages-and-a-good-pr-description)

Your PR should have a clear, descriptive title and a detailed description of the changes. Follow the [Conventional Commits](https://www.conventionalcommits.org/)  standard for your commit messages.

- **Good PR Title:** `feat(cli): Add --json flag to 'config get' command`
- **Bad PR Title:** `Made some changes`

In the PR description, explain the “why” behind your changes and link to the relevant issue (e.g., `Fixes #123`).

## Development Setup and Workflow[](#development-setup-and-workflow)

This section guides contributors on how to build, modify, and understand the development setup of this project.

### Setting Up the Development Environment[](#setting-up-the-development-environment)

**Prerequisites:**

1. **Node.js**:
   
   - **Development:** Please use Node.js `~20.19.0`. This specific version is required due to an upstream development dependency issue. You can use a tool like [nvm](https://github.com/nvm-sh/nvm)  to manage Node.js versions.
   - **Production:** For running the CLI in a production environment, any version of Node.js `>=20` is acceptable.
2. **Git**

### Build Process[](#build-process)

To clone the repository:

```
git clone https://github.com/QwenLM/qwen-code.git # Or your fork's URL
cd qwen-code
```

To install dependencies defined in `package.json` as well as root dependencies:

To build the entire project (all packages):

This command typically compiles TypeScript to JavaScript, bundles assets, and prepares the packages for execution. Refer to `scripts/build.js` and `package.json` scripts for more details on what happens during the build.

### Enabling Sandboxing[](#enabling-sandboxing)

[Sandboxing](#sandboxing) is highly recommended and requires, at a minimum, setting `QWEN_SANDBOX=true` in your `~/.env` and ensuring a sandboxing provider (e.g. `macOS Seatbelt`, `docker`, or `podman`) is available. See [Sandboxing](#sandboxing) for details.

To build both the `qwen-code` CLI utility and the sandbox container, run `build:all` from the root directory:

To skip building the sandbox container, you can use `npm run build` instead.

### Running[](#running)

To start the Qwen Code application from the source code (after building), run the following command from the root directory:

If you’d like to run the source build outside of the qwen-code folder, you can utilize `npm link path/to/qwen-code/packages/cli` (see: [docs](https://docs.npmjs.com/cli/v9/commands/npm-link) ) to run with `qwen-code`

### Running Tests[](#running-tests)

This project contains two types of tests: unit tests and integration tests.

#### Unit Tests[](#unit-tests)

To execute the unit test suite for the project:

This will run tests located in the `packages/core` and `packages/cli` directories. Ensure tests pass before submitting any changes. For a more comprehensive check, it is recommended to run `npm run preflight`.

#### Integration Tests[](#integration-tests)

The integration tests are designed to validate the end-to-end functionality of Qwen Code. They are not run as part of the default `npm run test` command.

To run the integration tests, use the following command:

For more detailed information on the integration testing framework, please see the [Integration Tests documentation](https://qwenlm.github.io/qwen-code-docs/en/developers/docs/integration-tests/).

### Linting and Preflight Checks[](#linting-and-preflight-checks)

To ensure code quality and formatting consistency, run the preflight check:

This command will run ESLint, Prettier, all tests, and other checks as defined in the project’s `package.json`.

*ProTip*

after cloning create a git precommit hook file to ensure your commits are always clean.

```
echo "
# Run npm build and check for errors
if ! npm run preflight; then
  echo "npm build failed. Commit aborted."
  exit 1
fi
" > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

#### Formatting[](#formatting)

To separately format the code in this project by running the following command from the root directory:

This command uses Prettier to format the code according to the project’s style guidelines.

#### Linting[](#linting)

To separately lint the code in this project, run the following command from the root directory:

### Coding Conventions[](#coding-conventions)

- Please adhere to the coding style, patterns, and conventions used throughout the existing codebase.
- **Imports:** Pay special attention to import paths. The project uses ESLint to enforce restrictions on relative imports between packages.

### Project Structure[](#project-structure)

- `packages/`: Contains the individual sub-packages of the project.
  
  - `cli/`: The command-line interface.
  - `core/`: The core backend logic for Qwen Code.
- `docs/`: Contains all project documentation.
- `scripts/`: Utility scripts for building, testing, and development tasks.

For more detailed architecture, see `docs/architecture.md`.

## Documentation Development[](#documentation-development)

This section describes how to develop and preview the documentation locally.

### Prerequisites[](#prerequisites)

1. Ensure you have Node.js (version 18+) installed
2. Have npm or yarn available

### Setup Documentation Site Locally[](#setup-documentation-site-locally)

To work on the documentation and preview changes locally:

1. Navigate to the `docs-site` directory:
2. Install dependencies:
3. Link the documentation content from the main `docs` directory:
   
   This creates a symbolic link from `../docs` to `content` in the docs-site project, allowing the documentation content to be served by the Next.js site.
4. Start the development server:
5. Open [http://localhost:3000](http://localhost:3000)  in your browser to see the documentation site with live updates as you make changes.

Any changes made to the documentation files in the main `docs` directory will be reflected immediately in the documentation site.

## Debugging[](#debugging)

### VS Code:[](#vs-code)

0. Run the CLI to interactively debug in VS Code with `F5`
1. Start the CLI in debug mode from the root directory: This command runs `node --inspect-brk dist/index.js` within the `packages/cli` directory, pausing execution until a debugger attaches. You can then open `chrome://inspect` in your Chrome browser to connect to the debugger.
2. In VS Code, use the “Attach” launch configuration (found in `.vscode/launch.json`).

Alternatively, you can use the “Launch Program” configuration in VS Code if you prefer to launch the currently open file directly, but ‘F5’ is generally recommended.

To hit a breakpoint inside the sandbox container run:

**Note:** If you have `DEBUG=true` in a project’s `.env` file, it won’t affect qwen-code due to automatic exclusion. Use `.qwen-code/.env` files for qwen-code specific debug settings.

### React DevTools[](#react-devtools)

To debug the CLI’s React-based UI, you can use React DevTools. Ink, the library used for the CLI’s interface, is compatible with React DevTools version 4.x.

1. **Start the Qwen Code application in development mode:**
2. **Install and run React DevTools version 4.28.5 (or the latest compatible 4.x version):**
   
   You can either install it globally:
   
   ```
   npm install -g react-devtools@4.28.5
   react-devtools
   ```
   
   Or run it directly using npx:
   
   ```
   npx react-devtools@4.28.5
   ```
   
   Your running CLI application should then connect to React DevTools.

## Sandboxing[](#sandboxing)

> TBD

## Manual Publish[](#manual-publish)

We publish an artifact for each commit to our internal registry. But if you need to manually cut a local build, then run the following commands:

```
npm run clean
npm install
npm run auth
npm run prerelease:dev
npm publish --workspaces
```