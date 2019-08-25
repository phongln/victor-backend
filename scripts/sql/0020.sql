insert into ref_contact(contact_type_id, contact_type, ord_num)
values
(1, 'phone', 2),
(2, 'mail', 3),
(3, 'address', 1);

insert into ref_media (media_id, media_name, ord_num)
values 
(1, 'github', 1),
(2, 'skype', 2),
(3, 'linkedin', 3),
(4, 'reddit', 4);


insert into user_profile (
 status ,
 username,
 password,
 fullname,
 nickname,
 birthday,
 gender
)
values ('1', 'vinhpham', md5('Aa123456'), 'Pham Tan Vinh', 'Victor Pham', '1994-12-08', 'm');

insert into user_profile (
 status ,
 username,
 password,
 fullname,
 nickname,
 birthday,
 gender
)
values ('1', 'vinhpham', md5('Aa123456'), 'Pham Tan Vinh', 'Victor Pham', '1994-12-08', 'm');

insert into user_contact (user_id, contact_type_id, contact_name, ord_num)
values 
('1', '3', 'Ho Chi Minh, Vietnam', 1),
('1', '3', 'Tien Giang, Vietnam', 2),
('1', '1', '836299xxxx', 1),
('1', '1', '090485xxxx', 2),
('1', '2', 'phamtanvinh.me@gmail.com', 1),
('1', '2', 'phamtanvinh_me@yahoo.com', 2);