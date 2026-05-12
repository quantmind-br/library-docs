---
title: s3_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/s3_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:18.170296926-03:00
rendered_js: false
word_count: 185
summary: This document provides technical documentation and function signatures for S3 file listing utilities, allowing for filtered retrieval of file paths from cloud storage.
tags:
    - s3-utility
    - file-listing
    - cloud-storage
    - pattern-filtering
    - python-api
category: api
---

## glob [¶](#vllm.transformers_utils.s3_utils.glob "Permanent link")

```
glob(
    s3: BaseClient | None = None,
    path: str = "",
    allow_pattern: list[str] | None = None,
) -> list[str]
```

List full file names from S3 path and filter by allow pattern.

Parameters:

Name Type Description Default `s3` `BaseClient | None`

S3 client to use.

`None` `path` `str`

The S3 path to list from.

`''` `allow_pattern` `list[str] | None`

A list of patterns of which files to pull.

`None`

Returns:

Type Description `list[str]`

list\[str]: List of full S3 paths allowed by the pattern

Source code in `vllm/transformers_utils/s3_utils.py`

```
defglob(
    s3: "BaseClient | None" = None,
    path: str = "",
    allow_pattern: list[str] | None = None,
) -> list[str]:
"""
    List full file names from S3 path and filter by allow pattern.

    Args:
        s3: S3 client to use.
        path: The S3 path to list from.
        allow_pattern: A list of patterns of which files to pull.

    Returns:
        list[str]: List of full S3 paths allowed by the pattern
    """
    if s3 is None:
        s3 = boto3.client("s3")
    if not path.endswith("/"):
        path = path + "/"
    bucket_name, _, paths = list_files(s3, path=path, allow_pattern=allow_pattern)
    return [f"s3://{bucket_name}/{path}" for path in paths]
```

## list\_files [¶](#vllm.transformers_utils.s3_utils.list_files "Permanent link")

List files from S3 path and filter by pattern.

Parameters:

Name Type Description Default `s3` `BaseClient`

S3 client to use.

*required* `path` `str`

The S3 path to list from.

*required* `allow_pattern` `list[str] | None`

A list of patterns of which files to pull.

`None` `ignore_pattern` `list[str] | None`

A list of patterns of which files not to pull.

`None`

Returns:

Type Description `tuple[str, str, list[str]]`

tuple\[str, str, list\[str]]: A tuple where: - The first element is the bucket name - The second element is string represent the bucket and the prefix as a dir like string - The third element is a list of files allowed or disallowed by pattern

Source code in `vllm/transformers_utils/s3_utils.py`

```
deflist_files(
    s3: "BaseClient",
    path: str,
    allow_pattern: list[str] | None = None,
    ignore_pattern: list[str] | None = None,
) -> tuple[str, str, list[str]]:
"""
    List files from S3 path and filter by pattern.

    Args:
        s3: S3 client to use.
        path: The S3 path to list from.
        allow_pattern: A list of patterns of which files to pull.
        ignore_pattern: A list of patterns of which files not to pull.

    Returns:
        tuple[str, str, list[str]]: A tuple where:
            - The first element is the bucket name
            - The second element is string represent the bucket
              and the prefix as a dir like string
            - The third element is a list of files allowed or
              disallowed by pattern
    """
    parts = path.removeprefix("s3://").split("/")
    prefix = "/".join(parts[1:])
    bucket_name = parts[0]

    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    paths = [obj["Key"] for obj in objects.get("Contents", [])]

    paths = _filter_ignore(paths, ["*/"])
    if allow_pattern is not None:
        paths = _filter_allow(paths, allow_pattern)

    if ignore_pattern is not None:
        paths = _filter_ignore(paths, ignore_pattern)

    return bucket_name, prefix, paths
```