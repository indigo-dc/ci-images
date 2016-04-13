FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update
RUN apt-get -y install git make

# erlang v17 is required for elvis
COPY build-erlang.sh /tmp/build-erlang.sh
RUN bash -x /tmp/build-erlang.sh 18.3

RUN git clone https://github.com/inaka/elvis /tmp/elvis
WORKDIR /tmp/elvis
RUN make && make install

RUN wget https://raw.githubusercontent.com/inaka/erlang_guidelines/master/elvis.config -O /etc/elvis.config 
