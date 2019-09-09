# Welcome to Victor Blog Backend

This is my backend repo to setup working framework with docker.


### Features
- Microservice.
- Docker maintanence.
- Gateway for security, reverse proxy and load-balancing ...
- Scalability.


### Tech stack
- Database: postgres + pgadmin4, redis
- Task: celery + redis + flower
- Gateway: Kong + Konga + Nginx
- API backend: Flask


### Requirements
Your machine will be installed docker.

Let's start.


### How to use
```sh
git clone --depth 1 git@github.com:phamtanvinh/victor-backend.git
cd victor-backend
bash ./start_all.sh
```


### Test
```sh
curl localhost:5000/test
```


### Monitor
- [flower for tasks](http://localhost:5555)
- [pgadmin4 for postgres](httl://localhost:8088)


### Todo
- Setup Kong to control all APIs
- Setup Nginx Web server
- Integrate Search engine (elasticsearch), ELK
- Integrate Kafka
