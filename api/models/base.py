from api.database import db, ma


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'autoload': True,
                      'autoload_with': db.engine, 'extend_existing': True}

    @classmethod
    def get_schema(cls):
        raise NotImplementedError('Need to add schema.')


class BaseSchema(ma.Schema):
    class Meta:
        fields = []

    @classmethod
    def merge_fields(cls, fields=[]):
        return cls.Meta.fields + fields
