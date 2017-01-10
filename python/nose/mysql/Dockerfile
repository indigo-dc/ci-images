FROM indigodatacloud/ci-images:python_nose
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get clean
RUN apt-get update

RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y install mysql-server openssh-server supervisor
RUN pip install mock

RUN mkdir -p /var/run/sshd

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22 3306
CMD ["/usr/bin/supervisord"]
