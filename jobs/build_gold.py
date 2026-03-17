from jobs.spark_session import create_spark_session
from jobs.constants import (
    SILVER_ONLINE_RETAIL,
    GOLD_COUNTRY_REVENUE,
    GOLD_MONTHLY_REVENUE,
)
from transformations.gold import build_country_revenue, build_monthly_revenue


def main() -> None:
    spark = create_spark_session("gold")

    df_silver = spark.read.parquet(SILVER_ONLINE_RETAIL)

    df_country_revenue = build_country_revenue(df_silver)
    df_monthly_revenue = build_monthly_revenue(df_silver)

    df_country_revenue.write.mode("overwrite").parquet(GOLD_COUNTRY_REVENUE)
    df_monthly_revenue.write.mode("overwrite").parquet(GOLD_MONTHLY_REVENUE)

    spark.stop()


if __name__ == "__main__":
    main()