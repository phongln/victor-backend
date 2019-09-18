ARG ELK_VERSION

FROM store/elastic/filebeat:${ELK_VERSION}

ADD filebeat.yml /usr/share/filebeat/filebeat.yml

USER root

RUN mkdir /usr/share/filebeat/dockerlogs
RUN chown -R root /usr/share/filebeat/
RUN chmod -R go-w /usr/share/filebeat/