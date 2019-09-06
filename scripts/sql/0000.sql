drop database if exists blog;
create database blog;

drop user if exists blog_api;
create user blog_api with encrypted password 'Aa123456';
grant all privileges on database blog to blog_api;