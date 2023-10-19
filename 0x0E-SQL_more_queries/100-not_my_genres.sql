-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT DISTINCT gen.name
FROM tv_genres g
INNER JOIN tv_show_genres s ON g.id = s.genre_id
INNER JOIN tv_shows t ON s.show_id = t.id
WHERE gen.name NOT IN (
  SELECT DISTINCT gen2.name
  FROM tv_genres gen2
  INNER JOIN tv_show_genres s2 ON gen2.id = s2.genre_id
  INNER JOIN tv_shows t2 ON s2.show_id = t2.id
  WHERE t2.title = 'Dexter'
)
ORDER BY gen.name ASC;
