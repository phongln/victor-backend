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

create materialized view v_all_ref_table
as
select 'ref_contact' as table_name,  array_to_json(array_agg(row_to_json(t1))) as table_data from ref_contact t1 union all
select 'ref_media' as table_name,  array_to_json(array_agg(row_to_json(t1))) as table_data from ref_media t1 union all
select 'ref_skill' as table_name,  array_to_json(array_agg(row_to_json(t1))) as table_data from ref_skill t1 union all
select 'ref_topic' as table_name,  array_to_json(array_agg(row_to_json(t1))) as table_data from ref_topic t1;


create unique index user_id_uniq on v_user_profile(user_id);
create unique index id_uniq on v_user_contact(id);
create unique index table_name_uniq on v_all_ref_table(table_name);

REFRESH MATERIALIZED VIEW CONCURRENTLY v_user_profile;
REFRESH MATERIALIZED VIEW CONCURRENTLY v_user_contact;
REFRESH MATERIALIZED VIEW CONCURRENTLY v_all_ref_table;
