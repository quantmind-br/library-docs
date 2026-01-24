---
title: Quickstart
url: https://docs.docker.com/scout/quickstart/
source: llms
fetched_at: 2026-01-24T14:29:29.531146227-03:00
rendered_js: false
word_count: 1102
summary: This guide provides a step-by-step introduction to using Docker Scout for identifying vulnerabilities, evaluating security policies, and improving container image compliance. It demonstrates how to analyze images through the CLI and Dashboard while remediating discovered issues in a sample application.
tags:
    - docker-scout
    - vulnerability-scanning
    - container-security
    - image-analysis
    - supply-chain-management
    - policy-evaluation
category: tutorial
---

## Docker Scout quickstart

Docker Scout analyzes image contents and generates a detailed report of packages and vulnerabilities that it detects. It can provide you with suggestions for how to remediate issues discovered by image analysis.

This guide takes a vulnerable container image and shows you how to use Docker Scout to identify and fix the vulnerabilities, compare image versions over time, and share the results with your team.

[This example project](https://github.com/docker/scout-demo-service) contains a vulnerable Node.js application that you can use to follow along.

1. Clone its repository:
2. Move into the directory:
3. Make sure you're signed in to your Docker account, either by running the `docker login` command or by signing in with Docker Desktop.
4. Build the image and push it to a `<ORG_NAME>/scout-demo:v1`, where `<ORG_NAME>` is the Docker Hub namespace you push to.

Docker Scout analyzes all local images by default. To analyze images in remote repositories, you need to enable it first. You can do this from Docker Hub, the Docker Scout Dashboard, and CLI. [Find out how in the overview guide](https://docs.docker.com/scout).

1. Sign in to your Docker account with the `docker login` command or use the **Sign in** button in Docker Desktop.
2. Next, enroll your organization with Docker Scout, using the `docker scout enroll` command.
3. Enable Docker Scout for your image repository with the `docker scout repo enable` command.

After building, use the `docker scout` CLI command to see vulnerabilities detected by Docker Scout.

The example application for this guide uses a vulnerable version of Express. The following command shows all CVEs affecting Express in the image you just built:

Docker Scout analyzes the image you built most recently by default, so there's no need to specify the name of the image in this case.

Learn more about the `docker scout cves` command in the [`CLI reference documentation`](https://docs.docker.com/reference/cli/docker/scout/cves).

After the Docker Scout analysis, a high vulnerability CVE-2022-24999 was found, caused by an outdated version of the **express** package.

The version 4.17.3 of the express package fixes the vulnerability. Therefore, update the `package.json` file to the new version:

Rebuild the image with a new tag and push it to your Docker Hub repository:

Run the `docker scout` command again and verify that HIGH CVE-2022-24999 is no longer present:

While inspecting vulnerabilities based on specific packages can be useful, it isn't the most effective way to improve your supply chain conduct.

Docker Scout also supports policy evaluation, a higher-level concept for detecting and fixing issues in your images. Policies are a set of customizable rules that let organizations track whether images are compliant with their supply chain requirements.

Because policy rules are specific to each organization, you must specify which organization's policy you're evaluating against. Use the `docker scout config` command to configure your Docker organization.

Now you can run the `quickview` command to get an overview of the compliance status for the image you just built. The image is evaluated against the default policy configurations. You'll see output similar to the following:

Exclamation marks in the status column indicate a violated policy. Question marks indicate that there isn't enough metadata to complete the evaluation. A check mark indicates compliance.

The output of the `quickview` command shows that there's room for improvement. Some of the policies couldn't evaluate successfully (`No data`) because the image lacks provenance and SBOM attestations. The image also failed the check on a few of the evaluations.

Policy evaluation does more than just check for vulnerabilities. Take the `Default non-root user` policy for example. This policy helps improve runtime security by ensuring that images aren't set to run as the `root` superuser by default.

To address this policy violation, edit the Dockerfile by adding a `USER` instruction, specifying a non-root user:

Additionally, to get a more complete policy evaluation result, your image should have SBOM and provenance attestations attached to it. Docker Scout uses the provenance attestations to determine how the image was built so that it can provide a better evaluation result.

Before you can build an image with attestations, you must enable the [containerd image store](https://docs.docker.com/desktop/features/containerd/) (or create a custom builder using the `docker-container` driver). The classic image store doesn't support manifest lists, which is how the provenance attestations are attached to an image.

Open **Settings** in Docker Desktop. Under the **General** section, make sure that the **Use containerd for pulling and storing images** option is checked, then select **Apply**. Note that changing image stores temporarily hides images and containers of the inactive image store until you switch back.

With the containerd image store enabled, rebuild the image with a new `v3` tag. This time, add the `--provenance=true` and `--sbom=true` flags.

After pushing the updated image with attestations, it's time to view the results through a different lens: the Docker Scout Dashboard.

1. Open the [Docker Scout Dashboard](https://scout.docker.com/).
2. Sign in with your Docker account.
3. Select **Images** in the left-hand navigation.

The images page lists your Scout-enabled repositories.

Select the row for the image you want to view, anywhere in the row except on a link, to open the **Image details** sidebar.

The sidebar shows a compliance overview for the last pushed tag of a repository.

> If policy results haven't appeared yet, try refreshing the page. It might take a few minutes before the results appear if this is your first time using the Docker Scout Dashboard.

Go back to the image list and select the image version, available in the **Most recent image** column. Then, at the top right of the page, select the **Update base image** button to inspect the policy.

This policy checks whether base images you use are up-to-date. It currently has a non-compliant status, because the example image uses an old version `alpine` as a base image.

Close the **Recommended fixes for base image** modal. In the policy listing, select **View fixes** button, next to the policy name for details about the violation, and recommendations on how to address it.

In this case, the recommended action is to enable [Docker Scout's GitHub integration](https://docs.docker.com/scout/integrations/source-code-management/github/), which helps keep your base images up-to-date automatically.

> You can't enable this integration for the demo app used in this guide. Feel free to push the code to a GitHub repository that you own, and try out the integration there!

This quickstart guide has scratched the surface on some of the ways Docker Scout can support software supply chain management:

- How to enable Docker Scout for your repositories
- Analyzing images for vulnerabilities
- Policy and compliance
- Fixing vulnerabilities and improving compliance

There's lots more to discover, from third-party integrations, to policy customization, and runtime environment monitoring in real-time.

Check out the following sections:

- [Image analysis](https://docs.docker.com/scout/explore/analysis/)
- [Data sources](https://docs.docker.com/scout/advisory-db-sources)
- [Docker Scout Dashboard](https://docs.docker.com/scout/dashboard)
- [Integrations](https://docs.docker.com/scout/integrations/)
- [Policy evaluation](https://docs.docker.com/scout/policy/)