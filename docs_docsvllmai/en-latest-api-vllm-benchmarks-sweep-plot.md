---
title: plot - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/sweep/plot/
source: sitemap
fetched_at: 2026-05-07T21:15:59.971777954-03:00
rendered_js: false
word_count: 69
summary: Defines utility classes and functions for processing and binning performance sweep data in pandas DataFrames, including support for string-based numeric conversion.
tags:
    - data-processing
    - pandas-dataframe
    - benchmark-sweep
    - json-serialization
    - data-binning
category: reference
---

## PlotBinner `dataclass` [¶](#vllm.benchmarks.sweep.plot.PlotBinner "Permanent link")

Source code in `vllm/benchmarks/sweep/plot.py`

```
@dataclass
classPlotBinner:
    var: str
    bin_size: float

    @classmethod
    defparse_str(cls, s: str):
        for op_key in PLOT_BINNERS:
            if op_key in s:
                key, value = s.split(op_key)
                return PLOT_BINNERS[op_key](key, float(value.removeprefix(op_key)))
        else:
            raise ValueError(
                f"Invalid operator for plot binner '{s}'. "
                f"Valid operators are: {sorted(PLOT_BINNERS)}",
            )

    defapply(self, df: "pd.DataFrame") -> "pd.DataFrame":
"""Applies this binner to a DataFrame."""
        df = df.copy()
        df[self.var] = df[self.var] // self.bin_size * self.bin_size
        return df
```

### apply [¶](#vllm.benchmarks.sweep.plot.PlotBinner.apply "Permanent link")

```
apply(df: DataFrame) -> DataFrame
```

Applies this binner to a DataFrame.

Source code in `vllm/benchmarks/sweep/plot.py`

```
defapply(self, df: "pd.DataFrame") -> "pd.DataFrame":
"""Applies this binner to a DataFrame."""
    df = df.copy()
    df[self.var] = df[self.var] // self.bin_size * self.bin_size
    return df
```

## PlotFilterBase `dataclass` [¶](#vllm.benchmarks.sweep.plot.PlotFilterBase "Permanent link")

Bases: `ABC`

Source code in `vllm/benchmarks/sweep/plot.py`

```
@dataclass
classPlotFilterBase(ABC):
    var: str
    target: str

    @classmethod
    defparse_str(cls, s: str):
        for op_key in PLOT_FILTERS:
            if op_key in s:
                key, value = s.split(op_key)
                return PLOT_FILTERS[op_key](
                    key,
                    value.removeprefix(op_key).strip("'").strip('"'),
                )
        else:
            raise ValueError(
                f"Invalid operator for plot filter '{s}'. "
                f"Valid operators are: {sorted(PLOT_FILTERS)}",
            )

    @abstractmethod
    defapply(self, df: "pd.DataFrame") -> "pd.DataFrame":
"""Applies this filter to a DataFrame."""
        raise NotImplementedError
```

### apply `abstractmethod` [¶](#vllm.benchmarks.sweep.plot.PlotFilterBase.apply "Permanent link")

```
apply(df: DataFrame) -> DataFrame
```

Applies this filter to a DataFrame.

Source code in `vllm/benchmarks/sweep/plot.py`

```
@abstractmethod
defapply(self, df: "pd.DataFrame") -> "pd.DataFrame":
"""Applies this filter to a DataFrame."""
    raise NotImplementedError
```

## \_convert\_inf\_nan\_strings [¶](#vllm.benchmarks.sweep.plot._convert_inf_nan_strings "Permanent link")

Convert string values "inf", "-inf", and "nan" to their float equivalents.

This handles the case where JSON serialization represents inf/nan as strings.

Source code in `vllm/benchmarks/sweep/plot.py`

```
def_convert_inf_nan_strings(data: list[dict[str, object]]) -> list[dict[str, object]]:
"""
    Convert string values "inf", "-inf", and "nan" to their float equivalents.

    This handles the case where JSON serialization represents inf/nan as strings.
    """
    converted_data = []
    for record in data:
        converted_record = {}
        for key, value in record.items():
            if isinstance(value, str):
                if value in ["inf", "-inf", "nan"]:
                    converted_record[key] = float(value)
                else:
                    converted_record[key] = value
            else:
                converted_record[key] = value
        converted_data.append(converted_record)
    return converted_data
```