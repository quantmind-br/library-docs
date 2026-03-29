---
title: ForgeCode
url: https://forgecode.dev/docs/custom-rules-guide/
source: sitemap
fetched_at: 2026-03-29T14:51:41.839336458-03:00
rendered_js: false
word_count: 926
summary: This document explains how to create and use project-specific guidelines through an AGENTS.md file to customize AI coding standards and practices for development teams.
tags:
    - ai-coding
    - project-guidelines
    - development-standards
    - team-configuration
    - custom-rules
    - code-quality
category: guide
---

Every development team has its own way of doing things. Code style preferences, testing patterns, error handling approaches, naming conventions - the list goes on. The problem? A coding harness doesn't know your team's specific practices unless you tell them.

ForgeCode's custom rules feature solves this by letting you embed your team's standards directly into every AI interaction. Instead of repeating the same guidelines in every conversation, you define them once in an `AGENTS.md` file and the AI follows them automatically.

Project-specific guidelines are persistent instructions that get injected into every AI conversation. Think of them as your team's development constitution - fundamental principles that should guide every decision the AI makes in your codebase.

When you define project guidelines, they become part of the AI's system prompt, meaning they're always active and take priority over default behaviors.

Let's start with something simple. Create an `AGENTS.md` file in your project root:

That's it! Now every AI interaction will follow these three basic principles. Let's see how this works in practice.

### Before Project Guidelines[​](#before-project-guidelines "Direct link to Before Project Guidelines")

### After Project Guidelines[​](#after-project-guidelines "Direct link to After Project Guidelines")

Project guidelines are defined using an **`AGENTS.md` file** in your project root directory. This file uses markdown format for comprehensive, documentation-style guidelines.

### Basic Setup (Recommended for Teams)[​](#basic-setup-recommended-for-teams "Direct link to Basic Setup (Recommended for Teams)")

Create an `AGENTS.md` file in your project root with your team's core standards:

### Specialized Rules by Domain[​](#specialized-rules-by-domain "Direct link to Specialized Rules by Domain")

You can organize rules by different areas of development:

### Level 1: Basic Standards (Start Here)[​](#level-1-basic-standards-start-here "Direct link to Level 1: Basic Standards (Start Here)")

Perfect for teams just getting started with project guidelines:

### Level 2: Language-Specific Patterns[​](#level-2-language-specific-patterns "Direct link to Level 2: Language-Specific Patterns")

Once comfortable with basic rules, add language-specific conventions:

### Level 3: Team-Specific Architecture[​](#level-3-team-specific-architecture "Direct link to Level 3: Team-Specific Architecture")

Advanced rules for established teams with specific patterns:

### React/TypeScript Teams[​](#reacttypescript-teams "Direct link to React/TypeScript Teams")

### Python/Django Projects[​](#pythondjango-projects "Direct link to Python/Django Projects")

### Node.js/Express APIs[​](#nodejsexpress-apis "Direct link to Node.js/Express APIs")

When you start an AI agent session, the system:

1. **Searches for `AGENTS.md` files** in multiple locations using a priority system
2. **Parses the markdown content** and extracts your guidelines from the first file found
3. **Injects guidelines into the AI's system prompt**
4. **Applies guidelines to every response throughout the session**

The guidelines become part of the AI's "personality" for that session, influencing every decision it makes about your code.

### File Location Priority[​](#file-location-priority "Direct link to File Location Priority")

The system searches for `AGENTS.md` files in three locations in order of priority:

- **Base path** (environment.base\_path) - highest priority
- **Git root directory** (if available) - medium priority
- **Current working directory** (environment.cwd) - lowest priority

The system uses the first `AGENTS.md` file it finds, starting from the base path and working down the priority list.

### Conditional Rules by File Type[​](#conditional-rules-by-file-type "Direct link to Conditional Rules by File Type")

### Environment-Specific Rules[​](#environment-specific-rules "Direct link to Environment-Specific Rules")

### Common Issues and Solutions[​](#common-issues-and-solutions "Direct link to Common Issues and Solutions")

