#!/bin/bash

PROJECT_NAME=victor
DOCKER_COMPOSE_DIR='./docker-compose'

bash ./init-env-file.sh
bash ./init-docker-resource.sh
docker-compose -f $DOCKER_COMPOSE_DIR/db.yml -p $PROJECT_NAME up -d --build
docker-compose -f $DOCKER_COMPOSE_DIR/tasks.yml -p $PROJECT_NAME up -d --build
docker-compose -f $DOCKER_COMPOSE_DIR/api.yml -p $PROJECT_NAME up -d --build
docker-compose -f $DOCKER_COMPOSE_DIR/gateway.yml -p $PROJECT_NAME up -d --build
docker system prune -f
