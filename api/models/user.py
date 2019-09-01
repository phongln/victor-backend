from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import backref, relationship
from marshmallow.fields import Nested

from .base import BaseModel, BaseSchema
from ._util import getTable


# View user profile

class ViewUserProfile(BaseModel):
    columns = [Column('user_id', Integer, primary_key=True)]

    __table__ = getTable('v_user_profile', columns)

    @classmethod
    def get_schema(cls):
        return ViewUserProfileSchema


class ViewUserProfileSchema(BaseSchema):
    class Meta:
        model = ViewUserProfile
        fields = ['user_id', 'status', 'username',
                  'fullname', 'nickname', 'birthday', 'gender',
                  'createdon', 'updatedon', 'brief_description',
                  'education', 'position', 'company_name']


# View user contact

class ViewUserContact(BaseModel):
    columns = (
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey('v_user_profile.user_id')),
    )

    __table__ = getTable('v_user_contact', columns)

    @classmethod
    def get_schema(cls):
        return ViewUserContactSchema


class ViewUserContactSchema(BaseSchema):
    class Meta:
        model = ViewUserContact
        fields = ['id', 'user_id', 'contact_type', 'contact_name', 'ord_num']


# --------------------------------------------------------
# ---- User Info Relationship
# --------------------------------------------------------

class UserInfoAll(ViewUserProfile):
    __table__ = ViewUserProfile.__table__

    rel_child = relationship(
        "JsonUserContact", backref=backref("user_info"))

    @classmethod
    def get_schema(cls):
        return UserInfoAllSchema


class UserInfoAllSchema(BaseSchema):
    contacts = Nested('JsonUserContactSchema',
                      exclude=('user_id', 'user_info'))

    class Meta:
        model = UserInfoAll
        fields = ViewUserProfileSchema.merge_fields(['contacts'])


class JsonUserContact(BaseModel):
    columns = [
        Column('user_id', Integer,  ForeignKey(
            'v_user_profile.user_id'), primary_key=True),
    ]
    __table__ = getTable('json_user_contact', columns)

    @classmethod
    def get_schema(cls):
        return JsonUserContactSchema

    rel_parent = relationship(
        "UserInfoAll", backref=backref("contacts", uselist=False))


class JsonUserContactSchema(BaseSchema):
    user_info = Nested('UserInfoAllSchema',
                       only=('username',))

    class Meta:
        model = JsonUserContact
        fields = ['user_id', 'json_contacts', 'user_info']
