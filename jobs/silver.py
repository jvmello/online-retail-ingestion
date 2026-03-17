from jobs.spark_session import create_spark_session
from jobs.constants import RAW_ONLINE_RETAIL, SILVER_ONLINE_RETAIL
from transformations.silver import build_silver_online_retail


def main() -> None:
    spark = create_spark_session("build-silver-online-retail")

    df_raw = spark.read.parquet(RAW_ONLINE_RETAIL)
    df_silver = build_silver_online_retail(df_raw)

    df_silver.write.mode("overwrite").parquet(SILVER_ONLINE_RETAIL)
    spark.stop()


if __name__ == "__main__":
    main()