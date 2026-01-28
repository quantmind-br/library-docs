---
title: mitmproxy.certs
url: https://docs.mitmproxy.org/stable/api/mitmproxy/certs.html
source: crawler
fetched_at: 2026-01-28T15:03:24.469512273-03:00
rendered_js: false
word_count: 3447
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/certs.py) View Source

```
  1importcontextlib
  2importdatetime
  3importipaddress
  4importlogging
  5importos
  6importsys
  7importwarnings
  8fromcollections.abcimport Iterable
  9fromdataclassesimport dataclass
 10frompathlibimport Path
 11fromtypingimport cast
 12fromtypingimport NewType
 13fromtypingimport Optional
 14fromtypingimport Union
 15
 16importOpenSSL
 17fromcryptographyimport x509
 18fromcryptography.hazmat.primitivesimport hashes
 19fromcryptography.hazmat.primitivesimport serialization
 20fromcryptography.hazmat.primitives.asymmetricimport dsa
 21fromcryptography.hazmat.primitives.asymmetricimport ec
 22fromcryptography.hazmat.primitives.asymmetricimport rsa
 23fromcryptography.hazmat.primitives.asymmetric.typesimport CertificatePublicKeyTypes
 24fromcryptography.hazmat.primitives.serializationimport pkcs12
 25fromcryptography.x509import ExtendedKeyUsageOID
 26fromcryptography.x509import NameOID
 27
 28frommitmproxy.coretypesimport serializable
 29
 30if sys.version_info < (3, 13):  # pragma: no cover
 31    fromtyping_extensionsimport deprecated
 32else:
 33    fromwarningsimport deprecated
 34
 35logger = logging.getLogger(__name__)
 36
 37# Default expiry must not be too long: https://github.com/mitmproxy/mitmproxy/issues/815
 38CA_EXPIRY = datetime.timedelta(days=10 * 365)
 39CERT_EXPIRY = datetime.timedelta(days=365)
 40CRL_EXPIRY = datetime.timedelta(days=7)
 41
 42# Generated with "openssl dhparam". It's too slow to generate this on startup.
 43DEFAULT_DHPARAM = b"""
 44-----BEGIN DH PARAMETERS-----
 45MIICCAKCAgEAyT6LzpwVFS3gryIo29J5icvgxCnCebcdSe/NHMkD8dKJf8suFCg3
 46O2+dguLakSVif/t6dhImxInJk230HmfC8q93hdcg/j8rLGJYDKu3ik6H//BAHKIv
 47j5O9yjU3rXCfmVJQic2Nne39sg3CreAepEts2TvYHhVv3TEAzEqCtOuTjgDv0ntJ
 48Gwpj+BJBRQGG9NvprX1YGJ7WOFBP/hWU7d6tgvE6Xa7T/u9QIKpYHMIkcN/l3ZFB
 49chZEqVlyrcngtSXCROTPcDOQ6Q8QzhaBJS+Z6rcsd7X+haiQqvoFcmaJ08Ks6LQC
 50ZIL2EtYJw8V8z7C0igVEBIADZBI6OTbuuhDwRw//zU1uq52Oc48CIZlGxTYG/Evq
 51o9EWAXUYVzWkDSTeBH1r4z/qLPE2cnhtMxbFxuvK53jGB0emy2y1Ei6IhKshJ5qX
 52IB/aE7SSHyQ3MDHHkCmQJCsOd4Mo26YX61NZ+n501XjqpCBQ2+DfZCBh8Va2wDyv
 53A2Ryg9SUz8j0AXViRNMJgJrr446yro/FuJZwnQcO3WQnXeqSBnURqKjmqkeFP+d8
 546mk2tqJaY507lRNqtGlLnj7f5RNoBFJDCLBNurVgfvq9TCVWKDIFD4vZRjCrnl6I
 55rD693XKIHUCWOjMh1if6omGXKHH40QuME2gNa50+YPn1iYDl88uDbbMCAQI=
 56-----END DH PARAMETERS-----
 57"""
 58
 59
 60classCert(serializable.Serializable):
 61"""Representation of a (TLS) certificate."""
 62
 63    _cert: x509.Certificate
 64
 65    def__init__(self, cert: x509.Certificate):
 66        assert isinstance(cert, x509.Certificate)
 67        self._cert = cert
 68
 69    def__eq__(self, other):
 70        return self.fingerprint() == other.fingerprint()
 71
 72    def__repr__(self):
 73        altnames = [str(x.value) for x in self.altnames]
 74        return f"<Cert(cn={self.cn!r}, altnames={altnames!r})>"
 75
 76    def__hash__(self):
 77        return self._cert.__hash__()
 78
 79    @classmethod
 80    deffrom_state(cls, state):
 81        return cls.from_pem(state)
 82
 83    defget_state(self):
 84        return self.to_pem()
 85
 86    defset_state(self, state):
 87        self._cert = x509.load_pem_x509_certificate(state)
 88
 89    @classmethod
 90    deffrom_pem(cls, data: bytes) -> "Cert":
 91        cert = x509.load_pem_x509_certificate(data)  # type: ignore
 92        return cls(cert)
 93
 94    defto_pem(self) -> bytes:
 95        return self._cert.public_bytes(serialization.Encoding.PEM)
 96
 97    @classmethod
 98    deffrom_pyopenssl(self, x509: OpenSSL.crypto.X509) -> "Cert":
 99        return Cert(x509.to_cryptography())
100
101    @deprecated("Use `to_cryptography` instead.")
102    defto_pyopenssl(self) -> OpenSSL.crypto.X509:  # pragma: no cover
103        return OpenSSL.crypto.X509.from_cryptography(self._cert)
104
105    defto_cryptography(self) -> x509.Certificate:
106        return self._cert
107
108    defpublic_key(self) -> CertificatePublicKeyTypes:
109        return self._cert.public_key()
110
111    deffingerprint(self) -> bytes:
112        return self._cert.fingerprint(hashes.SHA256())
113
114    @property
115    defissuer(self) -> list[tuple[str, str]]:
116        return _name_to_keyval(self._cert.issuer)
117
118    @property
119    defnotbefore(self) -> datetime.datetime:
120        try:
121            # type definitions haven't caught up with new API yet.
122            return self._cert.not_valid_before_utc  # type: ignore
123        except AttributeError:  # pragma: no cover
124            # cryptography < 42.0
125            return self._cert.not_valid_before.replace(tzinfo=datetime.UTC)
126
127    @property
128    defnotafter(self) -> datetime.datetime:
129        try:
130            return self._cert.not_valid_after_utc  # type: ignore
131        except AttributeError:  # pragma: no cover
132            return self._cert.not_valid_after.replace(tzinfo=datetime.UTC)
133
134    defhas_expired(self) -> bool:
135        if sys.version_info < (3, 11):  # pragma: no cover
136            return datetime.datetime.now(datetime.UTC) > self.notafter
137        return datetime.datetime.now(datetime.UTC) > self.notafter
138
139    @property
140    defsubject(self) -> list[tuple[str, str]]:
141        return _name_to_keyval(self._cert.subject)
142
143    @property
144    defserial(self) -> int:
145        return self._cert.serial_number
146
147    @property
148    defis_ca(self) -> bool:
149        constraints: x509.BasicConstraints
150        try:
151            constraints = self._cert.extensions.get_extension_for_class(
152                x509.BasicConstraints
153            ).value
154            return constraints.ca
155        except x509.ExtensionNotFound:
156            return False
157
158    @property
159    defkeyinfo(self) -> tuple[str, int]:
160        public_key = self._cert.public_key()
161        if isinstance(public_key, rsa.RSAPublicKey):
162            return "RSA", public_key.key_size
163        if isinstance(public_key, dsa.DSAPublicKey):
164            return "DSA", public_key.key_size
165        if isinstance(public_key, ec.EllipticCurvePublicKey):
166            return f"EC ({public_key.curve.name})", public_key.key_size
167        return (
168            public_key.__class__.__name__.replace("PublicKey", "").replace("_", ""),
169            getattr(public_key, "key_size", -1),
170        )  # pragma: no cover
171
172    @property
173    defcn(self) -> str | None:
174        attrs = self._cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)
175        if attrs:
176            return cast(str, attrs[0].value)
177        return None
178
179    @property
180    deforganization(self) -> str | None:
181        attrs = self._cert.subject.get_attributes_for_oid(
182            x509.NameOID.ORGANIZATION_NAME
183        )
184        if attrs:
185            return cast(str, attrs[0].value)
186        return None
187
188    @property
189    defaltnames(self) -> x509.GeneralNames:
190"""
191        Get all SubjectAlternativeName DNS altnames.
192        """
193        try:
194            sans = self._cert.extensions.get_extension_for_class(
195                x509.SubjectAlternativeName
196            ).value
197        except x509.ExtensionNotFound:
198            return x509.GeneralNames([])
199        else:
200            return x509.GeneralNames(sans)
201
202    @property
203    defcrl_distribution_points(self) -> list[str]:
204        try:
205            ext = self._cert.extensions.get_extension_for_class(
206                x509.CRLDistributionPoints
207            ).value
208        except x509.ExtensionNotFound:
209            return []
210        else:
211            return [
212                dist_point.full_name[0].value
213                for dist_point in ext
214                if dist_point.full_name
215                and isinstance(dist_point.full_name[0], x509.UniformResourceIdentifier)
216            ]
217
218
219def_name_to_keyval(name: x509.Name) -> list[tuple[str, str]]:
220    parts = []
221    for attr in name:
222        k = attr.rfc4514_string().partition("=")[0]
223        v = cast(str, attr.value)
224        parts.append((k, v))
225    return parts
226
227
228defcreate_ca(
229    organization: str,
230    cn: str,
231    key_size: int,
232) -> tuple[rsa.RSAPrivateKeyWithSerialization, x509.Certificate]:
233    now = datetime.datetime.now()
234
235    private_key = rsa.generate_private_key(
236        public_exponent=65537,
237        key_size=key_size,
238    )  # type: ignore
239    name = x509.Name(
240        [
241            x509.NameAttribute(NameOID.COMMON_NAME, cn),
242            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
243        ]
244    )
245    builder = x509.CertificateBuilder()
246    builder = builder.serial_number(x509.random_serial_number())
247    builder = builder.subject_name(name)
248    builder = builder.not_valid_before(now - datetime.timedelta(days=2))
249    builder = builder.not_valid_after(now + CA_EXPIRY)
250    builder = builder.issuer_name(name)
251    builder = builder.public_key(private_key.public_key())
252    builder = builder.add_extension(
253        x509.BasicConstraints(ca=True, path_length=None), critical=True
254    )
255    builder = builder.add_extension(
256        x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]), critical=False
257    )
258    builder = builder.add_extension(
259        x509.KeyUsage(
260            digital_signature=False,
261            content_commitment=False,
262            key_encipherment=False,
263            data_encipherment=False,
264            key_agreement=False,
265            key_cert_sign=True,
266            crl_sign=True,
267            encipher_only=False,
268            decipher_only=False,
269        ),
270        critical=True,
271    )
272    builder = builder.add_extension(
273        x509.SubjectKeyIdentifier.from_public_key(private_key.public_key()),
274        critical=False,
275    )
276    cert = builder.sign(private_key=private_key, algorithm=hashes.SHA256())  # type: ignore
277    return private_key, cert
278
279
280def_fix_legacy_sans(sans: Iterable[x509.GeneralName] | list[str]) -> x509.GeneralNames:
281"""
282    SANs used to be a list of strings in mitmproxy 10.1 and below, but now they're a list of GeneralNames.
283    This function converts the old format to the new one.
284    """
285    if isinstance(sans, x509.GeneralNames):
286        return sans
287    elif (
288        isinstance(sans, list) and len(sans) > 0 and isinstance(sans[0], str)
289    ):  # pragma: no cover
290        warnings.warn(
291            "Passing SANs as a list of strings is deprecated.",
292            DeprecationWarning,
293            stacklevel=2,
294        )
295
296        ss: list[x509.GeneralName] = []
297        for x in cast(list[str], sans):
298            try:
299                ip = ipaddress.ip_address(x)
300            except ValueError:
301                x = x.encode("idna").decode()
302                ss.append(x509.DNSName(x))
303            else:
304                ss.append(x509.IPAddress(ip))
305        return x509.GeneralNames(ss)
306    else:
307        return x509.GeneralNames(cast(Iterable[x509.GeneralName], sans))
308
309
310defdummy_cert(
311    privkey: rsa.RSAPrivateKey,
312    cacert: x509.Certificate,
313    commonname: str | None,
314    sans: Iterable[x509.GeneralName],
315    organization: str | None = None,
316    crl_url: str | None = None,
317) -> Cert:
318"""
319    Generates a dummy certificate.
320
321    privkey: CA private key
322    cacert: CA certificate
323    commonname: Common name for the generated certificate.
324    sans: A list of Subject Alternate Names.
325    organization: Organization name for the generated certificate.
326    crl_url: URL of CRL distribution point
327
328    Returns cert if operation succeeded, None if not.
329    """
330    builder = x509.CertificateBuilder()
331    builder = builder.issuer_name(cacert.subject)
332    builder = builder.add_extension(
333        x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]), critical=False
334    )
335    builder = builder.public_key(cacert.public_key())
336
337    now = datetime.datetime.now()
338    builder = builder.not_valid_before(now - datetime.timedelta(days=2))
339    builder = builder.not_valid_after(now + CERT_EXPIRY)
340
341    subject = []
342    is_valid_commonname = commonname is not None and len(commonname) < 64
343    if is_valid_commonname:
344        assert commonname is not None
345        subject.append(x509.NameAttribute(NameOID.COMMON_NAME, commonname))
346    if organization is not None:
347        assert organization is not None
348        subject.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization))
349    builder = builder.subject_name(x509.Name(subject))
350    builder = builder.serial_number(x509.random_serial_number())
351
352    # RFC 5280 §4.2.1.6: subjectAltName is critical if subject is empty.
353    builder = builder.add_extension(
354        x509.SubjectAlternativeName(_fix_legacy_sans(sans)),
355        critical=not is_valid_commonname,
356    )
357
358    # https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1
359    builder = builder.add_extension(
360        x509.AuthorityKeyIdentifier.from_issuer_public_key(cacert.public_key()),  # type: ignore
361        critical=False,
362    )
363    # If CA and leaf cert have the same Subject Key Identifier, SChannel breaks in funny ways,
364    # see https://github.com/mitmproxy/mitmproxy/issues/6494.
365    # https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2 states
366    # that SKI is optional for the leaf cert, so we skip that.
367
368    if crl_url:
369        builder = builder.add_extension(
370            x509.CRLDistributionPoints(
371                [
372                    x509.DistributionPoint(
373                        [x509.UniformResourceIdentifier(crl_url)],
374                        relative_name=None,
375                        crl_issuer=None,
376                        reasons=None,
377                    )
378                ]
379            ),
380            critical=False,
381        )
382
383    cert = builder.sign(private_key=privkey, algorithm=hashes.SHA256())  # type: ignore
384    return Cert(cert)
385
386
387defdummy_crl(
388    privkey: rsa.RSAPrivateKey,
389    cacert: x509.Certificate,
390) -> bytes:
391"""
392    Generates an empty CRL signed with the CA key
393
394    privkey: CA private key
395    cacert: CA certificate
396
397    Returns a CRL DER encoded
398    """
399    builder = x509.CertificateRevocationListBuilder()
400    builder = builder.issuer_name(cacert.issuer)
401
402    now = datetime.datetime.now()
403    builder = builder.last_update(now - datetime.timedelta(days=2))
404    builder = builder.next_update(now + CRL_EXPIRY)
405
406    builder = builder.add_extension(x509.CRLNumber(1000), False)  # meaningless number
407    crl = builder.sign(private_key=privkey, algorithm=hashes.SHA256())
408    return crl.public_bytes(serialization.Encoding.DER)
409
410
411@dataclass(frozen=True)
412classCertStoreEntry:
413    cert: Cert
414    privatekey: rsa.RSAPrivateKey
415    chain_file: Path | None
416    chain_certs: list[Cert]
417
418
419TCustomCertId = str  # manually provided certs (e.g. mitmproxy's --certs)
420TGeneratedCertId = tuple[Optional[str], x509.GeneralNames]  # (common_name, sans)
421TCertId = Union[TCustomCertId, TGeneratedCertId]
422
423DHParams = NewType("DHParams", bytes)
424
425
426classCertStore:
427"""
428    Implements an in-memory certificate store.
429    """
430
431    STORE_CAP = 100
432    default_privatekey: rsa.RSAPrivateKey
433    default_ca: Cert
434    default_chain_file: Path | None
435    default_chain_certs: list[Cert]
436    dhparams: DHParams
437    certs: dict[TCertId, CertStoreEntry]
438    expire_queue: list[CertStoreEntry]
439
440    def__init__(
441        self,
442        default_privatekey: rsa.RSAPrivateKey,
443        default_ca: Cert,
444        default_chain_file: Path | None,
445        default_crl: bytes,
446        dhparams: DHParams,
447    ):
448        self.default_privatekey = default_privatekey
449        self.default_ca = default_ca
450        self.default_chain_file = default_chain_file
451        self.default_crl = default_crl
452        self.default_chain_certs = (
453            [
454                Cert(c)
455                for c in x509.load_pem_x509_certificates(
456                    self.default_chain_file.read_bytes()
457                )
458            ]
459            if self.default_chain_file
460            else [default_ca]
461        )
462        self.dhparams = dhparams
463        self.certs = {}
464        self.expire_queue = []
465
466    defexpire(self, entry: CertStoreEntry) -> None:
467        self.expire_queue.append(entry)
468        if len(self.expire_queue) > self.STORE_CAP:
469            d = self.expire_queue.pop(0)
470            self.certs = {k: v for k, v in self.certs.items() if v != d}
471
472    @staticmethod
473    defload_dhparam(path: Path) -> DHParams:
474        # mitmproxy<=0.10 doesn't generate a dhparam file.
475        # Create it now if necessary.
476        if not path.exists():
477            path.write_bytes(DEFAULT_DHPARAM)
478
479        # we could use cryptography for this, but it's unclear how to convert cryptography's object to pyOpenSSL's
480        # expected format.
481        bio = OpenSSL.SSL._lib.BIO_new_file(  # type: ignore
482            str(path).encode(sys.getfilesystemencoding()), b"r"
483        )
484        if bio != OpenSSL.SSL._ffi.NULL:  # type: ignore
485            bio = OpenSSL.SSL._ffi.gc(bio, OpenSSL.SSL._lib.BIO_free)  # type: ignore
486            dh = OpenSSL.SSL._lib.PEM_read_bio_DHparams(  # type: ignore
487                bio,
488                OpenSSL.SSL._ffi.NULL,  # type: ignore
489                OpenSSL.SSL._ffi.NULL,  # type: ignore
490                OpenSSL.SSL._ffi.NULL,  # type: ignore
491            )
492            dh = OpenSSL.SSL._ffi.gc(dh, OpenSSL.SSL._lib.DH_free)  # type: ignore
493            return dh
494        raise RuntimeError("Error loading DH Params.")  # pragma: no cover
495
496    @classmethod
497    deffrom_store(
498        cls,
499        path: Path | str,
500        basename: str,
501        key_size: int,
502        passphrase: bytes | None = None,
503    ) -> "CertStore":
504        path = Path(path)
505        ca_file = path / f"{basename}-ca.pem"
506        dhparam_file = path / f"{basename}-dhparam.pem"
507        if not ca_file.exists():
508            cls.create_store(path, basename, key_size)
509        return cls.from_files(ca_file, dhparam_file, passphrase)
510
511    @classmethod
512    deffrom_files(
513        cls, ca_file: Path, dhparam_file: Path, passphrase: bytes | None = None
514    ) -> "CertStore":
515        raw = ca_file.read_bytes()
516        key = load_pem_private_key(raw, passphrase)
517        dh = cls.load_dhparam(dhparam_file)
518        certs = x509.load_pem_x509_certificates(raw)
519        ca = Cert(certs[0])
520        crl = dummy_crl(key, ca._cert)
521        if len(certs) > 1:
522            chain_file: Path | None = ca_file
523        else:
524            chain_file = None
525        return cls(key, ca, chain_file, crl, dh)
526
527    @staticmethod
528    @contextlib.contextmanager
529    defumask_secret():
530"""
531        Context to temporarily set umask to its original value bitor 0o77.
532        Useful when writing private keys to disk so that only the owner
533        will be able to read them.
534        """
535        original_umask = os.umask(0)
536        os.umask(original_umask | 0o77)
537        try:
538            yield
539        finally:
540            os.umask(original_umask)
541
542    @staticmethod
543    defcreate_store(
544        path: Path, basename: str, key_size: int, organization=None, cn=None
545    ) -> None:
546        path.mkdir(parents=True, exist_ok=True)
547
548        organization = organization or basename
549        cn = cn or basename
550
551        key: rsa.RSAPrivateKeyWithSerialization
552        ca: x509.Certificate
553        key, ca = create_ca(organization=organization, cn=cn, key_size=key_size)
554
555        # Dump the CA plus private key.
556        with CertStore.umask_secret():
557            # PEM format
558            (path / f"{basename}-ca.pem").write_bytes(
559                key.private_bytes(
560                    encoding=serialization.Encoding.PEM,
561                    format=serialization.PrivateFormat.TraditionalOpenSSL,
562                    encryption_algorithm=serialization.NoEncryption(),
563                )
564                + ca.public_bytes(serialization.Encoding.PEM)
565            )
566
567            # PKCS12 format for Windows devices
568            (path / f"{basename}-ca.p12").write_bytes(
569                pkcs12.serialize_key_and_certificates(  # type: ignore
570                    name=basename.encode(),
571                    key=key,
572                    cert=ca,
573                    cas=None,
574                    encryption_algorithm=serialization.NoEncryption(),
575                )
576            )
577
578        # Dump the certificate in PEM format
579        pem_cert = ca.public_bytes(serialization.Encoding.PEM)
580        (path / f"{basename}-ca-cert.pem").write_bytes(pem_cert)
581        # Create a .cer file with the same contents for Android
582        (path / f"{basename}-ca-cert.cer").write_bytes(pem_cert)
583
584        # Dump the certificate in PKCS12 format for Windows devices
585        (path / f"{basename}-ca-cert.p12").write_bytes(
586            pkcs12.serialize_key_and_certificates(
587                name=basename.encode(),
588                key=None,  # type: ignore
589                cert=ca,
590                cas=None,
591                encryption_algorithm=serialization.NoEncryption(),
592            )
593        )
594
595        (path / f"{basename}-dhparam.pem").write_bytes(DEFAULT_DHPARAM)
596
597    defadd_cert_file(
598        self, spec: str, path: Path, passphrase: bytes | None = None
599    ) -> None:
600        raw = path.read_bytes()
601        cert = Cert.from_pem(raw)
602        try:
603            private_key = load_pem_private_key(raw, password=passphrase)
604        except ValueError as e:
605            private_key = self.default_privatekey
606            if cert.public_key() != private_key.public_key():
607                raise ValueError(
608                    f'Unable to find private key in "{path.absolute()}": {e}'
609                ) frome
610        else:
611            if cert.public_key() != private_key.public_key():
612                raise ValueError(
613                    f'Private and public keys in "{path.absolute()}" do not match:\n'
614                    f"{cert.public_key()=}\n"
615                    f"{private_key.public_key()=}"
616                )
617
618        try:
619            chain = [Cert(x) for x in x509.load_pem_x509_certificates(raw)]
620        except ValueError as e:
621            logger.warning(f"Failed to read certificate chain: {e}")
622            chain = [cert]
623
624        if cert.is_ca:
625            logger.warning(
626                f'"{path.absolute()}" is a certificate authority and not a leaf certificate. '
627                f"This indicates a misconfiguration, see https://docs.mitmproxy.org/stable/concepts-certificates/."
628            )
629
630        self.add_cert(CertStoreEntry(cert, private_key, path, chain), spec)
631
632    defadd_cert(self, entry: CertStoreEntry, *names: str) -> None:
633"""
634        Adds a cert to the certstore. We register the CN in the cert plus
635        any SANs, and also the list of names provided as an argument.
636        """
637        if entry.cert.cn:
638            self.certs[entry.cert.cn] = entry
639        for i in entry.cert.altnames:
640            self.certs[str(i.value)] = entry
641        for i in names:
642            self.certs[i] = entry
643
644    @staticmethod
645    defasterisk_forms(dn: str | x509.GeneralName) -> list[str]:
646"""
647        Return all asterisk forms for a domain. For example, for www.example.com this will return
648        [b"www.example.com", b"*.example.com", b"*.com"]. The single wildcard "*" is omitted.
649        """
650        if isinstance(dn, str):
651            parts = dn.split(".")
652            ret = [dn]
653            for i in range(1, len(parts)):
654                ret.append("*." + ".".join(parts[i:]))
655            return ret
656        elif isinstance(dn, x509.DNSName):
657            return CertStore.asterisk_forms(dn.value)
658        else:
659            return [str(dn.value)]
660
661    defget_cert(
662        self,
663        commonname: str | None,
664        sans: Iterable[x509.GeneralName],
665        organization: str | None = None,
666        crl_url: str | None = None,
667    ) -> CertStoreEntry:
668"""
669        commonname: Common name for the generated certificate. Must be a
670        valid, plain-ASCII, IDNA-encoded domain name.
671
672        sans: A list of Subject Alternate Names.
673
674        organization: Organization name for the generated certificate.
675
676        crl_url: URL of CRL distribution point
677        """
678        sans = _fix_legacy_sans(sans)
679
680        potential_keys: list[TCertId] = []
681        if commonname:
682            potential_keys.extend(self.asterisk_forms(commonname))
683        for s in sans:
684            potential_keys.extend(self.asterisk_forms(s))
685        potential_keys.append("*")
686        potential_keys.append((commonname, sans))
687
688        name = next(filter(lambda key: key in self.certs, potential_keys), None)
689        if name:
690            entry = self.certs[name]
691        else:
692            entry = CertStoreEntry(
693                cert=dummy_cert(
694                    self.default_privatekey,
695                    self.default_ca._cert,
696                    commonname,
697                    sans,
698                    organization,
699                    crl_url,
700                ),
701                privatekey=self.default_privatekey,
702                chain_file=self.default_chain_file,
703                chain_certs=self.default_chain_certs,
704            )
705            self.certs[(commonname, sans)] = entry
706            self.expire(entry)
707
708        return entry
709
710
711defload_pem_private_key(data: bytes, password: bytes | None) -> rsa.RSAPrivateKey:
712"""
713    like cryptography's load_pem_private_key, but silently falls back to not using a password
714    if the private key is unencrypted.
715    """
716    try:
717        return serialization.load_pem_private_key(data, password)  # type: ignore
718    except TypeError:
719        if password is not None:
720            return load_pem_private_key(data, None)
721        raise
```

