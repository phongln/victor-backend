from flask_restful import Api

from .user import UserResource
from .post import PostResource

api = Api()
api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(PostResource, '/post')
