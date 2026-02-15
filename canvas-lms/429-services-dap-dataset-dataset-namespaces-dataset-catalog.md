---
title: catalog | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog
source: sitemap
fetched_at: 2026-02-15T09:12:13.651303-03:00
rendered_js: false
word_count: 4014
summary: This document provides a technical reference for the Canvas Catalog dataset schema, defining the properties and data types for accounts, admins, waitlists, and bulk checkout records.
tags:
    - canvas-catalog
    - database-schema
    - data-reference
    - account-management
    - bulk-checkout
    - instructure-dap
category: reference
---

Catalog account admins.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **canvas\_user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The Canvas identifier of the user.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The unique identifier of an account.
- **name** (str | None) - The name of the admin.
- **email** (str | None) - The email address of the admin.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **root\_account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The root account of the account. The unique identifier of an account.
- **deleted\_at** (datetime | None) - Timestamp of when a record was soft deleted.

Catalog accounts (known as catalogs and sub-catalogs).

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **parent\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The parent account of the account. The unique identifier of an account.
- **name** (str | None) - The name of the account.
- **about** (str | None) - The description of the the account.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **portal\_path** (str | None) - The URL/Path of the account.
- **canvas\_domain** (str | None) - The Canvas URL for the account.
- **type** (str | None) - The type of the account: `DomainAccount`/`PortalAccount`.
- **settings** (str | None) - The JSON representation of the account's settings.
- **canvas\_id** (int64 | None) - The unique identifier of the Canvas account.
- **locale** (str) - The locale setting of the account.
- **text\_overrides** (str | None) - The JSON representation of the text overrides for the account (for example: programs heading).
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **logo\_file\_name** (str | None) - The filename of the account's logo.
- **logo\_content\_type** (str | None) - The content type of the account's logo.
- **logo\_file\_size** (int32 | None) - The file size of the account's logo.
- **logo\_updated\_at** (datetime | None) - Timestamp of when the account's logo updated.
- **favicon\_file\_name** (str | None) - The filename of the account's favicon.
- **favicon\_content\_type** (str | None) - The content type of the account's favicon.
- **favicon\_file\_size** (int32 | None) - The file size of the account's favicon.
- **favicon\_updated\_at** (datetime | None) - Timestamp of when the account's favicon updated.
- **header\_image\_file\_name** (str | None) - The filename of the account's header image.
- **header\_image\_content\_type** (str | None) - The content type of the account's header image.
- **header\_image\_file\_size** (int32 | None) - The file size of the account's header image.
- **header\_image\_updated\_at** (datetime | None) - Timestamp of when the account's header image updated.
- **canvas\_account\_uuid** (str | None) - The UUID of the Canvas account.
- **alias\_path** (str | None) - Alias path the account.

Applicants for a product's wait list.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The unique identifier of a product.
- **name** (str | None) - The name of the applicant.
- **email** (str | None) - The email address of the applicant.
- **canvas\_user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The identifier of the Canvas user.
- **notified\_of\_opening\_at** (datetime | None) - Timestamp when the applicant was notified about getting in for the product.
- **status** (str | None) - The status of the application.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **token** (str | None) - The token for identifying an applicant (used when the user wants leave the wait list).
- **activated** (bool | None) - Indicates whether the user for the applicant is activated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.

Promotions applied in a bulk checkout transaction.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **bulk\_checkout\_id** (int64 | None) - The unique identifier for a record.
- **promotion\_id** ([promotions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.promotions) | None) - The promotion. The unique identifier of a promotion.
- **discount** (Decimal | None) - The amount of the promotion discount in the bulk checkout.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.

Bulk checkout transactions.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **canvas\_user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The Canvas identifier of the user.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The product of the bulk checkout. The unique identifier of a product.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The account of the bulk checkout. The unique identifier of an account.
- **order\_id** ([orders](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.orders) | None) - The order of the bulk checkout. The unique identifier of an order.
- **seats** (int32 | None) - Indicates how many seats purchased.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **checkout\_time** (datetime | None) - Timestamp of the bulk checkout.

