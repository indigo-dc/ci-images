FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update
RUN apt-get -y install git software-properties-common

RUN apt-add-repository -y ppa:brightbox/ruby-ng
RUN apt-get update
RUN apt-get install -y ruby2.2 ruby2.2-dev make zlib1g-dev

RUN gem install rubocop 

RUN gem install json -v '1.8.3'
RUN gem install nokogiri -v '1.6.7.2'
RUN gem install bundle

RUN apt-get -y install g++
