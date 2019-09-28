import numpy as np
import pandas as pd
import sys
import os
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
from keras.utils import np_utils


def one_hot_encode_object_array(arr):
    """One hot encode a numpy array of objects (e.g. strings)"""
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))


l = sys.argv[1]
l = l.split(",")

for x in range(0, len(l)):
    l[x] = int(float(l[x]))


data = pd.read_csv("./heart.csv")
x_data = data.drop("target", axis=1)
y_values = data["target"]


X_train, X_test, y_train, y_test = train_test_split(
    x_data, y_values, test_size=0.3, random_state=42
)

clf = LogisticRegression()
clf.fit(X_train, y_train)
lr_pred = clf.predict(X_test)


print(" ")
print(" ")
print("Constant: ", clf.intercept_)
print("Nilai Coefision Variabel Independent:", clf.coef_)
print(" ")
print(" ")
print(
    "=================================================================================================== "
)
print("Accuracy:{} ".format(clf.score(X_test, y_test) * 100))
print("Error Rate:{} ".format((1 - clf.score(X_test, y_test)) * 100))
# print("Recall:{} ".format(recall_score(lr_pred, y_test) * 100))
# print("Precision:{} ".format(precision_score(lr_pred, y_test) * 100))
print(" ")
print(" ")
sys.stdout = open("klasifikasi_result.txt", "w")
print(int(clf.predict([l])), end="")
sys.stdout.close()
