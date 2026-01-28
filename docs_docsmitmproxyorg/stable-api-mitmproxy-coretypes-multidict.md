---
title: mitmproxy.coretypes.multidict
url: https://docs.mitmproxy.org/stable/api/mitmproxy/coretypes/multidict.html
source: crawler
fetched_at: 2026-01-28T15:03:24.474005752-03:00
rendered_js: false
word_count: 1942
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/coretypes/multidict.py) View Source

```
  1fromabcimport ABCMeta
  2fromabcimport abstractmethod
  3fromcollections.abcimport Iterator
  4fromcollections.abcimport MutableMapping
  5fromcollections.abcimport Sequence
  6fromtypingimport TypeVar
  7
  8frommitmproxy.coretypesimport serializable
  9
 10KT = TypeVar("KT")
 11VT = TypeVar("VT")
 12
 13
 14class_MultiDict(MutableMapping[KT, VT], metaclass=ABCMeta):
 15"""
 16    A MultiDict is a dictionary-like data structure that supports multiple values per key.
 17    """
 18
 19    fields: tuple[tuple[KT, VT], ...]
 20"""The underlying raw datastructure."""
 21
 22    def__repr__(self):
 23        fields = (repr(field) for field in self.fields)
 24        return "{cls}[{fields}]".format(
 25            cls=type(self).__name__, fields=", ".join(fields)
 26        )
 27
 28    @staticmethod
 29    @abstractmethod
 30    def_reduce_values(values: Sequence[VT]) -> VT:
 31"""
 32        If a user accesses multidict["foo"], this method
 33        reduces all values for "foo" to a single value that is returned.
 34        For example, HTTP headers are folded, whereas we will just take
 35        the first cookie we found with that name.
 36        """
 37
 38    @staticmethod
 39    @abstractmethod
 40    def_kconv(key: KT) -> KT:
 41"""
 42        This method converts a key to its canonical representation.
 43        For example, HTTP headers are case-insensitive, so this method returns key.lower().
 44        """
 45
 46    def__getitem__(self, key: KT) -> VT:
 47        values = self.get_all(key)
 48        if not values:
 49            raise KeyError(key)
 50        return self._reduce_values(values)
 51
 52    def__setitem__(self, key: KT, value: VT) -> None:
 53        self.set_all(key, [value])
 54
 55    def__delitem__(self, key: KT) -> None:
 56        if key not in self:
 57            raise KeyError(key)
 58        key = self._kconv(key)
 59        self.fields = tuple(
 60            field for field in self.fields if key != self._kconv(field[0])
 61        )
 62
 63    def__iter__(self) -> Iterator[KT]:
 64        seen = set()
 65        for key, _ in self.fields:
 66            key_kconv = self._kconv(key)
 67            if key_kconv not in seen:
 68                seen.add(key_kconv)
 69                yield key
 70
 71    def__len__(self) -> int:
 72        return len({self._kconv(key) for key, _ in self.fields})
 73
 74    def__eq__(self, other) -> bool:
 75        if isinstance(other, MultiDict):
 76            return self.fields == other.fields
 77        return False
 78
 79    defget_all(self, key: KT) -> list[VT]:
 80"""
 81        Return the list of all values for a given key.
 82        If that key is not in the MultiDict, the return value will be an empty list.
 83        """
 84        key = self._kconv(key)
 85        return [value for k, value in self.fields if self._kconv(k) == key]
 86
 87    defset_all(self, key: KT, values: list[VT]) -> None:
 88"""
 89        Remove the old values for a key and add new ones.
 90        """
 91        key_kconv = self._kconv(key)
 92
 93        new_fields: list[tuple[KT, VT]] = []
 94        for field in self.fields:
 95            if self._kconv(field[0]) == key_kconv:
 96                if values:
 97                    new_fields.append((field[0], values.pop(0)))
 98            else:
 99                new_fields.append(field)
100        while values:
101            new_fields.append((key, values.pop(0)))
102        self.fields = tuple(new_fields)
103
104    defadd(self, key: KT, value: VT) -> None:
105"""
106        Add an additional value for the given key at the bottom.
107        """
108        self.insert(len(self.fields), key, value)
109
110    definsert(self, index: int, key: KT, value: VT) -> None:
111"""
112        Insert an additional value for the given key at the specified position.
113        """
114        item = (key, value)
115        self.fields = self.fields[:index] + (item,) + self.fields[index:]
116
117    defkeys(self, multi: bool = False):
118"""
119        Get all keys.
120
121        If `multi` is True, one key per value will be returned.
122        If `multi` is False, duplicate keys will only be returned once.
123        """
124        return (k for k, _ in self.items(multi))
125
126    defvalues(self, multi: bool = False):
127"""
128        Get all values.
129
130        If `multi` is True, all values will be returned.
131        If `multi` is False, only the first value per key will be returned.
132        """
133        return (v for _, v in self.items(multi))
134
135    defitems(self, multi: bool = False):
136"""
137        Get all (key, value) tuples.
138
139        If `multi` is True, all `(key, value)` pairs will be returned.
140        If False, only one tuple per key is returned.
141        """
142        if multi:
143            return self.fields
144        else:
145            return super().items()
146
147
148classMultiDict(_MultiDict[KT, VT], serializable.Serializable):
149"""A concrete MultiDict, storing its own data."""
150
151    def__init__(self, fields=()):
152        super().__init__()
153        self.fields = tuple(tuple(i) for i in fields)  # type: ignore
154
155    @staticmethod
156    def_reduce_values(values):
157        return values[0]
158
159    @staticmethod
160    def_kconv(key):
161        return key
162
163    defget_state(self):
164        return self.fields
165
166    defset_state(self, state):
167        self.fields = tuple(tuple(x) for x in state)  # type: ignore
168
169    @classmethod
170    deffrom_state(cls, state):
171        return cls(state)
172
173
174classMultiDictView(_MultiDict[KT, VT]):
175"""
176    The MultiDictView provides the MultiDict interface over calculated data.
177    The view itself contains no state - data is retrieved from the parent on
178    request, and stored back to the parent on change.
179    """
180
181    def__init__(self, getter, setter):
182        self._getter = getter
183        self._setter = setter
184        super().__init__()
185
186    @staticmethod
187    def_kconv(key):
188        # All request-attributes are case-sensitive.
189        return key
190
191    @staticmethod
192    def_reduce_values(values):
193        # We just return the first element if
194        # multiple elements exist with the same key.
195        return values[0]
196
197    @property  # type: ignore
198    deffields(self):
199        return self._getter()
200
201    @fields.setter
202    deffields(self, value):
203        self._setter(value)
204
205    defcopy(self) -> "MultiDict[KT,VT]":
206        return MultiDict(self.fields)
```

