FROM indigodatacloud/ci-images:python_nose
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get clean
RUN apt-get update

RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y install mysql-server
RUN pip install mock
