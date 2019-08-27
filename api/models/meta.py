from sqlalchemy import orm, Table, Column, Integer, ForeignKey, String

from .base import BaseModel, BaseSchema, apply_schema, getTable


@apply_schema('RefContactSchema')
class RefContact(BaseModel):
    __tablename__ = 'ref_contact'


class RefContactSchema(BaseSchema):
    class Meta:
        model = RefContact
        fields = ['contact_type_id', 'contact_type']


@apply_schema('RefMediaSchema')
class RefMedia(BaseModel):
    __tablename__ = 'ref_media'


class RefMediaSchema(BaseSchema):
    class Meta:
        model = RefMedia
        fields = ['media_id', 'media_name']


@apply_schema('RefSkillSchema')
class RefSkill(BaseModel):
    __tablename__ = 'ref_skill'


class RefSkillSchema(BaseSchema):
    class Meta:
        model = RefSkill
        fields = ['skill_id', 'skill_name']


@apply_schema('RefTopicSchema')
class RefTopic(BaseModel):
    __tablename__ = 'ref_topic'


class RefTopicSchema(BaseSchema):
    class Meta:
        model = RefTopic
        fields = ['topic_id', 'topic_name', 'description']


@apply_schema('ViewAllRefTableSchema')
class ViewAllRefTable(BaseModel):
    columns = [Column('table_name', String(64), primary_key=True), ]
    __table__ = getTable('v_all_ref_table', columns)


class ViewAllRefTableSchema(BaseSchema):
    class Meta:
        model = ViewAllRefTable
        fields = ['table_name', 'table_data']
