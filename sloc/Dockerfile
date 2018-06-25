FROM indigodatacloud/ci-images:base
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y wget \
                                                  git \
                                                  make \
                                                  gcc \
                                                  flex \
						  libc6-dev

WORKDIR /tmp
RUN wget http://www.dwheeler.com/sloccount/sloccount-2.26.tar.gz
RUN gunzip -c sloccount*.tar.gz | tar xvf -
WORKDIR /tmp/sloccount-2.26
RUN sed -i 's/^CC=.*/CC=gcc -Wall -c/g' makefile
RUN make
RUN make install

RUN apt-get -y install cloc
