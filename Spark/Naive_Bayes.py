import os

os.environ["SPARK_HOME"] = "/home/drogon/spark-2.2.0-bin-hadoop2.7"

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.classification import NaiveBayes,NaiveBayesModel
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.sql.functions import *

sc = SparkSession.builder.appName('ops').getOrCreate()

df = sc.read.csv('/home/drogon/Flight2.csv',inferSchema= True,header=True)
print df.dtypes

#print df.describe
#cSchema = df.schema.names
#list_df = df.take(5000000)
# df2 = sc.createDataFrame(list_df,schema=cSchema)

numeric_cols = ['Month','DayofMonth','DepTime','ArrTime','FlightNum','ActualElapsedTime','Distance']

labelIndexer = StringIndexer(inputCol='Class', outputCol='label', handleInvalid = 'keep')
UniqueCarrierIndexer = StringIndexer(inputCol='UniqueCarrier', outputCol='Index_UniqueCarrier', handleInvalid = 'keep')
TailNumIndexer = StringIndexer(inputCol='TailNum', outputCol='Index_TailNum', handleInvalid = 'keep')
OriginIndexer = StringIndexer(inputCol='Origin', outputCol='Index_Origin', handleInvalid = 'keep')
DestIndexer = StringIndexer(inputCol='Dest', outputCol='Index_Dest', handleInvalid = 'keep')



assembler = VectorAssembler(inputCols = ['O/N_Indexed'] + ['Duration_Indexer'] +
                                        ['Town_Indexer'] + ['District_Indexer'] +
                                        ['County_Indexer'] + ['PPDCType_Indexer'] +
                                        ['RS_Indexer'] + numeric_cols, outputCol='features')

assembler = VectorAssembler(inputCols = ['Index_UniqueCarrier']+['Index_TailNum']
+['Index_Origin']+['Index_Dest'] + numeric_cols , outputCol= 'features')
#classifier = DecisionTreeClassifier(labelCol='label', featuresCol='features', maxBins=10000)
classifier = NaiveBayes(labelCol='label',featuresCol = 'features')
pipeline = Pipeline(stages=[UniqueCarrierIndexer, TailNumIndexer, OriginIndexer, DestIndexer, labelIndexer, assembler, classifier])
(train, test) = df.randomSplit([0.7, 0.3])

paramGrid = ParamGridBuilder().addGrid(classifier, (10, 10, 10)).build()

cvEvaluator = MulticlassClassificationEvaluator(metricName="accuracy")
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=paramGrid, evaluator=cvEvaluator, numFolds=10)
model = cv.fit(train)

#model = pipeline.fit(train)
predictions = model.transform(test)
evaluator = MulticlassClassificationEvaluator()
acc = evaluator.evaluate(predictions, {evaluator.metricName: "accuracy"})
print(acc)

