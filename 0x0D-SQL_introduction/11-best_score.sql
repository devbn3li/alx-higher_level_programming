-- file list all records in table second_table with score >= 10 in my MySQL server
-- file record are ordered by descending score
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10  ORDER BY `score` DESC;
