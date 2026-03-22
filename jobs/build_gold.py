from validations import (
    assert_columns_exist,
    assert_no_nulls,
    assert_non_negative,
    assert_not_empty,
)

from jobs.constants import (
    GOLD_COUNTRY_REVENUE,
    GOLD_MONTHLY_REVENUE,
    SILVER_ONLINE_RETAIL,
)
from jobs.spark_session import create_spark_session
from transformations.gold import build_country_revenue, build_monthly_revenue

expected_country_revenue_columns = [
    "Country",
    "TotalRevenue",
]

expected_monthly_revenue_columns = [
    "RevenueMonth",
    "TotalRevenue",
]


def main() -> None:
    spark = create_spark_session("gold")

    df_silver = spark.read.parquet(SILVER_ONLINE_RETAIL)

    df_country_revenue = build_country_revenue(df_silver)
    df_monthly_revenue = build_monthly_revenue(df_silver)

    assert_not_empty(df_country_revenue, "gold.country_revenue")
    assert_columns_exist(
        df_country_revenue, expected_country_revenue_columns, "gold.country_revenue"
    )
    assert_no_nulls(
        df_country_revenue, ["Country", "TotalRevenue"], "gold.country_revenue"
    )
    assert_non_negative(df_country_revenue, ["TotalRevenue"], "gold.country_revenue")

    df_country_revenue.write.mode("overwrite").parquet(GOLD_COUNTRY_REVENUE)

    assert_not_empty(df_monthly_revenue, "gold.monthly_revenue")
    assert_columns_exist(
        df_monthly_revenue, expected_monthly_revenue_columns, "gold.monthly_revenue"
    )
    assert_no_nulls(
        df_monthly_revenue, ["RevenueMonth", "TotalRevenue"], "gold.monthly_revenue"
    )
    assert_non_negative(df_monthly_revenue, ["TotalRevenue"], "gold.monthly_revenue")

    df_monthly_revenue.write.mode("overwrite").parquet(GOLD_MONTHLY_REVENUE)

    spark.stop()


if __name__ == "__main__":
    main()
