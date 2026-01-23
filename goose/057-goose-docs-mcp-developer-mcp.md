---
title: Developer Extension | goose
url: https://block.github.io/goose/docs/mcp/developer-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:03.447168249-03:00
rendered_js: true
word_count: 874
summary: This document explains how to enable, use, and secure the Developer extension for goose, which automates file editing and shell command execution.
tags:
    - goose-extension
    - developer-tools
    - automation
    - access-control
    - shell-execution
    - configuration
category: guide
---

🎥Plug & Play

Watch the demo

* * *

The Developer extension allows goose to automate developer-centric tasks such as file editing, shell command execution, and project setup. It also provides tools for [enhanced code editing](https://block.github.io/goose/docs/guides/enhanced-code-editing) and [codebase analysis](https://block.github.io/goose/docs/guides/codebase-analysis).

This tutorial will cover enabling and using the Developer MCP Server, which is a built-in goose extension.

## Configuration[​](#configuration "Direct link to Configuration")

info

The Developer extension is already enabled by default when goose is installed.

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `Extensions` in the sidebar
3. Toggle `Developer` on

## Example Usage[​](#example-usage "Direct link to Example Usage")

In this example, I'm going to have goose automate setting up my JavaScript developer environment with Express, Mongoose, Nodemon, Dotenv and initialize Git.

LLM

Anthropic's Claude 4 Sonnet was used for this task.

- goose Desktop
- goose CLI

<!--THE END-->

1. Open a new session in goose Desktop

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
set up a new JavaScript project with Express, Mongoose, Nodemon, and Dotenv? Fetch the latest package versions, generate a README with those versions, and initialize Git
```

After 1 minute, goose was done setting up my entire dev environment! 🎉

### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll help you set up a new JavaScript project with those dependencies. I'll break this down into steps:

1. First, let's create a new directory and initialize the project
2. Then install the dependencies
3. Create a detailed README
4. Initialize git
5. Create some starter files
6. Let's begin:

[... shell commands, files created ...]

Great! I've set up a complete Express project with MongoDB and Dotenv integrations:

1. Created a new project directory and initialized npm
2. Installed Express, Mongoose, and dotenv dependencies
3. set up the basic project structure with directories for:
- config/
- models/
- routes/ 
- controllers/
4. Created essential files:
- index.js (main server file)
- .env (environment variables)
- .ignore (with common node.js ignores)
5. Added a basic user model with basic name and email fields
6. Created a user controller with two methods:
- getUsers (GET all users)
- createUser (POST new user)
7. Added user routes under `/api/routes`
8. Updated package.json with start scripts
9. Created a comprehensive README.md with:
- Installation scripts
- Project structure
- Available scripts
- Environment variables 
- Latest package versions

The project structure is:

my-express-app/
├── config/         # Configuration files
├── models/        # MongoDB models
│   └── User.js    # User model
├── routes/        # API routes
│   └── userRoutes.js
├── controllers/   # Route controllers
│   └── userController.js
├── .env           # Environment variables
├── .gitignore     # Git ignore file
├── index.js       # Entry point
└── package.json   # Project dependencies and scripts

To start developing you can:

1. Run `npm install` to install dependencies
2. start the server with `npm run dev`

The API will be available at:
-`http://localhost:3000/api/users` (GET to get all users)
-`http://localhost:3000/api/users` (POST to create a new user)

To test out the API you can use tools like postman or curl, for example, to create a new user:

curl x POST http://localhost:3000/api/users \
-H "Content-Type: application/json" \
-d '{"name": "Ebony Louis" , "email": "ebony@example.com"}'

Would you like me to add any additional features or make other improvements to the setup?
```

## Configuring Access Controls[​](#configuring-access-controls "Direct link to Configuring Access Controls")

By default, goose can run system commands with your user privileges and edit any accessible file **without your approval**. This is because goose runs in Autonomous permission mode by default and has access to the Developer extension's shell and file editing tools. While this configuration allows goose to work quickly and independently, there's potential for unexpected outcomes. Understanding the available access control features can help you configure goose to match your comfort level and specific needs.

tip

See the [Quick Setup Example](#quick-setup-example) below for some ways to configure more control over goose's behavior.

### Developer Extension Tools[​](#developer-extension-tools "Direct link to Developer Extension Tools")

The Developer extension provides these tools:

ToolDescriptionUse CasesRisk Level`shell`Execute shell commandsRunning tests, installing packages, git operations⚠️ High  
Can run any system command with your user privileges`text_editor`Read, write, and edit filesCode refactoring, creating files, updating configs⚠️ High  
Can modify any accessible file`analyze`Analyze code structureUnderstanding codebase, finding dependencies✅ Low  
Read-only code analysis`screen_capture`Take screenshotsDebugging UI issues, documenting state✅ Low  
Visual information only`image_processor`Process and resize imagesOptimizing assets, format conversion✅ Low  
Image manipulation only

### Access Control Features[​](#access-control-features "Direct link to Access Control Features")

You can layer multiple controls to match your risk tolerance and workflow:

- [**goose Permission Modes**](https://block.github.io/goose/docs/guides/goose-permissions) control when goose asks for approval:
  
  ModeDescriptionUse CasesAutonomous  
  CLI: `auto`No approval requiredBest for experienced users in safe environmentsManual Approval  
  CLI: `approve`Review every actionRecommended for sensitive work or when you want maximum controlSmart Approval  
  CLI: `smart_approve`AI decides what needs reviewBalanced approachChat Only  
  CLI: `chat`Disable all toolsFor maximum security and models that don't support tool-calling
- [**Tool Permissions**](https://block.github.io/goose/docs/guides/managing-tools/tool-permissions) let you set `Always allow`, `Ask before`, and `Never allow` permissions for individual extension tools when in Manual Approval or Smart Approval modes
- [**.gooseignore files**](https://block.github.io/goose/docs/guides/using-gooseignore) restrict which files and directories goose can access (`.gitignore` files are fallback)

Changing Modes In-Session

You can change goose permission modes during a session without restarting:

- **CLI**: Use the `/mode` command (e.g. `/mode approve`)
- **Desktop**: Use the mode selector button in the bottom menu

#### Quick Setup Example[​](#quick-setup-example "Direct link to Quick Setup Example")

You might want more control over goose's operations when working with sensitive systems, exploring unfamiliar codebases, using untrusted models, or simply preferring to review actions before execution.

Here's an example configuration that enables oversight:

1. **Set the [permission mode](https://block.github.io/goose/docs/guides/goose-permissions)** to Smart Approval or Manual Approval:
   
   ```
   # ~/.config/goose/config.yaml
   GOOSE_MODE: smart_approve  # or approve
   ```
2. **Create a [`.gooseignore` file](https://block.github.io/goose/docs/guides/using-gooseignore)** in your project to protect sensitive files:
   
   ```
   .env*
   secrets.*
   *.key
   *.pem
   .git/
   ```
3. **Configure [tool permissions](https://block.github.io/goose/docs/guides/managing-tools/tool-permissions)** based on your needs

As you become more comfortable with goose's behavior, you can adjust these settings to reduce friction while maintaining appropriate safeguards for your environment.

info

Also see the [Security Guide](https://block.github.io/goose/docs/guides/security/) for information about using goose safely.