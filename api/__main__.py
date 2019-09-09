from api import app


if __name__ == '__main__':
    from api.config import API_HOST, API_PORT
    app.run(host=API_HOST, port=API_PORT, threaded=True)
