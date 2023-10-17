-- lists all records of the table second_table having a name value in my MySQL server
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC
