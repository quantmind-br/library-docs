---
title: collect_env - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/collect_env/
source: sitemap
fetched_at: 2026-05-07T21:16:08.023332452-03:00
rendered_js: false
word_count: 197
summary: This document provides a reference for utility functions used to collect environment information, hardware driver versions, and installed software packages for the vLLM project.
tags:
    - environment-collection
    - system-diagnostic
    - vllm-internals
    - hardware-versioning
    - package-introspection
category: reference
---

## get\_cudnn\_version [¶](#vllm.collect_env.get_cudnn_version "Permanent link")

```
get_cudnn_version(run_lambda)
```

Return a list of libcudnn.so; it's hard to tell which one is being used.

Source code in `vllm/collect_env.py`

```
defget_cudnn_version(run_lambda):
"""Return a list of libcudnn.so; it's hard to tell which one is being used."""
    if get_platform() == "win32":
        system_root = os.environ.get("SYSTEMROOT", "C:\\Windows")
        cuda_path = os.environ.get("CUDA_PATH", "%CUDA_PATH%")
        where_cmd = os.path.join(system_root, "System32", "where")
        cudnn_cmd = '{} /R "{}\\bin" cudnn*.dll'.format(where_cmd, cuda_path)
    elif get_platform() == "darwin":
        # CUDA libraries and drivers can be found in /usr/local/cuda/. See
        # https://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html#install
        # https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installmac
        # Use CUDNN_LIBRARY when cudnn library is installed elsewhere.
        cudnn_cmd = "ls /usr/local/cuda/lib/libcudnn*"
    else:
        cudnn_cmd = 'ldconfig -p | grep libcudnn | rev | cut -d" " -f1 | rev'
    rc, out, _ = run_lambda(cudnn_cmd)
    # find will return 1 if there are permission errors or if not found
    if len(out) == 0 or (rc != 1 and rc != 0):
        l = os.environ.get("CUDNN_LIBRARY")
        if l is not None and os.path.isfile(l):
            return os.path.realpath(l)
        return None
    files_set = set()
    for fn in out.split("\n"):
        fn = os.path.realpath(fn)  # eliminate symbolic links
        if os.path.isfile(fn):
            files_set.add(fn)
    if not files_set:
        return None
    # Alphabetize the result because the order is non-deterministic otherwise
    files = sorted(files_set)
    if len(files) == 1:
        return files[0]
    result = "\n".join(files)
    return "Probably one of the following:\n{}".format(result)
```

## get\_intel\_graphics\_compiler\_version [¶](#vllm.collect_env.get_intel_graphics_compiler_version "Permanent link")

```
get_intel_graphics_compiler_version(run_lambda)
```

Return Intel Graphics Compiler (IGC) version.

Source code in `vllm/collect_env.py`

```
defget_intel_graphics_compiler_version(run_lambda):
"""Return Intel Graphics Compiler (IGC) version."""
    return get_pkg_version(run_lambda, "igc")
```

## get\_level\_zero\_driver\_version [¶](#vllm.collect_env.get_level_zero_driver_version "Permanent link")

```
get_level_zero_driver_version(run_lambda)
```

Return Level Zero driver version.

Source code in `vllm/collect_env.py`

```
defget_level_zero_driver_version(run_lambda):
"""Return Level Zero driver version."""
    return get_pkg_version(run_lambda, "level_zero_driver")
```

## get\_level\_zero\_loader\_version [¶](#vllm.collect_env.get_level_zero_loader_version "Permanent link")

```
get_level_zero_loader_version(run_lambda)
```

Return Level Zero loader runtime version.

Source code in `vllm/collect_env.py`

```
defget_level_zero_loader_version(run_lambda):
"""Return Level Zero loader runtime version."""
    return get_pkg_version(run_lambda, "level_zero_loader")
```

## get\_oneapi\_ccl\_version [¶](#vllm.collect_env.get_oneapi_ccl_version "Permanent link")

```
get_oneapi_ccl_version(run_lambda)
```

Return oneAPI Collective Communications Library (oneCCL) version.

Source code in `vllm/collect_env.py`

```
defget_oneapi_ccl_version(run_lambda):
"""Return oneAPI Collective Communications Library (oneCCL) version."""
    return get_pkg_version(run_lambda, "oneccl")
```

## get\_oneapi\_compiler\_version [¶](#vllm.collect_env.get_oneapi_compiler_version "Permanent link")

```
get_oneapi_compiler_version(run_lambda)
```

Return Intel oneAPI DPC++/C++ Compiler version via icpx.

Source code in `vllm/collect_env.py`

