---
title: Managing Moodle version documentation | Moodle Developer Resources
url: https://moodledev.io/general/documentation/forking-versions
source: sitemap
fetched_at: 2026-02-17T16:02:03.032575-03:00
rendered_js: false
word_count: 250
summary: This document outlines the procedural steps for creating and archiving version-specific developer documentation for Moodle using Docusaurus.
tags:
    - moodle
    - documentation
    - versioning
    - docusaurus
    - release-management
    - content-archiving
category: guide
---

We generate version-specific documentation and maintain this for each supported version of Moodle.

When a new version of Moodle is released, the documentation is 'forked'.

When a version of Moodle goes out of support, its developer documentation is archived.

Further information about this functionality is available in the [Docusaurus documentation on the topic](https://docusaurus.io/docs/versioning).

## Creating a new version of the docs[​](#creating-a-new-version-of-the-docs "Direct link to Creating a new version of the docs")

Typically this task is performed by the Integration team using the following steps:

1. Ensure that all pending appropriate merge requests have been merged
2. Ensure that your local branch is up-to-date
3. Run the docusaurus version command:
   
   ```
   yarn docusaurus docs:version [version]
   ```
4. Commit the initial changes ([Example from Moodle 4.4](https://github.com/moodle/devdocs/commit/e9e7fa0074753487c315d2f91ad64a8503f32054))
5. Update non-automated version mentions:
   
   1. Open `versioned_docs/version-[version]/intro.md` in your editor
      
      1. Uncomment and update the link to the release notes for this version
   2. Open `docs/devupdate.md` in your editor
      
      1. Clear the content of this file and update the version numbers
   3. Open `docs/intro.md` in your editor
      
      1. Update the occurrences of the version number for the recent release with the version number for the next major version of Moodle
   4. Open `nextVersion.js` in your editor
      
      1. Update the values for `nextVersion` (and `nextLTSVersion` after the release of an LTS version)
   5. Open `general/releases/[version].md`
      
      1. Update links to the release notes in User Docs to point to the actual version
   6. Open `/static/_redirects`
      
      1. Update the `nextVersion` redirect
6. Commit these changes ([Example from Moodle 4.4](https://github.com/moodle/devdocs/commit/aeb6385209caed38d757d53bc47f9bd66fdcfa0c))
7. Create a pull request ([Example from Moodle 4.4](https://github.com/moodle/devdocs/pull/1006))

## Archiving a version of the docs[​](#archiving-a-version-of-the-docs "Direct link to Archiving a version of the docs")

The archival of a set of documentation usually happens immediately after the forking of documentation for the latest version.

1. After the Pull Request for this new version has been accepted, navigate to the Deploy Logs, and locate its "Permalink".
2. Remove the entire folder from `versioned_docs` and `versioned_sidebars`:
   
   ```
   rm -rf versioned_docs/version-4.3 versioned_sidebars/version-4.3-*
   ```
3. Commit the changes
4. Update any remaining references to the version:
   
   1. Open the `versionsArchived.json` file and add the full link to the Netlify build.
   2. Open the `versions.json` file and remove the version from the list
   3. Search for any remaining occurrences as a path, for example:
5. Commit these changes
6. Create a pull request