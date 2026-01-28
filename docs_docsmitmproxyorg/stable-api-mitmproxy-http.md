---
title: mitmproxy.http
url: https://docs.mitmproxy.org/stable/api/mitmproxy/http.html
source: crawler
fetched_at: 2026-01-28T15:03:25.536224647-03:00
rendered_js: false
word_count: 12722
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/http.py) View Source

```
   1importbinascii
   2importjson
   3importos
   4importtime
   5importurllib.parse
   6importwarnings
   7fromcollections.abcimport Callable
   8fromcollections.abcimport Iterable
   9fromcollections.abcimport Iterator
  10fromcollections.abcimport Mapping
  11fromcollections.abcimport Sequence
  12fromdataclassesimport dataclass
  13fromdataclassesimport fields
  14fromemail.utilsimport formatdate
  15fromemail.utilsimport mktime_tz
  16fromemail.utilsimport parsedate_tz
  17fromtypingimport Any
  18fromtypingimport cast
  19
  20frommitmproxyimport flow
  21frommitmproxy.coretypesimport multidict
  22frommitmproxy.coretypesimport serializable
  23frommitmproxy.netimport encoding
  24frommitmproxy.net.httpimport cookies
  25frommitmproxy.net.httpimport multipart
  26frommitmproxy.net.httpimport status_codes
  27frommitmproxy.net.httpimport url
  28frommitmproxy.net.http.headersimport assemble_content_type
  29frommitmproxy.net.http.headersimport infer_content_encoding
  30frommitmproxy.net.http.headersimport parse_content_type
  31frommitmproxy.utilsimport human
  32frommitmproxy.utilsimport strutils
  33frommitmproxy.utilsimport typecheck
  34frommitmproxy.utils.strutilsimport always_bytes
  35frommitmproxy.utils.strutilsimport always_str
  36frommitmproxy.websocketimport WebSocketData
  37
  38
  39# While headers _should_ be ASCII, it's not uncommon for certain headers to be utf-8 encoded.
  40def_native(x: bytes) -> str:
  41    return x.decode("utf-8", "surrogateescape")
  42
  43
  44def_always_bytes(x: str | bytes) -> bytes:
  45    return strutils.always_bytes(x, "utf-8", "surrogateescape")
  46
  47
  48# This cannot be easily typed with mypy yet, so we just specify MultiDict without concrete types.
  49classHeaders(multidict.MultiDict):  # type: ignore
  50"""
  51    Header class which allows both convenient access to individual headers as well as
  52    direct access to the underlying raw data. Provides a full dictionary interface.
  53
  54    Create headers with keyword arguments:
  55    >>> h = Headers(host="example.com", content_type="application/xml")
  56
  57    Headers mostly behave like a normal dict:
  58    >>> h["Host"]
  59    "example.com"
  60
  61    Headers are case insensitive:
  62    >>> h["host"]
  63    "example.com"
  64
  65    Headers can also be created from a list of raw (header_name, header_value) byte tuples:
  66    >>> h = Headers([
  67        (b"Host",b"example.com"),
  68        (b"Accept",b"text/html"),
  69        (b"accept",b"application/xml")
  70    ])
  71
  72    Multiple headers are folded into a single header as per RFC 7230:
  73    >>> h["Accept"]
  74    "text/html, application/xml"
  75
  76    Setting a header removes all existing headers with the same name:
  77    >>> h["Accept"] = "application/text"
  78    >>> h["Accept"]
  79    "application/text"
  80
  81    `bytes(h)` returns an HTTP/1 header block:
  82    >>> print(bytes(h))
  83    Host: example.com
  84    Accept: application/text
  85
  86    For full control, the raw header fields can be accessed:
  87    >>> h.fields
  88
  89    Caveats:
  90     - For use with the "Set-Cookie" and "Cookie" headers, either use `Response.cookies` or see `Headers.get_all`.
  91    """
  92
  93    def__init__(self, fields: Iterable[tuple[bytes, bytes]] = (), **headers):
  94"""
  95        *Args:*
  96         - *fields:* (optional) list of ``(name, value)`` header byte tuples,
  97           e.g. ``[(b"Host", b"example.com")]``. All names and values must be bytes.
  98         - *\\*\\*headers:* Additional headers to set. Will overwrite existing values from `fields`.
  99           For convenience, underscores in header names will be transformed to dashes -
 100           this behaviour does not extend to other methods.
 101
 102        If ``**headers`` contains multiple keys that have equal ``.lower()`` representations,
 103        the behavior is undefined.
 104        """
 105        super().__init__(fields)
 106
 107        for key, value in self.fields:
 108            if not isinstance(key, bytes) or not isinstance(value, bytes):
 109                raise TypeError("Header fields must be bytes.")
 110
 111        # content_type -> content-type
 112        self.update(
 113            {
 114                _always_bytes(name).replace(b"_", b"-"): _always_bytes(value)
 115                for name, value in headers.items()
 116            }
 117        )
 118
 119    fields: tuple[tuple[bytes, bytes], ...]
 120
 121    @staticmethod
 122    def_reduce_values(values) -> str:
 123        # Headers can be folded
 124        return ", ".join(values)
 125
 126    @staticmethod
 127    def_kconv(key) -> str:
 128        # Headers are case-insensitive
 129        return key.lower()
 130
 131    def__bytes__(self) -> bytes:
 132        if self.fields:
 133            return b"\r\n".join(b": ".join(field) for field in self.fields) + b"\r\n"
 134        else:
 135            return b""
 136
 137    def__delitem__(self, key: str | bytes) -> None:
 138        key = _always_bytes(key)
 139        super().__delitem__(key)
 140
 141    def__iter__(self) -> Iterator[str]:
 142        for x in super().__iter__():
 143            yield _native(x)
 144
 145    defget_all(self, name: str | bytes) -> list[str]:
 146"""
 147        Like `Headers.get`, but does not fold multiple headers into a single one.
 148        This is useful for Set-Cookie and Cookie headers, which do not support folding.
 149
 150        *See also:*
 151         - <https://tools.ietf.org/html/rfc7230#section-3.2.2>
 152         - <https://datatracker.ietf.org/doc/html/rfc6265#section-5.4>
 153         - <https://datatracker.ietf.org/doc/html/rfc7540#section-8.1.2.5>
 154        """
 155        name = _always_bytes(name)
 156        return [_native(x) for x in super().get_all(name)]
 157
 158    defset_all(self, name: str | bytes, values: Iterable[str | bytes]):
 159"""
 160        Explicitly set multiple headers for the given key.
 161        See `Headers.get_all`.
 162        """
 163        name = _always_bytes(name)
 164        values = [_always_bytes(x) for x in values]
 165        return super().set_all(name, values)
 166
 167    definsert(self, index: int, key: str | bytes, value: str | bytes):
 168        key = _always_bytes(key)
 169        value = _always_bytes(value)
 170        super().insert(index, key, value)
 171
 172    defitems(self, multi=False):
 173        if multi:
 174            return ((_native(k), _native(v)) for k, v in self.fields)
 175        else:
 176            return super().items()
 177
 178
 179@dataclass
 180classMessageData(serializable.Serializable):
 181    http_version: bytes
 182    headers: Headers
 183    content: bytes | None
 184    trailers: Headers | None
 185    timestamp_start: float
 186    timestamp_end: float | None
 187
 188    # noinspection PyUnreachableCode
 189    if __debug__:
 190
 191        def__post_init__(self):
 192            for field in fields(self):
 193                val = getattr(self, field.name)
 194                typecheck.check_option_type(field.name, val, field.type)
 195
 196    defset_state(self, state):
 197        for k, v in state.items():
 198            if k in ("headers", "trailers") and v is not None:
 199                v = Headers.from_state(v)
 200            setattr(self, k, v)
 201
 202    defget_state(self):
 203        state = vars(self).copy()
 204        state["headers"] = state["headers"].get_state()
 205        if state["trailers"] is not None:
 206            state["trailers"] = state["trailers"].get_state()
 207        return state
 208
 209    @classmethod
 210    deffrom_state(cls, state):
 211        state["headers"] = Headers.from_state(state["headers"])
 212        if state["trailers"] is not None:
 213            state["trailers"] = Headers.from_state(state["trailers"])
 214        return cls(**state)
 215
 216
 217@dataclass
 218classRequestData(MessageData):
 219    host: str
 220    port: int
 221    method: bytes
 222    scheme: bytes
 223    authority: bytes
 224    path: bytes
 225
 226
 227@dataclass
 228classResponseData(MessageData):
 229    status_code: int
 230    reason: bytes
 231
 232
 233classMessage(serializable.Serializable):
 234"""Base class for `Request` and `Response`."""
 235
 236    @classmethod
 237    deffrom_state(cls, state):
 238        return cls(**state)
 239
 240    defget_state(self):
 241        return self.data.get_state()
 242
 243    defset_state(self, state):
 244        self.data.set_state(state)
 245
 246    data: MessageData
 247    stream: Callable[[bytes], Iterable[bytes] | bytes] | bool = False
 248"""
 249    This attribute controls if the message body should be streamed.
 250
 251    If `False`, mitmproxy will buffer the entire body before forwarding it to the destination.
 252    This makes it possible to perform string replacements on the entire body.
 253    If `True`, the message body will not be buffered on the proxy
 254    but immediately forwarded instead.
 255    Alternatively, a transformation function can be specified, which will be called for each chunk of data.
 256    Please note that packet boundaries generally should not be relied upon.
 257
 258    This attribute must be set in the `requestheaders` or `responseheaders` hook.
 259    Setting it in `request` or  `response` is already too late, mitmproxy has buffered the message body already.
 260    """
 261
 262    @property
 263    defhttp_version(self) -> str:
 264"""
 265        HTTP version string, for example `HTTP/1.1`.
 266        """
 267        return self.data.http_version.decode("utf-8", "surrogateescape")
 268
 269    @http_version.setter
 270    defhttp_version(self, http_version: str | bytes) -> None:
 271        self.data.http_version = strutils.always_bytes(
 272            http_version, "utf-8", "surrogateescape"
 273        )
 274
 275    @property
 276    defis_http10(self) -> bool:
 277        return self.data.http_version == b"HTTP/1.0"
 278
 279    @property
 280    defis_http11(self) -> bool:
 281        return self.data.http_version == b"HTTP/1.1"
 282
 283    @property
 284    defis_http2(self) -> bool:
 285        return self.data.http_version == b"HTTP/2.0"
 286
 287    @property
 288    defis_http3(self) -> bool:
 289        return self.data.http_version == b"HTTP/3"
 290
 291    @property
 292    defheaders(self) -> Headers:
 293"""
 294        The HTTP headers.
 295        """
 296        return self.data.headers
 297
 298    @headers.setter
 299    defheaders(self, h: Headers) -> None:
 300        self.data.headers = h
 301
 302    @property
 303    deftrailers(self) -> Headers | None:
 304"""
 305        The [HTTP trailers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Trailer).
 306        """
 307        return self.data.trailers
 308
 309    @trailers.setter
 310    deftrailers(self, h: Headers | None) -> None:
 311        self.data.trailers = h
 312
 313    @property
 314    defraw_content(self) -> bytes | None:
 315"""
 316        The raw (potentially compressed) HTTP message body.
 317
 318        In contrast to `Message.content` and `Message.text`, accessing this property never raises.
 319        `raw_content` may be `None` if the content is missing, for example due to body streaming
 320        (see `Message.stream`). In contrast, `b""` signals a present but empty message body.
 321
 322        *See also:* `Message.content`, `Message.text`
 323        """
 324        return self.data.content
 325
 326    @raw_content.setter
 327    defraw_content(self, content: bytes | None) -> None:
 328        self.data.content = content
 329
 330    @property
 331    defcontent(self) -> bytes | None:
 332"""
 333        The uncompressed HTTP message body as bytes.
 334
 335        Accessing this attribute may raise a `ValueError` when the HTTP content-encoding is invalid.
 336
 337        *See also:* `Message.raw_content`, `Message.text`
 338        """
 339        return self.get_content()
 340
 341    @content.setter
 342    defcontent(self, value: bytes | None) -> None:
 343        self.set_content(value)
 344
 345    @property
 346    deftext(self) -> str | None:
 347"""
 348        The uncompressed and decoded HTTP message body as text.
 349
 350        Accessing this attribute may raise a `ValueError` when either content-encoding or charset is invalid.
 351
 352        *See also:* `Message.raw_content`, `Message.content`
 353        """
 354        return self.get_text()
 355
 356    @text.setter
 357    deftext(self, value: str | None) -> None:
 358        self.set_text(value)
 359
 360    defset_content(self, value: bytes | None) -> None:
 361        if value is None:
 362            self.raw_content = None
 363            return
 364        if not isinstance(value, bytes):
 365            raise TypeError(
 366                f"Message content must be bytes, not {type(value).__name__}. "
 367                "Please use .text if you want to assign a str."
 368            )
 369        ce = self.headers.get("content-encoding")
 370        try:
 371            self.raw_content = encoding.encode(value, ce or "identity")
 372        except ValueError:
 373            # So we have an invalid content-encoding?
 374            # Let's remove it!
 375            del self.headers["content-encoding"]
 376            self.raw_content = value
 377
 378        if "transfer-encoding" in self.headers:
 379            # https://httpwg.org/specs/rfc7230.html#header.content-length
 380            # don't set content-length if a transfer-encoding is provided
 381            pass
 382        else:
 383            self.headers["content-length"] = str(len(self.raw_content))
 384
 385    defget_content(self, strict: bool = True) -> bytes | None:
 386"""
 387        Similar to `Message.content`, but does not raise if `strict` is `False`.
 388        Instead, the compressed message body is returned as-is.
 389        """
 390        if self.raw_content is None:
 391            return None
 392        ce = self.headers.get("content-encoding")
 393        if ce:
 394            try:
 395                content = encoding.decode(self.raw_content, ce)
 396                # A client may illegally specify a byte -> str encoding here (e.g. utf8)
 397                if isinstance(content, str):
 398                    raise ValueError(f"Invalid Content-Encoding: {ce}")
 399                return content
 400            except ValueError:
 401                if strict:
 402                    raise
 403                return self.raw_content
 404        else:
 405            return self.raw_content
 406
 407    defset_text(self, text: str | None) -> None:
 408        if text is None:
 409            self.content = None
 410            return
 411        enc = infer_content_encoding(self.headers.get("content-type", ""))
 412
 413        try:
 414            self.content = cast(bytes, encoding.encode(text, enc))
 415        except ValueError:
 416            # Fall back to UTF-8 and update the content-type header.
 417            ct = parse_content_type(self.headers.get("content-type", "")) or (
 418                "text",
 419                "plain",
 420                {},
 421            )
 422            ct[2]["charset"] = "utf-8"
 423            self.headers["content-type"] = assemble_content_type(*ct)
 424            enc = "utf8"
 425            self.content = text.encode(enc, "surrogateescape")
 426
 427    defget_text(self, strict: bool = True) -> str | None:
 428"""
 429        Similar to `Message.text`, but does not raise if `strict` is `False`.
 430        Instead, the message body is returned as surrogate-escaped UTF-8.
 431        """
 432        content = self.get_content(strict)
 433        if content is None:
 434            return None
 435        enc = infer_content_encoding(self.headers.get("content-type", ""), content)
 436        try:
 437            return cast(str, encoding.decode(content, enc))
 438        except ValueError:
 439            if strict:
 440                raise
 441            return content.decode("utf8", "surrogateescape")
 442
 443    @property
 444    deftimestamp_start(self) -> float:
 445"""
 446        *Timestamp:* Headers received.
 447        """
 448        return self.data.timestamp_start
 449
 450    @timestamp_start.setter
 451    deftimestamp_start(self, timestamp_start: float) -> None:
 452        self.data.timestamp_start = timestamp_start
 453
 454    @property
 455    deftimestamp_end(self) -> float | None:
 456"""
 457        *Timestamp:* Last byte received.
 458        """
 459        return self.data.timestamp_end
 460
 461    @timestamp_end.setter
 462    deftimestamp_end(self, timestamp_end: float | None):
 463        self.data.timestamp_end = timestamp_end
 464
 465    defdecode(self, strict: bool = True) -> None:
 466"""
 467        Decodes body based on the current Content-Encoding header, then
 468        removes the header.
 469
 470        If the message body is missing or empty, no action is taken.
 471
 472        *Raises:*
 473         - `ValueError`, when the content-encoding is invalid and strict is True.
 474        """
 475        if not self.raw_content:
 476            # The body is missing (for example, because of body streaming or because it's a response
 477            # to a HEAD request), so we can't correctly update content-length.
 478            return
 479        decoded = self.get_content(strict)
 480        self.headers.pop("content-encoding", None)
 481        self.content = decoded
 482
 483    defencode(self, encoding: str) -> None:
 484"""
 485        Encodes body with the given encoding, where e is "gzip", "deflate", "identity", "br", or "zstd".
 486        Any existing content-encodings are overwritten, the content is not decoded beforehand.
 487
 488        *Raises:*
 489         - `ValueError`, when the specified content-encoding is invalid.
 490        """
 491        self.headers["content-encoding"] = encoding
 492        self.content = self.raw_content
 493        if "content-encoding" not in self.headers:
 494            raise ValueError(f"Invalid content encoding {encoding!r}")
 495
 496    defjson(self, **kwargs: Any) -> Any:
 497"""
 498        Returns the JSON encoded content of the response, if any.
 499        `**kwargs` are optional arguments that will be
 500        passed to `json.loads()`.
 501
 502        Will raise if the content can not be decoded and then parsed as JSON.
 503
 504        *Raises:*
 505         - `json.decoder.JSONDecodeError` if content is not valid JSON.
 506         - `TypeError` if the content is not available, for example because the response
 507            has been streamed.
 508        """
 509        content = self.get_content(strict=False)
 510        if content is None:
 511            raise TypeError("Message content is not available.")
 512        else:
 513            return json.loads(content, **kwargs)
 514
 515
 516classRequest(Message):
 517"""
 518    An HTTP request.
 519    """
 520
 521    data: RequestData
 522
 523    def__init__(
 524        self,
 525        host: str,
 526        port: int,
 527        method: bytes,
 528        scheme: bytes,
 529        authority: bytes,
 530        path: bytes,
 531        http_version: bytes,
 532        headers: Headers | tuple[tuple[bytes, bytes], ...],
 533        content: bytes | None,
 534        trailers: Headers | tuple[tuple[bytes, bytes], ...] | None,
 535        timestamp_start: float,
 536        timestamp_end: float | None,
 537    ):
 538        # auto-convert invalid types to retain compatibility with older code.
 539        if isinstance(host, bytes):
 540            host = host.decode("idna", "strict")
 541        if isinstance(method, str):
 542            method = method.encode("ascii", "strict")
 543        if isinstance(scheme, str):
 544            scheme = scheme.encode("ascii", "strict")
 545        if isinstance(authority, str):
 546            authority = authority.encode("ascii", "strict")
 547        if isinstance(path, str):
 548            path = path.encode("ascii", "strict")
 549        if isinstance(http_version, str):
 550            http_version = http_version.encode("ascii", "strict")
 551
 552        if isinstance(content, str):
 553            raise ValueError(f"Content must be bytes, not {type(content).__name__}")
 554        if not isinstance(headers, Headers):
 555            headers = Headers(headers)
 556        if trailers is not None and not isinstance(trailers, Headers):
 557            trailers = Headers(trailers)
 558
 559        self.data = RequestData(
 560            host=host,
 561            port=port,
 562            method=method,
 563            scheme=scheme,
 564            authority=authority,
 565            path=path,
 566            http_version=http_version,
 567            headers=headers,
 568            content=content,
 569            trailers=trailers,
 570            timestamp_start=timestamp_start,
 571            timestamp_end=timestamp_end,
 572        )
 573
 574    def__repr__(self) -> str:
 575        if self.host and self.port:
 576            hostport = f"{self.host}:{self.port}"
 577        else:
 578            hostport = ""
 579        path = self.path or ""
 580        return f"Request({self.method}{hostport}{path})"
 581
 582    @classmethod
 583    defmake(
 584        cls,
 585        method: str,
 586        url: str,
 587        content: bytes | str = "",
 588        headers: (
 589            Headers | dict[str | bytes, str | bytes] | Iterable[tuple[bytes, bytes]]
 590        ) = (),
 591    ) -> "Request":
 592"""
 593        Simplified API for creating request objects.
 594        """
 595        # Headers can be list or dict, we differentiate here.
 596        if isinstance(headers, Headers):
 597            pass
 598        elif isinstance(headers, dict):
 599            headers = Headers(
 600                (
 601                    always_bytes(k, "utf-8", "surrogateescape"),
 602                    always_bytes(v, "utf-8", "surrogateescape"),
 603                )
 604                for k, v in headers.items()
 605            )
 606        elif isinstance(headers, Iterable):
 607            headers = Headers(headers)  # type: ignore
 608        else:
 609            raise TypeError(
 610                "Expected headers to be an iterable or dict, but is {}.".format(
 611                    type(headers).__name__
 612                )
 613            )
 614
 615        req = cls(
 616            "",
 617            0,
 618            method.encode("utf-8", "surrogateescape"),
 619            b"",
 620            b"",
 621            b"",
 622            b"HTTP/1.1",
 623            headers,
 624            b"",
 625            None,
 626            time.time(),
 627            time.time(),
 628        )
 629
 630        req.url = url
 631        # Assign this manually to update the content-length header.
 632        if isinstance(content, bytes):
 633            req.content = content
 634        elif isinstance(content, str):
 635            req.text = content
 636        else:
 637            raise TypeError(
 638                f"Expected content to be str or bytes, but is {type(content).__name__}."
 639            )
 640
 641        return req
 642
 643    @property
 644    deffirst_line_format(self) -> str:
 645"""
 646        *Read-only:* HTTP request form as defined in [RFC 7230](https://tools.ietf.org/html/rfc7230#section-5.3).
 647
 648        origin-form and asterisk-form are subsumed as "relative".
 649        """
 650        if self.method == "CONNECT":
 651            return "authority"
 652        elif self.authority:
 653            return "absolute"
 654        else:
 655            return "relative"
 656
 657    @property
 658    defmethod(self) -> str:
 659"""
 660        HTTP request method, e.g. "GET".
 661        """
 662        return self.data.method.decode("utf-8", "surrogateescape").upper()
 663
 664    @method.setter
 665    defmethod(self, val: str | bytes) -> None:
 666        self.data.method = always_bytes(val, "utf-8", "surrogateescape")
 667
 668    @property
 669    defscheme(self) -> str:
 670"""
 671        HTTP request scheme, which should be "http" or "https".
 672        """
 673        return self.data.scheme.decode("utf-8", "surrogateescape")
 674
 675    @scheme.setter
 676    defscheme(self, val: str | bytes) -> None:
 677        self.data.scheme = always_bytes(val, "utf-8", "surrogateescape")
 678
 679    @property
 680    defauthority(self) -> str:
 681"""
 682        HTTP request authority.
 683
 684        For HTTP/1, this is the authority portion of the request target
 685        (in either absolute-form or authority-form).
 686        For origin-form and asterisk-form requests, this property is set to an empty string.
 687
 688        For HTTP/2, this is the :authority pseudo header.
 689
 690        *See also:* `Request.host`, `Request.host_header`, `Request.pretty_host`
 691        """
 692        try:
 693            return self.data.authority.decode("idna")
 694        except UnicodeError:
 695            return self.data.authority.decode("utf8", "surrogateescape")
 696
 697    @authority.setter
 698    defauthority(self, val: str | bytes) -> None:
 699        if isinstance(val, str):
 700            try:
 701                val = val.encode("idna", "strict")
 702            except UnicodeError:
 703                val = val.encode("utf8", "surrogateescape")  # type: ignore
 704        self.data.authority = val
 705
 706    @property
 707    defhost(self) -> str:
 708"""
 709        Target server for this request. This may be parsed from the raw request
 710        (e.g. from a ``GET http://example.com/ HTTP/1.1`` request line)
 711        or inferred from the proxy mode (e.g. an IP in transparent mode).
 712
 713        Setting the host attribute also updates the host header and authority information, if present.
 714
 715        *See also:* `Request.authority`, `Request.host_header`, `Request.pretty_host`
 716        """
 717        return self.data.host
 718
 719    @host.setter
 720    defhost(self, val: str | bytes) -> None:
 721        self.data.host = always_str(val, "idna", "strict")
 722        self._update_host_and_authority()
 723
 724    @property
 725    defhost_header(self) -> str | None:
 726"""
 727        The request's host/authority header.
 728
 729        This property maps to either ``request.headers["Host"]`` or
 730        ``request.authority``, depending on whether it's HTTP/1.x or HTTP/2.0.
 731
 732        *See also:* `Request.authority`,`Request.host`, `Request.pretty_host`
 733        """
 734        if self.is_http2 or self.is_http3:
 735            return self.authority or self.data.headers.get("Host", None)
 736        else:
 737            return self.data.headers.get("Host", None)
 738
 739    @host_header.setter
 740    defhost_header(self, val: None | str | bytes) -> None:
 741        if val is None:
 742            if self.is_http2 or self.is_http3:
 743                self.data.authority = b""
 744            self.headers.pop("Host", None)
 745        else:
 746            if self.is_http2 or self.is_http3:
 747                self.authority = val  # type: ignore
 748            if not (self.is_http2 or self.is_http3) or "Host" in self.headers:
 749                # For h2, we only overwrite, but not create, as :authority is the h2 host header.
 750                self.headers["Host"] = val
 751
 752    @property
 753    defport(self) -> int:
 754"""
 755        Target port.
 756        """
 757        return self.data.port
 758
 759    @port.setter
 760    defport(self, port: int) -> None:
 761        if not isinstance(port, int):
 762            raise ValueError(f"Port must be an integer, not {port!r}.")
 763
 764        self.data.port = port
 765        self._update_host_and_authority()
 766
 767    def_update_host_and_authority(self) -> None:
 768        val = url.hostport(self.scheme, self.host, self.port)
 769
 770        # Update host header
 771        if "Host" in self.data.headers:
 772            self.data.headers["Host"] = val
 773        # Update authority
 774        if self.data.authority:
 775            self.authority = val
 776
 777    @property
 778    defpath(self) -> str:
 779"""
 780        HTTP request path, e.g. "/index.html" or "/index.html?a=b".
 781        Usually starts with a slash, except for OPTIONS requests, which may just be "*".
 782
 783        This attribute includes both path and query parts of the target URI
 784        (see Sections 3.3 and 3.4 of [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986)).
 785        """
 786        return self.data.path.decode("utf-8", "surrogateescape")
 787
 788    @path.setter
 789    defpath(self, val: str | bytes) -> None:
 790        self.data.path = always_bytes(val, "utf-8", "surrogateescape")
 791
 792    @property
 793    defurl(self) -> str:
 794"""
 795        The full URL string, constructed from `Request.scheme`, `Request.host`, `Request.port` and `Request.path`.
 796
 797        Settings this property updates these attributes as well.
 798        """
 799        if self.first_line_format == "authority":
 800            return f"{self.host}:{self.port}"
 801        path = self.path if self.path != "*" else ""
 802        return url.unparse(self.scheme, self.host, self.port, path)
 803
 804    @url.setter
 805    defurl(self, val: str | bytes) -> None:
 806        val = always_str(val, "utf-8", "surrogateescape")
 807        self.scheme, self.host, self.port, self.path = url.parse(val)  # type: ignore
 808
 809    @property
 810    defpretty_host(self) -> str:
 811"""
 812        *Read-only:* Like `Request.host`, but using `Request.host_header` header as an additional (preferred) data source.
 813        This is useful in transparent mode where `Request.host` is only an IP address.
 814
 815        *Warning:* When working in adversarial environments, this may not reflect the actual destination
 816        as the Host header could be spoofed.
 817        """
 818        authority = self.host_header
 819        if authority:
 820            return url.parse_authority(authority, check=False)[0]
 821        else:
 822            return self.host
 823
 824    @property
 825    defpretty_url(self) -> str:
 826"""
 827        *Read-only:* Like `Request.url`, but using `Request.pretty_host` instead of `Request.host`.
 828        """
 829        if self.first_line_format == "authority":
 830            return self.authority
 831
 832        host_header = self.host_header
 833        if not host_header:
 834            return self.url
 835
 836        pretty_host, pretty_port = url.parse_authority(host_header, check=False)
 837        pretty_port = pretty_port or url.default_port(self.scheme) or 443
 838        path = self.path if self.path != "*" else ""
 839
 840        return url.unparse(self.scheme, pretty_host, pretty_port, path)
 841
 842    def_get_query(self):
 843        query = urllib.parse.urlparse(self.url).query
 844        return tuple(url.decode(query))
 845
 846    def_set_query(self, query_data):
 847        query = url.encode(query_data)
 848        _, _, path, params, _, fragment = urllib.parse.urlparse(self.url)
 849        self.path = urllib.parse.urlunparse(["", "", path, params, query, fragment])
 850
 851    @property
 852    defquery(self) -> multidict.MultiDictView[str, str]:
 853"""
 854        The request query as a mutable mapping view on the request's path.
 855        For the most part, this behaves like a dictionary.
 856        Modifications to the MultiDictView update `Request.path`, and vice versa.
 857        """
 858        return multidict.MultiDictView(self._get_query, self._set_query)
 859
 860    @query.setter
 861    defquery(self, value):
 862        self._set_query(value)
 863
 864    def_get_cookies(self):
 865        h = self.headers.get_all("Cookie")
 866        return tuple(cookies.parse_cookie_headers(h))
 867
 868    def_set_cookies(self, value):
 869        self.headers["cookie"] = cookies.format_cookie_header(value)
 870
 871    @property
 872    defcookies(self) -> multidict.MultiDictView[str, str]:
 873"""
 874        The request cookies.
 875        For the most part, this behaves like a dictionary.
 876        Modifications to the MultiDictView update `Request.headers`, and vice versa.
 877        """
 878        return multidict.MultiDictView(self._get_cookies, self._set_cookies)
 879
 880    @cookies.setter
 881    defcookies(self, value):
 882        self._set_cookies(value)
 883
 884    @property
 885    defpath_components(self) -> tuple[str, ...]:
 886"""
 887        The URL's path components as a tuple of strings.
 888        Components are unquoted.
 889        """
 890        path = urllib.parse.urlparse(self.url).path
 891        # This needs to be a tuple so that it's immutable.
 892        # Otherwise, this would fail silently:
 893        #   request.path_components.append("foo")
 894        return tuple(url.unquote(i) for i in path.split("/") if i)
 895
 896    @path_components.setter
 897    defpath_components(self, components: Iterable[str]):
 898        components = map(lambda x: url.quote(x, safe=""), components)
 899        path = "/" + "/".join(components)
 900        _, _, _, params, query, fragment = urllib.parse.urlparse(self.url)
 901        self.path = urllib.parse.urlunparse(["", "", path, params, query, fragment])
 902
 903    defanticache(self) -> None:
 904"""
 905        Modifies this request to remove headers that might produce a cached response.
 906        """
 907        delheaders = (
 908            "if-modified-since",
 909            "if-none-match",
 910        )
 911        for i in delheaders:
 912            self.headers.pop(i, None)
 913
 914    defanticomp(self) -> None:
 915"""
 916        Modify the Accept-Encoding header to only accept uncompressed responses.
 917        """
 918        self.headers["accept-encoding"] = "identity"
 919
 920    defconstrain_encoding(self) -> None:
 921"""
 922        Limits the permissible Accept-Encoding values, based on what we can decode appropriately.
 923        """
 924        accept_encoding = self.headers.get("accept-encoding")
 925        if accept_encoding:
 926            self.headers["accept-encoding"] = ", ".join(
 927                e
 928                for e in {"gzip", "identity", "deflate", "br", "zstd"}
 929                if e in accept_encoding
 930            )
 931
 932    def_get_urlencoded_form(self):
 933        is_valid_content_type = (
 934            "application/x-www-form-urlencoded"
 935            in self.headers.get("content-type", "").lower()
 936        )
 937        if is_valid_content_type:
 938            return tuple(url.decode(self.get_text(strict=False)))
 939        return ()
 940
 941    def_set_urlencoded_form(self, form_data: Sequence[tuple[str, str]]) -> None:
 942"""
 943        Sets the body to the URL-encoded form data, and adds the appropriate content-type header.
 944        This will overwrite the existing content if there is one.
 945        """
 946        self.headers["content-type"] = "application/x-www-form-urlencoded"
 947        self.content = url.encode(form_data, self.get_text(strict=False)).encode()
 948
 949    @property
 950    defurlencoded_form(self) -> multidict.MultiDictView[str, str]:
 951"""
 952        The URL-encoded form data.
 953
 954        If the content-type indicates non-form data or the form could not be parsed, this is set to
 955        an empty `MultiDictView`.
 956
 957        Modifications to the MultiDictView update `Request.content`, and vice versa.
 958        """
 959        return multidict.MultiDictView(
 960            self._get_urlencoded_form, self._set_urlencoded_form
 961        )
 962
 963    @urlencoded_form.setter
 964    defurlencoded_form(self, value):
 965        self._set_urlencoded_form(value)
 966
 967    def_get_multipart_form(self) -> list[tuple[bytes, bytes]]:
 968        is_valid_content_type = (
 969            "multipart/form-data" in self.headers.get("content-type", "").lower()
 970        )
 971        if is_valid_content_type and self.content is not None:
 972            try:
 973                return multipart.decode_multipart(
 974                    self.headers.get("content-type"), self.content
 975                )
 976            except ValueError:
 977                pass
 978        return []
 979
 980    def_set_multipart_form(self, value: list[tuple[bytes, bytes]]) -> None:
 981        ct = self.headers.get("content-type", "")
 982        is_valid_content_type = ct.lower().startswith("multipart/form-data")
 983        if not is_valid_content_type:
 984"""
 985            Generate a random boundary here.
 986
 987            See <https://datatracker.ietf.org/doc/html/rfc2046#section-5.1.1> for specifications
 988            on generating the boundary.
 989            """
 990            boundary = "-" * 20 + binascii.hexlify(os.urandom(16)).decode()
 991            self.headers["content-type"] = ct = f"multipart/form-data; {boundary=!s}"
 992        self.content = multipart.encode_multipart(ct, value)
 993
 994    @property
 995    defmultipart_form(self) -> multidict.MultiDictView[bytes, bytes]:
 996"""
 997        The multipart form data.
 998
 999        If the content-type indicates non-form data or the form could not be parsed, this is set to
1000        an empty `MultiDictView`.
1001
1002        Modifications to the MultiDictView update `Request.content`, and vice versa.
1003        """
1004        return multidict.MultiDictView(
1005            self._get_multipart_form, self._set_multipart_form
1006        )
1007
1008    @multipart_form.setter
1009    defmultipart_form(self, value: list[tuple[bytes, bytes]]) -> None:
1010        self._set_multipart_form(value)
1011
1012
1013classResponse(Message):
1014"""
1015    An HTTP response.
1016    """
1017
1018    data: ResponseData
1019
1020    def__init__(
1021        self,
1022        http_version: bytes,
1023        status_code: int,
1024        reason: bytes,
1025        headers: Headers | tuple[tuple[bytes, bytes], ...],
1026        content: bytes | None,
1027        trailers: None | Headers | tuple[tuple[bytes, bytes], ...],
1028        timestamp_start: float,
1029        timestamp_end: float | None,
1030    ):
1031        # auto-convert invalid types to retain compatibility with older code.
1032        if isinstance(http_version, str):
1033            http_version = http_version.encode("ascii", "strict")
1034        if isinstance(reason, str):
1035            reason = reason.encode("ascii", "strict")
1036
1037        if isinstance(content, str):
1038            raise ValueError(f"Content must be bytes, not {type(content).__name__}")
1039        if not isinstance(headers, Headers):
1040            headers = Headers(headers)
1041        if trailers is not None and not isinstance(trailers, Headers):
1042            trailers = Headers(trailers)
1043
1044        self.data = ResponseData(
1045            http_version=http_version,
1046            status_code=status_code,
1047            reason=reason,
1048            headers=headers,
1049            content=content,
1050            trailers=trailers,
1051            timestamp_start=timestamp_start,
1052            timestamp_end=timestamp_end,
1053        )
1054
1055    def__repr__(self) -> str:
1056        if self.raw_content:
1057            ct = self.headers.get("content-type", "unknown content type")
1058            size = human.pretty_size(len(self.raw_content))
1059            details = f"{ct}, {size}"
1060        else:
1061            details = "no content"
1062        return f"Response({self.status_code}, {details})"
1063
1064    @classmethod
1065    defmake(
1066        cls,
1067        status_code: int = 200,
1068        content: bytes | str = b"",
1069        headers: (
1070            Headers | Mapping[str, str | bytes] | Iterable[tuple[bytes, bytes]]
1071        ) = (),
1072    ) -> "Response":
1073"""
1074        Simplified API for creating response objects.
1075        """
1076        if isinstance(headers, Headers):
1077            headers = headers
1078        elif isinstance(headers, dict):
1079            headers = Headers(
1080                (
1081                    always_bytes(k, "utf-8", "surrogateescape"),  # type: ignore
1082                    always_bytes(v, "utf-8", "surrogateescape"),
1083                )
1084                for k, v in headers.items()
1085            )
1086        elif isinstance(headers, Iterable):
1087            headers = Headers(headers)  # type: ignore
1088        else:
1089            raise TypeError(
1090                "Expected headers to be an iterable or dict, but is {}.".format(
1091                    type(headers).__name__
1092                )
1093            )
1094
1095        resp = cls(
1096            b"HTTP/1.1",
1097            status_code,
1098            status_codes.RESPONSES.get(status_code, "").encode(),
1099            headers,
1100            None,
1101            None,
1102            time.time(),
1103            time.time(),
1104        )
1105
1106        # Assign this manually to update the content-length header.
1107        if isinstance(content, bytes):
1108            resp.content = content
1109        elif isinstance(content, str):
1110            resp.text = content
1111        else:
1112            raise TypeError(
1113                f"Expected content to be str or bytes, but is {type(content).__name__}."
1114            )
1115
1116        return resp
1117
1118    @property
1119    defstatus_code(self) -> int:
1120"""
1121        HTTP Status Code, e.g. ``200``.
1122        """
1123        return self.data.status_code
1124
1125    @status_code.setter
1126    defstatus_code(self, status_code: int) -> None:
1127        self.data.status_code = status_code
1128
1129    @property
1130    defreason(self) -> str:
1131"""
1132        HTTP reason phrase, for example "Not Found".
1133
1134        HTTP/2 responses do not contain a reason phrase, an empty string will be returned instead.
1135        """
1136        # Encoding: http://stackoverflow.com/a/16674906/934719
1137        return self.data.reason.decode("ISO-8859-1")
1138
1139    @reason.setter
1140    defreason(self, reason: str | bytes) -> None:
1141        self.data.reason = strutils.always_bytes(reason, "ISO-8859-1")
1142
1143    def_get_cookies(self):
1144        h = self.headers.get_all("set-cookie")
1145        all_cookies = cookies.parse_set_cookie_headers(h)
1146        return tuple((name, (value, attrs)) for name, value, attrs in all_cookies)
1147
1148    def_set_cookies(self, value):
1149        cookie_headers = []
1150        for k, v in value:
1151            header = cookies.format_set_cookie_header([(k, v[0], v[1])])
1152            cookie_headers.append(header)
1153        self.headers.set_all("set-cookie", cookie_headers)
1154
1155    @property
1156    defcookies(
1157        self,
1158    ) -> multidict.MultiDictView[str, tuple[str, multidict.MultiDict[str, str | None]]]:
1159"""
1160        The response cookies. A possibly empty `MultiDictView`, where the keys are cookie
1161        name strings, and values are `(cookie value, attributes)` tuples. Within
1162        attributes, unary attributes (e.g. `HTTPOnly`) are indicated by a `None` value.
1163        Modifications to the MultiDictView update `Response.headers`, and vice versa.
1164
1165        *Warning:* Changes to `attributes` will not be picked up unless you also reassign
1166        the `(cookie value, attributes)` tuple directly in the `MultiDictView`.
1167        """
1168        return multidict.MultiDictView(self._get_cookies, self._set_cookies)
1169
1170    @cookies.setter
1171    defcookies(self, value):
1172        self._set_cookies(value)
1173
1174    defrefresh(self, now=None):
1175"""
1176        This fairly complex and heuristic function refreshes a server
1177        response for replay.
1178
1179         - It adjusts date, expires, and last-modified headers.
1180         - It adjusts cookie expiration.
1181        """
1182        if not now:
1183            now = time.time()
1184        delta = now - self.timestamp_start
1185        refresh_headers = [
1186            "date",
1187            "expires",
1188            "last-modified",
1189        ]
1190        for i in refresh_headers:
1191            if i in self.headers:
1192                d = parsedate_tz(self.headers[i])
1193                if d:
1194                    new = mktime_tz(d) + delta
1195                    try:
1196                        self.headers[i] = formatdate(new, usegmt=True)
1197                    except OSError:  # pragma: no cover
1198                        pass  # value out of bounds on Windows only (which is why we exclude it from coverage).
1199        c = []
1200        for set_cookie_header in self.headers.get_all("set-cookie"):
1201            try:
1202                refreshed = cookies.refresh_set_cookie_header(set_cookie_header, delta)
1203            except ValueError:
1204                refreshed = set_cookie_header
1205            c.append(refreshed)
1206        if c:
1207            self.headers.set_all("set-cookie", c)
1208
1209
1210classHTTPFlow(flow.Flow):
1211"""
1212    An HTTPFlow is a collection of objects representing a single HTTP
1213    transaction.
1214    """
1215
1216    request: Request
1217"""The client's HTTP request."""
1218    response: Response | None = None
1219"""The server's HTTP response."""
1220    error: flow.Error | None = None
1221"""
1222    A connection or protocol error affecting this flow.
1223
1224    Note that it's possible for a Flow to have both a response and an error
1225    object. This might happen, for instance, when a response was received
1226    from the server, but there was an error sending it back to the client.
1227    """
1228
1229    websocket: WebSocketData | None = None
1230"""
1231    If this HTTP flow initiated a WebSocket connection, this attribute contains all associated WebSocket data.
1232    """
1233
1234    defget_state(self) -> serializable.State:
1235        return {
1236            **super().get_state(),
1237            "request": self.request.get_state(),
1238            "response": self.response.get_state() if self.response else None,
1239            "websocket": self.websocket.get_state() if self.websocket else None,
1240        }
1241
1242    defset_state(self, state: serializable.State) -> None:
1243        self.request = Request.from_state(state.pop("request"))
1244        self.response = Response.from_state(r) if (r := state.pop("response")) else None
1245        self.websocket = (
1246            WebSocketData.from_state(w) if (w := state.pop("websocket")) else None
1247        )
1248        super().set_state(state)
1249
1250    def__repr__(self):
1251        s = "<HTTPFlow"
1252        for a in (
1253            "request",
1254            "response",
1255            "websocket",
1256            "error",
1257            "client_conn",
1258            "server_conn",
1259        ):
1260            if getattr(self, a, False):
1261                s += f"\r\n{a} = {{flow.{a}}}"
1262        s += ">"
1263        return s.format(flow=self)
1264
1265    @property
1266    deftimestamp_start(self) -> float:
1267"""*Read-only:* An alias for `Request.timestamp_start`."""
1268        return self.request.timestamp_start
1269
1270    @property
1271    defmode(self) -> str:  # pragma: no cover
1272        warnings.warn("HTTPFlow.mode is deprecated.", DeprecationWarning, stacklevel=2)
1273        return getattr(self, "_mode", "regular")
1274
1275    @mode.setter
1276    defmode(self, val: str) -> None:  # pragma: no cover
1277        warnings.warn("HTTPFlow.mode is deprecated.", DeprecationWarning, stacklevel=2)
1278        self._mode = val
1279
1280    defcopy(self):
1281        f = super().copy()
1282        if self.request:
1283            f.request = self.request.copy()
1284        if self.response:
1285            f.response = self.response.copy()
1286        return f
1287
1288
1289__all__ = [
1290    "HTTPFlow",
1291    "Message",
1292    "Request",
1293    "Response",
1294    "Headers",
1295]
```

