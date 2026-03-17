from jobs.spark_session import create_spark_session

from pyspark.sql.functions import col, to_timestamp

spark = create_spark_session("silver")

df_raw = spark.read.parquet("s3a://lakehouse/raw/online_retail/")

df_silver = (
    df_raw
    .withColumn("InvoiceDate", to_timestamp(col("InvoiceDate")))
    .withColumn("Quantity", col("Quantity").cast("int"))
    .withColumn("UnitPrice", col("UnitPrice").cast("double"))
    .filter(col("Quantity").isNotNull())
    .filter(col("UnitPrice").isNotNull())
    .withColumn("Revenue", col("Quantity") * col("UnitPrice"))
)

df_silver.write.mode("overwrite").parquet("s3a://lakehouse/silver/online_retail/")