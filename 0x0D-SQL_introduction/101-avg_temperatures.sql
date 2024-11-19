-- Displays the ave. temp (Fahr.) by city ordered by temp (Desc)
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
