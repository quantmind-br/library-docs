---
title: Machine learning backends | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/plugintypes/mlbackend
source: sitemap
fetched_at: 2026-02-17T15:44:23.324532-03:00
rendered_js: false
word_count: 635
summary: This document explains the architecture and implementation of machine learning backend plugins within Moodle's analytics subsystem. It details the file structure and PHP interfaces required for model training, prediction, and evaluation using supervised learning algorithms.
tags:
    - moodle-development
    - machine-learning
    - analytics-api
    - mlbackend
    - php-interfaces
    - python-tensorflow
    - supervised-learning
category: guide
---

Machine learning backends process the datasets generated from the indicators and targets calculated by the [Analytics API](https://moodledev.io/docs/5.2/apis/subsystems/analytics). They are used for machine learning training, prediction and models evaluation.

tip

We strongly recommend that you read the [Analytics API](https://moodledev.io/docs/5.2/apis/subsystems/analytics) documentation to help understand the core concepts, how they are implemented in Moodle, and how machine learning backend plugins fit into the analytics API.

The communication between machine learning backends and Moodle is through files because the code that will process the dataset can be written in PHP, in Python, in other languages or even use cloud services. This needs to be scalable so they are expected to be able to manage big files and train algorithms reading input files in batches if necessary.

## Backends included in Moodle core[​](#backends-included-in-moodle-core "Direct link to Backends included in Moodle core")

### Python[​](#python "Direct link to Python")

The **Python backend** requires *python* binary (either python 2 or python 3) and [moodlemlbackend python package](https://pypi.python.org/pypi?name=moodlemlbackend&version=0.0.5&%3Aaction=display) which is maintained by Moodle HQ.

The Python version and libraries versions used are **very important**. We recommend using Python 3.7 for mlbackend 3.x versions.

The Python backend is based on [Google's tensorflow library](https://www.tensorflow.org/) and uses a feed-forward neural network with 1 single hidden layer.

The *moodlemlbackend* package does store model performance information that can be visualised using [tensorboard](https://www.tensorflow.org/get_started/summaries_and_tensorboard). Information generated during models evaluation is available through the models management page, under each model *Actions &gt; Log* menu.

tip

We recommend use of the **Python** backend as it is able to predict more accurately than the PHP backend and it is faster.

info

You can [view the source](https://github.com/moodlehq/moodle-mlbackend-python) of the *moodlemlbackend* library that Moodle uses.

## File structure[​](#file-structure "Direct link to File structure")

Machine learning backends are located in the `lib/mlbackend` directory.

Each plugin is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

View an example directory layout for the `mlbackend_python` plugin.

```
lib/mlbackend/python
├── classes
│   ├── privacy
│   │   └── provider.php
│   └── processor.php
├── lang
│   └── en
│       └── mlbackend_python.php
├── phpunit.xml
├── settings.php
├── tests
│   └── processor_test.php
├── upgrade.txt
└── version.php
```

Some of the important files for the mlbackend plugintype are described below. See the [common plugin files](https://moodledev.io/docs/5.2/apis/commonfiles) documentation for details of other files which may be useful in your plugin.

## Interfaces[​](#interfaces "Direct link to Interfaces")

A summary of these interfaces purpose:

- Evaluate a provided prediction model
- Train machine learning algorithms with the existing site data
- Predict targets based on previously trained algorithms

### Predictor[​](#predictor "Direct link to Predictor")

This is the basic interface to be implemented by machine learning backends. Two main types are, *classifiers* and *regressors*. We provide the *Regressor* interface but it is not currently implemented by core Machine learning backends. Both of these are supervised algorithms. Each type includes methods to train, predict and evaluate datasets.

You can use **is\_ready** to check that the backend is available.

```
/**
 * Is it ready to predict?
 *
 * @return bool
 */
publicfunctionis_ready();
```

**clear\_model** and **delete\_output\_dir** purpose is to clean up stuff created by the machine learning backend.

```
/**
 * Delete all stored information of the current model id.
 *
 * This method is called when there are important changes to a model,
 * all previous training algorithms using that version of the model
 * should be deleted.
 *
 * @param string $uniqueid The site model unique id string
 * @param string $modelversionoutputdir The output dir of this model version
 * @return null
 */
publicfunctionclear_model($uniqueid,$modelversionoutputdir);

/**
 * Delete the output directory.
 *
 * This method is called when a model is completely deleted.
 *
 * @param string $modeloutputdir The model directory id (parent of all model versions subdirectories).
 * @param string $uniqueid The site model unique id string
 * @return null
 */
publicfunctiondelete_output_dir($modeloutputdir,$uniqueid);
```

### Classifier[​](#classifier "Direct link to Classifier")

A [classifier](https://en.wikipedia.org/wiki/Statistical_classification) sorts input into two or more categories, based on analysis of the indicators. This is frequently used in binary predictions, e.g. course completion vs. dropout. This machine learning algorithm is "supervised": It requires a training data set of elements whose classification is known (e.g. courses in the past with a clear definition of whether the student has dropped out or not). This is an interface to be implemented by machine learning backends that support classification. It extends the *Predictor* interface.

Both these methods and *Predictor* methods should be implemented.

```
/**
 * Train this processor classification model using the provided supervised learning dataset.
 *
 * @param string $uniqueid
 * @param \stored_file $dataset
 * @param string $outputdir
 * @return \stdClass
 */
publicfunctiontrain_classification($uniqueid,\stored_file$dataset,$outputdir);

/**
 * Classifies the provided dataset samples.
 *
 * @param string $uniqueid
 * @param \stored_file $dataset
 * @param string $outputdir
 * @return \stdClass
 */
publicfunctionclassify($uniqueid,\stored_file$dataset,$outputdir);

/**
 * Evaluates this processor classification model using the provided supervised learning dataset.
 *
 * @param string $uniqueid
 * @param float $maxdeviation
 * @param int $niterations
 * @param \stored_file $dataset
 * @param string $outputdir
 * @param  string $trainedmodeldir
 * @return \stdClass
 */
publicfunctionevaluate_classification($uniqueid,$maxdeviation,$niterations,\stored_file$dataset,$outputdir);
```

### Regressor[​](#regressor "Direct link to Regressor")

A [regressor](https://en.wikipedia.org/wiki/Regression_analysis) predicts the value of an outcome (or dependent) variable based on analysis of the indicators. This value is linear, such as a final grade in a course or the likelihood a student is to pass a course. This machine learning algorithm is "supervised": It requires a training data set of elements whose classification is known (e.g. courses in the past with a clear definition of whether the student has dropped out or not). This is an interface to be implemented by machine learning backends that support regression. It extends *Predictor* interface.

Both these methods and *Predictor* methods should be implemented.

```
/**
 * Train this processor regression model using the provided supervised learning dataset.
 *
 * @param string $uniqueid
 * @param \stored_file $dataset
 * @param string $outputdir
 * @return \stdClass
 */
publicfunctiontrain_regression($uniqueid,\stored_file$dataset,$outputdir);

/**
 * Estimates linear values for the provided dataset samples.
 *
 * @param string $uniqueid
 * @param \stored_file $dataset
 * @param mixed $outputdir
 * @return void
 */
publicfunctionestimate($uniqueid,\stored_file$dataset,$outputdir);


/**
 * Evaluates this processor regression model using the provided supervised learning dataset.
 *
 * @param string $uniqueid
 * @param float $maxdeviation
 * @param int $niterations
 * @param \stored_file $dataset
 * @param string $outputdir
 * @param  string $trainedmodeldir
 * @return \stdClass
 */
publicfunctionevaluate_regression($uniqueid,$maxdeviation,$niterations,\stored_file$dataset,$outputdir);
```