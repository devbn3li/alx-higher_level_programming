-- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres g
INNER JOIN tv_show_genres s ON s.genre_id = g.id
INNER JOIN tv_show_ratings r ON r.show_id = s.show_id
GROUP BY g.name
ORDER BY rating DESC;
