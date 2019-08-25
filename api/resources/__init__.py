from flask_restful import Api

api = Api()
LIMIT_ROWS = 10


def init_blueprint(app):
    from api.resources import post, user, meta
    app.register_blueprint(user.user_bp)
    app.register_blueprint(post.post_bp)
    app.register_blueprint(meta.meta_bp)
