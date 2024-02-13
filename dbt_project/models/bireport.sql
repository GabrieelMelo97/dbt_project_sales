{{
    config(
        materialized='table'
    )

}}
select * from {{ref('joins')}}