**Problem: Guidelines aren't being applied**

- Check your `AGENTS.md` file is in your project root directory
- Ensure the file is named exactly `AGENTS.md` (case-sensitive)
- Verify the markdown syntax is valid
- Restart your AI agent session after making changes

**Problem: Guidelines conflict with each other**

- Review your `AGENTS.md` file for contradictory statements
- Later guidelines in the same section may override earlier ones
- Be specific about when guidelines apply (file types, contexts)

**Problem: Guidelines are too vague**

**Problem: Too many guidelines causing confusion**

- Start with 3-5 core guidelines
- Add new guidelines gradually as patterns emerge
- Group related guidelines under clear categories

### Debugging Your Guidelines[​](#debugging-your-guidelines "Direct link to Debugging Your Guidelines")

To verify your guidelines are active, ask the AI agent to describe what project guidelines it's currently following. The guidelines from `AGENTS.md` will be part of the AI's system prompt and influence all responses.

### Performance Tips[​](#performance-tips "Direct link to Performance Tips")

- Keep guidelines concise and specific
- Use bullet points for better readability
- Group related guidelines under clear headings
- Avoid duplicate or contradictory guidelines

### Writing Effective Guidelines[​](#writing-effective-guidelines "Direct link to Writing Effective Guidelines")

**Do:**

- Be specific about what you want
- Use action-oriented language ("Add", "Use", "Include")
- Group related guidelines together
- Start simple and iterate

**Don't:**

- Write vague instructions ("write good code")
- Create conflicting guidelines
- Add too many guidelines at once
- Forget to test your guidelines

### Team Adoption[​](#team-adoption "Direct link to Team Adoption")

1. **Start with team consensus** - Get buy-in on 3-5 core guidelines
2. **Document the why** - Explain reasoning behind each guideline
3. **Review regularly** - Update guidelines as practices evolve
4. **Share examples** - Show before/after comparisons

<!--THE END-->

- Create an `AGENTS.md` file in your project root
- Add 3-5 basic project guidelines using markdown format
- Test with a small feature implementation
- Ask the AI to describe what guidelines it's following
- Iterate based on results
- Gradually add more specific guidelines

* * *

### Verify Your Guidelines[​](#verify-your-guidelines "Direct link to Verify Your Guidelines")

Ask the AI agent: "What project guidelines are you currently following?" or "Can you summarize the development guidelines you're using?" to verify your `AGENTS.md` file is being loaded correctly.

### Get Support[​](#get-support "Direct link to Get Support")

- **Discord**: [Join our Discord community](https://discord.gg/kRZBPpkgwq)
- **Twitter/X**: Send us a DM [@forgecodehq](https://x.com/forgecodehq)

* * *

### Common Questions[​](#common-questions "Direct link to Common Questions")

**Q: Can I have different guidelines for different projects?** A: Yes! Each project's `AGENTS.md` file can have its own specific guidelines.

**Q: How many guidelines can I add?** A: There's no hard limit, but we recommend starting with 5-10 guidelines and growing gradually.

**Q: Do guidelines apply to all AI models?** A: Yes, project guidelines work with all supported AI models.

**Q: Can I share guidelines between projects?** A: You can copy guidelines between `AGENTS.md` files, or create a template for your organization.

* * *

Project-specific guidelines transform AI coding from a series of corrections into a smooth, standards-compliant workflow. Your AI learns your team's way of doing things once through your `AGENTS.md` file, then applies that knowledge consistently across every development session.

To maximize your team's productivity with ForgeCode, explore these complementary guides:

- [**Agent Selection Guide**](https://forgecode.dev/docs/operating-agents/) - Choose the right AI assistant for your specific development tasks
- [**Model Selection Guide**](https://forgecode.dev/docs/model-selection-guide/) - Choose the right AI models for your specific development tasks
- [**File Tagging**](https://forgecode.dev/docs/file-tagging/) - Use @ mentions to provide better context for AI code generation
- [**Plan and Act Guide**](https://forgecode.dev/docs/plan-and-act-guide/) - Structure your development workflow with AI planning before implementation