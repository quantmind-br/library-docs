---
title: parser_manager - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/parser/parser_manager/
source: sitemap
fetched_at: 2026-05-07T21:34:29.350248389-03:00
rendered_js: false
word_count: 50
summary: The ParserManager class provides a centralized registry for managing, importing, and retrieving parser implementations with support for both eager and lazy module loading.
tags:
    - registry-pattern
    - python-class
    - dynamic-loading
    - parser-implementation
    - dependency-injection
category: reference
---

```
classParserManager:
"""
    Central registry for Parser implementations.

    Supports two registration modes:
      - Eager registration via `register_module`
      - Lazy registration via `register_lazy_module`
    """

    parsers: dict[str, type[Parser]] = {}
    lazy_parsers: dict[str, tuple[str, str]] = {}  # name -> (module_path, class_name)

    @classmethod
    defget_parser_internal(cls, name: str) -> type[Parser]:
"""
        Retrieve a registered or lazily registered Parser class.

        Args:
            name: The registered name of the parser.

        Returns:
            The Parser class.

        Raises:
            KeyError: If no parser is found under the given name.
        """
        if name in cls.parsers:
            return cls.parsers[name]

        if name in cls.lazy_parsers:
            return cls._load_lazy_parser(name)

        registered = ", ".join(cls.list_registered())
        raise KeyError(f"Parser '{name}' not found. Available parsers: {registered}")

    @classmethod
    def_load_lazy_parser(cls, name: str) -> type[Parser]:
"""Import and register a lazily loaded parser."""
        fromvllm.parser.abstract_parserimport Parser

        module_path, class_name = cls.lazy_parsers[name]
        try:
            mod = importlib.import_module(module_path)
            parser_cls = getattr(mod, class_name)
            if not issubclass(parser_cls, Parser):
                raise TypeError(
                    f"{class_name} in {module_path} is not a Parser subclass."
                )
            cls.parsers[name] = parser_cls  # cache
            return parser_cls
        except Exception as e:
            logger.exception(
                "Failed to import lazy parser '%s' from %s: %s",
                name,
                module_path,
                e,
            )
            raise

    @classmethod
    def_register_module(
        cls,
        module: type[Parser],
        module_name: str | list[str] | None = None,
        force: bool = True,
    ) -> None:
"""Register a Parser class immediately."""
        fromvllm.parser.abstract_parserimport Parser

        if not issubclass(module, Parser):
            raise TypeError(
                f"module must be subclass of Parser, but got {type(module)}"
            )

        if module_name is None:
            module_names = [module.__name__]
        elif isinstance(module_name, str):
            module_names = [module_name]
        elif is_list_of(module_name, str):
            module_names = module_name
        else:
            raise TypeError("module_name must be str, list[str], or None.")

        for name in module_names:
            if not force and name in cls.parsers:
                existed = cls.parsers[name]
                raise KeyError(f"{name} is already registered at {existed.__module__}")
            cls.parsers[name] = module

    @classmethod
    defregister_lazy_module(cls, name: str, module_path: str, class_name: str) -> None:
"""
        Register a lazy module mapping for delayed import.

        Example:
            ParserManager.register_lazy_module(
                name="minimax_m2",
                module_path="vllm.parser.minimax_m2_parser",
                class_name="MiniMaxM2Parser",
            )
        """
        cls.lazy_parsers[name] = (module_path, class_name)

    @classmethod
    defregister_module(
        cls,
        name: str | list[str] | None = None,
        force: bool = True,
        module: type[Parser] | None = None,
    ) -> type[Parser] | Callable[[type[Parser]], type[Parser]]:
"""
        Register a Parser class.

        Can be used as a decorator or called directly.

        Usage:
            @ParserManager.register_module("my_parser")
            class MyParser(Parser):
                ...

        Or:
            ParserManager.register_module(module=MyParser)
        """
        if not isinstance(force, bool):
            raise TypeError(f"force must be a boolean, but got {type(force)}")

        # Immediate registration
        if module is not None:
            cls._register_module(module=module, module_name=name, force=force)
            return module

        # Decorator usage
        def_decorator(obj: type[Parser]) -> type[Parser]:
            module_path = obj.__module__
            class_name = obj.__name__

            if isinstance(name, str):
                names = [name]
            elif is_list_of(name, str):
                names = name
            else:
                names = [class_name]

            for n in names:
                cls.lazy_parsers[n] = (module_path, class_name)

            return obj

        return _decorator

    @classmethod
    deflist_registered(cls) -> list[str]:
"""Return names of all registered parsers."""
        return sorted(set(cls.parsers.keys()) | set(cls.lazy_parsers.keys()))

    @classmethod
    defimport_parser(cls, plugin_path: str) -> None:
"""Import a user-defined parser from an arbitrary path."""
        module_name = os.path.splitext(os.path.basename(plugin_path))[0]
        try:
            import_from_path(module_name, plugin_path)
        except Exception:
            logger.exception(
                "Failed to load module '%s' from %s.", module_name, plugin_path
            )

    @classmethod
    defget_tool_parser(
        cls,
        tool_parser_name: str | None = None,
        enable_auto_tools: bool = False,
        model_name: str | None = None,
    ) -> type[ToolParser] | None:
"""Get the tool parser based on the name."""
        fromvllm.tool_parsersimport ToolParserManager

        parser: type[ToolParser] | None = None
        if not enable_auto_tools or tool_parser_name is None:
            return parser
        logger.info_once('"auto" tool choice has been enabled.')

        try:
            if (
                tool_parser_name == "pythonic"
                and model_name
                and model_name.startswith("meta-llama/Llama-3.2")
            ):
                logger.warning(
                    "Llama3.2 models may struggle to emit valid pythonic tool calls"
                )
            parser = ToolParserManager.get_tool_parser(tool_parser_name)
        except Exception as e:
            raise TypeError(
                "Error: --enable-auto-tool-choice requires "
                f"tool_parser:'{tool_parser_name}' which has not "
                "been registered"
            ) frome
        return parser

    @classmethod
    defget_reasoning_parser(
        cls,
        reasoning_parser_name: str | None,
    ) -> type[ReasoningParser] | None:
"""Get the reasoning parser based on the name."""
        fromvllm.reasoningimport ReasoningParserManager

        parser: type[ReasoningParser] | None = None
        if not reasoning_parser_name:
            return None
        try:
            parser = ReasoningParserManager.get_reasoning_parser(reasoning_parser_name)
            assert parser is not None
        except Exception as e:
            raise TypeError(f"{reasoning_parser_name=} has not been registered") frome
        return parser

    @classmethod
    defget_parser(
        cls,
        tool_parser_name: str | None = None,
        reasoning_parser_name: str | None = None,
        enable_auto_tools: bool = False,
        model_name: str | None = None,
    ) -> type[Parser] | None:
"""
        Get a unified Parser that handles both reasoning and tool parsing.

        This method checks if a unified Parser exists that can handle both
        reasoning extraction and tool call parsing. If no unified parser
        exists, it creates a DelegatingParser that wraps the individual
        reasoning and tool parsers.

        Args:
            tool_parser_name: The name of the tool parser.
            reasoning_parser_name: The name of the reasoning parser.
            enable_auto_tools: Whether auto tool choice is enabled.
            model_name: The model name for parser-specific warnings.

        Returns:
            A Parser class, or None if neither parser is specified.
        """
        fromvllm.parser.abstract_parserimport _WrappedParser

        if not tool_parser_name and not reasoning_parser_name:
            return None

        # Strategy 1: If both names match, check for a unified parser with that name
        if tool_parser_name and tool_parser_name == reasoning_parser_name:
            try:
                parser = cls.get_parser_internal(tool_parser_name)
                logger.info(
                    "Using unified parser '%s' for both reasoning and tool parsing.",
                    tool_parser_name,
                )
                return parser
            except KeyError:
                pass  # No unified parser with this name

        # Strategy 2: Check for parser with either name
        for name in [tool_parser_name, reasoning_parser_name]:
            if name:
                try:
                    parser = cls.get_parser_internal(name)
                    logger.info(
                        "Using unified parser '%s' for reasoning and tool parsing.",
                        name,
                    )
                    return parser
                except KeyError:
                    pass

        # Strategy 3: Create a DelegatingParser with the individual parser classes
        reasoning_parser_cls = cls.get_reasoning_parser(reasoning_parser_name)
        tool_parser_cls = cls.get_tool_parser(
            tool_parser_name, enable_auto_tools, model_name
        )

        if reasoning_parser_cls is None and tool_parser_cls is None:
            return None

        # Set the class-level attributes on the imported _WrappedParser
        _WrappedParser.reasoning_parser_cls = reasoning_parser_cls
        _WrappedParser.tool_parser_cls = tool_parser_cls

        return _WrappedParser
```