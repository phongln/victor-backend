import os

redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_db = os.getenv('CELERY_REDIS_DB')

BROKER_URL = os.getenv(
    'BROKER_URL') or f'redis://{redis_host}:{redis_port}/{redis_db}'
CELERY_RESULT_BACKEND = os.getenv(
    'CELERY_RESULT_BACKEND') or f'redis://{redis_host}:{redis_port}/{redis_db}'

broker_url = BROKER_URL
result_backend = CELERY_RESULT_BACKEND
