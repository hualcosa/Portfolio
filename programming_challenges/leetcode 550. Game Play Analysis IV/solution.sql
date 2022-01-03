# Write your MySQL query statement below
with
 first_date_of_each_player as (
 select player_id, min(event_date) as first_date
 from activity
 group by player_id
)
select round(count(distinct a.player_id) / count(f.player_id), 2) as fraction
from Activity a
right join first_date_of_each_player f
    on  a.player_id = f.player_id AND
        a.event_date = f.first_date + 1