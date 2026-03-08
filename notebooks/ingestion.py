from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RetailPipeline") \
    .config("spark.jars.packages",
            "io.delta:delta-core_2.12:2.4.0") \
    .getOrCreate()

df = spark.read.csv("/data/online_retail.csv", header=True)

df.write.format("delta").save("/data/datalake/raw")

clean_df = df.filter("Quantity > 0")

clean_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/data/datalake/silver/transactions")