```
defget_oneapi_compiler_version(run_lambda):
"""Return Intel oneAPI DPC++/C++ Compiler version via icpx."""
    return run_and_parse_first_match(
        run_lambda, "icpx --version", r"oneAPI DPC\+\+/C\+\+ Compiler (\S+)"
    )
```

## get\_pip\_packages [¶](#vllm.collect_env.get_pip_packages "Permanent link")

```
get_pip_packages(run_lambda, patterns=None)
```

Return `pip list` output. Note: will also find conda-installed pytorch and numpy packages.

Source code in `vllm/collect_env.py`

```
defget_pip_packages(run_lambda, patterns=None):
"""Return `pip list` output. Note: will also find conda-installed pytorch and numpy packages."""
    if patterns is None:
        patterns = DEFAULT_PIP_PATTERNS

    defrun_with_pip():
        try:
            importimportlib.util

            pip_spec = importlib.util.find_spec("pip")
            pip_available = pip_spec is not None
        except ImportError:
            pip_available = False

        if pip_available:
            cmd = [sys.executable, "-mpip", "list", "--format=freeze"]
        elif is_uv_venv():
            print("uv is set")
            cmd = ["uv", "pip", "list", "--format=freeze"]
        else:
            raise RuntimeError(
                "Could not collect pip list output (pip or uv module not available)"
            )

        out = run_and_read_all(run_lambda, cmd)
        return "\n".join(
            line for line in out.splitlines() if any(name in line for name in patterns)
        )

    pip_version = "pip3" if sys.version[0] == "3" else "pip"
    out = run_with_pip()
    return pip_version, out
```

## get\_rocm\_version [¶](#vllm.collect_env.get_rocm_version "Permanent link")

```
get_rocm_version(run_lambda)
```

Returns the ROCm version if available, otherwise 'N/A'.

Source code in `vllm/collect_env.py`

```
defget_rocm_version(run_lambda):
"""Returns the ROCm version if available, otherwise 'N/A'."""
    return run_and_parse_first_match(
        run_lambda, "hipcc --version", r"HIP version: (\S+)"
    )
```

## get\_sycl\_version [¶](#vllm.collect_env.get_sycl_version "Permanent link")

```
get_sycl_version(run_lambda)
```

Return SYCL/DPC++ compiler build version.

Source code in `vllm/collect_env.py`

```
defget_sycl_version(run_lambda):
"""Return SYCL/DPC++ compiler build version."""
    return run_and_parse_first_match(run_lambda, "icpx --version", r"\((\d[\d.]+)\)")
```

## run [¶](#vllm.collect_env.run "Permanent link")

Return (return-code, stdout, stderr).

Source code in `vllm/collect_env.py`

```
defrun(command):
"""Return (return-code, stdout, stderr)."""
    shell = True if type(command) is str else False
    try:
        p = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell
        )
        raw_output, raw_err = p.communicate()
        rc = p.returncode
        if get_platform() == "win32":
            enc = "oem"
        else:
            enc = locale.getpreferredencoding()
        output = raw_output.decode(enc)
        if command == "nvidia-smi topo -m":
            # don't remove the leading whitespace of `nvidia-smi topo -m`
            #   because they are meaningful
            output = output.rstrip()
        else:
            output = output.strip()
        err = raw_err.decode(enc)
        return rc, output, err.strip()

    except FileNotFoundError:
        cmd_str = command if isinstance(command, str) else command[0]
        return 127, "", f"Command not found: {cmd_str}"
```

## run\_and\_parse\_first\_match [¶](#vllm.collect_env.run_and_parse_first_match "Permanent link")

```
run_and_parse_first_match(run_lambda, command, regex)
```

Run command using run\_lambda, returns the first regex match if it exists.

Source code in `vllm/collect_env.py`

```
defrun_and_parse_first_match(run_lambda, command, regex):
"""Run command using run_lambda, returns the first regex match if it exists."""
    rc, out, _ = run_lambda(command)
    if rc != 0:
        return None
    match = re.search(regex, out)
    if match is None:
        return None
    return match.group(1)
```

## run\_and\_read\_all [¶](#vllm.collect_env.run_and_read_all "Permanent link")

```
run_and_read_all(run_lambda, command)
```

Run command using run\_lambda; reads and returns entire output if rc is 0.

Source code in `vllm/collect_env.py`

```
defrun_and_read_all(run_lambda, command):
"""Run command using run_lambda; reads and returns entire output if rc is 0."""
    rc, out, _ = run_lambda(command)
    if rc != 0:
        return None
    return out
```