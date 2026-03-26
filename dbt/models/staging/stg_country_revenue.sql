select
    Country as country,
    TotalRevenue as total_revenue
from {{ source('retail_gold', 'country_revenue') }}