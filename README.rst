.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/GeneClassifier.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/GeneClassifier
    .. image:: https://readthedocs.org/projects/GeneClassifier/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://GeneClassifier.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/GeneClassifier/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/GeneClassifier
    .. image:: https://img.shields.io/pypi/v/GeneClassifier.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/GeneClassifier/
    .. image:: https://img.shields.io/conda/vn/conda-forge/GeneClassifier.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/GeneClassifier
    .. image:: https://pepy.tech/badge/GeneClassifier/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/GeneClassifier
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/GeneClassifier

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

==============
GeneClassifier
==============
    Package that uses dimensionality reduction and classification model from sklearn, keeping compatibility with the rest of the sklearn framework

### Installation

pip install git+https:https://github.com/simomounir/GeneClassifier.git

### Built With

* [![sklearn][Scikit-learn]][sklearn-url]
* [![seabornn][Seaborn]][seaborn-url]
* [![smote][SMOTE]][smote-url]


<!-- GETTING STARTED -->
## Getting Started


As a start, two importants input parameters are passed when creating an instance of GeneClassifier:
* Model: a valid model from the **sklearn**family.
* Reduction: a dimensionality reduction method.

### Prerequisites
Python 3.8 o higher required to run the class. 


<!-- MARKDOWN LINKS -->

[sklearn-url]: https://scikit-learn.org/stable/
[seaborn-url]: https://seaborn.pydata.org/
[smote-url]: https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html

## Example Notebook: Prediction using Gene expression data:

 The GeneClassifier class can take the prediction model and reduction method as inputs. The class also takes care of generating the plots after reduction and also balances the labels in order to avoid a big discrepancy in the different label classes. the method used for balancing is called SMOTE (Synthetic Minority Oversampling Technique).

A Grid Search is alro run to find the combination of parameters that gives the best prediction results




.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
