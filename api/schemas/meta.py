from .base import BaseSchema
from api.models.meta import *

__all__ = [
    'RefContactSchema',
    'RefMediaSchema',
    'RefSkillSchema',
    'RefTopicSchema',
    'ViewAllRefTableSchema'
]


class RefContactSchema(BaseSchema):
    class Meta:
        model = RefContact
        fields = ['contact_type_id', 'contact_type']


class RefMediaSchema(BaseSchema):
    class Meta:
        model = RefMedia
        fields = ['media_id', 'media_name']


class RefSkillSchema(BaseSchema):
    class Meta:
        model = RefSkill
        fields = ['skill_id', 'skill_name']


class RefTopicSchema(BaseSchema):
    class Meta:
        model = RefTopic
        fields = ['topic_id', 'topic_name', 'description']


class ViewAllRefTableSchema(BaseSchema):
    class Meta:
        model = ViewAllRefTable
        fields = ['table_name', 'table_data']
