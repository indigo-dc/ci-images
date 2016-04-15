FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update
RUN apt-get -y install git maven checkstyle 

RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get -y install openjdk-8-jdk openjdk-8-jre

RUN update-alternatives --config java  --set 
RUN update-alternatives --config javac --set
