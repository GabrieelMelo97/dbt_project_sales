select sh.company_name   ,  se.shipper_email from 
{{source('sources','shippers')}} sh
left join {{source('sources','shippers_emails')}} se on (sh.shipper_id = se.shipper_id)