---
title: PythonInterpreter - DSPy
url: https://dspy.ai/api/tools/PythonInterpreter/
source: sitemap
fetched_at: 2026-01-23T08:02:48.363188163-03:00
rendered_js: false
word_count: 360
summary: This document details the dspy.PythonInterpreter class, which provides a secure, sandboxed environment for executing Python code using Deno and Pyodide. It outlines configuration options for host isolation, including filesystem access, network permissions, and the integration of host-side tools.
tags:
    - dspy
    - python-interpreter
    - sandboxing
    - pyodide
    - deno
    - secure-execution
    - code-interpreter
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/tools/PythonInterpreter.md "Edit this page")

## `dspy.PythonInterpreter(deno_command: list[str] | None = None, enable_read_paths: list[PathLike | str] | None = None, enable_write_paths: list[PathLike | str] | None = None, enable_env_vars: list[str] | None = None, enable_network_access: list[str] | None = None, sync_files: bool = True, tools: dict[str, Callable[..., str]] | None = None, output_fields: list[dict] | None = None)` [¶](#dspy.PythonInterpreter "Permanent link")

Local interpreter for secure Python execution using Deno and Pyodide.

Implements the Interpreter protocol for secure code execution in a WASM-based sandbox. Code runs in an isolated Pyodide environment with no access to the host filesystem, network, or environment by default.

Prerequisites

Deno must be installed: https://docs.deno.com/runtime/getting\_started/installation/

Example

```
# Basic execution
with PythonInterpreter() as interp:
    result = interp("print(1 + 2)")  # Returns "3"

# With host-side tools
defmy_tool(question: str) -> str:
    return "answer"

with PythonInterpreter(tools={"my_tool": my_tool}) as interp:
    result = interp("print(my_tool(question='test'))")
```

Parameters:

Name Type Description Default `deno_command` `list[str] | None`

command list to launch Deno.

`None` `enable_read_paths` `list[PathLike | str] | None`

Files or directories to allow reading from in the sandbox.

`None` `enable_write_paths` `list[PathLike | str] | None`

Files or directories to allow writing to in the sandbox. All write paths will also be able to be read from for mounting.

`None` `enable_env_vars` `list[str] | None`

Environment variable names to allow in the sandbox.

`None` `enable_network_access` `list[str] | None`

Domains or IPs to allow network access in the sandbox.

`None` `sync_files` `bool`

If set, syncs changes within the sandbox back to original files after execution.

`True` `tools` `dict[str, Callable[..., str]] | None`

Dictionary mapping tool names to callable functions. Each function should accept keyword arguments and return a string. Tools are callable directly from sandbox code by name.

`None` `output_fields` `list[dict] | None`

List of output field definitions for typed SUBMIT signature. Each dict should have 'name' and optionally 'type' keys.

`None`

Source code in `dspy/primitives/python_interpreter.py`

```
def__init__(
    self,
    deno_command: list[str] | None = None,
    enable_read_paths: list[PathLike | str] | None = None,
    enable_write_paths: list[PathLike | str] | None = None,
    enable_env_vars: list[str] | None = None,
    enable_network_access: list[str] | None = None,
    sync_files: bool = True,
    tools: dict[str, Callable[..., str]] | None = None,
    output_fields: list[dict] | None = None,
) -> None:
"""
    Args:
        deno_command: command list to launch Deno.
        enable_read_paths: Files or directories to allow reading from in the sandbox.
        enable_write_paths: Files or directories to allow writing to in the sandbox.
            All write paths will also be able to be read from for mounting.
        enable_env_vars: Environment variable names to allow in the sandbox.
        enable_network_access: Domains or IPs to allow network access in the sandbox.
        sync_files: If set, syncs changes within the sandbox back to original files after execution.
        tools: Dictionary mapping tool names to callable functions.
               Each function should accept keyword arguments and return a string.
               Tools are callable directly from sandbox code by name.
        output_fields: List of output field definitions for typed SUBMIT signature.
               Each dict should have 'name' and optionally 'type' keys.
    """
    if isinstance(deno_command, dict):
        raise TypeError("deno_command must be a list of strings, not a dict")

    self.enable_read_paths = enable_read_paths or []
    self.enable_write_paths = enable_write_paths or []
    self.enable_env_vars = enable_env_vars or []
    self.enable_network_access = enable_network_access or []
    self.sync_files = sync_files
    self.tools = dict(tools) if tools else {}
    self.output_fields = output_fields
    self._tools_registered = False
    # TODO later on add enable_run (--allow-run) by proxying subprocess.run through Deno.run() to fix 'emscripten does not support processes' error

    if deno_command:
        self.deno_command = list(deno_command)
    else:
        args = ["deno", "run"]

        # Allow reading runner.js and explicitly enabled paths
        allowed_read_paths = [self._get_runner_path()]

        # Also allow reading Deno's cache directory so Pyodide can load its files
        deno_dir = self._get_deno_dir()
        if deno_dir:
            allowed_read_paths.append(deno_dir)

        if self.enable_read_paths:
            allowed_read_paths.extend(str(p) for p in self.enable_read_paths)
        if self.enable_write_paths:
            allowed_read_paths.extend(str(p) for p in self.enable_write_paths)
        args.append(f"--allow-read={','.join(allowed_read_paths)}")

        self._env_arg = ""
        if self.enable_env_vars:
            user_vars = [str(v).strip() for v in self.enable_env_vars]
            args.append("--allow-env=" + ",".join(user_vars))
            self._env_arg = ",".join(user_vars)
        if self.enable_network_access:
            args.append(f"--allow-net={','.join(str(x)forxinself.enable_network_access)}")
        if self.enable_write_paths:
            args.append(f"--allow-write={','.join(str(x)forxinself.enable_write_paths)}")

        args.append(self._get_runner_path())

        # For runner.js to load in env vars
        if self._env_arg:
            args.append(self._env_arg)
        self.deno_command = args

    self.deno_process = None
    self._mounted_files = False
```

