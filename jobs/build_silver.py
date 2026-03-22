from jobs.spark_session import create_spark_session
from jobs.constants import RAW_ONLINE_RETAIL, SILVER_ONLINE_RETAIL
from transformations.silver import build_silver_online_retail
from jobs.validations import (
    assert_not_empty,
    assert_columns_exist,
    assert_no_nulls,
    assert_non_negative,
    assert_row_count_above,
)


expected_silver_columns = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
    "Revenue",
]

def main() -> None:
    spark = create_spark_session("silver")

    df_raw = spark.read.parquet(RAW_ONLINE_RETAIL)
    df_silver = build_silver_online_retail(df_raw)

    assert_not_empty(df_silver, "silver.online_retail")
    assert_columns_exist(df_silver, expected_silver_columns, "silver.online_retail")
    assert_no_nulls(
        df_silver,
        ["InvoiceDate", "Quantity", "UnitPrice", "Revenue"],
        "silver.online_retail",
    )
    # assert_non_negative(
    #     df_silver,
    #     ["UnitPrice", "Revenue"],
    #     "silver.online_retail",
    # )
    # assert_row_count_above(df_silver, 1000, "silver.online_retail")

    df_silver.write.mode("overwrite").parquet(SILVER_ONLINE_RETAIL)
    spark.stop()


if __name__ == "__main__":
    main()
