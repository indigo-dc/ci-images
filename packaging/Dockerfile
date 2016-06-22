FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get clean
RUN apt-get update
RUN apt-get -y install git wget make gcc flex

WORKDIR /tmp
RUN wget http://www.dwheeler.com/sloccount/sloccount-2.26.tar.gz
RUN gunzip -c sloccount*.tar.gz | tar xvf -
WORKDIR /tmp/sloccount-2.26
RUN sed -i 's/^CC=.*/CC=gcc -Wall -c/g' makefile
RUN make
RUN make install
