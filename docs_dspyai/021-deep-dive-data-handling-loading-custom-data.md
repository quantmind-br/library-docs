---
title: Loading custom data - DSPy
url: https://dspy.ai/deep-dive/data-handling/loading-custom-data/
source: sitemap
fetched_at: 2026-01-23T08:03:12.697795869-03:00
rendered_js: false
word_count: 473
summary: This document explains how to create and load custom datasets in DSPy by converting raw data into Example objects using either standard Python logic or the built-in Dataset class.
tags:
    - dspy
    - data-loading
    - custom-datasets
    - python-pandas
    - dataset-class
    - machine-learning
category: guide
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/deep-dive/data-handling/loading-custom-data.md "Edit this page")

This page is outdated and may not be fully accurate in DSPy 2.5

## Creating a Custom Dataset[¶](#creating-a-custom-dataset "Permanent link")

We've seen how to work with with `Example` objects and use the `HotPotQA` class to load the HuggingFace HotPotQA dataset as a list of `Example` objects. But in production, such structured datasets are rare. Instead, you'll find yourself working on a custom dataset and might question: how do I create my own dataset or what format should it be?

In DSPy, your dataset is a list of `Examples`, which we can accomplish in two ways:

- **Recommended: The Pythonic Way:** Using native python utility and logic.
- **Advanced: Using DSPy's `Dataset` class**

## Recommended: The Pythonic Way[¶](#recommended-the-pythonic-way "Permanent link")

To create a list of `Example` objects, we can simply load data from the source and formulate it into a Python list. Let's load an example CSV `sample.csv` that contains 3 fields: (**context**, **question** and **summary**) via Pandas. From there, we can construct our data list.

```
importpandasaspd

df = pd.read_csv("sample.csv")
print(df.shape)
```

**Output:**

```
dataset = []

for context, question, answer in df.values:
    dataset.append(dspy.Example(context=context, question=question, answer=answer).with_inputs("context", "question"))

print(dataset[:3])
```

**Output:**

```
[Example({'context': nan, 'question': 'Which is a species of fish? Tope or Rope', 'answer': 'Tope'}) (input_keys={'question', 'context'}),
 Example({'context': nan, 'question': 'Why can camels survive for long without water?', 'answer': 'Camels use the fat in their humps to keep them filled with energy and hydration for long periods of time.'}) (input_keys={'question', 'context'}),
 Example({'context': nan, 'question': "Alice's parents have three daughters: Amy, Jessy, and what’s the name of the third daughter?", 'answer': 'The name of the third daughter is Alice'}) (input_keys={'question', 'context'})]
```

While this is fairly simple, let's take a look at how loading datasets would look in DSPy - via the DSPythonic way!

## Advanced: Using DSPy's `Dataset` class (Optional)[¶](#advanced-using-dspys-dataset-class-optional "Permanent link")

Let's take advantage of the `Dataset` class we defined in the previous article to accomplish the preprocessing:

- Load data from CSV to a dataframe.
- Split the data to train, dev and test splits.
- Populate `_train`, `_dev` and `_test` class attributes. Note that these attributes should be a list of dictionary, or an iterator over mapping like HuggingFace Dataset, to make it work.

This is all done through the `__init__` method, which is the only method we have to implement.

```
importpandasaspd
fromdspy.datasets.datasetimport Dataset

classCSVDataset(Dataset):
    def__init__(self, file_path, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        df = pd.read_csv(file_path)
        self._train = df.iloc[0:700].to_dict(orient='records')

        self._dev = df.iloc[700:].to_dict(orient='records')

dataset = CSVDataset("sample.csv")
print(dataset.train[:3])
```

**Output:**

```
[Example({'context': nan, 'question': 'Which is a species of fish? Tope or Rope', 'answer': 'Tope'}) (input_keys={'question', 'context'}),
 Example({'context': nan, 'question': 'Why can camels survive for long without water?', 'answer': 'Camels use the fat in their humps to keep them filled with energy and hydration for long periods of time.'}) (input_keys={'question', 'context'}),
 Example({'context': nan, 'question': "Alice's parents have three daughters: Amy, Jessy, and what’s the name of the third daughter?", 'answer': 'The name of the third daughter is Alice'}) (input_keys={'question', 'context'})]
```

Let's understand the code step by step:

- It inherits the base `Dataset` class from DSPy. This inherits all the useful data loading/processing functionality.
- We load the data in CSV into a DataFrame.
- We get the **train** split i.e first 700 rows in the DataFrame and convert it to lists of dicts using `to_dict(orient='records')` method and is then assigned to `self._train`.
- We get the **dev** split i.e first 300 rows in the DataFrame and convert it to lists of dicts using `to_dict(orient='records')` method and is then assigned to `self._dev`.

Using the Dataset base class now makes loading custom datasets incredibly easy and avoids having to write all that boilerplate code ourselves for every new dataset.

Caution

We did not populate `_test` attribute in the above code, which is fine and won't cause any unnecessary error as such. However it'll give you an error if you try to access the test split.

* * *

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-59-5202f6de3c7b> in <cell line: 1>()
----> 1 dataset.test[:5]

/usr/local/lib/python3.10/dist-packages/dspy/datasets/dataset.py in test(self)
    51     def test(self):
    52         if not hasattr(self, '_test_'):
---> 53             self._test_ = self._shuffle_and_sample('test', self._test, self.test_size, self.test_seed)
    54 
    55         return self._test_

AttributeError: 'CSVDataset' object has no attribute '_test'
```

To prevent that you'll just need to make sure `_test` is not `None` and populated with the appropriate data.

You can override the methods in `Dataset` class to customize your class even more.

In summary, the Dataset base class provides a simplistic way to load and preprocess custom datasets with minimal code!