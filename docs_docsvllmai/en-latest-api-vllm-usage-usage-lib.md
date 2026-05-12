---
title: usage_lib - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/usage/usage_lib/
source: sitemap
fetched_at: 2026-05-07T21:38:26.435353142-03:00
rendered_js: false
word_count: 0
summary: This document defines a mechanism for collecting and transmitting platform, hardware, and usage metrics for the vLLM system to a remote server.
tags:
    - telemetry
    - data-collection
    - usage-stats
    - platform-monitoring
    - system-metrics
    - vllm-infrastructure
category: api
---

```
classUsageMessage:
"""Collect platform information and send it to the usage stats server."""

    def__init__(self) -> None:
        # NOTE: vLLM's server _only_ support flat KV pair.
        # Do not use nested fields.

        self.uuid = str(uuid4())

        # Environment Information
        self.provider: str | None = None
        self.num_cpu: int | None = None
        self.cpu_type: str | None = None
        self.cpu_family_model_stepping: str | None = None
        self.total_memory: int | None = None
        self.architecture: str | None = None
        self.platform: str | None = None
        self.xpu_runtime: str | None = None
        self.cuda_runtime: str | None = None
        self.gpu_count: int | None = None
        self.gpu_type: str | None = None
        self.gpu_memory_per_device: int | None = None
        self.env_var_json: str | None = None

        # vLLM Information
        self.model_architecture: str | None = None
        self.vllm_version: str | None = None
        self.context: str | None = None

        # Metadata
        self.log_time: int | None = None
        self.source: str | None = None

    defreport_usage(
        self,
        model_architecture: str,
        usage_context: UsageContext,
        extra_kvs: dict[str, Any] | None = None,
    ) -> None:
        t = Thread(
            target=self._report_usage_worker,
            args=(model_architecture, usage_context, extra_kvs or {}),
            daemon=True,
        )
        t.start()

    def_report_usage_worker(
        self,
        model_architecture: str,
        usage_context: UsageContext,
        extra_kvs: dict[str, Any],
    ) -> None:
        self._report_usage_once(model_architecture, usage_context, extra_kvs)
        self._report_continuous_usage()

    def_report_tpu_inference_usage(self) -> bool:
        try:
            fromtpu_inferenceimport tpu_info, utils

            self.gpu_count = tpu_info.get_num_chips()
            self.gpu_type = tpu_info.get_tpu_type()
            self.gpu_memory_per_device = utils.get_device_hbm_limit()
            self.cuda_runtime = "tpu_inference"
            return True
        except Exception:
            return False

    def_report_usage_once(
        self,
        model_architecture: str,
        usage_context: UsageContext,
        extra_kvs: dict[str, Any],
    ) -> None:
        # Platform information
        fromvllm.platformsimport current_platform

        if current_platform.is_cuda_alike():
            self.gpu_count = current_platform.device_count()
            self.gpu_type, self.gpu_memory_per_device = cuda_get_device_properties(
                0, ("name", "total_memory")
            )
        if current_platform.is_cuda():
            self.cuda_runtime = torch.version.cuda
        if current_platform.is_xpu():
            self.xpu_runtime = torch.version.xpu
            self.gpu_count = torch.xpu.device_count()
            self.gpu_type = torch.xpu.get_device_name(0)
            self.gpu_memory_per_device = torch.xpu.get_device_properties(0).total_memory
        if current_platform.is_tpu():  # noqa: SIM102
            if not self._report_tpu_inference_usage():
                logger.exception("Failed to collect TPU information")
        self.provider = _detect_cloud_provider()
        self.architecture = platform.machine()
        self.platform = platform.platform()
        self.total_memory = psutil.virtual_memory().total

        info = cpuinfo.get_cpu_info()
        self.num_cpu = info.get("count", None)
        self.cpu_type = info.get("brand_raw", "")
        self.cpu_family_model_stepping = ",".join(
            [
                str(info.get("family", "")),
                str(info.get("model", "")),
                str(info.get("stepping", "")),
            ]
        )

        # vLLM information
        self.context = usage_context.value
        self.vllm_version = VLLM_VERSION
        self.model_architecture = model_architecture

        # Environment variables
        self.env_var_json = json.dumps(
            {env_var: getattr(envs, env_var) for env_var in _USAGE_ENV_VARS_TO_COLLECT}
        )

        # Metadata
        self.log_time = _get_current_timestamp_ns()
        self.source = envs.VLLM_USAGE_SOURCE

        data = vars(self)
        if extra_kvs:
            data.update(extra_kvs)

        self._write_to_file(data)
        self._send_to_server(data)

    def_report_continuous_usage(self):
"""Report usage every 10 minutes.

        This helps us to collect more data points for uptime of vLLM usages.
        This function can also help send over performance metrics over time.
        """
        while True:
            time.sleep(600)
            data = {
                "uuid": self.uuid,
                "log_time": _get_current_timestamp_ns(),
            }
            data.update(_GLOBAL_RUNTIME_DATA)

            self._write_to_file(data)
            self._send_to_server(data)

    def_send_to_server(self, data: dict[str, Any]) -> None:
        try:
            global_http_client = global_http_connection.get_sync_client()
            global_http_client.post(_USAGE_STATS_SERVER, json=data)
        except requests.exceptions.RequestException:
            # silently ignore unless we are using debug log
            logging.debug("Failed to send usage data to server")

    def_write_to_file(self, data: dict[str, Any]) -> None:
        os.makedirs(os.path.dirname(_USAGE_STATS_JSON_PATH), exist_ok=True)
        Path(_USAGE_STATS_JSON_PATH).touch(exist_ok=True)
        with open(_USAGE_STATS_JSON_PATH, "a") as f:
            json.dump(data, f)
            f.write("\n")
```