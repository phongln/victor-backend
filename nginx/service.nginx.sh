#!/bin/sh

/usr/sbin/nginx -t \
&& exec /usr/sbin/nginx -g "daemon off;"