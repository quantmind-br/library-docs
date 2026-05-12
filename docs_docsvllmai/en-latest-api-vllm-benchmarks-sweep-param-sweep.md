---
title: param_sweep - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/sweep/param_sweep/
source: sitemap
fetched_at: 2026-05-07T21:15:58.880108085-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python class that manages parameter sweep configurations and facilitates their conversion into command-line arguments.
tags:
    - python-class
    - parameter-sweep
    - cli-arguments
    - data-normalization
    - config-management
category: reference
---

```
classParameterSweepItem(dict[str, object]):
    @classmethod
    deffrom_record(cls, record: dict[str, object]):
        if not isinstance(record, dict):
            raise TypeError(
                f"Each item in the parameter sweep should be a dictionary, "
                f"but found type: {type(record)}"
            )

        return cls(record)

    def__or__(self, other: dict[str, Any]):
        return type(self)(super().__or__(other))

    @property
    defname(self) -> str:
"""
        Get the name for this parameter sweep item.

        Returns the '_benchmark_name' field if present, otherwise returns a text
        representation of all parameters.
        """
        if "_benchmark_name" in self:
            return str(self["_benchmark_name"])

        return self.as_text(sep="-")

    # In JSON, we prefer "_"
    def_iter_param_key_candidates(self, param_key: str):
        # Inner config arguments are not converted by the CLI
        if "." in param_key:
            prefix, rest = param_key.split(".", 1)
            for prefix_candidate in self._iter_param_key_candidates(prefix):
                yield prefix_candidate + "." + rest

            return

        yield param_key
        yield param_key.replace("-", "_")
        yield param_key.replace("_", "-")

    # In CLI, we prefer "-"
    def_iter_cmd_key_candidates(self, param_key: str):
        for k in reversed(tuple(self._iter_param_key_candidates(param_key))):
            yield "--" + k

    def_normalize_cmd_key(self, param_key: str):
        return next(self._iter_cmd_key_candidates(param_key))

    defhas_param(self, param_key: str) -> bool:
        return any(k in self for k in self._iter_param_key_candidates(param_key))

    def_normalize_cmd_kv_pair(self, k: str, v: object) -> list[str]:
"""
        Normalize a key-value pair into command-line arguments.

        Returns a list containing either:
        - A single element for boolean flags (e.g., ['--flag'] or ['--flag=true'])
        - Two elements for key-value pairs (e.g., ['--key', 'value'])
        """
        if isinstance(v, bool):
            # For nested params (containing "."), use =true/false syntax
            if "." in k:
                return [f"{self._normalize_cmd_key(k)}={'true'ifvelse'false'}"]
            else:
                return [self._normalize_cmd_key(k if v else "no-" + k)]
        else:
            return [self._normalize_cmd_key(k), str(v)]

    defapply_to_cmd(self, cmd: list[str]) -> list[str]:
        cmd = list(cmd)

        for k, v in self.items():
            # Skip the '_benchmark_name' field, not a parameter
            if k == "_benchmark_name":
                continue

            # Serialize dict values as JSON
            if isinstance(v, dict):
                v = json.dumps(v)

            for k_candidate in self._iter_cmd_key_candidates(k):
                try:
                    k_idx = cmd.index(k_candidate)

                    # Replace existing parameter
                    normalized = self._normalize_cmd_kv_pair(k, v)
                    if len(normalized) == 1:
                        # Boolean flag
                        cmd[k_idx] = normalized[0]
                    else:
                        # Key-value pair
                        cmd[k_idx] = normalized[0]
                        cmd[k_idx + 1] = normalized[1]

                    break
                except ValueError:
                    continue
            else:
                # Add new parameter
                cmd.extend(self._normalize_cmd_kv_pair(k, v))

        return cmd

    defas_text(self, sep: str = ", ") -> str:
        return sep.join(f"{k}={v}" for k, v in self.items() if k != "_benchmark_name")
```