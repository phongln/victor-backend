FROM backend-api:latest

USER root

WORKDIR /home
COPY . /home/api
RUN mv ./api/api.env ./api/.env
RUN cp ./api/docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "f", "http:/localhost:/test" ]

EXPOSE 5000