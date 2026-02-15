---
title: Filtering Using ODATA Like Statements | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters
source: sitemap
fetched_at: 2026-02-15T09:04:26.968888-03:00
rendered_js: false
word_count: 1041
summary: This document explains how to implement filtering in AB Connect API requests using specific query parameters and logical operators. It details the construction of atomic and complex filter statements, including support for boolean logic and advanced text search functionality.
tags:
    - ab-connect
    - api-filtering
    - query-syntax
    - logical-operators
    - text-search
    - url-parameters
category: guide
---

The main directive for filtering entities in AB Connect is the inclusion of the `filter` parameter in the URL query. This document outlines how to use filtering with AB Connect. Examples are given with different endpoints and objects but the general principles are independent of the object type or endpoint. In any case, the filter limits the results that are returned or updated by the request.

At its simplest, the filtering utilizes the following syntax:

```
`<endpoint URI>?filter[<object of filter>]=<URL encoded filter statement>`
```

E.g. the following URL retrieves alignable 5th grade math Standards from Kentucky.

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?filter[standards]=(disciplines.subjects.code%20eq%20%27MATH%27%20and%20education_levels.grades.code%20eq%20%275%27%20and%20document.publication.authorities.descr%20eq%20%27Kentucky%20DOE%27%20and%20utilizations.type%20eq%20%27alignable%27)`
```

That's a bit messy so let's break it down. The first part is the primary resource endpoint.

```
`https://api.abconnect.instructure.com/rest/v4.1/standards`
```

The next bit is the filter parameter. The square brackets contain the type of object being filtered. In this case, we are limiting the Standards being returned.

The value of the filter argument is the URL encoded filter string.

```
`(disciplines.subjects.code%20eq%20%27MATH%27%20and%20education_levels.grades.code%20eq%20%275%27%20and%20document.publication.authorities.descr%20eq%20%27Kentucky%20DOE%27%20and%20utilizations.type%20eq%20%27alignable%27)`
```

Let's decode it to make it readable:

```
`(disciplines.subjects.code eq 'MATH' and education_levels.grades.code eq '5' and document.publication.authorities.descr eq 'Kentucky DOE' and utilizations.type eq 'alignable')`
```

That makes it a little more readable and clarifies the intent. The specifics of the field names aren't critical here. See the endpoint specific documentation for an explanation of each field.

## Constructing the Filter Statement

At an atomic level, the most common filter statement appears like `<property> <comparator> '<value>'` but some functions are also supported (e.g. `isempty(<property>)`).

A `<property>` would be any attribute of the object being filtered. Examples of a property for a Standard would be `level` or `status`. Alternatively, a property can be the attribute of a complex property. E.g. for a Standard, `<property>` could also be `number.raw` or `disciplines.subjects.code`.

A `<value>` could be any value appropriate for the property in question. Values are delimited with single quotes.

Together, various operators, properties and values combine to build a logical statements. The following operators are supported by AB Connect in order of decreasing precedence by group.

Function call. E.g. `isempty(concepts)` or `query('triangle pythagorean theorem')` - see below for details)

Logical negation. E.g. `not propertyX in ('a', 'b, 'c')`

Equals. E.g. `propertyX eq 'apple'`

Not equals. E.g. `propertyX ne 'fruit'`

Greater than. E.g. `propertyX gt 5`

Greater than or equal to. E.g. `propertyX ge 5`

Less than. E.g. `propertyX lt 5`

Less than or equal to. E.g. `propertyX le 5`

The value of the specified property is in the supplied list of values. E.g. `propertyX in ('value1', 'value2', 'value3')`

Combine two conditions and return true if both are true, otherwise false. E.g. `propertyX eq 5 and propertyY ne 'A'`

Combine two conditions and return true if either are true, otherwise false. E.g. `propertyX eq 5 or propertyY ne 'A'`

- Inequality operators can be used with date, number and text attributes but the results vary by attribute type. Date attributes filter chronologically. Number attributes filter numerically. Text attributes filter alphabetically.
- Custom attributes can be defined as text or numbers. If you aren't sure of the types for your custom attributes, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) for guidance.
- It is possible to create custom attributes with the same name and different data types in different asset types (or when searching across multiple owners). The treatment of inequalities filtering across multiple data types is deterministic but relatively complex and isn't covered here. Where possible, we recommend you avoid this situation by ensuring your custom attributes don't have name conflicts across data types where possible. For details on the way AB Connect handles filtering across mixed types, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29).

