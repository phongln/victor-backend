import os
import click
import docker
from . import config, ROOT_DIR

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

client = docker.from_env()


def __create_resource(resource_type, config_value):
    if resource_type == 'networks':
        client.networks.create(**config_value)
    elif resource_type == 'volumes':
        client.volumes.create(**config_value)
    elif resource_type == 'images':
        print('Initializing images {}'.format(config_value['tag']))
        config_value["path"] = os.path.join(ROOT_DIR, config_value["path"])
        client.images.build(rm=True, **config_value)
        print('Created images {}'.format(config_value['tag']))


def __init_resource(resource_type, configs):
    for config_value in configs:
        try:
            __create_resource(resource_type, config_value)
        except docker.errors.APIError as e:
            pass
        except docker.errors.BuildError as e:
            pass


@click.command()
@click.option("--resource_type", help='Resource type in ["volumes", "images", "networks"]')
def init_resource(resource_type):
    if resource_type is None:
        pass
    elif resource_type == 'all':
        __init_resource('networks', config.config_networks)
        __init_resource('volumes', config.config_volumes)
        __init_resource('images', config.config_images)
    elif resource_type in ('volumes', 'networks', 'images'):
        __init_resource(resource_type, config.config_volumes)
    else:
        print("Invalid docker resource type. Only support: all, volumes, images, networks")