class \_MultiDict(collections.abc.MutableMapping\[~KT, ~VT]): View Source

[](#_MultiDict)

```
 15class_MultiDict(MutableMapping[KT, VT], metaclass=ABCMeta):
 16"""
 17    A MultiDict is a dictionary-like data structure that supports multiple values per key.
 18    """
 19
 20    fields: tuple[tuple[KT, VT], ...]
 21"""The underlying raw datastructure."""
 22
 23    def__repr__(self):
 24        fields = (repr(field) for field in self.fields)
 25        return "{cls}[{fields}]".format(
 26            cls=type(self).__name__, fields=", ".join(fields)
 27        )
 28
 29    @staticmethod
 30    @abstractmethod
 31    def_reduce_values(values: Sequence[VT]) -> VT:
 32"""
 33        If a user accesses multidict["foo"], this method
 34        reduces all values for "foo" to a single value that is returned.
 35        For example, HTTP headers are folded, whereas we will just take
 36        the first cookie we found with that name.
 37        """
 38
 39    @staticmethod
 40    @abstractmethod
 41    def_kconv(key: KT) -> KT:
 42"""
 43        This method converts a key to its canonical representation.
 44        For example, HTTP headers are case-insensitive, so this method returns key.lower().
 45        """
 46
 47    def__getitem__(self, key: KT) -> VT:
 48        values = self.get_all(key)
 49        if not values:
 50            raise KeyError(key)
 51        return self._reduce_values(values)
 52
 53    def__setitem__(self, key: KT, value: VT) -> None:
 54        self.set_all(key, [value])
 55
 56    def__delitem__(self, key: KT) -> None:
 57        if key not in self:
 58            raise KeyError(key)
 59        key = self._kconv(key)
 60        self.fields = tuple(
 61            field for field in self.fields if key != self._kconv(field[0])
 62        )
 63
 64    def__iter__(self) -> Iterator[KT]:
 65        seen = set()
 66        for key, _ in self.fields:
 67            key_kconv = self._kconv(key)
 68            if key_kconv not in seen:
 69                seen.add(key_kconv)
 70                yield key
 71
 72    def__len__(self) -> int:
 73        return len({self._kconv(key) for key, _ in self.fields})
 74
 75    def__eq__(self, other) -> bool:
 76        if isinstance(other, MultiDict):
 77            return self.fields == other.fields
 78        return False
 79
 80    defget_all(self, key: KT) -> list[VT]:
 81"""
 82        Return the list of all values for a given key.
 83        If that key is not in the MultiDict, the return value will be an empty list.
 84        """
 85        key = self._kconv(key)
 86        return [value for k, value in self.fields if self._kconv(k) == key]
 87
 88    defset_all(self, key: KT, values: list[VT]) -> None:
 89"""
 90        Remove the old values for a key and add new ones.
 91        """
 92        key_kconv = self._kconv(key)
 93
 94        new_fields: list[tuple[KT, VT]] = []
 95        for field in self.fields:
 96            if self._kconv(field[0]) == key_kconv:
 97                if values:
 98                    new_fields.append((field[0], values.pop(0)))
 99            else:
100                new_fields.append(field)
101        while values:
102            new_fields.append((key, values.pop(0)))
103        self.fields = tuple(new_fields)
104
105    defadd(self, key: KT, value: VT) -> None:
106"""
107        Add an additional value for the given key at the bottom.
108        """
109        self.insert(len(self.fields), key, value)
110
111    definsert(self, index: int, key: KT, value: VT) -> None:
112"""
113        Insert an additional value for the given key at the specified position.
114        """
115        item = (key, value)
116        self.fields = self.fields[:index] + (item,) + self.fields[index:]
117
118    defkeys(self, multi: bool = False):
119"""
120        Get all keys.
121
122        If `multi` is True, one key per value will be returned.
123        If `multi` is False, duplicate keys will only be returned once.
124        """
125        return (k for k, _ in self.items(multi))
126
127    defvalues(self, multi: bool = False):
128"""
129        Get all values.
130
131        If `multi` is True, all values will be returned.
132        If `multi` is False, only the first value per key will be returned.
133        """
134        return (v for _, v in self.items(multi))
135
136    defitems(self, multi: bool = False):
137"""
138        Get all (key, value) tuples.
139
140        If `multi` is True, all `(key, value)` pairs will be returned.
141        If False, only one tuple per key is returned.
142        """
143        if multi:
144            return self.fields
145        else:
146            return super().items()
```

A MultiDict is a dictionary-like data structure that supports multiple values per key.

fields: tuple\[tuple\[~KT, ~VT], ...]

The underlying raw datastructure.

def get\_all(self, key: ~KT) -&gt; list\[~VT]: View Source

```
80    defget_all(self, key: KT) -> list[VT]:
81"""
82        Return the list of all values for a given key.
83        If that key is not in the MultiDict, the return value will be an empty list.
84        """
85        key = self._kconv(key)
86        return [value for k, value in self.fields if self._kconv(k) == key]
```

Return the list of all values for a given key. If that key is not in the MultiDict, the return value will be an empty list.

def set\_all(self, key: ~KT, values: list\[~VT]) -&gt; None: View Source

```
 88    defset_all(self, key: KT, values: list[VT]) -> None:
 89"""
 90        Remove the old values for a key and add new ones.
 91        """
 92        key_kconv = self._kconv(key)
 93
 94        new_fields: list[tuple[KT, VT]] = []
 95        for field in self.fields:
 96            if self._kconv(field[0]) == key_kconv:
 97                if values:
 98                    new_fields.append((field[0], values.pop(0)))
 99            else:
100                new_fields.append(field)
101        while values:
102            new_fields.append((key, values.pop(0)))
103        self.fields = tuple(new_fields)
```

Remove the old values for a key and add new ones.

def add(self, key: ~KT, value: ~VT) -&gt; None: View Source

```
105    defadd(self, key: KT, value: VT) -> None:
106"""
107        Add an additional value for the given key at the bottom.
108        """
109        self.insert(len(self.fields), key, value)
```

Add an additional value for the given key at the bottom.

def insert(self, index: int, key: ~KT, value: ~VT) -&gt; None: View Source

```
111    definsert(self, index: int, key: KT, value: VT) -> None:
112"""
113        Insert an additional value for the given key at the specified position.
114        """
115        item = (key, value)
116        self.fields = self.fields[:index] + (item,) + self.fields[index:]
```

Insert an additional value for the given key at the specified position.

def keys(self, multi: bool = False): View Source

```
118    defkeys(self, multi: bool = False):
119"""
120        Get all keys.
121
122        If `multi` is True, one key per value will be returned.
123        If `multi` is False, duplicate keys will only be returned once.
124        """
125        return (k for k, _ in self.items(multi))
```

Get all keys.

If `multi` is True, one key per value will be returned. If `multi` is False, duplicate keys will only be returned once.

def values(self, multi: bool = False): View Source

```
127    defvalues(self, multi: bool = False):
128"""
129        Get all values.
130
131        If `multi` is True, all values will be returned.
132        If `multi` is False, only the first value per key will be returned.
133        """
134        return (v for _, v in self.items(multi))
```

Get all values.

If `multi` is True, all values will be returned. If `multi` is False, only the first value per key will be returned.

def items(self, multi: bool = False): View Source

```
136    defitems(self, multi: bool = False):
137"""
138        Get all (key, value) tuples.
139
140        If `multi` is True, all `(key, value)` pairs will be returned.
141        If False, only one tuple per key is returned.
142        """
143        if multi:
144            return self.fields
145        else:
146            return super().items()
```

Get all (key, value) tuples.

If `multi` is True, all `(key, value)` pairs will be returned. If False, only one tuple per key is returned.

class MultiDict([mitmproxy.coretypes.multidict.\_MultiDict\[~KT, ~VT\]](#_MultiDict), mitmproxy.coretypes.serializable.Serializable): View Source

[](#MultiDict)

```
149classMultiDict(_MultiDict[KT, VT], serializable.Serializable):
150"""A concrete MultiDict, storing its own data."""
151
152    def__init__(self, fields=()):
153        super().__init__()
154        self.fields = tuple(tuple(i) for i in fields)  # type: ignore
155
156    @staticmethod
157    def_reduce_values(values):
158        return values[0]
159
160    @staticmethod
161    def_kconv(key):
162        return key
163
164    defget_state(self):
165        return self.fields
166
167    defset_state(self, state):
168        self.fields = tuple(tuple(x) for x in state)  # type: ignore
169
170    @classmethod
171    deffrom_state(cls, state):
172        return cls(state)
```

A concrete MultiDict, storing its own data.

MultiDict(fields=()) View Source

```
152    def__init__(self, fields=()):
153        super().__init__()
154        self.fields = tuple(tuple(i) for i in fields)  # type: ignore
```

fields

The underlying raw datastructure.

##### Inherited Members

[\_MultiDict](#_MultiDict)

[get\_all](#_MultiDict.get_all)

[set\_all](#_MultiDict.set_all)

[add](#_MultiDict.add)

[insert](#_MultiDict.insert)

[keys](#_MultiDict.keys)

[values](#_MultiDict.values)

[items](#_MultiDict.items)

class MultiDictView([mitmproxy.coretypes.multidict.\_MultiDict\[~KT, ~VT\]](#_MultiDict)): View Source

[](#MultiDictView)

```
175classMultiDictView(_MultiDict[KT, VT]):
176"""
177    The MultiDictView provides the MultiDict interface over calculated data.
178    The view itself contains no state - data is retrieved from the parent on
179    request, and stored back to the parent on change.
180    """
181
182    def__init__(self, getter, setter):
183        self._getter = getter
184        self._setter = setter
185        super().__init__()
186
187    @staticmethod
188    def_kconv(key):
189        # All request-attributes are case-sensitive.
190        return key
191
192    @staticmethod
193    def_reduce_values(values):
194        # We just return the first element if
195        # multiple elements exist with the same key.
196        return values[0]
197
198    @property  # type: ignore
199    deffields(self):
200        return self._getter()
201
202    @fields.setter
203    deffields(self, value):
204        self._setter(value)
205
206    defcopy(self) -> "MultiDict[KT,VT]":
207        return MultiDict(self.fields)
```

The MultiDictView provides the MultiDict interface over calculated data. The view itself contains no state - data is retrieved from the parent on request, and stored back to the parent on change.

MultiDictView(getter, setter) View Source

```
182    def__init__(self, getter, setter):
183        self._getter = getter
184        self._setter = setter
185        super().__init__()
```

fields View Source

```
198    @property  # type: ignore
199    deffields(self):
200        return self._getter()
```

The underlying raw datastructure.

def copy(self) -&gt; [MultiDict](#MultiDict)\[~KT, ~VT]: View Source

```
206    defcopy(self) -> "MultiDict[KT,VT]":
207        return MultiDict(self.fields)
```

##### Inherited Members

[\_MultiDict](#_MultiDict)

[get\_all](#_MultiDict.get_all)

[set\_all](#_MultiDict.set_all)

[add](#_MultiDict.add)

[insert](#_MultiDict.insert)

[keys](#_MultiDict.keys)

[values](#_MultiDict.values)

[items](#_MultiDict.items)