# Setup Kong
docker run --rm  \
    --link=postgres \
    -e "KONG_DATABASE=postgres" \
    -e "KONG_PG_HOST=postgres" \
    -e "KONG_PG_USER=kong" \
    -e "KONG_PG_PORT=5432" \
    -e "KONG_PG_PASSWORD=Aa123456" \
    kong:latest kong migrations bootstrap

docker run -d --name kong \
    --link=postgres \
    -e "KONG_DATABASE=postgres" \
    -e "KONG_PG_HOST=postgres" \
    -e "KONG_PG_USER=kong" \
    -e "KONG_PG_PASSWORD=Aa123456" \
    -e "KONG_PG_PORT=5432" \
    -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
    -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
    -e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
    -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
    -e "KONG_ADMIN_LISTEN=0.0.0.0:8001, 0.0.0.0:8444 ssl" \
    -p 80:8000 \
    -p 8443:8443 \
    -p 8001:8001 \
    -p 8444:8444 \
    kong:latest

# Setup Konga Admin dashboard

docker run --rm \
    --link=postgres \
    pantsel/konga -c prepare -a postgres -u postgresql://kong:Aa123456@postgres:5432/konga

docker run -d --name konga \
    --link=postgres \
    -e "DB_ADAPTER=postgres" \
    -e "DB_HOST=postgres" \
    -e "DB_USER=kong" \
    -e "DB_PASSWORD=Aa123456" \
    -e "DB_DATABASE=konga" \
    -e "KONGA_HOOK_TIMEOUT=120000" \
    -e "NODE_ENV=production" \
    -p 1337:1337 \
    pantsel/konga:latest