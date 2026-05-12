---
title: ssm_conv_transfer_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils/
source: sitemap
fetched_at: 2026-05-07T21:18:58.011409183-03:00
rendered_js: false
word_count: 398
summary: This document defines utilities for managing Mamba convolution state memory layouts and calculating byte offsets for RDMA transfers in a distributed tensor-parallel environment.
tags:
    - mamba
    - memory-layout
    - rdma
    - tensor-parallel
    - distributed-computing
    - kv-transfer
category: reference
---

Mamba conv-state sub-projection decomposition for the 3-read transfer.

With DS conv state layout (dim, state\_len), x/B/C sub-projections are contiguous in memory. Each D rank reads its x, B, C slices via 3 separate RDMA transfers — no P-side permutation needed.

## MambaConvSplitInfo `dataclass` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo "Permanent link")

Per-rank byte sizes of x, B, C sub-projections in the Mamba conv state.

Used by both P and D sides for NIXL descriptor registration. All fields are LOCAL to this engine's TP (already divided by TP size).

DS memory layout within one page (contiguous in memory): |--- x (x\_local * conv\_rows) ---|- B (b\_local * conv\_rows) -|- C -|

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils.py`

```
@dataclass(frozen=True)
classMambaConvSplitInfo:
"""Per-rank byte sizes of x, B, C sub-projections in the Mamba conv state.

    Used by both P and D sides for NIXL descriptor registration.
    All fields are LOCAL to this engine's TP (already divided by TP size).

    DS memory layout within one page (contiguous in memory):
        |--- x (x_local * conv_rows) ---|- B (b_local * conv_rows) -|- C -|
    """

    conv_rows: int  # conv_kernel - 1 (typically 3)
    x_local: int  # intermediate_size / TP  (columns for x)
    b_local: int  # groups_ss / TP  (columns for B; C is same size)
    conv_dtype_size: int  # bytes per element (e.g. 2 for float16)
    ssm_sizes: tuple[int, int]  # (conv_state_bytes, ssm_state_bytes)

    @property
    defconv_dim_local(self) -> int:
"""Total conv columns per rank: x + B + C."""
        return self.x_local + 2 * self.b_local

    @property
    defx_bytes(self) -> int:
"""Byte size of the x sub-projection for one rank."""
        return self.x_local * self.conv_rows * self.conv_dtype_size

    @property
    defb_bytes(self) -> int:
"""Byte size of the B (or C) sub-projection for one rank."""
        return self.b_local * self.conv_rows * self.conv_dtype_size

    @property
    deflocal_conv_offsets(self) -> list[tuple[int, int]]:
"""(byte_offset, byte_size) of x, B, C within this engine's page.

        Used by both P and D for local descriptor registration.
        """
        xb = self.x_bytes
        bb = self.b_bytes
        return [(0, xb), (xb, bb), (xb + bb, bb)]

    defremote_conv_offsets(
        self, local_rank_offset: int, tp_ratio: int
    ) -> list[tuple[int, int]]:
"""(byte_offset, byte_size) of this D rank's x, B, C slice within
        one P page.

        Used by D side only, during remote descriptor registration.

        Args:
            local_rank_offset: which slice this D rank reads.
                tp_ratio > 0: tp_rank % tp_ratio (selects slice of P's page).
                tp_ratio < 0: always 0 (read P's full page).
            tp_ratio: effective ratio (>= 1 when D_TP > P_TP, 1 when
                P_TP > D_TP since each P rank is read in full).
        """
        xb = self.x_bytes
        bb = self.b_bytes
        xr = xb * tp_ratio  # full remote x section in bytes
        br = bb * tp_ratio  # full remote B section in bytes
        return [
            (local_rank_offset * xb, xb),
            (xr + local_rank_offset * bb, bb),
            (xr + br + local_rank_offset * bb, bb),
        ]
