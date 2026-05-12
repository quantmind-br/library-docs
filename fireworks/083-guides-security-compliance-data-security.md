---
title: Data Security
url: https://docs.fireworks.ai/guides/security_compliance/data_security
source: sitemap
fetched_at: 2026-04-27T20:18:20.968168937-03:00
rendered_js: false
word_count: 476
summary: Overview of Fireworks AI security measures: zero data retention, secure data handling, workload isolation, and compliance certifications.
tags:
    - security-measures
    - data-protection
    - compliance-frameworks
    - zero-retention
    - workload-isolation
    - encryption
category: guide
optimized: true
optimized_at: 2026-04-27T23:00:00Z
---
Fireworks designs all systems, infrastructure, and business processes to ensure customer trust through verifiable security and compliance. See our [Trust Center](https://trust.fireworks.ai/) for documentation and audit reports.

## Zero Data Retention

Fireworks does not log or store prompt or generation data for open models, without explicit user opt-in. See our [[098-guides-security-compliance-data-handling|Zero Data Retention Policy]].

## Secure Data Handling

- **Data Ownership & Control:** Customers maintain ownership. Data stored as part of an active workflow can be permanently deleted with auditable confirmation. Secure wipe processes ensure deleted assets cannot be reconstructed.
- **Encryption:** Data encrypted in transit (TLS 1.2+) and at rest (AES-256).
- **Bring Your Own Bucket:** Customers may integrate their own cloud storage to retain governance and apply their own compliance frameworks:
  - **Datasets:** [[048-fine-tuning-secure-fine-tuning#gcs-bucket-integration|GCS Bucket Integration]] (AWS S3 coming soon)
  - **Models:** [[087-models-uploading-custom-models#uploading-your-model|External AWS S3 Bucket Integration]]
  - **Encryption Keys (coming soon):** Customers may choose their own keys and policies for end-to-end control.

- **Access Logging:** All customer data access is logged, monitored, and protected against tampering. See [[082-guides-security-compliance-audit-logs|Audit & Access Logs]].

## Workload Isolation

Dedicated workloads run in logically isolated environments, preventing cross-customer access or data leakage.

## Secure Training

Fireworks enables secure model training (fine-tuning and reinforcement learning) while maintaining customer control over sensitive components and data.

- **Customer-Controlled Architecture:** For advanced workflows like RL, critical components remain under customer control:
  - Reward models and reward functions are proprietary and not shared
  - Rollout servers and training metrics are built and managed by customers
  - Model checkpoints managed through secure cloud storage registries
- **Minimal Data Sharing:** Training data shared via controlled bucket access with minimal sharing and step-wise retention.
- **API-Based Integration:** Customers leverage Fireworks training APIs while maintaining full control over sensitive components.

## Technical Safeguards

- **Device Trust:** Only approved, secured devices with strong authentication can access sensitive Fireworks systems.
- **Identity & Access Management:** Fine-grained access controls enforced across all environments, following least privilege principle.
- **Network Security:**
  - Private network isolation for customer workloads
  - Firewalls and security groups prevent unauthorized traffic
  - DDoS protection across core services
- **Monitoring & Detection:** Real-time anomaly detection alerts on suspicious activity
- **Vulnerability Management:** Continuous scanning and patching keep infrastructure current

## Operational Security

- **Security Reviews & Testing:** Regular penetration testing validates controls
- **Incident Response:** Formal response plan ensures swift containment, customer notification, and remediation
- **Employee Access:** Minimal subset of Fireworks personnel have production access; all access is logged and periodically reviewed
- **Third-Party Risk Management:** Vendors and subprocessors undergo rigorous due diligence and contractual security obligations

## Compliance & Certifications

- **SOC 2 Type II** — certified
- **ISO 27001 / ISO 27701 / ISO 42001** — in progress
- **HIPAA Support:** Fireworks is HIPAA compliant, supporting healthcare and life sciences organizations
- **Regulatory Alignment:** Controls mapped to GDPR, CCPA, and other international data protection frameworks