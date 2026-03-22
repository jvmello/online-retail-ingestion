from pyspark.sql import DataFrame
from pyspark.sql.functions import col, sum as _sum, date_trunc


def build_country_revenue(df_silver: DataFrame) -> DataFrame:
    return (
        df_silver
        .groupBy("Country")
        .agg(_sum("Revenue").alias("TotalRevenue"))
        .orderBy(col("TotalRevenue").desc())
    )


def build_monthly_revenue(df_silver: DataFrame) -> DataFrame:
    return (
        df_silver
        .withColumn("RevenueMonth", date_trunc("month", col("InvoiceDate")))
        .groupBy("RevenueMonth")
        .agg(_sum("Revenue").alias("TotalRevenue"))
        .orderBy("RevenueMonth")
    )