import os
import docker
from .config import get_config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

config = get_config()
client = docker.from_env()


def create_resource(resource_type, config_value):
    if resource_type == 'networks':
        client.networks.create(**config_value)
    elif resource_type == 'volumes':
        client.volumes.create(**config_value)
    elif resource_type == 'images':
        print('Initializing images {}'.format(config_value['tag']))
        config_value["path"] = os.path.join(ROOT_DIR, config_value["path"])
        client.images.build(rm=True, **config_value)
        print('Created images {}'.format(config_value['tag']))


def init_resource(resource_type, configs):
    for config_value in configs:
        try:
            create_resource(resource_type, config_value)
        except docker.errors.APIError as e:
            pass
        except docker.errors.BuildError as e:
            pass

def init_all_resources():
    init_resource('networks', config.config_networks)
    init_resource('volumes', config.config_volumes)
    init_resource('images', config.config_images)