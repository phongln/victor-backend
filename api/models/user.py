from api.database import db, ma


class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    __table_args__ = {'autoload': True, 'autoload_with': db.engine}

    @staticmethod
    def jsonify(respone):
        return user_profiles_schema.jsonify(respone)


class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'status', 'username', 'fullname')


user_profile_schema = UserProfileSchema()
user_profiles_schema = UserProfileSchema(many=True)
