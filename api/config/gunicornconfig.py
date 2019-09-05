import os
import multiprocessing

# The maximum concurrent requests are workers * threads
# I/O bound or CPU bound => worker_class
bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count()*2 + 1
threads = 2
timeout = 180
keepalive = 26*3600
capture_output = True
worker_class = 'gevent'