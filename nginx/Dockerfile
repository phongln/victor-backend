FROM nginx:alpine

ARG CT_VERSION
ARG CT_FILENAME
ARG CT_URL

ENV CT_VERSION ${CT_VERSION:-0.22.0}
ENV CT_FILENAME ${CT_FILENAME:-consul-template_0.22.0_linux_amd64.zip}
ENV CT_URL ${CT_URL:-https://releases.hashicorp.com/consul-template}

RUN apk add --no-cache bash curl runit

RUN curl -O $CT_URL/$CT_VERSION/$CT_FILENAME

RUN unzip $CT_FILENAME -d /usr/local/bin

ADD service.nginx.sh /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run


EXPOSE 80 443