---
title: LiteLLM Self-Hosted Security & Encryption FAQ | liteLLM
url: https://docs.litellm.ai/docs/proxy/security_encryption_faq
source: sitemap
fetched_at: 2026-01-21T19:53:35.598557473-03:00
rendered_js: false
word_count: 923
summary: This document outlines the security protocols for LiteLLM, detailing how data in transit and at rest are secured through TLS/SSL and specific database encryption practices. It provides technical configuration steps for SSL certificates and identifies which data types, such as API keys, are encrypted versus stored in plaintext.
tags:
    - litellm
    - encryption
    - security-configuration
    - tls-ssl
    - data-security
    - ssl-certificates
category: reference
---

## Data in Transit Encryption[​](#data-in-transit-encryption "Direct link to Data in Transit Encryption")

### Does the product encrypt data in transit?[​](#does-the-product-encrypt-data-in-transit "Direct link to Does the product encrypt data in transit?")

**Yes**, LiteLLM encrypts data in transit using TLS/SSL.

### Available in both OSS and Enterprise?[​](#available-in-both-oss-and-enterprise "Direct link to Available in both OSS and Enterprise?")

**Yes**, TLS encryption is available in both Open Source and Enterprise versions.

### In transit between the calling client and the product?[​](#in-transit-between-the-calling-client-and-the-product "Direct link to In transit between the calling client and the product?")

**Yes**, HTTPS/TLS is supported through SSL certificate configuration.

**Configuration:**

```
# CLI
litellm --ssl_keyfile_path /path/to/key.pem --ssl_certfile_path /path/to/cert.pem

# Environment Variables
export SSL_KEYFILE_PATH="/path/to/key.pem"
export SSL_CERTFILE_PATH="/path/to/cert.pem"
```

**Documentation Reference:** `docs/my-website/docs/guides/security_settings.md`

### In transit between the product and the LLM providers?[​](#in-transit-between-the-product-and-the-llm-providers "Direct link to In transit between the product and the LLM providers?")

**Yes**, all connections to LLM providers use TLS encryption by default.

**Implementation Details:**

- Uses Python's `ssl.create_default_context()`
- Leverages HTTPX and aiohttp libraries with SSL/TLS enabled
- Uses certifi CA bundle by default for SSL verification

**Code Reference:** `litellm/llms/custom_httpx/http_handler.py` (lines 43-105)

### Are TCP sessions to the LLM providers shared?[​](#are-tcp-sessions-to-the-llm-providers-shared "Direct link to Are TCP sessions to the LLM providers shared?")

**Yes**, TCP connections are pooled and reused.

**Details:**

- Connection pooling is enabled by default
- Default: 1000 max concurrent connections with keepalive
- Sessions are maintained across requests to the same provider
- Reduces overhead of TLS handshakes

**Code Reference:** `litellm/llms/custom_httpx/http_handler.py` (lines 704-712)

### Or does the product negotiate a new TLS session with the same LLM provider for every sequential call?[​](#or-does-the-product-negotiate-a-new-tls-session-with-the-same-llm-provider-for-every-sequential-call "Direct link to Or does the product negotiate a new TLS session with the same LLM provider for every sequential call?")

**No**, TLS sessions are reused through connection pooling. New TLS handshakes are not performed for every request.

### How is it encrypted?[​](#how-is-it-encrypted "Direct link to How is it encrypted?")

**TLS 1.2 and TLS 1.3**

Uses Python's default SSL context which supports both TLS 1.2 and TLS 1.3. The specific version negotiated depends on:

- Python version
- System SSL library (typically OpenSSL)
- Server capabilities

**Implementation:** `ssl.create_default_context()` in Python

### How are these added to the product's configuration?[​](#how-are-these-added-to-the-products-configuration "Direct link to How are these added to the product's configuration?")

#### x.509 Certificate[​](#x509-certificate "Direct link to x.509 Certificate")

**Method 1: CLI Arguments**

```
litellm --ssl_certfile_path /path/to/certificate.pem
```

**Method 2: Environment Variable**

```
export SSL_CERTFILE_PATH="/path/to/certificate.pem"
```

#### Private Key[​](#private-key "Direct link to Private Key")

**Method 1: CLI Arguments**

```
litellm --ssl_keyfile_path /path/to/private_key.pem
```

**Method 2: Environment Variable**

```
export SSL_KEYFILE_PATH="/path/to/private_key.pem"
```

#### Certificate Bundle/Chain[​](#certificate-bundlechain "Direct link to Certificate Bundle/Chain")

**For client-to-proxy connections:** Use standard SSL certificate setup with intermediate certificates bundled in the certfile.

**For proxy-to-LLM provider connections:**

**Method 1: Config YAML**

```
litellm_settings:
ssl_verify:"/path/to/ca_bundle.pem"
```

**Method 2: Environment Variable**

```
export SSL_CERT_FILE="/path/to/ca_bundle.pem"
```

**Method 3: Client Certificate Authentication**

