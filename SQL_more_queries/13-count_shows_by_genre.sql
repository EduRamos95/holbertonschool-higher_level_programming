-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- each record should display: tv_genres.name - number_shows
-- don’t display a genre that doesn’t have any shows linked
-- results must be sorted in descending order by the number of shows linked
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT `g`.`name` AS `genre`,
COUNT(`t`.`genre_id`) AS `number_of_shows`
FROM `tv_genres` AS `g` 
	INNER JOIN `tv_show_genres` AS `t`
ON `g`.`id` = `t`.`genre_id`
 GROUP BY `genre` HAVING `number_of_shows` > 0
 ORDER BY `number_of_shows` DESC;
