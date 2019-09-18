ARG ELK_VERSION
ARG ES_HOST

FROM kibana:${ELK_VERSION}

ENV ES_HOST ${ES_HOST:-elasticsearch}

ADD kibana.yml /usr/share/kibana/config