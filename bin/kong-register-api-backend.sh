# register a service
curl -i -X POST \
    --url http://localhost:8001/services/ \
    --data 'name=backend-api' \
    --data 'url=http://backend-api:5000'


# register a route
curl -i -X POST \
    --url http://localhost:8001/services/backend-api/routes \
    --data 'hosts[]=backend-api' \
    --data 'strip_path=false' \
    --data 'methods[]=GET'


# test api
curl -i -X GET \
    --url http://localhost:8000/user \
    --header 'Host: backend-api'