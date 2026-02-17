---
title: Parameters | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/subsystems/routing/parameters
source: sitemap
fetched_at: 2026-02-17T15:28:09.264936-03:00
rendered_js: false
word_count: 1347
summary: This document explains how to define and handle path, query, and header parameters within the routing subsystem using PHP attributes and parameter classes.
tags:
    - routing
    - path-parameters
    - query-parameters
    - header-parameters
    - parameter-validation
    - php-attributes
category: guide
---

The Routing subsystem supports three types of parameter to a request:

- Path parameters
- Query parameters
- Header key/value pairs

Parameters are specified with a `name`, and a parameter `type` which is used to validate the input before passing it to the routed method. All types are cases of the `\core\param` enum, for example `\core\param::TEXT`.

Parameters also support optional features including:

- a description specified in the `description` property;
- allowing a field to be marked as required via the boolean `required` property;
- allowing an optional field to provide a default value using the `default` property;
- allowing a field to be deprecated via the boolean `deprected` property; and
- the specification of examples by specifying an array in the `examples` property.

## Path parameters[​](#path-parameters "Direct link to Path parameters")

When defining the path in a route, it is possible to specify parts of the URI as variables using placeholders. These are known as path parameters. Each path parameter must be appropriately described in the `pathtypes` array property of the route attribute using instances of `\core\router\schema\parameters\path_parameter`.

In the following example a `username` parameter is described in the path, and described further in the `pathtypes` array:

Defining a basic path parameter

```
namespacecore\route\api;

usecore\param;
usecore\router\route;
usecore\router\schema\parameters\path_parameter;

classexample{
#[route(
path:'/users/{username}',
pathtypes:[
newpath_parameter(
name:'username',
type:param::ALPHANUM,
),
],
)]
publicfunctionget_user_information(
string$username,
):ResponseInterface{
// ...
}
}
```

When a user accesses the URI the name will be validated using the `\core\param::ALPHANUM` type specified in the `path_parameter` constructor, and provided to the method.

### Retrieving parameter values[​](#retrieving-parameter-values "Direct link to Retrieving parameter values")

Path parameters can be retrieved from the request in two ways:

- by specifying an `array $args` parameter on the method; or
- by naming the individual parameters you wish to access.

Fetching parameters

```
namespacecore\route\api;

usecore\param;
usecore\router\route;
usecore\router\schema\parameters\path_parameter;

classexample{
#[route(
path:'/users/{username}',
pathtypes:[
newpath_parameter(
name:'username',
type:param::ALPHANUM,
),
],
)]
publicfunctionget_user_information(
string$username,
array$args,
):ResponseInterface{
// ...
$args['username']===$username;
}
}
```

### Optional path parameters[​](#optional-path-parameters "Direct link to Optional path parameters")

Path parameters can be made optional by wrapping them in `[]` braces in the path definition, for example:

An optional parameter in the path

```
path:'/users[/{username}]',
```

The full usage of this is therefore:

Defining an optional path parameter

```
#[route(
path:'/users[/{username}]',
pathtypes:[
newpath_parameter(
name:'username',
type:param::TEXT,
),
],
)]
```

This creates *two* routes:

- `/path/to/route/users`
- `/path/to/route/users/{username}`

If the username is not specified then its value will default to `null` or the supplied default.

note

If fetching the value using a named method parameter, and the default is `null`, then the optional parameter must be nullable, for example:

```
publicfunctionget_user_information(
?string$name,
):ResponseInterface{
// ...
}
```

#### Multiple optional parameters[​](#multiple-optional-parameters "Direct link to Multiple optional parameters")

In some cases it is necessary to capture multiple optional parameters. This can be achieved by adding them within the optional path braces, for example:

Defining multiple optional path parameters

```
#[route(
path:'/users[/{name}/[{pet}]]',
pathtypes:[
newpath_parameter(
name:'name',
type:param::TEXT,
),
newpath_parameter(
name:'pet',
type:param::TEXT,
),
],
)]
publicfunctionget_user_information(
?string$name,
?string$pet,
):ResponseInterface{
// ...
}
```

warning

All parameters after the first optional parameter are considered to be optional. The following is an example of an invalid path:

An example of incorrect behaviour

```
#[route(
path:'/users[/{name}]/example'
)]
```

#### Default values[​](#default-values "Direct link to Default values")

The default value for an unspecified optional parameter is `null`, but an alternative default can be provided by defining the `default` property in the `path_parameter` constructor, for example:

Specifying a default value for an optional path parameter

```
#[route(
path:'/users[/{name}/]',
pathtypes:[
newpath_parameter(
name:'name',
type:param::TEXT,
default:'dave',
),
],
)]
```

note

Optional parameters cannot be set on a required parameter.

## Query parameters[​](#query-parameters "Direct link to Query parameters")

Query parameters are similar to path parameters in that they allow data to be passed in the URI, but instead of forming part of the *path*, they are specified after the path in the query section.

Consider the following example URI:

```
https://example.com/api/rest/v2/mod_example/users/colin?pet=james&type=bird
```

In this example:

