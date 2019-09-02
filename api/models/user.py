from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import backref, relationship

from .base import BaseModel
from . import getTable


__all__ = [
    'ViewUserProfile',
    'ViewUserContact',
    'UserInfoAll',
    'JsonUserContact'
]

# View user profile


class ViewUserProfile(BaseModel):
    columns = [Column('user_id', Integer, primary_key=True)]

    __table__ = getTable('v_user_profile', columns)
    __schemaname__ = 'ViewUserProfileSchema'

# View user contact


class ViewUserContact(BaseModel):
    columns = (
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey('v_user_profile.user_id')),
    )

    __table__ = getTable('v_user_contact', columns)
    __schemaname__ = 'ViewUserContactSchema'


# --------------------------------------------------------
# ---- User Info Relationship
# --------------------------------------------------------


class UserInfoAll(ViewUserProfile):
    __table__ = ViewUserProfile.__table__
    __schemaname__ = 'UserInfoAllSchema'

    rel_child = relationship(
        "JsonUserContact", backref=backref("user_info"))


class JsonUserContact(BaseModel):
    columns = [
        Column('user_id', Integer,  ForeignKey(
            'v_user_profile.user_id'), primary_key=True),
    ]
    __table__ = getTable('json_user_contact', columns)
    __schemaname__ = 'JsonUserContactSchema'

    rel_parent = relationship(
        "UserInfoAll", backref=backref("contacts", uselist=False))