class Cert(mitmproxy.coretypes.serializable.Serializable): View Source

[](#Cert)

```
 61classCert(serializable.Serializable):
 62"""Representation of a (TLS) certificate."""
 63
 64    _cert: x509.Certificate
 65
 66    def__init__(self, cert: x509.Certificate):
 67        assert isinstance(cert, x509.Certificate)
 68        self._cert = cert
 69
 70    def__eq__(self, other):
 71        return self.fingerprint() == other.fingerprint()
 72
 73    def__repr__(self):
 74        altnames = [str(x.value) for x in self.altnames]
 75        return f"<Cert(cn={self.cn!r}, altnames={altnames!r})>"
 76
 77    def__hash__(self):
 78        return self._cert.__hash__()
 79
 80    @classmethod
 81    deffrom_state(cls, state):
 82        return cls.from_pem(state)
 83
 84    defget_state(self):
 85        return self.to_pem()
 86
 87    defset_state(self, state):
 88        self._cert = x509.load_pem_x509_certificate(state)
 89
 90    @classmethod
 91    deffrom_pem(cls, data: bytes) -> "Cert":
 92        cert = x509.load_pem_x509_certificate(data)  # type: ignore
 93        return cls(cert)
 94
 95    defto_pem(self) -> bytes:
 96        return self._cert.public_bytes(serialization.Encoding.PEM)
 97
 98    @classmethod
 99    deffrom_pyopenssl(self, x509: OpenSSL.crypto.X509) -> "Cert":
100        return Cert(x509.to_cryptography())
101
102    @deprecated("Use `to_cryptography` instead.")
103    defto_pyopenssl(self) -> OpenSSL.crypto.X509:  # pragma: no cover
104        return OpenSSL.crypto.X509.from_cryptography(self._cert)
105
106    defto_cryptography(self) -> x509.Certificate:
107        return self._cert
108
109    defpublic_key(self) -> CertificatePublicKeyTypes:
110        return self._cert.public_key()
111
112    deffingerprint(self) -> bytes:
113        return self._cert.fingerprint(hashes.SHA256())
114
115    @property
116    defissuer(self) -> list[tuple[str, str]]:
117        return _name_to_keyval(self._cert.issuer)
118
119    @property
120    defnotbefore(self) -> datetime.datetime:
121        try:
122            # type definitions haven't caught up with new API yet.
123            return self._cert.not_valid_before_utc  # type: ignore
124        except AttributeError:  # pragma: no cover
125            # cryptography < 42.0
126            return self._cert.not_valid_before.replace(tzinfo=datetime.UTC)
127
128    @property
129    defnotafter(self) -> datetime.datetime:
130        try:
131            return self._cert.not_valid_after_utc  # type: ignore
132        except AttributeError:  # pragma: no cover
133            return self._cert.not_valid_after.replace(tzinfo=datetime.UTC)
134
135    defhas_expired(self) -> bool:
136        if sys.version_info < (3, 11):  # pragma: no cover
137            return datetime.datetime.now(datetime.UTC) > self.notafter
138        return datetime.datetime.now(datetime.UTC) > self.notafter
139
140    @property
141    defsubject(self) -> list[tuple[str, str]]:
142        return _name_to_keyval(self._cert.subject)
143
144    @property
145    defserial(self) -> int:
146        return self._cert.serial_number
147
148    @property
149    defis_ca(self) -> bool:
150        constraints: x509.BasicConstraints
151        try:
152            constraints = self._cert.extensions.get_extension_for_class(
153                x509.BasicConstraints
154            ).value
155            return constraints.ca
156        except x509.ExtensionNotFound:
157            return False
158
159    @property
160    defkeyinfo(self) -> tuple[str, int]:
161        public_key = self._cert.public_key()
162        if isinstance(public_key, rsa.RSAPublicKey):
163            return "RSA", public_key.key_size
164        if isinstance(public_key, dsa.DSAPublicKey):
165            return "DSA", public_key.key_size
166        if isinstance(public_key, ec.EllipticCurvePublicKey):
167            return f"EC ({public_key.curve.name})", public_key.key_size
168        return (
169            public_key.__class__.__name__.replace("PublicKey", "").replace("_", ""),
170            getattr(public_key, "key_size", -1),
171        )  # pragma: no cover
172
173    @property
174    defcn(self) -> str | None:
175        attrs = self._cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)
176        if attrs:
177            return cast(str, attrs[0].value)
178        return None
179
180    @property
181    deforganization(self) -> str | None:
182        attrs = self._cert.subject.get_attributes_for_oid(
183            x509.NameOID.ORGANIZATION_NAME
184        )
185        if attrs:
186            return cast(str, attrs[0].value)
187        return None
188
189    @property
190    defaltnames(self) -> x509.GeneralNames:
191"""
192        Get all SubjectAlternativeName DNS altnames.
193        """
194        try:
195            sans = self._cert.extensions.get_extension_for_class(
196                x509.SubjectAlternativeName
197            ).value
198        except x509.ExtensionNotFound:
199            return x509.GeneralNames([])
200        else:
201            return x509.GeneralNames(sans)
202
203    @property
204    defcrl_distribution_points(self) -> list[str]:
205        try:
206            ext = self._cert.extensions.get_extension_for_class(
207                x509.CRLDistributionPoints
208            ).value
209        except x509.ExtensionNotFound:
210            return []
211        else:
212            return [
213                dist_point.full_name[0].value
214                for dist_point in ext
215                if dist_point.full_name
216                and isinstance(dist_point.full_name[0], x509.UniformResourceIdentifier)
217            ]
```

Representation of a (TLS) certificate.

Cert(cert: cryptography.hazmat.bindings.\_rust.x509.Certificate) View Source

```
66    def__init__(self, cert: x509.Certificate):
67        assert isinstance(cert, x509.Certificate)
68        self._cert = cert
```

@classmethod

def from\_pem(cls, data: bytes) -&gt; [Cert](#Cert): View Source

```
90    @classmethod
91    deffrom_pem(cls, data: bytes) -> "Cert":
92        cert = x509.load_pem_x509_certificate(data)  # type: ignore
93        return cls(cert)
```

def to\_pem(self) -&gt; bytes: View Source

```
95    defto_pem(self) -> bytes:
96        return self._cert.public_bytes(serialization.Encoding.PEM)
```

@classmethod

def from\_pyopenssl(self, x509: OpenSSL.crypto.X509) -&gt; [Cert](#Cert): View Source

```
 98    @classmethod
 99    deffrom_pyopenssl(self, x509: OpenSSL.crypto.X509) -> "Cert":
100        return Cert(x509.to_cryptography())
```

@deprecated('Use \`to\_cryptography\` instead.')

def to\_pyopenssl(self) -&gt; OpenSSL.crypto.X509: View Source

```
102    @deprecated("Use `to_cryptography` instead.")
103    defto_pyopenssl(self) -> OpenSSL.crypto.X509:  # pragma: no cover
104        return OpenSSL.crypto.X509.from_cryptography(self._cert)
```

def to\_cryptography(self) -&gt; cryptography.hazmat.bindings.\_rust.x509.Certificate: View Source

```
106    defto_cryptography(self) -> x509.Certificate:
107        return self._cert
```

def public\_key( self) -&gt; cryptography.hazmat.primitives.asymmetric.dsa.DSAPublicKey | cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey | cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicKey | cryptography.hazmat.primitives.asymmetric.ed25519.Ed25519PublicKey | cryptography.hazmat.primitives.asymmetric.ed448.Ed448PublicKey | cryptography.hazmat.primitives.asymmetric.x25519.X25519PublicKey | cryptography.hazmat.primitives.asymmetric.x448.X448PublicKey: View Source

```
109    defpublic_key(self) -> CertificatePublicKeyTypes:
110        return self._cert.public_key()
```

def fingerprint(self) -&gt; bytes: View Source

```
112    deffingerprint(self) -> bytes:
113        return self._cert.fingerprint(hashes.SHA256())
```

issuer: list\[tuple\[str, str]] View Source

```
115    @property
116    defissuer(self) -> list[tuple[str, str]]:
117        return _name_to_keyval(self._cert.issuer)
```

notbefore: datetime.datetime View Source

```
119    @property
120    defnotbefore(self) -> datetime.datetime:
121        try:
122            # type definitions haven't caught up with new API yet.
123            return self._cert.not_valid_before_utc  # type: ignore
124        except AttributeError:  # pragma: no cover
125            # cryptography < 42.0
126            return self._cert.not_valid_before.replace(tzinfo=datetime.UTC)
```

notafter: datetime.datetime View Source

```
128    @property
129    defnotafter(self) -> datetime.datetime:
130        try:
131            return self._cert.not_valid_after_utc  # type: ignore
132        except AttributeError:  # pragma: no cover
133            return self._cert.not_valid_after.replace(tzinfo=datetime.UTC)
```

def has\_expired(self) -&gt; bool: View Source

```
135    defhas_expired(self) -> bool:
136        if sys.version_info < (3, 11):  # pragma: no cover
137            return datetime.datetime.now(datetime.UTC) > self.notafter
138        return datetime.datetime.now(datetime.UTC) > self.notafter
```

subject: list\[tuple\[str, str]] View Source

```
140    @property
141    defsubject(self) -> list[tuple[str, str]]:
142        return _name_to_keyval(self._cert.subject)
```

serial: int View Source

```
144    @property
145    defserial(self) -> int:
146        return self._cert.serial_number
```

is\_ca: bool View Source

```
148    @property
149    defis_ca(self) -> bool:
150        constraints: x509.BasicConstraints
151        try:
152            constraints = self._cert.extensions.get_extension_for_class(
153                x509.BasicConstraints
154            ).value
155            return constraints.ca
156        except x509.ExtensionNotFound:
157            return False
```

keyinfo: tuple\[str, int] View Source

```
159    @property
160    defkeyinfo(self) -> tuple[str, int]:
161        public_key = self._cert.public_key()
162        if isinstance(public_key, rsa.RSAPublicKey):
163            return "RSA", public_key.key_size
164        if isinstance(public_key, dsa.DSAPublicKey):
165            return "DSA", public_key.key_size
166        if isinstance(public_key, ec.EllipticCurvePublicKey):
167            return f"EC ({public_key.curve.name})", public_key.key_size
168        return (
169            public_key.__class__.__name__.replace("PublicKey", "").replace("_", ""),
170            getattr(public_key, "key_size", -1),
171        )  # pragma: no cover
```

cn: str | None View Source

```
173    @property
174    defcn(self) -> str | None:
175        attrs = self._cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)
176        if attrs:
177            return cast(str, attrs[0].value)
178        return None
```

organization: str | None View Source

```
180    @property
181    deforganization(self) -> str | None:
182        attrs = self._cert.subject.get_attributes_for_oid(
183            x509.NameOID.ORGANIZATION_NAME
184        )
185        if attrs:
186            return cast(str, attrs[0].value)
187        return None
```

altnames: cryptography.x509.extensions.GeneralNames View Source

```
189    @property
190    defaltnames(self) -> x509.GeneralNames:
191"""
192        Get all SubjectAlternativeName DNS altnames.
193        """
194        try:
195            sans = self._cert.extensions.get_extension_for_class(
196                x509.SubjectAlternativeName
197            ).value
198        except x509.ExtensionNotFound:
199            return x509.GeneralNames([])
200        else:
201            return x509.GeneralNames(sans)
```

Get all SubjectAlternativeName DNS altnames.

crl\_distribution\_points: list\[str] View Source

```
203    @property
204    defcrl_distribution_points(self) -> list[str]:
205        try:
206            ext = self._cert.extensions.get_extension_for_class(
207                x509.CRLDistributionPoints
208            ).value
209        except x509.ExtensionNotFound:
210            return []
211        else:
212            return [
213                dist_point.full_name[0].value
214                for dist_point in ext
215                if dist_point.full_name
216                and isinstance(dist_point.full_name[0], x509.UniformResourceIdentifier)
217            ]
```