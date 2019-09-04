# register a service
curl -i -X POST \
    --url http://localhost:8001/services/ \
    --data 'name=testApi' \
    --data 'url=https://jsonplaceholder.typicode.com'


# register a route
curl -i -X POST \
    --url http://localhost:8001/services/testApi/routes \
    --data 'hosts[]=localhost' \
    --data 'strip_path=false' \
    --data 'paths[]=/todos' \
    --data 'methods[]=GET'


# test api
curl -i -X GET \
    --url http://localhost:8000/todos/1 \
    --header 'Host:localhost'