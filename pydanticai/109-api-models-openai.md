---
title: pydantic_ai.models.openai - Pydantic AI
url: https://ai.pydantic.dev/api/models/openai/
source: sitemap
fetched_at: 2026-01-22T22:24:36.807767355-03:00
rendered_js: false
word_count: 68
summary: This document defines a Python class for interacting with the OpenAI Responses API, providing support for both standard and streamed requests along with built-in tool integration.
tags:
    - openai-api
    - python-sdk
    - llm-integration
    - async-io
    - openai-responses
category: api
---

```
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
1681
1682
1683
1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
1758
1759
1760
1761
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
1789
1790
1791
1792
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
1815
1816
1817
1818
1819
1820
1821
1822
1823
1824
1825
1826
1827
1828
1829
1830
1831
1832
1833
1834
1835
1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
1848
1849
1850
1851
1852
1853
1854
1855
1856
1857
1858
1859
1860
1861
1862
1863
1864
1865
1866
1867
1868
1869
1870
1871
1872
1873
1874
1875
1876
1877
1878
1879
1880
1881
1882
1883
1884
1885
1886
1887
1888
1889
1890
1891
1892
1893
1894
1895
1896
1897
1898
1899
1900
1901
1902
1903
1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
1914
1915
1916
1917
1918
1919
1920
1921
1922
1923
1924
1925
1926
1927
1928
1929
1930
1931
1932
1933
1934
1935
1936
1937
1938
1939
1940
1941
1942
1943
1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029
2030
2031
2032
2033
2034
2035
2036
2037
2038
2039
2040
2041
2042
2043
2044
2045
2046
2047
2048
2049
2050
2051
2052
```

