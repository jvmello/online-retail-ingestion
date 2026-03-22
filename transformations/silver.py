from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_timestamp


def build_silver_online_retail(df_raw: DataFrame) -> DataFrame:
    return (
        df_raw.withColumn("InvoiceDate", to_timestamp(col("InvoiceDate")))
        .withColumn("Quantity", col("Quantity").cast("int"))
        .withColumn("UnitPrice", col("UnitPrice").cast("double"))
        .withColumn("CustomerID", col("CustomerID").cast("string"))
        .filter(col("Quantity").isNotNull())
        .filter(col("UnitPrice").isNotNull())
        .withColumn("Revenue", col("Quantity") * col("UnitPrice"))
    )
