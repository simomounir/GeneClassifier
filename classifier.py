import pandas as pd
import seaborn as sns


### Machine Learning

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from imblearn.over_sampling import SMOTE

class GeneClassifier(BaseEstimator, ClassifierMixin):
    """
        A class used to build a classifier using gene expression data

    ...

    Attributes
    ----------
    model : BaseEstimator
        model to use for fitting and predicting 
    reduction : BaseTransformer
        the method used for dimensionality reduction


    Methods
    -------
    fit(X, Y)
        fit the model to be used for predicting

    predict(X):
        Use fitted model to produce predictions

    transform(X):
        returns transformed data according to chosen reduction model

    plot_reduction_model(self):
        return a plot showing the transformed data

    plot_balancing(self):
        return a plot showing the balanced data
    """


    def __init__(self, reduction= None, model = None, **kwargs):

        
        if str(type(reduction)).find("sklearn.decomposition") > 0 or reduction == None :

            self.reduction = reduction
        else:
            raise ValueError('Dimensionality reduction method must be a valid sklearn.decomposition class', str(reduction))

        if isinstance(model,ClassifierMixin) or reduction == None:
            self.model = model
        else:
            raise ValueError('Model should be a valid sklearn Classifier')
        
        self.X_balanced = None
        self.y_balanced = None
        self.X_reduced = None


    def fit(self, X, y):
        """
            Fitting model according to chosen model 

        The model passed as an argument should be in the sklearn family of Classifiers

        Parameters
        ----------
        X : str, optional
            gene expression data
        y : labels of classes
        
        """
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.X_ = X
        self.y_ = y
        oversample = SMOTE()
        self.X_balanced, self.y_balanced = oversample.fit_resample(X,y)
        self.classes_ = unique_labels(y)
        self.X_reduced = self.reduction.fit_transform(self.X_balanced)
        self.model.fit(self.X_reduced, self.y_balanced)
        # Return the classifier
        
        return self

    def predict(self, X):
        """Use fitted model to generate predictions. 

        The model used should be checked whether it was fitted. This method returns the predicted labels

        Parameters
        ----------
        X : gene expression data

        """
        # Check if fit has been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)
    
        X_tansformed = self.reduction.transform(X)
        return self.model.predict(X_tansformed)

    def transform(self, X):
        """Transforms gene expression data according to valid reduction model and returns it. 

        Parameters
        ----------
        X : gene expression data
        
        """
        # Check if fit has been called
        check_is_fitted(self)
        return self.reduction.transform(X)

    def plot_reduction_model(self):
        """plot transformed data with dimensionality reduction.This method returns a seaborn plot

        Parameters
        ----------
        NONE. Plotting data from object X_reduced holding transformed data    
        """
        
        check_is_fitted(self)
        X_reduced = pd.DataFrame(data = self.transform(self.X_))
        Y = pd.DataFrame(self.y_,columns=['Class'])
        X_reduced = pd.concat([X_reduced.reset_index().drop(['index'],axis=1),Y.reset_index().drop(['index'],axis=1)], axis=1)

        return sns.pairplot(x_vars=0, y_vars=1, data=X_reduced, hue="Class",palette="YlGnBu",height=7,aspect=1.2).fig.suptitle( str(type(self.reduction)).rsplit("'")[1])

    def plot_balancing(self):
        """plot balanced data vs original data count .This method returns a seaborn plot

        Parameters
        ----------
        NONE. 
        """
        check_is_fitted(self)
        balanced = pd.DataFrame(self.X_balanced)
        original = pd.DataFrame(self.X_)
        balanced['type'] = 'balanced'
        balanced['class'] = self.y_balanced
        original['type'] = 'initial'
        original['class'] = self.y_
        compare_data = pd.concat([original, balanced], axis=0)
        
        return sns.countplot(data=compare_data, x="class", hue="type").set(title='SMOTE data balancing results')


