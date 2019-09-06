# register a service
curl -i -X POST \
    --url http://localhost:8001/services/ \
    --data 'name=task-monitor' \
    --data 'url=https://task-monitor:5555'


# register a route
curl -i -X POST \
    --url http://localhost:8001/services/task-monitor/routes \
    --data 'hosts[]=task-monitor' \
    --data 'strip_path=false' \
    --data 'methods[]=GET'


# test api
curl -i -X GET \
    --url http://localhost:8000/ \
    --header 'Host:task-monitor'