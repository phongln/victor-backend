create materialized view v_user_profile 
as
select 
	t1.*,
	t2.brief_description, t2.education, t2.position, t2.company_name
from user_profile t1
left join user_info t2 on t2.user_id = t1.user_id;

create materialized view v_user_contact
as
select
	t1.id,
	t1.user_id, 
	t2.contact_type, 
	t1.contact_name,
	t1.ord_num 
from user_contact t1
inner join ref_contact t2 on t1.contact_type_id = t2.contact_type_id;