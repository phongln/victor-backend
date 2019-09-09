ENV_FILE='.env'

# variables Setting
CONTEXT_ROOT="$(realpath .)"
CONTEXT_API="$CONTEXT_ROOT/api"
CONTEXT_DB="$CONTEXT_ROOT/scripts"
CONTEXT_TASK="$CONTEXT_API"

cat > $ENV_FILE <<EOF
##########################################################################
#
# Base Setting
#
##########################################################################

CONTEXT_ROOT=$CONTEXT_ROOT
CONTEXT_API=$CONTEXT_API
CONTEXT_TASK=$CONTEXT_TASK
CONTEXT_DB=$CONTEXT_DB


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

EOF