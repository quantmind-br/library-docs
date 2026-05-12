---
title: tool - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/mcp/tool/
source: sitemap
fetched_at: 2026-05-07T21:19:44.964458596-03:00
rendered_js: false
word_count: 57
summary: This document defines the HarmonyPythonTool class, which integrates a code execution environment into vLLM, and provides utility functions to validate and interface with external Python tools.
tags:
    - python-tool
    - vllm
    - code-interpreter
    - mcp
    - integration
    - software-validation
category: reference
---

## HarmonyPythonTool [¶](#vllm.entrypoints.mcp.tool.HarmonyPythonTool "Permanent link")

Bases: `Tool`

Source code in `vllm/entrypoints/mcp/tool.py`

```
classHarmonyPythonTool(Tool):
    def__init__(self):
        self.enabled = True

        try:
            validate_gpt_oss_install()
            fromgpt_oss.tools.python_docker.docker_toolimport PythonTool
        except ImportError as e:
            self.enabled = False
            logger.warning_once(
                "gpt_oss is not installed properly (%s), code interpreter is disabled",
                e,
            )
            return

        self.python_tool = PythonTool()

    async defvalidate(self):
        if not self.enabled:
            return
        try:
            message = Message(
                author=Author(role=Role.ASSISTANT),
                content=[TextContent(text="print('Hello, world!')")],
                channel="analysis",
                recipient="python",
                content_type="code",
            )
            msgs = []
            async for msg in self.python_tool.process(message):
                msgs.append(msg)
            assert msgs[0].content[0].text == "Hello, world!\n"
        except Exception as e:
            self.enabled = False
            logger.warning_once(
                "Code interpreter tool failed to initialize (%s), code "
                "interpreter is disabled",
                e,
            )
            return
        logger.info_once("Code interpreter tool initialized")

    async defget_result(self, context: "ConversationContext") -> Any:
        fromvllm.entrypoints.openai.responses.contextimport HarmonyContext

        assert isinstance(context, HarmonyContext)
        last_msg = context.messages[-1]
        tool_output_msgs = []
        async for msg in self.python_tool.process(last_msg):
            tool_output_msgs.append(msg)
        return tool_output_msgs

    async defget_result_parsable_context(self, context: "ConversationContext") -> Any:
"""
        This function converts parsable context types to harmony and
        back so we can use GPTOSS demo python tool
        """
        fromvllm.entrypoints.openai.responses.contextimport ParsableContext

        assert isinstance(context, ParsableContext)

        last_msg = context.parser.response_messages[-1]
        args = json.loads(last_msg.arguments)

        last_msg_harmony = Message(
            author=Author(role="assistant", name=None),
            content=[TextContent(text=args["code"])],
            channel="analysis",
            recipient="python",
            content_type="code",
        )

        tool_output_msgs = []
        async for msg in self.python_tool.process(last_msg_harmony):
            processed = ResponseFunctionToolCallOutputItem(
                id=f"fco_{random_uuid()}",
                type="function_call_output",
                call_id=f"call_{random_uuid()}",
                output=msg.content[0].text,
                status="completed",
            )
            tool_output_msgs.append(processed)
        return tool_output_msgs

    @property
    deftool_config(self) -> Any:
        return self.python_tool.tool_config
```

### get\_result\_parsable\_context `async` [¶](#vllm.entrypoints.mcp.tool.HarmonyPythonTool.get_result_parsable_context "Permanent link")

```
get_result_parsable_context(
    context: ConversationContext,
) -> Any
```

This function converts parsable context types to harmony and back so we can use GPTOSS demo python tool

Source code in `vllm/entrypoints/mcp/tool.py`

```
async defget_result_parsable_context(self, context: "ConversationContext") -> Any:
"""
    This function converts parsable context types to harmony and
    back so we can use GPTOSS demo python tool
    """
    fromvllm.entrypoints.openai.responses.contextimport ParsableContext

    assert isinstance(context, ParsableContext)

    last_msg = context.parser.response_messages[-1]
    args = json.loads(last_msg.arguments)

    last_msg_harmony = Message(
        author=Author(role="assistant", name=None),
        content=[TextContent(text=args["code"])],
        channel="analysis",
        recipient="python",
        content_type="code",
    )

    tool_output_msgs = []
    async for msg in self.python_tool.process(last_msg_harmony):
        processed = ResponseFunctionToolCallOutputItem(
            id=f"fco_{random_uuid()}",
            type="function_call_output",
            call_id=f"call_{random_uuid()}",
            output=msg.content[0].text,
            status="completed",
        )
        tool_output_msgs.append(processed)
    return tool_output_msgs
```

## validate\_gpt\_oss\_install [¶](#vllm.entrypoints.mcp.tool.validate_gpt_oss_install "Permanent link")

```
validate_gpt_oss_install()
```

Check if the gpt-oss is installed and its version is at least 0.0.7. If not, raise an ImportError.

Source code in `vllm/entrypoints/mcp/tool.py`

```
defvalidate_gpt_oss_install():
"""
    Check if the gpt-oss is installed and its version is at least 0.0.7.
    If not, raise an ImportError.
    """
    fromimportlib.metadataimport PackageNotFoundError, version

    frompackaging.versionimport InvalidVersion, Version

    try:
        pkg_version_str = version("gpt_oss")
        pkg_version = Version(pkg_version_str)
    except PackageNotFoundError:
        raise ImportError("Package 'gpt_oss' is not installed.") fromNone
    except InvalidVersion as e:
        raise ImportError(f"Invalid version string for 'gpt_oss': {e}") fromNone

    if pkg_version < Version(MIN_GPT_OSS_VERSION):
        raise ImportError(
            f"gpt_oss >= {MIN_GPT_OSS_VERSION} is required, "
            f"but {pkg_version} is installed."
        ) fromNone
```