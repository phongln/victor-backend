create materialized view v_user_profile 
as
select 
	t1.*,
	t2.brief_description, t2.education, t2.position, t2.company_name,
	t3.address1, t3.address2, t3.phone1, t3.phone2, t3.mail, t3.mail2
from user_profile t1
left join user_info t2 on t2.user_id = t1.user_id
left join user_contact t3 on t3.user_id = t1.user_id
