from jobs.spark_session import create_spark_session
from jobs.constants import LOCAL_ONLINE_RETAIL_CSV, RAW_ONLINE_RETAIL


def main() -> None:
    spark = create_spark_session("raw")

    df = spark.read.csv(
        LOCAL_ONLINE_RETAIL_CSV,
        header=True,
        inferSchema=True,
    )

    df.write.mode("overwrite").parquet(RAW_ONLINE_RETAIL)
    spark.stop()


if __name__ == "__main__":
    main()