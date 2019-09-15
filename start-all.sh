#!/bin/bash

PROJECT_NAME=victor
DOCKER_COMPOSE_DIR='./docker-compose'

bash ./init-env-file.sh
bash ./init-docker-resource.sh

for _compose_file in $DOCKER_COMPOSE_DIR/[^_]*.yml; do
    docker-compose -p $PROJECT_NAME -f $_compose_file up -d --build
done

# register services to kong
bash ./bin/register-api/_all.sh

docker system prune -f
