select
    country,
    total_revenue
from {{ ref('stg_country_revenue') }}