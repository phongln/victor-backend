import docker
import json
import sys
import os
import re

client = docker.from_env()

__config_path = sys.argv[1]
__config_filename = os.path.basename(__config_path)

client_create = None
if __config_filename == 'networks.json':
    client_create = client.networks.create
elif __config_filename == 'volumes.join':
    client_create = client.volumes.create 

with open(__config_path) as _file:
    data = json.load(_file)
    for _config in data:
        try:
            client_create(**_config)  
        except docker.errors.APIError as e:
            pass
