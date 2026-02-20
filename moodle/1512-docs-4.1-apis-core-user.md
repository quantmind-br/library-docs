---
title: User-related APIs | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/apis/core/user
source: sitemap
fetched_at: 2026-02-17T14:55:01.683544-03:00
rendered_js: false
word_count: 881
summary: This document outlines the miscellaneous APIs in Moodle for handling user lists, specifically focusing on user field display, validation, sanitization, and UI selection components.
tags:
    - moodle-development
    - user-api
    - data-validation
    - data-cleaning
    - user-fields
    - user-selector
category: api
---

This is a collection of miscellaneous APIs that can help with doing things with lists of users.

## User field display[​](#user-field-display "Direct link to User field display")

The [User fields](https://docs.moodle.org/dev/User_fields) class is mainly used when displaying tables of data about users. It indicates which extra fields (e.g. email) should be displayed in the current context based on the permissions of the current user. It also provides ways to get the necessary data from a query, and to obtain other generally-useful fields for user names and pictures.

## User fields definition[​](#user-fields-definition "Direct link to User fields definition")

To guarantee the sanity of the data inserted into Moodle and avoid security bugs, new user fields definition methods have been created for use in Moodle 3.1 onwards. The purpose of these new methods is to create a central point of user fields data validation and guarantee all data inserted into Moodle will be cleaned against the correct parameter type. Another goal of this new API is to create consistency across Moodle core and avoid different parameter validations for the same user fields. For now on, user data must validate against the user field, not using clean\_param() directly.

### `$propertiescache`[​](#propertiescache "Direct link to propertiescache")

Cached information of each user field and its attributes filled by the fill\_properties\_cache.

### `fill_properties_cache()`[​](#fill_properties_cache "Direct link to fill_properties_cache")

The main method of the user definition is to keep the definition of each user field and its properties. It verifies if the **`core_user::$propertiescache`** is already filled and caches all user fields attributes into this same attribute. Each field matches the exact field name on the user table. That said, every new field added to the user table should be added to fill\_properties\_cache $fields array, otherwise it won't be validated or cleaned. Each field has four possible properties, being choices and default optional:

- **`null`** - Whether the field is NULL or NOT\_NULL, it SHOULD NOT be used as form validation, as many fields in the user table have NOT\_NULL property but have the default value as (\`\`).
- **`type`** - The expected parameter type (PARAM\_\*) to be used as validation and sanitizing.
- **`choices`** - A list of accepted values of that field. For example the list of the available countries, timezones, calendar type etc.
- **`default`** - The default value in case the user field didn't pass the validation or cleaned and we must set the default value. For example if the user country is invalid and it is not in the list of choices, set $CFG-&gt;country.

### `validate()`[​](#validate "Direct link to validate")

A static method to validate user fields, accepts an array or the user object as parameter, validate each parameter individually and can return true if all user data is correct or an array of validation errors. The purpose of this method is to just validate the user data, it won't do any cleaning of the data.

### `clean_data()`[​](#clean_data "Direct link to clean_data")

A static method that has the purpose of clean the user data and return the same user array/object. It receives an array with user data or a user object as parameter and it checks if the data is in the list of choices and if the property has a default value and clean the data if the user object doesn't have a choices property. It will display a debugging message if one the operations above has problems.

### `clean_field()`[​](#clean_field "Direct link to clean_field")

A static method to clean a single user field. It has two parameters, the data to be cleaned and its user field. The behaviour of the method is similar to the clean\_data. It will do the validations and cleaning and can display a debug message if an error has been found. It returns the cleaned data.

### `get_property_type()`[​](#get_property_type "Direct link to get_property_type")

A helper method to get the type of the property. It receives the user field name as parameter and if it doesn't exist will throw an exception. If the property has been found, it will return its type.

### `get_property_null()`[​](#get_property_null "Direct link to get_property_null")

A helper method to get the null property of the user field. It receives the user field name as parameter and if it doesn't exist it throws an exception. If the property has been found, it will return the null value.

### `get_property_choices()`[​](#get_property_choices "Direct link to get_property_choices")

A helper method to get the list of choices of a user field. It receives the user field name as parameter and if it doesn't exist will throw an exception. If the property has been found, it will return the list of accepted values.

### `get_property_default()`[​](#get_property_default "Direct link to get_property_default")

A helper method to get the default value of a property. It receives the user field name as parameter and if it doesn't exist or if it doesn't have a default attribute will throw an exception. If the property has been found, it will return its default value.

## User selector[​](#user-selector "Direct link to User selector")

The base class `user_selector_base` defined in `user/selector/lib.php`, which you can subclass to make a widget that lets you select users in an AJAX-y way. It is used, for example, on the Add group members page. The best way to learn how to use it is to search the code for other users, and see how they work. The base class also has good PHPdoc comments.

## Sorting lists of users[​](#sorting-lists-of-users "Direct link to Sorting lists of users")

When you fetch a list of users from the database, they should always be sorted consistently, by using the `users_order_by_sql` function to generate the order-by clause. Again, the best way to see how that works is to search the code for existing uses.

## See also[​](#see-also "Direct link to See also")

- [Core APIs](https://moodledev.io/docs/4.1/apis)
- [Access API](https://moodledev.io/docs/4.1/apis/subsystems/access)
- [Groups API](https://moodledev.io/docs/4.1/apis/subsystems/group)
- [Enrolment API](https://moodledev.io/docs/4.1/apis/subsystems/enrol)