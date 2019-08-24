from sqlalchemy import orm, Table, Column, Integer, ForeignKey
from marshmallow import fields as ma_fields

from api.database import db, ma


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'autoload': True,
                      'autoload_with': db.engine, 'extend_existing': True}

    @classmethod
    def get_ma_schema(cls):
        pass

    @classmethod
    def jsonify(cls, respone, many=False):
        ma_schema = cls.get_ma_schema()
        return ma_schema(many=many).jsonify(respone)

    def json(self, many=False):
        ma_class = self.__class__ if not many else self[0].__class__
        ma_schema = ma_class.get_ma_schema()
        return ma_schema().jsonify(self, many=many)


class UserProfile(BaseModel):
    __tablename__ = 'user_profile'

    def get_ma_schema():
        return UserProfileSchema


class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'status', 'username', 'fullname',
                  'nickname', 'birthday', 'gender')


# View user profile


class ViewUserProfile(BaseModel):
    __table__ = Table('v_user_profile', db.metadata,
                      Column('user_id', Integer, primary_key=True),
                      **BaseModel.__table_args__)

    def get_ma_schema():
        return ViewUserProfileSchema


class ViewUserProfileSchema(ma.Schema):
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
    user_info = orm.relationship('ViewUserProfile', backref='contacts')

    __table__ = Table('v_user_contact', db.metadata,
                      *columns,
                      **BaseModel.__table_args__)

    def get_ma_schema():
        return ViewUserContactSchema


class ViewUserContactSchema(ma.Schema):
    class Meta:
        model = ViewUserContact
        fields = ['id', 'user_id', 'contact_type', 'contact_name', 'ord_num']

# Get all info


class UserInfoAll(ViewUserProfile):
    __table__ = ViewUserProfile.__table__

    def get_ma_schema():
        return UserInfoAllSchema


class UserInfoAllSchema(ma.Schema):

    class Meta:
        model = UserInfoAll
        fields = ViewUserProfileSchema.Meta.fields + ['contacts']
    contacts = ma.Nested(ViewUserContactSchema,
                         many=True, exclude=('user_id',))
