---
title: Session Automation - Factory Documentation
url: https://docs.factory.ai/guides/hooks/session-automation
source: sitemap
fetched_at: 2026-01-13T19:04:11.481358323-03:00
rendered_js: false
word_count: 337
summary: Explains how to configure SessionStart hooks in Droid to automatically load project context, set up development environments, and check dependencies when a session begins.
tags:
    - sessionstart-hooks
    - automation
    - environment-setup
    - project-context
    - dependencies
    - bash-scripting
    - development-workflow
category: tutorial
---

This cookbook shows how to use SessionStart hooks to automatically prepare your development environment when Droid starts, saving time and ensuring consistency.

## How it works

SessionStart hooks:

1. **Run at session start**: Triggered when starting new sessions or resuming
2. **Load context**: Add relevant project information to the conversation
3. **Setup environment**: Configure paths, environment variables, tools
4. **Check dependencies**: Verify required tools and packages are available
5. **Persist state**: Set environment variables for the entire session

## Prerequisites

Basic tools for automation:

### Load project context

Automatically provide Droid with project information. Create `.factory/hooks/load-context.sh`:

```
#!/bin/bash
set -e

input=$(cat)
source_type=$(echo "$input" | jq -r '.source')

# Only load context on startup and resume
if [ "$source_type" != "startup" ] && [ "$source_type" != "resume" ]; then
  exit 0
fi

cwd=$(echo "$input" | jq -r '.cwd')
cd "$cwd"

echo "📋 Loading project context..."
echo ""

# Project overview
if [ -f "README.md" ]; then
  echo "## Project Overview"
  echo ""
  head -n 20 README.md
  echo ""
fi

# Recent git activity
if [ -d ".git" ]; then
  echo "## Recent Changes"
  echo ""
  echo "Latest commits:"
  git log --oneline -5
  echo ""

  echo "Current branch: $(git branch --show-current)"
  echo "Uncommitted changes: $(git status --short | wc -l | tr -d ' ') files"
  echo ""
fi

# Project structure
if [ -f "package.json" ]; then
  echo "## Package Info"
  echo ""
  echo "Name: $(jq -r '.name' package.json)"
  echo "Version: $(jq -r '.version' package.json)"
  echo ""

  echo "Scripts available:"
  jq -r '.scripts | keys[]' package.json | head -n 10 | sed 's/^/  - /'
  echo ""
fi

# TODO/FIXME comments
echo "## Open TODOs"
echo ""
echo "Found $(grep -r "TODO\|FIXME" src/ 2>/dev/null | wc -l | tr -d ' ') TODO/FIXME comments in src/"
echo ""

exit 0
```

```
chmod +x .factory/hooks/load-context.sh
```

Add to `.factory/settings.json`:

```
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$DROID_PROJECT_DIR\"/.factory/hooks/load-context.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Setup development environment

Configure tools and paths automatically. Create `.factory/hooks/setup-env.sh`:

```
#!/bin/bash
set -e

input=$(cat)
cwd=$(echo "$input" | jq -r '.cwd')
cd "$cwd"

echo "🔧 Setting up development environment..."

# Detect and setup Node.js version
if [ -f ".nvmrc" ] && command -v nvm &> /dev/null; then
  NODE_VERSION=$(cat .nvmrc)
  echo "📦 Switching to Node.js $NODE_VERSION"

  # Persist environment changes using DROID_ENV_FILE
  if [ -n "$DROID_ENV_FILE" ]; then
    # Capture environment before nvm
    ENV_BEFORE=$(export -p | sort)

    # Source nvm and switch version
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    nvm use

    # Capture changes and persist them
    ENV_AFTER=$(export -p | sort)
    comm -13 <(echo "$ENV_BEFORE") <(echo "$ENV_AFTER") >> "$DROID_ENV_FILE"

    echo "✓ Node.js environment configured"
  fi
fi

