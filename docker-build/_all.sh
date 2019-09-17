#!/bin/sh

export BASE_DIR=$(realpath $(dirname $0))
[ -z $ROOT_DIR ] && ROOT_DIR=$(dirname $BASE_DIR)

cd $ROOT_DIR

for _command in $BASE_DIR/[^_]*.sh; do
    bash $_command
done