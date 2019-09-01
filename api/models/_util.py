import sys
from functools import wraps
from flask import Response
from sqlalchemy import Table, Column
from typing import Any, List

from api.database import db
from api.models.base import BaseModel


def apply_schema(schema_name: str) -> db.Model:
    """Add schema name string to class"""
    def inner_class(cls):
        @wraps(cls)
        def wrapper():
            setattr(cls, 'schema_name', schema_name)
            return cls
        return wrapper()
    return inner_class


def getTable(tablename: str, columns: List[Column]) -> Table:
    return Table(tablename, db.metadata, *columns, **BaseModel.__table_args__)


def jsonify_respone(respone: BaseModel, many=False):
    if type(respone) == list:
        schema = respone[0].get_schema()
    else:
        schema = respone.get_schema()

    return schema(many=many).jsonify(respone)