Invitations that applied in a bulk checkout.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **order\_item\_id** ([order\_items](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.order_items) | None) - The order item for the invitation. The unique identifier of an order item.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The product for the invitation. The unique identifier of a product.
- **email** (str | None) - Email where the invitation sent.
- **code** (str | None) - Code for the invitation.
- **status** (str | None) - Status of the invitation.
- **invited\_at** (datetime | None) - Timestamp when the invitation sent.
- **revoked\_at** (datetime | None) - Timestamp when the invitation revoked.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **enrollment\_id** ([enrollments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.enrollments) | None) - The enrollment for the invitation. The unique identifier of an enrollment.

Promotions applied in a shopping cart transaction.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **cart\_item\_id** ([cart\_items](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.cart_items) | None) - The cart item. The unique identifier of a cart item.
- **promotion\_id** ([promotions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.promotions) | None) - The promotion. The unique identifier of a promotion.
- **discount** (Decimal | None) - The amount of the promotion discount in the cart.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.

Items in a shopping cart transaction.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **cart\_id** ([carts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.carts) | None) - The cart for the item. The unique identifier of a cart.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The product for the cart. The unique identifier of a product.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.

Represents a shopping cart transaction until the checkout.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The account for the cart. The unique identifier of an account.
- **canvas\_user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The Canvas identifier of the user.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **order\_id** ([orders](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.orders) | None) - The order for the cart. The unique identifier of an order.
- **checkout\_time** (datetime | None) - Timestamp of the cart checkout.
- **root\_account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The root account for the cart. The unique identifier of an account.

Used to populate the list of filtering options for a given catalog. Basically a group for a given account or a tag.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - Unique identifier of the account this category belongs to.
- **group\_id** (int32 | None) - Unique identifier of the account or tag this category belongs to.
- **group\_type** (str | None) - The type of the group this category belongs to. Can be "Account" or "Tag".
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was last updated.

Templates for certificates.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The account for the certificate template. The unique identifier of an account.
- **name** (str | None) - Name of the template.
- **template** (str | None) - Template String (not a YAML, regular Template String).
- **pdf\_settings** (str | None) - Settings JSON for the generated PDF (for example, orientation).
- **code** (str | None) - Code of the template.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.

Certificate that can be awarded for completing a product.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - Product for the certificate. The unique identifier of a product.
- **name** (str | None) - Name of the certificate.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **old\_template** (str | None) - Leftover data that was used before the certificate\_templates. Backward compatibility.
- **old\_pdf\_settings** (str | None) - Leftover data that was used before the certificate\_templates. Backward compatibility.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **certificate\_template\_id** ([certificate\_templates](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.certificate_templates) | None) - The template for the certificate. The unique identifier of a certificate template.
- **active** (bool) - Indicates whether the certificate active or not.
- **custom\_template\_id** ([certificate\_templates](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.certificate_templates) | None) - The custom template for the certificate. The unique identifier of a certificate template.
- **days\_to\_expire** (int32 | None) - Expiration time for the certificate.
- **expires\_at** (datetime | None) - Expiration date for the certificate.

Customized emails.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts)) - The account of the email. The unique identifier of an account.
- **email\_type** (str) - Type of the email.
- **draft** (str | None) - JSON of the draft version.
- **published** (str | None) - JSON of the published version.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **created\_by** (str) - Name of the creator.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **updated\_by** (str) - Name of the user who updated the custom email.
- **published\_at** (datetime | None) - Timestamp of the publication.
- **published\_by** (str | None) - Name of the publisher.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.

Email layouts.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The account of the layout. The unique identifier of an account.
- **header** (str | None) - Header of the email layout.
- **footer** (str | None) - Footer of the email layout.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.

Enrollment for a product (course or program).

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **canvas\_user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The Canvas identifier of the user.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - Product for the enrollment. The unique identifier of a product.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **root\_program\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - Product for the enrollment. The unique identifier of a product.
- **requirements\_completed\_at** (datetime | None) - Completion time for the requirements.
- **ends\_at** (datetime | None) - End time for the enrollment.
- **external\_id** ([canvas.enrollments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.enrollments) | None) - External identifier for an enrollment (for example canvas course id).
- **status** (str) - Status of the enrollment: active, dropped, concluded.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **last\_sync\_error** (str | None) - The error of the last synchronization, if applicable.
- **order\_item\_id** ([order\_items](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.order_items) | None) - Order item of the enrollment. The unique identifier of an order item.

