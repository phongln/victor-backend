docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=Aa123456 -d postgres
docker run --name pgadmin4 -p 443:443 -e PGADMIN_DEFAULT_EMAIL=phamtanvinh.me@gmail.com -e PGADMIN_DEFAULT_PASSWORD=Aa123456 -d dpage/pgadmin4
