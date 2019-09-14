#!/bin/python
import os
import sys

__path = os.path.realpath(sys.argv[1])

print(os.path.join(__path, *sys.argv[2:]))