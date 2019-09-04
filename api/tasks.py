import time
from api.celery import celery


@celery.task()
def very_long_task(seconds=5):
    time.sleep(seconds)
    return {'ok': '200'}
