import zmq
import time
import random
import sys
import json
import time
import os

os.environ["SPARK_HOME"] = "/home/drogon/spark-2.2.0-bin-hadoop2.7"

from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame as DF
from pyspark.streaming import StreamingContext
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

sc = SparkSession.builder.appName('ops').getOrCreate()
df = sc.read.csv('/home/drogon/Desktop/FYP/iris.csv', inferSchema=True, header=True)

rdd = df.rdd

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:6666")

for row in rdd.take(rdd.count()):
        time.sleep(1)
        socket.send_string(str(row))
        msg = socket.recv()
        print("Message from Client ",msg)