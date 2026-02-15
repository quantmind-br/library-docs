---
title: Datasets | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dataset
source: sitemap
fetched_at: 2026-02-15T09:11:58.870199-03:00
rendered_js: false
word_count: 195
summary: This document explains how the Data Access Platform (DAP) organizes data replication through tables and namespaces while outlining data accuracy expectations and limitations.
tags:
    - data-replication
    - data-access-platform
    - namespaces
    - data-synchronization
    - canvas-data
category: concept
---

Data replication in Data Access Platform (DAP) is based on **tables**. You can synchronize the state of each table individually with the data stored in DAP.

Tables are organized into **namespaces**. For example, the Canvas tables `assignments`, `content_tags` or `submissions` are in the namespace `canvas`. The table `web_logs` is in the namespace `canvas_logs`. Other products have their own namespace, e.g. `catalog`.

**Disclaimer:** The data is a `best effort` attempt, and is not guaranteed to be complete or wholly accurate. This data is meant to be used for rollups and analysis in the aggregate, *not* in isolation for auditing, or other high-stakes analysis involving examining single users or small samples. Canvas logs data is generated from the Canvas logs files, not a transactional database, there are many places along the way data can be lost and/or duplicated (though uncommon). Additionally, given the size of this data, our processes ensure that errors can be rectified at any point in time, with corrections integrated as soon as they are identified and processed.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).