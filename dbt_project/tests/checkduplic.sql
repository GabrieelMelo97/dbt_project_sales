select count(*) count, companyname, contactname from
{{ref('customers')}}
group by companyname, contactname
having count > 1

/*este teste deve falhar
select count(*) count, companyname, contactname from
{{source('sources','customers')}}
group by companyname, contactname
having count > 1
*/