# Setup Python virtual environment
if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
  if [ ! -d "venv" ]; then
    echo "⚠️ Virtual environment not found. Consider creating one:"
    echo "   python -m venv venv"
  else
    echo "🐍 Python virtual environment detected"

    if [ -n "$DROID_ENV_FILE" ]; then
      # Activate venv for session
      echo "source \"$cwd/venv/bin/activate\"" >> "$DROID_ENV_FILE"
      echo "✓ Virtual environment will be activated for Bash commands"
    fi
  fi
fi

# Add project binaries to PATH
if [ -d "node_modules/.bin" ] && [ -n "$DROID_ENV_FILE" ]; then
  echo "export PATH=\"\$PATH:$cwd/node_modules/.bin\"" >> "$DROID_ENV_FILE"
  echo "✓ Added node_modules/.bin to PATH"
fi

# Setup Go workspace
if [ -f "go.mod" ]; then
  echo "🔷 Go module detected"
  if [ -n "$DROID_ENV_FILE" ]; then
    echo "export GO111MODULE=on" >> "$DROID_ENV_FILE"
    echo "export GOPATH=$HOME/go" >> "$DROID_ENV_FILE"
  fi
fi

echo ""
echo "✓ Environment setup complete"

exit 0
```

```
chmod +x .factory/hooks/setup-env.sh
```

## Advanced automation

### Load recent Linear/GitHub issues

Provide Droid with context about current work. Create `.factory/hooks/load-issues.sh`:

```
#!/bin/bash
set -e

input=$(cat)
source_type=$(echo "$input" | jq -r '.source')

if [ "$source_type" != "startup" ]; then
  exit 0
fi

echo "📋 Loading recent issues..."
echo ""

# Load GitHub issues if gh CLI is available
if command -v gh &> /dev/null; then
  echo "## Recent GitHub Issues"
  echo ""

  # Get assigned issues
  gh issue list --assignee @me --limit 5 --json number,title,state | \
    jq -r '.[] | "  - #\(.number): \(.title) [\(.state)]"'
  echo ""
fi

# Load Linear issues if linear CLI is available
if command -v linear &> /dev/null; then
  echo "## Recent Linear Issues"
  echo ""

  # Get assigned issues
  linear issue list --assignee @me --limit 5 2>/dev/null | head -n 10
  echo ""
fi

# Check for CHANGELOG or ROADMAP
if [ -f "CHANGELOG.md" ]; then
  echo "## Recent Changelog"
  echo ""
  head -n 15 CHANGELOG.md
  echo ""
fi

exit 0
```

```
chmod +x .factory/hooks/load-issues.sh
```

### Check and install dependencies

Automatically ensure dependencies are up-to-date. Create `.factory/hooks/check-dependencies.sh`:

```
#!/bin/bash
set -e

input=$(cat)
cwd=$(echo "$input" | jq -r '.cwd')
cd "$cwd"

echo "📦 Checking dependencies..."
echo ""

# Node.js projects
if [ -f "package.json" ]; then
  if [ ! -d "node_modules" ]; then
    echo "⚠️ node_modules not found"
    echo "Suggestion: Run 'npm install' or 'yarn install'"
    echo ""
  else
    # Check if package.json is newer than node_modules
    if [ "package.json" -nt "node_modules" ]; then
      echo "⚠️ package.json modified since last install"
      echo "Suggestion: Run 'npm install' to update dependencies"
      echo ""
    else
      echo "✓ Node dependencies up to date"
      echo ""
    fi
  fi
fi

# Python projects
if [ -f "requirements.txt" ]; then
  if [ ! -d "venv" ]; then
    echo "⚠️ Python virtual environment not found"
    echo "Suggestion: Run 'python -m venv venv && source venv/bin/activate && pip install -r requirements.txt'"
    echo ""
  else
    echo "✓ Python virtual environment exists"
    echo ""
  fi
fi