Promotions that has been applied on an order.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **order\_item\_id** ([order\_items](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.order_items) | None) - The unique identifier of an order item.
- **promotion\_id** ([promotions](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.promotions) | None) - The unique identifier of an promotion.
- **discount** (Decimal | None) - Amount of discount which is applied to the product in the order.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.

Order item for a product.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **order\_id** ([orders](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.orders) | None) - The unique identifier of an order.
- **item\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The unique identifier of a product.
- **amount** (Decimal | None) - Product quantity price.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was soft deleted.
- **discounted\_amount** (Decimal | None) - Product quantity price with discounts.
- **quantity** (int32) - Product quantity.
- **unit\_price** (Decimal | None) - Single product price.

Order for a product.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The unique identifier of an account.
- **canvas\_user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The Canvas identifier of the user.
- **email** (str | None) - Email of the user for the order.
- **name** (str | None) - Name of the user for the order.
- **total** (Decimal | None) - Total price of the order.
- **currency** (str | None) - Currency of the order.
- **purchased\_at** (datetime | None) - Timestamp of when an order was purchased.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **full\_id** (str | None) - Full id of the order with account order id prefix.
- **deleted\_at** (datetime | None) - Timestamp of when a record was soft deleted.
- **source** (str | None) - Source from which order was created.
- **user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.users) | None) - The unique identifier of an user.

Payment information for an order.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **order\_id** ([orders](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.orders) | None) - The order of the payment. The unique identifier of an order.
- **reference\_id** (str | None) - Reference identifier used to find payment.
- **amount** (Decimal | None) - The amount of money paid.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **status** (str | None) - Status of the payment.
- **purchase\_params** (str | None) - Purchase parameters from the Payment Redirector for the payment.
- **deleted\_at** (datetime | None) - Timestamp of when a record was created.

Images for a product.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The product for the image The unique identifier of an order.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **image\_file\_name** (str | None) - The file name of the image.
- **image\_content\_type** (str | None) - The content type of the image.
- **image\_file\_size** (int32 | None) - The file size of the image.
- **image\_updated\_at** (datetime | None) - Timestamp of when the image updated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.

Associative table between products and tags.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The unique identifier of a product.
- **tag\_id** ([tags](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.tags) | None) - The unique identifier of a tag.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was soft updated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was soft deleted.

A product that can be a course or a program. A program contains multiple courses or programs.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **visibility** (str | None) - Visibility of the product.
- **enrollment\_open** (bool) - Indicates whether the enrollment is open for the product.
- **title** (str | None) - Title of the product.
- **start\_date** (datetime | None) - Start time of the product.
- **end\_date** (datetime | None) - End time of the product.
- **description** (str | None) - Description of the product.
- **enrollment\_fee** (Decimal) - Price of the product.
- **canvas\_course\_id** ([canvas.courses](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.courses) | None) - Course identifier of the Catalog course in the Canvas account.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **path** (str | None) - Portal path for the product.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The account for the product. The unique identifier of an account.
- **list\_order** (int32 | None) - Order number in the product list (for custom product ordering).
- **type** (str | None) - Type of the product.
- **teaser** (str | None) - Teaser of the product.
- **owner\_id** (int32 | None) - Who is offering the course/program (may be different than account).
- **canvas\_section\_id** (int64 | None) - Id of the section for the Catalog course in the Canvas account.
- **sequential** (bool) - Indicates whether the program is sequential (courses should be completed in order).
- **days\_to\_complete** (int32 | None) - Days to complete the product.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **enrollment\_cap** (int32 | None) - Enrollment cap for the product.
- **waitlist** (bool) - Indicates whether wait-list is available for the product.
- **credits** (Decimal | None) - Credit number for the product.
- **waitlist\_cap** (int32 | None) - Wait-list cap for the product.
- **sku** (str | None) - SKU of a product.
- **show\_free\_banner** (bool) - Option to remove the free banner from product.
- **image\_alt\_text** (str | None) - Alt text for the product's image.
- **external\_redirect\_url** (str | None) - External redirect URL for the product (after enrollment a logged in user will be redirected here).
- **allowed\_payment\_types** (str) - Allowed payment types for the product (can be `standard` or `purchase_order`).
- **workflow\_state** (str) - Workflow state of the product.
- **workflow\_state\_timestamp** (datetime) - Timestamp when the workflow state changed.
- **detail\_code** (str | None) - Detail code of the product.
- **bulk\_purchase\_disabled** (bool) - Bulk purchase enabled or disabled for the product.
- **enrollment\_open\_from** (datetime | None) - The start of the product's enrollment period.
- **enrollment\_open\_to** (datetime | None) - The end of the product's enrollment period.

