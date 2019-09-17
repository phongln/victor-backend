#!/bin/bash

export PROJECT_NAME=victor
export DOCKER_API_VERSION='1.40'
export DOCKER_SOCKET='/var/run/docker.sock'

export ROOT_DIR=$(realpath $(dirname $0))
export PY_SCRIPTS=$ROOT_DIR/bin/py-scripts


# prepairing
bash ./init-env-file.sh
bash ./docker-build/_all.sh
bash ./docker-resource/_all.sh

# up all services
bash ./docker-compose/_all.sh

# register services to kong
bash ./bin/register-api/_all.sh

docker system prune -f