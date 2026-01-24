---
title: Archive
url: https://docs.docker.com/docker-hub/repos/archive/
source: llms
fetched_at: 2026-01-24T14:21:34.90321518-03:00
rendered_js: false
word_count: 243
summary: This guide explains the process and effects of archiving and unarchiving repositories on Docker Hub to manage outdated content and maintain image security.
tags:
    - docker-hub
    - repository-management
    - archiving
    - maintenance
    - image-registry
    - repo-settings
category: guide
---

## Archive or unarchive a repository

You can archive a repository on Docker Hub to mark it as read-only and indicate that it's no longer actively maintained. This helps prevent the use of outdated or unsupported images in workflows. Archived repositories can also be unarchived if needed.

Docker Hub highlights repositories that haven't been updated in over a year by displaying an icon ( ![outdated icon](https://docs.docker.com/docker-hub/repos/images/outdated-icon.webp) ) next to them on the [**Repositories** page](https://hub.docker.com/repositories/). Consider reviewing these highlighted repositories and archiving them if necessary.

When a repository is archived, the following occurs:

- The repository information can't be modified.
- New images can't be pushed to the repository.
- An **Archived** label is displayed on the public repository page.
- Users can still pull the images.

You can unarchive an archived repository to remove the archived state. When unarchived, the following occurs:

- The repository information can be modified.
- New images can be pushed to the repository.
- The **Archived** label is removed on the public repository page.

## [Archive a repository](#archive-a-repository)

1. Sign in to [Docker Hub](https://hub.docker.com).
2. Select **My Hub** &gt; **Repositories**.
   
   A list of your repositories appears.
3. Select a repository.
   
   The **General** page for the repository appears.
4. Select the **Settings** tab.
5. Select **Archive repository**.
6. Enter the name of your repository to confirm.
7. Select **Archive**.

## [Unarchive a repository](#unarchive-a-repository)

1. Sign in to [Docker Hub](https://hub.docker.com).
2. Select **My Hub** &gt; **Repositories**.
   
   A list of your repositories appears.
3. Select a repository.
   
   The **General** page for the repository appears.
4. Select the **Settings** tab.
5. Select **Unarchive repository**.