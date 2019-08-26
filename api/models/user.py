from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import backref, relationship

from api.database import db, ma
from api.models import BaseModel, BaseSchema, apply_schema, getTable


@apply_schema('UserProfileSchema')
class UserProfile(BaseModel):
    __tablename__ = 'user_profile'


class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'status', 'username', 'fullname',
                  'nickname', 'birthday', 'gender')


# View user profile

@apply_schema('ViewUserProfileSchema')
class ViewUserProfile(BaseModel):
    columns = [Column('user_id', Integer, primary_key=True)]
    # child = orm.relationship('JsonUserContact', back_populates='contacts')

    __table__ = getTable('v_user_profile', columns)


class ViewUserProfileSchema(BaseSchema):
    class Meta:
        model = ViewUserProfile
        fields = ['user_id', 'status', 'username',
                  'fullname', 'nickname', 'birthday', 'gender',
                  'createdon', 'updatedon', 'brief_description',
                  'education', 'position', 'company_name']


# View user contact

@apply_schema('ViewUserContactSchema')
class ViewUserContact(BaseModel):
    columns = (
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey('v_user_profile.user_id')),
    )

    __table__ = getTable('v_user_contact', columns)


class ViewUserContactSchema(BaseSchema):
    class Meta:
        model = ViewUserContact
        fields = ['id', 'user_id', 'contact_type', 'contact_name', 'ord_num']


# ---------------
# ---- User Info Relaction Ship
# ---------------

@apply_schema('UserInfoAllSchema')
class UserInfoAll(ViewUserProfile):
    __table__ = ViewUserProfile.__table__

    rel_child = relationship(
        "JsonUserContact", backref=backref("user_info"))


@apply_schema('JsonUserContactSchema')
class JsonUserContact(BaseModel):
    columns = [
        Column('user_id', Integer,  ForeignKey(
            'v_user_profile.user_id'), primary_key=True),
    ]
    __table__ = getTable('json_user_contact', columns)

    rel_parent = relationship(
        "UserInfoAll", backref=backref("contacts", uselist=False))


class UserInfoAllSchema(BaseSchema):
    contacts = ma.Nested('JsonUserContactSchema',
                         exclude=('user_id', 'user_info'))

    class Meta:
        model = UserInfoAll
        fields = ViewUserProfileSchema.merge_fields(['contacts'])


class JsonUserContactSchema(BaseSchema):
    user_info = ma.Nested('UserInfoAllSchema',
                          only=('username',))

    class Meta:
        model = JsonUserContact
        fields = ['user_id', 'json_contacts', 'user_info']
