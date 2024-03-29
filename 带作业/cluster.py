import numpy as np
import scipy as sp
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import IPython
import platform

import pandas as pd

dataset = pd.read_csv('/home/kaede/下载/S1018bf.csv')
# print(dataset.head())
# print(dataset[:3])

dataset = dataset.dropna()
#提取特征和类别
X= dataset.loc[:,'Spectral.Index':'variability_index']
y= dataset.loc[:,'Optical.Class']

#划分训练集和测试集
from sklearn.model_selection import train_test_split 
from sklearn import preprocessing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3 ,random_state=0)

# 建立模型。 设置算法内核类型，有 'linear’, ‘poly’, ‘rbf’, ‘sigmoid’;惩罚参数为1，一般为10的幂次方

from sklearn import svm

svc_model = svm.SVC(kernel='rbf', C= 1,gamma='auto')
svc_model.fit(X_train, y_train)
predict_data = svc_model.predict(X_test)
accuracy = np.mean(predict_data==y_test)
print(accuracy)

from sklearn.neural_network import MLPClassifier
#建立MLP神经网络模型 ，MLP的求解方法为adam，可选lbfgs、sgd，正则化惩罚alpha = 0.1
mpl_model = MLPClassifier(solver='adam', learning_rate='constant', learning_rate_init=0.01,max_iter = 500,alpha =0.01)
mpl_model.fit(X_train, y_train)
predict_data = mpl_model.predict(X_test)
accuracy = np.mean(predict_data == y_test)
print(accuracy)


from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#建立逻辑回归模型 ，惩罚参数为100
lr_model = LogisticRegression(C= 100, max_iter=1000,solver='liblinear')
lr_model.fit(X_train, y_train)
predict_data = lr_model.predict(X_test)
accuracy = np.mean(predict_data == y_test)
print(accuracy)


from sklearn import tree
#划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# 建立决策树模型，选择算法为熵增益，可选gini,entropy,默认为gini
tree_model = tree.DecisionTreeClassifier(criterion='gini')
tree_model.fit(X_train, y_train)
predict_data = tree_model.predict(X_test)
accuracy = np.mean(predict_data==y_test)
print(accuracy)

from sklearn import neighbors
#划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# 建立KNN模型，邻居数选为7，默认为5
knn_model = neighbors.KNeighborsClassifier(n_neighbors = 7)
knn_model.fit(X_train, y_train)
#对测试集进行预测
predict_data = knn_model.predict(X_test)
accuracy = np.mean(predict_data==y_test)
print(accuracy)