- The path is: `/api/rest/v2/mode_example/users/colin`
- The query parameters are:
  
  - `pet=james`
  - `type=bird`

To define a query parameter it must be specified in the `queryparams` array, for example:

Defining query parameters

```
#[route(
path:'/users/{name}',
queryparams:[
newquery_parameter(
name:'pet',
type:param::TEXT,
),
newquery_parameter(
name:'type',
type:param::TEXT,
),
],
pathtypes:[
// ...
],
)]
```

The value of the query parameter can be fetched from the request using the `ServerRequestInterface::getQueryParams()` method, for example:

Fetching the value of a query parameter

```
publicfunctionget_user_information(
ServerRequestInterface$request,
?string$name,
):ResponseInterface{
$params=$request->getQueryParams();

// The pet name:
$params['pet'];

// The type of pet:
$params['type'];
}
```

### Optional query parameters[​](#optional-query-parameters "Direct link to Optional query parameters")

Query parameters are optional by default, but can be made required by specifying the `required` flag.

Making a query parameter required

```
newquery_parameter(
name:'pet',
type:param::TEXT,
required:true,
),
```

In addition to path and query parameters, it is sometimes necessary to specify options as Request Headers. This is particularly common in web service requests. An example of such a request might be to determine whether Moodle Filters should be applied to text content.

Header parameters are defined in the route attribute in a similar way as to path and query parameters, using the `headerparams` route property and specifying instances of the `\core\router\schema\parameters\header_object` class.

Creating a header parameter

```
#[route(
path:'/users',
headerparams:[
new\core\router\schema\parameters\header_object(
name:'Filters',
description:'Whether Moodle Filters should be applied to text in the response',
type:param::BOOL,
),
],
)]
```

### Retrieving parameter values[​](#retrieving-parameter-values-1 "Direct link to Retrieving parameter values")

Header values may be fetched using the `getHeaders()` and `getHeaderLine()` methods in the `ServerRequest` object, for example:

Retrieving header params

```
publicfunctionexample(
ServerRequestInterface$request,
):ResponseInterface{
// Get the header value as an Array.
$values=$request->getHeaders('Filters');

// Get the header value as a string.
$values=$request->getHeaderLine('Filters');
}
```

### Required and Optional header parameters[​](#required-and-optional-header-parameters "Direct link to Required and Optional header parameters")

Headers can be made required or optional by setting the `required` flag as required, for example:

Setting the required flag

```
#[route(
path:'/users',
headerparams:[
new\core\router\schema\parameters\header_object(
name:'X-Optional',
description:'An example optional parameter',
type:param::BOOL,
required:false,
default:false,
),
new\core\router\schema\parameters\header_object(
name:'X-Required',
description:'An example required parameter',
type:param::BOOL,
required:true,
),
],
)]
```

In some cases it is necessary to accept multiple header values. This can be configured using the `multiple` flag to the header object, for example:

Accepting multiple header values

```
#[route(
path:'/users',
headerparams:[
new\core\router\schema\parameters\header_object(
name:'X-Users',
description:'A list of usernames',
type:param::ALPHANUM,
multiple:true,
),
],
]
publicfunctionexample(
ServerRequestInterface$request,
):payload_response{
// Returns an array with all of the header values.
$values=$request->getHeader('X-users');

// Returns a comma-separated string with all of the header values.
$values=$request->getHeaderLine('X-users');
}
```

## Other features[​](#other-features "Direct link to Other features")

### Reusable parameters[​](#reusable-parameters "Direct link to Reusable parameters")

When writing endpoints it is common to reuse the same patterns frequently. This may be the same query, path, or header.

Since all parameter types are instances of the relevant class it is very easy to create reusable parameters by creating a new class which extends the relevant parameter type and just using that type instead.

In the following example a reusable path parameter is created for the theme name:

lib/classes/router/parameters/path\_themename.php

```
namespacecore\router\parameters;

usecore\param;
usecore\router\schema\referenced_object;

classpath_themename
extends\core\router\schema\parameters\path_parameter
implementsreferenced_object
{
publicfunction__construct(
string$name='themename',
...$args,
){
$args['name']=$name;

$args['type']=param::ALPHANUMEXT;
$args['description']='The name of a Moodle theme.';

parent::__construct(...$args);
}
}
```

To use this theme name parameter, it can be provided as a path parameter instead of `path_parameter`, for example:

Using the path\_themename parameter

```
#[route(
path:'/users/{themename}',
pathtypes:[
new\core\router\parameters\path_themename(
name:'username',
type:param::ALPHANUM,
),
],
)]
```

Use of the `referenced_object` interface for reusable components

When creating any kind of reusable component it is strongly advisable to have it implement the `\core\router\schema\referenced_object` interface.

This empty interface informs the OpenAPI specification generator that this parameter is a reusable component and that it should create an entry for it in the OpenAPI specification. Internally any use of this reusable parameter will use an OpenAPI reference.

The primary benefit of usign this interface is to reduce the size of the generated OpenAPI Schema.

### Mapped parameters[​](#mapped-parameters "Direct link to Mapped parameters")

