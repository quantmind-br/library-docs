---
title: pydantic_ai.messages - Pydantic AI
url: https://ai.pydantic.dev/api/messages/
source: sitemap
fetched_at: 2026-01-22T22:24:07.611682162-03:00
rendered_js: false
word_count: 207
summary: This document defines the ModelResponse data structure used to represent and manage LLM outputs, including text content, tool calls, media parts, and cost calculations.
tags:
    - llm-responses
    - pydantic-ai
    - api-reference
    - data-models
    - observability
    - cost-calculation
category: reference
---

```
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
```

```
@dataclass(repr=False)
classModelResponse:
"""A response from a model, e.g. a message from the model to the Pydantic AI app."""

    parts: Sequence[ModelResponsePart]
"""The parts of the model message."""

    _: KW_ONLY

    usage: RequestUsage = field(default_factory=RequestUsage)
"""Usage information for the request.

    This has a default to make tests easier, and to support loading old messages where usage will be missing.
    """

    model_name: str | None = None
"""The name of the model that generated the response."""

    timestamp: datetime = field(default_factory=_now_utc)
"""The timestamp when the response was received locally.

    This is always a high-precision local datetime. Provider-specific timestamps
    (if available) are stored in `provider_details['timestamp']`.
    """

    kind: Literal['response'] = 'response'
"""Message type identifier, this is available on all parts as a discriminator."""

    provider_name: str | None = None
"""The name of the LLM provider that generated the response."""

    provider_url: str | None = None
"""The base URL of the LLM provider that generated the response."""

    provider_details: Annotated[
        dict[str, Any] | None,
        # `vendor_details` is deprecated, but we still want to support deserializing model responses stored in a DB before the name was changed
        pydantic.Field(validation_alias=pydantic.AliasChoices('provider_details', 'vendor_details')),
    ] = None
"""Additional data returned by the provider that can't be mapped to standard fields."""

    provider_response_id: Annotated[
        str | None,
        # `vendor_id` is deprecated, but we still want to support deserializing model responses stored in a DB before the name was changed
        pydantic.Field(validation_alias=pydantic.AliasChoices('provider_response_id', 'vendor_id')),
    ] = None
"""request ID as specified by the model provider. This can be used to track the specific request to the model."""

    finish_reason: FinishReason | None = None
"""Reason the model finished generating the response, normalized to OpenTelemetry values."""

    run_id: str | None = None
"""The unique identifier of the agent run in which this message originated."""

    metadata: dict[str, Any] | None = None
"""Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    @property
    deftext(self) -> str | None:
"""Get the text in the response."""
        texts: list[str] = []
        last_part: ModelResponsePart | None = None
        for part in self.parts:
            if isinstance(part, TextPart):
                # Adjacent text parts should be joined together, but if there are parts in between
                # (like built-in tool calls) they should have newlines between them
                if isinstance(last_part, TextPart):
                    texts[-1] += part.content
                else:
                    texts.append(part.content)
            last_part = part
        if not texts:
            return None

        return '\n\n'.join(texts)

    @property
    defthinking(self) -> str | None:
"""Get the thinking in the response."""
        thinking_parts = [part.content for part in self.parts if isinstance(part, ThinkingPart)]
        if not thinking_parts:
            return None
        return '\n\n'.join(thinking_parts)

    @property
    deffiles(self) -> list[BinaryContent]:
"""Get the files in the response."""
        return [part.content for part in self.parts if isinstance(part, FilePart)]

    @property
    defimages(self) -> list[BinaryImage]:
"""Get the images in the response."""
        return [file for file in self.files if isinstance(file, BinaryImage)]

    @property
    deftool_calls(self) -> list[ToolCallPart]:
"""Get the tool calls in the response."""
        return [part for part in self.parts if isinstance(part, ToolCallPart)]

    @property
    defbuiltin_tool_calls(self) -> list[tuple[BuiltinToolCallPart, BuiltinToolReturnPart]]:
"""Get the builtin tool calls and results in the response."""
        calls = [part for part in self.parts if isinstance(part, BuiltinToolCallPart)]
        if not calls:
            return []
        returns_by_id = {part.tool_call_id: part for part in self.parts if isinstance(part, BuiltinToolReturnPart)}
        return [
            (call_part, returns_by_id[call_part.tool_call_id])
            for call_part in calls
            if call_part.tool_call_id in returns_by_id
        ]

    @deprecated('`price` is deprecated, use `cost` instead')
    defprice(self) -> genai_types.PriceCalculation:  # pragma: no cover
        return self.cost()

    defcost(self) -> genai_types.PriceCalculation:
"""Calculate the cost of the usage.

        Uses [`genai-prices`](https://github.com/pydantic/genai-prices).
        """
        assert self.model_name, 'Model name is required to calculate price'
        # Try matching on provider_api_url first as this is more specific, then fall back to provider_id.
        if self.provider_url:
            try:
                return calc_price(
                    self.usage,
                    self.model_name,
                    provider_api_url=self.provider_url,
                    genai_request_timestamp=self.timestamp,
                )
            except LookupError:
                pass
        return calc_price(
            self.usage,
            self.model_name,
            provider_id=self.provider_name,
            genai_request_timestamp=self.timestamp,
        )

    defotel_events(self, settings: InstrumentationSettings) -> list[LogRecord]:
"""Return OpenTelemetry events for the response."""
        result: list[LogRecord] = []

        defnew_event_body():
            new_body: dict[str, Any] = {'role': 'assistant'}
            ev = LogRecord(attributes={'event.name': 'gen_ai.assistant.message'}, body=new_body)
            result.append(ev)
            return new_body

        body = new_event_body()
        for part in self.parts:
            if isinstance(part, ToolCallPart):
                body.setdefault('tool_calls', []).append(
                    {
                        'id': part.tool_call_id,
                        'type': 'function',
                        'function': {
                            'name': part.tool_name,
                            **({'arguments': part.args} if settings.include_content else {}),
                        },
                    }
                )
            elif isinstance(part, TextPart | ThinkingPart):
                kind = part.part_kind
                body.setdefault('content', []).append(
                    {'kind': kind, **({'text': part.content} if settings.include_content else {})}
                )
            elif isinstance(part, FilePart):
                body.setdefault('content', []).append(
                    {
                        'kind': 'binary',
                        'media_type': part.content.media_type,
                        **(
                            {'binary_content': part.content.base64}
                            if settings.include_content and settings.include_binary_content
                            else {}
                        ),
                    }
                )

        if content := body.get('content'):
            text_content = content[0].get('text')
            if content == [{'kind': 'text', 'text': text_content}]:
                body['content'] = text_content

        return result

    defotel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        parts: list[_otel_messages.MessagePart] = []
        for part in self.parts:
            if isinstance(part, TextPart):
                parts.append(
                    _otel_messages.TextPart(
                        type='text',
                        **({'content': part.content} if settings.include_content else {}),
                    )
                )
            elif isinstance(part, ThinkingPart):
                parts.append(
                    _otel_messages.ThinkingPart(
                        type='thinking',
                        **({'content': part.content} if settings.include_content else {}),
                    )
                )
            elif isinstance(part, FilePart):
                converted_part = _otel_messages.BinaryDataPart(type='binary', media_type=part.content.media_type)
                if settings.include_content and settings.include_binary_content:
                    converted_part['content'] = part.content.base64
                parts.append(converted_part)
            elif isinstance(part, BaseToolCallPart):
                call_part = _otel_messages.ToolCallPart(type='tool_call', id=part.tool_call_id, name=part.tool_name)
                if isinstance(part, BuiltinToolCallPart):
                    call_part['builtin'] = True
                if settings.include_content and part.args is not None:
                    from.models.instrumentedimport InstrumentedModel

                    if isinstance(part.args, str):
                        call_part['arguments'] = part.args
                    else:
                        call_part['arguments'] = {k: InstrumentedModel.serialize_any(v) for k, v in part.args.items()}

                parts.append(call_part)
            elif isinstance(part, BuiltinToolReturnPart):
                return_part = _otel_messages.ToolCallResponsePart(
                    type='tool_call_response',
                    id=part.tool_call_id,
                    name=part.tool_name,
                    builtin=True,
                )
                if settings.include_content and part.content is not None:  # pragma: no branch
                    from.models.instrumentedimport InstrumentedModel

                    return_part['result'] = InstrumentedModel.serialize_any(part.content)

                parts.append(return_part)
        return parts

    @property
    @deprecated('`vendor_details` is deprecated, use `provider_details` instead')
    defvendor_details(self) -> dict[str, Any] | None:
        return self.provider_details

    @property
    @deprecated('`vendor_id` is deprecated, use `provider_response_id` instead')
    defvendor_id(self) -> str | None:
        return self.provider_response_id

    @property
    @deprecated('`provider_request_id` is deprecated, use `provider_response_id` instead')
    defprovider_request_id(self) -> str | None:
        return self.provider_response_id

    __repr__ = _utils.dataclasses_no_defaults_repr
```