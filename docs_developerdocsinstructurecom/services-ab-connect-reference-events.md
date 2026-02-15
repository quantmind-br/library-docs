---
title: Events | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/events
source: sitemap
fetched_at: 2026-02-15T09:04:25.126634-03:00
rendered_js: false
word_count: 1108
summary: This document explains how to use the AB Connect events endpoint to maintain a fresh cache of standards through differential updates and sequence-based synchronization.
tags:
    - ab-connect
    - events-api
    - data-synchronization
    - delta-updates
    - standards-management
    - api-integration
category: guide
---

Standards evolve over time. An authority may make a major update to their Standards document. In this case, an authority re-issues an updated document that totally replaces the Standards of the past. This results in a new document being added to your license. Alternately, an authority may modify, remove or add individual Standards within the current document. If your organization is caching Standards data, it is important that you keep your cache fresh. While it is possible to purge your cache and retrieve the entire set of Standards periodically, that is inefficient and does not support the maintenance of alignments and other related data. It is more efficient and useful to request differential updates. With AB Connect, you do this using the `events` endpoint.

In addition to changes to Standards themselves, the `events` endpoint exposes changes to your access to Standards. Your access can change due to licensing changes or configuration of which Standards you have opted to have delivered. For the context of this documentation, we will refer to Standards as "deliverable" regardless of whether the changes were due to license or configuration changes because Events do not treat the various sources of the change differently. For information on changing your licensing or delivery, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29).

When a document is added to your delivery, you will receive an Event with `target` set to `document` and `change_type` set to `added`. This Event indicates that you should request and download the Standards related to the specified document. E.g. you may receive an Event that looks something like:

```
    ...
    "data": {
        "id": "0ae17409-38fd-4e26-809d-03a309139be2",
        "type": "events",
        "attributes": {
            "seq": 12354,
            "date_utc": "2017-11-12 00:00:00",
            "change_type": "added",
            "target": "document",
            "section_guid": "721CFFCC-9BDD-11E6-ABFB-8C24CDC8CA83",
            "document_guid": "351CFFCC-9BDD-11E6-ABFB-8C24CDC8CA83",
            "affected_properties": []
        },
        "relationships": {
            "standard": {
               "data": {
                }
            },
            "nondeliverable_standard": {
                "data": { }
            },
            "deleted_standard": {
               "data": {
                }
            }
       }
    }
    ...
```

That would initiate a process that requests Standards related to that document:

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?filter[standards]=document.id EQ '351CFFCC-9BDD-11E6-ABFB-8C24CDC8CA83'`
```

Similarly, if you receive an Event with `change_type` set to `removed`, your license requires that you purge the related document and references from your system.

Notes:

- Delivery Events can occur on sections as well as documents.
- Events that occur on Standards that are not delivered to you are not visible to you. The filtering of Events by deliverability is time sensitive so you will not receive Events that occurred on Standards that were not deliverable to you at the time of the Event, even if the Standard is deliverable at the time of the call.
- Since Standards changes are delivered based on the status at the time of the Event, it is possible for you to receive Events on Standards that you no longer have access to. So if you receive a change Event for a Standard and your change management process tries to look up the details of the Standard but doesn't have access, silently skip the process because a `removed` Event is somewhere later in the queue. For example:
  
  1. You are licensed to Standard A.
  2. Standard A changes so an Event is created and you have access to it.
  3. You remove Standard A from your delivery.
  4. You get a change Event for Standard A but you no longer have access to it.
  5. You get a change Event to remove Standard A.

You can request individual Events but more commonly you would request Events that have occurred since your last sync. In previous versions, the filter for requesting updates focused the filter on the date. However, this can be problematic due to concurrency and race conditions. Now, AB Connect gives each Event a sequence number to ensure no Events are missed. After each refresh, store the sequence number of the last Event you received. Future requests should request Events with sequence numbers greater than the last one you received. E.g. if the last Event you received had a sequence number of 28974, the request may look like:

```
`https://api.abconnect.instructure.com/rest/v4.1/events?filter[events]=seq GT 28974&sort[events]=seq`
```

A couple of important notes about the sequence number:

- Sequence numbers will not appear incremental. Each Event in the system gets a unique number and since the Events include partner specific Events (like changes in license and Standards delivery settings), Events received by any individual partner will not have incremental numbers.

## Using Events As A New Partner

New partners can use `seq GT 0` to start. Since you will not receive Events that occur before your license was active, you won't be flooded with historical data. The first Events you will see will be Events to add documents (and possibly sections). You can use this approach to do the initial download of the Standards into your cache. However, if you've already downloaded all of the Standards you have access to, you will want to skip this first set of Events.

One of the advantages of using Events is that you can build a workflow around them. You may want to consider caching Events before acting on them in your system. That will allow you to put the changes into an editorial workflow so you can make decisions for accurately updating alignments and other relationships.

For example, if you receive an Event indicating a Standard has been deleted, you may want to flag content aligned to that Standard as being in need of an alignment review.

Unlike Standard change Events, deliverability Events should be acted upon immediately to ensure your system is in line with license agreements.

Using filtering, it is possible to retrieve sets of Events. These Events are returned in an array of Events objects. See the Introduction for an explanation on [filtering](https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters). This section covers the specifics of using these parameters with the Events resource.

A note on filtering Events. Events can be filtered on the properties of the Event object AND on the same subset of properties of the Standards that are listed in the section on [Filtering Resources by Properties on Related Resources](https://developerdocs.instructure.com/services/ab-connect/introduction/related-objects#filtering-resources-by-properties-on-related-resources). The exceptions are the Event `affected_properties.new_value` and `affected_properties.previous_value` fields since those are of variant types.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[events]stringOptional

comma separated list of field names

filter\[events]stringOptional

an ODATA-like query string used to filter

sort\[events]stringOptional

a comma separated list of property names specifying the sort order of the returned results

facetstringOptional

A comma separated list of facet names that you are requesting the options on.

facet\_summarystringOptional

A comma separated list of facet names for which you are requesting summary information.

includestringOptional

A comma separated list of resource names that will be returned in the response.

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).