const fs = require('fs');

const metadata = JSON.parse(fs.readFileSync('metadata.json', 'utf8'));

const renameMap = {
  "docs-core.md": "001-docs-core.md",
  "docs-core-architecture.md": "002-docs-core-architecture.md",
  "docs-core-features.md": "003-docs-core-features.md",
  "docs-core-comparison.md": "004-docs-core-comparison.md",
  "docs-core-cloud.md": "005-docs-core-cloud.md",
  "docs-core-overview.md": "006-docs-core-overview.md",
  "docs-core-videos.md": "007-docs-core-videos.md",
  "docs-core-installation.md": "008-docs-core-installation.md",
  "docs-core-manual-installation.md": "009-docs-core-manual-installation.md",
  "docs-core-uninstall.md": "010-docs-core-uninstall.md",
  "docs-core-reset-password.md": "011-docs-core-reset-password.md",
  "docs-core-troubleshooting.md": "012-docs-core-troubleshooting.md",
  "docs-core-goodies.md": "013-docs-core-goodies.md",
  "docs-core-applications.md": "014-docs-core-applications.md",
  "docs-core-databases.md": "015-docs-core-databases.md",
  "docs-core-docker-compose.md": "016-docs-core-docker-compose.md",
  "docs-core-domains.md": "017-docs-core-domains.md",
  "docs-core-variables.md": "018-docs-core-variables.md",
  "docs-core-providers.md": "019-docs-core-providers.md",
  "docs-core-ssh-keys.md": "020-docs-core-ssh-keys.md",
  "docs-core-registry.md": "021-docs-core-registry.md",
  "docs-core-certificates.md": "022-docs-core-certificates.md",
  "docs-core-github.md": "023-docs-core-github.md",
  "docs-core-gitlab.md": "024-docs-core-gitlab.md",
  "docs-core-bitbucket.md": "025-docs-core-bitbucket.md",
  "docs-core-gitea.md": "026-docs-core-gitea.md",
  "docs-core-Docker.md": "027-docs-core-Docker.md",
  "docs-core-auto-deploy.md": "028-docs-core-auto-deploy.md",
  "docs-core-registry-dockerhub.md": "029-docs-core-registry-dockerhub.md",
  "docs-core-registry-ghcr.md": "030-docs-core-registry-ghcr.md",
  "docs-core-registry-digital-ocean.md": "031-docs-core-registry-digital-ocean.md",
  "docs-core-actions.md": "032-docs-core-actions.md",
  "docs-core-aws-s3.md": "033-docs-core-aws-s3.md",
  "docs-core-cloudflare-r2.md": "034-docs-core-cloudflare-r2.md",
  "docs-core-cloud-storage.md": "035-docs-core-cloud-storage.md",
  "docs-core-backblaze-b2.md": "036-docs-core-backblaze-b2.md",
  "docs-core-backups.md": "037-docs-core-backups.md",
  "docs-core-volume-backups.md": "038-docs-core-volume-backups.md",
  "docs-core-monitoring.md": "039-docs-core-monitoring.md",
  "docs-core-webhook.md": "040-docs-core-webhook.md",
  "docs-core-telegram.md": "041-docs-core-telegram.md",
  "docs-core-discord.md": "042-docs-core-discord.md",
  "docs-core-slack.md": "043-docs-core-slack.md",
  "docs-core-email.md": "044-docs-core-email.md",
  "docs-core-pushover.md": "045-docs-core-pushover.md",
  "docs-core-gotify.md": "046-docs-core-gotify.md",
  "docs-core-ntfy.md": "047-docs-core-ntfy.md",
  "docs-core-lark.md": "048-docs-core-lark.md",
  "docs-core-applications-build-type.md": "049-docs-core-applications-build-type.md",
  "docs-core-applications-advanced.md": "050-docs-core-applications-advanced.md",
  "docs-core-applications-preview-deployments.md": "051-docs-core-applications-preview-deployments.md",
  "docs-core-applications-rollbacks.md": "052-docs-core-applications-rollbacks.md",
  "docs-core-applications-zero-downtime.md": "053-docs-core-applications-zero-downtime.md",
  "docs-core-applications-going-production.md": "054-docs-core-applications-going-production.md",
  "docs-core-watch-paths.md": "055-docs-core-watch-paths.md",
  "docs-core-schedule-jobs.md": "056-docs-core-schedule-jobs.md",
  "docs-core-databases-backups.md": "057-docs-core-databases-backups.md",
  "docs-core-databases-restore.md": "058-docs-core-databases-restore.md",
  "docs-core-databases-connection.md": "059-docs-core-databases-connection.md",
  "docs-core-databases-connection-mariadb.md": "060-docs-core-databases-connection-mariadb.md",
  "docs-core-databases-connection-mysql.md": "061-docs-core-databases-connection-mysql.md",
  "docs-core-databases-connection-mongo-atlas.md": "062-docs-core-databases-connection-mongo-atlas.md",
  "docs-core-databases-connection-pg-admin.md": "063-docs-core-databases-connection-pg-admin.md",
  "docs-core-docker-compose-example.md": "064-docs-core-docker-compose-example.md",
  "docs-core-docker-compose-utilities.md": "065-docs-core-docker-compose-utilities.md",
  "docs-core-docker-compose-domains.md": "066-docs-core-docker-compose-domains.md",
  "docs-core-domains-generated.md": "067-docs-core-domains-generated.md",
  "docs-core-domains-cloudflare.md": "068-docs-core-domains-cloudflare.md",
  "docs-core-domains-others.md": "069-docs-core-domains-others.md",
  "docs-core-remote-servers.md": "070-docs-core-remote-servers.md",
  "docs-core-remote-servers-instructions.md": "071-docs-core-remote-servers-instructions.md",
  "docs-core-remote-servers-deployments.md": "072-docs-core-remote-servers-deployments.md",
  "docs-core-remote-servers-validate.md": "073-docs-core-remote-servers-validate.md",
  "docs-core-remote-servers-security.md": "074-docs-core-remote-servers-security.md",
  "docs-core-remote-servers-build-server.md": "075-docs-core-remote-servers-build-server.md",
  "docs-core-cluster.md": "076-docs-core-cluster.md",
  "docs-core-html.md": "077-docs-core-html.md",
  "docs-core-vuejs.md": "078-docs-core-vuejs.md",
  "docs-core-nextjs.md": "079-docs-core-nextjs.md",
  "docs-core-astro.md": "080-docs-core-astro.md",
  "docs-core-astro-ssr.md": "081-docs-core-astro-ssr.md",
  "docs-core-remix.md": "082-docs-core-remix.md",
  "docs-core-nestjs.md": "083-docs-core-nestjs.md",
  "docs-core-deno.md": "084-docs-core-deno.md",
  "docs-core-preact.md": "085-docs-core-preact.md",
  "docs-core-solidjs.md": "086-docs-core-solidjs.md",
  "docs-core-svelte.md": "087-docs-core-svelte.md",
  "docs-core-tanstack.md": "088-docs-core-tanstack.md",
  "docs-core-lit.md": "089-docs-core-lit.md",
  "docs-core-qwik.md": "090-docs-core-qwik.md",
  "docs-core-turborepo.md": "091-docs-core-turborepo.md",
  "docs-core-vite-react.md": "092-docs-core-vite-react.md",
  "docs-core-11ty.md": "093-docs-core-11ty.md",
  "docs-core-enterprise.md": "094-docs-core-enterprise.md",
  "docs-core-enterprise-license-keys.md": "095-docs-core-enterprise-license-keys.md",
  "docs-core-enterprise-sso.md": "096-docs-core-enterprise-sso.md",
  "docs-core-enterprise-sso-auth0.md": "097-docs-core-enterprise-sso-auth0.md",
  "docs-core-enterprise-sso-azure.md": "098-docs-core-enterprise-sso-azure.md",
  "docs-core-enterprise-sso-keycloak.md": "099-docs-core-enterprise-sso-keycloak.md",
  "docs-core-enterprise-sso-okta.md": "100-docs-core-enterprise-sso-okta.md",
  "docs-core-guides-ec2-instructions.md": "101-docs-core-guides-ec2-instructions.md",
  "docs-core-guides-tailscale.md": "102-docs-core-guides-tailscale.md",
  "docs-core-guides-cloudflare-tunnels.md": "103-docs-core-guides-cloudflare-tunnels.md",
  "docs-core-permissions.md": "104-docs-core-permissions.md"
};

