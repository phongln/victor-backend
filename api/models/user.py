from sqlalchemy import orm, Table, Column, Integer, ForeignKey

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
    user_info = orm.relationship('ViewUserProfile', backref='contacts')

    __table__ = getTable('v_user_contact', columns)


class ViewUserContactSchema(BaseSchema):
    class Meta:
        model = ViewUserContact
        fields = ['id', 'user_id', 'contact_type', 'contact_name', 'ord_num']


# Get all info

@apply_schema('UserInfoAllSchema')
class UserInfoAll(ViewUserProfile):
    __table__ = ViewUserProfile.__table__


class UserInfoAllSchema(BaseSchema):

    class Meta:
        model = UserInfoAll
        fields = ViewUserProfileSchema.merge_fields(['contacts'])
    contacts = ma.Nested(ViewUserContactSchema,
                         many=True, exclude=('user_id',))
