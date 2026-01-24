---
title: pydantic_ai.format_prompt - Pydantic AI
url: https://ai.pydantic.dev/api/format_prompt/
source: sitemap
fetched_at: 2026-01-22T22:24:04.713167752-03:00
rendered_js: false
word_count: 220
summary: Documentation for the format_as_xml function which serializes Python objects, including Pydantic models and dataclasses, into XML to improve readability for Large Language Models.
tags:
    - python
    - xml-serialization
    - pydantic
    - llm-formatting
    - data-conversion
category: api
---

Format a Python object as XML.

This is useful since LLMs often find it easier to read semi-structured data (e.g. examples) as XML, rather than JSON etc.

Supports: `str`, `bytes`, `bytearray`, `bool`, `int`, `float`, `date`, `datetime`, `time`, `timedelta`, `Enum`, `Mapping`, `Iterable`, `dataclass`, and `BaseModel`.

Parameters:

Name Type Description Default `obj` `Any`

Python Object to serialize to XML.

*required* `root_tag` `str | None`

Outer tag to wrap the XML in, use `None` to omit the outer tag.

`None` `item_tag` `str`

Tag to use for each item in an iterable (e.g. list), this is overridden by the class name for dataclasses and Pydantic models.

`'item'` `none_str` `str`

String to use for `None` values.

`'null'` `indent` `str | None`

Indentation string to use for pretty printing.

`' '` `include_field_info` `Literal['once'] | bool`

Whether to include attributes like Pydantic `Field` attributes and dataclasses `field()` `metadata` as XML attributes. In both cases the allowed `Field` attributes and `field()` metadata keys are `title` and `description`. If a field is repeated in the data (e.g. in a list) by setting `once` the attributes are included only in the first occurrence of an XML element relative to the same field.

`False`

Returns:

Type Description `str`

XML representation of the object.

Example:

format\_as\_xml\_example.py

```
frompydantic_aiimport format_as_xml

print(format_as_xml({'name': 'John', 'height': 6, 'weight': 200}, root_tag='user'))
'''
<user>
  <name>John</name>
  <height>6</height>
  <weight>200</weight>
</user>
'''
```

Source code in `pydantic_ai_slim/pydantic_ai/format_prompt.py`

```
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
```

````
defformat_as_xml(
    obj: Any,
    root_tag: str | None = None,
    item_tag: str = 'item',
    none_str: str = 'null',
    indent: str | None = '  ',
    include_field_info: Literal['once'] | bool = False,
) -> str:
"""Format a Python object as XML.

    This is useful since LLMs often find it easier to read semi-structured data (e.g. examples) as XML,
    rather than JSON etc.

    Supports: `str`, `bytes`, `bytearray`, `bool`, `int`, `float`, `date`, `datetime`, `time`, `timedelta`, `Enum`,
    `Mapping`, `Iterable`, `dataclass`, and `BaseModel`.

    Args:
        obj: Python Object to serialize to XML.
        root_tag: Outer tag to wrap the XML in, use `None` to omit the outer tag.
        item_tag: Tag to use for each item in an iterable (e.g. list), this is overridden by the class name
            for dataclasses and Pydantic models.
        none_str: String to use for `None` values.
        indent: Indentation string to use for pretty printing.
        include_field_info: Whether to include attributes like Pydantic `Field` attributes and dataclasses `field()`
            `metadata` as XML attributes. In both cases the allowed `Field` attributes and `field()` metadata keys are
            `title` and `description`. If a field is repeated in the data (e.g. in a list) by setting `once`
            the attributes are included only in the first occurrence of an XML element relative to the same field.

    Returns:
        XML representation of the object.

    Example:
    ```python {title="format_as_xml_example.py" lint="skip"}
    from pydantic_ai import format_as_xml

    print(format_as_xml({'name': 'John', 'height': 6, 'weight': 200}, root_tag='user'))
    '''
    <user>
      <name>John</name>
      <height>6</height>
      <weight>200</weight>
    </user>
    '''
    ```
    """
    el = _ToXml(
        data=obj,
        item_tag=item_tag,
        none_str=none_str,
        include_field_info=include_field_info,
    ).to_xml(root_tag)
    if root_tag is None and el.text is None:
        join = '' if indent is None else '\n'
        return join.join(_rootless_xml_elements(el, indent))
    else:
        if indent is not None:
            ElementTree.indent(el, space=indent)
        return ElementTree.tostring(el, encoding='unicode')
````