-- lists the num of records with the same score in the table second_table in my MySQL server
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