```
@dataclass(init=False)
classOpenAIResponsesModel(Model):
"""A model that uses the OpenAI Responses API.

    The [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses) is the
    new API for OpenAI models.

    If you are interested in the differences between the Responses API and the Chat Completions API,
    see the [OpenAI API docs](https://platform.openai.com/docs/guides/responses-vs-chat-completions).
    """

    client: AsyncOpenAI = field(repr=False)

    _model_name: OpenAIModelName = field(repr=False)
    _provider: Provider[AsyncOpenAI] = field(repr=False)

    def__init__(
        self,
        model_name: OpenAIModelName,
        *,
        provider: OpenAIResponsesCompatibleProvider
        | Literal[
            'openai',
            'gateway',
        ]
        | Provider[AsyncOpenAI] = 'openai',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Initialize an OpenAI Responses model.

        Args:
            model_name: The name of the OpenAI model to use.
            provider: The provider to use. Defaults to `'openai'`.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            settings: Default model settings for this model instance.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider('gateway/openai' if provider == 'gateway' else provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    defbase_url(self) -> str:
        return str(self.client.base_url)

    @property
    defmodel_name(self) -> OpenAIModelName:
"""The model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The model provider."""
        return self._provider.name

    @classmethod
    defsupported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
"""Return the set of builtin tool types this model can handle."""
        return frozenset({WebSearchTool, CodeExecutionTool, FileSearchTool, MCPServerTool, ImageGenerationTool})

    async defrequest(
        self,
        messages: list[ModelRequest | ModelResponse],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._responses_create(
            messages, False, cast(OpenAIResponsesModelSettings, model_settings or {}), model_request_parameters
        )

        # Handle ModelResponse
        if isinstance(response, ModelResponse):
            return response

        return self._process_response(response, model_request_parameters)

    @asynccontextmanager
    async defrequest_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._responses_create(
            messages, True, cast(OpenAIResponsesModelSettings, model_settings or {}), model_request_parameters
        )
        async with response:
            yield await self._process_streamed_response(response, model_request_parameters)

    def_process_response(  # noqa: C901
        self, response: responses.Response, model_request_parameters: ModelRequestParameters
    ) -> ModelResponse:
"""Process a non-streamed response, and prepare a message to return."""
        items: list[ModelResponsePart] = []
        for item in response.output:
            if isinstance(item, responses.ResponseReasoningItem):
                signature = item.encrypted_content
                # Handle raw CoT content from gpt-oss models
                provider_details: dict[str, Any] = {}
                raw_content: list[str] | None = [c.text for c in item.content] if item.content else None
                if raw_content:
                    provider_details['raw_content'] = raw_content

                if item.summary:
                    for summary in item.summary:
                        # We use the same id for all summaries so that we can merge them on the round trip.
                        items.append(
                            ThinkingPart(
                                content=summary.text,
                                id=item.id,
                                signature=signature,
                                provider_name=self.system if (signature or provider_details) else None,
                                provider_details=provider_details or None,
                            )
                        )
                        # We only need to store the signature and raw_content once.
                        signature = None
                        provider_details = None
                elif signature or provider_details:
                    items.append(
                        ThinkingPart(
                            content='',
                            id=item.id,
                            signature=signature,
                            provider_name=self.system if (signature or provider_details) else None,
                            provider_details=provider_details or None,
                        )
                    )
            elif isinstance(item, responses.ResponseOutputMessage):
                for content in item.content:
                    if isinstance(content, responses.ResponseOutputText):  # pragma: no branch
                        part_provider_details: dict[str, Any] | None = None
                        if content.logprobs:
                            part_provider_details = {'logprobs': _map_logprobs(content.logprobs)}
                        items.append(TextPart(content.text, id=item.id, provider_details=part_provider_details))
            elif isinstance(item, responses.ResponseFunctionToolCall):
                items.append(
                    ToolCallPart(
                        item.name,
                        item.arguments,
                        tool_call_id=item.call_id,
                        id=item.id,
                    )
                )
            elif isinstance(item, responses.ResponseCodeInterpreterToolCall):
                call_part, return_part, file_parts = _map_code_interpreter_tool_call(item, self.system)
                items.append(call_part)
                if file_parts:
                    items.extend(file_parts)
                items.append(return_part)
            elif isinstance(item, responses.ResponseFunctionWebSearch):
                call_part, return_part = _map_web_search_tool_call(item, self.system)
                items.append(call_part)
                items.append(return_part)
            elif isinstance(item, responses.response_output_item.ImageGenerationCall):
                call_part, return_part, file_part = _map_image_generation_tool_call(item, self.system)
                items.append(call_part)
                if file_part:  # pragma: no branch
                    items.append(file_part)
                items.append(return_part)
            elif isinstance(item, responses.ResponseComputerToolCall):  # pragma: no cover
                # Pydantic AI doesn't yet support the ComputerUse built-in tool
                pass
            elif isinstance(item, responses.ResponseCustomToolCall):  # pragma: no cover
                # Support is being implemented in https://github.com/pydantic/pydantic-ai/pull/2572
                pass
            elif isinstance(item, responses.response_output_item.LocalShellCall):  # pragma: no cover
                # Pydantic AI doesn't yet support the `codex-mini-latest` LocalShell built-in tool
                pass
            elif isinstance(item, responses.ResponseFileSearchToolCall):
                call_part, return_part = _map_file_search_tool_call(item, self.system)
                items.append(call_part)
                items.append(return_part)
            elif isinstance(item, responses.response_output_item.McpCall):
                call_part, return_part = _map_mcp_call(item, self.system)
                items.append(call_part)
                items.append(return_part)
            elif isinstance(item, responses.response_output_item.McpListTools):
                call_part, return_part = _map_mcp_list_tools(item, self.system)
                items.append(call_part)
                items.append(return_part)
            elif isinstance(item, responses.response_output_item.McpApprovalRequest):  # pragma: no cover
                # Pydantic AI doesn't yet support McpApprovalRequest (explicit tool usage approval)
                pass

        finish_reason: FinishReason | None = None
        provider_details: dict[str, Any] = {}
        raw_finish_reason = details.reason if (details := response.incomplete_details) else response.status
        if raw_finish_reason:
            provider_details['finish_reason'] = raw_finish_reason
            finish_reason = _RESPONSES_FINISH_REASON_MAP.get(raw_finish_reason)
        if response.created_at:  # pragma: no branch
            provider_details['timestamp'] = number_to_datetime(response.created_at)

        return ModelResponse(
            parts=items,
            usage=_map_usage(response, self._provider.name, self._provider.base_url, self.model_name),
            model_name=response.model,
            provider_response_id=response.id,
            timestamp=_now_utc(),
            provider_name=self._provider.name,
            provider_url=self._provider.base_url,
            finish_reason=finish_reason,
            provider_details=provider_details or None,
        )

    async def_process_streamed_response(
        self,
        response: AsyncStream[responses.ResponseStreamEvent],
        model_request_parameters: ModelRequestParameters,
    ) -> OpenAIResponsesStreamedResponse:
"""Process a streamed response, and prepare a streaming response to return."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):  # pragma: no cover
            raise UnexpectedModelBehavior('Streamed response ended without content or tool calls')

        assert isinstance(first_chunk, responses.ResponseCreatedEvent)
        return OpenAIResponsesStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=first_chunk.response.model,
            _response=peekable_response,
            _provider_name=self._provider.name,
            _provider_url=self._provider.base_url,
            _provider_timestamp=number_to_datetime(first_chunk.response.created_at)
            if first_chunk.response.created_at
            else None,
        )

    @overload
    async def_responses_create(
        self,
        messages: list[ModelRequest | ModelResponse],
        stream: Literal[False],
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> responses.Response: ...

    @overload
    async def_responses_create(
        self,
        messages: list[ModelRequest | ModelResponse],
        stream: Literal[True],
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncStream[responses.ResponseStreamEvent]: ...

    async def_responses_create(  # noqa: C901
        self,
        messages: list[ModelRequest | ModelResponse],
        stream: bool,
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> responses.Response | AsyncStream[responses.ResponseStreamEvent] | ModelResponse:
        tools = (
            self._get_builtin_tools(model_request_parameters)
            + list(model_settings.get('openai_builtin_tools', []))
            + self._get_tools(model_request_parameters)
        )
        profile = OpenAIModelProfile.from_profile(self.profile)
        if not tools:
            tool_choice: Literal['none', 'required', 'auto'] | None = None
        elif not model_request_parameters.allow_text_output and profile.openai_supports_tool_choice_required:
            tool_choice = 'required'
        else:
            tool_choice = 'auto'

        previous_response_id = model_settings.get('openai_previous_response_id')
        if previous_response_id == 'auto':
            previous_response_id, messages = self._get_previous_response_id_and_new_messages(messages)

        instructions, openai_messages = await self._map_messages(messages, model_settings, model_request_parameters)
        reasoning = self._get_reasoning(model_settings)

        text: responses.ResponseTextConfigParam | None = None
        if model_request_parameters.output_mode == 'native':
            output_object = model_request_parameters.output_object
            assert output_object is not None
            text = {'format': self._map_json_schema(output_object)}
        elif (
            model_request_parameters.output_mode == 'prompted' and self.profile.supports_json_object_output
        ):  # pragma: no branch
            text = {'format': {'type': 'json_object'}}

            # Without this trick, we'd hit this error:
            # > Response input messages must contain the word 'json' in some form to use 'text.format' of type 'json_object'.
            # Apparently they're only checking input messages for "JSON", not instructions.
            assert isinstance(instructions, str)
            system_prompt_count = sum(1 for m in openai_messages if m.get('role') == 'system')
            openai_messages.insert(
                system_prompt_count, responses.EasyInputMessageParam(role='system', content=instructions)
            )
            instructions = OMIT

        if verbosity := model_settings.get('openai_text_verbosity'):
            text = text or {}
            text['verbosity'] = verbosity

        unsupported_model_settings = profile.openai_unsupported_model_settings
        for setting in unsupported_model_settings:
            model_settings.pop(setting, None)

        include: list[responses.ResponseIncludable] = []
        if profile.openai_supports_encrypted_reasoning_content:
            include.append('reasoning.encrypted_content')
        if model_settings.get('openai_include_code_execution_outputs'):
            include.append('code_interpreter_call.outputs')
        if model_settings.get('openai_include_web_search_sources'):
            include.append('web_search_call.action.sources')
        if model_settings.get('openai_include_file_search_results'):
            include.append('file_search_call.results')
        if model_settings.get('openai_logprobs'):
            include.append('message.output_text.logprobs')

        # When there are no input messages and we're not reusing a previous response,
        # the OpenAI API will reject a request without any input,
        # even if there are instructions.
        # To avoid this provide an explicit empty user message.
        if not openai_messages and not previous_response_id:
            openai_messages.append(
                responses.EasyInputMessageParam(
                    role='user',
                    content='',
                )
            )

        try:
            extra_headers = model_settings.get('extra_headers', {})
            extra_headers.setdefault('User-Agent', get_user_agent())
            return await self.client.responses.create(
                input=openai_messages,
                model=self.model_name,
                instructions=instructions,
                parallel_tool_calls=model_settings.get('parallel_tool_calls', OMIT),
                tools=tools or OMIT,
                tool_choice=tool_choice or OMIT,
                max_output_tokens=model_settings.get('max_tokens', OMIT),
                stream=stream,
                temperature=model_settings.get('temperature', OMIT),
                top_p=model_settings.get('top_p', OMIT),
                truncation=model_settings.get('openai_truncation', OMIT),
                timeout=model_settings.get('timeout', NOT_GIVEN),
                service_tier=model_settings.get('openai_service_tier', OMIT),
                previous_response_id=previous_response_id or OMIT,
                top_logprobs=model_settings.get('openai_top_logprobs', OMIT),
                reasoning=reasoning,
                user=model_settings.get('openai_user', OMIT),
                text=text or OMIT,
                include=include or OMIT,
                prompt_cache_key=model_settings.get('openai_prompt_cache_key', OMIT),
                prompt_cache_retention=model_settings.get('openai_prompt_cache_retention', OMIT),
                extra_headers=extra_headers,
                extra_body=model_settings.get('extra_body'),
            )
        except APIStatusError as e:
            if model_response := _check_azure_content_filter(e, self.system, self.model_name):
                return model_response

            if (status_code := e.status_code) >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) frome
            raise  # pragma: lax no cover
        except APIConnectionError as e:
            raise ModelAPIError(model_name=self.model_name, message=e.message) frome

    def_get_reasoning(self, model_settings: OpenAIResponsesModelSettings) -> Reasoning | Omit:
        reasoning_effort = model_settings.get('openai_reasoning_effort', None)
        reasoning_summary = model_settings.get('openai_reasoning_summary', None)
        reasoning_generate_summary = model_settings.get('openai_reasoning_generate_summary', None)

        if reasoning_summary and reasoning_generate_summary:  # pragma: no cover
            raise ValueError('`openai_reasoning_summary` and `openai_reasoning_generate_summary` cannot both be set.')

        if reasoning_generate_summary is not None:  # pragma: no cover
            warnings.warn(
                '`openai_reasoning_generate_summary` is deprecated, use `openai_reasoning_summary` instead',
                DeprecationWarning,
            )
            reasoning_summary = reasoning_generate_summary

        reasoning: Reasoning = {}
        if reasoning_effort:
            reasoning['effort'] = reasoning_effort
        if reasoning_summary:
            reasoning['summary'] = reasoning_summary
        return reasoning or OMIT

    def_get_tools(self, model_request_parameters: ModelRequestParameters) -> list[responses.FunctionToolParam]:
        return [self._map_tool_definition(r) for r in model_request_parameters.tool_defs.values()]

    def_get_builtin_tools(self, model_request_parameters: ModelRequestParameters) -> list[responses.ToolParam]:
        tools: list[responses.ToolParam] = []
        has_image_generating_tool = False
        for tool in model_request_parameters.builtin_tools:
            if isinstance(tool, WebSearchTool):
                web_search_tool = responses.WebSearchToolParam(
                    type='web_search', search_context_size=tool.search_context_size
                )
                if tool.user_location:
                    web_search_tool['user_location'] = responses.web_search_tool_param.UserLocation(
                        type='approximate', **tool.user_location
                    )
                tools.append(web_search_tool)
            elif isinstance(tool, FileSearchTool):
                file_search_tool = cast(
                    responses.FileSearchToolParam,
                    {'type': 'file_search', 'vector_store_ids': list(tool.file_store_ids)},
                )
                tools.append(file_search_tool)
            elif isinstance(tool, CodeExecutionTool):
                has_image_generating_tool = True
                tools.append({'type': 'code_interpreter', 'container': {'type': 'auto'}})
            elif isinstance(tool, MCPServerTool):
                mcp_tool = responses.tool_param.Mcp(
                    type='mcp',
                    server_label=tool.id,
                    require_approval='never',
                )

                if tool.authorization_token:  # pragma: no branch
                    mcp_tool['authorization'] = tool.authorization_token

                if tool.allowed_tools is not None:  # pragma: no branch
                    mcp_tool['allowed_tools'] = tool.allowed_tools

                if tool.description:  # pragma: no branch
                    mcp_tool['server_description'] = tool.description

                if tool.headers:  # pragma: no branch
                    mcp_tool['headers'] = tool.headers

                if tool.url.startswith(MCP_SERVER_TOOL_CONNECTOR_URI_SCHEME + ':'):
                    _, connector_id = tool.url.split(':', maxsplit=1)
                    mcp_tool['connector_id'] = connector_id  # pyright: ignore[reportGeneralTypeIssues]
                else:
                    mcp_tool['server_url'] = tool.url

                tools.append(mcp_tool)
            elif isinstance(tool, ImageGenerationTool):  # pragma: no branch
                has_image_generating_tool = True
                size = _resolve_openai_image_generation_size(tool)
                output_compression = tool.output_compression if tool.output_compression is not None else 100
                tools.append(
                    responses.tool_param.ImageGeneration(
                        type='image_generation',
                        background=tool.background,
                        input_fidelity=tool.input_fidelity,
                        moderation=tool.moderation,
                        output_compression=output_compression,
                        output_format=tool.output_format or 'png',
                        partial_images=tool.partial_images,
                        quality=tool.quality,
                        size=size,
                    )
                )
            else:
                raise UserError(  # pragma: no cover
                    f'`{tool.__class__.__name__}` is not supported by `OpenAIResponsesModel`. If it should be, please file an issue.'
                )

        if model_request_parameters.allow_image_output and not has_image_generating_tool:
            tools.append({'type': 'image_generation'})
        return tools

    def_map_tool_definition(self, f: ToolDefinition) -> responses.FunctionToolParam:
        return {
            'name': f.name,
            'parameters': f.parameters_json_schema,
            'type': 'function',
            'description': f.description,
            'strict': bool(
                f.strict and OpenAIModelProfile.from_profile(self.profile).openai_supports_strict_tool_definition
            ),
        }

    def_get_previous_response_id_and_new_messages(
        self, messages: list[ModelMessage]
    ) -> tuple[str | None, list[ModelMessage]]:
        # When `openai_previous_response_id` is set to 'auto', the most recent
        # `provider_response_id` from the message history is selected and all
        # earlier messages are omitted. This allows the OpenAI SDK to reuse
        # server-side history for efficiency. The returned tuple contains the
        # `previous_response_id` (if found) and the trimmed list of messages.
        previous_response_id = None
        trimmed_messages: list[ModelMessage] = []
        for m in reversed(messages):
            if isinstance(m, ModelResponse) and m.provider_name == self.system:
                previous_response_id = m.provider_response_id
                break
            else:
                trimmed_messages.append(m)

        if previous_response_id and trimmed_messages:
            return previous_response_id, list(reversed(trimmed_messages))
        else:
            return None, messages

    async def_map_messages(  # noqa: C901
        self,
        messages: list[ModelMessage],
        model_settings: OpenAIResponsesModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[str | Omit, list[responses.ResponseInputItemParam]]:
"""Maps a `pydantic_ai.Message` to a `openai.types.responses.ResponseInputParam` i.e. the OpenAI Responses API input format.

        For `ThinkingParts`, this method:
        - Sends `signature` back as `encrypted_content` (for official OpenAI reasoning)
        - Sends `content` back as `summary` text
        - Sends `provider_details['raw_content']` back as `content` items (for gpt-oss raw CoT)

        Raw CoT is sent back to improve model performance in multi-turn conversations.
        """
        profile = OpenAIModelProfile.from_profile(self.profile)
        send_item_ids = model_settings.get(
            'openai_send_reasoning_ids', profile.openai_supports_encrypted_reasoning_content
        )

        openai_messages: list[responses.ResponseInputItemParam] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                for part in message.parts:
                    if isinstance(part, SystemPromptPart):
                        openai_messages.append(responses.EasyInputMessageParam(role='system', content=part.content))
                    elif isinstance(part, UserPromptPart):
                        openai_messages.append(await self._map_user_prompt(part))
                    elif isinstance(part, ToolReturnPart):
                        call_id = _guard_tool_call_id(t=part)
                        call_id, _ = _split_combined_tool_call_id(call_id)
                        item = FunctionCallOutput(
                            type='function_call_output',
                            call_id=call_id,
                            output=part.model_response_str(),
                        )
                        openai_messages.append(item)
                    elif isinstance(part, RetryPromptPart):
                        if part.tool_name is None:
                            openai_messages.append(
                                Message(role='user', content=[{'type': 'input_text', 'text': part.model_response()}])
                            )
                        else:
                            call_id = _guard_tool_call_id(t=part)
                            call_id, _ = _split_combined_tool_call_id(call_id)
                            item = FunctionCallOutput(
                                type='function_call_output',
                                call_id=call_id,
                                output=part.model_response(),
                            )
                            openai_messages.append(item)
                    else:
                        assert_never(part)
            elif isinstance(message, ModelResponse):
                send_item_ids = send_item_ids and message.provider_name == self.system

                message_item: responses.ResponseOutputMessageParam | None = None
                reasoning_item: responses.ResponseReasoningItemParam | None = None
                web_search_item: responses.ResponseFunctionWebSearchParam | None = None
                file_search_item: responses.ResponseFileSearchToolCallParam | None = None
                code_interpreter_item: responses.ResponseCodeInterpreterToolCallParam | None = None
                for item in message.parts:
                    if isinstance(item, TextPart):
                        if item.id and send_item_ids:
                            if message_item is None or message_item['id'] != item.id:  # pragma: no branch
                                message_item = responses.ResponseOutputMessageParam(
                                    role='assistant',
                                    id=item.id,
                                    content=[],
                                    type='message',
                                    status='completed',
                                )
                                openai_messages.append(message_item)

                            message_item['content'] = [
                                *message_item['content'],
                                responses.ResponseOutputTextParam(
                                    text=item.content, type='output_text', annotations=[]
                                ),
                            ]
                        else:
                            openai_messages.append(
                                responses.EasyInputMessageParam(role='assistant', content=item.content)
                            )
                    elif isinstance(item, ToolCallPart):
                        call_id = _guard_tool_call_id(t=item)
                        call_id, id = _split_combined_tool_call_id(call_id)
                        id = id or item.id

                        param = responses.ResponseFunctionToolCallParam(
                            name=item.tool_name,
                            arguments=item.args_as_json_str(),
                            call_id=call_id,
                            type='function_call',
                        )
                        if profile.openai_responses_requires_function_call_status_none:
                            param['status'] = None  # type: ignore[reportGeneralTypeIssues]
                        if id and send_item_ids:  # pragma: no branch
                            param['id'] = id
                        openai_messages.append(param)
                    elif isinstance(item, BuiltinToolCallPart):
                        if item.provider_name == self.system and send_item_ids:  # pragma: no branch
                            if (
                                item.tool_name == CodeExecutionTool.kind
                                and item.tool_call_id
                                and (args := item.args_as_dict())
                                and (container_id := args.get('container_id'))
                            ):
                                code_interpreter_item = responses.ResponseCodeInterpreterToolCallParam(
                                    id=item.tool_call_id,
                                    code=args.get('code'),
                                    container_id=container_id,
                                    outputs=None,  # These can be read server-side
                                    status='completed',
                                    type='code_interpreter_call',
                                )
                                openai_messages.append(code_interpreter_item)
                            elif (
                                item.tool_name == WebSearchTool.kind
                                and item.tool_call_id
                                and (args := item.args_as_dict())
                            ):
                                # We need to exclude None values because of https://github.com/pydantic/pydantic-ai/issues/3653
                                args = {k: v for k, v in args.items() if v is not None}
                                web_search_item = responses.ResponseFunctionWebSearchParam(
                                    id=item.tool_call_id,
                                    action=cast(responses.response_function_web_search_param.Action, args),
                                    status='completed',
                                    type='web_search_call',
                                )
                                openai_messages.append(web_search_item)
                            elif (  # pragma: no cover
                                item.tool_name == FileSearchTool.kind
                                and item.tool_call_id
                                and (args := item.args_as_dict())
                            ):
                                file_search_item = cast(
                                    responses.ResponseFileSearchToolCallParam,
                                    {
                                        'id': item.tool_call_id,
                                        'queries': args.get('queries', []),
                                        'status': 'completed',
                                        'type': 'file_search_call',
                                    },
                                )
                                openai_messages.append(file_search_item)
                            elif item.tool_name == ImageGenerationTool.kind and item.tool_call_id:
                                # The cast is necessary because of https://github.com/openai/openai-python/issues/2648
                                image_generation_item = cast(
                                    responses.response_input_item_param.ImageGenerationCall,
                                    {
                                        'id': item.tool_call_id,
                                        'type': 'image_generation_call',
                                    },
                                )
                                openai_messages.append(image_generation_item)
                            elif (  # pragma: no branch
                                item.tool_name.startswith(MCPServerTool.kind)
                                and item.tool_call_id
                                and (server_id := item.tool_name.split(':', 1)[1])
                                and (args := item.args_as_dict())
                                and (action := args.get('action'))
                            ):
                                if action == 'list_tools':
                                    mcp_list_tools_item = responses.response_input_item_param.McpListTools(
                                        id=item.tool_call_id,
                                        type='mcp_list_tools',
                                        server_label=server_id,
                                        tools=[],  # These can be read server-side
                                    )
                                    openai_messages.append(mcp_list_tools_item)
                                elif (  # pragma: no branch
                                    action == 'call_tool'
                                    and (tool_name := args.get('tool_name'))
                                    and (tool_args := args.get('tool_args'))
                                ):
                                    mcp_call_item = responses.response_input_item_param.McpCall(
                                        id=item.tool_call_id,
                                        server_label=server_id,
                                        name=tool_name,
                                        arguments=to_json(tool_args).decode(),
                                        error=None,  # These can be read server-side
                                        output=None,  # These can be read server-side
                                        type='mcp_call',
                                    )
                                    openai_messages.append(mcp_call_item)

                    elif isinstance(item, BuiltinToolReturnPart):
                        if item.provider_name == self.system and send_item_ids:  # pragma: no branch
                            content_is_dict = isinstance(item.content, dict)
                            status = item.content.get('status') if content_is_dict else None
                            kind_to_item = {
                                CodeExecutionTool.kind: code_interpreter_item,
                                WebSearchTool.kind: web_search_item,
                                FileSearchTool.kind: file_search_item,
                            }
                            if status and (builtin_item := kind_to_item.get(item.tool_name)) is not None:
                                builtin_item['status'] = status
                            elif item.tool_name == ImageGenerationTool.kind:
                                # Image generation result does not need to be sent back, just the `id` off of `BuiltinToolCallPart`.
                                pass
                            elif item.tool_name.startswith(MCPServerTool.kind):  # pragma: no branch
                                # MCP call result does not need to be sent back, just the fields off of `BuiltinToolCallPart`.
                                pass
                    elif isinstance(item, FilePart):
                        # This was generated by the `ImageGenerationTool` or `CodeExecutionTool`,
                        # and does not need to be sent back separately from the corresponding `BuiltinToolReturnPart`.
                        # If `send_item_ids` is false, we won't send the `BuiltinToolReturnPart`, but OpenAI does not have a type for files from the assistant.
                        pass
                    elif isinstance(item, ThinkingPart):
                        # Get raw CoT content from provider_details if present and from this provider
                        raw_content: list[str] | None = None
                        if item.provider_name == self.system:
                            raw_content = (item.provider_details or {}).get('raw_content')

                        if item.id and (send_item_ids or raw_content):
                            signature: str | None = None
                            if (
                                item.signature
                                and item.provider_name == self.system
                                and profile.openai_supports_encrypted_reasoning_content
                            ):
                                signature = item.signature

                            if (reasoning_item is None or reasoning_item['id'] != item.id) and (
                                signature or item.content or raw_content
                            ):  # pragma: no branch
                                reasoning_item = responses.ResponseReasoningItemParam(
                                    id=item.id,
                                    summary=[],
                                    encrypted_content=signature,
                                    type='reasoning',
                                )
                                openai_messages.append(reasoning_item)

                            if item.content:
                                # The check above guarantees that `reasoning_item` is not None
                                assert reasoning_item is not None
                                reasoning_item['summary'] = [
                                    *reasoning_item['summary'],
                                    ReasoningSummary(text=item.content, type='summary_text'),
                                ]

                            if raw_content:
                                # Send raw CoT back
                                assert reasoning_item is not None
                                reasoning_item['content'] = [
                                    ReasoningContent(text=text, type='reasoning_text') for text in raw_content
                                ]
                        else:
                            start_tag, end_tag = profile.thinking_tags
                            openai_messages.append(
                                responses.EasyInputMessageParam(
                                    role='assistant', content='\n'.join([start_tag, item.content, end_tag])
                                )
                            )
                    else:
                        assert_never(item)
            else:
                assert_never(message)
        instructions = self._get_instructions(messages, model_request_parameters) or OMIT
        return instructions, openai_messages

    def_map_json_schema(self, o: OutputObjectDefinition) -> responses.ResponseFormatTextJSONSchemaConfigParam:
        response_format_param: responses.ResponseFormatTextJSONSchemaConfigParam = {
            'type': 'json_schema',
            'name': o.name or DEFAULT_OUTPUT_TOOL_NAME,
            'schema': o.json_schema,
        }
        if o.description:
            response_format_param['description'] = o.description
        if OpenAIModelProfile.from_profile(self.profile).openai_supports_strict_tool_definition:  # pragma: no branch
            response_format_param['strict'] = o.strict
        return response_format_param

    @staticmethod
    async def_map_user_prompt(part: UserPromptPart) -> responses.EasyInputMessageParam:  # noqa: C901
        content: str | list[responses.ResponseInputContentParam]
        if isinstance(part.content, str):
            content = part.content
        else:
            content = []
            for item in part.content:
                if isinstance(item, str):
                    content.append(responses.ResponseInputTextParam(text=item, type='input_text'))
                elif isinstance(item, BinaryContent):
                    if item.is_image:
                        detail: Literal['auto', 'low', 'high'] = 'auto'
                        if metadata := item.vendor_metadata:
                            detail = cast(
                                Literal['auto', 'low', 'high'],
                                metadata.get('detail', 'auto'),
                            )
                        content.append(
                            responses.ResponseInputImageParam(
                                image_url=item.data_uri,
                                type='input_image',
                                detail=detail,
                            )
                        )
                    elif item.is_document:
                        content.append(
                            responses.ResponseInputFileParam(
                                type='input_file',
                                file_data=item.data_uri,
                                # NOTE: Type wise it's not necessary to include the filename, but it's required by the
                                # API itself. If we add empty string, the server sends a 500 error - which OpenAI needs
                                # to fix. In any case, we add a placeholder name.
                                filename=f'filename.{item.format}',
                            )
                        )
                    elif item.is_audio:
                        raise NotImplementedError('Audio as binary content is not supported for OpenAI Responses API.')
                    else:  # pragma: no cover
                        raise RuntimeError(f'Unsupported binary content type: {item.media_type}')
                elif isinstance(item, ImageUrl):
                    detail: Literal['auto', 'low', 'high'] = 'auto'
                    image_url = item.url
                    if metadata := item.vendor_metadata:
                        detail = cast(Literal['auto', 'low', 'high'], metadata.get('detail', 'auto'))
                    if item.force_download:
                        downloaded_item = await download_item(item, data_format='base64_uri', type_format='extension')
                        image_url = downloaded_item['data']

                    content.append(
                        responses.ResponseInputImageParam(
                            image_url=image_url,
                            type='input_image',
                            detail=detail,
                        )
                    )
                elif isinstance(item, AudioUrl | DocumentUrl):
                    if item.force_download:
                        downloaded_item = await download_item(item, data_format='base64_uri', type_format='extension')
                        content.append(
                            responses.ResponseInputFileParam(
                                type='input_file',
                                file_data=downloaded_item['data'],
                                filename=f'filename.{downloaded_item["data_type"]}',
                            )
                        )
                    else:
                        content.append(
                            responses.ResponseInputFileParam(
                                type='input_file',
                                file_url=item.url,
                            )
                        )
                elif isinstance(item, VideoUrl):  # pragma: no cover
                    raise NotImplementedError('VideoUrl is not supported for OpenAI.')
                elif isinstance(item, CachePoint):
                    # OpenAI doesn't support prompt caching via CachePoint, so we filter it out
                    pass
                else:
                    assert_never(item)
        return responses.EasyInputMessageParam(role='user', content=content)
```