-- lists all genres not linked to the show Dexter
USE hbtn_0d_tvshows;

SELECT genres.name
FROM genres
WHERE genres.id NOT IN (
    SELECT genre_id
FROM tv_show_genres
    JOIN tv_shows ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_shows.title = 'Dexter'
)
ORDER BY genres.name ASC;
