from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def assert_not_empty(df: DataFrame, df_name: str) -> None:
    if df.rdd.isEmpty():
        raise ValueError(f"{df_name} is empty")


def assert_columns_exist(df: DataFrame, expected_columns: list[str], df_name: str) -> None:
    missing = [column for column in expected_columns if column not in df.columns]
    if missing:
        raise ValueError(f"{df_name} is missing columns: {missing}")


def assert_no_nulls(df: DataFrame, columns: list[str], df_name: str) -> None:
    for column_name in columns:
        null_count = df.filter(col(column_name).isNull()).count()
        if null_count > 0:
            raise ValueError(f"{df_name}.{column_name} has {null_count} null values")


def assert_non_negative(df: DataFrame, columns: list[str], df_name: str) -> None:
    for column_name in columns:
        invalid_count = df.filter(col(column_name) < 0).count()
        if invalid_count > 0:
            raise ValueError(f"{df_name}.{column_name} has {invalid_count} negative values")


def assert_row_count_above(df: DataFrame, minimum: int, df_name: str) -> None:
    row_count = df.count()
    if row_count < minimum:
        raise ValueError(f"{df_name} has only {row_count} rows, expected at least {minimum}")