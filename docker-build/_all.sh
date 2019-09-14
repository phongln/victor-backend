BASE_DIR=$(dirname $0)

for _command in $BASE_DIR/[^_]*; do
    bash $_command
done