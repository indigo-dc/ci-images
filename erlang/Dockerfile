FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update
RUN apt-get -y install git make

# erlang v17 is required for elvis
COPY build-erlang-17.0.sh /tmp/build-erlang-17.0.sh
RUN bash -x /tmp/build-erlang-17.0.sh

RUN git clone https://github.com/inaka/elvis /tmp/elvis
WORKDIR /tmp/elvis
RUN make && make install

RUN wget https://raw.githubusercontent.com/inaka/erlang_guidelines/master/elvis.config -O /etc/elvis.config 
