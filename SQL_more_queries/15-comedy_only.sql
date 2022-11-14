-- script that lists all Comedy shows in the database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy (but the id can be different)
-- each record should display: tv_shows.title
-- results must be sorted in ascending order by the show title
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT `t`.`title`
FROM `tv_shows` AS `t`
       INNER JOIN `tv_show_genres` AS `s`
       ON `t`.`id` = `s`.`show_id`

       INNER JOIN `tv_genres` AS `g`
       ON `g`.`id` = `s`.`genre_id`
 WHERE `g`.`name` = "Comedy"
 ORDER BY `t`.`title` ASC;
