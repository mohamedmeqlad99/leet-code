WITH RankedScores AS (
    SELECT 
        student_id,
        subject,
        score,
        exam_date,
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date ASC) AS rn_first,
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS rn_last
    FROM Scores
),
first_score AS (
    SELECT student_id, subject, score AS first_score
    FROM RankedScores
    WHERE rn_first = 1
),
latest_score AS (
    SELECT student_id, subject, score AS latest_score
    FROM RankedScores
    WHERE rn_last = 1
)
SELECT 
    f.student_id,
    f.subject,
    f.first_score,
    l.latest_score
FROM first_score AS f
JOIN latest_score AS l
    ON f.student_id = l.student_id AND f.subject = l.subject AND f.first_score < l.latest_score
ORDER BY f.student_id, f.subject;