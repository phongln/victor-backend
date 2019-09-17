#!/bin/sh

# config setting
NETWORK_CONFIG='networks.json'
VOLUME_CONFIG='volumes.json'
BASE_DIR=$(realpath $(dirname $0))

[ -z $ROOT_DIR ] && ROOT_DIR=$(dirname $BASE_DIR)
[ -z $DOCKER_API_VERSION ] && DOCKER_API_VERSION='1.40'
[ -z $DOCKER_SOCKET ] && DOCKER_SOCKET='/var/run/docker.sock'
PY_SCRIPTS="$ROOT_DIR/bin/py-scripts"

cd $ROOT_DIR
python=$(which python)
cmd_load_json=$PY_SCRIPTS/load-json.py


OLD_IFS=$IFS && IFS=$'\n'

# initialize networks
for _config in $($python $cmd_load_json $BASE_DIR/$NETWORK_CONFIG); do
    curl -s -X POST http:/$DOCKER_API_VERSION/networks/create \
        --unix-socket $DOCKER_SOCKET \
        -H "Content-Type: application/json" \
        -d $_config > /dev/null
done

# initialize volumes
for _config in $($python $cmd_load_json $BASE_DIR/$VOLUME_CONFIG); do
    curl -s -X POST http:/$DOCKER_API_VERSION/volumes/create \
        --unix-socket $DOCKER_SOCKET \
        -H "Content-Type: application/json" \
        -d $_config > /dev/null
done

IFS=$OLD_IFS

echo 'Created resources.'
