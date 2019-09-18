#!/bin/bash

export PROJECT_NAME=victor
export DOCKER_API_VERSION='1.40'
export DOCKER_SOCKET='/var/run/docker.sock' # default for linux and darwin

export ROOT_DIR=$(realpath $(dirname $0))
export PY_SCRIPTS=$ROOT_DIR/bin/py-scripts

python=$(which python || which python3)

# Prepairing
bash ./init-env-file.sh
$python -m pip install -q -r docker-client/requirements.txt
$python -m docker-client --resource_type all # Arg: all, volumes, images, networks

# Up all services
bash ./docker-compose/_all.sh

# Register services to kong
bash ./bin/register-api/_all.sh
