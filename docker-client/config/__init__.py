import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

NETWORKS_JSON = os.path.join(BASE_DIR, 'networks.json')
VOLUMES_JSON = os.path.join(BASE_DIR, 'volumes.json') 
IMAGES_JSON = os.path.join(BASE_DIR, 'images.json') 

def load_config(path):
    with open(path) as _file:
        return json.load(_file)

class Config():
    config_networks =load_config(NETWORKS_JSON)
    config_volumes = load_config(VOLUMES_JSON)
    config_images = load_config(IMAGES_JSON)

def get_config():
    return Config()