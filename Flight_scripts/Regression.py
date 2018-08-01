import math
import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso, LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import *
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

# data = pd.read_csv("/home/drogon/Flight(regression).csv")
#
# df = data.head(1000)
#
# df = pd.get_dummies(data, columns=['UniqueCarrier','TailNum','Origin','Dest'], sparse=True)
#
# X = df.drop('TotalDelay', axis=1)
# y = df[['TotalDelay']]
#
# # trainx, testx, trainy, testy = train_test_split(X, Y, test_size=0.3)
# #
# # model = LinearRegression()
# # model.fit(trainx, trainy)
# # prediction = model.predict(testx)
# # loss1 = mean_squared_error(testy, prediction)
# # R_squared = r2_score(testy,prediction)
# # accuracy = model.score(testx,testy)
# #
# # print loss1
# # print("-----------------------")
# # print R_squared
# # print accuracy
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#
# clf = LinearRegression()
# clf.fit(x_train, y_train.values.ravel())
# prediction = clf.predict(x_test)
# accuracy = accuracy_score(y_test, prediction)
# print 'accuracy: ', accuracy

# model = Lasso()
# model.fit(trainx, trainy)
# prediction = model.predict(testx)
# loss2 = mean_squared_error(testy, prediction)
# print(loss2)
#
df = pd.read_csv("/home/drogon/Flight(classification).csv")
df = df.head(100)

df2 = pd.get_dummies(df, columns=['UniqueCarrier','TailNum','Origin','Dest'], sparse=True)
print df2.head()

# X = df2.drop('Class', axis=1)
# y = df2[['Class']]
# #
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#
# clf = LogisticRegression()
# clf.fit(x_train, y_train.values.ravel())
# prediction = clf.predict(x_test)
# accuracy = accuracy_score(y_test, prediction)
# print 'accuracy: ', accuracy