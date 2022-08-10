-- imported database
SELECT state, MAX(value) AS temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