// Update each document with new file path and original file path
metadata.documents.forEach(doc => {
  const oldPath = doc.file_path;
  if (renameMap[oldPath]) {
    doc.original_file_path = oldPath;
    doc.file_path = renameMap[oldPath];
  }
});

// Add organization metadata
metadata.organization = {
  method: "sequential-numbering",
  organized_at: new Date().toISOString(),
  total_files: 104,
  categories: [
    "Introduction & Overview",
    "Installation & Quick Start",
    "Core Concepts & Fundamentals",
    "Configuration - Git Providers",
    "Configuration - Registry Providers",
    "Configuration - Storage & Backups",
    "Configuration - Monitoring & Notifications",
    "Application Management",
    "Database Management",
    "Docker Compose Deep Dive",
    "Domains & SSL Configuration",
    "Remote Servers & Clustering",
    "Tutorials - Framework Deployment",
    "Enterprise Features",
    "Guides & Advanced Networking",
    "Permissions & Reference"
  ]
};

// Write updated metadata
fs.writeFileSync('metadata.json', JSON.stringify(metadata, null, 2));
console.log('Metadata updated successfully!');
console.log(`Total documents: ${metadata.documents.length}`);
console.log(`Organization method: ${metadata.organization.method}`);
console.log(`Categories: ${metadata.organization.categories.length}`);