---
title: inputs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/inputs/
source: sitemap
fetched_at: 2026-05-07T21:34:08.957858394-03:00
rendered_js: false
word_count: 3
summary: This document defines the MultiModalFieldConfig class and its static methods, which provide various strategies for structuring and extracting multi-modal data inputs for model processing.
tags:
    - multi-modal
    - data-extraction
    - tensor-manipulation
    - batching
    - configuration
    - python
category: api
---

````
@dataclass(frozen=True)
classMultiModalFieldConfig:
    @staticmethod
    defbatched(modality: str, *, keep_on_cpu: bool = False):
"""
        Defines a field where an element in the batch is obtained by
        indexing into the first dimension of the underlying data.

        Args:
            modality: The modality of the multi-modal item that uses this
                keyword argument.
            keep_on_cpu: Whether to keep this field on the CPU for the model inputs.

        Example:

        ```
        Input:
            Data: [[AAAA]
                [BBBB]
                [CCCC]]

        Output:
            Element 1: [AAAA]
            Element 2: [BBBB]
            Element 3: [CCCC]
        ```
        """
        return MultiModalFieldConfig(
            field=MultiModalBatchedField(keep_on_cpu=keep_on_cpu),
            modality=modality,
        )

    @staticmethod
    defflat(
        modality: str,
        slices: Sequence[slice] | Sequence[Sequence[slice]],
        dim: int = 0,
        *,
        keep_on_cpu: bool = False,
    ):
"""
        Defines a field where an element in the batch is obtained by
        slicing along the first dimension of the underlying data.

        Args:
            modality: The modality of the multi-modal item that uses this
                keyword argument.
            slices: For each multi-modal item, a slice (dim=0) or a tuple of
                slices (dim>0) that is used to extract the data corresponding
                to it.
            dim: The dimension to extract data, default to 0.
            keep_on_cpu: Whether to keep this field on the CPU for the model inputs.

        Example:

        ```
        Given:
            slices: [slice(0, 3), slice(3, 7), slice(7, 9)]

        Input:
            Data: [AAABBBBCC]

        Output:
            Element 1: [AAA]
            Element 2: [BBBB]
            Element 3: [CC]
        ```

        ```
        Given:
            slices: [
                (slice(None), slice(0, 3)),
                (slice(None), slice(3, 7)),
                (slice(None), slice(7, 9))]
            dim: 1

        Input:
            Data: [[A],[A],[A],[B],[B],[B],[B],[C],[C]]

        Output:
            Element 1: [[A],[A],[A]]
            Element 2: [[B],[B],[B],[B]]
            Element 3: [[C],[C]]
        ```
        """
        return MultiModalFieldConfig(
            field=MultiModalFlatField(
                slices=slices,
                dim=dim,
                keep_on_cpu=keep_on_cpu,
            ),
            modality=modality,
        )

    @staticmethod
    defflat_from_sizes(
        modality: str,
        size_per_item: "torch.Tensor",
        dim: int = 0,
        *,
        keep_on_cpu: bool = False,
    ):
"""
        Defines a field where an element in the batch is obtained by
        slicing along the first dimension of the underlying data.

        Args:
            modality: The modality of the multi-modal item that uses this
                keyword argument.
            size_per_item: For each multi-modal item, the size of the slice
                that is used to extract the data corresponding to it.
            dim: The dimension to slice, default to 0.
            keep_on_cpu: Whether to keep this field on the CPU for the model inputs.

        Example:

        ```
        Given:
            size_per_item: [3, 4, 2]

        Input:
            Data: [AAABBBBCC]

        Output:
            Element 1: [AAA]
            Element 2: [BBBB]
            Element 3: [CC]
        ```

        ```
        Given:
            size_per_item: [3, 4, 2]
            dim: 1

        Input:
            Data: [[A],[A],[A],[B],[B],[B],[B],[C],[C]]

        Output:
            Element 1: [[A],[A],[A]]
            Element 2: [[B],[B],[B],[B]]
            Element 3: [[C],[C]]
        ```

        Info:
            [`MultiModalFieldConfig.flat`][vllm.multimodal.inputs.MultiModalFieldConfig.flat]
        """

        if size_per_item.ndim != 1:
            raise ValueError(
                "size_per_item should be a 1-D tensor, "
                f"but found shape: {size_per_item.shape}"
            )

        slice_idxs = [0, *accumulate(size_per_item)]
        slices = [
            (slice(None, None, None),) * dim
            + (slice(slice_idxs[i], slice_idxs[i + 1]),)
            for i in range(len(size_per_item))
        ]

        return MultiModalFieldConfig.flat(
            modality,
            slices,
            dim=dim,
            keep_on_cpu=keep_on_cpu,
        )

    @staticmethod
    defshared(
        modality: str,
        batch_size: int,
        *,
        keep_on_cpu: bool = False,
    ):
"""
        Defines a field where an element in the batch is obtained by
        taking the entirety of the underlying data.

        This means that the data is the same for each element in the batch.

        Args:
            modality: The modality of the multi-modal item that uses this
                keyword argument.
            batch_size: The number of multi-modal items which share this data.
            keep_on_cpu: Whether to keep this field on the CPU for the model inputs.

        Example:

        ```
        Given:
            batch_size: 4

        Input:
            Data: [XYZ]

        Output:
            Element 1: [XYZ]
            Element 2: [XYZ]
            Element 3: [XYZ]
            Element 4: [XYZ]
        ```
        """
        return MultiModalFieldConfig(
            field=MultiModalSharedField(
                batch_size=batch_size,
                keep_on_cpu=keep_on_cpu,
            ),
            modality=modality,
        )

    field: BaseMultiModalField
    modality: str

    defbuild_elems(
        self,
        key: str,
        batch: NestedTensors,
    ) -> Sequence[MultiModalFieldElem]:
        return self.field.build_elems(self.modality, key, batch)
````