FROM nginx:alpine

RUN apk add --no-cache bash curl runit

ENV CT_URL https://releases.hashicorp.com/consul-template/0.19.5/consul-template_0.19.5_linux_amd64.zip
RUN curl -O $CT_URL
RUN unzip consul-template_0.19.5_linux_amd64.zip -d /usr/local/bin

ADD service.nginx.sh /etc/service/nginx/run
ADD service.consul-template.sh /etc/service/consul-template/run
RUN chmod +x /etc/service/nginx/run
RUN chmod +x /etc/service/consul-template/run

RUN rm -v /etc/nginx/conf.d/*
ADD nginx.default.conf /etc/consul-templates/nginx.default.conf
ADD nginx.index.html /etc/consul-templates/nginx.index.html

EXPOSE 80 443


CMD ["/sbin/runsvdir", "/etc/service"]
