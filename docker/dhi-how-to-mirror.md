---
title: Mirror a repository
url: https://docs.docker.com/dhi/how-to/mirror/
source: llms
fetched_at: 2026-01-24T14:20:56.260515876-03:00
rendered_js: false
word_count: 1177
summary: This guide explains how to mirror Docker Hardened Image (DHI) repositories to Docker Hub or external registries to access compliance variants, support customization, and enable air-gapped workflows.
tags:
    - docker-hardened-images
    - dhi-enterprise
    - mirroring
    - container-registry
    - image-customization
    - compliance-images
    - oci-artifacts
category: guide
---

## Mirror a Docker Hardened Image repository DHI Enterprise

Subscription: Docker Hardened Images Enterprise

Mirroring requires a DHI Enterprise subscription. Without a DHI Enterprise subscription, you can pull Docker Hardened Images directly from `dhi.io` without mirroring. With a DHI Enterprise subscription, you must mirror to get:

- Compliance variants (FIPS-enabled or STIG-ready images)
- Extended Lifecycle Support (ELS) variants (requires add-on)
- Image or Helm chart customization
- Air-gapped or restricted network environments
- SLA-backed security updates

This topic covers two types of mirroring for Docker Hardened Image (DHI) repositories:

- [Mirror to Docker Hub](#mirror-a-dhi-repository-to-docker-hub): Mirror a DHI repository to your organization's namespace on Docker Hub. This requires a DHI Enterprise subscription and is used to [customize an image or chart](https://docs.docker.com/dhi/how-to/customize/) and access compliance variants and ELS variants (requires add-on). This must be done through the Docker Hub web interface.
- [Mirror to a third-party registry](#mirror-a-dhi-repository-to-a-third-party-registry): Mirror a repository to another container registry, such as Amazon ECR, Google Artifact Registry, or a private Harbor instance.

Mirroring a repository to Docker Hub requires a DHI Enterprise subscription and enables access to compliance variants, Extended Lifecycle Support (ELS) variants (requires add-on), and customization capabilities:

- Image repositories: Mirroring lets you customize images by adding packages, OCI artifacts (such as custom certificates or additional tools), environment variables, labels, and other configuration settings. For more details, see [Customize a Docker Hardened Image](https://docs.docker.com/dhi/how-to/customize/#customize-a-docker-hardened-image).
- Chart repositories: Mirroring lets you customize image references within the chart. This is particularly useful when using customized images or when you've mirrored images to a third-party registry and need the chart to reference those custom locations. For more details, see [Customize a Docker Hardened Helm chart](https://docs.docker.com/dhi/how-to/customize/#customize-a-docker-hardened-helm-chart).

Only organization owners can perform mirroring. Once mirrored, the repository becomes available in your organization's namespace, and you can customize it as needed.

To mirror a Docker Hardened Image repository:

1. Go to [Docker Hub](https://hub.docker.com) and sign in.
2. Select **My Hub**.
3. In the namespace drop-down, select your organization.
4. Select **Hardened Images** &gt; **Catalog**.
5. Select a DHI repository to view its details.
6. Mirror the repository:
   
   - To mirror an image repository, select **Use this image** &gt; **Mirror repository**, and then follow the on-screen instructions. If you have the ELS add-on, you can also select **Enable support for end-of-life versions**.
   - To mirror a Helm chart repository, select **Get Helm chart**, and then follow the on-screen instructions.

It may take a few minutes for all the tags to finish mirroring.

After mirroring a repository, the repository appears in your organization's repository list, prefixed by `dhi-`. It will continue to receive updated images.

Once mirrored, the repository works like any other private repository on Docker Hub and you can now customize it. To learn more about customization, see [Customize a Docker Hardened Image or chart](https://docs.docker.com/dhi/how-to/customize/).

### [Webhook integration for syncing and alerts](#webhook-integration-for-syncing-and-alerts)

To keep external registries or systems in sync with your mirrored Docker Hardened Images, and to receive notifications when updates occur, you can configure a [webhook](https://docs.docker.com/docker-hub/repos/manage/webhooks/) on the mirrored repository in Docker Hub. A webhook sends a `POST` request to a URL you define whenever a new image tag is pushed or updated.

For example, you might configure a webhook to call a CI/CD system at `https://ci.example.com/hooks/dhi-sync` whenever a new tag is mirrored. The automation triggered by this webhook can pull the updated image from Docker Hub and push it to an internal registry such as Amazon ECR, Google Artifact Registry, or GitHub Container Registry.

Other common webhook use cases include:

- Triggering validation or vulnerability scanning workflows
- Signing or promoting images
- Sending notifications to downstream systems

#### [Example webhook payload](#example-webhook-payload)

When a webhook is triggered, Docker Hub sends a JSON payload like the following:

### [Stop mirroring a repository](#stop-mirroring-a-repository)

Only organization owners can stop mirroring a repository. After you stop mirroring, the repository remains, but it will no longer receive updates. You can still use the last images or charts that were mirrored, but the repository will not receive new tags or updates from the original repository.

> If you only want to stop mirroring ELS versions, you can uncheck the ELS option in the mirrored repository's **Settings** tab. For more details, see [Disable ELS for a repository](https://docs.docker.com/dhi/how-to/els/#disable-els-for-a-repository).

To stop mirroring a repository:

1. Go to [Docker Hub](https://hub.docker.com) and sign in.
2. Select **My Hub**.
3. In the namespace drop-down, select your organization that has access to DHI.
4. Select **Hardened Images** &gt; **Manage**.
5. Select the **Mirrored Images** or **Mirrored Helm charts** tab.
6. In the far right column of the repository you want to stop mirroring, select the menu icon.
7. Select **Stop mirroring**.

You can optionally mirror a DHI repository to another container registry, such as Amazon ECR, Google Artifact Registry, GitHub Container Registry, or a private Harbor instance.

You can use any standard workflow to mirror the image, such as the [Docker CLI](https://docs.docker.com/reference/cli/docker/), [Docker Hub Registry API](https://docs.docker.com/reference/api/registry/latest/), third-party registry tools, or CI/CD automation.

However, to preserve the full security context, including attestations, you must also mirror its associated OCI artifacts. DHI repositories store the image layers on `dhi.io` (or `docker.io` for customized images) and the signed attestations in a separate registry (`registry.scout.docker.com`).

To copy both, you can use [`regctl`](https://regclient.org/cli/regctl/), an OCI-aware CLI that supports mirroring images along with attached artifacts such as SBOMs, vulnerability reports, and SLSA provenance. For ongoing synchronization, you can use [`regsync`](https://regclient.org/cli/regsync/).

### [Example mirroring with `regctl`](#example-mirroring-with-regctl)

The following example shows how to mirror a specific tag of a Docker Hardened Image from Docker Hub to another registry, along with its associated attestations using `regctl`. You must [install `regctl`](https://github.com/regclient/regclient) first.

The example assumes you have mirrored the DHI repository to your organization's namespace on Docker Hub as described in the previous section. You can apply the same steps to a non-mirrored image by updating the the `SRC_ATT_REPO` and `SRC_REPO` variables accordingly.

1. Set environment variables for your specific environment. Replace the placeholders with your actual values.
   
   In this example, you use a Docker username to represent a member of the Docker Hub organization that the DHI repositories are mirrored in. Prepare a [personal access token (PAT)](https://docs.docker.com/security/access-tokens/) for the user with `read only` access. Alternatively, you can use an organization namespace and an [organization access token (OAT)](https://docs.docker.com/enterprise/security/access-tokens/) to sign in to Docker Hub, but OATs are not yet supported for `registry.scout.docker.com`.
2. Sign in via `regctl` to Docker Hub, the Scout registry that contains the attestations, and your destination registry.
3. Mirror the image and attestations using `--referrers` and referrer endpoints:
4. Verify that artifacts were preserved.
   
   First, get a digest for a specific tag and platform. For example, `linux/amd64`.
   
   List attached artifacts (SBOM, provenance, VEX, vulnerability reports).
   
   Or, list attached artifacts with `docker scout`.

### [Example ongoing mirroring with `regsync`](#example-ongoing-mirroring-with-regsync)

`regsync` automates pulling from your organizations mirrored DHI repositories on Docker Hub and pushing to your external registry including attestations. It reads a YAML configuration file and can filter tags.

The following example uses a `regsync.yaml` file that syncs Node 24 and Python 3.12 Debian 13 variants, excluding Alpine and Debian 12.

To do a dry run with the configuration file, you can run the following command. You must [install `regsync`](https://github.com/regclient/regclient) first.

To run the sync with the configuration file:

After mirroring, see [Pull a DHI](https://docs.docker.com/dhi/how-to/use/#pull-a-dhi) to learn how to pull and use mirrored images.