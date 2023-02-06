SELECT HOUR(DATETIME) AS HOUR, COUNT(ANIMAL_ID) AS COUNT FROM ANIMAL_OUTS WHERE HOUR(DATETIME) BETWEEN 9 AND 20 GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME);