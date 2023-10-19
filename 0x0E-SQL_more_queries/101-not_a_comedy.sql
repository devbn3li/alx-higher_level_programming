-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT DISTINCT t.title
FROM tv_shows t
LEFT JOIN tv_show_genres s ON s.show_id = t.id
LEFT JOIN tv_genres g ON g.id = s.genre_id
WHERE t.title NOT IN (
  SELECT t2.title
  FROM tv_shows t2
  INNER JOIN tv_show_genres s2 ON s2.show_id = t2.id
  INNER JOIN tv_genres g2 ON g2.id = s2.genre_id
  WHERE g2.name = 'Comedy'
)
ORDER BY t.title ASC;
