FROM postgres:latest

COPY ./backup/blog.bak /home
COPY ./sql/0000.sql /home
COPY ./10-init.sh  /docker-entrypoint-initdb.d/10-init.sh