FROM python:3.7-alpine

WORKDIR /home
COPY ./requirements.txt /home

RUN echo "@edge-community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
# RUN apk update
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev python3-dev libpq
RUN pip install -r ./requirements.txt
# RUN apk del .build-deps

