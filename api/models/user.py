from sqlalchemy import orm, Table

from api.database import db, ma


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'autoload': True, 'autoload_with': db.engine}

    @classmethod
    def get_ma_schema(cls):
        pass

    @classmethod
    def jsonify(cls, respone, many=False):
        ma_schema = cls.get_ma_schema()
        return ma_schema(many=many).jsonify(respone)


class UserProfile(BaseModel):
    __tablename__ = 'user_profile'

    def get_ma_schema():
        return UserProfileSchema


class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'status', 'username', 'fullname',
                  'nickname', 'birthday', 'gender')


class ViewUserProfile(BaseModel):
    __table__ = Table('v_user_profile', db.metadata,
                      db.Column('user_id', db.Integer, primary_key=True),
                      autoload=True, autoload_with=db.engine, extend_existing=True)

    def get_ma_schema():
        return ViewUserProfileSchema


class ViewUserProfileSchema(ma.Schema):
    class Meta:
        model = ViewUserProfile
        fields = ('user_id', 'status', 'username',
                  'fullname', 'nickname', 'birthday', 'gender',
                  'createdon', 'updatedon', 'brief_description',
                  'education', 'position', 'company_name', 'address1',
                  'address2', 'phone1', 'phone2', 'mail', 'mail2')
