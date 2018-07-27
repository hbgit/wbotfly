# import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, \
    cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report, \
    confusion_matrix, \
    accuracy_score

from sklearn.externals.six import StringIO
import pydot

# from sklearn import preprocessing
# from sklearn.pipeline import make_pipeline

balance_data = pd.read_csv('balance-scale.data',
                           sep=',',
                           header=None)

# print("Dataset Lenght:: ", len(balance_data))
# print("Dataset Shape:: ", balance_data.shape)

# print(balance_data.head())

# Feature set
X = balance_data.values[:, 1:5]
# X = balance_data.drop('Class', axis=1)
# print(X)
# Target set
Y = balance_data.values[:, 0]
# Y = dataset('Class')
# print(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.3,
                                                    random_state=100)
"""
clf_gini = DecisionTreeClassifier(criterion="gini",
                                  random_state=100,
                                  max_depth=3,
                                  min_samples_leaf=5)
"""
clf = DecisionTreeClassifier()
# clf = make_pipeline(preprocessing.StandardScaler(), DecisionTreeClassifier())

scores = cross_val_score(clf, X, Y, cv=5)
print("Accuracy with cross validation: %0.2f (+/- %0.2f)"
      % (scores.mean(), scores.std() * 2))

clf.fit(X_train, y_train)

# print(clf_gini.predict([[1, 1, 1, 1]]))
y_pred = clf.predict(X_test)


print("Accuracy is ", accuracy_score(y_test, y_pred) * 100)
print("Confusion matrix: ")
print(confusion_matrix(y_test, y_pred))
print("Classification Report: ")
print(classification_report(y_test, y_pred))

# Print tree
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("tree.pdf")
