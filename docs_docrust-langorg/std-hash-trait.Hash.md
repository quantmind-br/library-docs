---
title: Hash in std::hash - Rust
url: https://doc.rust-lang.org/std/hash/trait.Hash.html#method.hash_slice
source: crawler
fetched_at: 2026-05-06T21:23:37.779383588-03:00
rendered_js: false
word_count: 834
summary: The Hash trait defines a standard interface for types that can be fed into a Hasher to produce a hash value, with specific requirements regarding consistency with equality and prefix-freedom.
tags:
    - rust
    - hashing
    - traits
    - data-structures
    - programming-concepts
category: reference
---

## Trait Hash

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#185)

```rust
pub trait Hash {
    // Required method
    fn hash<H>(&self, state: &mut H)
       where H: Hasher;

    // Provided method
    fn hash_slice<H>(data: &[Self], state: &mut H)
       where H: Hasher,
             Self: Sized { ... }
}
```

Expand description

A hashable type.

Types implementing `Hash` are able to be [`hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html#tymethod.hash "method std::hash::Hash::hash")ed with an instance of [`Hasher`](https://doc.rust-lang.org/std/hash/trait.Hasher.html "trait std::hash::Hasher").

### [§](#implementing-hash)Implementing `Hash`

You can derive `Hash` with `#[derive(Hash)]` if all fields implement `Hash`. The resulting hash will be the combination of the values from calling [`hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html#tymethod.hash "method std::hash::Hash::hash") on each field.

```rust
#[derive(Hash)]
struct Rustacean {
    name: String,
    country: String,
}
```

If you need more control over how a value is hashed, you can of course implement the `Hash` trait yourself:

```rust
use std::hash::{Hash, Hasher};

struct Person {
    id: u32,
    name: String,
    phone: u64,
}

impl Hash for Person {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.id.hash(state);
        self.phone.hash(state);
    }
}
```

### [§](#hash-and-eq)`Hash` and `Eq`

When implementing both `Hash` and [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq"), it is important that the following property holds:

```text
k1 == k2 -> hash(k1) == hash(k2)
```

In other words, if two keys are equal, their hashes must also be equal. [`HashMap`](https://doc.rust-lang.org/std/collections/struct.HashMap.html) and [`HashSet`](https://doc.rust-lang.org/std/collections/struct.HashSet.html) both rely on this behavior.

Thankfully, you won’t need to worry about upholding this property when deriving both [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") and `Hash` with `#[derive(PartialEq, Eq, Hash)]`.

Violating this property is a logic error. The behavior resulting from a logic error is not specified, but users of the trait must ensure that such logic errors do *not* result in undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these methods.

### [§](#prefix-collisions)Prefix collisions

Implementations of `hash` should ensure that the data they pass to the `Hasher` are prefix-free. That is, values which are not equal should cause two different sequences of values to be written, and neither of the two sequences should be a prefix of the other.

For example, the standard implementation of [`Hash` for `&str`](https://doc.rust-lang.org/std/primitive.str.html#impl-Hash-for-str) passes an extra `0xFF` byte to the `Hasher` so that the values `("ab", "c")` and `("a", "bc")` hash differently.

### [§](#portability)Portability

Due to differences in endianness and type sizes, data fed by `Hash` to a `Hasher` should not be considered portable across platforms. Additionally the data passed by most standard library types should not be considered stable between compiler versions.

This means tests shouldn’t probe hard-coded hash values or data fed to a `Hasher` and instead should check consistency with `Eq`.

Serialization formats intended to be portable between platforms or compiler versions should either avoid encoding hashes or only rely on `Hash` and `Hasher` implementations that provide additional guarantees.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#198)

Feeds this value into the given [`Hasher`](https://doc.rust-lang.org/std/hash/trait.Hasher.html "trait std::hash::Hasher").

##### [§](#examples)Examples

```rust
use std::hash::{DefaultHasher, Hash, Hasher};

let mut hasher = DefaultHasher::new();
7920.hash(&mut hasher);
println!("Hash is {:x}!", hasher.finish());
```

1.3.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#234-236)

Feeds a slice of this type into the given [`Hasher`](https://doc.rust-lang.org/std/hash/trait.Hasher.html "trait std::hash::Hasher").

This method is meant as a convenience, but its implementation is also explicitly left unspecified. It isn’t guaranteed to be equivalent to repeated calls of [`hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html#tymethod.hash "method std::hash::Hash::hash") and implementations of [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html#tymethod.hash "method std::hash::Hash::hash") should keep that in mind and call [`hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html#tymethod.hash "method std::hash::Hash::hash") themselves if the slice isn’t treated as a whole unit in the [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") implementation.

For example, a [`VecDeque`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html) implementation might naïvely call [`as_slices`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.as_slices) and then [`hash_slice`](https://doc.rust-lang.org/std/hash/trait.Hash.html#method.hash_slice "associated function std::hash::Hash::hash_slice") on each slice, but this is wrong since the two slices can change with a call to [`make_contiguous`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.make_contiguous) without affecting the [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") result. Since these slices aren’t treated as singular units, and instead part of a larger deque, this method cannot be used.

##### [§](#examples-1)Examples

```rust
use std::hash::{DefaultHasher, Hash, Hasher};

let mut hasher = DefaultHasher::new();
let numbers = [6, 28, 496, 8128];
Hash::hash_slice(&numbers, &mut hasher);
println!("Hash is {:x}!", hasher.finish());
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#57)[§](#impl-Hash-for-Char)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#396)[§](#impl-Hash-for-Ordering)

1.44.0 · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#995)[§](#impl-Hash-for-Infallible)

[Source](https://doc.rust-lang.org/src/core/hint.rs.html#893)[§](#impl-Hash-for-Locality)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/error.rs.html#230)[§](#impl-Hash-for-ErrorKind)

1.7.0 · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#29)[§](#impl-Hash-for-IpAddr)

[Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#215)[§](#impl-Hash-for-Ipv6MulticastScope)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/net/socket_addr.rs.html#31)[§](#impl-Hash-for-SocketAddr)

1.55.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#81)[§](#impl-Hash-for-IntErrorKind)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#438)[§](#impl-Hash-for-Ordering-1)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#846)[§](#impl-Hash-for-bool)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#854)[§](#impl-Hash-for-char)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-i8)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-i16)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-i32)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-i64)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-i128)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-isize)

1.29.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#870)[§](#impl-Hash-for-!)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#862)[§](#impl-Hash-for-str)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-u8)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-u16)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-u32)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-u64)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-u128)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#916)[§](#impl-Hash-for-%28%29)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#830-843)[§](#impl-Hash-for-usize)

1.28.0 · [Source](https://doc.rust-lang.org/src/core/alloc/layout.rs.html#28)[§](#impl-Hash-for-Layout)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#869)[§](#impl-Hash-for-TypeId)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#36)[§](#impl-Hash-for-ByteStr)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#460)[§](#impl-Hash-for-ByteString)

1.64.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#91)[§](#impl-Hash-for-CStr)

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#impl-Hash-for-CString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1608-1613)[§](#impl-Hash-for-OsStr)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#804-809)[§](#impl-Hash-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#108)[§](#impl-Hash-for-Error)

1.1.0 · [Source](https://doc.rust-lang.org/src/std/fs.rs.html#299)[§](#impl-Hash-for-FileType)

1.33.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#1026)[§](#impl-Hash-for-PhantomPinned)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#78)[§](#impl-Hash-for-Ipv4Addr)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#171)[§](#impl-Hash-for-Ipv6Addr)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/net/socket_addr.rs.html#79)[§](#impl-Hash-for-SocketAddrV4)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/net/socket_addr.rs.html#145)[§](#impl-Hash-for-SocketAddrV6)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#41)[§](#impl-Hash-for-RangeFull)

[Source](https://doc.rust-lang.org/src/std/os/unix/net/ucred.rs.html#11)[§](#impl-Hash-for-UCred)

Available on **Unix** only.

1.10.0 · [Source](https://doc.rust-lang.org/src/core/panic/location.rs.html#79)[§](#impl-Hash-for-Location%3C'_%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3691-3744)[§](#impl-Hash-for-Path)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2256-2260)[§](#impl-Hash-for-PathBuf)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#486-490)[§](#impl-Hash-for-PrefixComponent%3C'_%3E)

[Source](https://doc.rust-lang.org/src/core/ptr/alignment.rs.html#310)[§](#impl-Hash-for-Alignment)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2725)[§](#impl-Hash-for-String)

1.19.0 · [Source](https://doc.rust-lang.org/src/std/thread/id.rs.html#30)[§](#impl-Hash-for-ThreadId)

1.3.0 · [Source](https://doc.rust-lang.org/src/core/time.rs.html#79)[§](#impl-Hash-for-Duration)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/time.rs.html#154)[§](#impl-Hash-for-Instant)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/time.rs.html#248)[§](#impl-Hash-for-SystemTime)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#514)[§](#impl-Hash-for-Component%3C'a%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#149)[§](#impl-Hash-for-Prefix%3C'a%3E)

[Source](https://doc.rust-lang.org/src/core/marker/variance.rs.html#130-180)[§](#impl-Hash-for-PhantomContravariantLifetime%3C'a%3E)

[Source](https://doc.rust-lang.org/src/core/marker/variance.rs.html#130-180)[§](#impl-Hash-for-PhantomCovariantLifetime%3C'a%3E)

[Source](https://doc.rust-lang.org/src/core/marker/variance.rs.html#130-180)[§](#impl-Hash-for-PhantomInvariantLifetime%3C'a%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#445-447)[§](#impl-Hash-for-Cow%3C'_,+B%3E)

1.55.0 · [Source](https://doc.rust-lang.org/src/core/ops/control_flow.rs.html#87)[§](#impl-Hash-for-ControlFlow%3CB,+C%3E)

[Source](https://doc.rust-lang.org/src/core/ptr/metadata.rs.html#262)[§](#impl-Hash-for-DynMetadata%3CDyn%3E)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mod.rs.html#2573)[§](#impl-Hash-for-F)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#79)[§](#impl-Hash-for-Range%3CIdx%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#194)[§](#impl-Hash-for-RangeFrom%3CIdx%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#354)[§](#impl-Hash-for-RangeInclusive%3CIdx%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#278)[§](#impl-Hash-for-RangeTo%3CIdx%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#607)[§](#impl-Hash-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#68)[§](#impl-Hash-for-Range%3CIdx%3E-1)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#452)[§](#impl-Hash-for-RangeFrom%3CIdx%3E-1)

1.95.0 · [Source](https://doc.rust-lang.org/src/core/range.rs.html#254)[§](#impl-Hash-for-RangeInclusive%3CIdx%3E-1)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#621)[§](#impl-Hash-for-RangeToInclusive%3CIdx%3E-1)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/map.rs.html#2583)[§](#impl-Hash-for-BTreeMap%3CK,+V,+A%3E)

1.41.0 · [Source](https://doc.rust-lang.org/src/core/pin.rs.html#1153)[§](#impl-Hash-for-Pin%3CPtr%3E)

1.17.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#690)[§](#impl-Hash-for-Bound%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/option.rs.html#594)[§](#impl-Hash-for-Option%3CT%3E)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-Hash-for-Poll%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#956)[§](#impl-Hash-for-*const+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#966)[§](#impl-Hash-for-*mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#940)[§](#impl-Hash-for-%26T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#948)[§](#impl-Hash-for-%26mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#931)[§](#impl-Hash-for-%5BT%5D)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#917)[§](#impl-Hash-for-%28T,%29)

This trait is implemented for tuples up to twelve items long.

1.19.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#679)[§](#impl-Hash-for-Reverse%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/marker/variance.rs.html#182-234)[§](#impl-Hash-for-PhantomContravariant%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/marker/variance.rs.html#182-234)[§](#impl-Hash-for-PhantomCovariant%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#817)[§](#impl-Hash-for-PhantomData%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/marker/variance.rs.html#182-234)[§](#impl-Hash-for-PhantomInvariant%3CT%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/core/mem/mod.rs.html#1096)[§](#impl-Hash-for-Discriminant%3CT%3E)

1.20.0 · [Source](https://doc.rust-lang.org/src/core/mem/manually_drop.rs.html#321)[§](#impl-Hash-for-ManuallyDrop%3CT%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#295-297)[§](#impl-Hash-for-NonZero%3CT%3E)

1.74.0 · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#35)[§](#impl-Hash-for-Saturating%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#40)[§](#impl-Hash-for-Wrapping%3CT%3E)

1.25.0 · [Source](https://doc.rust-lang.org/src/core/ptr/non_null.rs.html#1743)[§](#impl-Hash-for-NonNull%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/sync/exclusive.rs.html#291-293)[§](#impl-Hash-for-Exclusive%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#2131)[§](#impl-Hash-for-Box%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#86)[§](#impl-Hash-for-BTreeSet%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2188)[§](#impl-Hash-for-LinkedList%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3608)[§](#impl-Hash-for-VecDeque%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2786)[§](#impl-Hash-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#4150)[§](#impl-Hash-for-UniqueRc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3840)[§](#impl-Hash-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4578)[§](#impl-Hash-for-UniqueArc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#3791)[§](#impl-Hash-for-Vec%3CT,+A%3E)

The hash of a vector is the same as that of the corresponding slice, as required by the `core::borrow::Borrow` implementation.

```rust
use std::hash::BuildHasher;

let b = std::hash::RandomState::new();
let v: Vec<u8> = vec![0xa8, 0x3c, 0x09];
let s: &[u8] = &[0xa8, 0x3c, 0x09];
assert_eq!(b.hash_one(v), b.hash_one(s));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/result.rs.html#552)[§](#impl-Hash-for-Result%3CT,+E%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#347)[§](#impl-Hash-for-%5BT;+N%5D)

The hash of an array is the same as that of the corresponding slice, as required by the `Borrow` implementation.

```rust
use std::hash::BuildHasher;

let b = std::hash::RandomState::new();
let a: [u8; 3] = [0xa8, 0x3c, 0x09];
let s: &[u8] = &[0xa8, 0x3c, 0x09];
assert_eq!(b.hash_one(a), b.hash_one(s));
```

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#962-964)[§](#impl-Hash-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/ops/coroutine.rs.html#8)[§](#impl-Hash-for-CoroutineState%3CY,+R%3E)