### Functions[¶](#dspy.PythonInterpreter-functions "Permanent link")

#### `__call__(code: str, variables: dict[str, Any] | None = None) -> Any` [¶](#dspy.PythonInterpreter.__call__ "Permanent link")

Source code in `dspy/primitives/python_interpreter.py`

```
def__call__(
    self,
    code: str,
    variables: dict[str, Any] | None = None,
) -> Any:
    return self.execute(code, variables)
```

#### `execute(code: str, variables: dict[str, Any] | None = None) -> Any` [¶](#dspy.PythonInterpreter.execute "Permanent link")

Source code in `dspy/primitives/python_interpreter.py`

```
defexecute(
    self,
    code: str,
    variables: dict[str, Any] | None = None,
) -> Any:
    variables = variables or {}
    code = self._inject_variables(code, variables)
    self._ensure_deno_process()
    self._mount_files()
    self._register_tools()

    # Send the code as JSON
    input_data = json.dumps({"code": code})
    try:
        self.deno_process.stdin.write(input_data + "\n")
        self.deno_process.stdin.flush()
    except BrokenPipeError:
        # If the process died, restart and try again once
        self._tools_registered = False
        self._ensure_deno_process()
        self._register_tools()
        self.deno_process.stdin.write(input_data + "\n")
        self.deno_process.stdin.flush()

    # Read and handle messages until we get the final output.
    # Loop is needed because tool calls require back-and-forth communication.
    while True:
        output_line = self.deno_process.stdout.readline().strip()
        if not output_line:
            # Possibly the subprocess died or gave no output
            err_output = self.deno_process.stderr.read()
            raise CodeInterpreterError(f"No output from Deno subprocess. Stderr: {err_output}")

        # Parse that line as JSON
        try:
            result = json.loads(output_line)
        except json.JSONDecodeError:
            # If not valid JSON, just return raw text
            result = {"output": output_line}

        # Handle tool call requests from sandbox
        if result.get("type") == "tool_call":
            self._handle_tool_call(result)
            continue

        # Handle errors based on errorType
        if "error" in result:
            error_msg = result["error"]
            error_type = result.get("errorType", "Sandbox Error")
            error_args = result.get("errorArgs", [])

            if error_type == "FinalOutput":
                output = error_args[0] if error_args else None
                self._sync_files()
                return FinalOutput(output)
            elif error_type == "SyntaxError":
                raise SyntaxError(f"Invalid Python syntax. message: {error_msg}")
            else:
                raise CodeInterpreterError(f"{error_type}: {error_argsorerror_msg}")

        # If there's no error or got `FinalAnswer`, return the "output" field
        self._sync_files()
        return result.get("output", None)
```

#### `shutdown() -> None` [¶](#dspy.PythonInterpreter.shutdown "Permanent link")

Source code in `dspy/primitives/python_interpreter.py`

```
defshutdown(self) -> None:
    if self.deno_process and self.deno_process.poll() is None:
        self.deno_process.stdin.write(json.dumps({"shutdown": True}) + "\n")
        self.deno_process.stdin.flush()
        self.deno_process.stdin.close()
        self.deno_process.wait()
    self.deno_process = None
```

#### `start() -> None` [¶](#dspy.PythonInterpreter.start "Permanent link")

Initialize the Deno/Pyodide sandbox.

This pre-warms the sandbox by starting the Deno subprocess. Can be called explicitly for pooling, or will be called lazily on first execute().

Idempotent: safe to call multiple times.

Source code in `dspy/primitives/python_interpreter.py`

```
defstart(self) -> None:
"""Initialize the Deno/Pyodide sandbox.

    This pre-warms the sandbox by starting the Deno subprocess.
    Can be called explicitly for pooling, or will be called lazily
    on first execute().

    Idempotent: safe to call multiple times.
    """
    self._ensure_deno_process()
```

:::