[](#HTTPFlow)

```
1211classHTTPFlow(flow.Flow):
1212"""
1213    An HTTPFlow is a collection of objects representing a single HTTP
1214    transaction.
1215    """
1216
1217    request: Request
1218"""The client's HTTP request."""
1219    response: Response | None = None
1220"""The server's HTTP response."""
1221    error: flow.Error | None = None
1222"""
1223    A connection or protocol error affecting this flow.
1224
1225    Note that it's possible for a Flow to have both a response and an error
1226    object. This might happen, for instance, when a response was received
1227    from the server, but there was an error sending it back to the client.
1228    """
1229
1230    websocket: WebSocketData | None = None
1231"""
1232    If this HTTP flow initiated a WebSocket connection, this attribute contains all associated WebSocket data.
1233    """
1234
1235    defget_state(self) -> serializable.State:
1236        return {
1237            **super().get_state(),
1238            "request": self.request.get_state(),
1239            "response": self.response.get_state() if self.response else None,
1240            "websocket": self.websocket.get_state() if self.websocket else None,
1241        }
1242
1243    defset_state(self, state: serializable.State) -> None:
1244        self.request = Request.from_state(state.pop("request"))
1245        self.response = Response.from_state(r) if (r := state.pop("response")) else None
1246        self.websocket = (
1247            WebSocketData.from_state(w) if (w := state.pop("websocket")) else None
1248        )
1249        super().set_state(state)
1250
1251    def__repr__(self):
1252        s = "<HTTPFlow"
1253        for a in (
1254            "request",
1255            "response",
1256            "websocket",
1257            "error",
1258            "client_conn",
1259            "server_conn",
1260        ):
1261            if getattr(self, a, False):
1262                s += f"\r\n{a} = {{flow.{a}}}"
1263        s += ">"
1264        return s.format(flow=self)
1265
1266    @property
1267    deftimestamp_start(self) -> float:
1268"""*Read-only:* An alias for `Request.timestamp_start`."""
1269        return self.request.timestamp_start
1270
1271    @property
1272    defmode(self) -> str:  # pragma: no cover
1273        warnings.warn("HTTPFlow.mode is deprecated.", DeprecationWarning, stacklevel=2)
1274        return getattr(self, "_mode", "regular")
1275
1276    @mode.setter
1277    defmode(self, val: str) -> None:  # pragma: no cover
1278        warnings.warn("HTTPFlow.mode is deprecated.", DeprecationWarning, stacklevel=2)
1279        self._mode = val
1280
1281    defcopy(self):
1282        f = super().copy()
1283        if self.request:
1284            f.request = self.request.copy()
1285        if self.response:
1286            f.response = self.response.copy()
1287        return f
```

An HTTPFlow is a collection of objects representing a single HTTP transaction.

request: [Request](#Request)

The client's HTTP request.

response: [Response](#Response) | None = None

The server's HTTP response.

A connection or protocol error affecting this flow.

Note that it's possible for a Flow to have both a response and an error object. This might happen, for instance, when a response was received from the server, but there was an error sending it back to the client.

If this HTTP flow initiated a WebSocket connection, this attribute contains all associated WebSocket data.

timestamp\_start: float View Source

```
1266    @property
1267    deftimestamp_start(self) -> float:
1268"""*Read-only:* An alias for `Request.timestamp_start`."""
1269        return self.request.timestamp_start
```

*Read-only:* An alias for `Request.timestamp_start`.

mode: str View Source

```
1271    @property
1272    defmode(self) -> str:  # pragma: no cover
1273        warnings.warn("HTTPFlow.mode is deprecated.", DeprecationWarning, stacklevel=2)
1274        return getattr(self, "_mode", "regular")
```

def copy(self): View Source

```
1281    defcopy(self):
1282        f = super().copy()
1283        if self.request:
1284            f.request = self.request.copy()
1285        if self.response:
1286            f.response = self.response.copy()
1287        return f
```

Make a copy of this flow.

type: ClassVar\[str] = 'http'

The flow type, for example `http`, `tcp`, or `dns`.

class Message(mitmproxy.coretypes.serializable.Serializable): View Source

[](#Message)

```
234classMessage(serializable.Serializable):
235"""Base class for `Request` and `Response`."""
236
237    @classmethod
238    deffrom_state(cls, state):
239        return cls(**state)
240
241    defget_state(self):
242        return self.data.get_state()
243
244    defset_state(self, state):
245        self.data.set_state(state)
246
247    data: MessageData
248    stream: Callable[[bytes], Iterable[bytes] | bytes] | bool = False
249"""
250    This attribute controls if the message body should be streamed.
251
252    If `False`, mitmproxy will buffer the entire body before forwarding it to the destination.
253    This makes it possible to perform string replacements on the entire body.
254    If `True`, the message body will not be buffered on the proxy
255    but immediately forwarded instead.
256    Alternatively, a transformation function can be specified, which will be called for each chunk of data.
257    Please note that packet boundaries generally should not be relied upon.
258
259    This attribute must be set in the `requestheaders` or `responseheaders` hook.
260    Setting it in `request` or  `response` is already too late, mitmproxy has buffered the message body already.
261    """
262
263    @property
264    defhttp_version(self) -> str:
265"""
266        HTTP version string, for example `HTTP/1.1`.
267        """
268        return self.data.http_version.decode("utf-8", "surrogateescape")
269
270    @http_version.setter
271    defhttp_version(self, http_version: str | bytes) -> None:
272        self.data.http_version = strutils.always_bytes(
273            http_version, "utf-8", "surrogateescape"
274        )
275
276    @property
277    defis_http10(self) -> bool:
278        return self.data.http_version == b"HTTP/1.0"
279
280    @property
281    defis_http11(self) -> bool:
282        return self.data.http_version == b"HTTP/1.1"
283
284    @property
285    defis_http2(self) -> bool:
286        return self.data.http_version == b"HTTP/2.0"
287
288    @property
289    defis_http3(self) -> bool:
290        return self.data.http_version == b"HTTP/3"
291
292    @property
293    defheaders(self) -> Headers:
294"""
295        The HTTP headers.
296        """
297        return self.data.headers
298
299    @headers.setter
300    defheaders(self, h: Headers) -> None:
301        self.data.headers = h
302
303    @property
304    deftrailers(self) -> Headers | None:
305"""
306        The [HTTP trailers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Trailer).
307        """
308        return self.data.trailers
309
310    @trailers.setter
311    deftrailers(self, h: Headers | None) -> None:
312        self.data.trailers = h
313
314    @property
315    defraw_content(self) -> bytes | None:
316"""
317        The raw (potentially compressed) HTTP message body.
318
319        In contrast to `Message.content` and `Message.text`, accessing this property never raises.
320        `raw_content` may be `None` if the content is missing, for example due to body streaming
321        (see `Message.stream`). In contrast, `b""` signals a present but empty message body.
322
323        *See also:* `Message.content`, `Message.text`
324        """
325        return self.data.content
326
327    @raw_content.setter
328    defraw_content(self, content: bytes | None) -> None:
329        self.data.content = content
330
331    @property
332    defcontent(self) -> bytes | None:
333"""
334        The uncompressed HTTP message body as bytes.
335
336        Accessing this attribute may raise a `ValueError` when the HTTP content-encoding is invalid.
337
338        *See also:* `Message.raw_content`, `Message.text`
339        """
340        return self.get_content()
341
342    @content.setter
343    defcontent(self, value: bytes | None) -> None:
344        self.set_content(value)
345
346    @property
347    deftext(self) -> str | None:
348"""
349        The uncompressed and decoded HTTP message body as text.
350
351        Accessing this attribute may raise a `ValueError` when either content-encoding or charset is invalid.
352
353        *See also:* `Message.raw_content`, `Message.content`
354        """
355        return self.get_text()
356
357    @text.setter
358    deftext(self, value: str | None) -> None:
359        self.set_text(value)
360
361    defset_content(self, value: bytes | None) -> None:
362        if value is None:
363            self.raw_content = None
364            return
365        if not isinstance(value, bytes):
366            raise TypeError(
367                f"Message content must be bytes, not {type(value).__name__}. "
368                "Please use .text if you want to assign a str."
369            )
370        ce = self.headers.get("content-encoding")
371        try:
372            self.raw_content = encoding.encode(value, ce or "identity")
373        except ValueError:
374            # So we have an invalid content-encoding?
375            # Let's remove it!
376            del self.headers["content-encoding"]
377            self.raw_content = value
378
379        if "transfer-encoding" in self.headers:
380            # https://httpwg.org/specs/rfc7230.html#header.content-length
381            # don't set content-length if a transfer-encoding is provided
382            pass
383        else:
384            self.headers["content-length"] = str(len(self.raw_content))
385
386    defget_content(self, strict: bool = True) -> bytes | None:
387"""
388        Similar to `Message.content`, but does not raise if `strict` is `False`.
389        Instead, the compressed message body is returned as-is.
390        """
391        if self.raw_content is None:
392            return None
393        ce = self.headers.get("content-encoding")
394        if ce:
395            try:
396                content = encoding.decode(self.raw_content, ce)
397                # A client may illegally specify a byte -> str encoding here (e.g. utf8)
398                if isinstance(content, str):
399                    raise ValueError(f"Invalid Content-Encoding: {ce}")
400                return content
401            except ValueError:
402                if strict:
403                    raise
404                return self.raw_content
405        else:
406            return self.raw_content
407
408    defset_text(self, text: str | None) -> None:
409        if text is None:
410            self.content = None
411            return
412        enc = infer_content_encoding(self.headers.get("content-type", ""))
413
414        try:
415            self.content = cast(bytes, encoding.encode(text, enc))
416        except ValueError:
417            # Fall back to UTF-8 and update the content-type header.
418            ct = parse_content_type(self.headers.get("content-type", "")) or (
419                "text",
420                "plain",
421                {},
422            )
423            ct[2]["charset"] = "utf-8"
424            self.headers["content-type"] = assemble_content_type(*ct)
425            enc = "utf8"
426            self.content = text.encode(enc, "surrogateescape")
427
428    defget_text(self, strict: bool = True) -> str | None:
429"""
430        Similar to `Message.text`, but does not raise if `strict` is `False`.
431        Instead, the message body is returned as surrogate-escaped UTF-8.
432        """
433        content = self.get_content(strict)
434        if content is None:
435            return None
436        enc = infer_content_encoding(self.headers.get("content-type", ""), content)
437        try:
438            return cast(str, encoding.decode(content, enc))
439        except ValueError:
440            if strict:
441                raise
442            return content.decode("utf8", "surrogateescape")
443
444    @property
445    deftimestamp_start(self) -> float:
446"""
447        *Timestamp:* Headers received.
448        """
449        return self.data.timestamp_start
450
451    @timestamp_start.setter
452    deftimestamp_start(self, timestamp_start: float) -> None:
453        self.data.timestamp_start = timestamp_start
454
455    @property
456    deftimestamp_end(self) -> float | None:
457"""
458        *Timestamp:* Last byte received.
459        """
460        return self.data.timestamp_end
461
462    @timestamp_end.setter
463    deftimestamp_end(self, timestamp_end: float | None):
464        self.data.timestamp_end = timestamp_end
465
466    defdecode(self, strict: bool = True) -> None:
467"""
468        Decodes body based on the current Content-Encoding header, then
469        removes the header.
470
471        If the message body is missing or empty, no action is taken.
472
473        *Raises:*
474         - `ValueError`, when the content-encoding is invalid and strict is True.
475        """
476        if not self.raw_content:
477            # The body is missing (for example, because of body streaming or because it's a response
478            # to a HEAD request), so we can't correctly update content-length.
479            return
480        decoded = self.get_content(strict)
481        self.headers.pop("content-encoding", None)
482        self.content = decoded
483
484    defencode(self, encoding: str) -> None:
485"""
486        Encodes body with the given encoding, where e is "gzip", "deflate", "identity", "br", or "zstd".
487        Any existing content-encodings are overwritten, the content is not decoded beforehand.
488
489        *Raises:*
490         - `ValueError`, when the specified content-encoding is invalid.
491        """
492        self.headers["content-encoding"] = encoding
493        self.content = self.raw_content
494        if "content-encoding" not in self.headers:
495            raise ValueError(f"Invalid content encoding {encoding!r}")
496
497    defjson(self, **kwargs: Any) -> Any:
498"""
499        Returns the JSON encoded content of the response, if any.
500        `**kwargs` are optional arguments that will be
501        passed to `json.loads()`.
502
503        Will raise if the content can not be decoded and then parsed as JSON.
504
505        *Raises:*
506         - `json.decoder.JSONDecodeError` if content is not valid JSON.
507         - `TypeError` if the content is not available, for example because the response
508            has been streamed.
509        """
510        content = self.get_content(strict=False)
511        if content is None:
512            raise TypeError("Message content is not available.")
513        else:
514            return json.loads(content, **kwargs)
```

Base class for `Request` and `Response`.

stream: Callable\[\[bytes], Iterable\[bytes] | bytes] | bool = False

This attribute controls if the message body should be streamed.

If `False`, mitmproxy will buffer the entire body before forwarding it to the destination. This makes it possible to perform string replacements on the entire body. If `True`, the message body will not be buffered on the proxy but immediately forwarded instead. Alternatively, a transformation function can be specified, which will be called for each chunk of data. Please note that packet boundaries generally should not be relied upon.

This attribute must be set in the `requestheaders` or `responseheaders` hook. Setting it in `request` or `response` is already too late, mitmproxy has buffered the message body already.

http\_version: str View Source

```
263    @property
264    defhttp_version(self) -> str:
265"""
266        HTTP version string, for example `HTTP/1.1`.
267        """
268        return self.data.http_version.decode("utf-8", "surrogateescape")
```

HTTP version string, for example `HTTP/1.1`.

is\_http10: bool View Source

```
276    @property
277    defis_http10(self) -> bool:
278        return self.data.http_version == b"HTTP/1.0"
```

is\_http11: bool View Source

```
280    @property
281    defis_http11(self) -> bool:
282        return self.data.http_version == b"HTTP/1.1"
```

is\_http2: bool View Source

```
284    @property
285    defis_http2(self) -> bool:
286        return self.data.http_version == b"HTTP/2.0"
```

is\_http3: bool View Source

```
288    @property
289    defis_http3(self) -> bool:
290        return self.data.http_version == b"HTTP/3"
```

trailers: [Headers](#Headers) | None View Source

```
303    @property
304    deftrailers(self) -> Headers | None:
305"""
306        The [HTTP trailers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Trailer).
307        """
308        return self.data.trailers
```

raw\_content: bytes | None View Source

```
314    @property
315    defraw_content(self) -> bytes | None:
316"""
317        The raw (potentially compressed) HTTP message body.
318
319        In contrast to `Message.content` and `Message.text`, accessing this property never raises.
320        `raw_content` may be `None` if the content is missing, for example due to body streaming
321        (see `Message.stream`). In contrast, `b""` signals a present but empty message body.
322
323        *See also:* `Message.content`, `Message.text`
324        """
325        return self.data.content
```

The raw (potentially compressed) HTTP message body.

In contrast to `Message.content` and `Message.text`, accessing this property never raises. `raw_content` may be `None` if the content is missing, for example due to body streaming (see `Message.stream`). In contrast, `b""` signals a present but empty message body.

*See also:* `Message.content`, `Message.text`

content: bytes | None View Source

```
331    @property
332    defcontent(self) -> bytes | None:
333"""
334        The uncompressed HTTP message body as bytes.
335
336        Accessing this attribute may raise a `ValueError` when the HTTP content-encoding is invalid.
337
338        *See also:* `Message.raw_content`, `Message.text`
339        """
340        return self.get_content()
```

The uncompressed HTTP message body as bytes.

Accessing this attribute may raise a `ValueError` when the HTTP content-encoding is invalid.

*See also:* `Message.raw_content`, `Message.text`

text: str | None View Source

```
346    @property
347    deftext(self) -> str | None:
348"""
349        The uncompressed and decoded HTTP message body as text.
350
351        Accessing this attribute may raise a `ValueError` when either content-encoding or charset is invalid.
352
353        *See also:* `Message.raw_content`, `Message.content`
354        """
355        return self.get_text()
```

The uncompressed and decoded HTTP message body as text.

Accessing this attribute may raise a `ValueError` when either content-encoding or charset is invalid.

*See also:* `Message.raw_content`, `Message.content`

def set\_content(self, value: bytes | None) -&gt; None: View Source

```
361    defset_content(self, value: bytes | None) -> None:
362        if value is None:
363            self.raw_content = None
364            return
365        if not isinstance(value, bytes):
366            raise TypeError(
367                f"Message content must be bytes, not {type(value).__name__}. "
368                "Please use .text if you want to assign a str."
369            )
370        ce = self.headers.get("content-encoding")
371        try:
372            self.raw_content = encoding.encode(value, ce or "identity")
373        except ValueError:
374            # So we have an invalid content-encoding?
375            # Let's remove it!
376            del self.headers["content-encoding"]
377            self.raw_content = value
378
379        if "transfer-encoding" in self.headers:
380            # https://httpwg.org/specs/rfc7230.html#header.content-length
381            # don't set content-length if a transfer-encoding is provided
382            pass
383        else:
384            self.headers["content-length"] = str(len(self.raw_content))
```

def get\_content(self, strict: bool = True) -&gt; bytes | None: View Source

```
386    defget_content(self, strict: bool = True) -> bytes | None:
387"""
388        Similar to `Message.content`, but does not raise if `strict` is `False`.
389        Instead, the compressed message body is returned as-is.
390        """
391        if self.raw_content is None:
392            return None
393        ce = self.headers.get("content-encoding")
394        if ce:
395            try:
396                content = encoding.decode(self.raw_content, ce)
397                # A client may illegally specify a byte -> str encoding here (e.g. utf8)
398                if isinstance(content, str):
399                    raise ValueError(f"Invalid Content-Encoding: {ce}")
400                return content
401            except ValueError:
402                if strict:
403                    raise
404                return self.raw_content
405        else:
406            return self.raw_content
```

Similar to `Message.content`, but does not raise if `strict` is `False`. Instead, the compressed message body is returned as-is.

def set\_text(self, text: str | None) -&gt; None: View Source

```
408    defset_text(self, text: str | None) -> None:
409        if text is None:
410            self.content = None
411            return
412        enc = infer_content_encoding(self.headers.get("content-type", ""))
413
414        try:
415            self.content = cast(bytes, encoding.encode(text, enc))
416        except ValueError:
417            # Fall back to UTF-8 and update the content-type header.
418            ct = parse_content_type(self.headers.get("content-type", "")) or (
419                "text",
420                "plain",
421                {},
422            )
423            ct[2]["charset"] = "utf-8"
424            self.headers["content-type"] = assemble_content_type(*ct)
425            enc = "utf8"
426            self.content = text.encode(enc, "surrogateescape")
```

def get\_text(self, strict: bool = True) -&gt; str | None: View Source

```
428    defget_text(self, strict: bool = True) -> str | None:
429"""
430        Similar to `Message.text`, but does not raise if `strict` is `False`.
431        Instead, the message body is returned as surrogate-escaped UTF-8.
432        """
433        content = self.get_content(strict)
434        if content is None:
435            return None
436        enc = infer_content_encoding(self.headers.get("content-type", ""), content)
437        try:
438            return cast(str, encoding.decode(content, enc))
439        except ValueError:
440            if strict:
441                raise
442            return content.decode("utf8", "surrogateescape")
```

Similar to `Message.text`, but does not raise if `strict` is `False`. Instead, the message body is returned as surrogate-escaped UTF-8.

timestamp\_start: float View Source

```
444    @property
445    deftimestamp_start(self) -> float:
446"""
447        *Timestamp:* Headers received.
448        """
449        return self.data.timestamp_start
```

*Timestamp:* Headers received.

timestamp\_end: float | None View Source

```
455    @property
456    deftimestamp_end(self) -> float | None:
457"""
458        *Timestamp:* Last byte received.
459        """
460        return self.data.timestamp_end
```

*Timestamp:* Last byte received.

def decode(self, strict: bool = True) -&gt; None: View Source

```
466    defdecode(self, strict: bool = True) -> None:
467"""
468        Decodes body based on the current Content-Encoding header, then
469        removes the header.
470
471        If the message body is missing or empty, no action is taken.
472
473        *Raises:*
474         - `ValueError`, when the content-encoding is invalid and strict is True.
475        """
476        if not self.raw_content:
477            # The body is missing (for example, because of body streaming or because it's a response
478            # to a HEAD request), so we can't correctly update content-length.
479            return
480        decoded = self.get_content(strict)
481        self.headers.pop("content-encoding", None)
482        self.content = decoded
```

Decodes body based on the current Content-Encoding header, then removes the header.

If the message body is missing or empty, no action is taken.

*Raises:*

- `ValueError`, when the content-encoding is invalid and strict is True.

def encode(self, encoding: str) -&gt; None: View Source

```
484    defencode(self, encoding: str) -> None:
485"""
486        Encodes body with the given encoding, where e is "gzip", "deflate", "identity", "br", or "zstd".
487        Any existing content-encodings are overwritten, the content is not decoded beforehand.
488
489        *Raises:*
490         - `ValueError`, when the specified content-encoding is invalid.
491        """
492        self.headers["content-encoding"] = encoding
493        self.content = self.raw_content
494        if "content-encoding" not in self.headers:
495            raise ValueError(f"Invalid content encoding {encoding!r}")
```

Encodes body with the given encoding, where e is "gzip", "deflate", "identity", "br", or "zstd". Any existing content-encodings are overwritten, the content is not decoded beforehand.

*Raises:*

- `ValueError`, when the specified content-encoding is invalid.

def json(self, \*\*kwargs: Any) -&gt; Any: View Source

```
497    defjson(self, **kwargs: Any) -> Any:
498"""
499        Returns the JSON encoded content of the response, if any.
500        `**kwargs` are optional arguments that will be
501        passed to `json.loads()`.
502
503        Will raise if the content can not be decoded and then parsed as JSON.
504
505        *Raises:*
506         - `json.decoder.JSONDecodeError` if content is not valid JSON.
507         - `TypeError` if the content is not available, for example because the response
508            has been streamed.
509        """
510        content = self.get_content(strict=False)
511        if content is None:
512            raise TypeError("Message content is not available.")
513        else:
514            return json.loads(content, **kwargs)
```

Returns the JSON encoded content of the response, if any. `**kwargs` are optional arguments that will be passed to `json.loads()`.

Will raise if the content can not be decoded and then parsed as JSON.

*Raises:*

- `json.decoder.JSONDecodeError` if content is not valid JSON.
- `TypeError` if the content is not available, for example because the response has been streamed.

class Request([Message](#Message)): View Source

[](#Request)

```
 517classRequest(Message):
 518"""
 519    An HTTP request.
 520    """
 521
 522    data: RequestData
 523
 524    def__init__(
 525        self,
 526        host: str,
 527        port: int,
 528        method: bytes,
 529        scheme: bytes,
 530        authority: bytes,
 531        path: bytes,
 532        http_version: bytes,
 533        headers: Headers | tuple[tuple[bytes, bytes], ...],
 534        content: bytes | None,
 535        trailers: Headers | tuple[tuple[bytes, bytes], ...] | None,
 536        timestamp_start: float,
 537        timestamp_end: float | None,
 538    ):
 539        # auto-convert invalid types to retain compatibility with older code.
 540        if isinstance(host, bytes):
 541            host = host.decode("idna", "strict")
 542        if isinstance(method, str):
 543            method = method.encode("ascii", "strict")
 544        if isinstance(scheme, str):
 545            scheme = scheme.encode("ascii", "strict")
 546        if isinstance(authority, str):
 547            authority = authority.encode("ascii", "strict")
 548        if isinstance(path, str):
 549            path = path.encode("ascii", "strict")
 550        if isinstance(http_version, str):
 551            http_version = http_version.encode("ascii", "strict")
 552
 553        if isinstance(content, str):
 554            raise ValueError(f"Content must be bytes, not {type(content).__name__}")
 555        if not isinstance(headers, Headers):
 556            headers = Headers(headers)
 557        if trailers is not None and not isinstance(trailers, Headers):
 558            trailers = Headers(trailers)
 559
 560        self.data = RequestData(
 561            host=host,
 562            port=port,
 563            method=method,
 564            scheme=scheme,
 565            authority=authority,
 566            path=path,
 567            http_version=http_version,
 568            headers=headers,
 569            content=content,
 570            trailers=trailers,
 571            timestamp_start=timestamp_start,
 572            timestamp_end=timestamp_end,
 573        )
 574
 575    def__repr__(self) -> str:
 576        if self.host and self.port:
 577            hostport = f"{self.host}:{self.port}"
 578        else:
 579            hostport = ""
 580        path = self.path or ""
 581        return f"Request({self.method}{hostport}{path})"
 582
 583    @classmethod
 584    defmake(
 585        cls,
 586        method: str,
 587        url: str,
 588        content: bytes | str = "",
 589        headers: (
 590            Headers | dict[str | bytes, str | bytes] | Iterable[tuple[bytes, bytes]]
 591        ) = (),
 592    ) -> "Request":
 593"""
 594        Simplified API for creating request objects.
 595        """
 596        # Headers can be list or dict, we differentiate here.
 597        if isinstance(headers, Headers):
 598            pass
 599        elif isinstance(headers, dict):
 600            headers = Headers(
 601                (
 602                    always_bytes(k, "utf-8", "surrogateescape"),
 603                    always_bytes(v, "utf-8", "surrogateescape"),
 604                )
 605                for k, v in headers.items()
 606            )
 607        elif isinstance(headers, Iterable):
 608            headers = Headers(headers)  # type: ignore
 609        else:
 610            raise TypeError(
 611                "Expected headers to be an iterable or dict, but is {}.".format(
 612                    type(headers).__name__
 613                )
 614            )
 615
 616        req = cls(
 617            "",
 618            0,
 619            method.encode("utf-8", "surrogateescape"),
 620            b"",
 621            b"",
 622            b"",
 623            b"HTTP/1.1",
 624            headers,
 625            b"",
 626            None,
 627            time.time(),
 628            time.time(),
 629        )
 630
 631        req.url = url
 632        # Assign this manually to update the content-length header.
 633        if isinstance(content, bytes):
 634            req.content = content
 635        elif isinstance(content, str):
 636            req.text = content
 637        else:
 638            raise TypeError(
 639                f"Expected content to be str or bytes, but is {type(content).__name__}."
 640            )
 641
 642        return req
 643
 644    @property
 645    deffirst_line_format(self) -> str:
 646"""
 647        *Read-only:* HTTP request form as defined in [RFC 7230](https://tools.ietf.org/html/rfc7230#section-5.3).
 648
 649        origin-form and asterisk-form are subsumed as "relative".
 650        """
 651        if self.method == "CONNECT":
 652            return "authority"
 653        elif self.authority:
 654            return "absolute"
 655        else:
 656            return "relative"
 657
 658    @property
 659    defmethod(self) -> str:
 660"""
 661        HTTP request method, e.g. "GET".
 662        """
 663        return self.data.method.decode("utf-8", "surrogateescape").upper()
 664
 665    @method.setter
 666    defmethod(self, val: str | bytes) -> None:
 667        self.data.method = always_bytes(val, "utf-8", "surrogateescape")
 668
 669    @property
 670    defscheme(self) -> str:
 671"""
 672        HTTP request scheme, which should be "http" or "https".
 673        """
 674        return self.data.scheme.decode("utf-8", "surrogateescape")
 675
 676    @scheme.setter
 677    defscheme(self, val: str | bytes) -> None:
 678        self.data.scheme = always_bytes(val, "utf-8", "surrogateescape")
 679
 680    @property
 681    defauthority(self) -> str:
 682"""
 683        HTTP request authority.
 684
 685        For HTTP/1, this is the authority portion of the request target
 686        (in either absolute-form or authority-form).
 687        For origin-form and asterisk-form requests, this property is set to an empty string.
 688
 689        For HTTP/2, this is the :authority pseudo header.
 690
 691        *See also:* `Request.host`, `Request.host_header`, `Request.pretty_host`
 692        """
 693        try:
 694            return self.data.authority.decode("idna")
 695        except UnicodeError:
 696            return self.data.authority.decode("utf8", "surrogateescape")
 697
 698    @authority.setter
 699    defauthority(self, val: str | bytes) -> None:
 700        if isinstance(val, str):
 701            try:
 702                val = val.encode("idna", "strict")
 703            except UnicodeError:
 704                val = val.encode("utf8", "surrogateescape")  # type: ignore
 705        self.data.authority = val
 706
 707    @property
 708    defhost(self) -> str:
 709"""
 710        Target server for this request. This may be parsed from the raw request
 711        (e.g. from a ``GET http://example.com/ HTTP/1.1`` request line)
 712        or inferred from the proxy mode (e.g. an IP in transparent mode).
 713
 714        Setting the host attribute also updates the host header and authority information, if present.
 715
 716        *See also:* `Request.authority`, `Request.host_header`, `Request.pretty_host`
 717        """
 718        return self.data.host
 719
 720    @host.setter
 721    defhost(self, val: str | bytes) -> None:
 722        self.data.host = always_str(val, "idna", "strict")
 723        self._update_host_and_authority()
 724
 725    @property
 726    defhost_header(self) -> str | None:
 727"""
 728        The request's host/authority header.
 729
 730        This property maps to either ``request.headers["Host"]`` or
 731        ``request.authority``, depending on whether it's HTTP/1.x or HTTP/2.0.
 732
 733        *See also:* `Request.authority`,`Request.host`, `Request.pretty_host`
 734        """
 735        if self.is_http2 or self.is_http3:
 736            return self.authority or self.data.headers.get("Host", None)
 737        else:
 738            return self.data.headers.get("Host", None)
 739
 740    @host_header.setter
 741    defhost_header(self, val: None | str | bytes) -> None:
 742        if val is None:
 743            if self.is_http2 or self.is_http3:
 744                self.data.authority = b""
 745            self.headers.pop("Host", None)
 746        else:
 747            if self.is_http2 or self.is_http3:
 748                self.authority = val  # type: ignore
 749            if not (self.is_http2 or self.is_http3) or "Host" in self.headers:
 750                # For h2, we only overwrite, but not create, as :authority is the h2 host header.
 751                self.headers["Host"] = val
 752
 753    @property
 754    defport(self) -> int:
 755"""
 756        Target port.
 757        """
 758        return self.data.port
 759
 760    @port.setter
 761    defport(self, port: int) -> None:
 762        if not isinstance(port, int):
 763            raise ValueError(f"Port must be an integer, not {port!r}.")
 764
 765        self.data.port = port
 766        self._update_host_and_authority()
 767
 768    def_update_host_and_authority(self) -> None:
 769        val = url.hostport(self.scheme, self.host, self.port)
 770
 771        # Update host header
 772        if "Host" in self.data.headers:
 773            self.data.headers["Host"] = val
 774        # Update authority
 775        if self.data.authority:
 776            self.authority = val
 777
 778    @property
 779    defpath(self) -> str:
 780"""
 781        HTTP request path, e.g. "/index.html" or "/index.html?a=b".
 782        Usually starts with a slash, except for OPTIONS requests, which may just be "*".
 783
 784        This attribute includes both path and query parts of the target URI
 785        (see Sections 3.3 and 3.4 of [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986)).
 786        """
 787        return self.data.path.decode("utf-8", "surrogateescape")
 788
 789    @path.setter
 790    defpath(self, val: str | bytes) -> None:
 791        self.data.path = always_bytes(val, "utf-8", "surrogateescape")
 792
 793    @property
 794    defurl(self) -> str:
 795"""
 796        The full URL string, constructed from `Request.scheme`, `Request.host`, `Request.port` and `Request.path`.
 797
 798        Settings this property updates these attributes as well.
 799        """
 800        if self.first_line_format == "authority":
 801            return f"{self.host}:{self.port}"
 802        path = self.path if self.path != "*" else ""
 803        return url.unparse(self.scheme, self.host, self.port, path)
 804
 805    @url.setter
 806    defurl(self, val: str | bytes) -> None:
 807        val = always_str(val, "utf-8", "surrogateescape")
 808        self.scheme, self.host, self.port, self.path = url.parse(val)  # type: ignore
 809
 810    @property
 811    defpretty_host(self) -> str:
 812"""
 813        *Read-only:* Like `Request.host`, but using `Request.host_header` header as an additional (preferred) data source.
 814        This is useful in transparent mode where `Request.host` is only an IP address.
 815
 816        *Warning:* When working in adversarial environments, this may not reflect the actual destination
 817        as the Host header could be spoofed.
 818        """
 819        authority = self.host_header
 820        if authority:
 821            return url.parse_authority(authority, check=False)[0]
 822        else:
 823            return self.host
 824
 825    @property
 826    defpretty_url(self) -> str:
 827"""
 828        *Read-only:* Like `Request.url`, but using `Request.pretty_host` instead of `Request.host`.
 829        """
 830        if self.first_line_format == "authority":
 831            return self.authority
 832
 833        host_header = self.host_header
 834        if not host_header:
 835            return self.url
 836
 837        pretty_host, pretty_port = url.parse_authority(host_header, check=False)
 838        pretty_port = pretty_port or url.default_port(self.scheme) or 443
 839        path = self.path if self.path != "*" else ""
 840
 841        return url.unparse(self.scheme, pretty_host, pretty_port, path)
 842
 843    def_get_query(self):
 844        query = urllib.parse.urlparse(self.url).query
 845        return tuple(url.decode(query))
 846
 847    def_set_query(self, query_data):
 848        query = url.encode(query_data)
 849        _, _, path, params, _, fragment = urllib.parse.urlparse(self.url)
 850        self.path = urllib.parse.urlunparse(["", "", path, params, query, fragment])
 851
 852    @property
 853    defquery(self) -> multidict.MultiDictView[str, str]:
 854"""
 855        The request query as a mutable mapping view on the request's path.
 856        For the most part, this behaves like a dictionary.
 857        Modifications to the MultiDictView update `Request.path`, and vice versa.
 858        """
 859        return multidict.MultiDictView(self._get_query, self._set_query)
 860
 861    @query.setter
 862    defquery(self, value):
 863        self._set_query(value)
 864
 865    def_get_cookies(self):
 866        h = self.headers.get_all("Cookie")
 867        return tuple(cookies.parse_cookie_headers(h))
 868
 869    def_set_cookies(self, value):
 870        self.headers["cookie"] = cookies.format_cookie_header(value)
 871
 872    @property
 873    defcookies(self) -> multidict.MultiDictView[str, str]:
 874"""
 875        The request cookies.
 876        For the most part, this behaves like a dictionary.
 877        Modifications to the MultiDictView update `Request.headers`, and vice versa.
 878        """
 879        return multidict.MultiDictView(self._get_cookies, self._set_cookies)
 880
 881    @cookies.setter
 882    defcookies(self, value):
 883        self._set_cookies(value)
 884
 885    @property
 886    defpath_components(self) -> tuple[str, ...]:
 887"""
 888        The URL's path components as a tuple of strings.
 889        Components are unquoted.
 890        """
 891        path = urllib.parse.urlparse(self.url).path
 892        # This needs to be a tuple so that it's immutable.
 893        # Otherwise, this would fail silently:
 894        #   request.path_components.append("foo")
 895        return tuple(url.unquote(i) for i in path.split("/") if i)
 896
 897    @path_components.setter
 898    defpath_components(self, components: Iterable[str]):
 899        components = map(lambda x: url.quote(x, safe=""), components)
 900        path = "/" + "/".join(components)
 901        _, _, _, params, query, fragment = urllib.parse.urlparse(self.url)
 902        self.path = urllib.parse.urlunparse(["", "", path, params, query, fragment])
 903
 904    defanticache(self) -> None:
 905"""
 906        Modifies this request to remove headers that might produce a cached response.
 907        """
 908        delheaders = (
 909            "if-modified-since",
 910            "if-none-match",
 911        )
 912        for i in delheaders:
 913            self.headers.pop(i, None)
 914
 915    defanticomp(self) -> None:
 916"""
 917        Modify the Accept-Encoding header to only accept uncompressed responses.
 918        """
 919        self.headers["accept-encoding"] = "identity"
 920
 921    defconstrain_encoding(self) -> None:
 922"""
 923        Limits the permissible Accept-Encoding values, based on what we can decode appropriately.
 924        """
 925        accept_encoding = self.headers.get("accept-encoding")
 926        if accept_encoding:
 927            self.headers["accept-encoding"] = ", ".join(
 928                e
 929                for e in {"gzip", "identity", "deflate", "br", "zstd"}
 930                if e in accept_encoding
 931            )
 932
 933    def_get_urlencoded_form(self):
 934        is_valid_content_type = (
 935            "application/x-www-form-urlencoded"
 936            in self.headers.get("content-type", "").lower()
 937        )
 938        if is_valid_content_type:
 939            return tuple(url.decode(self.get_text(strict=False)))
 940        return ()
 941
 942    def_set_urlencoded_form(self, form_data: Sequence[tuple[str, str]]) -> None:
 943"""
 944        Sets the body to the URL-encoded form data, and adds the appropriate content-type header.
 945        This will overwrite the existing content if there is one.
 946        """
 947        self.headers["content-type"] = "application/x-www-form-urlencoded"
 948        self.content = url.encode(form_data, self.get_text(strict=False)).encode()
 949
 950    @property
 951    defurlencoded_form(self) -> multidict.MultiDictView[str, str]:
 952"""
 953        The URL-encoded form data.
 954
 955        If the content-type indicates non-form data or the form could not be parsed, this is set to
 956        an empty `MultiDictView`.
 957
 958        Modifications to the MultiDictView update `Request.content`, and vice versa.
 959        """
 960        return multidict.MultiDictView(
 961            self._get_urlencoded_form, self._set_urlencoded_form
 962        )
 963
 964    @urlencoded_form.setter
 965    defurlencoded_form(self, value):
 966        self._set_urlencoded_form(value)
 967
 968    def_get_multipart_form(self) -> list[tuple[bytes, bytes]]:
 969        is_valid_content_type = (
 970            "multipart/form-data" in self.headers.get("content-type", "").lower()
 971        )
 972        if is_valid_content_type and self.content is not None:
 973            try:
 974                return multipart.decode_multipart(
 975                    self.headers.get("content-type"), self.content
 976                )
 977            except ValueError:
 978                pass
 979        return []
 980
 981    def_set_multipart_form(self, value: list[tuple[bytes, bytes]]) -> None:
 982        ct = self.headers.get("content-type", "")
 983        is_valid_content_type = ct.lower().startswith("multipart/form-data")
 984        if not is_valid_content_type:
 985"""
 986            Generate a random boundary here.
 987
 988            See <https://datatracker.ietf.org/doc/html/rfc2046#section-5.1.1> for specifications
 989            on generating the boundary.
 990            """
 991            boundary = "-" * 20 + binascii.hexlify(os.urandom(16)).decode()
 992            self.headers["content-type"] = ct = f"multipart/form-data; {boundary=!s}"
 993        self.content = multipart.encode_multipart(ct, value)
 994
 995    @property
 996    defmultipart_form(self) -> multidict.MultiDictView[bytes, bytes]:
 997"""
 998        The multipart form data.
 999
1000        If the content-type indicates non-form data or the form could not be parsed, this is set to
1001        an empty `MultiDictView`.
1002
1003        Modifications to the MultiDictView update `Request.content`, and vice versa.
1004        """
1005        return multidict.MultiDictView(
1006            self._get_multipart_form, self._set_multipart_form
1007        )
1008
1009    @multipart_form.setter
1010    defmultipart_form(self, value: list[tuple[bytes, bytes]]) -> None:
1011        self._set_multipart_form(value)
```

An HTTP request.

Request( host: str, port: int, method: bytes, scheme: bytes, authority: bytes, path: bytes, http\_version: bytes, headers: [Headers](#Headers) | tuple\[tuple\[bytes, bytes], ...], content: bytes | None, trailers: [Headers](#Headers) | tuple\[tuple\[bytes, bytes], ...] | None, timestamp\_start: float, timestamp\_end: float | None) View Source

```
524    def__init__(
525        self,
526        host: str,
527        port: int,
528        method: bytes,
529        scheme: bytes,
530        authority: bytes,
531        path: bytes,
532        http_version: bytes,
533        headers: Headers | tuple[tuple[bytes, bytes], ...],
534        content: bytes | None,
535        trailers: Headers | tuple[tuple[bytes, bytes], ...] | None,
536        timestamp_start: float,
537        timestamp_end: float | None,
538    ):
539        # auto-convert invalid types to retain compatibility with older code.
540        if isinstance(host, bytes):
541            host = host.decode("idna", "strict")
542        if isinstance(method, str):
543            method = method.encode("ascii", "strict")
544        if isinstance(scheme, str):
545            scheme = scheme.encode("ascii", "strict")
546        if isinstance(authority, str):
547            authority = authority.encode("ascii", "strict")
548        if isinstance(path, str):
549            path = path.encode("ascii", "strict")
550        if isinstance(http_version, str):
551            http_version = http_version.encode("ascii", "strict")
552
553        if isinstance(content, str):
554            raise ValueError(f"Content must be bytes, not {type(content).__name__}")
555        if not isinstance(headers, Headers):
556            headers = Headers(headers)
557        if trailers is not None and not isinstance(trailers, Headers):
558            trailers = Headers(trailers)
559
560        self.data = RequestData(
561            host=host,
562            port=port,
563            method=method,
564            scheme=scheme,
565            authority=authority,
566            path=path,
567            http_version=http_version,
568            headers=headers,
569            content=content,
570            trailers=trailers,
571            timestamp_start=timestamp_start,
572            timestamp_end=timestamp_end,
573        )
```

@classmethod

def make( cls, method: str, url: str, content: bytes | str = '', headers: [Headers](#Headers) | dict\[str | bytes, str | bytes] | Iterable\[tuple\[bytes, bytes]] = ()) -&gt; [Request](#Request): View Source

```
583    @classmethod
584    defmake(
585        cls,
586        method: str,
587        url: str,
588        content: bytes | str = "",
589        headers: (
590            Headers | dict[str | bytes, str | bytes] | Iterable[tuple[bytes, bytes]]
591        ) = (),
592    ) -> "Request":
593"""
594        Simplified API for creating request objects.
595        """
596        # Headers can be list or dict, we differentiate here.
597        if isinstance(headers, Headers):
598            pass
599        elif isinstance(headers, dict):
600            headers = Headers(
601                (
602                    always_bytes(k, "utf-8", "surrogateescape"),
603                    always_bytes(v, "utf-8", "surrogateescape"),
604                )
605                for k, v in headers.items()
606            )
607        elif isinstance(headers, Iterable):
608            headers = Headers(headers)  # type: ignore
609        else:
610            raise TypeError(
611                "Expected headers to be an iterable or dict, but is {}.".format(
612                    type(headers).__name__
613                )
614            )
615
616        req = cls(
617            "",
618            0,
619            method.encode("utf-8", "surrogateescape"),
620            b"",
621            b"",
622            b"",
623            b"HTTP/1.1",
624            headers,
625            b"",
626            None,
627            time.time(),
628            time.time(),
629        )
630
631        req.url = url
632        # Assign this manually to update the content-length header.
633        if isinstance(content, bytes):
634            req.content = content
635        elif isinstance(content, str):
636            req.text = content
637        else:
638            raise TypeError(
639                f"Expected content to be str or bytes, but is {type(content).__name__}."
640            )
641
642        return req
```

Simplified API for creating request objects.

first\_line\_format: str View Source

```
644    @property
645    deffirst_line_format(self) -> str:
646"""
647        *Read-only:* HTTP request form as defined in [RFC 7230](https://tools.ietf.org/html/rfc7230#section-5.3).
648
649        origin-form and asterisk-form are subsumed as "relative".
650        """
651        if self.method == "CONNECT":
652            return "authority"
653        elif self.authority:
654            return "absolute"
655        else:
656            return "relative"
```

*Read-only:* HTTP request form as defined in [RFC 7230](https://tools.ietf.org/html/rfc7230#section-5.3).

origin-form and asterisk-form are subsumed as "relative".

method: str View Source

```
658    @property
659    defmethod(self) -> str:
660"""
661        HTTP request method, e.g. "GET".
662        """
663        return self.data.method.decode("utf-8", "surrogateescape").upper()
```

HTTP request method, e.g. "GET".

scheme: str View Source

```
669    @property
670    defscheme(self) -> str:
671"""
672        HTTP request scheme, which should be "http" or "https".
673        """
674        return self.data.scheme.decode("utf-8", "surrogateescape")
```

HTTP request scheme, which should be "http" or "https".

authority: str View Source

```
681    defauthority(self) -> str:
682"""
683        HTTP request authority.
684
685        For HTTP/1, this is the authority portion of the request target
686        (in either absolute-form or authority-form).
687        For origin-form and asterisk-form requests, this property is set to an empty string.
688
689        For HTTP/2, this is the :authority pseudo header.
690
691        *See also:* `Request.host`, `Request.host_header`, `Request.pretty_host`
692        """
693        try:
694            return self.data.authority.decode("idna")
695        except UnicodeError:
696            return self.data.authority.decode("utf8", "surrogateescape")
```

HTTP request authority.

For HTTP/1, this is the authority portion of the request target (in either absolute-form or authority-form). For origin-form and asterisk-form requests, this property is set to an empty string.

For HTTP/2, this is the :authority pseudo header.

*See also:* `Request.host`, `Request.host_header`, `Request.pretty_host`

host: str View Source

```
707    @property
708    defhost(self) -> str:
709"""
710        Target server for this request. This may be parsed from the raw request
711        (e.g. from a ``GET http://example.com/ HTTP/1.1`` request line)
712        or inferred from the proxy mode (e.g. an IP in transparent mode).
713
714        Setting the host attribute also updates the host header and authority information, if present.
715
716        *See also:* `Request.authority`, `Request.host_header`, `Request.pretty_host`
717        """
718        return self.data.host
```

Target server for this request. This may be parsed from the raw request (e.g. from a `GET http://example.com/ HTTP/1.1` request line) or inferred from the proxy mode (e.g. an IP in transparent mode).

Setting the host attribute also updates the host header and authority information, if present.

*See also:* `Request.authority`, `Request.host_header`, `Request.pretty_host`

port: int View Source

```
753    @property
754    defport(self) -> int:
755"""
756        Target port.
757        """
758        return self.data.port
```

Target port.

path: str View Source

```
778    @property
779    defpath(self) -> str:
780"""
781        HTTP request path, e.g. "/index.html" or "/index.html?a=b".
782        Usually starts with a slash, except for OPTIONS requests, which may just be "*".
783
784        This attribute includes both path and query parts of the target URI
785        (see Sections 3.3 and 3.4 of [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986)).
786        """
787        return self.data.path.decode("utf-8", "surrogateescape")
```

HTTP request path, e.g. "/index.html" or "/index.html?a=b". Usually starts with a slash, except for OPTIONS requests, which may just be "\*".

This attribute includes both path and query parts of the target URI (see Sections 3.3 and 3.4 of [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986)).

url: str View Source

```
793    @property
794    defurl(self) -> str:
795"""
796        The full URL string, constructed from `Request.scheme`, `Request.host`, `Request.port` and `Request.path`.
797
798        Settings this property updates these attributes as well.
799        """
800        if self.first_line_format == "authority":
801            return f"{self.host}:{self.port}"
802        path = self.path if self.path != "*" else ""
803        return url.unparse(self.scheme, self.host, self.port, path)
```

The full URL string, constructed from `Request.scheme`, `Request.host`, `Request.port` and `Request.path`.

Settings this property updates these attributes as well.

pretty\_host: str View Source

```
810    @property
811    defpretty_host(self) -> str:
812"""
813        *Read-only:* Like `Request.host`, but using `Request.host_header` header as an additional (preferred) data source.
814        This is useful in transparent mode where `Request.host` is only an IP address.
815
816        *Warning:* When working in adversarial environments, this may not reflect the actual destination
817        as the Host header could be spoofed.
818        """
819        authority = self.host_header
820        if authority:
821            return url.parse_authority(authority, check=False)[0]
822        else:
823            return self.host
```

*Read-only:* Like `Request.host`, but using `Request.host_header` header as an additional (preferred) data source. This is useful in transparent mode where `Request.host` is only an IP address.

*Warning:* When working in adversarial environments, this may not reflect the actual destination as the Host header could be spoofed.

pretty\_url: str View Source

```
825    @property
826    defpretty_url(self) -> str:
827"""
828        *Read-only:* Like `Request.url`, but using `Request.pretty_host` instead of `Request.host`.
829        """
830        if self.first_line_format == "authority":
831            return self.authority
832
833        host_header = self.host_header
834        if not host_header:
835            return self.url
836
837        pretty_host, pretty_port = url.parse_authority(host_header, check=False)
838        pretty_port = pretty_port or url.default_port(self.scheme) or 443
839        path = self.path if self.path != "*" else ""
840
841        return url.unparse(self.scheme, pretty_host, pretty_port, path)
```

*Read-only:* Like `Request.url`, but using `Request.pretty_host` instead of `Request.host`.

```
852    @property
853    defquery(self) -> multidict.MultiDictView[str, str]:
854"""
855        The request query as a mutable mapping view on the request's path.
856        For the most part, this behaves like a dictionary.
857        Modifications to the MultiDictView update `Request.path`, and vice versa.
858        """
859        return multidict.MultiDictView(self._get_query, self._set_query)
```

The request query as a mutable mapping view on the request's path. For the most part, this behaves like a dictionary. Modifications to the MultiDictView update `Request.path`, and vice versa.

```
872    @property
873    defcookies(self) -> multidict.MultiDictView[str, str]:
874"""
875        The request cookies.
876        For the most part, this behaves like a dictionary.
877        Modifications to the MultiDictView update `Request.headers`, and vice versa.
878        """
879        return multidict.MultiDictView(self._get_cookies, self._set_cookies)
```

The request cookies. For the most part, this behaves like a dictionary. Modifications to the MultiDictView update `Request.headers`, and vice versa.

path\_components: tuple\[str, ...] View Source

```
885    @property
886    defpath_components(self) -> tuple[str, ...]:
887"""
888        The URL's path components as a tuple of strings.
889        Components are unquoted.
890        """
891        path = urllib.parse.urlparse(self.url).path
892        # This needs to be a tuple so that it's immutable.
893        # Otherwise, this would fail silently:
894        #   request.path_components.append("foo")
895        return tuple(url.unquote(i) for i in path.split("/") if i)
```

The URL's path components as a tuple of strings. Components are unquoted.

def anticache(self) -&gt; None: View Source

```
904    defanticache(self) -> None:
905"""
906        Modifies this request to remove headers that might produce a cached response.
907        """
908        delheaders = (
909            "if-modified-since",
910            "if-none-match",
911        )
912        for i in delheaders:
913            self.headers.pop(i, None)
```

Modifies this request to remove headers that might produce a cached response.

def anticomp(self) -&gt; None: View Source

```
915    defanticomp(self) -> None:
916"""
917        Modify the Accept-Encoding header to only accept uncompressed responses.
918        """
919        self.headers["accept-encoding"] = "identity"
```

Modify the Accept-Encoding header to only accept uncompressed responses.

def constrain\_encoding(self) -&gt; None: View Source

```
921    defconstrain_encoding(self) -> None:
922"""
923        Limits the permissible Accept-Encoding values, based on what we can decode appropriately.
924        """
925        accept_encoding = self.headers.get("accept-encoding")
926        if accept_encoding:
927            self.headers["accept-encoding"] = ", ".join(
928                e
929                for e in {"gzip", "identity", "deflate", "br", "zstd"}
930                if e in accept_encoding
931            )
```

Limits the permissible Accept-Encoding values, based on what we can decode appropriately.

```
950    @property
951    defurlencoded_form(self) -> multidict.MultiDictView[str, str]:
952"""
953        The URL-encoded form data.
954
955        If the content-type indicates non-form data or the form could not be parsed, this is set to
956        an empty `MultiDictView`.
957
958        Modifications to the MultiDictView update `Request.content`, and vice versa.
959        """
960        return multidict.MultiDictView(
961            self._get_urlencoded_form, self._set_urlencoded_form
962        )
```

The URL-encoded form data.

If the content-type indicates non-form data or the form could not be parsed, this is set to an empty `MultiDictView`.

Modifications to the MultiDictView update `Request.content`, and vice versa.

```
 995    @property
 996    defmultipart_form(self) -> multidict.MultiDictView[bytes, bytes]:
 997"""
 998        The multipart form data.
 999
1000        If the content-type indicates non-form data or the form could not be parsed, this is set to
1001        an empty `MultiDictView`.
1002
1003        Modifications to the MultiDictView update `Request.content`, and vice versa.
1004        """
1005        return multidict.MultiDictView(
1006            self._get_multipart_form, self._set_multipart_form
1007        )
```

The multipart form data.

If the content-type indicates non-form data or the form could not be parsed, this is set to an empty `MultiDictView`.

Modifications to the MultiDictView update `Request.content`, and vice versa.

class Response([Message](#Message)): View Source

[](#Response)

```
1014classResponse(Message):
1015"""
1016    An HTTP response.
1017    """
1018
1019    data: ResponseData
1020
1021    def__init__(
1022        self,
1023        http_version: bytes,
1024        status_code: int,
1025        reason: bytes,
1026        headers: Headers | tuple[tuple[bytes, bytes], ...],
1027        content: bytes | None,
1028        trailers: None | Headers | tuple[tuple[bytes, bytes], ...],
1029        timestamp_start: float,
1030        timestamp_end: float | None,
1031    ):
1032        # auto-convert invalid types to retain compatibility with older code.
1033        if isinstance(http_version, str):
1034            http_version = http_version.encode("ascii", "strict")
1035        if isinstance(reason, str):
1036            reason = reason.encode("ascii", "strict")
1037
1038        if isinstance(content, str):
1039            raise ValueError(f"Content must be bytes, not {type(content).__name__}")
1040        if not isinstance(headers, Headers):
1041            headers = Headers(headers)
1042        if trailers is not None and not isinstance(trailers, Headers):
1043            trailers = Headers(trailers)
1044
1045        self.data = ResponseData(
1046            http_version=http_version,
1047            status_code=status_code,
1048            reason=reason,
1049            headers=headers,
1050            content=content,
1051            trailers=trailers,
1052            timestamp_start=timestamp_start,
1053            timestamp_end=timestamp_end,
1054        )
1055
1056    def__repr__(self) -> str:
1057        if self.raw_content:
1058            ct = self.headers.get("content-type", "unknown content type")
1059            size = human.pretty_size(len(self.raw_content))
1060            details = f"{ct}, {size}"
1061        else:
1062            details = "no content"
1063        return f"Response({self.status_code}, {details})"
1064
1065    @classmethod
1066    defmake(
1067        cls,
1068        status_code: int = 200,
1069        content: bytes | str = b"",
1070        headers: (
1071            Headers | Mapping[str, str | bytes] | Iterable[tuple[bytes, bytes]]
1072        ) = (),
1073    ) -> "Response":
1074"""
1075        Simplified API for creating response objects.
1076        """
1077        if isinstance(headers, Headers):
1078            headers = headers
1079        elif isinstance(headers, dict):
1080            headers = Headers(
1081                (
1082                    always_bytes(k, "utf-8", "surrogateescape"),  # type: ignore
1083                    always_bytes(v, "utf-8", "surrogateescape"),
1084                )
1085                for k, v in headers.items()
1086            )
1087        elif isinstance(headers, Iterable):
1088            headers = Headers(headers)  # type: ignore
1089        else:
1090            raise TypeError(
1091                "Expected headers to be an iterable or dict, but is {}.".format(
1092                    type(headers).__name__
1093                )
1094            )
1095
1096        resp = cls(
1097            b"HTTP/1.1",
1098            status_code,
1099            status_codes.RESPONSES.get(status_code, "").encode(),
1100            headers,
1101            None,
1102            None,
1103            time.time(),
1104            time.time(),
1105        )
1106
1107        # Assign this manually to update the content-length header.
1108        if isinstance(content, bytes):
1109            resp.content = content
1110        elif isinstance(content, str):
1111            resp.text = content
1112        else:
1113            raise TypeError(
1114                f"Expected content to be str or bytes, but is {type(content).__name__}."
1115            )
1116
1117        return resp
1118
1119    @property
1120    defstatus_code(self) -> int:
1121"""
1122        HTTP Status Code, e.g. ``200``.
1123        """
1124        return self.data.status_code
1125
1126    @status_code.setter
1127    defstatus_code(self, status_code: int) -> None:
1128        self.data.status_code = status_code
1129
1130    @property
1131    defreason(self) -> str:
1132"""
1133        HTTP reason phrase, for example "Not Found".
1134
1135        HTTP/2 responses do not contain a reason phrase, an empty string will be returned instead.
1136        """
1137        # Encoding: http://stackoverflow.com/a/16674906/934719
1138        return self.data.reason.decode("ISO-8859-1")
1139
1140    @reason.setter
1141    defreason(self, reason: str | bytes) -> None:
1142        self.data.reason = strutils.always_bytes(reason, "ISO-8859-1")
1143
1144    def_get_cookies(self):
1145        h = self.headers.get_all("set-cookie")
1146        all_cookies = cookies.parse_set_cookie_headers(h)
1147        return tuple((name, (value, attrs)) for name, value, attrs in all_cookies)
1148
1149    def_set_cookies(self, value):
1150        cookie_headers = []
1151        for k, v in value:
1152            header = cookies.format_set_cookie_header([(k, v[0], v[1])])
1153            cookie_headers.append(header)
1154        self.headers.set_all("set-cookie", cookie_headers)
1155
1156    @property
1157    defcookies(
1158        self,
1159    ) -> multidict.MultiDictView[str, tuple[str, multidict.MultiDict[str, str | None]]]:
1160"""
1161        The response cookies. A possibly empty `MultiDictView`, where the keys are cookie
1162        name strings, and values are `(cookie value, attributes)` tuples. Within
1163        attributes, unary attributes (e.g. `HTTPOnly`) are indicated by a `None` value.
1164        Modifications to the MultiDictView update `Response.headers`, and vice versa.
1165
1166        *Warning:* Changes to `attributes` will not be picked up unless you also reassign
1167        the `(cookie value, attributes)` tuple directly in the `MultiDictView`.
1168        """
1169        return multidict.MultiDictView(self._get_cookies, self._set_cookies)
1170
1171    @cookies.setter
1172    defcookies(self, value):
1173        self._set_cookies(value)
1174
1175    defrefresh(self, now=None):
1176"""
1177        This fairly complex and heuristic function refreshes a server
1178        response for replay.
1179
1180         - It adjusts date, expires, and last-modified headers.
1181         - It adjusts cookie expiration.
1182        """
1183        if not now:
1184            now = time.time()
1185        delta = now - self.timestamp_start
1186        refresh_headers = [
1187            "date",
1188            "expires",
1189            "last-modified",
1190        ]
1191        for i in refresh_headers:
1192            if i in self.headers:
1193                d = parsedate_tz(self.headers[i])
1194                if d:
1195                    new = mktime_tz(d) + delta
1196                    try:
1197                        self.headers[i] = formatdate(new, usegmt=True)
1198                    except OSError:  # pragma: no cover
1199                        pass  # value out of bounds on Windows only (which is why we exclude it from coverage).
1200        c = []
1201        for set_cookie_header in self.headers.get_all("set-cookie"):
1202            try:
1203                refreshed = cookies.refresh_set_cookie_header(set_cookie_header, delta)
1204            except ValueError:
1205                refreshed = set_cookie_header
1206            c.append(refreshed)
1207        if c:
1208            self.headers.set_all("set-cookie", c)
```

An HTTP response.

Response( http\_version: bytes, status\_code: int, reason: bytes, headers: [Headers](#Headers) | tuple\[tuple\[bytes, bytes], ...], content: bytes | None, trailers: None | [Headers](#Headers) | tuple\[tuple\[bytes, bytes], ...], timestamp\_start: float, timestamp\_end: float | None) View Source

```
1021    def__init__(
1022        self,
1023        http_version: bytes,
1024        status_code: int,
1025        reason: bytes,
1026        headers: Headers | tuple[tuple[bytes, bytes], ...],
1027        content: bytes | None,
1028        trailers: None | Headers | tuple[tuple[bytes, bytes], ...],
1029        timestamp_start: float,
1030        timestamp_end: float | None,
1031    ):
1032        # auto-convert invalid types to retain compatibility with older code.
1033        if isinstance(http_version, str):
1034            http_version = http_version.encode("ascii", "strict")
1035        if isinstance(reason, str):
1036            reason = reason.encode("ascii", "strict")
1037
1038        if isinstance(content, str):
1039            raise ValueError(f"Content must be bytes, not {type(content).__name__}")
1040        if not isinstance(headers, Headers):
1041            headers = Headers(headers)
1042        if trailers is not None and not isinstance(trailers, Headers):
1043            trailers = Headers(trailers)
1044
1045        self.data = ResponseData(
1046            http_version=http_version,
1047            status_code=status_code,
1048            reason=reason,
1049            headers=headers,
1050            content=content,
1051            trailers=trailers,
1052            timestamp_start=timestamp_start,
1053            timestamp_end=timestamp_end,
1054        )
```

@classmethod

def make( cls, status\_code: int = 200, content: bytes | str = b'', headers: [Headers](#Headers) | Mapping\[str, str | bytes] | Iterable\[tuple\[bytes, bytes]] = ()) -&gt; [Response](#Response): View Source

```
1065    @classmethod
1066    defmake(
1067        cls,
1068        status_code: int = 200,
1069        content: bytes | str = b"",
1070        headers: (
1071            Headers | Mapping[str, str | bytes] | Iterable[tuple[bytes, bytes]]
1072        ) = (),
1073    ) -> "Response":
1074"""
1075        Simplified API for creating response objects.
1076        """
1077        if isinstance(headers, Headers):
1078            headers = headers
1079        elif isinstance(headers, dict):
1080            headers = Headers(
1081                (
1082                    always_bytes(k, "utf-8", "surrogateescape"),  # type: ignore
1083                    always_bytes(v, "utf-8", "surrogateescape"),
1084                )
1085                for k, v in headers.items()
1086            )
1087        elif isinstance(headers, Iterable):
1088            headers = Headers(headers)  # type: ignore
1089        else:
1090            raise TypeError(
1091                "Expected headers to be an iterable or dict, but is {}.".format(
1092                    type(headers).__name__
1093                )
1094            )
1095
1096        resp = cls(
1097            b"HTTP/1.1",
1098            status_code,
1099            status_codes.RESPONSES.get(status_code, "").encode(),
1100            headers,
1101            None,
1102            None,
1103            time.time(),
1104            time.time(),
1105        )
1106
1107        # Assign this manually to update the content-length header.
1108        if isinstance(content, bytes):
1109            resp.content = content
1110        elif isinstance(content, str):
1111            resp.text = content
1112        else:
1113            raise TypeError(
1114                f"Expected content to be str or bytes, but is {type(content).__name__}."
1115            )
1116
1117        return resp
```

Simplified API for creating response objects.

status\_code: int View Source

```
1119    @property
1120    defstatus_code(self) -> int:
1121"""
1122        HTTP Status Code, e.g. ``200``.
1123        """
1124        return self.data.status_code
```

HTTP Status Code, e.g. `200`.

reason: str View Source

```
1130    @property
1131    defreason(self) -> str:
1132"""
1133        HTTP reason phrase, for example "Not Found".
1134
1135        HTTP/2 responses do not contain a reason phrase, an empty string will be returned instead.
1136        """
1137        # Encoding: http://stackoverflow.com/a/16674906/934719
1138        return self.data.reason.decode("ISO-8859-1")
```

HTTP reason phrase, for example "Not Found".

HTTP/2 responses do not contain a reason phrase, an empty string will be returned instead.

```
1156    @property
1157    defcookies(
1158        self,
1159    ) -> multidict.MultiDictView[str, tuple[str, multidict.MultiDict[str, str | None]]]:
1160"""
1161        The response cookies. A possibly empty `MultiDictView`, where the keys are cookie
1162        name strings, and values are `(cookie value, attributes)` tuples. Within
1163        attributes, unary attributes (e.g. `HTTPOnly`) are indicated by a `None` value.
1164        Modifications to the MultiDictView update `Response.headers`, and vice versa.
1165
1166        *Warning:* Changes to `attributes` will not be picked up unless you also reassign
1167        the `(cookie value, attributes)` tuple directly in the `MultiDictView`.
1168        """
1169        return multidict.MultiDictView(self._get_cookies, self._set_cookies)
```

The response cookies. A possibly empty `MultiDictView`, where the keys are cookie name strings, and values are `(cookie value, attributes)` tuples. Within attributes, unary attributes (e.g. `HTTPOnly`) are indicated by a `None` value. Modifications to the MultiDictView update `Response.headers`, and vice versa.

*Warning:* Changes to `attributes` will not be picked up unless you also reassign the `(cookie value, attributes)` tuple directly in the `MultiDictView`.

def refresh(self, now=None): View Source

```
1175    defrefresh(self, now=None):
1176"""
1177        This fairly complex and heuristic function refreshes a server
1178        response for replay.
1179
1180         - It adjusts date, expires, and last-modified headers.
1181         - It adjusts cookie expiration.
1182        """
1183        if not now:
1184            now = time.time()
1185        delta = now - self.timestamp_start
1186        refresh_headers = [
1187            "date",
1188            "expires",
1189            "last-modified",
1190        ]
1191        for i in refresh_headers:
1192            if i in self.headers:
1193                d = parsedate_tz(self.headers[i])
1194                if d:
1195                    new = mktime_tz(d) + delta
1196                    try:
1197                        self.headers[i] = formatdate(new, usegmt=True)
1198                    except OSError:  # pragma: no cover
1199                        pass  # value out of bounds on Windows only (which is why we exclude it from coverage).
1200        c = []
1201        for set_cookie_header in self.headers.get_all("set-cookie"):
1202            try:
1203                refreshed = cookies.refresh_set_cookie_header(set_cookie_header, delta)
1204            except ValueError:
1205                refreshed = set_cookie_header
1206            c.append(refreshed)
1207        if c:
1208            self.headers.set_all("set-cookie", c)
```

This fairly complex and heuristic function refreshes a server response for replay.

- It adjusts date, expires, and last-modified headers.
- It adjusts cookie expiration.