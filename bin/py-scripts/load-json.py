#!/usr/local/bin/python

import json
import sys

with open(sys.argv[1]) as file:
    data = json.load(file)

    for item in data:
        print(json.dumps(item))