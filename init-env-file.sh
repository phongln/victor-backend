# declaration
# HOST_NAME=$(hostname)
HOST_NAME='localhost'
ENV_FILE='.env'
HOST_IP= # osx default

function join_path {
    python bin/py-scripts/get-path.py "$@"
}

function darwin_init {
    HOST_IP='172.17.0.1'
}

function linux_init {
    HOST_IP=$(/sbin/ip route|awk '/default/ { print $3 }')
}

case $OSTYPE in 
    darwin*) darwin_init ;;
    linux*) linux_init ;;
    msys*) ;;
    *) ;;
esac

# variables Setting

CONTEXT_ROOT=$(join_path "$(pwd)")
CONTEXT_API=$(join_path "$CONTEXT_ROOT" "api")
CONTEXT_TASK="$CONTEXT_API"

cat > $ENV_FILE <<EOF
##########################################################################
#
# Base Setting
#
##########################################################################

CONTEXT_ROOT=$CONTEXT_ROOT
CONTEXT_TASK=$CONTEXT_TASK

HOST_IP=$HOST_IP

##########################################################################
#
# Database Setting
#
##########################################################################

POSTGRES_USER=postgres
POSTGRES_PASSWORD=Aa123456

PGADMIN_DEFAULT_EMAIL=phamtanvinh.me@gmail.com
PGADMIN_DEFAULT_PASSWORD=Aa123456


##########################################################################
#
# Task Setting
#
##########################################################################

TASK_QUEUE_HOST=
TASK_QUEUE_PORT=

BROKER_REDIS_DB=0
RESULT_REDIS_DB=1


##########################################################################
#
# Gateway Setting
#
##########################################################################

KONG_PG_DATABASE=postgres
KONG_PG_USER=kong
KONG_PG_PASSWORD=Aa123456

KONGA_DB=konga


##########################################################################
#
# API Backend Setting
#
##########################################################################

API_PG_PORT=5432
API_PG_DB=blog
API_PG_USER=blog_api
API_PG_PASSWORD=Aa123456

##########################################################################
#
# Nginx Setting
#
##########################################################################

HOST_NAME=$HOST_NAME

PROXY_TASK_MONITOR=task-monitor.$HOST_NAME
PROXY_PGADMIN=pgadmin.$HOST_NAME
PROXY_KONGA=konga.$HOST_NAME
PROXY_BACKEND_API=backend-api.$HOST_NAME
PROXY_GATEWAY=api.$HOST_NAME
PROXY_BALANCER_CONSUL=balancer-consul.$HOST_NAME
PROXY_ELK_KIBANA=elk-kibana.$HOST_NAME

EOF