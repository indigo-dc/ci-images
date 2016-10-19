FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update
RUN apt-get -y install git wget

WORKDIR /tmp
RUN wget https://storage.googleapis.com/golang/go1.5.linux-amd64.tar.gz
RUN tar -C /usr/local -xvf go1.5.linux-amd64.tar.gz
RUN echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.bashrc
