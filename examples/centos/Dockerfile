FROM centos
RUN yum update && yum install -y epel-release
RUN yum install -y nginx net-tools

ENTRYPOINT /usr/sbin/init

EXPOSE 80