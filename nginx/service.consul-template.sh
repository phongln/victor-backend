#!/bin/sh

exec consul-template \
    -consul-addr consul:8500 \
    -template "/etc/consul-templates/nginx.default.conf:/etc/nginx/conf.d/default.conf:service nginx reload" \
    -template "/etc/consul-templates/nginx.index.html:/usr/share/nginx/html/index.html"
