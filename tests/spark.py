from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("lakehouse-test").getOrCreate()

spark.range(10).show()
