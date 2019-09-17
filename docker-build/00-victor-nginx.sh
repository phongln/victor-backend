#!/bin/sh

BASE_DIR=$(realpath $(dirname $0))
[ -z $ROOT_DIR ] && ROOT_DIR=$(dirname $BASE_DIR)

CT_VERSION=0.22.0
CT_FILENAME=consul-template_0.22.0_linux_amd64.zip
CT_URL=https://releases.hashicorp.com/consul-template

cd $ROOT_DIR/nginx

docker build -t victor-nginx . \
    --build-arg CT_VERSION=$CT_VERSION \
    --build-arg CT_FILENAME=$CT_FILENAME \
    --build-arg CT_URL=$CT_URL