import time
from celery import task


@task
def very_long_task(seconds=5):
    time.sleep(seconds)
    return {'message': 'This task only hangs out', 'status_code': '200'}
