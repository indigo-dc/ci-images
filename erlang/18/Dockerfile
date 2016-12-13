FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update
# git for cloning the sources
# make for building
# curl and jq are needed by the tts-client
# wget is used to fetch the erlang sources
# the TTS plugins are written in python
RUN apt-get -y install git make curl jq wget python

# erlang v18
COPY build-erlang.sh /tmp/build-erlang.sh
RUN bash -x /tmp/build-erlang.sh 18.3

# rebar
RUN git clone https://github.com/rebar/rebar.git /tmp/rebar
WORKDIR /tmp/rebar
RUN ./bootstrap
RUN cp rebar /usr/bin/rebar

# covertool
RUN git clone https://github.com/idubrov/covertool.git /tmp/covertool
WORKDIR /tmp/covertool
# FIXME(orviz) `make` should do it but fails in unit testing
#RUN make
#RUN make deps
RUN make compile
RUN cp covertool /usr/bin/covertool

## GOlang for TTS
RUN apt-get -y install wget
WORKDIR /tmp
RUN wget https://storage.googleapis.com/golang/go1.5.linux-amd64.tar.gz
RUN tar -C /usr/local -xvf go1.5.linux-amd64.tar.gz
RUN echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.bashrc
RUN echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile

WORKDIR /root
