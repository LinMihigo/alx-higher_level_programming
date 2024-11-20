-- lists all shows and all genres linked to that show from hbtn_0d_tvshows
USE hbtn_0d_tvshows;

SELECT tv_shows.title, genres.name
FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
    LEFT JOIN genres ON genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, genres.name ASC;
