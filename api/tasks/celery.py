import re
from celery import Celery


__all__ = ['make_celery', 'celery', 'set_name']
TASK_NAME = __package__.split('.')[-1]


class BaseCelery(Celery):

    def gen_task_name(self, name, module):
        pattern = f'({TASK_NAME}.*)'
        result = re.search(pattern, module)
        if result:
            module = result.groups()[0]

        if module.endswith('.tasks'):
            module = module[:-6]

        return super().gen_task_name(name, module)


celery = BaseCelery()

with celery:
    from . import celeryconfig

    celery.config_from_object(celeryconfig)


def set_name(name) -> str:
    return f'{__name__}.{name}'


def make_celery(app=None):
    if app:
        celery.conf.update(app.config)

        class ContextTask(celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)
        celery.Task = ContextTask

    return celery
