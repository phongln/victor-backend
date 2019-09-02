from api import app


if __name__ == '__main__':
    from api.config import BLOG_HOST, BLOG_PORT
    app.run(host=BLOG_HOST, port=BLOG_PORT, threaded=True)
