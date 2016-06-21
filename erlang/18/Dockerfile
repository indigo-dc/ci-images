FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update
RUN apt-get -y install git make curl jq

# erlang v18
COPY build-erlang.sh /tmp/build-erlang.sh
RUN bash -x /tmp/build-erlang.sh 18.3

# elvis
RUN git clone https://github.com/inaka/elvis /tmp/elvis
WORKDIR /tmp/elvis
RUN make && make install
RUN wget https://raw.githubusercontent.com/inaka/erlang_guidelines/master/elvis.config -O /etc/elvis.config

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
RUN make deps
RUN make compile
RUN cp covertool /usr/bin/covertool

WORKDIR /root