# Go projects
if [ -f "go.mod" ]; then
  if [ ! -d "vendor" ] && ! command -v go &> /dev/null; then
    echo "⚠️ Go not found in PATH"
    echo "Suggestion: Install Go from https://go.dev"
    echo ""
  else
    echo "✓ Go environment ready"
    echo ""
  fi
fi

# Ruby projects
if [ -f "Gemfile" ]; then
  if ! command -v bundle &> /dev/null; then
    echo "⚠️ Bundler not found"
    echo "Suggestion: gem install bundler"
    echo ""
  else
    if ! bundle check &>/dev/null; then
      echo "⚠️ Ruby gems out of date"
      echo "Suggestion: bundle install"
      echo ""
    else
      echo "✓ Ruby gems up to date"
      echo ""
    fi
  fi
fi

exit 0
```

```
chmod +x .factory/hooks/check-dependencies.sh
```

### Load custom project guidelines

Provide project-specific instructions automatically. Create `.factory/AGENTS.md` with project guidelines:

```
# Project Guidelines for Droid

## Code Style
- Use TypeScript for all new files
- Follow ESLint configuration strictly
- Prefer functional components in React
- Use async/await over promises

## Testing
- Write tests for all new features
- Run `npm test` before committing
- Maintain >80% code coverage

## Architecture
- Keep components under 200 lines
- Use Redux for global state
- Local state for component-specific data
- No direct API calls from components (use services)

## Git Workflow
- Create feature branches from `dev`
- Name branches: `feature/FAC-123-description`
- Write descriptive commit messages
- Squash commits before merging
```

Create `.factory/hooks/load-guidelines.sh`:

```
#!/bin/bash
set -e

input=$(cat)
source_type=$(echo "$input" | jq -r '.source')

if [ "$source_type" != "startup" ]; then
  exit 0
fi

cwd=$(echo "$input" | jq -r '.cwd')

# Load project-specific guidelines
if [ -f "$cwd/.factory/AGENTS.md" ]; then
  echo "## Project Guidelines"
  echo ""
  cat "$cwd/.factory/AGENTS.md"
  echo ""
fi

# Load PR templates
if [ -f "$cwd/.github/PULL_REQUEST_TEMPLATE.md" ]; then
  echo "## PR Template Reference"
  echo ""
  head -n 20 "$cwd/.github/PULL_REQUEST_TEMPLATE.md"
  echo ""
fi

exit 0
```

```
chmod +x .factory/hooks/load-guidelines.sh
```

### Smart context based on Git branch

Load different context based on the current branch: Create `.factory/hooks/branch-context.sh`:

```
#!/bin/bash
set -e

input=$(cat)
cwd=$(echo "$input" | jq -r '.cwd')
cd "$cwd"

if [ ! -d ".git" ]; then
  exit 0
fi

branch=$(git branch --show-current)

echo "## Current Context: $branch"
echo ""

