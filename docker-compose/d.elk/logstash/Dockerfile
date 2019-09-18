ARG ELK_VERSION
ARG ES_HOST
ARG FILEBEAT_HOST

FROM logstash:${ELK_VERSION}

ENV ES_HOST ${ES_HOST:-elasticsearch}
ENV FILEBEAT_HOST ${FILEBEAT_HOST:-filebeat}

ADD logstash.yml /usr/share/logstash/config
ADD pipeline /usr/share/logstash