#!/bin/bash

PROJECT_NAME=victor
DOCKER_COMPOSE_DIR='./docker-compose'

bash ./init-env-file.sh
bash ./init-docker-resource.sh
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/db.yml up -d --build
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/tasks.yml up -d --build
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/api.yml up -d --build
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/gateway.yml up -d --build
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/nginx-proxy.yml up -d --build
docker system prune -f


# register services to kong
bash ./bin/kong-register-api-backend.sh