```
litellm_settings:
ssl_certificate:"/path/to/client_certificate.pem"
```

or

```
export SSL_CERTIFICATE="/path/to/client_certificate.pem"
```

### Documentation Coverage[​](#documentation-coverage "Direct link to Documentation Coverage")

**Primary Documentation:**

- `docs/my-website/docs/guides/security_settings.md` - SSL/TLS configuration guide

**Additional References:**

- `litellm/proxy/proxy_cli.py` (lines 455-467) - CLI options
- `docs/my-website/docs/completion/http_handler_config.md` - Custom HTTP handler configuration

* * *

## Data at Rest Encryption[​](#data-at-rest-encryption "Direct link to Data at Rest Encryption")

### Does the product encrypt data at rest?[​](#does-the-product-encrypt-data-at-rest "Direct link to Does the product encrypt data at rest?")

**Partially**. Only specific sensitive data is encrypted at rest.

### What data is stored in encrypted form?[​](#what-data-is-stored-in-encrypted-form "Direct link to What data is stored in encrypted form?")

#### Encrypted Data:[​](#encrypted-data "Direct link to Encrypted Data:")

1. **LLM API Keys** - Model credentials in `LiteLLM_ProxyModelTable.litellm_params`
2. **Provider Credentials** - Stored in `LiteLLM_CredentialsTable.credential_values`
3. **Configuration Secrets** - Sensitive config values in `LiteLLM_Config` table
4. **Virtual Keys** - When using secret managers (optional feature)

#### NOT Encrypted:[​](#not-encrypted "Direct link to NOT Encrypted:")

1. **Spend Logs** - Request/response data in `LiteLLM_SpendLogs`
2. **Audit Logs** - Change history in `LiteLLM_AuditLog`
3. **User/Team/Organization Data** - Metadata and configuration
4. **Cached Prompts and Completions** - Cache data is stored in plaintext

### Cached prompts and completions?[​](#cached-prompts-and-completions "Direct link to Cached prompts and completions?")

**No**, cached prompts and completions are **NOT encrypted**.

Cache backends (Redis, S3, local disk) store data as plaintext JSON.

**Code References:**

- `litellm/caching/redis_cache.py`
- `litellm/caching/s3_cache.py`
- `litellm/caching/caching.py`

### Configuration data?[​](#configuration-data "Direct link to Configuration data?")

**Partially encrypted**.

#### What IS Encrypted:[​](#what-is-encrypted "Direct link to What IS Encrypted:")

- LLM API keys and credentials in model configurations
- Sensitive values in `LiteLLM_Config` table
- Credential values in `LiteLLM_CredentialsTable`

#### What is NOT Encrypted:[​](#what-is-not-encrypted "Direct link to What is NOT Encrypted:")

- Model names and aliases
- Rate limits and budget settings
- User/team/organization metadata
- Non-sensitive configuration parameters

**Code Reference:** `litellm/proxy/management_endpoints/model_management_endpoints.py` (lines 275-308)

### Log data?[​](#log-data "Direct link to Log data?")

**No**, log data is **NOT encrypted**.

Log data stored in database tables is in plaintext:

- `LiteLLM_SpendLogs` - Contains request/response data, tokens, spend
- `LiteLLM_ErrorLogs` - Error information
- `LiteLLM_AuditLog` - Audit trail of changes

**Note:** You can disable logging to avoid storing sensitive data:

```
general_settings:
disable_spend_logs:True# Disable writing spend logs to DB
disable_error_logs:True# Disable writing error logs to DB
```

**Documentation:** `docs/my-website/docs/proxy/db_info.md` (lines 52-60)

### Where is it stored?[​](#where-is-it-stored "Direct link to Where is it stored?")

#### In the DB?[​](#in-the-db "Direct link to In the DB?")

**Yes**, encrypted data is stored in PostgreSQL database.

**Key Tables with Encrypted Data:**

- `LiteLLM_ProxyModelTable` - Model configurations with encrypted API keys
- `LiteLLM_CredentialsTable` - Credential values
- `LiteLLM_Config` - Configuration secrets

**Schema Reference:** `schema.prisma`

#### In the filesystem?[​](#in-the-filesystem "Direct link to In the filesystem?")

**No**, encrypted data is not stored in the filesystem by default.

**Note:** If using disk cache (`disk_cache_dir`), cached data is stored unencrypted.

#### Somewhere else?[​](#somewhere-else "Direct link to Somewhere else?")

**Optional:** When using secret managers (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault), encrypted data can be stored externally.

**Configuration:**

```
general_settings:
key_management_system:"aws_secret_manager"# or "azure_key_vault", "hashicorp_vault"
```

**Documentation:** `docs/my-website/docs/secret.md`

### How is it encrypted?[​](#how-is-it-encrypted-1 "Direct link to How is it encrypted?")

**Algorithm:** NaCl SecretBox (XSalsa20-Poly1305 AEAD)

