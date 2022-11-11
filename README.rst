.. -*- mode: rst -*-

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

.. image:: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
    :alt: LinkedIn
    :target: https://www.linkedin.com/in/mohamed-mounir/

|
|

==============
GeneClassifier
==============

    Package that uses dimensionality reduction and classification model from sklearn, keeping compatibility with the rest of the sklearn framework
  
==============
Installation
==============
The package can be installed by directly cloning from repository::

    git clone https://github.com/simomounir/GeneClassifier.git

Or by running ``pip``::

    pip install git+https:https://github.com/simomounir/GeneClassifier.git


==============
Important links  / Markdown
==============

- [sklearn-url]: https://scikit-learn.org/stable/
- [seaborn-url]: https://seaborn.pydata.org/
- [smote-url]: https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html


GETTING STARTED
---------------

As a start, two importants input parameters are passed when creating an instance of GeneClassifier:
- Model: a valid model from the **sklearn** family.
- Reduction: a dimensionality reduction method.

Prerequisites
~~~~~~~~~~~~~

Python 3.8 o higher required to run the class. 


Example Notebook: Prediction using Gene expression data:
---------------------------------------------------------

The GeneClassifier class can take the prediction model and reduction method as inputs. The class also takes care of generating the plots after reduction and also balances the labels in order to avoid a big discrepancy in the different label classes. the method used for balancing is called SMOTE (Synthetic Minority Oversampling Technique).

A Grid Search is alro run to find the combination of parameters that gives the best prediction results.




.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.3.1. For details and usage information:

 PyScaffold see https://pyscaffold.org/.
