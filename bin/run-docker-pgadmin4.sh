docker run -d --name pgadmin4 \
    -e PGADMIN_DEFAULT_EMAIL=phamtanvinh.me@gmail.com \
    -e PGADMIN_DEFAULT_PASSWORD=Aa123456 \
    -p 8088:80 \
    dpage/pgadmin4