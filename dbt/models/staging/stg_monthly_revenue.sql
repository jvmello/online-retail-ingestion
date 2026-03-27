select
    "RevenueMonth" as revenue_month,
    "TotalRevenue" as total_revenue
from {{ source('retail_gold', 'monthly_revenue') }}