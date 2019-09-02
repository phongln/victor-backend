from . import ma


class BaseSchema(ma.Schema):
    class Meta:
        fields = []

    @classmethod
    def merge_fields(cls, fields=[]):
        return cls.Meta.fields + fields
