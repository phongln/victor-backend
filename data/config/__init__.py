import os
import json
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')

env_path = os.path.join(APP_ROOT, '.flaskenv')
load_dotenv(dotenv_path=env_path)


REDDIT_URL = os.getenv('REDDIT_URL')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_SERCRET = os.getenv('REDDIT_SERCRET')


def get_reddit_config() -> object:
    from data.lib import get_reddit_token

    reddit_token_path = os.path.join(
        APP_ROOT, 'credentials', 'reddit_token.json')
    if not os.path.exists(reddit_token_path):
        with open(reddit_token_path, 'w') as _file:
            _token = get_reddit_token()
            _file.write(json.dumps(_token))
    with open(reddit_token_path) as _file:
        return json.load(_file)


reddit_config = get_reddit_config()
