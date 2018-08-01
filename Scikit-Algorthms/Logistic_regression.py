
# # Logistic Regression
# from sklearn import datasets
# from sklearn import metrics
# from sklearn.linear_model import LogisticRegression
# # load the iris datasets
# dataset = datasets.load_iris()
# # fit a logistic regression model to the data
# model = LogisticRegression()
# model.fit(dataset.data, dataset.target)
# print(model)
# # make predictions
# expected = dataset.target
# predicted = model.predict(dataset.data)
# # summarize the fit of the model
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score

df = pd.read_csv("/home/drogon/Desktop/Data-Codex/Small DS/Regression/Communities/communities.csv", header=None)
print df

# load dataset
dta = sm.datasets.fair.load_pandas().data

# add "affair" column: 1 represents having affairs, 0 represents not
dta['affair'] = (dta.affairs > 0).astype(int)

print dta.groupby('affair').mean()
dta.groupby('rate_marriage').mean()


# create dataframes with an intercept column and dummy variables for
# occupation and occupation_husband
y, X = dmatrices('affair ~ rate_marriage + age + yrs_married + children + \
                  religious + educ + C(occupation) + C(occupation_husb)',
                  dta, return_type="dataframe")
#print X.columns

# flatten y into a 1-D array
y = np.ravel(y)

# instantiate a logistic regression model, and fit with X and y
model = LogisticRegression()
model = model.fit(X, y)

# check the accuracy on the training set
model.score(X, y)

# what percentage had affairs?
y.mean()

# examine the coefficients
pd.DataFrame(zip(X.columns, np.transpose(model.coef_)))

# evaluate the model by splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model2 = LogisticRegression()
model2.fit(X_train, y_train)

# predict class labels for the test set
predicted = model2.predict(X_test)
print predicted

# generate class probabilities
probs = model2.predict_proba(X_test)
print probs

# generate evaluation metrics
print metrics.accuracy_score(y_test, predicted)
print metrics.roc_auc_score(y_test, probs[:, 1])

print metrics.confusion_matrix(y_test, predicted)
print metrics.classification_report(y_test, predicted)

# evaluate the model using 10-fold cross-validation
scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=10)
print scores
print scores.mean()



print model.predict_proba(np.array([[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 22, 1, 0, 1, 16]]))

#23-year-old teacher who graduated college, has been married for 1 year,
#has 0 childs, rates herself as strongly religious, rates her marriage as fair, and her husband is a white collar.
# occupation: woman's occupation ' \
#'(1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar",
#  4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)
# occupation_husb: husband's occupation (same coding as above)

#print model

