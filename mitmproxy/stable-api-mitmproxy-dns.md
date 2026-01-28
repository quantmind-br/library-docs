---
title: mitmproxy.dns
url: https://docs.mitmproxy.org/stable/api/mitmproxy/dns.html
source: crawler
fetched_at: 2026-01-28T16:21:22.852128512-03:00
rendered_js: false
word_count: 46
summary: This document defines Python classes for representing DNS questions and resource records within the mitmproxy project, providing methods for object initialization, data manipulation, and serialization to/from JSON format for various DNS record types.
tags:
    - dns-question
    - dns-resource-record
    - mitmproxy
    - python-dataclasses
    - data-serialization
    - dns-record-types
    - ipv4-ipv6
    - https-records
category: api
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/dns.py) View Source

```
  1from__future__import annotations
  2
  3importbase64
  4importitertools
  5importrandom
  6importstruct
  7importtime
  8fromcollections.abcimport Iterable
  9fromdataclassesimport dataclass
 10fromipaddressimport IPv4Address
 11fromipaddressimport IPv6Address
 12fromtypingimport Any
 13fromtypingimport cast
 14fromtypingimport ClassVar
 15fromtypingimport Self
 16
 17frommitmproxyimport flow
 18frommitmproxy.coretypesimport serializable
 19frommitmproxy.net.dnsimport classes
 20frommitmproxy.net.dnsimport domain_names
 21frommitmproxy.net.dnsimport https_records
 22frommitmproxy.net.dnsimport op_codes
 23frommitmproxy.net.dnsimport response_codes
 24frommitmproxy.net.dnsimport types
 25frommitmproxy.net.dns.https_recordsimport HTTPSRecord
 26frommitmproxy.net.dns.https_recordsimport HTTPSRecordJSON
 27frommitmproxy.net.dns.https_recordsimport SVCParamKeys
 28
 29# DNS parameters taken from https://www.iana.org/assignments/dns-parameters/dns-parameters.xml
 30
 31
 32@dataclass
 33classQuestion(serializable.SerializableDataclass):
 34    HEADER: ClassVar[struct.Struct] = struct.Struct("!HH")
 35
 36    name: str
 37    type: int
 38    class_: int
 39
 40    def__str__(self) -> str:
 41        return self.name
 42
 43    defto_json(self) -> dict:
 44"""
 45        Converts the question into json for mitmweb.
 46        Sync with web/src/flow.ts.
 47        """
 48        return {
 49            "name": self.name,
 50            "type": types.to_str(self.type),
 51            "class": classes.to_str(self.class_),
 52        }
 53
 54    @classmethod
 55    deffrom_json(cls, data: dict[str, str]) -> Self:
 56        return cls(
 57            name=data["name"],
 58            type=types.from_str(data["type"]),
 59            class_=classes.from_str(data["class"]),
 60        )
 61
 62
 63@dataclass
 64classResourceRecord(serializable.SerializableDataclass):
 65    DEFAULT_TTL: ClassVar[int] = 60
 66    HEADER: ClassVar[struct.Struct] = struct.Struct("!HHIH")
 67
 68    name: str
 69    type: int
 70    class_: int
 71    ttl: int
 72    data: bytes
 73
 74    def__str__(self) -> str:
 75        return str(self._data_json())
 76
 77    @property
 78    deftext(self) -> str:
 79        return self.data.decode("utf-8")
 80
 81    @text.setter
 82    deftext(self, value: str) -> None:
 83        self.data = value.encode("utf-8")
 84
 85    @property
 86    defipv4_address(self) -> IPv4Address:
 87        return IPv4Address(self.data)
 88
 89    @ipv4_address.setter
 90    defipv4_address(self, ip: IPv4Address) -> None:
 91        self.data = ip.packed
 92
 93    @property
 94    defipv6_address(self) -> IPv6Address:
 95        return IPv6Address(self.data)
 96
 97    @ipv6_address.setter
 98    defipv6_address(self, ip: IPv6Address) -> None:
 99        self.data = ip.packed
100
101    @property
102    defdomain_name(self) -> str:
103        return domain_names.unpack(self.data)
104
105    @domain_name.setter
106    defdomain_name(self, name: str) -> None:
107        self.data = domain_names.pack(name)
108
109    @property
110    defhttps_alpn(self) -> tuple[bytes, ...] | None:
111        record = https_records.unpack(self.data)
112        alpn_bytes = record.params.get(SVCParamKeys.ALPN.value, None)
113        if alpn_bytes is not None:
114            i = 0
115            ret = []
116            while i < len(alpn_bytes):
117                token_len = alpn_bytes[i]
118                ret.append(alpn_bytes[i + 1 : i + 1 + token_len])
119                i += token_len + 1
120            return tuple(ret)
121        else:
122            return None
123
124    @https_alpn.setter
125    defhttps_alpn(self, alpn: Iterable[bytes] | None) -> None:
126        record = https_records.unpack(self.data)
127        if alpn is None:
128            record.params.pop(SVCParamKeys.ALPN.value, None)
129        else:
130            alpn_bytes = b"".join(bytes([len(a)]) + a for a in alpn)
131            record.params[SVCParamKeys.ALPN.value] = alpn_bytes
132        self.data = https_records.pack(record)
133
134    @property
135    defhttps_ech(self) -> str | None:
136        record = https_records.unpack(self.data)
137        ech_bytes = record.params.get(SVCParamKeys.ECH.value, None)
138        if ech_bytes is not None:
139            return base64.b64encode(ech_bytes).decode("utf-8")
140        else:
141            return None
142
143    @https_ech.setter
144    defhttps_ech(self, ech: str | None) -> None:
145        record = https_records.unpack(self.data)
146        if ech is None:
147            record.params.pop(SVCParamKeys.ECH.value, None)
148        else:
149            ech_bytes = base64.b64decode(ech.encode("utf-8"))
150            record.params[SVCParamKeys.ECH.value] = ech_bytes
151        self.data = https_records.pack(record)
152
153    def_data_json(self) -> str | HTTPSRecordJSON:
154        try:
155            match self.type:
156                case types.A:
157                    return str(self.ipv4_address)
158                case types.AAAA:
159                    return str(self.ipv6_address)
160                case types.NS | types.CNAME | types.PTR:
161                    return self.domain_name
162                case types.TXT:
163                    return self.text
164                case types.HTTPS:
165                    return https_records.unpack(self.data).to_json()
166                case_:
167                    return f"0x{self.data.hex()}"
168        except Exception:
169            return f"0x{self.data.hex()} (invalid {types.to_str(self.type)} data)"
170
171    defto_json(self) -> dict[str, str | int | HTTPSRecordJSON]:
172"""
173        Converts the resource record into json for mitmweb.
174        Sync with web/src/flow.ts.
175        """
176        return {
177            "name": self.name,
178            "type": types.to_str(self.type),
179            "class": classes.to_str(self.class_),
180            "ttl": self.ttl,
181            "data": self._data_json(),
182        }
183
184    @classmethod
185    deffrom_json(cls, data: dict[str, Any]) -> Self:
186        inst = cls(
187            name=data["name"],
188            type=types.from_str(data["type"]),
189            class_=classes.from_str(data["class"]),
190            ttl=data["ttl"],
191            data=b"",
192        )
193
194        d: str = data["data"]
195        try:
196            match inst.type:
197                case types.A:
198                    inst.ipv4_address = IPv4Address(d)
199                case types.AAAA:
200                    inst.ipv6_address = IPv6Address(d)
201                case types.NS | types.CNAME | types.PTR:
202                    inst.domain_name = d
203                case types.TXT:
204                    inst.text = d
205                case types.HTTPS:
206                    record = HTTPSRecord.from_json(cast(HTTPSRecordJSON, d))
207                    inst.data = https_records.pack(record)
208                case_:
209                    raise ValueError
210        except Exception:
211            inst.data = bytes.fromhex(d.removeprefix("0x").partition(" (")[0])
212
213        return inst
214
215    @classmethod
216    defA(cls, name: str, ip: IPv4Address, *, ttl: int = DEFAULT_TTL) -> ResourceRecord:
217"""Create an IPv4 resource record."""
218        return cls(name, types.A, classes.IN, ttl, ip.packed)
219
220    @classmethod
221    defAAAA(
222        cls, name: str, ip: IPv6Address, *, ttl: int = DEFAULT_TTL
223    ) -> ResourceRecord:
224"""Create an IPv6 resource record."""
225        return cls(name, types.AAAA, classes.IN, ttl, ip.packed)
226
227    @classmethod
228    defCNAME(
229        cls, alias: str, canonical: str, *, ttl: int = DEFAULT_TTL
230    ) -> ResourceRecord:
231"""Create a canonical internet name resource record."""
232        return cls(alias, types.CNAME, classes.IN, ttl, domain_names.pack(canonical))
233
234    @classmethod
235    defPTR(cls, inaddr: str, ptr: str, *, ttl: int = DEFAULT_TTL) -> ResourceRecord:
236"""Create a canonical internet name resource record."""
237        return cls(inaddr, types.PTR, classes.IN, ttl, domain_names.pack(ptr))
238
239    @classmethod
240    defTXT(cls, name: str, text: str, *, ttl: int = DEFAULT_TTL) -> ResourceRecord:
241"""Create a textual resource record."""
242        return cls(name, types.TXT, classes.IN, ttl, text.encode("utf-8"))
243
244    @classmethod
245    defHTTPS(
246        cls, name: str, record: HTTPSRecord, ttl: int = DEFAULT_TTL
247    ) -> ResourceRecord:
248"""Create a HTTPS resource record"""
249        return cls(name, types.HTTPS, classes.IN, ttl, https_records.pack(record))
250
251
252# comments are taken from rfc1035
253@dataclass
254classDNSMessage(serializable.SerializableDataclass):
255    HEADER: ClassVar[struct.Struct] = struct.Struct("!HHHHHH")
256
257    id: int
258"""An identifier assigned by the program that generates any kind of query."""
259    query: bool
260"""A field that specifies whether this message is a query."""
261    op_code: int
262"""
263    A field that specifies kind of query in this message.
264    This value is set by the originator of a request and copied into the response.
265    """
266    authoritative_answer: bool
267"""
268    This field is valid in responses, and specifies that the responding name server
269    is an authority for the domain name in question section.
270    """
271    truncation: bool
272"""Specifies that this message was truncated due to length greater than that permitted on the transmission channel."""
273    recursion_desired: bool
274"""
275    This field may be set in a query and is copied into the response.
276    If set, it directs the name server to pursue the query recursively.
277    """
278    recursion_available: bool
279"""This field is set or cleared in a response, and denotes whether recursive query support is available in the name server."""
280    reserved: int
281"""Reserved for future use.  Must be zero in all queries and responses."""
282    response_code: int
283"""This field is set as part of responses."""
284    questions: list[Question]
285"""
286    The question section is used to carry the "question" in most queries, i.e.
287    the parameters that define what is being asked.
288    """
289    answers: list[ResourceRecord]
290"""First resource record section."""
291    authorities: list[ResourceRecord]
292"""Second resource record section."""
293    additionals: list[ResourceRecord]
294"""Third resource record section."""
295
296    timestamp: float | None = None
297"""The time at which the message was sent or received."""
298
299    def__str__(self) -> str:
300        return "\r\n".join(
301            map(
302                str,
303                itertools.chain(
304                    self.questions, self.answers, self.authorities, self.additionals
305                ),
306            )
307        )
308
309    @property
310    defcontent(self) -> bytes:
311        return self.packed
312
313    @property
314    defquestion(self) -> Question | None:
315"""DNS practically only supports a single question at the
316        same time, so this is a shorthand for this."""
317        if len(self.questions) == 1:
318            return self.questions[0]
319        return None
320
321    @property
322    defsize(self) -> int:
323"""Returns the cumulative data size of all resource record sections."""
324        return sum(
325            len(x.data)
326            for x in itertools.chain.from_iterable(
327                [self.answers, self.authorities, self.additionals]
328            )
329        )
330
331    deffail(self, response_code: int) -> DNSMessage:
332        if response_code == response_codes.NOERROR:
333            raise ValueError("response_code must be an error code.")
334        return DNSMessage(
335            timestamp=time.time(),
336            id=self.id,
337            query=False,
338            op_code=self.op_code,
339            authoritative_answer=False,
340            truncation=False,
341            recursion_desired=self.recursion_desired,
342            recursion_available=False,
343            reserved=0,
344            response_code=response_code,
345            questions=self.questions,
346            answers=[],
347            authorities=[],
348            additionals=[],
349        )
350
351    defsucceed(self, answers: list[ResourceRecord]) -> DNSMessage:
352        return DNSMessage(
353            timestamp=time.time(),
354            id=self.id,
355            query=False,
356            op_code=self.op_code,
357            authoritative_answer=False,
358            truncation=False,
359            recursion_desired=self.recursion_desired,
360            recursion_available=True,
361            reserved=0,
362            response_code=response_codes.NOERROR,
363            questions=self.questions,
364            answers=answers,
365            authorities=[],
366            additionals=[],
367        )
368
369    @classmethod
370    defunpack(cls, buffer: bytes, timestamp: float | None = None) -> DNSMessage:
371"""Converts the entire given buffer into a DNS message."""
372        length, msg = cls.unpack_from(buffer, 0, timestamp)
373        if length != len(buffer):
374            raise struct.error(f"unpack requires a buffer of {length} bytes")
375        return msg
376
377    @classmethod
378    defunpack_from(
379        cls, buffer: bytes | bytearray, offset: int, timestamp: float | None = None
380    ) -> tuple[int, DNSMessage]:
381"""Converts the buffer from a given offset into a DNS message and also returns its length."""
382        (
383            id,
384            flags,
385            len_questions,
386            len_answers,
387            len_authorities,
388            len_additionals,
389        ) = DNSMessage.HEADER.unpack_from(buffer, offset)
390        msg = DNSMessage(
391            timestamp=timestamp,
392            id=id,
393            query=(flags & (1 << 15)) == 0,
394            op_code=(flags >> 11) & 0b1111,
395            authoritative_answer=(flags & (1 << 10)) != 0,
396            truncation=(flags & (1 << 9)) != 0,
397            recursion_desired=(flags & (1 << 8)) != 0,
398            recursion_available=(flags & (1 << 7)) != 0,
399            reserved=(flags >> 4) & 0b111,
400            response_code=flags & 0b1111,
401            questions=[],
402            answers=[],
403            authorities=[],
404            additionals=[],
405        )
406        offset += DNSMessage.HEADER.size
407        cached_names = domain_names.cache()
408
409        defunpack_domain_name() -> str:
410            nonlocal buffer, offset, cached_names
411            name, length = domain_names.unpack_from_with_compression(
412                buffer, offset, cached_names
413            )
414            offset += length
415            return name
416
417        for i in range(0, len_questions):
418            try:
419                name = unpack_domain_name()
420                type, class_ = Question.HEADER.unpack_from(buffer, offset)
421                offset += Question.HEADER.size
422                msg.questions.append(Question(name=name, type=type, class_=class_))
423            except struct.error as e:
424                raise struct.error(f"question #{i}: {e}")
425
426        defunpack_rrs(
427            section: list[ResourceRecord], section_name: str, count: int
428        ) -> None:
429            nonlocal buffer, offset
430            for i in range(0, count):
431                try:
432                    name = unpack_domain_name()
433                    type, class_, ttl, len_data = ResourceRecord.HEADER.unpack_from(
434                        buffer, offset
435                    )
436                    offset += ResourceRecord.HEADER.size
437                    end_data = offset + len_data
438                    if len(buffer) < end_data:
439                        raise struct.error(
440                            f"unpack requires a data buffer of {len_data} bytes"
441                        )
442                    data = buffer[offset:end_data]
443
444                    if domain_names.record_data_can_have_compression(type):
445                        data = domain_names.decompress_from_record_data(
446                            buffer, offset, end_data, cached_names
447                        )
448
449                    section.append(ResourceRecord(name, type, class_, ttl, data))
450                    offset += len_data
451                except struct.error as e:
452                    raise struct.error(f"{section_name} #{i}: {e}")
453
454        unpack_rrs(msg.answers, "answer", len_answers)
455        unpack_rrs(msg.authorities, "authority", len_authorities)
456        unpack_rrs(msg.additionals, "additional", len_additionals)
457        return (offset, msg)
458
459    @property
460    defpacked(self) -> bytes:
461"""Converts the message into network bytes."""
462        if self.id < 0 or self.id > 65535:
463            raise ValueError(f"DNS message's id {self.id} is out of bounds.")
464        flags = 0
465        if not self.query:
466            flags |= 1 << 15
467        if self.op_code < 0 or self.op_code > 0b1111:
468            raise ValueError(f"DNS message's op_code {self.op_code} is out of bounds.")
469        flags |= self.op_code << 11
470        if self.authoritative_answer:
471            flags |= 1 << 10
472        if self.truncation:
473            flags |= 1 << 9
474        if self.recursion_desired:
475            flags |= 1 << 8
476        if self.recursion_available:
477            flags |= 1 << 7
478        if self.reserved < 0 or self.reserved > 0b111:
479            raise ValueError(
480                f"DNS message's reserved value of {self.reserved} is out of bounds."
481            )
482        flags |= self.reserved << 4
483        if self.response_code < 0 or self.response_code > 0b1111:
484            raise ValueError(
485                f"DNS message's response_code {self.response_code} is out of bounds."
486            )
487        flags |= self.response_code
488        data = bytearray()
489        data.extend(
490            DNSMessage.HEADER.pack(
491                self.id,
492                flags,
493                len(self.questions),
494                len(self.answers),
495                len(self.authorities),
496                len(self.additionals),
497            )
498        )
499        # TODO implement compression
500        for question in self.questions:
501            data.extend(domain_names.pack(question.name))
502            data.extend(Question.HEADER.pack(question.type, question.class_))
503        for rr in (*self.answers, *self.authorities, *self.additionals):
504            data.extend(domain_names.pack(rr.name))
505            data.extend(
506                ResourceRecord.HEADER.pack(rr.type, rr.class_, rr.ttl, len(rr.data))
507            )
508            data.extend(rr.data)
509        return bytes(data)
510
511    defto_json(self) -> dict:
512"""
513        Converts the message into json for mitmweb.
514        Sync with web/src/flow.ts.
515        """
516        ret = {
517            "id": self.id,
518            "query": self.query,
519            "op_code": op_codes.to_str(self.op_code),
520            "authoritative_answer": self.authoritative_answer,
521            "truncation": self.truncation,
522            "recursion_desired": self.recursion_desired,
523            "recursion_available": self.recursion_available,
524            "response_code": response_codes.to_str(self.response_code),
525            "status_code": response_codes.http_equiv_status_code(self.response_code),
526            "questions": [question.to_json() for question in self.questions],
527            "answers": [rr.to_json() for rr in self.answers],
528            "authorities": [rr.to_json() for rr in self.authorities],
529            "additionals": [rr.to_json() for rr in self.additionals],
530            "size": self.size,
531        }
532        if self.timestamp:
533            ret["timestamp"] = self.timestamp
534        return ret
535
536    @classmethod
537    deffrom_json(cls, data: Any) -> DNSMessage:
538"""Reconstruct a DNS message from JSON."""
539        inst = cls(
540            id=data["id"],
541            query=data["query"],
542            op_code=op_codes.from_str(data["op_code"]),
543            authoritative_answer=data["authoritative_answer"],
544            truncation=data["truncation"],
545            recursion_desired=data["recursion_desired"],
546            recursion_available=data["recursion_available"],
547            reserved=0,
548            response_code=response_codes.from_str(data["response_code"]),
549            questions=[Question.from_json(x) for x in data["questions"]],
550            answers=[ResourceRecord.from_json(x) for x in data["answers"]],
551            authorities=[ResourceRecord.from_json(x) for x in data["authorities"]],
552            additionals=[ResourceRecord.from_json(x) for x in data["additionals"]],
553        )
554        if ts := data.get("timestamp"):
555            inst.timestamp = ts
556        return inst
557
558    defcopy(self) -> DNSMessage:
559        # we keep the copy semantics but change the ID generation
560        state = self.get_state()
561        state["id"] = random.randint(0, 65535)
562        return DNSMessage.from_state(state)
563
564
565classDNSFlow(flow.Flow):
566"""A DNSFlow is a collection of DNS messages representing a single DNS query."""
567
568    request: DNSMessage
569"""The DNS request."""
570    response: DNSMessage | None = None
571"""The DNS response."""
572
573    defget_state(self) -> serializable.State:
574        return {
575            **super().get_state(),
576            "request": self.request.get_state(),
577            "response": self.response.get_state() if self.response else None,
578        }
579
580    defset_state(self, state: serializable.State) -> None:
581        self.request = DNSMessage.from_state(state.pop("request"))
582        self.response = (
583            DNSMessage.from_state(r) if (r := state.pop("response")) else None
584        )
585        super().set_state(state)
586
587    def__repr__(self) -> str:
588        return f"<DNSFlow\r\n  request={self.request!r}\r\n  response={self.response!r}\r\n>"
```

[](#DNSFlow)

```
566classDNSFlow(flow.Flow):
567"""A DNSFlow is a collection of DNS messages representing a single DNS query."""
568
569    request: DNSMessage
570"""The DNS request."""
571    response: DNSMessage | None = None
572"""The DNS response."""
573
574    defget_state(self) -> serializable.State:
575        return {
576            **super().get_state(),
577            "request": self.request.get_state(),
578            "response": self.response.get_state() if self.response else None,
579        }
580
581    defset_state(self, state: serializable.State) -> None:
582        self.request = DNSMessage.from_state(state.pop("request"))
583        self.response = (
584            DNSMessage.from_state(r) if (r := state.pop("response")) else None
585        )
586        super().set_state(state)
587
588    def__repr__(self) -> str:
589        return f"<DNSFlow\r\n  request={self.request!r}\r\n  response={self.response!r}\r\n>"
```

A DNSFlow is a collection of DNS messages representing a single DNS query.

request: mitmproxy.dns.DNSMessage

The DNS request.

response: mitmproxy.dns.DNSMessage | None = None

The DNS response.

type: ClassVar\[str] = 'dns'

The flow type, for example `http`, `tcp`, or `dns`.