select
    revenue_month,
    total_revenue
from {{ ref('stg_monthly_revenue') }}