# Lakehouse Retail Pipeline (Spark + MinIO + PostgreSQL + dbt)

## Overview

This project implements a local lakehouse architecture using PySpark, MinIO (S3-compatible storage), PostgreSQL, and dbt. The pipeline ingests a retail dataset, processes it through Raw, Silver, and Gold layers, and prepares analytical datasets for downstream consumption.

## Objective

This project was built as a learning and experimentation environment to practice modern data engineering concepts such as data lakehouse architecture, PySpark transformations, object storage (S3/MinIO), data quality checks, and analytical modeling with dbt.

## Architecture

Data Flow:

CSV → Spark → MinIO (Raw) → Spark Transformations → MinIO (Silver) → Aggregations (Gold) → PostgreSQL (Serving / Warehouse) → dbt Models

Main components:

- PySpark for data ingestion and transformations;
- MinIO as Data Lake (S3-compatible storage);
- PostgreSQL as serving layer / data warehouse (TODO);
- dbt for analytical modeling (TODO);
- Docker Compose for local infrastructure.

## Project Structure
```
lakehouse-project/
├── jobs/
│ ├── spark_session.py
│ ├── ingest_raw.py
│ ├── build_silver.py
│ ├── build_gold.py
│ ├── validations.py
│ └── constants.py
├── transformations/
│ ├── silver.py
│ └── gold.py
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_raw_ingestion.ipynb
│ ├── 03_silver_transformation.ipynb
│ └── 04_gold_aggregation.ipynb
├── data/
│ └── online_retail.xlsx (not included in the repository)
│ └── online_retail.csv (not included in the repository)
├── dbt/
├── docs/
│ └── transformation_rules.md
├── utils/
│ └── xlsx_to_csv.py
├── docker-compose.yml
└── README.md
```

## Data Layers

### Concepts
This project follows the Medallion Architecture pattern:

- **Raw Layer**: Stores data as ingested from the source;
- **Silver Layer**: Cleans and standardizes data;
- **Gold Layer**: Aggregated and business-ready datasets.

This approach improves data quality, reproducibility, and analytical performance.

### Original Dataset
The original dataset can be retrieved [here](https://archive.ics.uci.edu/dataset/352/online+retail). I've used a script to convert it from XLSX to CSV.

### Raw Layer
Stores the dataset exactly as ingested from the source CSV file.
No transformations are applied at this stage.

Location: s3a://lakehouse/raw/online_retail/


### Silver Layer
Data is cleaned and standardized:
- Data types are corrected;
- Invalid or null records are removed;
- Derived columns are created;
- Revenue column is calculated.

Location: s3a://lakehouse/silver/online_retail/

### Gold Layer
Aggregated tables for analytics:
- Revenue by country;
- Revenue by month;
- Product sales metrics.

Location: s3a://lakehouse/gold/


## Running the Pipeline

Run jobs in order:
```shell
python3 jobs/ingest_raw.py
python3 jobs/build_silver.py
python3 jobs/build_gold.py
```

These jobs will:
1. Ingest the dataset into the Raw layer;
2. Clean and standardize data into the Silver layer;
3. Generate aggregated datasets in the Gold layer.


## Data Quality Checks

Data quality validations are applied during Silver and Gold processing:
- Required columns must exist;
- Critical fields cannot be null;
- Numeric values must be valid;
- Dataset cannot be empty;
- Basic business rules validation.

## Technologies Used

- PySpark;
- MinIO (S3);
- PostgreSQL (TODO);
- dbt (TODO);
- Docker;
- Python;
- Parquet.

## Future Improvements

- Airflow orchestration;
- Delta Lake / Iceberg tables;
- CI/CD pipeline;
- Automated data quality framework;
- Partitioned tables;
- Incremental processing.