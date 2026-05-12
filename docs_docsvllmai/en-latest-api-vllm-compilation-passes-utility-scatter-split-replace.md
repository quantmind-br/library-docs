---
title: scatter_split_replace - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/utility/scatter_split_replace/
source: sitemap
fetched_at: 2026-05-07T21:16:45.957193317-03:00
rendered_js: false
word_count: 122
summary: This document describes a compiler optimization pass that simplifies PyTorch graph operations by replacing redundant sequences of getitem, slice_scatter, and split nodes with direct access to the original tensor.
tags:
    - compiler-optimization
    - graph-compilation
    - pytorch-aten
    - tensor-manipulation
    - vllm-framework
    - code-refactoring
category: concept
---

Bases: `VllmInductorPass`

Replace getitem+slice\_scatter+split nodes with a single getitem when the inplace subtensor written to by the slice\_scatter has no other users.

Here's an example graph with q\_size = 512, kv\_size = 64: split\_with\_sizes\_1 = torch.ops.aten.split\_with\_sizes.default(qkv, (512, 64, 64), -1) at = auto\_functionalized(torch.ops.\_C.rotary\_embedding.default(positions, q, k)) q = operator.getitem(at, 1) k = operator.getitem(at, 2) torch.ops.aten.slice\_scatter.default(qkv, q, \[0, 512], -1) torch.ops.aten.slice\_scatter.default(qkv, k, \[512, 512 + 64], -1) split\_with\_sizes\_2 = torch.ops.aten.split\_with\_sizes.default(qkv, (512, 64, 64), -1) q = operator.getitem(split\_with\_sizes\_2, 0) k = operator.getitem(split\_with\_sizes\_2, 1) v = operator.getitem(split\_with\_sizes\_2, 2)

After this pass, this sequence of nodes is replaced with: split\_with\_sizes\_1 = torch.ops.aten.split\_with\_sizes.default(qkv, (512, 64, 64), -1) at = auto\_functionalized(torch.ops.\_C.rotary\_embedding.default(positions, q, k)) q = operator.getitem(at, 1) k = operator.getitem(at, 2) v = operator.getitem(split\_with\_sizes\_1, 2)

Source code in `vllm/compilation/passes/utility/scatter_split_replace.py`

```
classScatterSplitReplacementPass(VllmInductorPass):
"""Replace getitem+slice_scatter+split nodes with a single getitem when
    the inplace subtensor written to by the slice_scatter has no other users.

    Here's an example graph with q_size = 512, kv_size = 64:
    split_with_sizes_1 = torch.ops.aten.split_with_sizes.default(qkv, (512, 64, 64), -1)
    at = auto_functionalized(torch.ops._C.rotary_embedding.default(positions, q, k))
    q = operator.getitem(at, 1)
    k = operator.getitem(at, 2)
    torch.ops.aten.slice_scatter.default(qkv, q, [0, 512], -1)
    torch.ops.aten.slice_scatter.default(qkv, k, [512, 512 + 64], -1)
    split_with_sizes_2 = torch.ops.aten.split_with_sizes.default(qkv, (512, 64, 64), -1)
    q = operator.getitem(split_with_sizes_2, 0)
    k = operator.getitem(split_with_sizes_2, 1)
    v = operator.getitem(split_with_sizes_2, 2)

    After this pass, this sequence of nodes is replaced with:
    split_with_sizes_1 = torch.ops.aten.split_with_sizes.default(qkv, (512, 64, 64), -1)
    at = auto_functionalized(torch.ops._C.rotary_embedding.default(positions, q, k))
    q = operator.getitem(at, 1)
    k = operator.getitem(at, 2)
    v = operator.getitem(split_with_sizes_1, 2)
    """

    @VllmInductorPass.time_and_log
    def__call__(self, graph: fx.Graph) -> None:
        count = 0

        target_ops = [torch.ops._C.rotary_embedding.default]
        if hasattr(torch.ops.vllm, "rocm_aiter_triton_rotary_embedding"):
            target_ops.append(torch.ops.vllm.rocm_aiter_triton_rotary_embedding.default)

        for node in graph.nodes:
            if not is_func(node, auto_functionalized):
                continue

            kwargs = node.kwargs
            at_target = node.args[0]

            if at_target in target_ops:
                query = kwargs["query"]
                key = kwargs["key"]
                getitem_nodes = {}
                for user in node.users:
                    if is_func(user, operator.getitem):
                        getitem_nodes[user.args[1]] = user

                if (
                    is_func(query, operator.getitem)
                    and is_func(key, operator.getitem)
                    and query.args[0] == key.args[0]
                    and is_func(query.args[0], torch.ops.aten.split_with_sizes.default)
                    and all(
                        is_func(user, torch.ops.aten.slice_scatter.default)
                        for getitem_node in getitem_nodes.values()
                        for user in getitem_node.users
                    )
                ):
                    # Pattern where query and key are slices of a qkv tensor.
                    # While functionalized, results at [1] and [2] are scattered
                    # back into qkv, then split again to get query and key.
                    # If the inplace tensor has no other users, we can replace
                    # the slice_scatter+split nodes with the original results.
                    for user in getitem_nodes[1].users:
                        slice_scatter_1_node = user
                    if not is_func(
                        slice_scatter_1_node, torch.ops.aten.slice_scatter.default
                    ):
                        continue

                    for user in getitem_nodes[2].users:
                        slice_scatter_2_node = user
                    if not is_func(
                        slice_scatter_2_node, torch.ops.aten.slice_scatter.default
                    ):
                        continue

                    for user in slice_scatter_2_node.users:
                        split_node = user
                    if not is_func(split_node, torch.ops.aten.split_with_sizes.default):
                        continue

                    split_getitem_users = {}
                    for user in split_node.users:
                        if is_func(user, operator.getitem):
                            split_getitem_users[user.args[1]] = user

                    # Replace query node
                    split_getitem_users[0].replace_all_uses_with(getitem_nodes[1])
                    graph.erase_node(split_getitem_users[0])
                    # Replace key node
                    split_getitem_users[1].replace_all_uses_with(getitem_nodes[2])
                    graph.erase_node(split_getitem_users[1])
                    # Redirect value node to original qkv tensor
                    split_getitem_users[2].replace_input_with(split_node, query.args[0])

                    # Erase unused nodes
                    graph.erase_node(split_node)
                    graph.erase_node(slice_scatter_2_node)
                    graph.erase_node(slice_scatter_1_node)

                    count += 1

        logger.debug("Eliminated %d slice_scatter+split nodes", count)
```