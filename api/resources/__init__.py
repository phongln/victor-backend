from flask_restful import Api

api = Api()
LIMIT_ROWS = 10


def init_blueprint(app):
    from api.resources import post, user, meta, test
    app.register_blueprint(user.user_bp)
    app.register_blueprint(post.post_bp)
    app.register_blueprint(meta.meta_bp)
    app.register_blueprint(test.test_bp)


def init_resources(app):
    api.init_app(app)
    init_blueprint(app)
