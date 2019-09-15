FROM victor-nginx

ADD service.consul-template.sh /etc/service/consul-template/run
RUN chmod +x /etc/service/consul-template/run

RUN rm -v /etc/nginx/conf.d/*
ADD nginx.default.conf /etc/consul-templates/nginx.default.conf
ADD nginx.api.conf /etc/consul-templates/nginx.api.conf
ADD nginx.index.html /etc/consul-templates/nginx.index.html

CMD ["/sbin/runsvdir", "/etc/service"]
