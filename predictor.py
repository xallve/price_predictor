from pyspark.sql import SparkSession
from pyspark.mllib.tree import RandomForest, RandomForestModel
import pandas as pd
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors


class Predictor:
    def __init__(self, model_path):
        self.spark = SparkSession.builder.appName("CryptoPredictor").getOrCreate()
        self.model = RandomForestModel.load(model_path)

    def predict(self, data):
        df = self.spark.createDataFrame(pd.DataFrame(data))
        transformed_df = df.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[0:-1])))
        predictions = self.model.predict(transformed_df.map(lambda x: x.features))
        return [row.prediction for row in predictions.collect()]
