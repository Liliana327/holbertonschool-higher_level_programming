-- Import the database dump of hbtn_0d_tvshows
SELECT tv_genres.name as genre, COUNT(tv_show_genres.genre_id) as number_shows
FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id  = tv_genres.id GROUP BY tv_genres.name
ORDER BY number_shows DESC;
