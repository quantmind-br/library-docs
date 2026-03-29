# Guia Completo: Slash Commands em Agentes de IA

**Data de criação:** 2026-02-05  
**Versão:** 1.1  
**Ferramentas analisadas:** Gemini CLI, Claude Code, Codex (OpenAI), OpenCode

> **Nota:** Este documento inclui referências à documentação local em `~/dev/library-docs/`. Consulte a seção [Referências](#referências) para acessar os arquivos originais de cada ferramenta.

---

## Sumário

1. [Introdução](#introdução)
2. [Gemini CLI](#gemini-cli)
3. [Claude Code](#claude-code)
4. [Codex (OpenAI)](#codex-openai)
5. [OpenCode](#opencode)
6. [Tabela Comparativa](#tabela-comparativa)
7. [Exemplos Práticos](#exemplos-práticos)
8. [Recomendações](#recomendações)

---

## Introdução

Slash commands são atalhos de comando que permitem aos usuários executar ações específicas, prompts personalizados ou workflows automatizados em agentes de IA. Cada ferramenta implementa este recurso de forma diferente, com variações em formato de arquivo, localização, sintaxe e recursos avançados.

Este guia documenta as implementações de quatro principais ferramentas de agentes de IA, permitindo que desenvolvedores escolham a melhor abordagem para seus casos de uso.

---

## Gemini CLI

**Documentação local:**
- Índice: `/home/diogo/dev/library-docs/gemini-cli/000-index.md`
- Custom Commands: `/home/diogo/dev/library-docs/gemini-cli/046-docs-cli-custom-commands.md`
- Skills: `/home/diogo/dev/library-docs/gemini-cli/047-docs-cli-skills.md`

### Visão Geral

O Gemini CLI utiliza arquivos **TOML** para definir custom commands. É a implementação mais simples e direta, ideal para comandos rápidos sem necessidade de recursos avançados.

### Localização dos Arquivos

| Escopo | Caminho | Disponibilidade |
|--------|---------|-----------------|
| **Global (Usuário)** | `~/.gemini/commands/` | Qualquer projeto |
| **Projeto (Local)** | `<project-root>/.gemini/commands/` | Apenas projeto atual |
| **Extensão** | `.gemini/extensions/<ext>/commands/` | Onde extensão está instalada |

**Precedência:** Projeto > Usuário > Extensão

### Formato do Arquivo

**Formato:** TOML (`.toml`)

**Campos obrigatórios:**
- `prompt` (String): Prompt enviado ao modelo

**Campos opcionais:**
- `description` (String): Descrição para o menu `/help`

### Convenção de Nomenclatura

O nome do comando é determinado pelo caminho relativo ao diretório `commands/`:

| Caminho do Arquivo | Comando Resultante |
|-------------------|-------------------|
| `commands/test.toml` | `/test` |
| `commands/git/commit.toml` | `/git:commit` |
| `commands/refactor/pure.toml` | `/refactor:pure` |

**Regra:** Separadores de diretório (`/` ou `\`) são convertidos para dois-pontos (`:`)

### Sintaxe e Recursos

#### Argumentos com `{{args}}`

```toml
# git/fix.toml
description = "Gera uma correção para um problema"
prompt = "Por favor, forneça uma correção de código para o problema descrito aqui: {{args}}."
```

**Comportamento inteligente:**
- Fora de `!{...}`: Injeção raw (texto exato)
- Dentro de `!{...}`: **Shell-escaped** automaticamente

#### Execução de Comandos Shell com `!{...}`

```toml
# git/commit.toml
description = "Gera mensagem de commit baseada nas mudanças staged"
prompt = """
Por favor, gere uma mensagem de commit no formato Conventional Commit baseada no seguinte diff:
```diff
!{git diff --staged}
```
"""
```

**Fluxo de segurança:**
1. CLI substitui `!{...}` pelo output do comando
2. Pede **confirmação** antes de executar
3. Se falhar, inclui stderr no output

#### Injeção de Arquivos com `@{...}`

```toml
# review.toml
description = "Revisa código usando guia de boas práticas"
prompt = """
Você é um revisor de código especialista.
Sua tarefa é revisar {{args}}.
Use as seguintes boas práticas:
@{docs/best-practices.md}
"""
```

**Suporta:**
- Arquivos de texto: conteúdo injetado diretamente
- Imagens (PNG, JPEG), PDFs, áudio, vídeo: multimodal encoding
- Diretórios: lista recursiva respeitando `.gitignore`

#### Argumentos Padrão (sem `{{args}}`)

Se o prompt não contiver `{{args}}`, o CLI anexa o comando completo ao final do prompt.

### Exemplo Completo

```toml
# ~/.gemini/commands/changelog.toml
description = "Adiciona uma nova entrada ao CHANGELOG.md"
prompt = """
# Tarefa: Atualizar Changelog
Você é um mantenedor experiente de projetos de software.

## Formato Esperado
O comando segue o formato: `/changelog <version> <type> <message>`
- `<type>` deve ser um de: "added", "changed", "fixed", "removed"

## Comportamento
1. Leia o arquivo `CHANGELOG.md`
2. Encontre a seção para a `<version>` especificada
3. Adicione a `<message>` sob o cabeçalho correto de `<type>`
4. Se a versão ou seção não existir, crie-a
5. Siga estritamente o formato "Keep a Changelog"
"""
```

**Uso:** `/changelog 1.2.0 added "Nova funcionalidade de busca"`

---

## Claude Code

**Documentação local:**
- Índice: `/home/diogo/dev/library-docs/claude-code/000-index.md`
- Skills: `/home/diogo/dev/library-docs/claude-code/019-docs-en-skills.md`
- Plugins: `/home/diogo/dev/library-docs/claude-code/017-docs-en-plugins.md`
- Plugins Reference: `/home/diogo/dev/library-docs/claude-code/043-docs-en-plugins-reference.md`

### Visão Geral

O Claude Code utiliza o conceito de **Skills** - arquivos Markdown com frontmatter YAML que seguem o padrão aberto [Agent Skills](https://agentskills.io). É a implementação mais flexível, com suporte a subagents, permissões granulares e auto-invocação.

### Localização dos Arquivos

| Escopo | Caminho | Disponibilidade |
|--------|---------|-----------------|
| **Enterprise** | Via managed settings | Todos usuários da organização |
| **Global (Personal)** | `~/.claude/skills/<skill-name>/SKILL.md` | Todos seus projetos |
| **Projeto (Local)** | `.claude/skills/<skill-name>/SKILL.md` | Apenas este projeto |
| **Plugin** | `<plugin>/skills/<skill-name>/SKILL.md` | Onde plugin está habilitado |

**Precedência:** Enterprise > Personal > Project > Plugin

### Formato do Arquivo

**Formato:** Markdown (`SKILL.md`) com **YAML Frontmatter**

**Estrutura básica:**
```markdown
---
name: nome-do-skill
description: Descrição que ajuda Claude a selecionar o skill
---

Suas instruções detalhadas aqui em markdown...
```

**Campos do Frontmatter:**

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `name` | Não | Nome do comando (usa diretório se omitido) |
| `description` | Recomendado | Quando usar o skill (usado para auto-seleção) |
| `argument-hint` | Não | Hint de autocomplete |
| `disable-model-invocation` | Não | Impede auto-invocação (`true`/`false`) |
| `user-invocable` | Não | Esconde do menu (`true`/`false`) |
| `allowed-tools` | Não | Ferramentas permitidas sem aprovação |
| `model` | Não | Modelo específico |
| `context` | Não | `fork` para executar em subagent |
| `agent` | Não | Tipo de subagent (`Explore`, `Plan`, etc.) |

### Convenção de Nomenclatura

| Localização | Comando de Invocação |
|-------------|---------------------|
| `~/.claude/skills/my-skill/SKILL.md` | `/my-skill` ou `$my-skill` |
| `plugin/skills/hello/SKILL.md` | `/plugin-name:hello` |

### Sintaxe e Recursos

#### Argumentos

```markdown
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---

Fix GitHub issue $ARGUMENTS following our coding standards.

1. Read the issue description
2. Understand the requirements
3. Implement the fix
4. Write tests
5. Create a commit
```

**Variáveis disponíveis:**

| Variável | Descrição |
|----------|-----------|
| `$ARGUMENTS` | Todos os argumentos |
| `$ARGUMENTS[N]` | Argumento específico por índice (0-based) |
| `$N` | Shorthand para `$ARGUMENTS[N]` (ex: `$0`, `$1`, `$2`) |
| `${CLAUDE_SESSION_ID}` | ID da sessão atual |

**Exemplo com múltiplos argumentos:**
```markdown
---
name: migrate-component
description: Migrate a component from one framework to another
---

Migrate the $0 component from $1 to $2.
Preserve all existing behavior and tests.
```

**Uso:** `/migrate-component SearchBar React Vue`

#### Execução de Comandos Shell

```markdown
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

## Your task
Summarize this pull request...
```

**Como funciona:**
1. Cada ``!`command``` executa imediatamente (antes do Claude ver)
2. O output substitui o placeholder
3. Claude recebe o prompt completamente renderizado

#### Subagents (Context Fork)

```markdown
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:

1. Find relevant files using Glob and Grep
2. Read and analyze the code
3. Summarize findings with specific file references
```

**Quando usar:**
- Tarefas que precisam de isolamento de contexto
- Pesquisas extensas
- Tarefas que não devem poluir o contexto principal

#### Arquivos Auxiliares

```
my-skill/
├── SKILL.md           # Instruções principais (obrigatório)
├── reference.md       # Documentação detalhada (opcional)
├── examples.md        # Exemplos de uso (opcional)
└── scripts/
    └── helper.py      # Script executável (opcional)
```

**Referência em SKILL.md:**
```markdown
## Additional resources

- For complete API details, see [reference.md](reference.md)
- For usage examples, see [examples.md](examples.md)
```

#### Controle de Invocação

| Frontmatter | Você pode invocar | Claude pode invocar | Quando carregado |
|-------------|-------------------|---------------------|------------------|
| (default) | Sim | Sim | Descrição sempre no contexto, skill completo quando invocado |
| `disable-model-invocation: true` | Sim | Não | Descrição não está no contexto, skill completo quando você invoca |
| `user-invocable: false` | Não | Sim | Descrição sempre no contexto, skill completo quando invocado |

### Exemplo Completo

```markdown
# ~/.claude/skills/explain-code/SKILL.md
---
name: explain-code
description: Explains code with visual diagrams and analogies. Use when explaining how code works, teaching about a codebase, or when the user asks "how does this work?"
---

When explaining code, always include:

1. **Start with an analogy**: Compare the code to something from everyday life
2. **Draw a diagram**: Use ASCII art to show the flow, structure, or relationships
3. **Walk through the code**: Explain step-by-step what happens
4. **Highlight a gotcha**: What's a common mistake or misconception?

Keep explanations conversational. For complex concepts, use multiple analogies.
```

**Uso:**
- Automático: "How does this code work?"
- Manual: `/explain-code src/auth/login.ts`

---

## Codex (OpenAI)

**Documentação local:**
- Índice: `/home/diogo/dev/library-docs/codex/000-index.md`
- Custom Prompts: `/home/diogo/dev/library-docs/codex/029-codex-custom-prompts.md`
- Create Skills: `/home/diogo/dev/library-docs/codex/033-codex-skills-create-skill.md`
- Agent Skills: `/home/diogo/dev/library-docs/codex/032-codex-skills.md`
- CLI Slash Commands: `/home/diogo/dev/library-docs/codex/020-codex-cli-slash-commands.md`

### Visão Geral

O Codex tem **dois sistemas diferentes**: Custom Prompts (pessoais) e Skills (compartilháveis). Custom Prompts são mais simples e diretos, enquanto Skills seguem o padrão Agent Skills e podem ser compartilhados.

### Localização dos Arquivos

#### Custom Prompts (Pessoal)

| Escopo | Caminho |
|--------|---------|
| **User** | `~/.codex/prompts/<nome>.md` |

#### Skills (Compartilhável)

| Escopo | Caminho | Precedência |
|--------|---------|-------------|
| **REPO (CWD)** | `$CWD/.codex/skills/<skill-name>/SKILL.md` | ⭐ Mais alta |
| **REPO (Parent)** | `$CWD/../.codex/skills/<skill-name>/SKILL.md` | |
| **REPO (Root)** | `$REPO_ROOT/.codex/skills/<skill-name>/SKILL.md` | |
| **USER** | `~/.codex/skills/<skill-name>/SKILL.md` | |
| **ADMIN** | `/etc/codex/skills/<skill-name>/SKILL.md` | |
| **SYSTEM** | Built-in com Codex | ⭐ Mais baixa |

### Formato do Arquivo

#### Custom Prompts

**Formato:** Markdown (`.md`) com **YAML Frontmatter**

```markdown
---
description: Prep a branch, commit, and open a draft PR
argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
---

Create a branch named `dev/<feature_name>` for this work.
If files are specified, stage them first: $FILES.
Commit the staged changes with a clear message.
Open a draft PR on the same branch. Use $PR_TITLE when supplied.
```

#### Skills

**Formato:** Markdown (`SKILL.md`) com **YAML Frontmatter**

```markdown
---
name: draft-commit-message
description: Draft a conventional commit message when the user asks for help writing a commit message.
metadata:
  short-description: Draft an informative commit message.
---

Draft a conventional commit message that matches the change summary provided by the user.

Requirements:
- Use the Conventional Commits format: `type(scope): summary`
- Use the imperative mood in the summary
- Keep the summary under 72 characters
```

### Convenção de Nomenclatura

| Tipo | Caminho | Comando |
|------|---------|---------|
| **Prompt** | `~/.codex/prompts/draftpr.md` | `/prompts:draftpr` |
| **Skill** | `.codex/skills/my-skill/SKILL.md` | `$my-skill` (mention) |

### Sintaxe e Recursos

#### Argumentos em Custom Prompts

```markdown
---
description: Create a new component
---

Create a new React component named $ARGUMENTS with TypeScript support.
Include proper typing and basic structure.
```

**Variáveis disponíveis:**

| Variável | Descrição |
|----------|-----------|
| `$1` - `$9` | Argumentos posicionais (1-9) |
| `$ARGUMENTS` | Todos os argumentos |
| `$KEY` | Placeholders nomeados (ex: `$FILES`, `$PR_TITLE`) |
| `$$` | Literal `$` (escape) |

**Formato de argumentos:**
- Posicionais: `arg1 arg2 arg3`
- Nomeados: `KEY=value` ou `KEY="value with spaces"`

**Exemplo:**
```markdown
---
description: Review code with specific focus
argument-hint: [FILES=<paths>] [FOCUS="<area>"]
---

Review the following files: $FILES
Focus specifically on: $FOCUS
```

**Uso:** `/prompts:review FILES="src/auth.ts" FOCUS="security"`

#### Invocação de Skills

**Explícita:**
```bash
# Via comando /skills
/skills

# Via mention com $
$skill-name
```

**Implícita (Automática):**
Codex pode invocar automaticamente baseado na `description` do skill.

**Exemplo:**
```markdown
---
name: draft-commit-message
description: Draft a conventional commit message when the user asks for help writing a commit message.
---
```

**Prompt que ativa:** *"Help me write a commit message for these changes..."*

#### Estrutura de Skills Completa

```
my-skill/
├── SKILL.md              # Instruções principais (obrigatório)
├── scripts/              # Código executável (opcional)
│   └── validate.py
├── references/           # Documentação (opcional)
│   └── api-docs.md
└── assets/               # Templates, recursos (opcional)
    └── template.json
```

### Exemplo Completo

#### Custom Prompt

```markdown
# ~/.codex/prompts/draftpr.md
---
description: Prep a branch, commit, and open a draft PR
argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
---

Create a branch named `dev/<feature_name>` for this work.
If files are specified, stage them first: $FILES.
Commit the staged changes with a clear message.
Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.
```

**Uso:** `/prompts:draftpr FILES="src/pages/index.astro" PR_TITLE="Add hero animation"`

#### Skill

```markdown
# .codex/skills/code-review/SKILL.md
---
name: code-review
description: Reviews code for best practices and potential issues. Use when reviewing code, checking PRs, or analyzing code quality.
---

When reviewing code, check for:
1. Code organization and structure
2. Error handling
3. Security concerns
4. Test coverage
```

**Uso:** `$code-review` ou automático quando relevante

---

## OpenCode

**Documentação local:**
- Índice: `/home/diogo/dev/library-docs/opencodeai/000-index.md`
- Commands: `/home/diogo/dev/library-docs/opencodeai/021-docs-commands.md`
- Agent Skills: `/home/diogo/dev/library-docs/opencodeai/022-docs-skills.md`
- TUI: `/home/diogo/dev/library-docs/opencodeai/004-docs-tui.md`

### Visão Geral

O OpenCode suporta **dois sistemas**: Custom Commands (Markdown) e Agent Skills. Além disso, é o único que oferece configuração via JSON e mantém compatibilidade com skills do Claude Code.

### Localização dos Arquivos

#### Custom Commands

| Escopo | Caminho |
|--------|---------|
| **Global** | `~/.config/opencode/commands/<nome>.md` |
| **Per-project** | `.opencode/commands/<nome>.md` |

#### Agent Skills

| Escopo | Caminho |
|--------|---------|
| **Project config** | `.opencode/skills/<nome>/SKILL.md` |
| **Global config** | `~/.config/opencode/skills/<nome>/SKILL.md` |
| **Claude-compatible (project)** | `.claude/skills/<nome>/SKILL.md` |
| **Claude-compatible (global)** | `~/.claude/skills/<nome>/SKILL.md` |

### Formato do Arquivo

#### Custom Commands (Markdown)

```markdown
---
description: Run tests with coverage
agent: build
model: anthropic/claude-3-5-sonnet-20241022
---

Run the full test suite with coverage report and show any failures.
Focus on the failing tests and suggest fixes.
```

#### Agent Skills (Markdown)

```markdown
---
name: git-release
description: Create consistent releases and changelogs
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: github
---

## What I do
- Draft release notes from merged PRs
- Propose a version bump
- Provide a copy-pasteable `gh release create` command

## When to use me
Use this when you are preparing a tagged release.
```

#### Configuração JSON

```json
{
  "$schema": "https://opencode.ai/config.json",
  "command": {
    "test": {
      "template": "Run the full test suite with coverage report...",
      "description": "Run tests with coverage",
      "agent": "build",
      "model": "anthropic/claude-3-5-sonnet-20241022"
    }
  }
}
```

### Convenção de Nomenclatura

| Tipo | Caminho do Arquivo | Comando Resultante |
|------|-------------------|-------------------|
| **Command** | `.opencode/commands/test.md` | `/test` |
| **Skill** | `.opencode/skills/git-release/SKILL.md` | Via `skill` tool |

### Sintaxe e Recursos

#### Argumentos

```markdown
---
description: Create a new component
---

Create a new React component named $ARGUMENTS with TypeScript support.
```

**Ou posicionais:**
```markdown
---
description: Create a new file with content
---

Create a file named $1 in the directory $2 with content: $3
```

**Uso:** `/create-file config.json src "{ \"key\": \"value\" }"`

**Variáveis disponíveis:**

| Variável | Descrição |
|----------|-----------|
| `$ARGUMENTS` | Todos os argumentos |
| `$1`, `$2`, `$3`... | Argumentos posicionais |

#### Shell Output Injection

```markdown
---
description: Analyze test coverage
---

Here are the current test results:
!`npm test`
Based on these results, suggest improvements.
```

#### File References

```markdown
---
description: Review component
---

Review the component in @src/components/Button.tsx.
Check for performance issues.
```

#### Opções de Configuração

| Opção | Descrição |
|-------|-----------|
| `template` | Prompt enviado ao LLM (obrigatório em JSON) |
| `description` | Descrição no TUI |
| `agent` | Qual agente executa (`build`, `plan`, etc.) |
| `model` | Override do modelo |
| `subtask` | Força execução como subagent (`true`/`false`) |

#### Skills - Campos do Frontmatter

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `name` | Sim | Nome do skill (1-64 caracteres, lowercase alphanumeric com hífens) |
| `description` | Sim | Descrição (1-1024 caracteres) |
| `license` | Não | Licença do skill |
| `compatibility` | Não | Compatibilidade (ex: `opencode`) |
| `metadata` | Não | Mapa de strings para metadados adicionais |

#### Permissões de Skills

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "pr-review": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

**Valores:**
- `allow`: Skill carrega imediatamente
- `deny`: Skill escondido do agente
- `ask`: Usuário é perguntado antes de carregar

### Exemplo Completo

#### Custom Command

```markdown
# .opencode/commands/test.md
---
description: Run tests with coverage
agent: build
model: anthropic/claude-3-5-sonnet-20241022
---

Run the full test suite with coverage report and show any failures.
Focus on the failing tests and suggest fixes.
```

**Uso:** `/test`

#### Agent Skill

```markdown
# .opencode/skills/git-release/SKILL.md
---
name: git-release
description: Create consistent releases and changelogs
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: github
---

## What I do
- Draft release notes from merged PRs
- Propose a version bump
- Provide a copy-pasteable `gh release create` command

## When to use me
Use this when you are preparing a tagged release.
Ask clarifying questions if the target versioning scheme is unclear.
```

**Uso:** `skill({ name: "git-release" })`

---

## Tabela Comparativa

### Visão Geral

| Aspecto | Gemini CLI | Claude Code | Codex | OpenCode |
|---------|------------|-------------|-------|----------|
| **Formato Principal** | TOML | Markdown + YAML | Markdown + YAML | Markdown + YAML |
| **Arquivo** | `.toml` | `SKILL.md` ou `.md` | `SKILL.md` ou `.md` | `.md` ou `SKILL.md` |
| **Config JSON** | ❌ Não | ❌ Não | ❌ Não | ✅ Sim |
| **Padrão** | Custom Commands | Skills | Prompts + Skills | Commands + Skills |

### Localização

| Ferramenta | Global | Projeto | Plugin/Extensão | Precedência |
|------------|--------|---------|-----------------|-------------|
| **Gemini CLI** | `~/.gemini/commands/` | `<proj>/.gemini/commands/` | `.gemini/extensions/<ext>/commands/` | Projeto > User > Extensão |
| **Claude Code** | `~/.claude/skills/` | `.claude/skills/` | `plugin/skills/` | Enterprise > User > Projeto > Plugin |
| **Codex** | `~/.codex/prompts/` + `~/.codex/skills/` | `.codex/skills/` | ❌ Não | REPO > USER > ADMIN > SYSTEM |
| **OpenCode** | `~/.config/opencode/commands/` + `~/.config/opencode/skills/` | `.opencode/commands/` + `.opencode/skills/` | ❌ Não | Projeto > Global |

### Variáveis e Argumentos

| Ferramenta | Posicionais | Todos Args | Nomeados | Shell | Arquivos |
|------------|-------------|------------|----------|-------|----------|
| **Gemini CLI** | ❌ Não | `{{args}}` | ❌ Não | `!{cmd}` | `@{path}` |
| **Claude Code** | `$0`, `$1`, `$2`... | `$ARGUMENTS` | `$ARGUMENTS[N]` | ``!`cmd``` | Manual |
| **Codex** | `$1`, `$2`... `$9` | `$ARGUMENTS` | `$KEY` | ❌ Não | `@file` |
| **OpenCode** | `$1`, `$2`... | `$ARGUMENTS` | ❌ Não | ``!`cmd``` | `@file` |

### Invocação

| Ferramenta | Comando | Mencionar | Auto-invocação |
|------------|---------|-----------|----------------|
| **Gemini CLI** | `/command` | ❌ Não | ❌ Não |
| **Claude Code** | `/skill-name` | `$skill-name` | ✅ Sim (por descrição) |
| **Codex** | `/prompts:name` | `$skill-name` | ✅ Sim (skills only) |
| **OpenCode** | `/command` | `skill({name})` | ❌ Não (skills via tool) |

### Features Avançadas

| Feature | Gemini CLI | Claude Code | Codex | OpenCode |
|---------|------------|-------------|-------|----------|
| **Subagent/Context fork** | ❌ Não | ✅ Sim (`context: fork`) | ❌ Não | ✅ Sim (`agent`, `subtask`) |
| **Arquivos auxiliares** | ❌ Não | ✅ Sim (scripts, templates) | ✅ Sim (scripts, assets) | ✅ Sim (scripts, references) |
| **Permissões granulares** | ❌ Não | ✅ Sim (`allowed-tools`) | ❌ Não | ✅ Sim (permission patterns) |
| **Model override** | ❌ Não | ✅ Sim (`model`) | ❌ Não | ✅ Sim (`model`) |
| **Namespace** | `dir:command` | `plugin:skill` | Não | Não |
| **Escape `$`** | Não aplicável | Não aplicável | `$$` | Não documentado |

---

## Exemplos Práticos

### Cenário 1: Gerar Commit Message

#### Gemini CLI
```toml
# ~/.gemini/commands/git/commit.toml
description = "Generate conventional commit message"
prompt = """
Generate a conventional commit message based on staged changes:
!{git diff --staged}

Use format: type(scope): summary
"""
```

**Uso:** `/git:commit`

---

#### Claude Code
```markdown
# ~/.claude/skills/commit-gen/SKILL.md
---
name: commit-gen
description: Generate conventional commit message from staged changes
disable-model-invocation: true
---

Generate a conventional commit message based on these changes:
!`git diff --staged`

Use format: type(scope): summary
```

**Uso:** `/commit-gen` ou `$commit-gen`

---

#### Codex (Prompt)
```markdown
# ~/.codex/prompts/commit.md
---
description: Generate conventional commit message
---

Generate a conventional commit message based on staged changes.
Use format: type(scope): summary
```

**Uso:** `/prompts:commit`

---

#### OpenCode (Command)
```markdown
# .opencode/commands/commit.md
---
description: Generate conventional commit message
agent: build
---

Generate a conventional commit message based on staged changes:
!`git diff --staged`

Use format: type(scope): summary
```

**Uso:** `/commit`

---

### Cenário 2: Code Review

#### Gemini CLI
```toml
# ~/.gemini/commands/review.toml
description = "Review code for issues"
prompt = """
Review the following code for:
1. Code quality and best practices
2. Potential bugs or issues
3. Security concerns
4. Performance optimizations

Code to review:
{{args}}
"""
```

**Uso:** `/review @src/components/Button.tsx`

---

#### Claude Code
```markdown
# ~/.claude/skills/code-review/SKILL.md
---
name: code-review
description: Reviews code for best practices and potential issues. Use when reviewing code, checking PRs, or analyzing code quality.
---

When reviewing code, check for:
1. Code organization and structure
2. Error handling
3. Security concerns
4. Test coverage

Provide specific, actionable feedback with examples.
```

**Uso:** `/code-review` ou automático quando relevante

---

#### Codex (Skill)
```markdown
# .codex/skills/code-review/SKILL.md
---
name: code-review
description: Reviews code for best practices and potential issues. Use when reviewing code, checking PRs, or analyzing code quality.
---

When reviewing code, check for:
1. Code organization and structure
2. Error handling
3. Security concerns
4. Test coverage
```

**Uso:** `$code-review` ou automático

---

#### OpenCode (Command)
```markdown
# .opencode/commands/review.md
---
description: Review code for issues
agent: plan
---

Review the following code for:
1. Code quality and best practices
2. Potential bugs or issues
3. Security concerns
4. Performance optimizations

Code to review:
@$1
```

**Uso:** `/review src/components/Button.tsx`

---

### Cenário 3: Criar Componente React

#### Gemini CLI
```toml
# ~/.gemini/commands/react/component.toml
description = "Create a new React component"
prompt = """
Create a new React component with the following specifications:
- Name: {{args}}
- TypeScript support
- Props interface
- Basic styling
- Usage example

Follow best practices for React development.
"""
```

**Uso:** `/react:component Button`

---

#### Claude Code
```markdown
# ~/.claude/skills/create-react-component/SKILL.md
---
name: create-react-component
description: Create a new React component with TypeScript support
disable-model-invocation: true
---

Create a new React component with:
1. TypeScript interfaces for props
2. Functional component structure
3. Basic styling (CSS modules or styled-components)
4. PropTypes or TypeScript validation
5. Usage example

Component name: $0
Location: $1 (optional, default: src/components/)
```

**Uso:** `/create-react-component Button src/components/ui/`

---

#### Codex (Prompt)
```markdown
# ~/.codex/prompts/react-component.md
---
description: Create a new React component
argument-hint: [NAME=<name>] [LOCATION=<path>]
---

Create a new React component named $NAME.

Requirements:
- TypeScript support with proper interfaces
- Functional component
- Basic styling
- Props validation
- Usage example

Save to: $LOCATION (default: src/components/)
```

**Uso:** `/prompts:react-component NAME=Button LOCATION=src/components/ui/`

---

#### OpenCode (Command)
```markdown
# .opencode/commands/react-component.md
---
description: Create a new React component
agent: build
---

Create a new React component with:
1. TypeScript interfaces for props
2. Functional component structure
3. Basic styling
4. Props validation
5. Usage example

Component name: $1
Location: $2 (optional, default: src/components/)
```

**Uso:** `/react-component Button src/components/ui/`

---

## Recomendações

### Por Caso de Uso

| Caso de Uso | Ferramenta Recomendada | Motivo |
|-------------|------------------------|--------|
| **Comandos simples e rápidos** | Gemini CLI | TOML é simples, sem boilerplate |
| **Workflows complexos com contexto** | Claude Code | Subagents, permissões granulares |
| **Prompts pessoais não compartilháveis** | Codex Prompts | Simples, direto ao ponto |
| **Skills compartilháveis em equipe** | Codex Skills | Fácil de versionar e compartilhar |
| **Flexibilidade máxima** | OpenCode | JSON config, múltiplos formatos, compatibilidade |
| **Integração com Claude existente** | OpenCode | Suporta `.claude/skills/` nativamente |

### Por Nível de Experiência

| Nível | Ferramenta Recomendada | Por quê |
|-------|------------------------|---------|
| **Iniciante** | Gemini CLI | Sintaxe TOML simples, fácil de começar |
| **Intermediário** | Codex Prompts | Markdown familiar, rápido de prototipar |
| **Avançado** | Claude Code | Recursos avançados, controle total |
| **Enterprise/Equipe** | OpenCode | Compatibilidade, configuração flexível |

### Por Tipo de Projeto

| Tipo de Projeto | Ferramenta | Padrão Recomendado |
|-----------------|------------|-------------------|
| **Projeto pessoal** | Qualquer | Commands ou Prompts |
| **Projeto em equipe** | Codex ou OpenCode | Skills (versionáveis) |
| **Empresa/Enterprise** | Claude Code ou OpenCode | Skills com permissões |
| **Multi-repositório** | Claude Code | Skills globais |

---

## Referências

### Documentação Oficial (Web)

- **Gemini CLI:** https://geminicli.com/docs/cli/custom-commands
- **Claude Code:** https://code.claude.com/docs/en/skills
- **Codex:** https://developers.openai.com/codex/custom-prompts
- **OpenCode:** https://opencode.ai/docs/commands

### Documentação Local (~/dev/library-docs/)

#### Índices Principais

| Ferramenta | Arquivo de Índice |
|------------|-------------------|
| **Gemini CLI** | `/home/diogo/dev/library-docs/gemini-cli/000-index.md` |
| **Claude Code** | `/home/diogo/dev/library-docs/claude-code/000-index.md` |
| **Codex (OpenAI)** | `/home/diogo/dev/library-docs/codex/000-index.md` |
| **OpenCode** | `/home/diogo/dev/library-docs/opencodeai/000-index.md` |

#### Documentação Específica por Ferramenta

**Gemini CLI:**
- Índice geral: `/home/diogo/dev/library-docs/gemini-cli/000-index.md`
- Custom Commands: `/home/diogo/dev/library-docs/gemini-cli/046-docs-cli-custom-commands.md`
- Skills: `/home/diogo/dev/library-docs/gemini-cli/047-docs-cli-skills.md`

**Claude Code:**
- Índice geral: `/home/diogo/dev/library-docs/claude-code/000-index.md`
- Skills: `/home/diogo/dev/library-docs/claude-code/019-docs-en-skills.md`
- Plugins: `/home/diogo/dev/library-docs/claude-code/017-docs-en-plugins.md`
- Plugins Reference: `/home/diogo/dev/library-docs/claude-code/043-docs-en-plugins-reference.md`

**Codex (OpenAI):**
- Índice geral: `/home/diogo/dev/library-docs/codex/000-index.md`
- Custom Prompts: `/home/diogo/dev/library-docs/codex/029-codex-custom-prompts.md`
- Create Skills: `/home/diogo/dev/library-docs/codex/033-codex-skills-create-skill.md`
- Agent Skills: `/home/diogo/dev/library-docs/codex/032-codex-skills.md`
- CLI Slash Commands: `/home/diogo/dev/library-docs/codex/020-codex-cli-slash-commands.md`

**OpenCode:**
- Índice geral: `/home/diogo/dev/library-docs/opencodeai/000-index.md`
- Commands: `/home/diogo/dev/library-docs/opencodeai/021-docs-commands.md`
- Agent Skills: `/home/diogo/dev/library-docs/opencodeai/022-docs-skills.md`
- TUI: `/home/diogo/dev/library-docs/opencodeai/004-docs-tui.md`

### Padrões e Especificações

- **Agent Skills Specification:** https://agentskills.io
- **TOML:** https://toml.io
- **YAML:** https://yaml.org

---

## Changelog

### v1.1 (2026-02-05)
- Adicionadas referências absolutas à documentação local em `~/dev/library-docs/`
- Incluídas tabelas de referência rápida para documentação específica de cada ferramenta
- Atualizada seção de referências com caminhos absolutos dos arquivos

### v1.0 (2026-02-05)
- Documentação inicial completa
- Comparação entre Gemini CLI, Claude Code, Codex e OpenCode
- Exemplos práticos para 3 cenários comuns
- Tabelas comparativas detalhadas
- Recomendações por caso de uso

---

*Documento gerado automaticamente a partir da análise da documentação oficial de cada ferramenta.*
