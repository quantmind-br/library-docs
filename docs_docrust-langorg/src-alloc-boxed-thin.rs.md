---
title: thin.rs - source
url: https://doc.rust-lang.org/src/alloc/boxed/thin.rs.html#142
source: crawler
fetched_at: 2026-05-06T21:36:16.287597864-03:00
rendered_js: false
word_count: 1932
summary: This document defines the ThinBox structure in Rust, which provides a heap-allocated pointer that maintains a single-word size by storing metadata inside the heap allocation rather than in the pointer itself.
tags:
    - rust
    - memory-management
    - pointers
    - heap-allocation
    - type-erasure
    - unsafe-rust
category: api
---

## alloc/boxed/ thin.rs

````rust
1//! Based on
2//! <https://github.com/matthieu-m/rfc2580/blob/b58d1d3cba0d4b5e859d3617ea2d0943aaa31329/examples/thin.rs>
3//! by matthieu-m
4
5use core::error::Error;
6use core::fmt::{self, Debug, Display, Formatter};
7#[cfg(not(no_global_oom_handling))]
8use core::intrinsics::{const_allocate, const_make_global};
9use core::marker::PhantomData;
10#[cfg(not(no_global_oom_handling))]
11use core::marker::Unsize;
12#[cfg(not(no_global_oom_handling))]
13use core::mem::{self, SizedTypeProperties};
14use core::ops::{Deref, DerefMut};
15use core::ptr::{self, NonNull, Pointee};
16
17use crate::alloc::{self, Layout, LayoutError};
18
19/// ThinBox.
20///
21/// A thin pointer for heap allocation, regardless of T.
22///
23/// # Examples
24///
25/// ```
26/// #![feature(thin_box)]
27/// use std::boxed::ThinBox;
28///
29/// let five = ThinBox::new(5);
30/// let thin_slice = ThinBox::<[i32]>::new_unsize([1, 2, 3, 4]);
31///
32/// let size_of_ptr = size_of::<*const ()>();
33/// assert_eq!(size_of_ptr, size_of_val(&five));
34/// assert_eq!(size_of_ptr, size_of_val(&thin_slice));
35/// ```
36#[unstable(feature = "thin_box", issue = "92791")]
37pub struct ThinBox<T: ?Sized> {
38    // This is essentially `WithHeader<<T as Pointee>::Metadata>`,
39    // but that would be invariant in `T`, and we want covariance.
40    ptr: WithOpaqueHeader,
41    _marker: PhantomData<T>,
42}
43
44/// `ThinBox<T>` is `Send` if `T` is `Send` because the data is owned.
45#[unstable(feature = "thin_box", issue = "92791")]
46unsafe impl<T: ?Sized + Send> Send for ThinBox<T> {}
47
48/// `ThinBox<T>` is `Sync` if `T` is `Sync` because the data is owned.
49#[unstable(feature = "thin_box", issue = "92791")]
50unsafe impl<T: ?Sized + Sync> Sync for ThinBox<T> {}
51
52#[unstable(feature = "thin_box", issue = "92791")]
53impl<T> ThinBox<T> {
54    /// Moves a type to the heap with its [`Metadata`] stored in the heap allocation instead of on
55    /// the stack.
56    ///
57    /// # Examples
58    ///
59    /// ```
60    /// #![feature(thin_box)]
61    /// use std::boxed::ThinBox;
62    ///
63    /// let five = ThinBox::new(5);
64    /// ```
65    ///
66    /// [`Metadata`]: core::ptr::Pointee::Metadata
67    #[cfg(not(no_global_oom_handling))]
68    pub fn new(value: T) -> Self {
69        let meta = ptr::metadata(&value);
70        let ptr = WithOpaqueHeader::new(meta, value);
71        ThinBox { ptr, _marker: PhantomData }
72    }
73
74    /// Moves a type to the heap with its [`Metadata`] stored in the heap allocation instead of on
75    /// the stack. Returns an error if allocation fails, instead of aborting.
76    ///
77    /// # Examples
78    ///
79    /// ```
80    /// #![feature(allocator_api)]
81    /// #![feature(thin_box)]
82    /// use std::boxed::ThinBox;
83    ///
84    /// let five = ThinBox::try_new(5)?;
85    /// # Ok::<(), std::alloc::AllocError>(())
86    /// ```
87    ///
88    /// [`Metadata`]: core::ptr::Pointee::Metadata
89    pub fn try_new(value: T) -> Result<Self, core::alloc::AllocError> {
90        let meta = ptr::metadata(&value);
91        WithOpaqueHeader::try_new(meta, value).map(|ptr| ThinBox { ptr, _marker: PhantomData })
92    }
93}
94
95#[unstable(feature = "thin_box", issue = "92791")]
96impl<Dyn: ?Sized> ThinBox<Dyn> {
97    /// Moves a type to the heap with its [`Metadata`] stored in the heap allocation instead of on
98    /// the stack.
99    ///
100    /// # Examples
101    ///
102    /// ```
103    /// #![feature(thin_box)]
104    /// use std::boxed::ThinBox;
105    ///
106    /// let thin_slice = ThinBox::<[i32]>::new_unsize([1, 2, 3, 4]);
107    /// ```
108    ///
109    /// [`Metadata`]: core::ptr::Pointee::Metadata
110    #[cfg(not(no_global_oom_handling))]
111    pub fn new_unsize<T>(value: T) -> Self
112    where
113        T: Unsize<Dyn>,
114    {
115        if size_of::<T>() == 0 {
116            let ptr = WithOpaqueHeader::new_unsize_zst::<Dyn, T>(value);
117            ThinBox { ptr, _marker: PhantomData }
118        } else {
119            let meta = ptr::metadata(&value as &Dyn);
120            let ptr = WithOpaqueHeader::new(meta, value);
121            ThinBox { ptr, _marker: PhantomData }
122        }
123    }
124}
125
126#[unstable(feature = "thin_box", issue = "92791")]
127impl<T: ?Sized + Debug> Debug for ThinBox<T> {
128    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
129        Debug::fmt(self.deref(), f)
130    }
131}
132
133#[unstable(feature = "thin_box", issue = "92791")]
134impl<T: ?Sized + Display> Display for ThinBox<T> {
135    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
136        Display::fmt(self.deref(), f)
137    }
138}
139
140#[unstable(feature = "thin_box", issue = "92791")]
141impl<T: ?Sized> Deref for ThinBox<T> {
142    type Target = T;
143
144    fn deref(&self) -> &T {
145        let value = self.data();
146        let metadata = self.meta();
147        let pointer = ptr::from_raw_parts(value as *const (), metadata);
148        unsafe { &*pointer }
149    }
150}
151
152#[unstable(feature = "thin_box", issue = "92791")]
153impl<T: ?Sized> DerefMut for ThinBox<T> {
154    fn deref_mut(&mut self) -> &mut T {
155        let value = self.data();
156        let metadata = self.meta();
157        let pointer = ptr::from_raw_parts_mut::<T>(value as *mut (), metadata);
158        unsafe { &mut *pointer }
159    }
160}
161
162#[unstable(feature = "thin_box", issue = "92791")]
163impl<T: ?Sized> Drop for ThinBox<T> {
164    fn drop(&mut self) {
165        unsafe {
166            let value = self.deref_mut();
167            let value = value as *mut T;
168            self.with_header().drop::<T>(value);
169        }
170    }
171}
172
173#[unstable(feature = "thin_box", issue = "92791")]
174impl<T: ?Sized> ThinBox<T> {
175    fn meta(&self) -> <T as Pointee>::Metadata {
176        //  Safety:
177        //  -   NonNull and valid.
178        unsafe { *self.with_header().header() }
179    }
180
181    fn data(&self) -> *mut u8 {
182        self.with_header().value()
183    }
184
185    fn with_header(&self) -> &WithHeader<<T as Pointee>::Metadata> {
186        // SAFETY: both types are transparent to `NonNull<u8>`
187        unsafe { &*((&raw const self.ptr) as *const WithHeader<_>) }
188    }
189}
190
191/// A pointer to type-erased data, guaranteed to either be:
192/// 1. `NonNull::dangling()`, in the case where both the pointee (`T`) and
193///    metadata (`H`) are ZSTs.
194/// 2. A pointer to a valid `T` that has a header `H` directly before the
195///    pointed-to location.
196#[repr(transparent)]
197struct WithHeader<H>(NonNull<u8>, PhantomData<H>);
198
199/// An opaque representation of `WithHeader<H>` to avoid the
200/// projection invariance of `<T as Pointee>::Metadata`.
201#[repr(transparent)]
202struct WithOpaqueHeader(NonNull<u8>);
203
204impl WithOpaqueHeader {
205    #[cfg(not(no_global_oom_handling))]
206    fn new<H, T>(header: H, value: T) -> Self {
207        let ptr = WithHeader::new(header, value);
208        Self(ptr.0)
209    }
210
211    #[cfg(not(no_global_oom_handling))]
212    fn new_unsize_zst<Dyn, T>(value: T) -> Self
213    where
214        Dyn: ?Sized,
215        T: Unsize<Dyn>,
216    {
217        let ptr = WithHeader::<<Dyn as Pointee>::Metadata>::new_unsize_zst::<Dyn, T>(value);
218        Self(ptr.0)
219    }
220
221    fn try_new<H, T>(header: H, value: T) -> Result<Self, core::alloc::AllocError> {
222        WithHeader::try_new(header, value).map(|ptr| Self(ptr.0))
223    }
224}
225
226impl<H> WithHeader<H> {
227    #[cfg(not(no_global_oom_handling))]
228    fn new<T>(header: H, value: T) -> WithHeader<H> {
229        let value_layout = Layout::new::<T>();
230        let Ok((layout, value_offset)) = Self::alloc_layout(value_layout) else {
231            // We pass an empty layout here because we do not know which layout caused the
232            // arithmetic overflow in `Layout::extend` and `handle_alloc_error` takes `Layout` as
233            // its argument rather than `Result<Layout, LayoutError>`, also this function has been
234            // stable since 1.28 ._.
235            //
236            // On the other hand, look at this gorgeous turbofish!
237            alloc::handle_alloc_error(Layout::new::<()>());
238        };
239
240        unsafe {
241            // Note: It's UB to pass a layout with a zero size to `alloc::alloc`, so
242            // we use `layout.dangling()` for this case, which should have a valid
243            // alignment for both `T` and `H`.
244            let ptr = if layout.size() == 0 {
245                // Some paranoia checking, mostly so that the ThinBox tests are
246                // more able to catch issues.
247                debug_assert!(value_offset == 0 && T::IS_ZST && H::IS_ZST);
248                layout.dangling_ptr()
249            } else {
250                let ptr = alloc::alloc(layout);
251                if ptr.is_null() {
252                    alloc::handle_alloc_error(layout);
253                }
254                // Safety:
255                // - The size is at least `aligned_header_size`.
256                let ptr = ptr.add(value_offset) as *mut _;
257
258                NonNull::new_unchecked(ptr)
259            };
260
261            let result = WithHeader(ptr, PhantomData);
262            ptr::write(result.header(), header);
263            ptr::write(result.value().cast(), value);
264
265            result
266        }
267    }
268
269    /// Non-panicking version of `new`.
270    /// Any error is returned as `Err(core::alloc::AllocError)`.
271    fn try_new<T>(header: H, value: T) -> Result<WithHeader<H>, core::alloc::AllocError> {
272        let value_layout = Layout::new::<T>();
273        let Ok((layout, value_offset)) = Self::alloc_layout(value_layout) else {
274            return Err(core::alloc::AllocError);
275        };
276
277        unsafe {
278            // Note: It's UB to pass a layout with a zero size to `alloc::alloc`, so
279            // we use `layout.dangling()` for this case, which should have a valid
280            // alignment for both `T` and `H`.
281            let ptr = if layout.size() == 0 {
282                // Some paranoia checking, mostly so that the ThinBox tests are
283                // more able to catch issues.
284                debug_assert!(value_offset == 0 && size_of::<T>() == 0 && size_of::<H>() == 0);
285                layout.dangling_ptr()
286            } else {
287                let ptr = alloc::alloc(layout);
288                if ptr.is_null() {
289                    return Err(core::alloc::AllocError);
290                }
291
292                // Safety:
293                // - The size is at least `aligned_header_size`.
294                let ptr = ptr.add(value_offset) as *mut _;
295
296                NonNull::new_unchecked(ptr)
297            };
298
299            let result = WithHeader(ptr, PhantomData);
300            ptr::write(result.header(), header);
301            ptr::write(result.value().cast(), value);
302
303            Ok(result)
304        }
305    }
306
307    // `Dyn` is `?Sized` type like `[u32]`, and `T` is ZST type like `[u32; 0]`.
308    #[cfg(not(no_global_oom_handling))]
309    fn new_unsize_zst<Dyn, T>(value: T) -> WithHeader<H>
310    where
311        Dyn: Pointee<Metadata = H> + ?Sized,
312        T: Unsize<Dyn>,
313    {
314        assert!(size_of::<T>() == 0);
315
316        const fn max(a: usize, b: usize) -> usize {
317            if a > b { a } else { b }
318        }
319
320        // Compute a pointer to the right metadata. This will point to the beginning
321        // of the header, past the padding, so the assigned type makes sense.
322        // It also ensures that the address at the end of the header is sufficiently
323        // aligned for T.
324        let alloc: &<Dyn as Pointee>::Metadata = const {
325            // FIXME: just call `WithHeader::alloc_layout` with size reset to 0.
326            // Currently that's blocked on `Layout::extend` not being `const fn`.
327
328            let alloc_align = max(align_of::<T>(), align_of::<<Dyn as Pointee>::Metadata>());
329
330            let alloc_size = max(align_of::<T>(), size_of::<<Dyn as Pointee>::Metadata>());
331
332            unsafe {
333                // SAFETY: align is power of two because it is the maximum of two alignments.
334                let alloc: *mut u8 = const_allocate(alloc_size, alloc_align);
335
336                let metadata_offset =
337                    alloc_size.checked_sub(size_of::<<Dyn as Pointee>::Metadata>()).unwrap();
338                // SAFETY: adding offset within the allocation.
339                let metadata_ptr: *mut <Dyn as Pointee>::Metadata =
340                    alloc.add(metadata_offset).cast();
341                // SAFETY: `*metadata_ptr` is within the allocation.
342                metadata_ptr.write(ptr::metadata::<Dyn>(ptr::dangling::<T>() as *const Dyn));
343                // SAFETY: valid heap allocation
344                const_make_global(alloc);
345                // SAFETY: we have just written the metadata.
346                &*metadata_ptr
347            }
348        };
349
350        // SAFETY: `alloc` points to `<Dyn as Pointee>::Metadata`, so addition stays in-bounds.
351        let value_ptr =
352            unsafe { (alloc as *const <Dyn as Pointee>::Metadata).add(1) }.cast::<T>().cast_mut();
353        debug_assert!(value_ptr.is_aligned());
354        mem::forget(value);
355        WithHeader(NonNull::new(value_ptr.cast()).unwrap(), PhantomData)
356    }
357
358    // Safety:
359    // - Assumes that either `value` can be dereferenced, or is the
360    //   `NonNull::dangling()` we use when both `T` and `H` are ZSTs.
361    unsafe fn drop<T: ?Sized>(&self, value: *mut T) {
362        struct DropGuard<H> {
363            ptr: NonNull<u8>,
364            value_layout: Layout,
365            _marker: PhantomData<H>,
366        }
367
368        impl<H> Drop for DropGuard<H> {
369            fn drop(&mut self) {
370                // All ZST are allocated statically.
371                if self.value_layout.size() == 0 {
372                    return;
373                }
374
375                unsafe {
376                    // SAFETY: Layout must have been computable if we're in drop
377                    let (layout, value_offset) =
378                        WithHeader::<H>::alloc_layout(self.value_layout).unwrap_unchecked();
379
380                    // Since we only allocate for non-ZSTs, the layout size cannot be zero.
381                    debug_assert!(layout.size() != 0);
382                    alloc::dealloc(self.ptr.as_ptr().sub(value_offset), layout);
383                }
384            }
385        }
386
387        unsafe {
388            // `_guard` will deallocate the memory when dropped, even if `drop_in_place` unwinds.
389            let _guard = DropGuard {
390                ptr: self.0,
391                value_layout: Layout::for_value_raw(value),
392                _marker: PhantomData::<H>,
393            };
394
395            // We only drop the value because the Pointee trait requires that the metadata is copy
396            // aka trivially droppable.
397            ptr::drop_in_place::<T>(value);
398        }
399    }
400
401    fn header(&self) -> *mut H {
402        //  Safety:
403        //  - At least `size_of::<H>()` bytes are allocated ahead of the pointer.
404        //  - We know that H will be aligned because the middle pointer is aligned to the greater
405        //    of the alignment of the header and the data and the header size includes the padding
406        //    needed to align the header. Subtracting the header size from the aligned data pointer
407        //    will always result in an aligned header pointer, it just may not point to the
408        //    beginning of the allocation.
409        let hp = unsafe { self.0.as_ptr().sub(Self::header_size()) as *mut H };
410        debug_assert!(hp.is_aligned());
411        hp
412    }
413
414    fn value(&self) -> *mut u8 {
415        self.0.as_ptr()
416    }
417
418    const fn header_size() -> usize {
419        size_of::<H>()
420    }
421
422    fn alloc_layout(value_layout: Layout) -> Result<(Layout, usize), LayoutError> {
423        Layout::new::<H>().extend(value_layout)
424    }
425}
426
427#[unstable(feature = "thin_box", issue = "92791")]
428impl<T: ?Sized + Error> Error for ThinBox<T> {
429    fn source(&self) -> Option<&(dyn Error + 'static)> {
430        self.deref().source()
431    }
432}
````