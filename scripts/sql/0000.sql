drop database blog;
create database blog;
create user blog_api with encrypted password='Aa123456';
grant all privilleges on database blog to blog_api;