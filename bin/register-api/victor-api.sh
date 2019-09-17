cd $([ ! -z $BASE_DIR ] && echo $BASE_DIR || echo $(dirname $0))
KONG_ADMIN_URL=$([ ! -z $KONG_HOST ] && echo "$KONG_HOST:$KONG_ADMIN_PORT" || echo "localhost:8001")
SERVICE_NAME="balancer-backend"

# register a service
curl -i -X POST \
    --url http://$KONG_ADMIN_URL/services/ \
    --data "name=$SERVICE_NAME" \
    --data "url=http://$SERVICE_NAME"


# register a route
curl -i -X POST \
    --url http://$KONG_ADMIN_URL/services/$SERVICE_NAME/routes \
    --data "name=$SERVICE_NAME" \
    --data "hosts[]=$SERVICE_NAME" \
    --data "strip_path=false" \
    --data "methods[]=GET"

exit 0

# test api
curl -i -X GET \
    --url http://localhost:8000/api/v1/user \
    --header "Host: $SERVICE_NAME"