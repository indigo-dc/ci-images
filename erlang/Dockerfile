FROM indigodatacloud/ci-images:base
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y wget \
                                                  git \
                                                  make \
						  erlang \
						  rebar \
						  golang \
                                                  gcc

# covertool
RUN git clone https://github.com/idubrov/covertool.git /tmp/covertool
WORKDIR /tmp/covertool
RUN make compile
RUN cp covertool /usr/bin/covertool

WORKDIR /root

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
