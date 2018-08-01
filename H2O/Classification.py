import os
os.environ["SPARK_HOME"] = "/home/drogon/spark-2.2.0-bin-hadoop2.7"

import h2o
from pyspark.sql import SparkSession
sc = SparkSession.builder.appName('classify').getOrCreate()

from pysparkling import *
hc = H2OContext.getOrCreate(sc)

print dir(h2o)

#column_type = ['Numeric','String','String','Enum','Enum','Enum','Enum','Enum','Enum','Enum','Numeric','Numeric','Numeric','Numeric','Enum','Numeric','Numeric','Numeric','Enum','Numeric','Numeric','Enum']
df = h2o.import_file(path ="/home/drogon/Flight(classification).csv")
print df
# numeric_cols = ['Month', 'DayofMonth', 'DepTime', 'ArrTime', 'FlightNum', 'ActualElapsedTime', 'Distance']
#
# print(df.shape)
# df.summary()


print df['Origin'].table()