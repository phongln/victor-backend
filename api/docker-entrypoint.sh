#!/bin/sh

gunicorn api:app -c python:api.config.gunicornconfig