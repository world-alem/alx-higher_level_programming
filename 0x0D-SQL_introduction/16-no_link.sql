-- exclude rows without a certain column
SELECT score, name
FROM second_table
WHERE NOT name=""
ORDER BY score DESC;
