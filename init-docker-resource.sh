VOLUMN_DB=db_data
VOLUMN_KONG=kong_data
NETWORK_BACKEND=backend-net
IMAGE_BACKEND_API=backend-api
BUILD_BACKEND_API='./bin/docker-build-api-backend.sh'
IMAGE_VICTOR_NGINX=victor-nginx
BUILD_VICTOR_NGINX='./bin/docker-build-victor-nginx.sh'


function create_volume {
    docker volume inspect $1 > /dev/null 2>&1 \
        && echo "Existed volume $1" \
        || (docker volume create $1 && echo "Created volume $1")
}

function create_network {
    docker network inspect $1 > /dev/null 2>&1 \
        && echo "Existed network $1" \
        || (docker network create $1 && echo "Created network $1")
}

function create_image {
    docker image inspect $1 > /dev/null 2>&1 \
        && echo "Existed image $1" \
        || (bash $2 && echo "Created image $1")
}

# initialize

create_network $NETWORK_BACKEND
create_volume $VOLUMN_DB
create_volume $VOLUMN_KONG
create_image $IMAGE_BACKEND_API $BUILD_BACKEND_API
create_image $IMAGE_VICTOR_NGINX $BUILD_VICTOR_NGINX