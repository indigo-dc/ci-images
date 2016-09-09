FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get clean
RUN apt-get update
RUN apt-get -y install openjdk-7-jdk
RUN apt-get -y install git curl gradle
RUN curl -sL https://github.com/jpm4j/jpm4j.installers/raw/master/dist/biz.aQute.jpm.run.jar > jpm4j.jar
RUN java -jar jpm4j.jar -g init
RUN jpm install com.liferay.blade.cli
