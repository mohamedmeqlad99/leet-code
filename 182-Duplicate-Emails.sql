SELECT email
FROM Person
GROUP by email
HAVING count(email) > 1
