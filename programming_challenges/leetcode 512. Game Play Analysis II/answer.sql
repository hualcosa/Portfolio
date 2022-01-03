# Write your MySQL query statement below
with min_date_per_player as
(SELECT player_id, MIN(event_date) as event_date
 FROM Activity
 GROUP BY player_id
)

SELECT act.player_id, act.device_id
FROM activity act
JOIN min_date_per_player m ON
    act.player_id = m.player_id AND  act.event_date = m.event_date