case "$branch" in
  main|master)
    echo "⚠️ Working on production branch!"
    echo "Extra care needed - changes go to production"
    echo ""

    # Show recent production issues
    if command -v gh &> /dev/null; then
      echo "Recent production issues:"
      gh issue list --label production --limit 3 --json number,title | \
        jq -r '.[] | "  - #\(.number): \(.title)"'
      echo ""
    fi
    ;;

  dev|develop)
    echo "📦 Working on development branch"
    echo "Standard development workflow applies"
    echo ""
    ;;

  feature/*)
    feature_name="${branch#feature/}"
    echo "🔨 Feature branch: $feature_name"
    echo ""

    # Try to find related issue
    if [[ $feature_name =~ FAC-[0-9]+ ]]; then
      issue_id="${BASH_REMATCH[0]}"
      echo "Related Linear issue: $issue_id"

      # Fetch issue details if linear CLI available
      if command -v linear &> /dev/null; then
        linear issue view "$issue_id" 2>/dev/null || true
        echo ""
      fi
    fi

    # Show uncommitted changes
    if [ -n "$(git status --short)" ]; then
      echo "Uncommitted changes:"
      git status --short | head -n 10
      echo ""
    fi
    ;;

  hotfix/*)
    echo "🚨 HOTFIX BRANCH"
    echo "Critical bug fix - expedite review and deployment"
    echo ""
    ;;
esac

exit 0
```

```
chmod +x .factory/hooks/branch-context.sh
```

## Real-world examples

### Example 1: Monorepo workspace setup

Automatically switch to the right package: Create `.factory/hooks/monorepo-setup.sh`:

```
#!/bin/bash
set -e

input=$(cat)
cwd=$(echo "$input" | jq -r '.cwd')

# Check if this is a monorepo
if [ ! -f "$cwd/package.json" ] || ! grep -q '"workspaces"' "$cwd/package.json"; then
  exit 0
fi

echo "## Monorepo Structure"
echo ""

# List workspaces
if command -v npm &> /dev/null; then
  echo "Available workspaces:"
  npm ls --workspaces --depth=0 2>/dev/null | grep -E "^[├└]" | sed 's/^[├└]── /  - /'
  echo ""
fi

# Show recent changes by workspace
if [ -d ".git" ]; then
  echo "Recently modified workspaces:"
  git diff --name-only HEAD~5..HEAD | \
    grep -E "^(packages|apps)/" | \
    cut -d/ -f1-2 | \
    sort -u | \
    head -n 5 | \
    sed 's/^/  - /'
  echo ""
fi

exit 0
```

### Example 2: Docker environment check

Ensure Docker services are running: Create `.factory/hooks/check-docker.sh`:

```
#!/bin/bash

if ! command -v docker &> /dev/null; then
  exit 0
fi

# Check if Docker daemon is running
if ! docker info &>/dev/null; then
  echo "⚠️ Docker daemon not running"
  echo "Suggestion: Start Docker Desktop or run 'sudo systemctl start docker'"
  echo ""
  exit 0
fi

echo "## Docker Environment"
echo ""

# Check for docker-compose.yml
if [ -f "docker-compose.yml" ] || [ -f "docker-compose.yaml" ]; then
  echo "Docker Compose configuration found"

  # Check if services are running
  if docker-compose ps &>/dev/null; then
    echo ""
    echo "Running services:"
    docker-compose ps --format "table {{.Name}}\t{{.Status}}" | tail -n +2 | sed 's/^/  /'
  else
    echo "Suggestion: Start services with 'docker-compose up -d'"
  fi
  echo ""
fi

exit 0
```

## Best practices

## Troubleshooting

**Problem**: Too much information loaded **Solution**: Summarize and link to details:

```
echo "README.md exists ($(wc -l < README.md) lines)"
echo "Run 'cat README.md' to view full content"
```

**Problem**: Variables not available in Bash commands **Solution**: Verify DROID\_ENV\_FILE usage:

```
if [ -z "$DROID_ENV_FILE" ]; then
  echo "DROID_ENV_FILE not available" >&2
  exit 1
fi

# Append, don't overwrite
echo 'export VAR=value' >> "$DROID_ENV_FILE"
```

**Problem**: Session start takes too long **Solution**: Run expensive operations asynchronously:

```
# Start background job for slow operations
(
  sleep 1  # Let Droid start first
  expensive_operation > /tmp/droid-context.txt
) &

# Return immediately with basic context
echo "Loading detailed context in background..."
```

## See also

- [Hooks reference](https://docs.factory.ai/reference/hooks-reference) - Complete hooks API documentation
- [Get started with hooks](https://docs.factory.ai/cli/configuration/hooks-guide) - Basic hooks introduction
- [Custom notifications](https://docs.factory.ai/guides/hooks/notifications) - Get notified about events
- [Logging and analytics](https://docs.factory.ai/guides/hooks/logging-analytics) - Track session metrics