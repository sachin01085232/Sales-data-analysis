-- Region-wise avg sales
select region,
avg(sales_amount) from sales
group by region
-- Orders with sales > company avg

select *
from sales
where sales_amount > (
select  avg(sales_amount)
from sales
 )

-- Top 3 orders per region (window function)

SELECT *
FROM (
    SELECT
        order_id,
        region,
        sales_amount,
        DENSE_RANK() OVER (
            PARTITION BY region
            ORDER BY sales_amount DESC
        ) AS drnk
    FROM sales
) t
WHERE drnk <= 3;

SELECT *
FROM (
    SELECT
        order_id,
        region,
        sales_amount,
        ROW_NUMBER	() OVER (
            PARTITION BY region
            ORDER BY sales_amount DESC
        ) AS drnk
    FROM sales
) t
WHERE drnk IN (1, 2, 3);



-- Monthly sales trend
SELECT
    EXTRACT(YEAR  FROM order_date::date)  AS year,
    EXTRACT(MONTH FROM order_date::date) AS month,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY year,month
ORDER BY year, month;

-- year wise sales

select 
 EXTRACT(YEAR FROM order_date::date) AS year,
sum (sales_amount) as total_sales
from sales
group by year
order by total_sales desc


--   % of returned orders
SELECT
    SUM(sales_amount) FILTER (WHERE returned = 'Yes') * 100.0 /
	SUM(sales_amount) AS returned_sales_percentage

FROM sales;
