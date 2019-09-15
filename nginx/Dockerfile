FROM nginx:alpine

RUN apk add --no-cache bash curl runit

ENV CONSUL_HOST consul
ENV CT_VERSION '0.22.0'
ENV CT_FILENAME 'consul-template_0.22.0_linux_amd64.zip' 
ENV CT_URL https://releases.hashicorp.com/consul-template/$CT_VERSION/$CT_FILENAME

RUN curl -O $CT_URL
RUN unzip $CT_FILENAME -d /usr/local/bin

ADD service.nginx.sh /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run


EXPOSE 80 443