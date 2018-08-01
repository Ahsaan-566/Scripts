import os

os.environ["SPARK_HOME"] = "/home/srm/spark_install/spark-2.2.0-bin-hadoop2.7"

from pyspark import SparkContext

sc = SparkContext(master='local[2]')

from pyspark.sql import SQLContext
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

sql = SQLContext(sc)


df = (sql.read
        .format("com.databricks.spark.csv")
       .option("header", "true").option("delimeter",",")
      .load("/home/srm/Chicago Data/Chicago1.csv"))


labelIndexer = StringIndexer(inputCol='PrimaryType', outputCol='label', handleInvalid = 'keep')
IUCRIndexer = StringIndexer(inputCol='IUCR', outputCol='Index_IUCR', handleInvalid = 'keep')
LocationIndexer = StringIndexer(inputCol='LocationDescription', outputCol='Index_LocationDescription', handleInvalid = 'keep')
ArrestIndexer = StringIndexer(inputCol='Arrest', outputCol='Index_Arrest', handleInvalid = 'keep')
DomesticIndexer = StringIndexer(inputCol='Domestic', outputCol='Index_Domestic', handleInvalid = 'keep')
BeatIndexer = StringIndexer(inputCol='Beat', outputCol='Index_Beat', handleInvalid = 'keep')
DistrictIndexer = StringIndexer(inputCol='District', outputCol='Index_District', handleInvalid = 'keep')
WardIndexer = StringIndexer(inputCol='Ward', outputCol='Index_Ward', handleInvalid = 'keep')
CommunityAreaIndexer = StringIndexer(inputCol='CommunityArea', outputCol='Index_CommunityArea', handleInvalid = 'keep')
FBICodeIndexer = StringIndexer(inputCol='FBICode', outputCol='Index_FBICode', handleInvalid = 'keep')


assembler = VectorAssembler(inputCols = ['Index_IUCR']+['Index_LocationDescription']
+['Index_Arrest']+['Index_Domestic']+['Index_Beat']+['Index_District']
+['Index_Ward']+['Index_CommunityArea']+['Index_FBICode'], outputCol= 'features')


classifier = NaiveBayes(labelCol='label',featuresCol= 'features')

pipeline = Pipeline(stages=[IUCRIndexer,ArrestIndexer,DomesticIndexer,BeatIndexer,DistrictIndexer
                            ,WardIndexer,CommunityAreaIndexer,FBICodeIndexer,LocationIndexer,labelIndexer,assembler,classifier])

(train,test) = df.randomSplit([0.7, 0.3])

model = pipeline.fit(train)


predictions = model.transform(test)
evaluator = MulticlassClassificationEvaluator()
roc = evaluator.evaluate(predictions,{evaluator.metricName: "accuracy"})
print(roc)

print df.describe



