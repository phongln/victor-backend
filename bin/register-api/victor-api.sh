cd $([ ! -z $BASE_DIR ] && echo $BASE_DIR || echo $(dirname $0))
KONG_ADMIN_URL=$([ ! -z $KONG_HOST ] && echo "$KONG_HOST:$KONG_ADMIN_PORT" || echo 'localhost:8001')

# register a service
curl -i -X POST \
    --url http://$KONG_ADMIN_URL/services/ \
    --data 'name=balancer-nginx' \
    --data 'url=http://balancer-nginx'


# register a route
curl -i -X POST \
    --url http://$KONG_ADMIN_URL/services/balancer-nginx/routes \
    --data "name=balancer-nginx" \
    --data 'hosts[]=balancer-nginx' \
    --data 'strip_path=false' \
    --data 'methods[]=GET'

exit 0

# test api
curl -i -X GET \
    --url http://localhost:8000/api/v1/user \
    --header 'Host: balancer-nginx'