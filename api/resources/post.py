from flask_restful import Resource


class PostResource(Resource):
    def get(self):
        return {'post': 'this is a post'}
