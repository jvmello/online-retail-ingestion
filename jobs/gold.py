from jobs.spark_session import create_spark_session

from pyspark.sql.functions import col

from pyspark.sql.functions import sum as _sum

spark = create_spark_session("gold")

df_silver = spark.read.parquet("s3a://lakehouse/silver/online_retail/")

df_country_revenue = (
    df_silver
    .groupBy("Country")
    .agg(_sum("Revenue").alias("TotalRevenue"))
    .orderBy(col("TotalRevenue").desc())
)