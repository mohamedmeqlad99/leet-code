WITH cte AS (
    SELECT actor_id, director_id
    FROM ActorDirector
    GROUP BY actor_id , director_id
    HAVING count(actor_id) > 2

)
SELECT actor_id , director_id
FROM cte
