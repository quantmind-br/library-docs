---
title: Bulk migrate images
url: https://docs.docker.com/docker-hub/repos/manage/hub-images/bulk-migrate/
source: llms
fetched_at: 2026-01-24T14:21:54.196827621-03:00
rendered_js: false
word_count: 779
summary: This guide provides instructions and workflows for migrating Docker images in bulk between Docker Hub organizations or namespaces using tools like crane and regctl. It details methods for moving individual tags, entire repositories, and multiple image collections while maintaining multi-architecture integrity.
tags:
    - docker-hub
    - image-migration
    - container-registry
    - crane
    - regctl
    - devops-workflows
    - registry-management
category: guide
---

This guide shows you how to migrate Docker images in bulk between Docker Hub organizations or namespaces. Whether you're consolidating repositories, changing organization structure, or moving images to a new account, these techniques help you migrate efficiently while preserving image integrity.

The topic is structured to build up in scale:

1. [Migrate a single image tag](#migrate-a-single-image-tag)
2. [Migrate all tags for a repository](#migrate-all-tags-for-a-repository)
3. [Migrate multiple repositories](#migrate-multiple-repositories)

The recommended tool for this workflow is `crane`. An equivalent alternative using `regctl` is also shown. Both tools perform registry-to-registry copies without pulling images locally and preserve multi-architecture images.

`crane` is recommended for its simplicity and focused image-copying workflow. `regctl` is also a good choice, particularly if you already use it for broader registry management tasks beyond image copying.

> The main workflows in this topic operate on tagged images only. Untagged manifests or content no longer reachable from tags are not migrated. In practice, these are usually unused artifacts, but be aware of this limitation before migration. While you can migrate specific untagged manifests using [digest references](#migrate-by-digest), there is no API to enumerate untagged manifests in a repository.

Before you begin, ensure you have:

- One of the following installed and available in your `$PATH`:
  
  - [`crane`](https://github.com/google/go-containerregistry)
  - [`regctl`](https://regclient.org/usage/regctl/)
- Push access to both the source and destination organizations
- Registry authentication configured for your chosen tool

Both tools authenticate directly against registries:

- `crane` uses Docker credential helpers and `~/.docker/config.json`. See the [crane documentation](https://github.com/google/go-containerregistry/tree/main/cmd/crane/doc).
- `regctl` uses its own configuration file and can import Docker credentials. See the [regctl documentation](https://github.com/regclient/regclient/tree/main/docs).

Follow the authentication instructions for your registry and tool of choice.

This is the simplest and most common migration scenario.

The following example script copies the image manifest directly between registries and preserves multi-architecture images when present. Repeat this process for each tag you want to migrate. Replace the environment variable values with your source and destination organization names, repository name, and tag.

### [Migrate by digest](#migrate-by-digest)

To migrate a specific image by digest instead of tag, use the digest in the source reference. This is useful when you need to migrate an exact image version, even if the tag has been updated. Replace the environment variable values with your source and destination organization names, repository name, digest, and tag. You can choose between `crane` and `regctl` for the copy operation.

To migrate every tagged image in a repository, use the Docker Hub API to enumerate tags and copy each one. The following example script retrieves all tags for a given repository and migrates them in a loop. This approach scales to repositories with many tags without overwhelming local resources. Note that there is a rate limit on Docker Hub requests, so you may need to add delays or pagination handling for large repositories.

Replace the environment variable values with your source and destination organization names and repository name. If your source repository is private, also set `HUB_USER` and `HUB_TOKEN` with credentials that have pull access. You can also choose between `crane` and `regctl` for the copy operation.

> Docker Hub automatically creates the destination repository on first push if your account has permission.

To migrate several repositories, create a list and run the single-repository script for each one.

For example, create a `repos.txt` file with repository names:

Save the script from the previous section as `migrate-single-repo.sh`. Then, run the following example script that processes each repository in the file. Replace the environment variable values with your source and destination organization names.

After copying, verify that source and destination match by comparing digests.

### [Basic digest verification](#basic-digest-verification)

The following example script retrieves the image digest for a specific tag from both source and destination and compares them. If the digests match, the migration is successful. Replace the environment variable values with your source and destination organization names, repository name, and tag. You can choose between `crane` and `regctl` for retrieving digests.

### [Multi-arch verification](#multi-arch-verification)

For multi-architecture images, also verify the manifest list to ensure all platforms were copied correctly. Replace the environment variable values with your source and destination organization names, repository name, and tag. You can choose between `crane` and `regctl` for retrieving manifests.

After migrating your images, complete these additional steps:

1. Copy repository metadata in the Docker Hub UI or via API:
   
   - README content
   - Repository description
   - Topics and tags
2. Configure repository settings to match the source:
   
   - Visibility (public or private)
   - Team permissions and access controls
3. Reconfigure integrations in the destination organization:
   
   - Webhooks
   - Automated builds
   - Security scanners
4. Update image references in your projects:
   
   - Change `FROM oldorg/repo:tag` to `FROM neworg/repo:tag` in Dockerfiles
   - Update deployment configurations
   - Update documentation
5. Deprecate the old location:
   
   - Update the source repository description to point to the new location
   - Consider adding a grace period before making the old repository private or read-only