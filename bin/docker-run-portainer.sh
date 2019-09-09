docker volume create portainer_data
docker run -d --name portainer \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    -p 9000:9000 \
    portainer/portainer