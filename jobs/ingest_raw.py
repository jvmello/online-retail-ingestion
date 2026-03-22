from jobs.constants import LOCAL_ONLINE_RETAIL_CSV, RAW_ONLINE_RETAIL
from jobs.spark_session import create_spark_session
from jobs.validations import assert_columns_exist, assert_not_empty

expected_raw_columns = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
]


def main() -> None:
    spark = create_spark_session("raw")

    df = spark.read.csv(
        LOCAL_ONLINE_RETAIL_CSV,
        header=True,
        inferSchema=True,
    )

    assert_not_empty(df, "raw.online_retail")
    assert_columns_exist(df, expected_raw_columns, "raw.online_retail")

    df.write.mode("overwrite").parquet(RAW_ONLINE_RETAIL)
    spark.stop()


if __name__ == "__main__":
    main()
