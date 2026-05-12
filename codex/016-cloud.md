---
number: 16
category: cloud
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://platform.openai.com/docs/codex-cloud
word_count: 572
---
# OpenAI Codex Cloud

> **BLUF:** Codex Cloud provides managed compute infrastructure for OpenAI Codex, offering remote connections to powerful VMs with pre-configured environments. Designed for teams and individuals who need scalable, reproducible development environments without local setup.

## Overview

Codex Cloud extends local Codex CLI functionality to remote, cloud-hosted environments. It enables:
- **Remote compute:** Access high-performance VMs without local hardware constraints
- **Pre-configured environments:** Standardized setups with dependencies pre-installed
- **Team collaboration:** Shared environments with consistent configurations
- **Persistent workspaces:** Code and state persist between sessions

## Architecture

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Local     │──────▶│  Codex      │──────▶│   Remote    │
│   Client    │◄──────│  Cloud      │◄──────│   VM        │
│   (CLI)     │      │  Gateway    │      │   (Sandbox) │
└─────────────┘      └─────────────┘      └─────────────┘
```

## Getting Started

### Prerequisites
- OpenAI account with Codex access
- Local Codex CLI installed (`npm install -g @openai/codex`)
- SSH key configured in OpenAI account settings

### Setup
1. **Enable Cloud Access:** Contact OpenAI sales or enable in platform dashboard
2. **Configure SSH Key:** Add public key at [platform.openai.com/settings](https://platform.openai.com/settings)
3. **Connect:** `codex cloud connect <workspace-name>`

## Workspaces

Workspaces are isolated, persistent environments with dedicated compute resources.

| Feature | Description |
|---------|-------------|
| Isolation | Each workspace has separate filesystem and processes |
| Persistence | Files survive session restarts |
| Snapshots | Create named checkpoints of workspace state |
| Sharing | Invite team members with read/write permissions |

### Workspace Commands
```bash
codex cloud create my-project --tier standard
codex cloud list
codex cloud connect my-project
codex cloud snapshot create my-project backup-2025-01-15
codex cloud share my-project --user teammate@company.com --role write
```

## Compute Tiers

| Tier | Specs | Best For |
|------|-------|----------|
| `standard` | 4 vCPU, 16GB RAM | General development, small projects |
| `performance` | 16 vCPU, 64GB RAM | Large codebases, intensive tasks |
| `gpu` | 8 vCPU, 32GB RAM, 1x GPU | ML training, GPU-accelerated workloads |

Set tier at creation: `codex cloud create --tier performance`

## Configuration

### Environment Variables
| Variable | Description |
|----------|-------------|
| `OPENAI_CLOUD_WORKSPACE` | Default workspace name |
| `OPENAI_CLOUD_TIER` | Default compute tier |
| `CODEX_CLOUD_REGION` | Preferred region (`us-east-1`, `eu-west-1`, `ap-southeast-1`) |

### Config File (`~/.codex/cloud.yaml`)
```yaml
default_workspace: my-project
preferred_tier: performance
region: us-east-1
auto_connect: true
sync_local_changes: true
```

## Security

- **Network Isolation:** Workspaces run in isolated VPCs with no inbound access except via Codex gateway
- **Encryption:** All traffic TLS 1.3; data at rest encrypted with AES-256
- **Sandboxing:** Remote execution uses same sandbox as local CLI (seatbelt/Landlock)
- **Audit Logging:** All commands and file changes logged with 90-day retention

## Billing

| Component | Pricing |
|-----------|---------|
| Compute | Per-minute based on tier |
| Storage | $0.10/GB/month |
| Egress | First 1TB free, then $0.09/GB |
| Snapshots | $0.05/GB/month |

Billing aggregated per OpenAI organization. Set budget alerts in dashboard.

## Limitations

- Max workspace uptime: 8 hours/session (auto-sleep after inactivity)
- Max storage: 100GB per workspace
- Max concurrent workspaces: 5 per organization
- GPU tier requires approval (contact sales)

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Connection timeout | Check `codex cloud status`; retry with `--region` |
| Permission denied | Verify SSH key added to platform settings |
| Workspace full | Delete old snapshots or upgrade tier |
| Sync conflicts | Run `codex cloud sync --resolve` to force local wins |

## Comparison: Local vs Cloud

| Feature | Local CLI | Cloud |
|---------|-----------|-------|
| Setup | Node.js 22+ required | Zero local dependencies |
| Compute | Local hardware | Scalable VMs |
| Persistence | Local filesystem only | Cloud storage + snapshots |
| Collaboration | Git-based | Real-time shared workspaces |
| Offline use | Yes | No |
| Cost | API usage only | Compute + storage fees |

---

*Source: [OpenAI Platform Docs](https://platform.openai.com/docs/codex-cloud)*
