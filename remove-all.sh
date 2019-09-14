#!/bin/bash

PROJECT_NAME=victor
DOCKER_COMPOSE_DIR='./docker-compose'

docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/db.yml down -v --rmi local
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/tasks.yml down -v --rmi local
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/api.yml down -v --rmi local
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/gateway.yml down -v --rmi local
docker-compose -p $PROJECT_NAME -f $DOCKER_COMPOSE_DIR/nginx-proxy.yml down -v --rmi local
docker system prune -f
echo 'Finish.'