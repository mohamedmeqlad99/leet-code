SELECT id,
CASE WHEN P_id IS NULL THEN 'Root'
WHEN id NOT IN (select p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
ELSE 'Inner' END as type
FROM Tree