**NOT AES-256** - LiteLLM uses NaCl (Networking and Cryptography Library) which provides:

- XSalsa20 stream cipher
- Poly1305 MAC for authentication
- Equivalent security to AES-256

**Key Derivation:**

1. Takes `LITELLM_SALT_KEY` (or `LITELLM_MASTER_KEY` if salt key not set)
2. Hashes with SHA-256 to derive 256-bit encryption key
3. Uses NaCl SecretBox for authenticated encryption

**Code Reference:** `litellm/proxy/common_utils/encrypt_decrypt_utils.py` (lines 69-112)

**Implementation:**

```
import hashlib
import nacl.secret

# Derive 256-bit key from salt
hash_object = hashlib.sha256(signing_key.encode())
hash_bytes = hash_object.digest()

# Create SecretBox and encrypt
box = nacl.secret.SecretBox(hash_bytes)
encrypted = box.encrypt(value_bytes)
```

### Setting the Encryption Key[​](#setting-the-encryption-key "Direct link to Setting the Encryption Key")

**Required Environment Variable:**

```
export LITELLM_SALT_KEY="your-strong-random-key-here"
```

**Important Notes:**

- ⚠️ **Must be set before adding any models**
- ⚠️ **Never change this key** - encrypted data becomes unrecoverable
- ⚠️ Use a strong random key (recommended: [https://1password.com/password-generator/](https://1password.com/password-generator/))
- If not set, falls back to `LITELLM_MASTER_KEY`

**Documentation:** `docs/my-website/docs/proxy/prod.md` (section 8, lines 184-196)

### Documentation Coverage[​](#documentation-coverage-1 "Direct link to Documentation Coverage")

**Primary Documentation:**

- `docs/my-website/docs/proxy/prod.md` (section 8) - LITELLM\_SALT\_KEY setup
- `docs/my-website/docs/secret.md` - Secret management systems
- `docs/my-website/docs/proxy/db_info.md` - Database information

**Additional References:**

- `security.md` - General security measures
- `docs/my-website/docs/data_security.md` - Data privacy overview
- `schema.prisma` - Database schema with encrypted fields

* * *

## Summary of Security Features[​](#summary-of-security-features "Direct link to Summary of Security Features")

### ✅ Provided Out of the Box[​](#-provided-out-of-the-box "Direct link to ✅ Provided Out of the Box")

1. **TLS/SSL encryption** for client-to-proxy connections
2. **TLS encryption** for proxy-to-LLM provider connections (with connection pooling)
3. **Encrypted storage** of LLM API keys and credentials
4. **Support for TLS 1.2 and TLS 1.3**
5. **Connection pooling** to reduce TLS handshake overhead

### ⚠️ Important Limitations[​](#%EF%B8%8F-important-limitations "Direct link to ⚠️ Important Limitations")

1. **Cached data is NOT encrypted** (Redis, S3, disk cache)
2. **Log data is NOT encrypted** (spend logs, audit logs)
3. **Request/response payloads in logs are NOT encrypted**
4. **Uses NaCl SecretBox, NOT AES-256** (equivalent security)
5. **TLS version not explicitly configured** - uses Python/system defaults

### 🔧 Configuration Requirements[​](#-configuration-requirements "Direct link to 🔧 Configuration Requirements")

**For Production Deployments:**

1. **Set LITELLM\_SALT\_KEY** before adding any models
2. **Configure SSL certificates** for HTTPS client connections
3. **Consider disabling logs** if they contain sensitive data
4. **Use secret managers** for enhanced security (optional)
5. **Configure CA bundles** if using custom certificates

* * *

## Quick Start Security Checklist[​](#quick-start-security-checklist "Direct link to Quick Start Security Checklist")

```
# 1. Generate a strong salt key
export LITELLM_SALT_KEY="$(openssl rand -base64 32)"

# 2. Set up SSL certificates (for HTTPS)
export SSL_KEYFILE_PATH="/path/to/private_key.pem"
export SSL_CERTFILE_PATH="/path/to/certificate.pem"

# 3. Configure database
export DATABASE_URL="postgresql://user:password@host:port/dbname"

# 4. (Optional) Disable logs if they contain sensitive data
# Add to config.yaml:
# general_settings:
#   disable_spend_logs: True
#   disable_error_logs: True

# 5. Start LiteLLM Proxy
litellm --config config.yaml
```

* * *

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- **LiteLLM Documentation:** [https://docs.litellm.ai/](https://docs.litellm.ai/)
- **Security Settings Guide:** [https://docs.litellm.ai/docs/guides/security\_settings](https://docs.litellm.ai/docs/guides/security_settings)
- **Production Deployment:** [https://docs.litellm.ai/docs/proxy/prod](https://docs.litellm.ai/docs/proxy/prod)
- **Secret Management:** [https://docs.litellm.ai/docs/secret](https://docs.litellm.ai/docs/secret)

For security inquiries: [support@berri.ai](mailto:support@berri.ai)