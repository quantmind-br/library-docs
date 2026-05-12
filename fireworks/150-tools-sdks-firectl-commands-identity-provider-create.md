---
title: firectl identity-provider create
optimized: true
optimized_at: 2026-04-27T20:16:50Z
source: sitemap
fetched_at: 2026-04-27T20:16:50.32418128-03:00
rendered_js: false
tags:
    - identity-provider
    - saml-oidc
    - create-command
    - sso
    - flags
    - authentication
    - fireworks
category: reference
word_count: 243
---
Register a new SAML or OIDC identity provider.

```
firectl identity-provider create [flags]
```

> [!note]
> `--display-name` is required.

### Examples

```bash
# SAML with metadata URL
firectl identity-provider create --display-name="Company SAML" \
  --saml-metadata-url="https://company.okta.com/app/xyz/sso/saml/metadata"

# SAML with IdP-initiated SSO
firectl identity-provider create --display-name="Company SAML" \
  --saml-metadata-url="https://company.okta.com/app/xyz/sso/saml/metadata" \
  --enable-idp-initiated-sso

# SAML with metadata XML file (URL not publicly accessible)
firectl identity-provider create --display-name="Company SAML" \
  --saml-metadata-xml-file="/path/to/metadata.xml"

# OIDC
firectl identity-provider create --display-name="Company OIDC" \
  --oidc-issuer="https://auth.company.com" \
  --oidc-client-id="abc123" \
  --oidc-client-secret="secret456"

# OIDC with multiple allowed domains
firectl identity-provider create --display-name="Example OIDC" \
  --oidc-issuer="https://accounts.google.com" \
  --oidc-client-id="client123" \
  --oidc-client-secret="secret456" \
  --tenant-domains="example.com,example.co.uk"
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--display-name` | string | **Required.** Display name of the IdP |
| `--dry-run` | | Print the request proto without running it |
| `--enable-idp-initiated-sso` | | Allow login directly from the IdP portal (SAML only) |
| `--enable-jit-user-provisioning` | | Auto-create users on first SSO login if they don't exist |
| `--enforce-sso` | | Restrict account access to approved email domains only |
| `--jit-default-role` | string | Default role for JIT-provisioned users (`admin`, `user`, `contributor`, `inference-user`) |
| `--oidc-client-id` | string | OIDC client ID |
| `--oidc-client-secret` | string | OIDC client secret |
| `--oidc-issuer` | string | OIDC issuer URL |
| `--saml-metadata-url` | string | SAML metadata URL |
| `--saml-metadata-xml-file` | string | Path to SAML metadata XML (for VPNs/behind firewall) |
| `--tenant-domains` | string | Allowed domains, comma-separated (e.g., `example.com,example.co.uk`) |
| `-o, --output` | Output | Set output format: `text`, `json`, or `flag` (default `text`) |
| `-h, --help` | | help for create |

### Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Falls back to `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |