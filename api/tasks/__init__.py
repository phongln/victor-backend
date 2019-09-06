from .celery import celery, make_celery
with celery:
    from . import test
