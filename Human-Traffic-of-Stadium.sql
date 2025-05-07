WITH visit AS (
    SELECT 
        id, 
        visit_date, 
        people,
        ROW_NUMBER() OVER (ORDER BY visit_date) AS row_num,
        id - ROW_NUMBER() OVER (ORDER BY visit_date) AS diff
    FROM Stadium
    WHERE people >= 100
)
SELECT 
    id, 
    visit_date, 
    people
FROM visit
WHERE diff IN (
    SELECT diff
    FROM visit
    GROUP BY diff
    HAVING COUNT(*) >= 3
);