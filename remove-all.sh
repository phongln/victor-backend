#!/bin/bash

# Warning: this will clean up docker system
# include:
# + unused containers
# + unused networks
# + unused dangling images
# + unused volumes

PROJECT_NAME=victor
DOCKER_COMPOSE_DIR='./docker-compose'

for _compose_file in $DOCKER_COMPOSE_DIR/[^_]*.yml; do

    docker-compose -p $PROJECT_NAME -f $_compose_file down -v --rmi local
done

docker system prune -f
docker image prune -f
docker volume prune -f

echo 'Finish.'