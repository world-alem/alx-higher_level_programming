-- imported database
SELECT city, AVG(value) AS temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY temp DESC LIMIT 3;

