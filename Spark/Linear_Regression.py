import os
os.environ["SPARK_HOME"] = "/home/drogon/spark-2.2.0-bin-hadoop2.7"

from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler



sc = SparkSession.builder.appName('ops').getOrCreate()

df = sc.read.csv('/home/drogon/Desktop/FYP/YearPredictionMSD.csv', inferSchema=True, header=False)

assembler = VectorAssembler(inputCols=['_c1', '_c2', '_c3', '_c4', '_c5', '_c6', '_c7', '_c8', '_c9', '_c10',
                                       '_c11', '_c12', '_c13', '_c14', '_c15', '_c16', '_c17', '_c18', '_c19',
                                       '_c20', '_c21', '_c22', '_c23', '_c24', '_c25', '_c26', '_c27', '_c28',
                                       '_c29', '_c30', '_c31', '_c32', '_c33', '_c34', '_c35', '_c36', '_c37',
                                       '_c38', '_c39', '_c40', '_c41', '_c42', '_c43', '_c44', '_c45', '_c46',
                                       '_c47', '_c48', '_c49', '_c50', '_c51', '_c52', '_c53', '_c54', '_c55',
                                       '_c56', '_c57', '_c58', '_c59', '_c60', '_c61', '_c62', '_c63', '_c64',
                                       '_c65', '_c66', '_c67', '_c68', '_c69', '_c70', '_c71', '_c72', '_c73',
                                       '_c74', '_c75', '_c76', '_c77', '_c78', '_c79', '_c80', '_c81', '_c82',
                                       '_c83', '_c84', '_c85', '_c86', '_c87', '_c88', '_c89', '_c90'],
                                       outputCol='features')
output = assembler.transform(df)

data = output.select('features','_c0')

(train, test) = data.randomSplit([0.7, 0.3])

lr = LinearRegression(labelCol='_c0')

lr_model = lr.fit(train)

test_results = lr_model.evaluate(test)

print 'RMS: ' , test_results.rootMeanSquaredError
print 'R squared: ' , test_results.r2
print 'Residuals: ' , test_results.residuals.show()
