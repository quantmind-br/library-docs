---
title: Pi Web UI - Example
url: https://github.com/badlogic/pi-mono/blob/main/packages/web-ui/example/README.md
source: git
fetched_at: 2026-05-03T09:32:25.513116899-03:00
rendered_js: false
word_count: 137
summary: Minimal example of @mariozechner/pi-web-ui in a Vite web application with chat interface.
tags:
    - pi-web-ui
    - web-development
    - ai-integration
    - api-configuration
    - frontend-setup
    - chat-interface
category: tutorial
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Pi Web UI - Example

Minimal example of `@mariozechner/pi-web-ui` in a web application.

## Setup

```bash
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in browser.

## Components

- **ChatPanel** — main chat interface
- **System Prompt** — AI assistant configuration
- **Tools** — JavaScript REPL and artifacts tool

## API Keys (Direct Mode)

The example calls AI provider APIs directly from the browser (no backend).

1. Click settings icon (⚙️) in chat interface
2. Click "Manage API Keys"
3. Add your API key:

| Provider | Key Source |
|----------|------------|
| Anthropic | [console.anthropic.com](https://console.anthropic.com/) |
| OpenAI | [platform.openai.com](https://platform.openai.com/) |
| Google | [makersuite.google.com](https://makersuite.google.com/) |

> [!note]
> API keys stored in browser's localStorage, sent only to the AI provider's API.

## Project Structure

```
example/
├── src/
│   ├── main.ts       # Application entry
│   └── app.css       # Tailwind CSS
├── index.html        # HTML entry
├── package.json      # Dependencies
├── vite.config.ts    # Vite config
└── tsconfig.json     # TypeScript config
```

## Learn More

- [[013-packages-web-ui-readme.md|Pi Web UI Documentation]]
- [[002-packages-ai-readme.md|Pi AI Documentation]]
- [Mini Lit](https://github.com/badlogic/mini-lit)

#pi-web-ui #ai-integration #chat-interface
