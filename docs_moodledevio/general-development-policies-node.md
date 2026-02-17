---
title: NodeJS | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/node
source: sitemap
fetched_at: 2026-02-17T15:59:24.170793-03:00
rendered_js: false
word_count: 276
summary: This document outlines Moodle's policy and procedures for maintaining and upgrading Node.js versions and project dependencies across supported software branches.
tags:
    - nodejs
    - moodle-development
    - dependency-management
    - versioning-policy
    - package-json
    - software-maintenance
category: guide
---

New LTS NodeJS versions are [released every 12 months](https://github.com/nodejs/release#release-schedule) and supported for three years. Moodle tries to ensure a compromise between support and churn by ensuring that the version of NodeJS in use is supported at all times.

## Policy statement[​](#policy-statement "Direct link to Policy statement")

### NodeJS[​](#nodejs "Direct link to NodeJS")

1. This policy will be applied to *all* supported branches, including stable and security-only releases.
2. This policy does not require that any tool be updated, unless strictly needed by nodejs/npm or its own dependencies/changes
3. It won't include npm audit changes either. Those are handled separately.
4. Normally, only changes to `.nvmrc` and `package.json` will happen.
5. Changes to project dependencies should be handled in a separate issue.

### Project Dependencies[​](#project-dependencies "Direct link to Project Dependencies")

1. To avoid impact to the community, dependency updates which impact built output should be kept to a minimum.
2. Dependency updates should be backported to the first Major release in a Series, for example Moodle 5.0.

## Upgrade guidelines[​](#upgrade-guidelines "Direct link to Upgrade guidelines")

### NodeJS[​](#nodejs-1 "Direct link to NodeJS")

To update the NodeJS version required, the following approach is typically recommended:

1. Update the `.nvmrc` file to reflect the `lts/[name]` of the new LTS version
2. Update the `package.json` to set the `engines` for the new restiction in the format: `>= [new version] < [next version]`, for example:
   
   ```
   "engines":{
   "node":">=20.11.0 <21"
   }
   ```
3. Install the new NodeJS version:
4. Update the NodeJS dependencies with the new version of NodeJS:
   
   ```
   rm -rf node_modules
   npm install
   ```
5. Verify the update:

In most situations there will be no issues here and changes can be committed and backported to all stable and security-supported branches.

#### Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

Where a project dependency is no longer supported due to the new version of NodeJS, it may be necessary to upgrade the dependency.

### Project dependencies[​](#project-dependencies-1 "Direct link to Project dependencies")

The following tooling may be useful for the purposes of updating the project dependencies:

- `npm outdated`
- `npm audit`