# Write your MySQL query statement below

with managers_info as (
SELECT managerId, COUNT(*) AS n
FROM Employee
GROUP BY managerId
HAVING COUNT(*) >= 5
)
select name from
Employee e
join managers_info m on e.id = m.managerId
