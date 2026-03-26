from spark_session import create_spark_session

GOLD_COUNTRY_REVENUE = "s3a://lakehouse/gold/country_revenue/"
GOLD_MONTHLY_REVENUE = "s3a://lakehouse/gold/monthly_revenue/"

POSTGRES_URL = "jdbc:postgresql://postgres:5432/warehouse"
POSTGRES_PROPERTIES = {
    "user": "dbt",
    "password": "dbt",
    "driver": "org.postgresql.Driver",
}


def main() -> None:
    spark = create_spark_session("load-gold-to-postgres")

    df_country_revenue = spark.read.parquet(GOLD_COUNTRY_REVENUE)
    df_monthly_revenue = spark.read.parquet(GOLD_MONTHLY_REVENUE)

    df_country_revenue.write.jdbc(
        url=POSTGRES_URL,
        table="country_revenue",
        mode="overwrite",
        properties=POSTGRES_PROPERTIES,
    )

    df_monthly_revenue.write.jdbc(
        url=POSTGRES_URL,
        table="monthly_revenue",
        mode="overwrite",
        properties=POSTGRES_PROPERTIES,
    )

    spark.stop()


if __name__ == "__main__":
    main()
