-- import db dump, hbtn_0d_tvshows. - lists all shows in db
USE hbtn_0d_tvshows;

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
