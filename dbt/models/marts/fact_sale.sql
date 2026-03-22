SELECT
    InvoiceNo,
    CustomerID,
    StockCode,
    Quantity,
    UnitPrice,
    Quantity * UnitPrice AS total_amount
FROM {{ ref('transactions_clean') }}