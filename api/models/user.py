from api.database import db


class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column('user_id', db.Integer, primary_key=True)
