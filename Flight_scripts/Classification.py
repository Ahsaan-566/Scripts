import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import (GaussianNB, BernoulliNB, MultinomialNB)
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('/home/drogon/Flight(classification).csv')

print data.columns.values


# data["UniqueCarrier"] = data["UniqueCarrier"].astype('category')
# data["UniqueCarrier"] = data["UniqueCarrier"].cat.codes
# data["TailNum"] = data["TailNum"].astype('category')
# data["TailNum"] = data["TailNum"].cat.codes
# data["Origin"] = data["Origin"].astype('category')
# data["Origin"] = data["Origin"].cat.codes
# data["Dest"] = data["Dest"].astype('category')
# data["Dest"] = data["Dest"].cat.codes
# data["Class"] = data["Class"].astype('category')
# data["Class"] = data["Class"].cat.codes
#
# # print data.head()
# # print data.columns.values
# # print len(data.index)
# # print data
#
# # #Feature selection
# # selector = VarianceThreshold(20)
# # selector.fit_transform(data)
# # print selector
# # print data.head()
#
# # corr = data.corr()
# # fig = plt.figure()
# # sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, linewidths=0.1)
# # plt.show()
#
# X = data.iloc[: , : 11]
# y = data.iloc[:,-1]
# #print X.head()
# #print y.head()
# #
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#
# # clf = DecisionTreeClassifier(criterion='entropy')
# # clf.fit(x_train, y_train)
# # prediction = clf.predict(x_test)
# # accuracy = accuracy_score(y_test, prediction)
# # print 'Decision tree: ', accuracy
#
# clf = RandomForestClassifier(n_estimators=20, criterion='entropy' , max_features='sqrt')
# clf.fit(x_train, y_train)
# prediction = clf.predict(x_test)
# accuracy = accuracy_score(y_test, prediction)
# print 'Random Forest: ', accuracy
#
# # clf = GaussianNB()
# # clf.fit(x_train, y_train)
# # prediction = clf.predict(x_test)
# # accuracy = accuracy_score(y_test, prediction)
# # print('Gaussian NB: ', accuracy)
# #
# # clf = BernoulliNB()
# # clf.fit(x_train, y_train)
# # prediction = clf.predict(x_test)
# # accuracy = accuracy_score(y_test, prediction)
# # print('Bernoulli NB: ', accuracy)
# #
# # clf = MultinomialNB()
# # clf.fit(x_train, y_train)
# # prediction = clf.predict(x_test)
# # accuracy = accuracy_score(y_test, prediction)
# # print('Multinomial NB: ', accuracy)

# X = data.iloc[: , : 11]
# y = data.iloc[:,-1]
#
# # print X.head()
# # print X.head()
#
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#
# clf = SVC()
#
# clf.fit(x_train, y_train)
# prediction = clf.predict(x_test)
# accuracy = accuracy_score(y_test, prediction)
# print 'accuracy: ', accuracy
# print 'actual:\n==========================\n',y_test,'\n==========================\npredicted',prediction
