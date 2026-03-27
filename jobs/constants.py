from jobs.ingest_raw import main as ingest_raw_main
from jobs.build_silver import main as build_silver_main
from jobs.build_gold import main as build_gold_main
from jobs.load_gold_to_postgres import main as load_gold_to_postgres_main

RAW_ONLINE_RETAIL = "s3a://lakehouse/raw/online_retail/"
SILVER_ONLINE_RETAIL = "s3a://lakehouse/silver/online_retail/"
GOLD_COUNTRY_REVENUE = "s3a://lakehouse/gold/country_revenue/"
GOLD_MONTHLY_REVENUE = "s3a://lakehouse/gold/monthly_revenue/"

LOCAL_ONLINE_RETAIL_CSV = "data/online_retail.csv"

STEPS = [
    ("Ingest Raw Layer", ingest_raw_main),
    ("Build Silver Layer", build_silver_main),
    ("Build Gold Layer", build_gold_main),
    ("Load Gold to PostgreSQL", load_gold_to_postgres_main),
]