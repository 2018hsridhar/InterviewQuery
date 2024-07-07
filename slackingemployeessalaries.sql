-- Sum of salaries ( emps ) no completed projects ( not grouped ) 
-- unfinished : no end_date
-- emps must have at least one project
-- all emp projects have NULL as an end_date
-- SELECT SUM(emp.salary) as `total_slack_salary` FROM employees AS emp
-- https://www.interviewquery.com/questions/slacking-employees-salaries
WITH T1 AS (
    SELECT salary, 
        SUM(CASE WHEN End_dt IS NOT NULL THEN 1 ELSE 0 END) AS completed_project
    FROM employees AS E
    INNER JOIN projects AS P
    ON (E.id = P.employee_id)
    GROUP BY E.id
) SELECT SUM(salary) as total_slack_salary FROM T1
    WHERE (completed_project = 0)
