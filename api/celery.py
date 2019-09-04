from celery import Celery


celery = Celery(__name__)

with celery:
    from api.config import celeryconfig
    from api import tasks

    celery.config_from_object(celeryconfig)


def make_celery(app=None):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask

    return celery
