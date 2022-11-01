<!-- Intro -->
## Prediction using Gene expression data:

Here we have made a classifier.py file that can take care of handling the data necessary to produce a report summarising the model performance. The GeneClassifier class can take the prediction model and reduction method as inputs. The class also takes care of generating the plots after reduction and also balances the labels in order to avoid a big discrepancy in the different label classes. the method used for balancinc is called SMOTE (Synthetic Minority Oversampling Technique).

A Grid Search is alro run to find the combination of parameters that gives the best prediction results

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
Python 3.8 o higher required to run the class. Also install requirements listed under **requirements.txt**


<!-- MARKDOWN LINKS -->

[sklearn-url]: https://scikit-learn.org/stable/
[seaborn-url]: https://seaborn.pydata.org/
[smote-url]: https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html