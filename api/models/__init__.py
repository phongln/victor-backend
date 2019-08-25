from functools import wraps
from sqlalchemy import Table

from api.database import db, ma


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'autoload': True,
                      'autoload_with': db.engine, 'extend_existing': True}

    @classmethod
    def get_ma_schema(cls):
        module_name = cls.__module__
        schema_name = cls.schema_name

        import sys
        ma_schema = getattr(sys.modules[module_name], schema_name)

        return ma_schema

    @classmethod
    def jsonify(cls, respone, many=False):
        ma_schema = cls.get_ma_schema()
        return ma_schema(many=many).jsonify(respone)

    def json(self, many=False):
        ma_schema = self.__class__.get_ma_schema()

        return ma_schema(many=many).jsonify(self)


class BaseSchema(ma.Schema):
    class Meta:
        fields = []

    @classmethod
    def merge_fields(cls, fields=[]):
        return cls.Meta.fields + fields


def apply_schema(schema_name: str) -> 'Model':
    """Add schema name string to class"""
    def inner_class(cls):
        @wraps(cls)
        def wrapper():
            setattr(cls, 'schema_name', schema_name)
            return cls
        return wrapper()
    return inner_class


def getTable(tablename, columns):
    return Table(tablename, db.metadata, *columns, **BaseModel.__table_args__)
