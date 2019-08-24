from api.database import db, ma


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'autoload': True,
                      'autoload_with': db.engine, 'extend_existing': True}

    @classmethod
    def get_ma_schema(cls):
        pass

    @classmethod
    def jsonify(cls, respone, many=False):
        ma_schema = cls.get_ma_schema()
        return ma_schema(many=many).jsonify(respone)

    def json(self, many=False):
        ma_schema = self.__class__.get_ma_schema()
        return ma_schema(many=many).jsonify(self)


class BaseSchema(ma.Schema):
    class Meta:
        pass

    @classmethod
    def merge_fields(cls, fields=[]):
        return cls.Meta.fields + fields
