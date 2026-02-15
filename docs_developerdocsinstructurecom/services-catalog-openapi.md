---
title: APIs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi
source: sitemap
fetched_at: 2026-02-15T08:59:30.597424-03:00
rendered_js: false
word_count: 1742
summary: This document provides technical specifications for a REST API designed to manage applicants, orders, user registrations, course programs, and administrative account associations.
tags:
    - api-documentation
    - rest-api
    - user-management
    - enrollment-management
    - authentication
    - account-administration
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

listing\_idstringOptional

Only include applicants for the specified listing

statusstringOptional

Only include applicants for the specified status (waitlist, accepted, declined, or expired)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

listing\_idintegerRequired

Only delete applicants for the specified listing

canvas\_user\_idstringOptional

Only delete applicants with the specified canvas user id if specified

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific applicant record

200

Getting a specific applicant record

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

fromstringOptional

Earliest date/time to return. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

tostringOptional

Latest date/time to return. See 'from' above for format.

canvas\_user\_idstringOptional

Return only orders for the specified Canvas user ID

completedstringOptional

When set, only return orders that were completed successfully

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific bulk enrollment

/api/v1/order\_items/history/bulk\_enrollments/{id}

200

Getting a specific bulk enrollment

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

fromstringOptional

Only include bulk enrollments from this date

tostringOptional

Only include bulk enrollments to this date

canvas\_user\_idsstringOptional

Only include bulk enrollments for the specified canvas user ids

/api/v1/order\_items/history/bulk\_enrollments

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

pageintegerOptional

Page number for pagination (defaults to 0)

searchstringOptional

Search query to filter account admins

per\_pagestringOptional

Number of results per page

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

canvas\_user\_idstringRequired

email\_addressstringRequired

Email address of the user

account\_idsstringRequired

Array of account IDs to associate with the user

201

Creating an account admin association

201

Creating an account admin association

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idintegerRequired

204

Deleting a specific account admin association

/api/v1/account\_admins/{id}/accounts/{account\_id}

204

Deleting a specific account admin association

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

204

Deleting all account admin associations

/api/v1/account\_admins/{id}

204

Deleting all account admin associations

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific user registration

/api/v1/user\_registrations/{id}

200

Getting a specific user registration

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

fromstringOptional

Earliest date/time to return (optional, String). Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

tostringOptional

Latest date/time to return (optional, String). See 'from' above for format.

200

Listing user registrations

/api/v1/user\_registrations

200

Listing user registrations

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

emailstringOptional

E-mail address (will also serve as login)

catalog\_idstringOptional

ID of subcatalog to associate with user (optional)

custom\_fieldsstringOptional

Hash of custom field values, e.g. { 'phone': '867-5309' } (optional)

/api/v1/user\_registrations

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

product\_actionstringRequired

Action to perform. Possible values: archive, reactivate

product\_idsinteger\[]Required

Array of product ids to perform the action on

200

All programs have been successfully processed

422

Some programs have failed to process successfully

/api/v1/programs/archived

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific program

200

Getting a specific program

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

204

Deleting a specific program

204

Deleting a specific program

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

descriptionstringOptional

listing\_pathstringOptional

is\_enrollablestringOptional

Filter by whether the listing is currently open for enrollment (true/false)

querystringOptional

General search query (title OR description OR tags)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific email domain set

/api/v1/email\_domain\_sets/{id}

200

Getting a specific email domain set

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Updating an email domain set

/api/v1/email\_domain\_sets/{id}

200

Updating an email domain set

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

List promotions by email domain set

/api/v1/email\_domain\_sets/{id}/promotions

200

List promotions by email domain set

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

searchstringOptional

A value to filter the Email Domain Sets by name

exactstringOptional

A boolean to set whether the search should only include results that match exactly

200

Listing email domain sets

/api/v1/email\_domain\_sets

200

Listing email domain sets

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

product\_actionstringRequired

Action to perform. Possible values: archive, reactivate

product\_idsinteger\[]Required

Array of product ids to perform the action on

200

All courses have been successfully processed

422

Some courses have failed to process successfully

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

descriptionstringOptional

listing\_pathstringOptional

is\_enrollablestringOptional

Filter by whether the listing is currently open for enrollment (true/false)

querystringOptional

General search query (title OR description OR tags)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

attachmentstring · binaryRequired

CSV containing a Catalog Course ID and Catalog Course SKU header

/api/v1/courses/update\_skus

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific course

200

Getting a specific course

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

204

Deleting a specific course

204

Deleting a specific course

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idsinteger\[]Optional

product\_idsinteger\[]Optional

product\_statusesstring\[]Optional

List of product statuses (OPEN, CLOSED, and/or DELETED)

creation\_date\_fromstringOptional

creation\_date\_tostringOptional

enrollment\_count\_minintegerOptional

enrollment\_count\_maxintegerOptional

completion\_count\_minintegerOptional

completion\_count\_maxintegerOptional

dropped\_count\_minintegerOptional

dropped\_count\_maxintegerOptional

listing\_price\_minnumberOptional

listing\_price\_maxnumberOptional

promo\_codesstring\[]Optional

List of promotion code states (APPLIED and/or NOT\_APPLIED)

revenue\_minnumberOptional

revenue\_maxnumberOptional

certificate\_offeredbooleanOptional

Certificate offered for the product

200

Getting products analytics

/api/v1/analytics/products

200

Getting products analytics

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idsinteger\[]Optional

