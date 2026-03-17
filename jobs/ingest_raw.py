from jobs.spark_session import create_spark_session

from jobs.constants import LOCAL_ONLINE_RETAIL_CSV

spark = create_spark_session("gold")

df = spark.read.csv(
    LOCAL_ONLINE_RETAIL_CSV,
    header=True,
    inferSchema=True
)

df.write \
  .mode("overwrite") \
  .parquet("s3a://lakehouse/raw/online_retail/")