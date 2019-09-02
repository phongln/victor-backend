from marshmallow.fields import Nested

from .base import BaseSchema
from api.models.user import *


__all__ = ['ViewUserProfileSchema', 'ViewUserContactSchema',
           'UserInfoAllSchema', 'JsonUserContactSchema']


class ViewUserProfileSchema(BaseSchema):
    class Meta:
        model = ViewUserProfile
        fields = ['user_id', 'status', 'username',
                  'fullname', 'nickname', 'birthday', 'gender',
                  'createdon', 'updatedon', 'brief_description',
                  'education', 'position', 'company_name']


class ViewUserContactSchema(BaseSchema):
    class Meta:
        model = ViewUserContact
        fields = ['id', 'user_id', 'contact_type', 'contact_name', 'ord_num']


class UserInfoAllSchema(BaseSchema):
    contacts = Nested('JsonUserContactSchema',
                      exclude=('user_id', 'user_info'))

    class Meta:
        model = UserInfoAll
        fields = ViewUserProfileSchema.merge_fields(['contacts'])


class JsonUserContactSchema(BaseSchema):
    user_info = Nested('UserInfoAllSchema',
                       only=('username',))

    class Meta:
        model = JsonUserContact
        fields = ['user_id', 'json_contacts', 'user_info']
