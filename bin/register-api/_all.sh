export BASE_DIR=$(dirname $0)
export KONG_HOST='localhost'
export KONG_ADMIN_PORT=8001

for _command in $BASE_DIR/[^_]*; do
    bash $_command
done