```

### b\_bytes `property` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.b_bytes "Permanent link")

Byte size of the B (or C) sub-projection for one rank.

### conv\_dim\_local `property` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.conv_dim_local "Permanent link")

Total conv columns per rank: x + B + C.

### local\_conv\_offsets `property` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.local_conv_offsets "Permanent link")

(byte\_offset, byte\_size) of x, B, C within this engine's page.

Used by both P and D for local descriptor registration.

### x\_bytes `property` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.x_bytes "Permanent link")

Byte size of the x sub-projection for one rank.

### remote\_conv\_offsets [¶](#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.remote_conv_offsets "Permanent link")

(byte\_offset, byte\_size) of this D rank's x, B, C slice within one P page.

Used by D side only, during remote descriptor registration.

Parameters:

Name Type Description Default `local_rank_offset` `int`

which slice this D rank reads. tp\_ratio &gt; 0: tp\_rank % tp\_ratio (selects slice of P's page). tp\_ratio &lt; 0: always 0 (read P's full page).

*required* `tp_ratio` `int`

effective ratio (&gt;= 1 when D\_TP &gt; P\_TP, 1 when P\_TP &gt; D\_TP since each P rank is read in full).

*required*

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils.py`

```
defremote_conv_offsets(
    self, local_rank_offset: int, tp_ratio: int
) -> list[tuple[int, int]]:
"""(byte_offset, byte_size) of this D rank's x, B, C slice within
    one P page.

    Used by D side only, during remote descriptor registration.

    Args:
        local_rank_offset: which slice this D rank reads.
            tp_ratio > 0: tp_rank % tp_ratio (selects slice of P's page).
            tp_ratio < 0: always 0 (read P's full page).
        tp_ratio: effective ratio (>= 1 when D_TP > P_TP, 1 when
            P_TP > D_TP since each P rank is read in full).
    """
    xb = self.x_bytes
    bb = self.b_bytes
    xr = xb * tp_ratio  # full remote x section in bytes
    br = bb * tp_ratio  # full remote B section in bytes
    return [
        (local_rank_offset * xb, xb),
        (xr + local_rank_offset * bb, bb),
        (xr + br + local_rank_offset * bb, bb),
    ]
```

## compute\_physical\_blocks\_per\_logical [¶](#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.compute_physical_blocks_per_logical "Permanent link")

```
compute_physical_blocks_per_logical(
    ssm_sizes: tuple[int, ...], block_len: int
) -> int
```

Derive \_physical\_blocks\_per\_logical\_kv\_block from remote metadata.

The remote engine's ratio is not sent directly in the handshake, so we reconstruct it: total mamba state per logical block / block\_len.

Parameters:

Name Type Description Default `ssm_sizes` `tuple[int, ...]`

(conv\_state\_bytes, ssm\_state\_bytes) from NixlAgentMetadata.

*required* `block_len` `int`

the engine's block\_len in bytes (from block\_lens\[0]).

*required*

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils.py`

```
defcompute_physical_blocks_per_logical(
    ssm_sizes: tuple[int, ...], block_len: int
) -> int:
"""Derive _physical_blocks_per_logical_kv_block from remote metadata.

    The remote engine's ratio is not sent directly in the handshake, so we
    reconstruct it: total mamba state per logical block / block_len.

    Args:
        ssm_sizes: (conv_state_bytes, ssm_state_bytes) from NixlAgentMetadata.
        block_len: the engine's block_len in bytes (from block_lens[0]).
    """
    return math.ceil((ssm_sizes[0] + ssm_sizes[1]) / block_len)
```

## derive\_mamba\_conv\_split [¶](#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.derive_mamba_conv_split "Permanent link")

```
derive_mamba_conv_split(
    mamba_spec: MambaSpec, local_tp: int
) -> MambaConvSplitInfo
```

Derive per-rank x/B/C byte sizes from a MambaSpec.

Called once at init on both P and D. Decomposes the conv dimension (= intermediate\_size + 2 * groups\_ss) into its x, B, C parts.

Parameters:

Name Type Description Default `mamba_spec` `MambaSpec`

MambaSpec whose shapes are: shapes\[0] = conv state: (conv\_dim\_local, conv\_rows) in DS layout. shapes\[1] = SSM temporal: (local\_num\_heads, head\_dim).

*required* `local_tp` `int`

this engine's tensor-parallel size.

*required*

Returns:

Type Description `MambaConvSplitInfo`

MambaConvSplitInfo with per-rank x\_local, b\_local, conv\_rows,

`MambaConvSplitInfo`

conv\_dtype\_size, and ssm\_sizes (conv\_state\_bytes, ssm\_state\_bytes).

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils.py`