## Building Complex Statements

AB Connect also supports Boolean operations to combine atomic filter statements into complex statements. You can also use parentheses to group statements together.

- `disciplines.subjects.code eq 'MATH' and education_levels.grades.code eq '5'` 5th grade math
- `document.publication.authorities.descr eq 'Kentucky DOE' and not disciplines.subjects.code eq 'MATH'` Standards from Kentucky not related to math
- `(disciplines.subjects.code eq 'MATH' and education_levels.grades.code eq '5') or (disciplines.subjects.code eq 'ELA' and education_levels.grades.code eq '7')` 5th grade math and 7th grade language arts Standards

One of the major improvements in AB Connect is the text filtering. The text filter is robust, will return results ordered by relevance and includes soft matches like partial matches. The format for text filtering is unique and utilizes a function style notation. There are two formats.

### Filtering a Specific Field

When filtering a particular field, include the field name as well as the value you are filtering for: `query(<field>, <string>)`. For example, to filter for Standards that contain the words "adding" and "fractions" in their statement, the filter would look like:

```
`filter[standards]=(query(statement.descr, 'adding fractions'))`
```

Note that the text filter is a very soft filter and will often return more Standards than you would expect. The results will be ordered by relevance so the top responses are usually the most important. For example, in the query statement above, the system would return Standards that contain the words "adding fractions" first, followed by Standards that contain "adding" or "fractions". It will also return Standards that contain "add", "addition", etc.

To be more specific, break phrases up into separate statements and be explicit about the Boolean operations to join the queries. The following will only return Standards if they contain both "fractions" and some form of derivation of the word "adding".

```
`filter[standards]=(query(statement.descr, 'fractions') and query(statement.descr, 'adding'))`
```

### Filtering Across Multiple Text Fields

To retrieve Standards that have the keywords in any general text field, remove the field name from the query statement: `query(<string>)`. E.g.

```
`filter[standards]=(query('adding fractions'))`
```

When using this approach, the system will search any fields it considers to be a text field. The specific fields vary by endpoint:

- Standards:
  
  - `statement.addendums.descr`

## Filtering by Number in Standards

In Standards documents, numbers are often separated, delimited or decorated with symbols (e.g. "24.B (i)"). Trying to ensure users are typing the numbers EXACTLY as they are entered in the Standards document is difficult. For this reason, AB Connect supports a soft match on the Standards' `number.raw`, `number.enhanced`, `number.prefix_enhanced`, `number.alternate` and `number.root_enhanced` fields when the query function is used. It treats any separator between alphanumeric values as a break between numbers and looks for Standards that match numbers returning results by how closely they match the results. In the example listed earlier, it will return Standards that have numbers that contain 24, B AND i first without regards to the separators used in the filter. It will follow that with Standards that contain two of the three, then Standards that contain any one of the numbers. Filtering for "24.B.i" will return the same results in the same order as filtering for "24-b-i" and "24.B (i)".

In ODATA, literal strings are quoted using single quotes ('). To include a single quote in a string literal in the filter, use a backslash to escape it ('). For example, to search for the word "don't" in Standards, you would use the following filter:

```
`filter[standards]=(query('don\'t'))`
```

## Checking for Empty Properties

Sometimes it is handy to search for properties that are empty. What "empty" means depends on the property type so AB Connect has an `isempty` function that will match true on objects with no properties, arrays with no elements and scalar properties with null values. For example, the following filter will return all assets that are missing a subject.

```
`filter[assets]=isempty(disciplines.subjects)`
```

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).