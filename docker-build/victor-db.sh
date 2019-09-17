#!/bin/sh

BASE_DIR=$(realpath $(dirname $0))
[ -z $ROOT_DIR ] && ROOT_DIR=$(dirname $BASE_DIR)

cd $ROOT_DIR/scripts

docker build -t victor-db .