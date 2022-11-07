
from sklearn.model_selection import train_test_split, GridSearchCV
print("hello")
from geneclassifier.clf import GeneClassifier
import pandas as pd
from matplotlib import pyplot 
import pandas as pd
import io
import tarfile
import urllib.request

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import FactorAnalysis, PCA

if __name__ == "__main__":

    source = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00401/TCGA-PANCAN-HiSeq-801x20531.tar.gz'
    tar = tarfile.open(fileobj=urllib.request.urlopen(source), mode="r|gz")

    for member in tar:
        filename = member.name
        if 'data' in filename : 
            content = tar.extractfile(member).read()
            data = pd.read_csv(io.BytesIO(content), encoding='utf8')
        elif 'labels' in filename:
            content = tar.extractfile(member).read()
            labels = pd.read_csv(io.BytesIO(content), encoding='utf8')
    print('Data Aquired from https://archive.ics.uci.edu')
    X = data.drop(data.columns[0],axis=1)
    Y = labels.Class
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)

    parameters = {'model':(RandomForestClassifier(), SVC()), 'reduction':(PCA(n_components=3),PCA(n_components=5), FactorAnalysis(n_components=5))}
    gc = GeneClassifier()
    print('Starting Grid Search')
    clf = GridSearchCV(gc, parameters)
    clf.fit(X_train, y_train)

    print(f"Gridsearch model trained ")
    for x in clf.cv_results_['params']:
        print(f"\t {x}")

    print(f"Gridsearch mean_test_score  ")
    for x in clf.cv_results_['mean_test_score']:
        print(f"\t {x}")
        
    print(f"Gridsearch mean_score_time  ")
    for x in clf.cv_results_['mean_score_time']:
        print(f"\t {x}")

    print(f"Gridsearch mean_score_time  ")
    for x in clf.cv_results_['mean_fit_time']:
        print(f"\t {x}")

    print(f"Best Model {clf.best_params_} ")