FROM python:3.7-alpine

RUN mkdir /queue
WORKDIR /queue

ADD ./tasks /queue/tasks
ADD ./monitor/requirements.txt /queue

RUN pip install -r requirements.txt

ENTRYPOINT celery -A tasks.celery worker -l info