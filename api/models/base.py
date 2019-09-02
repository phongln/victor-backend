from . import db


class BaseModel(db.Model):
    __abstract__ = True
    __schemaname__ = ''
    __table_args__ = {'autoload': True,
                      'autoload_with': db.engine, 'extend_existing': True}

    @classmethod
    def get_schema(cls):
        from api import schemas
        return getattr(schemas, cls.__schemaname__)