One very powerful feature of the Moodle Routing API is provision for 'mapped' parameters which allow a standard parameter of any type to be mapped to another value of some kind.

This has several main benefits, including:

- the ability to map an identifier into an instance of a specific object; and
- allowing for multiple dynamic mappings into a single value.

Mapped parameters must implement the `\core\router\schema\parameters\mapped_property_parameter` interface which declares a single method, `add_attributes_for_parameter_value`. It takes the `ServerRequestInterface` and the value supplied by the user.

The method must add the value as an attribute to the request using the same name.

Creating a mapped path parameter for a course

```
classpath_courseextends\core\router\schema\parameters\path_parameterimplements
referenced_object,
    mapped_property_parameter
{
#[\Override]
publicfunctionadd_attributes_for_parameter_value(
ServerRequestInterface$request,
string$value,
):ServerRequestInterface{
$course=$this->get_course_for_value($value);

return$request
->withAttribute($this->name,$course)
->withAttribute(
"{$this->name}_context",
\core\context\course::instance($course->id),
);
}
}
```

Where this becomes particularly powerful is the ability to use a prefix to map multiple possible options into a single value.

In the above example, the `get_course_for_value` method can accept any of the following:

- `([\d+])` - A numeric course id
- `^idnumber:(.*)$` - A course specified by its idnumber using the prefix `idnumber:`
- `^shortname:(.*)$` - A course specified by its shortname using the prefix `shortname:`

All of these values will return the database record for the specified course.

Uniqueness of mapped property

Mapped parameters work best with unique values. In the above example it is not advisable to use the course full name as this is not a unique value.

A complete example of a mapped property

This example includes a name, type, description, and examples of correct usage. The `get_schema_from_type` method is specified and allows a more detailed description of accepted patterns using a Perl-Compatible Regular Expression.

A full example

```
namespacecore\router\parameters;

usecore\exception\not_found_exception;
usecore\param;
usecore\router\schema\example;
usecore\router\schema\parameters\mapped_property_parameter;
usecore\router\schema\referenced_object;
usePsr\Http\Message\ServerRequestInterface;

/**
 * A Moodle parameter referenced in the path.
 *
 * @package    core
 * @copyright  2023 Andrew Lyons <andrew@nicols.co.uk>
 * @license    http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */
classpath_courseextends\core\router\schema\parameters\path_parameterimplements
referenced_object,
    mapped_property_parameter
{
/**
     * Create a new path_course parameter.
     *
     * @param string $name The name of the parameter to use for the course identifier
     * @param mixed ...$extra Additional arguments
     */
publicfunction__construct(
string$name='course',
...$extra,
){
$extra['name']=$name;
$extra['type']=param::RAW;
$extra['description']=<<<EOF
        The course identifier.

        This can be the id of the course, the idnumber of the course,or the shortname of the course.

If specifying a course idnumber, the value should be in the format `idnumber:[idnumber]`.

If specifying a course shortname, the value should be in the format `name:[shortname]`.
EOF;
$extra['examples']=[
newexample(
name:'A course id',
value:54,
),
newexample(
name:'A course specified by its idnumber',
value:'idnumber:000117-physics-101-1',
),
newexample(
name:'A course specified by its shortname',
value:'name:000117-phys101-0',
),
];

parent::__construct(...$extra);
}

/**
     * Get the course object for the given identifier.
     *
     * @param string $value A course id, idnumber, or shortname
     * @return object
     * @throws not_found_exception If the course cannot be found
     */
protectedfunctionget_course_for_value(string$value):mixed{
global$DB;

$data=false;

if(is_numeric($value)){
$data=$DB->get_record('course',[
'id'=>$value,
]);
}elseif(str_starts_with($value,'idnumber:')){
$data=$DB->get_record('course',[
'idnumber'=>substr($value,strlen('idnumber:')),
]);
}elseif(str_starts_with($value,'name:')){
$data=$DB->get_record('course',[
'shortname'=>substr($value,strlen('name:')),
]);
}

if($data){
return$data;
}

thrownewnot_found_exception('course',$value);
}

#[\Override]
publicfunctionadd_attributes_for_parameter_value(
ServerRequestInterface$request,
string$value,
):ServerRequestInterface{
$course=$this->get_course_for_value($value);

return$request
->withAttribute($this->name,$course)
->withAttribute("{$this->name}_context",\core\context\course::instance($course->id));
}

#[\Override]
publicfunctionget_schema_from_type(param$type):\stdClass{
$schema=parent::get_schema_from_type($type);

$schema->pattern="^(";
$schema->pattern.=implode("|",[
'\d+',
'idnumber:.+',
'name:.+',
]);
$schema->pattern.=")$";

return$schema;
}
}
```

### Examples[​](#examples "Direct link to Examples")

When writing web services it is often desirable to give an example of the correct usage of that parameter. This can be achieved by specifying instances of the `\core\router\schema\example` to the `examples` property, for example:

Specifying an example for a parameter

```
newpath_parameter(
name:'themename',
type:param::ALPHANUMEXT,
examples:[
new\core\router\schema\example(
name:'The Boost theme',
value:'boost',
),
],
)
```