from sklearn import metrics
from sklearn import tree
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np



df = pd.read_csv("/home/drogon/Flight2.csv", sep=',')
print '------' * 80
print list(df.columns.values)
#print list(df.head())


Month=map(float,df.c)
features = ['Month','DayofMonth','DepTime','ArrTime','UniqueCarrier','TailNum','FlightNum','ActualElapsedTime',
            'Origin','Dest','Distance']


#X = df[features]
X=df.iloc[:,:-1]
#y = df['Class']
y=df.iloc[:,11]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# clf = tree.DecisionTreeClassifier()
clf = MultinomialNB()

clf = clf.fit(X_train, y_train)

predicted = clf.predict(X_test)

metrics.accuracy_score(y_test, predicted)