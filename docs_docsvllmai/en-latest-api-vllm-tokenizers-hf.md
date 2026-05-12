---
title: hf - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tokenizers/hf/
source: sitemap
fetched_at: 2026-05-07T21:35:42.883101609-03:00
rendered_js: false
word_count: 9
summary: This code implements a mechanism to enable thread-safe operations for Hugging Face tokenizers by creating a pool of deep-copied tokenizer instances.
tags:
    - huggingface
    - concurrency
    - multithreading
    - python-optimization
    - tokenization
    - thread-safety
category: concept
---

```
defmaybe_make_thread_pool(tokenizer: _T, copies: int = 1):
"""
    If `tokenizer` is a `PreTrainedTokenizerFast`, modify the tokenizer
    in-place to make the public interface thread-safe by routing calls
    through a deep-copied tokenizer pool.

    Note that:
    - Only ``TokenizerLike``'s public interface is thread-safe.
      This doesn't include ``_tokenizer`` property nor any mutation
      methods like ``add_special_tokens`` or ``add_tokens``.
    - Adjacent method calls could happen on different deep copies.
    """
    if not isinstance(tokenizer, PreTrainedTokenizerFast) or isinstance(
        tokenizer, ThreadSafeHFTokenizerMixin
    ):
        return tokenizer

    og_tokenizer = copy.copy(tokenizer)

    tokenizer_pool: queue.Queue[PreTrainedTokenizerFast] = queue.Queue()
    for _ in range(copies):
        tokenizer_pool.put(copy.deepcopy(og_tokenizer))

    @contextlib.contextmanager
    def_borrow_from_pool():
        try:
            tok = tokenizer_pool.get_nowait()
            yield tok
        except queue.Empty:
            tok = copy.deepcopy(og_tokenizer)
            yield tok
        finally:
            tokenizer_pool.put(tok)

    classTokenizerPool(tokenizer.__class__, ThreadSafeHFTokenizerMixin):  # type: ignore
        defapply_chat_template(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.apply_chat_template(*args, **kwargs)

        defbatch_decode(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.batch_decode(*args, **kwargs)

        defbatch_encode(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.batch_encode(*args, **kwargs)

        defconvert_tokens_to_ids(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.convert_tokens_to_ids(*args, **kwargs)

        defconvert_ids_to_tokens(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.convert_ids_to_tokens(*args, **kwargs)

        defconvert_tokens_to_string(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.convert_tokens_to_string(*args, **kwargs)

        defdecode(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.decode(*args, **kwargs)

        defencode(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok.encode(*args, **kwargs)

        def__call__(self, *args, **kwargs):
            with _borrow_from_pool() as tok:
                return tok(*args, **kwargs)

        def__reduce__(self):
            return maybe_make_thread_pool, (og_tokenizer, copies)

    TokenizerPool.__name__ = f"TokenizerPool{og_tokenizer.__class__.__name__}"

    tokenizer.__class__ = TokenizerPool
```