Requirements of a program to complete. It can have a number of courses / programs as requirements.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **program\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The program that has a requirement. The unique identifier of a program.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The product that the program has as a requirement. The unique identifier of a product.
- **sequence** (int32 | None) - Sequence number of this requirement (scoped to program id).
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.

Promotions that can be applied on order.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The unique identifier of an account.
- **product\_id** ([products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products) | None) - The unique identifier of a product.
- **amount** (Decimal | None) - The amount of discount the promotion gives.
- **discount\_type** (str | None) - Type of the promotion discount, Can be: `flat`, `percent`.
- **code** (str | None) - The code of the promotion.
- **name** (str | None) - The name of the promotion.
- **description** (str | None) - The description of this promotion.
- **active** (bool) - Indicates whether the promotion is active.
- **start\_date** (datetime | None) - Timestamp of when the promotion will start working.
- **end\_date** (datetime | None) - Timestamp of when the promotion will cease working.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was last updated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was soft deleted.
- **usage\_type** (str) - Usage type of the promotion code. Can be: once-per-user, unlimited.

A tag for filtering products.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The unique identifier of an account.
- **name** (str | None) - The name of the tag.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was last updated.
- **deleted\_at** (datetime | None) - Timestamp of when a record was soft deleted.

A theme belonging to an account or product.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **name** (str | None) - The name of the theme.
- **css\_content** (str | None) - The content of the CSS file.
- **themeable\_type** (str | None) - The type of theme-able where the theme belongs.
- **themeable\_id** (None | [accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | [products](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.products)) - The account or product that the theme belongs to. The unique identifier of an account or product.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **js\_content** (str | None) - The content of the Javascript file.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **js\_file\_name** (str | None) - The name of the Javascript file.
- **js\_content\_type** (str | None) - The content type of the Javascript file.
- **js\_file\_size** (int32 | None) - The size of the Javascript file.
- **js\_updated\_at** (datetime | None) - Timestamp of when the Javascript file updated.
- **css\_file\_name** (str | None) - The name of the CSS file.
- **css\_content\_type** (str | None) - The type of the CSS file.
- **css\_file\_size** (int32 | None) - The size of the CSS file.
- **css\_updated\_at** (datetime | None) - Timestamp when the CSS file updated.

Custom fields for the user to submit at registration.

**Properties:**

- **id** (int32) - `primary key` The unique identifier for a record.
- **name** (str | None) - The name of the field.
- **label** (str | None) - The label of the field.
- **field\_type** (str) - The type of the field.
- **required** (bool) - Indicates whether the user defined field is required.
- **required\_message** (str | None) - The required message for the field.
- **account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The account where the user registered. The unique identifier of an account.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **list\_order** (int32 | None) - The order number for the field.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.
- **hide\_in\_user\_workflow** (bool) - Indicates whether the user defined field should be hidden in user workflow or not.

Users of the Catalog's (sub)account.

**Properties:**

- **id** (int64) - `primary key` The unique identifier for a record.
- **root\_account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts)) - The root account of the account where the user registered. The unique identifier of an account.
- **canvas\_user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users)) - The Canvas identifier of the user.
- **registered\_account\_id** ([accounts](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.accounts) | None) - The account where the user registered. The unique identifier of an account.
- **user\_name** (str | None) - The name of the user.
- **email\_address** (str | None) - The email address of the user.
- **custom\_fields** (str) - Timestamp of when a record was updated.
- **created\_at** (datetime) - Timestamp of when a record was created.
- **updated\_at** (datetime) - Timestamp of when a record was updated.
- **time\_zone** (str | None) - The time zone setting of the user.
- **merged\_into\_user\_id** ([users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-catalog#dap_schemas.catalog.users) | None) - The user where the user merged into. The unique identifier of an user.
- **deleted\_at** (datetime | None) - Timestamp of when a record was deleted.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).