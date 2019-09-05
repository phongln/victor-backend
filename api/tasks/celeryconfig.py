import os

redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')

broker_url = f'redis://{redis_host}:{redis_port}'
result_backend = f'redis://{redis_host}:{redis_port}'
