from sqlalchemy import orm, Table, Column, Integer, ForeignKey, String

from .base import BaseModel
from . import getTable


__all__ = [
    'RefContact',
    'RefMedia',
    'RefSkill',
    'RefTopic',
    'ViewAllRefTable'
]


class RefContact(BaseModel):
    __tablename__ = 'ref_contact'
    __schemaname__ = 'RefContactSchema'


class RefMedia(BaseModel):
    __tablename__ = 'ref_media'
    __schemaname__ = 'RefMediaSchema'


class RefSkill(BaseModel):
    __tablename__ = 'ref_skill'
    __schemaname__ = 'RefSkillSchema'


class RefTopic(BaseModel):
    __tablename__ = 'ref_topic'
    __schemaname__ = 'RefTopicSchema'


class ViewAllRefTable(BaseModel):
    columns = [Column('table_name', String(64), primary_key=True), ]
    __table__ = getTable('v_all_ref_table', columns)
    __schemaname__ = 'ViewAllRefTableSchema'
