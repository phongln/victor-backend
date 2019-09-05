from celery import Celery


__all__ = ['make_celery']
_celery = Celery(__name__)

with _celery:
    from api.config import celeryconfig

    _celery.config_from_object(celeryconfig)


def make_celery(app=None):
    _celery.conf.update(app.config)

    class ContextTask(_celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    _celery.Task = ContextTask

    return _celery
