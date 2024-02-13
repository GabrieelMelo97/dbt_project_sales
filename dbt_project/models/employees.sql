--model employees
with calc_employees as (
    select 
    date_part('year', current_date) - date_part('year', birth_date) AS age,
    date_part('year', current_date) - date_part('year', hire_date) AS lengthofservice,
    first_name || ' ' || last_name AS name, *
    from {{source('sources','employees')}}
)
select * from calc_employees