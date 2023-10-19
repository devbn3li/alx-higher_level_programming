-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT DISTINCT g.name
FROM tv_genres g
INNER JOIN tv_show_genres s ON g.id = s.genre_id
INNER JOIN tv_shows t ON s.show_id = t.id
WHERE g.name NOT IN (
  SELECT DISTINCT g2.name
  FROM tv_genres g2
  INNER JOIN tv_show_genres s2 ON g2.id = s2.genre_id
  INNER JOIN tv_shows t2 ON s2.show_id = t2.id
  WHERE t2.title = 'Dexter'
)
ORDER BY g.name ASC;
