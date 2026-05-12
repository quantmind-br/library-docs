---
title: repo_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/repo_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:15.995305915-03:00
rendered_js: false
word_count: 119
summary: Provides utility functions for interacting with the Hugging Face Hub to download files, retrieve file contents as bytes, or parse configuration files into dictionaries.
tags:
    - hugging-face
    - model-repository
    - file-download
    - data-extraction
    - python-utilities
category: api
---

## vllm.transformers\_utils.repo\_utils [¶](#vllm.transformers_utils.repo_utils "Permanent link")

Utilities for model repo interaction.

## \_try\_download\_from\_hf\_hub [¶](#vllm.transformers_utils.repo_utils._try_download_from_hf_hub "Permanent link")

```
_try_download_from_hf_hub(
    model: str | Path, file_name: str, revision: str | None
) -> Path | None
```

Try to download a file from HuggingFace Hub.

Returns the local path on success, None on failure. Skips download if model is a local directory.

Source code in `vllm/transformers_utils/repo_utils.py`

```
def_try_download_from_hf_hub(
    model: str | Path, file_name: str, revision: str | None
) -> Path | None:
"""Try to download a file from HuggingFace Hub.

    Returns the local path on success, None on failure.
    Skips download if model is a local directory.
    """
    if Path(model).is_dir():
        return None
    try:
        return Path(hf_hub_download(model, file_name, revision=revision))
    except huggingface_hub.errors.OfflineModeIsEnabled:
        return None
    except (
        RepositoryNotFoundError,
        RevisionNotFoundError,
        EntryNotFoundError,
        LocalEntryNotFoundError,
    ) as e:
        logger.debug("File or repository not found in hf_hub_download: %s", e)
        return None
    except HfHubHTTPError as e:
        logger.warning(
            "Cannot connect to Hugging Face Hub. Skipping file download for '%s':",
            file_name,
            exc_info=e,
        )
        return None
```

## get\_hf\_file\_bytes [¶](#vllm.transformers_utils.repo_utils.get_hf_file_bytes "Permanent link")

```
get_hf_file_bytes(
    file_name: str,
    model: str | Path,
    revision: str | None = "main",
) -> bytes | None
```

Get file contents from HuggingFace repository as bytes.

Source code in `vllm/transformers_utils/repo_utils.py`

```
defget_hf_file_bytes(
    file_name: str, model: str | Path, revision: str | None = "main"
) -> bytes | None:
"""Get file contents from HuggingFace repository as bytes."""
    file_path = try_get_local_file(model=model, file_name=file_name, revision=revision)

    if file_path is None:
        file_path = _try_download_from_hf_hub(model, file_name, revision)

    if file_path is not None and file_path.is_file():
        with open(file_path, "rb") as file:
            return file.read()

    return None
```

## get\_hf\_file\_to\_dict [¶](#vllm.transformers_utils.repo_utils.get_hf_file_to_dict "Permanent link")

```
get_hf_file_to_dict(
    file_name: str,
    model: str | Path,
    revision: str | None = "main",
)
```

Downloads a file from the Hugging Face Hub and returns its contents as a dictionary.

Parameters: - file\_name (str): The name of the file to download. - model (str): The name of the model on the Hugging Face Hub. - revision (str): The specific version of the model.

Returns: - config\_dict (dict): A dictionary containing the contents of the downloaded file.

Source code in `vllm/transformers_utils/repo_utils.py`

```
defget_hf_file_to_dict(
    file_name: str, model: str | Path, revision: str | None = "main"
):
"""
    Downloads a file from the Hugging Face Hub and returns
    its contents as a dictionary.

    Parameters:
    - file_name (str): The name of the file to download.
    - model (str): The name of the model on the Hugging Face Hub.
    - revision (str): The specific version of the model.

    Returns:
    - config_dict (dict): A dictionary containing
    the contents of the downloaded file.
    """

    file_path = try_get_local_file(model=model, file_name=file_name, revision=revision)

    if file_path is None:
        file_path = _try_download_from_hf_hub(model, file_name, revision)

    if file_path is not None and file_path.is_file():
        with open(file_path) as file:
            return json.load(file)

    return None
```