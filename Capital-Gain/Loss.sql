WITH cte AS (
    SELECT 
        stock_name,
        CASE
            WHEN operation = 'Buy' THEN -1 * price
            WHEN operation = 'Sell' THEN  price
        END AS new_price
    FROM Stocks
)
SELECT stock_name, SUM(new_price) AS capital_gain_loss
FROM cte
GROUP BY stock_name
