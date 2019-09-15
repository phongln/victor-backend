#!/bin/sh

exec consul-template \
    -consul-addr $CONSUL_HOST:8500 \
    -template "/etc/consul-templates/nginx.default.conf:/etc/nginx/conf.d/default.conf:nginx -s reload" \
    -template "/etc/consul-templates/nginx.api.conf:/etc/nginx/conf.d/api.conf:nginx -s reload" \
    -template "/etc/consul-templates/nginx.index.html:/usr/share/nginx/html/index.html"
