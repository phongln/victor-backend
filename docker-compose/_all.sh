#!/bin/sh

export BASE_DIR=$(realpath $(dirname $0))
[ -z $PROJECT_NAME ] && PROJECT_NAME='victor'
[ -z $ROOT_DIR ] && ROOT_DIR=$(dirname $BASE_DIR)

cd $ROOT_DIR

for _compose_file in $BASE_DIR/[^_]*.yml; do
    docker-compose -p $PROJECT_NAME -f $_compose_file up -d --build
done