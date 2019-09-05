FROM python:3.7-alpine

ENV REDIS_HOST redis_queue
ENV REDIS_PORT 6379

RUN mkdir /queue
WORKDIR /queue

ADD ./tasks /queue/tasks
ADD ./monitor/requirements.txt /queue

RUN pip install -r requirements.txt

ENTRYPOINT celery -A tasks.celery worker -l info