product\_idsinteger\[]Optional

product\_statusesstring\[]Optional

List of product statuses (OPEN, CLOSED, and/or DELETED)

student\_idsinteger\[]Optional

List of student ids(catalog user id)

student\_canvas\_user\_idsinteger\[]Optional

List of student ids(canvas user id)

enrollment\_date\_fromstringOptional

enrollment\_date\_tostringOptional

enrollment\_statusesstring\[]Optional

List of enrollment statuses (ACTIVE, COMPLETED, DROPPED and/or CONCLUDED)

completion\_date\_fromstringOptional

completion\_date\_tostringOptional

200

Getting enrollments analytics

/api/v1/analytics/enrollments

200

Getting enrollments analytics

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idsinteger\[]Optional

product\_idsinteger\[]Optional

product\_statusesstring\[]Optional

List of product statuses (OPEN, CLOSED, and/or DELETED)

student\_idsinteger\[]Optional

List of student ids(catalog user id)

student\_canvas\_user\_idsinteger\[]Optional

List of student ids(canvas user id)

purchaser\_idsinteger\[]Optional

List of purchaser ids(catalog user id)

purchaser\_canvas\_user\_idsinteger\[]Optional

List of purchaser ids(canvas user id)

bulk\_purchases\_onlybooleanOptional

purchase\_date\_fromstringOptional

purchase\_date\_tostringOptional

order\_feestring\[]Optional

List of order fee types (FREE and/or PAID)

listing\_price\_minnumberOptional

listing\_price\_maxnumberOptional

promo\_codesstring\[]Optional

List of promotion code states (APPLIED and/or NOT\_APPLIED)

revenue\_minnumberOptional

revenue\_maxnumberOptional

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idsinteger\[]Optional

student\_idsinteger\[]Optional

List of student ids(catalog user id)

student\_canvas\_user\_idsinteger\[]Optional

List of student ids(canvas user id)

enrollment\_count\_minintegerOptional

enrollment\_count\_maxintegerOptional

last\_enrollment\_date\_fromstringOptional

Last enrollment date from

last\_enrollment\_date\_tostringOptional

registration\_date\_fromstringOptional

registration\_date\_tostringOptional

registered\_throughstring\[]Optional

List of registration sources (CANVAS and/or CATALOG)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific catalog

200

Getting a specific catalog

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

only\_certificatesbooleanOptional

Indicates if the courses without certificates should be included, default is to include all courses

200

Listing user's completions with a certificate

/api/v1/completed\_certificates

200

Listing user's completions with a certificate

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

listing\_idstringOptional

Only include enrollments for the specified listing

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

create\_orderstringOptional

Create an order record for this enrollment, defaults to true

send\_emailstringOptional

Send an enrollment email to the user, defaults to true

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific enrollment

200

Getting a specific enrollment

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

namestringRequired

New tag name (minimum 1 and maximum 255 characters)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

idsinteger\[]Required

Array of tag IDs to delete

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

product\_idsstringOptional

List of product ids (maximum 20 ids)

namestringOptional

Search value which will be searched in tag name and associated products names

has\_categorybooleanOptional

updated\_at\_fromstringOptional

updated\_at\_tostringOptional

created\_at\_fromstringOptional

created\_at\_tostringOptional

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

namestringRequired

Tag name (minimum 1 and maximum 255 characters)

product\_idsstringOptional

List of product ids associate to this tag

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

clear\_merged\_into\_user\_idstringOptional

It will clear merged\_into\_user\_id field of user if set to true

custom\_fieldsstringOptional

An object containing custom field values, e.g. { "phone": "867-5309" }. Custom field values must be strings or nulls, anything else will result in a 400 response. If Catalog already has a value for a given key, it will be overwritten, or if the new value is null, it will be deleted. If Catalog does not already have a value for a given key, it will be added. UDFs that are not included in the request will remain unchanged.

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

only\_orders\_and\_enrollmentsstringOptional

Delete only orders and enrollments (user dependencies) except user and related account admins OR delete user dependencies including user and related account admins

200

Deleting a specific user with dependencies

200

Deleting a specific user with dependencies

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

registered\_in\_catalogbooleanOptional

If true, only queries users registered through Catalog. If false, only queries users registered through Canvas. If not specified, queries all users.

canvas\_user\_idintegerOptional

created\_at\_fromstringOptional

Created at from. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

created\_at\_tostringOptional

Created at to. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

updated\_at\_fromstringOptional

Updated at from. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

updated\_at\_tostringOptional

Updated at to. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

email\_addressstringRequired

E-mail address (will also serve as login)

registered\_account\_idstringOptional

ID of subcatalog to associate with user (optional). If not specified, the root account ID used to generate the API key will be registered\_account\_id

custom\_fieldsstringOptional

Hash of custom field values, e.g. { "phone": "867-5309" } (optional)

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific progress

200

Getting a specific progress

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

listing\_idintegerRequired

200

Getting a listing certificate

200

Getting a listing certificate

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

days\_to\_expirestringOptional

Days until the certificate expires after it is awarded. Defaults to null. Must not be present when expires\_at is present.

expires\_atstringOptional

Date of certificate expiration. Defaults to null. Must not be present when days\_to\_expire is present.

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

nullify\_requirements\_completed\_atstringOptional

Should nullify the requirements\_completed\_at for the enrollments, defaults to false

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Revoking users certificate

/api/v1/certificates/revoke\_users\_certificate

200

Revoking users certificate

Last updated 2 months ago