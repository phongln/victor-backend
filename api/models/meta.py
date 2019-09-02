from sqlalchemy import orm, Table, Column, Integer, ForeignKey, String

from .base import BaseModel, BaseSchema
from . import getTable


class RefContact(BaseModel):
    __tablename__ = 'ref_contact'

    @classmethod
    def get_schema(cls):
        return RefContactSchema


class RefContactSchema(BaseSchema):
    class Meta:
        model = RefContact
        fields = ['contact_type_id', 'contact_type']


class RefMedia(BaseModel):
    __tablename__ = 'ref_media'

    @classmethod
    def get_schema(cls):
        return RefMediaSchema


class RefMediaSchema(BaseSchema):
    class Meta:
        model = RefMedia
        fields = ['media_id', 'media_name']


class RefSkill(BaseModel):
    __tablename__ = 'ref_skill'

    @classmethod
    def get_schema(cls):
        return RefSkillSchema


class RefSkillSchema(BaseSchema):
    class Meta:
        model = RefSkill
        fields = ['skill_id', 'skill_name']


class RefTopic(BaseModel):
    __tablename__ = 'ref_topic'

    @classmethod
    def get_schema(cls):
        return RefTopicSchema


class RefTopicSchema(BaseSchema):
    class Meta:
        model = RefTopic
        fields = ['topic_id', 'topic_name', 'description']


class ViewAllRefTable(BaseModel):
    columns = [Column('table_name', String(64), primary_key=True), ]
    __table__ = getTable('v_all_ref_table', columns)

    @classmethod
    def get_schema(cls):
        return ViewAllRefTableSchema


class ViewAllRefTableSchema(BaseSchema):
    class Meta:
        model = ViewAllRefTable
        fields = ['table_name', 'table_data']
