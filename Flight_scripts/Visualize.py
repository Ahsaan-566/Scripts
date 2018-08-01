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

data = pd.read_csv('/home/drogon/Flight(regression).csv')
#data_without_ETL = pd.read_csv('/home/drogon/Desktop/FYP/Airline-data/2005.csv')


#Preprocessing

# le = preprocessing.LabelEncoder()
# d = defaultdict()
#
# fit = data.apply(lambda x: d[x.name].fit_transform(x))

# data_without_ETL["UniqueCarrier"] = data_without_ETL["UniqueCarrier"].astype('category')
# data_without_ETL["UniqueCarrier"] = data_without_ETL["UniqueCarrier"].cat.codes
# data_without_ETL["TailNum"] = data_without_ETL["TailNum"].astype('category')
# data_without_ETL["TailNum"] = data_without_ETL["TailNum"].cat.codes
# data_without_ETL["Origin"] = data_without_ETL["Origin"].astype('category')
# data_without_ETL["Origin"] = data_without_ETL["Origin"].cat.codes
# data_without_ETL["Dest"] = data_without_ETL["Dest"].astype('category')
# data_without_ETL["Dest"] = data_without_ETL["Dest"].cat.codes
# data_without_ETL["Class"] = data_without_ETL["Class"].astype('category')
# data_without_ETL["Class"] = data_without_ETL["Class"].cat.codes

data["UniqueCarrier"] = data["UniqueCarrier"].astype('category')
data["UniqueCarrier"] = data["UniqueCarrier"].cat.codes
data["TailNum"] = data["TailNum"].astype('category')
data["TailNum"] = data["TailNum"].cat.codes
data["Origin"] = data["Origin"].astype('category')
data["Origin"] = data["Origin"].cat.codes
data["Dest"] = data["Dest"].astype('category')
data["Dest"] = data["Dest"].cat.codes
# data["Class"] = data["Class"].astype('category')
# data["Class"] = data["Class"].cat.codes


print data.head()


# corr = data.corr()
#
# fig = plt.figure()
# sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, linewidths=0.1)
# plt.show()