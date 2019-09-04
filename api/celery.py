from celery import Celery
from api.config import config


celery = Celery(
    __name__,
    backend=config.CELERY_RESULT_BACKEND,
    broker=config.CELERY_BROKER_URL
)

with celery:
    from api import tasks


def make_celery(app=None):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask

    return celery
