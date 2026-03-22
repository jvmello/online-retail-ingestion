# Transformation Rules

This document describes the transformations applied between Raw, Silver, and Gold layers.

## Raw Layer

Source: online_retail.csv

Rules:
- Data is ingested exactly as received;
- No filtering or transformation;
- Stored in Parquet format;
- Raw layer is immutable and reproducible.

Purpose:
- Preserve original data;
- Allow reprocessing if transformation logic changes.

---

## Silver Layer

The Silver layer cleans and standardizes the raw data.

Transformations applied:

1. Data Type Conversion
   - InvoiceDate → timestamp;
   - Quantity → integer;
   - UnitPrice → double;
   - CustomerID → string.

2. Null Handling
   - Rows with null Quantity removed;
   - Rows with null UnitPrice removed;
   - Rows with invalid InvoiceDate removed.

3. Derived Columns
   - Revenue = Quantity * UnitPrice.

4. Basic Filtering
   - Remove rows with invalid numeric values;
   - Optional: remove negative quantities depending on business rule.

Purposes:
- Standardized dataset;
- Clean data for analytics;
- Consistent schema.

---

## Gold Layer

Gold layer contains aggregated analytical tables.

### Country Revenue
Aggregation:
- Group by Country;
- Sum Revenue.

Columns:
- Country;
- TotalRevenue.

### Monthly Revenue
Aggregation:
- Group by month;
- Sum Revenue.

Columns:
- RevenueMonth;
- TotalRevenue.

Purposes:
- Business analytics;
- Reporting;
- Dashboard consumption;
- Data warehouse serving layer.

---

## Data Quality Rules

Applied during Silver and Gold processing:

- Dataset cannot be empty;
- Required columns must exist;
- Critical columns cannot contain null values;
- Revenue must be calculated;
- Aggregations must not produce null metrics.

These validations prevent bad data from propagating to analytical layers.