```
defderive_mamba_conv_split(
    mamba_spec: MambaSpec,
    local_tp: int,
) -> MambaConvSplitInfo:
"""Derive per-rank x/B/C byte sizes from a MambaSpec.

    Called once at init on both P and D.  Decomposes the conv dimension
    (= intermediate_size + 2 * groups_ss) into its x, B, C parts.

    Args:
        mamba_spec: MambaSpec whose shapes are:
            shapes[0] = conv state: (conv_dim_local, conv_rows) in DS layout.
            shapes[1] = SSM temporal: (local_num_heads, head_dim).
        local_tp: this engine's tensor-parallel size.

    Returns:
        MambaConvSplitInfo with per-rank x_local, b_local, conv_rows,
        conv_dtype_size, and ssm_sizes (conv_state_bytes, ssm_state_bytes).
    """
    if mamba_spec.mamba_type != "mamba2":
        raise NotImplementedError(
            f"3-read conv transfer only supports Mamba2 models, "
            f"got mamba_type={mamba_spec.mamba_type!r}.  "
            f"Mamba1 SSM temporal shape is (intermediate_size // tp, state_size) "
            f"which cannot be used to reconstruct intermediate_size."
        )

    conv_shape = mamba_spec.shapes[0]
    assert len(conv_shape) == 2, f"Expected 2D conv state shape, got {conv_shape}"

    # NOTE (ZhanqiuHu): 3-read requires DS layout, which is already asserted
    # in nixl worker __init__.  Use it directly instead of heuristic detection.
    assert is_conv_state_dim_first(), "3-read requires DS conv state layout"
    local_conv_dim = conv_shape[0]  # DS: (conv_dim_local, conv_rows)
    conv_rows = conv_shape[1]

    # NOTE (ZhanqiuHu): intermediate_size (= global x dim) is not stored
    # in MambaSpec, so we reconstruct it from the SSM temporal state shape:
    #   shapes[1] = (local_num_heads, head_dim), already divided by TP.
    head_dim = mamba_spec.shapes[1][1]
    local_num_heads = mamba_spec.shapes[1][0]
    intermediate_size = local_num_heads * local_tp * head_dim

    # NOTE (ZhanqiuHu): global conv dim = intermediate_size + 2 * groups_ss,
    # where groups_ss is the B (= C) dimension.  B and C are always the same
    # size, so we recover groups_ss from the remainder after subtracting x.
    remainder = local_conv_dim * local_tp - intermediate_size
    assert remainder > 0 and remainder % 2 == 0, (
        f"Conv dim ({local_conv_dim}*tp={local_tp}) doesn't decompose into "
        f"intermediate_size={intermediate_size} + 2*groups_ss. "
        f"remainder={remainder}"
    )
    groups_ss = remainder // 2

    conv_dtype_size = torch.tensor(
        [],
        dtype=mamba_spec.dtypes[0],  # type: ignore[misc]
    ).element_size()

    ssm_dtype_size = torch.tensor(
        [],
        dtype=mamba_spec.dtypes[1],  # type: ignore[misc]
    ).element_size()
    conv_state_bytes = torch.Size(mamba_spec.shapes[0]).numel() * conv_dtype_size
    ssm_state_bytes = torch.Size(mamba_spec.shapes[1]).numel() * ssm_dtype_size

    # Divide by TP to get per-rank column counts.
    return MambaConvSplitInfo(
        conv_rows=conv_rows,
        x_local=intermediate_size // local_tp,
        b_local=groups_ss // local_tp,
        conv_dtype_size=conv_dtype_size,
        ssm_sizes=(conv_state_bytes, ssm_state_bytes),
    )
```