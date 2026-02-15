---
title: Catalogs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/catalogs
source: sitemap
fetched_at: 2026-02-15T09:10:39.267938-03:00
rendered_js: false
word_count: 0
summary: This document defines the data structure and schema for an account object, detailing its configuration settings, registration parameters, and user-defined fields.
tags:
    - canvas-catalog
    - account-settings
    - json-schema
    - api-resource
    - user-defined-fields
category: reference
---

```
{
  "account": {
    "id": 45,
    "name": "Domain Account 46",
    "parent": null,
    "created_at": "2024/01/01 00:00:00 +0000",
    "updated_at": "2024/01/01 00:00:00 +0000",
    "canvas_domain": "www.canvas-domain-46.com",
    "canvas_id": 46,
    "settings": {
      "privacy_policy_url": "https://www.instructure.com/policies/privacy/",
      "terms_url": "https://www.instructure.com/policies/acceptable-use",
      "currency": "USD",
      "supported_payment_types": "standard",
      "time_zone": null,
      "country": "US",
      "measurement": "credit",
      "email_from_name": "Canvas Catalog",
      "email_from_address": "notifications@instructure.com",
      "allow_user_registration": true,
      "title_tag": null,
      "meta_description": null,
      "custom_head_content": null,
      "custom_body_content": null,
      "show_listings_in_parent": true,
      "order_id_prefix": null,
      "inherit_categories": false,
      "inherit_user_defined_fields": false,
      "beta_canvas_domain": null,
      "skus_enabled": false,
      "canvas_enrollment_events": false,
      "include_noncatalog_courses_in_dashboard": true,
      "external_idp_logout_workflow": false,
      "private_catalog": false,
      "bulk_purchase_disabled": false,
      "enroll_button_behavior": "cart",
      "shopping_cart_enabled": true,
      "external_registration_url": null,
      "external_registration_public_key": null,
      "redirect_external_registration_condition": "authenticated",
      "include_captcha": false,
      "user_registration_domain_restriction_type": "inherit",
      "user_registration_domain_deny_list": "",
      "user_registration_domain_allow_list": "",
      "restrict_enrollment_to_user_registration_domain": false,
      "frame_ancestors": "",
      "email_reply_to": "",
      "has_sso_warning": false,
      "measurement_id": null,
      "redirect_non_admins_to_root_url": false,
      "canvas_feature_send_usage_metrics": false,
      "disable_passive_login": false,
      "new_storefront": false,
      "tags_permission_default_value": true,
      "cross_listing_permission_default_value": false,
      "inherit_storefront_theme": false,
      "canvas_authentication_provider_id": "CANVAS_FIRST",
      "udf_collection_level": "registration",
      "disable_drop_course_button": false,
      "google_tag_manager_id": null,
      "linkedin_partner_id": null,
      "enable_credentials": false,
      "enable_impact": false,
      "enable_pathways": false,
      "hide_missing_pathway": false,
      "storefront_product_recommendation_behavior": "popular",
      "storefront_product_recommendation_count": 4,
      "enable_recommendations": false,
      "product_page_recommendation_fallback": "no_fallback",
      "product_page_recommendation_count": 4,
      "enable_recommendations_for_product_page": false,
      "hide_self_paced_label": false,
      "login_auth_providers": "[]",
      "multiple_promo_codes_enabled": true,
      "custom_instructor_label": null,
      "custom_instructor_label_plural": null,
      "purchase_seats_for_others_enabled": true
    },
    "user_defined_fields": [
      {
        "list_order": 0,
        "name": "favorite_color",
        "label": "Favorite Color",
        "field_type": "text",
        "required": false,
        "required_message": "Favorite Color is required",
        "metadata": {},
        "hide_in_user_workflow": true
      },
      {
        "list_order": 1,
        "name": "code_of_conduct",
        "label": "Code of Conduct",
        "field_type": "checkbox",
        "required": true,
        "required_message": "You must accept the Code of Conduct.",
        "metadata": {},
        "hide_in_user_workflow": false
      },
      {
        "list_order": 2,
        "name": "age",
        "label": "Age",
        "field_type": "text",
        "required": true,
        "required_message": "You must provide an Age.",
        "metadata": {},
        "hide_in_user_workflow": false
      },
      {
        "list_order": 3,
        "name": "yes_no",
        "label": "Yes or No",
        "field_type": "select",
        "required": false,
        "required_message": "Yes or No is required",
        "metadata": {
          "options": [
            "Yes",
            "No"
          ]
        },
        "hide_in_user_workflow": false
      }
    ],
    "logo": "https://test-bucket.s3.amazonaws.com/production/logos/9c8da68dc6e957c9ffd0b1f8f95b1e4d6a86fcb0.jpeg",
    "locale": "en",
    "url": "https://www.my-catalog.edu",
    "measurement": "credit",
    "storefront_theme_id": null
  }
}
```